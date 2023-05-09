import re
text='''#BED
{
    color: #FfFdF8; background-color:#aef;
    font-size: 123px;
    background: -webkit-linear-gradient(top, #f9f9f9, #fff);
}
#Cab
{
    background-color: #ABC;
    border: 2px dashed #fff;
}'''

regex='#{1}[0-9A-Fa-f]{3,6}[;,)]{1}'

p= re.compile(regex)

x=re.findall(p,text)

for i in x:
    print(i.strip(",;)"))






