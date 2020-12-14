import collections
from collections import namedtuple

ValueDescriptor = namedtuple("ValueDescriptor", ["Type", "Register", "Description", "Unit"])

valueDescriptors =  [ValueDescriptor("Input Register", 6, "Active set system temp.", "°C"),
                     ValueDescriptor("Input Register", 14, "Actual system output", "%"),
                     ValueDescriptor("Input Register", 15, "Boiler water temperature", "°C"),
                     ValueDescriptor("Input Register", 29, "Heating circuit pump A1", "h"),
                     ValueDescriptor("Input Register", 43, "Cylinder primary pump", "h"),
                     ValueDescriptor("Input Register", 60, "Operating mode heating circuit", "None"),
                     ValueDescriptor("Input Register", 61, "Set room temp. HC1", "°C"),
                     ValueDescriptor("Input Register", 78, "COP DHW mode", "°C"),
                     ValueDescriptor("Input Register", 89, "Outside temperature", "°C"),
                     ValueDescriptor("Input Register", 95, "Flow temp. Secondary", "°C"),
                     ValueDescriptor("Input Register", 101, "System flow temp", "°C"),
                     ValueDescriptor("Input Register", 103, "Buffer cylinder temp", "°C"),
                     ValueDescriptor("Input Register", 105, "DHW temperature top", "°C"),
                     ValueDescriptor("Input Register", 161, "COP heating mode", "None"),
                     ValueDescriptor("Input Register", 171, "Speed, fan 1", "RPM"),
                     ValueDescriptor("Input Register", 174, "Output, defrost enabled", "None"),
                     ValueDescriptor("Discrete Input", 6, "Electric heating stage 1", "None"),
                     ValueDescriptor("Discrete Input", 9, "Heating circuit pump HC1", "None"),
                     ValueDescriptor("Discrete Input", 16, "DHW circulation pump", "None"),
                     ValueDescriptor("Discrete Input", 18, "Secondary pump", "None"),
                     ValueDescriptor("Discrete Input", 22, "Cylinder primary pump", "None"),
                     ValueDescriptor("Discrete Input", 52, "Primary source 1 (fan or primary pump)", "None"),
                     ValueDescriptor("Discrete Input", 200, "Device failure", "None")]