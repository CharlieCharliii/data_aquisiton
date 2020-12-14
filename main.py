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
        print("Could not connect to " + ipAddress, file=sys.stderr) # Why stderr? see below
        exit(-1)

    # go over data in valueDescriptors one by one
    for descriptor in valueDescriptors:
    # basing on Type get either a coil or input value specified by register
        if descriptor["type"] == "Input Register":
            # Get input value and handle errors
            value = 21.37 # placeholder
            print(descriptor["Descriptor"] + ": " + str(value) + descriptor["Unit"])
        elif descriptor["type"] == "Discrete Input":
            # Get coil value and handle errors
            pass
        else:
            # Print human readable errors to stderr so that the output is not cluttered if the data is to be parsed
            print("Unknown value type: " + descriptor["type"], file=sys.stderr)
