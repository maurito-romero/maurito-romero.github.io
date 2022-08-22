from netmiko import ConnectHandler
 ## Open a txt file with devices ip address
with open('C:\Configs\devices.txt') as routers:
    ## File with cisco configurations
    cfg_file = "C:\Configs\TACAS.txt"
    for IP in routers:
        Router = {
            'device_type': 'cisco_ios',
            'ip': IP,
            'username': 'root',
            'password': 'toor'
        }
 
        net_connect = ConnectHandler(**Router)
 
        print ('Connecting to ' + IP)
        print('-'*79)
        output = net_connect.send_config_from_file(cfg_file)
        print(output)
        print()
        print('-'*79)
 
# Finally close the connection
net_connect.disconnect()
