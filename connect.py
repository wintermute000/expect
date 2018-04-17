import netmiko
import argparse
import csv
from pprint import pprint
from netmiko import ConnectHandler


class connectdevice(object):
    def read_cli_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--list', action = 'store_true')
        parser.add_argument('--host', action = 'store')
        self.args = parser.parse_args()

    def __init__(self):
        self.read_cli_args()
        self.prompt()

    def prompt(self):
        net_connect = ConnectHandler(device_type='cisco_ios', ip='172.17.1.11', username='ansible', password='ansible')
        output = net_connect.send_command("show ip int brief")
        print(output)
        output = net_connect.send_command("show log")
        print(output)

if __name__ == '__main__':
    connectdevice()
