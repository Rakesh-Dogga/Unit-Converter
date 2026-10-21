"""
Unit Converter is a program that converts values from one unit to another within a specific category.

1. The program first asks the user to select a converter, such as Length, Temperature, Speed, Time, Volume, or Digital Storage.
2. Then, it asks the user to enter the source unit (from_metric), the value to be converted (from_value), and the target unit (target_metric).
3. Finally, the program converts the given value from the source unit to the target unit and displays the result.
"""
def length_converter(from_value, from_metric, target_metric):
    """Store conversion factors in dictrionary for km, m, cm with values with respect to meters."""
    conversion_factor = {
        "km" : 1000,                    # 1 kilo meter  = 1000 meters
        "m" : 1,                        # 1 meter  = 1 meters
        "cm" : 0.01,                    # 1 centi-meter = 0.01 meters
        "mm" : 0.001,                   # 1 milli-meter = 0.001 meters
        "nanometer" : 0.000000001,      # 1 nano-meter = 0.000000001 meters
        "mile" : 1609.34,               # 1 mile = 1609.34 meters
        "nautical_mile" : 1852,         # 1 natical-mile = 1852 meters
        "yard": 0.9144,                 # 1 yard = 0.9144 meters
        "foot" : 0.3048,                # 1 foot = 0.3048 meters
        "inch" : 0.0254                 # 1 inch = 0.0254 meters
    }

    from_metric = from_metric.lower().strip()
    target_metric = target_metric.lower().strip()

    #validate source and target unit
    if from_metric not in conversion_factor:
        raise ValueError(f"Unsupported source units: {from_metric}")
    if target_metric not in conversion_factor:
        raise ValueError(f"Unsupported souce unitts: {target_metric}")

    #convert any input value to meters
    value_in_meters = float(from_value) * conversion_factor[from_metric]

    #Then value_in_meters is again converted to required conversion of the input value.
    converted_value = value_in_meters / conversion_factor[target_metric]

    return converted_value

def temperature_converter(from_value, from_metric, target_metric):
    """Convert temperature bertween Celsius, Fahrenheit and Kelvin"""

    from_metric = from_metric.lower().strip()
    target_metric = target_metric.lower().strip()
    from_value = float(from_value)

    #supported units in temperature converter
    supported_units = ["c", "f", "k"]

    #validate source and target unit
    if from_metric not in supported_units:
        raise ValueError(f"Unsupported source units: {from_metric}")
    if target_metric not in supported_units:
        raise ValueError(f"Unsupported source units: {target_metric}")

    #convert the source temperature to celsius
    if from_metric == "c":
        celsius = from_value
    elif from_metric == "f":
        celsius = (from_value - 32) * 5/9
    else:
        celsius = from_value - 273.15

    #convert censius to the target temperature
    if target_metric == "c":
        result = celsius
    elif target_metric == "f":
        result = (celsius * 9/5) + 32
    else:
        result = celsius + 273.15

    if celsius < -273.15:
        raise ValueError(f"Temperature cannot be below absolute zero: {celsius}")
    return result

def speed_converter(from_value, from_metric, target_metric):
    """Convert speed bertween km/h, m/s, and knots."""

    # converstion factors related to speed i.e, meters per second, kilometers per hours, miles per hours and nautical mile per hour
    conversion_factor = {
        "m/s" : 1,              #with respect to meters per second
        "km/h" : 1/3.6,         #with respect to meters per second
        "mph" : 0.44704,        #with respect to meters per second
        "knot" : 0.514444       #with respect to meters per second
    }

    from_metric = from_metric.lower().strip()
    target_metric = target_metric.lower().strip()
    from_value = float(from_value)

    #validate source and target units
    if from_metric not in conversion_factor:
        raise ValueError(f"Unsupported source unit: {from_metric}")
    
    if target_metric not in conversion_factor:
        raise ValueError(f"Unsupported target unit: {target_metric}")

    #convert the input in to meters per seconds and then convert the meters per second to the target unit
    speed_in_mps = from_value * conversion_factor[from_metric]
    converted_value = speed_in_mps / conversion_factor[target_metric]

    return converted_value

