#!/usr/bin/python

from data import valueDescriptors
from data import ValueDescriptor

import sys
import json

from pymodbus.client.sync import ModbusTcpClient as ModbusClient

def run_sync_client():
    client = ModbusClient('127.0.0.1')

    # from pymodbus.transaction import ModbusRtuFramer
    # client = ModbusClient('localhost', port=5020, framer=ModbusRtuFramer)
    # client = ModbusClient(method='binary', port='/dev/ptyp0', timeout=1)
    # client = ModbusClient(method='ascii', port='/dev/ptyp0', timeout=1)
    # client = ModbusClient(method='rtu', port='/dev/ptyp0', timeout=1,
    #                       baudrate=9600)

    client.connect()

    # log.debug("Reading Coils")
    # rq = client.read_coils(1, 1, unit=UNIT)
    # log.debug("ReadBitResponse: " + str(rq.bits))

    # log.debug("Read discrete inputs")
    # rq = client.read_discrete_inputs(0, 8, unit=UNIT)
    # assert(not rq.isError())     # test that we are not an error

    # log.debug("Read input registers")
    # rq = client.read_input_registers(1, 8, unit=UNIT)
    # assert(not rq.isError())     # test that we are not an error

    client.close()

def switch():

    option = int(ValueDescriptor["Type"])

    if option == "Discrete Input":
        client.read_discrete_inputs(ipAddress,valueDescriptor["Register"])

    elif option == "Input Register":
        client.read_input_registers(ipAddress,valueDescriptor["Register"])

    else:
        print("Incorrect register type")

switch()

if __name__ == '__main__':

    ipAddress = "127.0.0.1"
    if len(sys.argv) == 2:
        ipAddress = sys.argv[1]

    client = ModbusClient(ipAddress)
    if client.connect() == False:
        print("Could not connect to " + ipAddress)
        exit(-1)

    for valueDescriptor in valueDescriptors:
        #check if it coil or input - check switch case in python, if else unknown type - inform user about fuckuo
        #for aproprieate you call certain function (coil or input register)


    client.close()

    # go over data in valueDescriptors one by one - write a loop (for each) to go through data
    # basing on Type get either a coil or input value specified by register
    # handle errors nicely
    # print either in human readable or "csv" format
    # pretty much done


# if patrzy na to jaki to typ (coil czy nie)
#jeżeli coil to pytam o coil (true/False)
#jeżeli to input to pytam o wartość
#printuję otrzymana wartość, jezeli nie otrzymano wartości to używamy funkcji is error
#koniec
