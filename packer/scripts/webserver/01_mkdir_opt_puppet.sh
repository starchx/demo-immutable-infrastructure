#!/usr/bin/env bash

sudo -E sh -c "rm -rf /opt/puppet"
sudo -E sh -c "mkdir -p /opt/puppet"
sudo -E sh -c "chown -R ubuntu:ubuntu /opt/puppet"

sudo -E sh -c "rm -rf /opt/application"
sudo -E sh -c "mkdir -p /opt/application"
sudo -E sh -c "chown -R ubuntu:ubuntu /opt/application"