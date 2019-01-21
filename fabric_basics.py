## EXECUTE REMOTE COMMAND IN HOST USING FABRIC LIBRARY (BASED ON INVOKE AND PARAMIKO)  
# DOC --> http://docs.fabfile.org/en/2.4/
# sudo pip3 install fabric2

from fabric2 import Connection

# HOST
host = 'HOST_IP'
username = 'HOST_USERNAME'
pass = 'HOST_SSH_PASS'	# NOT RECOMMENDED IN PRODUCTION, LOTS OF BETTER WAYS AT DOC

cmd = 'whoami'

c = Connection(
    host=host,
    user=username,
    connect_kwargs={
        "password":pass
    }
)

try:
    result = c.run(cmd).stdout
except Exception as e:
    print(e)
