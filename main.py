
#!/usr/bin/python

from data import valueDescriptorsTCP
from data import valueDescriptorsSerial1

import sys
import serial
import time

from pymodbus.client.sync import ModbusTcpClient
from pymodbus.client.sync import ModbusSerialClient

TCP_host = "192.168.1.20"

# RS485 ioctls define
TIOCGRS485 = 0x542E
TIOCSRS485 = 0x542F
SER_RS485_ENABLED = 0b00000001
SER_RS485_RTS_ON_SEND = 0b00000010
SER_RS485_RTS_AFTER_SEND = 0b00000100
SER_RS485_RX_DURING_TX = 0b00010000
# rs 485 port
ser1 = serial.Serial("/dev/ttySC0",19200)
ser2 = serial.Serial("/dev/ttySC1",9600)

#TCP client
def run_sync_client():
    clientTCP = ModbusTcpClient(host=TCP_host, port=502, retries=3)
    #clientRTU1 = ModbusSerialClient1(method='rtu', port='/dev/ttySC0', stopbits=1, timeout=1, baudrate=19200, parity='E')

    clientTCP.connect()

    clientTCP.close()

#serial client
def rs485_enable():
    buf = array.array('i', [0] * 8) # flags, delaytx, delayrx, padding
    #enable 485 chanel 1
    fcntl.ioctl(ser1, TIOCGRS485, buf)
    buf[0] |=  SER_RS485_ENABLED|SER_RS485_RTS_AFTER_SEND
    buf[1]  = 0
    buf[2]  = 0
    fcntl.ioctl(ser1, TIOCSRS485, buf)

    #enable 485 chanel 2
    fcntl.ioctl(ser2, TIOCGRS485, buf)
    buf[0] |=  SER_RS485_ENABLED|SER_RS485_RTS_AFTER_SEND
    buf[1]  = 0
    buf[2]  = 0
    fcntl.ioctl(ser2, TIOCSRS485, buf)
#end of rs485_enable():

clientSerial0 = ModbusSerialClient(method='rtu', port='/dev/ttySC0', stopbits=1, timeout=1, baudrate=19200, parity='E')
clientSerial1 = ModbusSerialClient(method='rtu', port='/dev/ttySC1', stopbits=1, timeout=1, baudrate=9600, parity='N')

clientSerial1.connect()

clientSerial1.close()



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
            #"SlaveID: " + str(ValueDescriptorTCP[0]) + ", " + ValueDescriptorTCP[1] + ": " + str(ValueDescriptorTCP[2]) + ", " +
            print(ValueDescriptorTCP[3] + ": " + str(value) + " " + ValueDescriptorTCP[4] + ";")

        elif ValueDescriptorTCP[1] == "Holding Register":
            # get holding registers values and handle error
            # raw value read from the Vitogate
            result = clientTCP.read_holding_registers(ValueDescriptorTCP[2],1, unit=ValueDescriptorTCP[0])
            # divider of the result to take decimal point info account
            divider = ValueDescriptorTCP[5]
            # result divided by the divider
            value = (float(result.registers[0])/divider)
            # print human readable values along with short description - Register Type, Register Number, Description, Register Value, Unit
            #"SlaveID: " + str(ValueDescriptorTCP[0]) + ", " + ValueDescriptorTCP[1] + ": " + str(ValueDescriptorTCP[2]) + ", " +
            print(ValueDescriptorTCP[3] + ": " + str(value) + " " + ValueDescriptorTCP[4] + ";")
            pass

        elif ValueDescriptorTCP[1] == "Discrete Input":
            # get coil status and handle error
            status = clientTCP.read_discrete_inputs(ValueDescriptorTCP[2],1, unit=ValueDescriptorTCP[0])
            # print human readable values along with short description - Register Type, Register Number, Description, Register Value, Unit
            #"SlaveID: " + str(ValueDescriptorTCP[0]) + ", " + ValueDescriptorTCP[1] + ": " + str(ValueDescriptorTCP[2]) + ", " +
            print(ValueDescriptorTCP[3] + ": " + str(status.bits[0]) + ", " + ValueDescriptorTCP[4] + ";")
            pass

        else:
            # Print human readable errors to certain Address
            print("Unknown value type: " + "Slave ID: " + ValueDescriptorTCP[0] + ", " + ValueDescriptorTCP[1] + ": " + ValueDescriptorTCP[2])

            
    #read PV production
    read_power = clientSerial1.read_holding_registers(address=10, count=2, unit=10)
    read_energy=clientSerial1.read_holding_registers(address = 20, count =2, unit=10)
    R10 = read_power.registers[0]
    R20=read_energy.registers[0]
    R21=read_energy.registers[1]
    PVprod = float(R10/1000)
    PVenergy = float((R20*(256**2)+R21)/100)
    print("PV production = " + str(PVprod) + "kW")
    print("PV energy = " + str(PVenergy) + " kWh") #printing value read in above line


    #delay needed by the RS485 bus
    time.sleep(.1)

    #read Heat Pump consumption
    read_power = clientSerial1.read_holding_registers(address=10, count=2, unit=20)
    read_energy=clientSerial1.read_holding_registers(address = 20, count =2, unit=20)
    R10 = read_power.registers[0]
    R20=read_energy.registers[0]
    R21=read_energy.registers[1]
    PVprod = float(R10/1000)
    PVenergy = float((R20*(256**2)+R21)/100)
    print("Heat pump consumption =  " + str(PVprod) + "kW")
    print("Heat pump energy = " + str(PVenergy) + " kWh") #printing value read in above line
            
