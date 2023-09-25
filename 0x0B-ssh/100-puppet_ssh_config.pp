# set up client SSH configuration file so that it can connect to a server
# without typing a password
include stdlib

file { 'NO password':
    ensure             => present,
    path               => '/etc/ssh/ssh_config',
    line               => '    PasswordAuthentication no',
    match              => '^PasswordAuthentication',
    append_on_no_match => true,
}

file { 'New private key holder':
    ensure             => present,
    path               => '/etc/ssh/ssh_config',
    line               => '    IdentityFile ~/.ssh/school',
    match              => '^IdentityFile',
    append_on_no_match => true,
}
