import re
import requests
import sys
import os

def create_directory(name):
    print('creating directory',name)
    try:
        os.mkdir(name)
    except FileExistsError:
        print(name,'already exhists')
def downloading_image(file_name,img_url):
    print('Downloading image',img_url)
    response=requests.get(img_url)
    with open(file_name,'wb',encoding=response.encoding) as wf:
        wf.write(response.content)
def get_directory_name(regexp,url):
    book_name=re.findall(regexp,url)
    li1=book_name[0]
    li=list(li1)
    dir_name='_'.join(li)
    return dir_name
def process():
    main_dir='dimik_pub'
    create_directory(main_dir)
    url='http://dimik.pub'
    response=requests.get(url)
    if response.ok is False:
        sys.exit('not responding:')
    page_content=response.text
    regexp=re.compile(r'<div class="book-cover">\s*<a href=(.*?)><img src=(.*?)>.*?<h2 class="sd-title"><a href=.*?>(.*?)<',re.S)
    result=re.findall(regexp,page_content)
    dir_regexp=re.compile(r'book/(\d+)/(\w+)-(\w+)-')
    for item in result:
        
        url=item[0]
        img_url=item[1]
        dir_name=main_dir+'/'+get_directory_name(dir_regexp,url)
        create_directory(dir_name)
        file_name=dir_name+'/'+'info.txt'
        with open(file_name,'w') as wf:
            #wf.write(name)
            print('\n')
            wf.write(url)
        img_file_name=dir_name+'/'+'image.png'
        downloading_image(img_file_name,img_url)
if __name__=='__main__':
        process()
           