def time_converter(from_value, from_metric, target_metric):
    """convert time between seconds, minutes, hours, days, and weeks"""

    conversion_factor = {
        "s": 1,                       # 1 second
        "min": 60,                    # 1 minute = 60 seconds
        "h": 3600,                    # 1 hour = 3600 seconds
        "day": 86400,                 # 1 day = 86400 seconds
        "week": 604800,               # 1 week = 7 days
        "month": 2592000,             # 1 month = 30 days
        "year": 31536000,             # 1 year = 365 days
        "decade": 315360000,          # 1 decade = 10 years
        "century": 3153600000         # 1 century = 100 years
    }

    from_metric = from_metric.lower().strip()
    from_value = float(from_value)
    target_metric = target_metric.lower().strip()

    #validate source and target units
    if from_metric not in conversion_factor:
        raise ValueError(f"Unsupported source unit: {from_metric}")
    if target_metric not in conversion_factor:
        raise ValueError(f"Unsupported target unit: {target_metric}")

    #convert the input into seconds and then into target unit
    value_in_seconds = from_value * conversion_factor[from_metric]
    converted_value = value_in_seconds / conversion_factor[target_metric]

    return converted_value
    
def volume_converter(from_value, from_metric, target_metric):
    """convert volume between liters. milliters, cubic meters, and gallons"""

    conversion_factor = {
        "l": 1,                     # 1 liter 
        "ml": 0.001,                # 1 milliliter = 0.001 liters
        "m3": 1000,                 # 1 cubic meter = 1000 liters
        "gal": 3.785411784,         # 1 US gallon = 3.785412 liters
        "oz": 0.0295735295625       # 1 US fluid ounce = 0.02957353 liters
    }

    from_metric = from_metric.lower().strip()
    from_value = float(from_value)
    target_metric = target_metric.lower().strip()

    # Validate source and target units
    if from_metric not in conversion_factor:
        raise ValueError(f"Unsupported source unit: {from_metric}")
    if target_metric not in conversion_factor:
        raise ValueError(f"Unsupported target unit: {target_metric}")

    # Convert source value to liters and then to target units
    value_in_liters = from_value * conversion_factor[from_metric]
    converted_value = value_in_liters / conversion_factor[target_metric]

    return converted_value

def digital_storage_coverter(from_value, from_metric, target_metric):
    """Convert digital storage units using bytes as the base unit."""

    conversion_factor = {
        "bit": 0.125,           # 1 bit = 0.125 bytes
        "byte": 1,              # 1 byte = 1 byte
        "kb": 1000,             # 1 kilobyte = 1000 bytes
        "mb": 1000 ** 2,        # 1 megabyte = 1000000 bytes
        "gb": 1000 ** 3,        # 1 gigabyte = 1000000000 bytes
        "tb": 1000 ** 4,        # 1 terabyte = 1000000000000 bytes
        "pb": 1000 ** 5,        # 1 petabyte = 1000000000000000 bytes
        "eb": 1000 ** 6         # 1 exabyte = 1000000000000000000 bytes
    }

    from_metric = from_metric.lower().strip()
    target_metric = target_metric.lower().strip()
    from_value = float(from_value)

    if from_metric not in conversion_factor:
        raise ValueError(f"Unsupported source unit: {from_metric}")
    if target_metric not in conversion_factor:
        raise ValueError(f"Unsupported target unit: {target_metric}")

    if from_value < 0:
        raise ValueError("Digital storage cannot be negative.")

    #convert source units in bytes and then into target units
    value_in_bytes = from_value * conversion_factor[from_metric]
    converted_value = value_in_bytes / conversion_factor[target_metric]

    return converted_value


#MAIN PROGRAM - Collects the inputs, validates the converter slection, call the appropriate convert function and display result

