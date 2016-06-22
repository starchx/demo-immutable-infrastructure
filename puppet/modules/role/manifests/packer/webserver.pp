# web server role - packer AMI bake
class role::packer::webserver (
) {

  package { 'php5':
    ensure => present,
  }

  class { 'apache': }

}
