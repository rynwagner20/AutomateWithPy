def isPhoneNumber2(text):
    if len(text) != 12: return False
    for i in range(0,3):
        if not text[i].isdigit(): return False
    if text[3] != '-': return False
    for i in range(4,7):
        if not text[i].isdigit(): return False
    if text[7] != '-': return False
    for i in range(8,12):
        if not text[i].isdigit(): return False
    return True

text = '917-436-2716'
print(isPhoneNumber2(text))

for i in range(len(text)):
    holder = text[i:i+12]
    if isPhoneNumber2(holder):
        print(holder + ' is a phone number')
