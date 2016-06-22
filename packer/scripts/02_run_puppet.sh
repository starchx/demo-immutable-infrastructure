#!/usr/bin/env bash

# Set external facts
sudo -E sh -c "mkdir -p /etc/facter/facts.d"
sudo -E sh -c "echo '---' > /etc/facter/facts.d/role_stage.yaml"
sudo -E sh -c "echo 'role: ${ROLE}' >> /etc/facter/facts.d/role_stage.yaml"
sudo -E sh -c "echo 'stage: ${STAGE}' >> /etc/facter/facts.d/role_stage.yaml"

# Run Puppet
rvmsudo -E sh -c "cd /opt/puppet; puppet apply --ordering=manifest --hiera_config=hiera.yaml --modulepath=modules manifests/site.pp | tee /root/${ROLE}_${STAGE}.log"

# Check run status
if [ $(echo $?) -ne 0 ];
then
  echo 'Puppet run failed with errors!'
  exit 1
fi
