#!/usr/bin/env bash

sudo -E sh -c "rm -rf /var/www/html/*"
sudo -E sh -c "cp -rf /opt/application/* /var/www/html"