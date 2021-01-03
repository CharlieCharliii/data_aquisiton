#!/usr/bin/python

from data import valueDescriptorsTCP

import sys

from pymodbus.client.sync import ModbusTcpClient
TCP_host = "192.168.1.20"

def run_sync_client():
    clientTCP = ModbusTcpClient(host=TCP_host, port=502, retries=3)
    #clientRTU1 = ModbusSerialClient1(method='rtu', port='/dev/ttySC0', stopbits=1, timeout=1, baudrate=19200, parity='E')

    # from pymodbus.transaction import ModbusRtuFramer
    # client = ModbusClient('localhost', port=5020, framer=ModbusRtuFramer)
    # client = ModbusClient(method='binary', port='/dev/ptyp0', timeout=1)
    # client = ModbusClient(method='ascii', port='/dev/ptyp0', timeout=1)
    # client = ModbusClient(method='rtu', port='/dev/ptyp0', timeout=1, baudrate=9600)

    clientTCP.connect()

    clientTCP.close()

if __name__ == '__main__':
    run_sync_client()

    ipAddress = TCP_host
    if len(sys.argv) == 2:
        ipAddress = sys.argv[1]

    clientTCP = ModbusTcpClient(ipAddress)
    if clientTCP.connect() == False:
        print("Could not connect to " + ipAddress)
        exit(-1)

    # switchcase - run function for Discrete Input or Input Register
    # go over data in valueDescriptorsTCP one by one
    for ValueDescriptorTCP in valueDescriptorsTCP:
        # Valuedescriptor: ["SlaveID", "Type", "Register", "Description", "Unit"]
        # based on the Register Type get either an Inout Register, Holding Register or Discrete Input status or return an Error

        if  ValueDescriptorTCP[1] == "Input Register":
            # get input registers values and handle error
            # raw value read from the Vitogate
            result = clientTCP.read_input_registers(ValueDescriptorTCP[2],1, unit=ValueDescriptorTCP[0])
            # divider of the result to take decimal point info account
            divider = ValueDescriptorTCP[5]
            res = result.registers
            # result divided by the divider
            value = (float(result.registers[0])/divider)
            # print human readable values along with short description - Register Type, Register Number, Description, Register Value, Unit
            print("SlaveID: " + str(ValueDescriptorTCP[0]) + ", " + ValueDescriptorTCP[1] + ": " + str(ValueDescriptorTCP[2]) + ", " + ValueDescriptorTCP[3] + ": " + str(value) + " " + ValueDescriptorTCP[4] + ";")

        elif ValueDescriptorTCP[1] == "Holding Register":
            # get holding registers values and handle error
            # raw value read from the Vitogate
            result = clientTCP.read_holding_registers(ValueDescriptorTCP[2],1, unit=ValueDescriptorTCP[0])
            # divider of the result to take decimal point info account
            divider = ValueDescriptorTCP[5]
            # result divided by the divider
            value = (float(result.registers[0])/divider)
            # print human readable values along with short description - Register Type, Register Number, Description, Register Value, Unit
            print("SlaveID: " + str(ValueDescriptorTCP[0]) + ", " + ValueDescriptorTCP[1] + ": " + str(ValueDescriptorTCP[2]) + ", " + ValueDescriptorTCP[3] + ": " + str(value) + " " + ValueDescriptorTCP[4] + ";")
            pass

        elif ValueDescriptorTCP[1] == "Discrete Input":
            # get coil status and handle error
            status = clientTCP.read_discrete_inputs(ValueDescriptorTCP[2],1, unit=ValueDescriptorTCP[0])
            # print human readable values along with short description - Register Type, Register Number, Description, Register Value, Unit
            print("SlaveID: " + str(ValueDescriptorTCP[0]) + ", " + ValueDescriptorTCP[1] + ": " + str(ValueDescriptorTCP[2]) + ", " + ValueDescriptorTCP[3] + ": " + str(status.bits[0]) + ", " + ValueDescriptorTCP[4] + ";")
            pass

        else:
            # Print human readable errors to certain Address
            print("Unknown value type: " + "Slave ID: " + ValueDescriptorTCP[0] + ", "  + ValueDescriptorTCP[1] +": "  + ValueDescriptorTCP[2])