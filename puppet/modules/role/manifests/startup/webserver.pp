# web server role - instance starts up
class role::startup::webserver (
  $environment = 'stg',
) {

  file { '/etc/apache2/conf.d/server-environment.conf':
    ensure  => present,
    owner   => 'root',
    group   => 'root',
    mode    => '0644',
    content => template('role/server-environment.conf.erb'),
    notify  => Service['apache2'],
  }

  service { 'apache2':
    ensure => running,
  }

}
