
import collections
from collections import namedtuple

##TCP connected devices

ValueDescriptorTCP = namedtuple("ValueDescriptorTCP", ["SlaveID", "Type", "Register", "Description", "Unit", "divider"])

valueDescriptorsTCP = [#ValueDescriptorTCP(1, "Input Register", 13, "Actual system output", "%", 1),
                       #ValueDescriptorTCP(1, "Input Register", 14, "Boiler water temperature", "deg.C", 100),
                       ValueDescriptorTCP(1, "Input Register", 24, "Elec. heating stage", "h", 1),
                       ValueDescriptorTCP(1, "Input Register", 28, "Heating circuit pump A1", "h", 1),
                       #ValueDescriptorTCP(1, "Input Register", 42, "Cylinder primary pump", "h", 1),
                       #ValueDescriptorTCP(1, "Input Register", 43, "Cylinder heating", "h", 1),
                       ValueDescriptorTCP(1, "Input Register", 59, "Operating mode heating circuit", "None", 1),
                       ValueDescriptorTCP(1, "Input Register", 60, "Set room temp. HC1", "deg.C", 10),
                       ValueDescriptorTCP(1, "Input Register", 77, "COP DHW mode (at the moment)", "None", 10),
                       ValueDescriptorTCP(1, "Input Register", 88, "Outside temperature", "deg.C", 10), #if negative temperature outside, returns value above 65k
                       ValueDescriptorTCP(1, "Input Register", 94, "Flow temp. Secondary", "deg.C", 10),
                       #ValueDescriptorTCP(1, "Input Register", 95, "Return temperature secondary", "deg.C", 10),
                       ValueDescriptorTCP(1, "Input Register", 102, "Buffer cylinder temp", "deg.C", 10),
                       ValueDescriptorTCP(1, "Input Register", 104, "DHW temperature top", "deg.C", 10),
                       ValueDescriptorTCP(1, "Input Register", 126, "Current compressor frequency", "Hz", 1),
                       ValueDescriptorTCP(1, "Input Register", 139, "Operating status of HC1", "None", 1),
                       ValueDescriptorTCP(1, "Input Register", 160, "COP heating mode (at the moment)", "None", 10),
                       ValueDescriptorTCP(1, "Input Register", 170, "Speed, fan 1", "RPM", 1),
                       ValueDescriptorTCP(1, "Input Register", 171, "Speed, fan 2", "RPM", 1),
                       #ValueDescriptorTCP(1, "Holding Register", 6, "Set boiler output", "%", 1),
                       #ValueDescriptorTCP(1, "Holding Register", 7, "Set boiler temperature", "deg. C", 1000),
                       #ValueDescriptorTCP(1, "Holding Register", 8, "Set boiler temperature", "deg. C", 1000),
                       #ValueDescriptorTCP(1, "Holding Register", 12, "Standard room temperature", "deg. C", 10),
                       #ValueDescriptorTCP(1, "Holding Register", 13, "Reduced room temperature", "deg. C", 10),
                       #ValueDescriptorTCP(1, "Holding Register", 26, "Compressor output", "%", 1),
                       #ValueDescriptorTCP(1, "Holding Register", 47, "Compressor output", "%", 1),
                       #ValueDescriptorTCP(1, "Holding Register", 49, "Set DHW temperature", "deg. C", 10),
                       ValueDescriptorTCP(1, "Discrete Input", 5, "Electric heating", "None", 1),
                       ValueDescriptorTCP(1, "Discrete Input", 8, "Heating circuit pump HC1", "None", 1),
                       ValueDescriptorTCP(1, "Discrete Input", 15, "DHW circulation pump", "None", 1),
                       ValueDescriptorTCP(1, "Discrete Input", 17, "Secondary pump", "None", 1),
                       ValueDescriptorTCP(1, "Discrete Input", 21, "Cylinder primary pump", "None", 1),
                       ValueDescriptorTCP(1, "Discrete Input", 48, "Relay status 3-way valve heating/DHW", "None", 1),
                       ValueDescriptorTCP(1, "Discrete Input", 49, "Relay EEV1 compressor", "None", 1),
                       ValueDescriptorTCP(1, "Discrete Input", 51, "Primary source 1 (fan or primary pump)", "None", 1)]

##serial connected devices port Serial1

ValueDescriptorSerial1 = namedtuple("ValueDescriptorSerial1", ["SlaveID", "Type", "Register", "Description", "Unit", "divider"])

valueDescriptorsSerial1 = [#energy meter value E=(R20x256^2 + R21)*10^-2 kWh
                        ValueDescriptorSerial1(10, "Holding Register", 20, "PV production", "(valuex256^2)*10^-2 kWh", 1),
                        ValueDescriptorSerial1(10, "Holding Register", 21, "PV production", "(value*10^-2) kWh", 1),
                        ValueDescriptorSerial1(20, "Holding Register", 20, "Heat Pump consumption", "(valuex256^2)*10^-2 kWh", 1),
                        ValueDescriptorSerial1(20, "Holding Register", 21, "Heat Pump consumption", "(value*10^-2) kWh", 1),]
