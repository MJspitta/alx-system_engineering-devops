exec { 'kill_killmenow':
  command     => 'pkill killmenow',
  path        => '/bin:/usr/bin:/sbin:/usr/sbin',
  refreshonly => true,
}
