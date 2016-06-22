#!/usr/bin/env bash

sudo -E sh -c 'cat << EOF >> /etc/rc.local

for i in /home/ec2-user/*jenkins*; do
  [ -f "\$i" ] && rm -f \$i || rm -rf \$i
done
EOF'
