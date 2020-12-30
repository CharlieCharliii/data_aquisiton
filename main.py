#!/usr/bin/python

from data import valueDescriptors

import sys
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
#from pymodbus.client.sync import ModbusSerialClient as ModbusClient
TCP_host = "192.168.1.20"

def run_sync_client():
    client = ModbusClient(host=TCP_host, port=502, retries=3)
    #client = ModbusClient(method='rtu', port='/dev/ttySC0', timeout=1, baudrate=19200, parity='E')

    # from pymodbus.transaction import ModbusRtuFramer
    # client = ModbusClient('localhost', port=5020, framer=ModbusRtuFramer)
    # client = ModbusClient(method='binary', port='/dev/ptyp0', timeout=1)
    # client = ModbusClient(method='ascii', port='/dev/ptyp0', timeout=1)
    # client = ModbusClient(method='rtu', port='/dev/ptyp0', timeout=1, baudrate=9600)

    client.connect()

    # log.debug("Reading Coils")
    # rq = client.read_coils(1, 1, unit=UNIT)
    # log.debug("ReadBitResponse: " + str(rq.bits))

    # log.debug("Read discrete inputs")
    # rq = client.read_discrete_inputs(9, 1, unit=UNIT)
    # assert(not rq.isError())     # test that we are not an error

    # log.debug("Read input registers")
    # rq = client.read_input_registers(6, 1, unit=UNIT)
    # assert(not rq.isError())     # test that we are not an error


    client.close()


if __name__ == '__main__':
    run_sync_client()

    ipAddress = TCP_host
    if len(sys.argv) == 2:
        ipAddress = sys.argv[1]

    client = ModbusClient(ipAddress)
    if client.connect() == False:
        print("Could not connect to " + ipAddress)
        exit(-1)

    # switchcase - run function for Discrete Input or Input Register
    # go over data in valueDescriptors one by one
    for ValueDescriptor in valueDescriptors:
        # Valuedescriptor: ["Type", "Register", "Description", "Unit"]
        # based on the Register Type get either a Discrete Input value, Input Register status or return an Error
        if  ValueDescriptor[0] == "Input Register":
            # get input registers values and handle error
            value = client.read_input_registers(ValueDescriptor[1],1, unit=1)
            #val = client.read_input_registers(15,0)
            #value = str(val)
            #value=21.37
            #print(value)
            # print human readable values along with short description - Register Type, Register Number, Description, Register Value, Unit
            print(ValueDescriptor[0] + ": " + str(ValueDescriptor[1]) + ", " + ValueDescriptor[2] + ": " + str(value.registers) + " " + ValueDescriptor[3] + ";")

        elif ValueDescriptor[0] == "Discrete Input":
            # get coil status and handle error
            status = client.read_discrete_inputs(ValueDescriptor[1],1,unit=1)
            # print human readable values along with short description - Register Type, Register Number, Description, Register Value, Unit
            print(ValueDescriptor[0] + ": " + str(ValueDescriptor[1]) + ", " + ValueDescriptor[2] + ": " + str(status.bits[0]) + ", " + ValueDescriptor[3] + ";")
            pass

        else:
            # Print human readable errors to certain Address
            print("Unknown value type: " + ValueDescriptor[0])
            
