import re
s='GET dsdsad.JpEg'
p=re.compile(r'GET .*\.(jpg|gif|png|bmp)$/i')
q =re.compile(r'(?i).*?\.jpg|.*\.gif|.*\.png|.*\.bmp|.*?\.jpeg')
a=re.findall(q,s)
print(a)