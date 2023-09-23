# create a manifest that kills a process using Puppet

exec { 'pkill -f killmenow':
  path => '/usr/bin/:usr/localbin/:bin/',
}
