#!/usr/bin/env bash

sudo -E sh -c "rm -rf /opt/puppet"
sudo -E sh -c "mkdir -p /opt/puppet"
sudo -E sh -c "chown -R ec2-user:ec2-user /opt/puppet"
