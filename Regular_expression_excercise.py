import re
s='''
<ul>
<li>
Australia
<ol>
<li>Steven Smith</li>
<li>David warner</li>
</ol>
</li>   
<li>
Bangladesh
<ol>
<li>Mashrafe Mortaza</li>
<li>Tamim Iqbal</li>
</ol>
</li>
<li>
England
<ol>
<li>Eoin Morgan</li>
<li>Jos buttler</li>
</ol>
</li>
</ul>
'''
pattern=re.compile(r'.*?<li>\s*(.*?)\s*<ol>\s*<li>(.*?)</li>\s*<li>(.*?)</li>.*?</li>',re.S)
matches=re.findall(pattern,s)
country=[]
player_name=[]
for match in matches:
     for a in range(len(match)):
         if a==0:
             country.append(match[0])
        
         elif a>0:
            player_name.append(match[a])
print('{} - {},{}'.format(country[0],player_name[0],player_name[1]))
print('{} - {},{}'.format(country[1],player_name[2],player_name[3]))
print('{} - {},{}'.format(country[2],player_name[4],player_name[5]))
