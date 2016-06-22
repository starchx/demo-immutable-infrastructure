# -*- mode: ruby -*-
# vi: set ft=ruby :

# solr node 01/02 needs to change '127.0.0.1 sbsstgsolr01' to '192.168.33.21 sbsstgsolr01' in /etc/hosts file.
nodes = {
  'demobox' => '192.168.33.11',
}

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). 
Vagrant.configure(2) do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  config.vm.box = "bento/centos-6.7"

  nodes.each do |node, nodeip|
    config.vm.define node do |nodeconfig|
      nodeconfig.vm.hostname = node
      nodeconfig.vm.network "private_network", ip: nodeip
      nodeconfig.vm.provider "virtualbox" do |vb|
        vb.memory = "1024"
      end
      nodeconfig.vm.synced_folder "./", "/opt/demo-immutable-infrastructure"
      nodeconfig.vm.provision "shell", inline: <<-SHELL
        sudo echo "# proxy environment vars" > /etc/profile.d/sbs_proxy.sh
        sudo echo "export http_proxy=http://10.21.160.105:8080" >> /etc/profile.d/sbs_proxy.sh
        sudo echo "export https_proxy=http://10.21.160.105:8080" >> /etc/profile.d/sbs_proxy.sh
        sudo echo "export HTTP_PROXY=http://10.21.160.105:8080" >> /etc/profile.d/sbs_proxy.sh
        sudo echo "export HTTPS_PROXY=http://10.21.160.105:8080" >> /etc/profile.d/sbs_proxy.sh
        sudo chmod 644 /etc/profile.d/sbs_proxy.sh

        echo "proxy=http://10.21.160.105:8080/" | sudo tee -a /etc/yum.conf
        echo "timeout=600" | sudo tee -a /etc/yum.conf
        rpm -ivh https://yum.puppetlabs.com/puppetlabs-release-el-6.noarch.rpm
        yum install -y puppet vim
      SHELL
    end
  end
end
