import re
#text='book at subeen.com, book At subeen.com, book (at) subeen dot com, book [at] subeen [dot] com'

#result=re.sub(r'\s+[\(\[]*\s*at\s*[\)\]]*\s+','@',text,flags=re.I)
#result=re.sub(r'\s+[\(\[]*\s*dot\s*[\)\]]*','.',text,flags=re.I)
#print(result)
s='http://dimik.pub/book/400/becoming-a-problem-solver-by-munem-ruhul'
pattern=re.compile(r'book/(\d+)/(\w+)-(\w+)-(\w+)-(\w+)')
book_name=re.findall(pattern,s)
li1=book_name[0]
li=list(li1)
print('_'.join(li))