import re
import requests
import sys
#s='''
#<div class="book-cover">
#<a href="http://dimik.pub/book/475/coding-interview-preparation-problem-solution-by-tamim-shahriar-subeen"><img src="http://dimik.pub/wp-content/uploads/2020/01/codingInterview.png"></a>
#</div><!-- end .book-cover -->
#<div class="slide-description">
#<div class="inner-sd">
#<div class="top-sd-head clearfix">
#<div class="tsh-left">
#<h2 class="sd-title"><a href="http://dimik.pub/book/475/coding-interview-preparation-problem-solution-by-tamim-shahriar-subeen">কোডিং ইন্টারভিউ: প্রস্তুতি, সমস্যা ও সমাধান</a></h2>

#'''
#pattern=re.compile(r'<div class="book-cover">\s*<a href=(.*?)><img src=(.*?)>.*?<h2 class="sd-title"><a href=(.*?)>(.*?)<',re.S)
#matches=re.findall(pattern,s)
#for match in matches:
#    print(match)
url='http://dimik.pub'
response=requests.get(url)
if response.ok is False:
    sys.exit('could not generate response from server:')
page_content=response.text
pattern=re.compile(r'<div class="book-cover">\s*<a href=(.*?)><img src=(.*?)>.*?<h2 class="sd-title"><a href=.*?>(.*?)<',re.S)
result=re.findall(pattern,page_content)
#for item in result:
 #   print('Name:',item[2])
  #  print('Url:',item[0])
   # print('Image:',item[1])
    #print(' ')

