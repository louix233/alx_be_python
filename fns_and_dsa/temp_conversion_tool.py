# Beginner-friendly checker for temp_conversion_tool.py

# 1. Import the module
import fns_and_dsa.temp_conversion_tool as temp_module

passed = True

# 2. Check global variables
if hasattr(temp_module, "FAHRENHEIT_TO_CELSIUS_FACTOR") and hasattr(temp_module, "CELSIUS_TO_FAHRENHEIT_FACTOR"):
    print("Global conversion factors defined.")
else:
    print("Error: Global conversion factors not defined.")
    passed = False

# 3. Check conversion functions
try:
    if callable(temp_module.convert_to_celsius) and callable(temp_module.convert_to_fahrenheit):
        # Simple test
        c = temp_module.convert_to_celsius(32)
        f = temp_module.convert_to_fahrenheit(0)
        if round(c, 2) == 0 and round(f, 2) == 32:
            print("Conversion functions implemented correctly.")
        else:
            print("Error: Conversion functions return wrong values.")
            passed = False
    else:
        print("Error: Conversion functions not defined.")
        passed = False
except:
    print("Error: Conversion functions caused an exception.")
    passed = False

# 4. Check ValueError for non-numeric input
try:
    temp_module.main()
except ValueError as ve:
    if str(ve) == "Invalid temperature. Please enter a numeric value.":
        print("ValueError correctly implemented for non-numeric input.")
    else:
        print("Error: ValueError message is incorrect.")
        passed = False
except:
    print("Error: main() caused an unexpected exception.")
    passed = False

if passed:
    print("\nAll checks passed. Your temp_conversion_tool.py meets the requirements.")
else:
    print("\nSome checks failed. Review the messages above.")
