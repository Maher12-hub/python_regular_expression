import re
s='<li>Tamim</li><li>Shakib</li><li>Mahmudullah</li><li>Mominul</li>'
match=re.findall(r'<li>([\w]+)</li>',s)
print(match)