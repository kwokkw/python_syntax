def convert_temp(unit_in, unit_out, temp):
    """
    Convert farenheit <-> celsius and return results.
    °C = (°F - 32) × 5/9
    °F = (°C × 9/5) + 32

    - unit_in: either "f" or "c" 
    - unit_out: either "f" or "c"
    - temp: temperature (in f or c, depending on unit_in)

    Return results of conversion, if any.

    If unit_in or unit_out are invalid, return "Invalid unit [UNIT_IN]".

    For example:

      convert_temp("c", "f", 0)  =>  32.0
      convert_temp("f", "c", 212) => 100.0
    """

    # VALIDATION

    # `not in` membership operator
    if unit_in not in ("c", "f"):
        return "INVALID UNIT_IN: " + unit_in
    
    if unit_out not in ("c", "f"):
        return "INVALID UNIT_OUT: " + unit_out
    
    if(not isinstance(temp, (int, float))):
        return "INVALID temp: " + str(temp)
    
    # CALCULATION

    if unit_in == "c" and unit_in != unit_out:
        return temp * 9/5+32
    
    elif unit_in == unit_out:
        return temp
    
    else:
        return (temp - 32) * 5/9
    
# Edge cases
# print("z", "f", 32, convert_temp("c", "f", 32), "should be Invalid unit z")
# print("c", "z", 32, convert_temp("c", "z", 32), "should be Invalid unit z")

# print("c", "f", 0, convert_temp("c", "f", 0), "should be 32.0")
# print("f", "c", 212, convert_temp("f", "c", 212), "should be 100.0")
# print("f", "f", 75.5, convert_temp("f", "f", 75.5), "should be 75.5")

testing = convert_temp("c", "c", 75.5)
print(testing)