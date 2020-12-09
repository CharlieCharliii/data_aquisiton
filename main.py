#!/usr/bin/python

from data import valueDescriptors

import sys

from pymodbus.client.sync import ModbusTcpClient as ModbusClient

if __name__ == '__main__':
    ipAddress = "127.0.0.1"
    if len(sys.argv) == 2:
        ipAddress = sys.argv[1]

    client = ModbusClient(ipAddress)
    if client.connect() == False:
        print("Could not connect to " + ipAddress)
        exit(-1)
