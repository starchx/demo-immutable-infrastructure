#!/usr/bin/env bash

# Run Puppet
sudo -E sh -c "cd /opt/puppet; puppet apply --ordering=manifest --hiera_config=hiera.yaml --modulepath=modules manifests/webserver_packer.pp | tee /root/packer.log"

# Check run status
if [ $(echo $?) -ne 0 ];
then
  echo 'Puppet run failed with errors!'
  exit 1
fi
