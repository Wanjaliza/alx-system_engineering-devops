# create a file in /tmp with different requirements
file { '/tmp/school':
    ensure  => 'file',
    owner   => 'www-data',
    mode    => '0744',
    group   => 'www-data',
    content => 'I love Puppet',
}
