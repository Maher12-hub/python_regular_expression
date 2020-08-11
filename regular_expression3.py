import re
with open('data.txt.txt','r') as rf:
    content=rf.read()
pattern=re.compile(r'\d{3}[-.]\d{3}[-.]\d{4}')
matches=pattern.finditer(content)
for match in matches:
    print(match)
    