import re
#text_to_search='''
#321-555-4321
#123.555.1234
#123*555*1234
#'''

#text_to_search='''
#800.555.1234
#900-555.1234
#'''
text_to_search='''
cat
mat
bat
'''
#pattern=re.compile(r'\d{3}.\d{3}.\d{4}')
#pattern=re.compile(r'\d{3}[.-]\d{3}[.-]\d{4}')
#pattern=re.compile(r'\d{3}.\d{3}.\d{4}')
pattern=re.compile(r'[^b]at')
matches=pattern.finditer(text_to_search)
for match in matches:
    print(match)