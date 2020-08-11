import re
text='''
this is line 1.date is 2017/06/01.and there is another date :2017-07-01. the
third and final date is 2017/08/30.
'''
pattern=re.compile(r'\d{4}[/-]\d{2}[/-]\d{2}')
matches=pattern.findall(text)
print(matches)