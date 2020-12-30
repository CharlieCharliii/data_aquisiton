import collections
from collections import namedtuple

ValueDescriptor = namedtuple("ValueDescriptor", ["Type", "Register", "Description", "Unit"])

valueDescriptors =  [ValueDescriptor("Input Register", 13, "Actual system output", "%"),
                     ValueDescriptor("Input Register", 14, "Boiler water temperature", "deg.C"),
                     ValueDescriptor("Input Register", 24, "Elec. heating stage", "h"),
                     ValueDescriptor("Input Register", 28, "Heating circuit pump A1", "h"),
                     ValueDescriptor("Input Register", 42, "Cylinder primary pump", "h"),
                     ValueDescriptor("Input Register", 43, "Cylinder heating", "h"),
                     ValueDescriptor("Input Register", 59, "Operating mode heating circuit", "None"),
                     ValueDescriptor("Input Register", 60, "Set room temp. HC1", "deg.C"),
                     ValueDescriptor("Input Register", 77, "COP DHW mode", "None"),
                     ValueDescriptor("Input Register", 88, "Outside temperature", "deg.C"),
                     ValueDescriptor("Input Register", 94, "Flow temp. Secondary", "deg.C"),
                     ValueDescriptor("Input Register", 95, "Return temperature secondary", "deg.C"),
                     ValueDescriptor("Input Register", 102, "Buffer cylinder temp", "deg.C"),
                     ValueDescriptor("Input Register", 104, "DHW temperature top", "deg.C"),
                     ValueDescriptor("Input Register", 126, "Current compressor frequency", "Hz"),
                     ValueDescriptor("Input Register", 139, "Operating status of HC1", "None"),
                     ValueDescriptor("Input Register", 160, "COP heating mode", "None"),
                     ValueDescriptor("Input Register", 170, "Speed, fan 1", "RPM"),
                     ValueDescriptor("Input Register", 171, "Speed, fan 2", "RPM"),
                     ValueDescriptor("Discrete Input", 5, "Electric heating stage", "None"),
                     ValueDescriptor("Discrete Input", 8, "Heating circuit pump HC1", "None"),
                     ValueDescriptor("Discrete Input", 15, "DHW circulation pump", "None"),
                     ValueDescriptor("Discrete Input", 17, "Secondary pump", "None"),
                     ValueDescriptor("Discrete Input", 21, "Cylinder primary pump", "None"),
                     ValueDescriptor("Discrete Input", 48, "Relay status 3-way valve heating/DHW", "None"),
                     ValueDescriptor("Discrete Input", 49, "Relay EEV1 compressor", "None"),
                     ValueDescriptor("Discrete Input", 51, "Primary source 1 (fan or primary pump)", "None")]