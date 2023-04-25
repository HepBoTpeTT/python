def mail_cheker(email):
    symbols=0
    for i in range (len(email)):
        if email[i]=="@":
            symbols=i
            break
            
    if symbols==0:
        return False
    for i in range (symbols):
        if symbols>254 or symbols<5:
            return False
            
        if i==0 and (ord(email[i])>=48 and ord(email[i])<=57):
            return False
            
        if i==0 or i==symbols-1:
            if email[i]=="." or email[i]=="_" or email[i]=="-":
                return False
        
        if i>1 and ((email[i]=="." or email[i]=="_" or email[i]=="-") and (email[i-1]=="." or email[i-1]=="_" or email[i-1]=="-")):
            return False
                
        if (ord(email[i])>=48 and ord(email[i])<=57) or (ord(email[i])>=65 and ord(email[i])<=90) or (ord(email[i])>=97 and ord(email[i])<=122):
            return True
        else:
            return False
