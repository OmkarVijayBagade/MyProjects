# temperature convertor 



def convert_temp(temp,unit):
    if unit == 'C' or 'c':
        return (temp*9/5)+32
    elif unit == 'F' or 'f':
        return (temp-32)*5/9
    else:
        return "Invalid unit"

print("Enter the temperature to be converted into: ")
unit = input()
temp = float(input("Enter the temperature: "))
print(f"the converted temperature to the input temperature: ",convert_temp(temp,unit))
