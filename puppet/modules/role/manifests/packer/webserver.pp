# web server role - packer AMI bake
class role::packer::webserver (
) {

  package { 'ntp':
    ensure => present,
  }

  class { 'apache': }

  package { ['php5', 'libapache2-mod-php5', 'php5-mcrypt']:
    ensure => present,
  }

}
