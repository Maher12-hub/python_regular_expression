import re
text='email your feedback here: maheribne12@gmail.com py.book@subeen.com'
result=re.findall(r'[\w\.]+@\w+\.\w+',text)
print(result)