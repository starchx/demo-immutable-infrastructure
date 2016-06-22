# web server role - instance starts up
class role::startup::webserver (
  $environment = 'stg',
) {

  file { '/etc/httpd/conf.d/server-environment.conf':
    ensure  => present,
    owner   => 'root',
    group   => 'root',
    mode    => '0644',
    content => template('role/server-environment.conf.erb'),
  }

}