'''
for ValueDescriptorSerial1 in valueDescriptorsSerial1:
    # Valuedescriptor: ["SlaveID", "Type", "Register", "Description", "Unit"]
    # based on the Register Type get either an Inout Register, Holding Register or Discrete Input status or return an Error
    time.sleep(0.1)
    if ValueDescriptorSerial1[1] == "Input Register":
        # get input registers values and handle error
        # raw value read from the Vitogate
        result = clientSerial1.read_input_registers(ValueDescriptorSerial1[2], 1, unit=ValueDescriptorSerial1[0])
        # divider of the result to take decimal point info account
        divider = ValueDescriptorSerial1[5]
        # result divided by the divider
        value = (float(result.registers[0]) / divider)
        # print human readable values along with short description - Register Type, Register Number, Description, Register Value, Unit
        print("SlaveID: " + str(ValueDescriptorSerial1[0]) + ", " + ValueDescriptorSerial1[1] + ": " + str(ValueDescriptorSerial1[2]) + ", " + ValueDescriptorSerial1[3] + ": " + str(value) + " " + ValueDescriptorSerial1[4] + ";")

    elif ValueDescriptorSerial1[1] == "Holding Register":
        # get holding registers values and handle error
        # raw value read from the Vitogate
        result = clientSerial1.read_holding_registers(ValueDescriptorSerial1[2], 1, unit=ValueDescriptorSerial1[0])
        # divider of the result to take decimal point info account
        divider = ValueDescriptorSerial1[5]
        # result divided by the divider
        value = (float(result.registers[0]) / divider)
        # print human readable values along with short description - Register Type, Register Number, Description, Register Value, Unit
        print("SlaveID: " + str(ValueDescriptorSerial1[0]) + ", " + ValueDescriptorSerial1[1] + ": " + str(ValueDescriptorSerial1[2]) + ", " + ValueDescriptorSerial1[3] + ": " + str(value) + " " + ValueDescriptorSerial1[4] + ";")
        pass

    elif ValueDescriptorSerial1[1] == "Discrete Input":
        # get coil status and handle error
        status = clientSerial1.read_discrete_inputs(ValueDescriptorSerial1[2], 1, unit=ValueDescriptorSerial1[0])
        # print human readable values along with short description - Register Type, Register Number, Description, Register Value, Unit
        print("SlaveID: " + str(ValueDescriptorSerial1[0]) + ", " + ValueDescriptorSerial1[1] + ": " + str(ValueDescriptorSerial1[2]) + ", " + ValueDescriptorSerial1[3] + ": " + str(status.bits[0]) + ", " + ValueDescriptorSerial1[4] + ";")
        pass

    else:
        # Print human readable errors to certain Address
        print("Unknown value type: " + "Slave ID: " + ValueDescriptorSerial1[0] + ", " + ValueDescriptorSerial1[1] + ": " + ValueDescriptorSerial1[2])
'''
