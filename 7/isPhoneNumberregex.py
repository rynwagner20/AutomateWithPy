import re

phoneNumberRegex = re.compile(r'\d{3}-d{3}-d{4}')
num = phoneNumberRegex.search()
