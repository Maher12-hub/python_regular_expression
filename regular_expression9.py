import re
#s='maher 1602154'
#result=re.sub(r'\d','5',s)
#print(result)
s='22/07/2017,20/01/2017,01/01/2018'
#result=re.sub(r'(\d{2})/(\d{2})/(\d{4})',r'\3-\2-\1',s)
result=re.sub(r'(\d{2})/(\d{2})/(\d{4})',r'\3-\2-\1',s)
print(result)