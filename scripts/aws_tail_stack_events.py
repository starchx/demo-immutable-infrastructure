#!/usr/bin/env python
from os import getenv
from time import sleep
import datetime
import boto
import boto.cloudformation
import sys
import argparse
import socket

BORDER = 105
HEADER = False
OLD_EVENTS = {}
UTC_NOW = datetime.datetime.utcnow()

def get_args():
  parser = argparse.ArgumentParser()
  parser.add_argument('--region', action='store', required=False, metavar='aws_region', dest='region', default='ap-southeast-2', help='Amazon AWS region name')
  parser.add_argument('stack_name', action='store', help='AWS CloudFormation stack name')
  return parser.parse_args()

def print_header():
  sys.stdout.write("-" * BORDER + "\n")
  sys.stdout.write("|\t\t%-22s|\t\t%-12s|\t\t\t%-24s|\n" %("RESOURCE", "STATUS", "TYPE"))
  sys.stdout.write("-" * BORDER + "\n")
  sys.stdout.flush()

def print_footer():
  sys.stdout.write("-" * BORDER + "\n")
  sys.stdout.flush()

def print_stack_status(status):
  sys.stdout.write("[%s] Stack Status: %s\n" %(datetime.datetime.now(), status))
  sys.stdout.flush()

def print_stack_events(stack_name, region):
  conn = get_ec2_cfn_connection(region)
  new_events = {}
  try:
    events = [i for i in conn.describe_stack_events(stack_name)]
  except boto.exception.BotoServerError as e:
    sys.stderr.write("%s(%s): %s!\n" %(e.error_code, e.status, e.message))
    sys.stderr.flush()
  except socket.gaierror as ge:
    sys.stderr.write("%s(%s): %s!\n" %(e.error_code, e.status, e.message))
    sys.stderr.flush()
  else:
    for event in events:
      if event.timestamp > UTC_NOW:
        resource = str(event).split()[2]
        status = str(event).split()[3]
        type = str(event).split()[1]
        if resource != stack_name and not new_events.has_key(resource):
            new_events[resource] = (status, type)
            if not OLD_EVENTS.has_key(resource):
              OLD_EVENTS[resource] = new_events[resource]
              sys.stdout.write("|\t%-30s|\t%-20s|\t%-40s|\n" %(resource, status, type))
              sys.stdout.flush()
            else:
              if OLD_EVENTS[resource][0] != new_events[resource][0]:
                OLD_EVENTS[resource] = new_events[resource]
                sys.stdout.write("|\t%-30s|\t%-20s|\t%-40s|\n" %(resource, status, type))
                sys.stdout.flush()
  finally:
    conn.close()

def get_ec2_cfn_connection(aws_region):
  return boto.cloudformation.connect_to_region(aws_region)
   
def get_stack_events(stack_name, region):
  conn = get_ec2_cfn_connection(region)
  global HEADER
  while True:
    try:
      status = [i.stack_status for i in conn.describe_stacks(stack_name)]
    except boto.exception.BotoServerError as e:
      if e.error_code == "Throttling" and e.message == "Rate exceeded":
        sleep(10)
        continue
      if "%s does not exist" %stack_name in e.message:
        if stack_name in [i.stack_name for i in conn.list_stacks('DELETE_COMPLETE')]:
          print_stack_events(stack_name, region)
          if HEADER:
            print_footer()
          sys.stderr.write("[%s] Stack Status: DELETE_COMPLETE\n" %datetime.datetime.now())
          sys.stderr.flush()
          conn.close()
          sys.exit(0)
      sys.stderr.write("%s(%s): %s!\n" %(e.error_code, e.status, e.message))
      sys.stderr.flush()
      conn.close()
      sys.exit(1)
    else:
      if any(status[0] in s for s in ['DELETE_IN_PROGRESS', 'CREATE_IN_PROGRESS', 'UPDATE_IN_PROGRESS']):
        if not HEADER:
          print_header()
          HEADER = True
        print_stack_events(stack_name, region)
        sleep(10)
        continue
      if 'CREATE_COMPLETE' in status or 'UPDATE_COMPLETE' in status:
        if HEADER:
          print_footer()
        print_stack_events(stack_name, region)
        print_stack_status(status[0])
        outputs = (i.outputs for i in conn.describe_stacks(stack_name))
        print("\nOutputs:")
        print("-"*10)
        for i in outputs:
          for output in i:
            print("%s = %s" %(output.key, output.value))
        conn.close()
        sys.exit(0)
      if any(status[0] in s for s in ['DELETE_FAILED', 'CREATE_FAILED', 'UPDATE_FAILED']):
        if HEADER:
          print_footer()
        print_stack_events(stack_name, region)
        print_stack_status(status[0])
        reason = [i.stack_status_reason for i in conn.describe_stacks(stack_name)]
        sys.stderr.write("Reason: %s\n" %reason[0])
        sys.stderr.flush()
        conn.close()
        sys.exit(1)

def main():
  args = get_args()
  sys.stdout.write("stack_name = %s\n" %args.stack_name)
  sys.stdout.write("region = %s\n" %args.region)
  sys.stdout.flush()
  try:
    get_stack_events(args.stack_name, args.region)
  except KeyboardInterrupt:
    sys.exit("User aborted script!")

if __name__ == '__main__':
  main()
