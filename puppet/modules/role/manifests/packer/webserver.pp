# web server role - packer AMI bake
class role::packer::webserver (
) {

  package { 'php':
    ensure => present,
  }

  class { 'apache': }

}
