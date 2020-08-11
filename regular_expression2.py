import re
#text_to_search='''
#Mr. Schafer
#Mr Smith
#Ms Davis
#Mrs. Robinson
#Mr. T
#'''
text_to_search='''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net

'''
#pattern=re.compile(r'Mr\.?\s\w*')
#pattern=re.compile(r'M[rs]*(rs)?\.?\s\w*')
#pattern=re.compile(r'M(rs)\.\s\w*')
#pattern=re.compile(r'\w*\d*[.-]*\@*\w*[-]?\.\w*')
#pattern=re.compile(r'[\w.-]+@[\w -]+\.\w+')
pattern=re.compile(r'\w+-\d+-\w+@\w+-\w+\.\w+')
matches=pattern.finditer(text_to_search)
for match in matches:
    print(match)
