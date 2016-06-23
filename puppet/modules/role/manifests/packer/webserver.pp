# web server role - packer AMI bake
class role::packer::webserver (
) {

  package { 'ntp':
    ensure => present,
  }

  package { 'php5':
    ensure => present,
  }

  class { 'apache': }

}