#display specific unit metrics for each converter and collect inputs
def get_conversion_inputs(converter_name, units):
    """Display available units and collect conversion inputs"""
    print(f"\nAvailable {converter_name} units: ")

    for units, description in units.items():
        print(f" {units:<6} - {description}")

    from_metric = input("\nConvert from units: ").lower().strip()
    from_value = float(input("Enter value: "))
    target_metric = input("Convert to units: ").lower().strip()

    return from_value, from_metric, target_metric

#display units in length converter
def run_length_converter():
    units = {
        "km" : "Kilometer",
        "m" : "meter",
        "cm" : "Centimeter",
        "mm" : "Millimeter",
        "nanometer" : "Nanometer",
        "mile" : "Mile",
        "nautical_mile" : "Nautical mile",
        "yard" : "Yard",
        "foot" : "Foot",
        "inch" :"Inch"
    }

    value, source, target = get_conversion_inputs("length", units)
    result = length_converter(value, source, target)
    return result, target

#display units in temperature converter
def run_temperature_converter():
    units = { 
        "c" : "Celsius",
        "f" : "Fahrenheit",
        "k" : "Kelvin"
    }

    value, source, target = get_conversion_inputs("temperature", units)
    result = temperature_converter(value, source, target)
    return result, target

#display units in speed converter
def run_speed_converter():
    units = {
        "m/s" : "Meters per second",
        "km/h" : "Kilometers per hour",
        "mph" : "Miles per hour",
        "knot" : "Nautical miles per hour"
    }

    value, source, target = get_conversion_inputs("speed", units)
    result = speed_converter(value, source, target)
    return result, target

#display units in time converter
def run_time_converter():
    units = {
        "s": "Seconds",
        "min": "Minutes",
        "h": "Hours",
        "day": "Days",
        "week": "Weeks",
        "month": "Months (30 days)",
        "year": "Years (365 days)",
        "decade": "Decades (10 years)",
        "century": "Centuries (100 years)"
    }

    value, source, target = get_conversion_inputs("time", units)
    result = time_converter(value, source, target)
    return result, target

#display units in volume converter
def run_volume_converter():
    units = {
        "l": "Liters",
        "ml": "Milliliters",
        "m3": "Cubic meters",
        "gal": "US gallons",
        "oz": "US fluid ounces"
    }

    value, source, target = get_conversion_inputs("volume", units)
    result = volume_converter(value, source, target)
    return result, target

def run_digital_storage_converter():
    units = {
        "bit" : "Bit",
        "byte" : "Byte",
        "kb" : "Kilobyte",
        "mb" : "Megabyte",
        "gb" : "Gigabyte",
        "tb" : "Terabyte",
        "pb" : "Petabyte",
        "eb" : "Exabyte",
    }

    value, source, target = get_conversion_inputs("digital storage", units)
    result = digital_storage_coverter(value, source, target)
    return result, target

print("=" * 10)
print("Unit Converter")
print("=" * 10)

#list of converters available
list_of_converters = ["length", "temperature", "speed", "time", "volume", "digital storage"]

#----------- select converter -----------#
print("\nAvailable converters: ")
for converter in list_of_converters:
    print(f"{converter.title()}")

select_converter = input("Enter selected converter: ")
select_converter = select_converter.lower().strip()

converter_function = {
    "length" : run_length_converter,
    "temperature" : run_temperature_converter,
    "speed" : run_speed_converter,
    "time" : run_time_converter,
    "volume" : run_volume_converter,
    "digital storage" : run_digital_storage_converter
}

if select_converter not in list_of_converters:
    print(f"Conveter not available: {select_converter}")

else:
    try:
        result, target_metric = converter_function[select_converter]()
        print("\n" + "=" * 30)
        print("CONVERSION RESULT")
        print(f"Result: {result:g} {target_metric}")
        print("=" * 30)

    except ValueError as error:
        print(f"Invalid input: {error}")


        
