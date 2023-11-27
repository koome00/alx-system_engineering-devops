# configure client to remove password authentification
file_line { 'passw_no_authentication':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}
file_line { 'passw_direction':
  path => '/etc/ssh/ssh_config',
  line => 'IdentifyFile ~/.ssh/school',
}
