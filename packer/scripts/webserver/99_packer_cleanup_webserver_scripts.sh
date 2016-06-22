#!/usr/bin/env bash

sudo -E sh -c 'cat << EOF >> /etc/rc.local

for i in /home/ubuntu/*webserver*; do
  [ -f "\$i" ] && rm -f \$i || rm -rf \$i
done
EOF'
