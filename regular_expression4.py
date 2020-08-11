import re
text_to_search='''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov

'''
pattern=re.compile(r'http(s)?[://]*[\w.]+\.\w+')
matches=pattern.finditer(text_to_search)
for match in matches:
    print(match)
