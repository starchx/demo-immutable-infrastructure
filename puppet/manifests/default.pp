node default {

  package { 'php':
    ensure => present,
  }

  class { 'apache': }

  

}
