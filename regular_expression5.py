s='Afganistan,America,Bangladesh,Canada,Denmark,England,Greenland,Iceland,Netherlands,New Zealand,Sweden,Switzerland'
#Country_list=list(s.split(','))
#country=[]
#for country_name in Country_list:
 #   if country_name.endswith('land') or country_name.endswith('lands'):
  #      country.append(country_name)
#print(country)
import re
li=re.findall(r'(\w+lands*)',s)
print(li)