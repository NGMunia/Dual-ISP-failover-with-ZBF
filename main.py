
'''
Configuring: NTP, SNMP, Syslog,
Verifying:   IPSLA, Tracking
'''
from Network.Devices import Routers
from netmiko import ConnectHandler
from rich import print as rp
from csv import writer
import json


'''
Verifying IPSLA on the Firewall
'''
router = Routers['ZBF']
c = ConnectHandler(**router)
c.enable()
result = c.send_command('show ip sla statistics').splitlines()
rp(json.dumps(result, indent=2))


'''
Backing up running-configuration
'''
filepath = input('filepath: ')
for devices in Routers.values():
    c = ConnectHandler(**devices)
    c.enable()
    hostname = c.send_command('show version',use_textfsm=True)[0]['hostname']

    output = c.send_command('show run')
    with open(f'{filepath}/{hostname}','w') as f:
        f.write(output)
        c.disconnect()
    rp(f'[cyan] Finished backing up running configs for {hostname}')


'''
Network Inventory
'''

filepath = input('Filepath: ')
with open(f'{filepath}/Data.csv','w') as f:
    write_data = writer(f)
    write_data.writerow(['Hostname','IP-Address','Software-Image','Version','Serial-No','Hardware'])
    for Devices in Routers.values():
        conn = ConnectHandler(**Devices)
        conn.enable()
        output = conn.send_command('show version',use_textfsm=True)[0]

        hostname = output['hostname']
        ip_addr  = Devices['ip']
        software = output['software_image']
        version  = output['version']
        serial   = output['serial']
        hardware = output['hardware']

        write_data.writerow([hostname,ip_addr,software,version,serial,hardware])
        conn.disconnect()
    
    rp(f"[cyan] Finished taking and Documenting Devices' information" )