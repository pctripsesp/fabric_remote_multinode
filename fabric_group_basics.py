## FABRIC LOOKS AT CONFIG FILES AT THE BEGINNING:
# ~/.ssh/config
# /etc/ssh/ssh_config
# IF EMPTY, EXECUTES WITH OUR TERMINAL USERNAME 
# CREATE AND EDIT ~/.ssh/config, IN ORDER TO CONFIGURATE A USERNAME FOR EACH HOST IP, LIKE:
##
#Host <HOST_IP_1>
#    User <USERNAME_1>
#Host <HOST_IP_2>
#    User <USERNAME_2>

# SerialGroup EXECUTES ONE AFTER ANOTHER; ThreadingGroup DOES IT SIMULTANEOUSLY
from fabric2 import SerialGroup, ThreadingGroup

# HOST 1
host1 = '<HOST_IP_1>'

# HOST 2
host2 = '<HOST_IP_2>'

MASTERPASS = '<COMMON_SSH_PASS>'	## NEED TO BE THE SAME PASS FOR ALL HOSTS

cmd = 'whoami'

# CHANGE TreadingGroup FOR SerialGroup AS YOU NEED
myGroup = ThreadingGroup(	
    host1,
    host2,
    connect_kwargs={
        "password":MASTERPASS
    }
)

try:
    result = myGroup.run(cmd)

except Exception as e:
    print(e)
