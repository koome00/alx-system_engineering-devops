Command line for the win
For this task, I followed these steps to upload my png files to my sandbox through sftp.
1.	To begin with, I opened my terminal and navigated to where the png files were located using this command:
cd C:\Users\user\Pictures\Screenshots
2.	I then started the connection to my sandbox through sftp using this command where the username, hostname, and password were required:
sftp c17514720c38@c17514720c38.c5f1be15.alx-cod.online
3.	Upon successfully connecting to the remote sandbox, I navigated to the directory where I wanted to upload the files using this command:
cd /root/alx-system_engineering-devops/command_line_for_the_win/
4.	Using this command, I uploaded all the files in the screenshot folder:
put *
5.	Using this command, I exited from the sftp interactive mode:
exit 


