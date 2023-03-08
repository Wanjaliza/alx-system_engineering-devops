# Changing OS configuration to enable login with holberton

# Increasing hard file limit 
exec { 'increasing-hard-holberton-user':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf'
  path    => '/usr/local/bin/:/bin/'
}

# Increasing soft file limit
exec { 'increasing-soft-holberton-user':
  command => 'sed -i "/holberton soft/s/4/50000" /etc/security/limits.conf'
  path    => '/usr/local/bin/:/bin/'
  }
