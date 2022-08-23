# maurito-romero.github.io
Personal Projects
## General Info
This script uses Netmiko for connecting to cisco devices using SSH cointained in a list of IP's in a deviec.txt file.
Then sends a list of commands to configure AAA with TACACS+ in another cnf.txt file
## Setup
Make a list of IP's Routers/Switches in a device.txt file
```
192.168.1.1
192.168.1.2
192.168.1.3
```
Then make a cnfg.txt containing a list of commands for AAA TACACS+ Configuration.
```
aaa new-model

tacacs server ISE-1
 address ipv4 172.16.1.1
 key ********
exit

tacacs server ISE-2
 address ipv4 172.22.1.10
 key ********
exit

aaa group server tacacs+ TACACS-ISE
  server name ISE-1
  server name ISE-2
  exit

aaa authentication login default group TACACS-ISE local
aaa authentication enable default group TACACS-ISE enable
aaa authorization exec default group TACACS-ISE local
aaa accounting exec default start-stop group TACACS-ISE
aaa accounting commands 15 default start-stop group TACACS-ISE
end
wr
```
Put those files in C:\Configs Directory
