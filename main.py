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

    # go over data in valueDescriptors one by one
    # basing on Type get either a coil or input value specified by register
    #   handle errors nicely
    # print either in human readable or "csv" format
    # pretty much done
