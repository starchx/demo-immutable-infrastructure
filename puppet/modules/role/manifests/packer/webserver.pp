# web server role - packer AMI bake
class role::packer::webserver (
) {

  package { 'ntp':
    ensure => present,
  }

  class { 'apache':
    mpm_module => 'prefork',
  }
  
  class { 'apache::mod::php': }

  #package { ['php5', 'libapache2-mod-php5', 'php5-mcrypt']:
  #  ensure => present,
  #}

}
