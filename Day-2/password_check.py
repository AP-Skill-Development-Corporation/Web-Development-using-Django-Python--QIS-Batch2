password = input("Enter Password:")
chars = 0
spe_char=0
num = 0
for char in password:
    if char.isalpha():
        chars = chars+1
    elif char.isnumeric():
        num = num+1
    else:
        spe_char +=1
#print('chars',chars,'spe',spe_char,'num',num)
if chars>=1 and spe_char>=1 and num>=1 and len(password)>=5:
    print("valid password")
else:
    print("invalid password try again")
