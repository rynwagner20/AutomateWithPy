def isPhoneNumber(text):
    if len(text) != 12: return False
    for i in range(0,3):
        if not text[i].isdigit():return False
    if text[3] != '-': return False
    for i in range(4,7):
        if not text[i].isdigit():return False
    if text[7] != '-': return False
    for i in range(8,12):
        if not text[i].isdigit():return False
    return True

text = 'hellow world this is my new number 917-437-2716'

for i in range(len(text)):
    new = text[i:i+12]
    if isPhoneNumber(new):
        print(new + " is a phone number")
print('fin')
