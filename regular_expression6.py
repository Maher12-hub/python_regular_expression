import re

#match=re.search('Ban','Bangladesh')
#match=re.search('dets','Bangladesh')
#match=re.search('.','Bangladesh')
#match=re.search('d.s','Bangladesh')
#s='Bangladesh is our homeland'
#match=re.search('o\w\w',s)
#match=re.search('\w+',s)
#match=re.search('B.+h',s)
#match=re.search('B.+h?',s)
#print(match.group())
#text='phone number:01303283008'
#match=re.search('\d+',text)
#print(match)
#text='house number:5,phone number:01303283008'
#match=re.search('\d{11}',text)
#print(match)
#text='house number:5,phone number:013 03283008'
#match=re.search('\d{3}\s*\d{8}',text)
#print(match)
#text='multiple phone number,01303283008,01875005811,01977605604,00000002233,01713605604'
#match=re.findall(r'01[3456789]\s*\d{8}',text)
#print(match)
#s='bangla english bangla'
#match=re.findall('^bangla',s)
#match=re.findall('^english',s)
#match=re.findall('bangla$',s)
#print(match)
#s='Bangla english Bangla'
#match=re.findall(r'bangla$',s,re.IGNORECASE)
#print(match)
with open('data.txt.txt','r') as rf:
    text=rf.read()
#print(text)
match=re.findall(r'.+',text,re.M)
print(match)