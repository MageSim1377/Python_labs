pres = float(input("Enter pressure (in paskals): "))
vol = float(input("Enter volume (in m^3): "))
tem = float(input("Enter temperature (in kelvin): "))

quantity = pres*vol/tem/8.314

print(f"Quantity of gase: {quantity}")
