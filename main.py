#!/usr/bin/python

from data import valueDescriptors

import sys

from pymodbus.client.sync import ModbusTcpClient as ModbusClient

def run_sync_client():
    client = ModbusClient(host="192.168.1.20", port=502, retries=3)

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



if __name__ == '__main__':

    ipAddress = "192.168.1.20"
    if len(sys.argv) == 2:
        ipAddress = sys.argv[1]

    client = ModbusClient(ipAddress)
    if client.connect() == False:
        print("Could not connect to " + ipAddress, file=sys.stderr)
        exit(-1)

    # switchcase - run function for Discrete Input or Input Register
    # go over data in valueDescriptors one by one
    for ValueDescriptor in valueDescriptors:
        # Valuedescriptor: ["Type", "Register", "Description", "Unit"]
        # based on the Register Type get either a Discrete Input value, Input Register status or return an Error
        if  ValueDescriptor[0] == "Input Register":
            #get input registers values and handle error
            #client.read_input_registers(ipAddress, ValueDescriptor[1])
            value=21.37 #value block as a placeholder
            #print(ValueDescriptor[0] + ": " + ValueDescriptor[1] + " " + ValueDescriptor[3])
            print(ValueDescriptor[0] + ": " + str(value) + " " + ValueDescriptor[3])

        elif ValueDescriptor[0] == "Discrete Input":
            #get coil status and handle error
            #client.read_discrete_inputs(ipAddress, ValueDescriptor[1])
            status=1
            #print(ValueDescriptor[0] + ": " + ValueDescriptor[1] + " " + ValueDescriptor[3])
            print(ValueDescriptor[0] + ": " + str(status) + " " + ValueDescriptor[3])
            pass

        else:
            # Print human readable errors to stderr so that the output is not cluttered if the data is to be parsed
            print("Unknown value type: " + ValueDescriptor[0], file=sys.stderr)

        #check if it coil or input - check switch case in python, if else unknown type - inform user about fuckuo
        #for aproprieate you call certain function (coil or input register)




    # go over data in valueDescriptors one by one - write a loop (for each) to go through data
    # basing on Type get either a coil or input value specified by register
    # handle errors nicely
    # print either in human readable or "csv" format
    # pretty much done


# if patrzy na to jaki to typ (coil czy nie)
#jezeli coil to pytam o coil (true/False)
#jezeli to input to pytam o wartosc
#printuje otrzymana wartosc, jezeli nie otrzymano wartosci to uzywamy funkcji is error
#koniec
