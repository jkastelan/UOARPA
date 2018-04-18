from paramiko import SSHClient
from scp import SCPClient

ssh = SSHClient()
# Make sure you have run key-based auth setup
ssh.load_system_host_keys()

# Connect to the server
ssh.connect('<server ip>')
scp = SCPClient(ssh.get_transport())

# Transfer the file from src path to dest path
scp.put('</path/to/source/file>', '</path/to/destination/file>')

# Close the connection
scp.close()
