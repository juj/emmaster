# Configure this file and copy it to secret.py

# Passwords that the build slaves are configured to use to connect to the master
buildslave_passwords = {
#	"win-slave": "insert_password_here",
#	"ubuntu-slave": "insert_password_here",
#	"osx-slave": "insert_password_here",
}

# User credentials for accessing the web GUI administration
web_gui_usernames_and_password = {
# 	"username1": "insert_password_here",
# 	"username2": "insert_password_here"
}

# Password that the IRC reporter bot uses
# irc_reporter_password = 'insert_password_here'

# The following are not secret, but configuration specific so separated from the main script:

# The server port on the buildmaster that is listening for incoming build slaves to connect
buildmaster_slave_listen_port = 9989

# The public port that the buildmaster hosts its web GUI on
buildmaster_web_gui_port = 8112

# The publicly visible URL of the web GUI of the build master
buildmaster_public_url = 'http://point_this_to_the_public_url_of_the_build_master:port/'
