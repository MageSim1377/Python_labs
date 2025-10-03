minutes = int(input("Enter amount of minutes you talked this month: "))
sms = int(input("Enter amount of sms you sent this month: "))
internet = int(input("Enter amount of Mb of internet you spent this month: "))

tarif = 24.99

sum = tarif
extraMin = 0
if minutes > 60:
    extraMin += minutes - 60
extraSms = 0
if sms > 30:
    extraSms += sms - 30
extraMb = 0
if internet > 1024:
    extraMb += internet - 1024

extraMinCost = extraMin * 0.89
extraSmsCost = extraSms * 0.59
extraMbCost = extraMb * 0.79

sum += extraMinCost + extraSmsCost + extraMbCost

tax = sum * 0.02

print("Tarif: " + f"{tarif:.2f}")
if extraMin != 0:
    print(f"Extra minutes cost: {extraMinCost:.2f}")
if extraSms != 0:
    print(f"Extra sms cost:{extraSmsCost:.2f}")
if extraMb != 0:
    print(f"Extra internet cost: {extraMbCost:.2f}")

print(f"Tax: {tax:.2f}")

print(f"Extra pay: {extraMin + extraSms + extraMb}")

print(f"All: {sum + tax:.2f}")
