from collections import namedtuple

ValueDescriptor = namedtuple("ValueDescriptor", ["Type", "Register", "Description", "Unit"])

valueDescriptors = [ValueDescriptor("Input", 6, "Active set system temp.", "°C"),
                    ValueDescriptor("Input", 14, "Actual system output", "%"),
                    ValueDescriptor("Input", 15, "Boiler water temperature", "°C"),
                    ValueDescriptor("Input", 29, "Heating circuit pump A1", "h"),
                    ValueDescriptor("Input", 43, "Cylinder primary pump", "h"),
                    ValueDescriptor("Input", 60, "Operating mode heating circuit", "None"),
                    ValueDescriptor("Input", 61, "Set room temp. HC1", "°C"),
                    ValueDescriptor("Input", 78, "COP DHW mode", "°C"),
                    ValueDescriptor("Input", 89, "Outside temperature", "°C"),
                    ValueDescriptor("Input", 95, "Flow temp. Secondary", "°C"),
                    ValueDescriptor("Input", 101, "System flow temp", "°C"),
                    ValueDescriptor("Input", 103, "Buffer cylinder temp", "°C"),
                    ValueDescriptor("Input", 105, "DHW temperature top", "°C"),
                    ValueDescriptor("Input", 161, "COP heating mode", "None"),
                    ValueDescriptor("Input", 171, "Speed, fan 1", "RPM"),
                    ValueDescriptor("Input", 174, "Output, defrost enabled", "None"),
                    ValueDescriptor("Coil", 6, "Electric heating stage 1", "None"),
                    ValueDescriptor("Coil", 9, "Heating circuit pump HC1", "None"),
                    ValueDescriptor("Coil", 16, "DHW circulation pump", "None"),
                    ValueDescriptor("Coil", 18, "Secondary pump", "None"),
                    ValueDescriptor("Coil", 22, "Cylinder primary pump", "None"),
                    ValueDescriptor("Coil", 52, "Primary source 1 (fan or primary pump)", "None"),
                    ValueDescriptor("Coil", 200, "Device failure", "None")]