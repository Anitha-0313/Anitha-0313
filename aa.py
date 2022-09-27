#string Pailndrome
n=input()
s=n[::-1]
if(n==s):
    print("String Palindrome",s)
else:
    print("Not String Palindrome",s)

print("=================================================")
# check vowels or not
sen=input()
vow=[]
no=[]
for word in sen:
   if word=='a' or word=='e'or word=='i'or word=='o'or word=='u':
       word.strip()
       vow.append(word)
   else:
       word.strip()
       no.append(word)
print("these are vowels",*vow)
print("these are not vowels",*no)
print("========================================")
#how many capitals and smalls
word=input()
cap=[]
sml=[]
for i in word:
    if(i.isupper()):
        i.strip()
        cap.append(i)  
    else:
        i.strip()
        sml.append(i)
        
print("Capital Letters",*cap)
print("Small Letters",*sml)
print("=================================")
#Count  words in a Sentence
sen=input()
letters=0
digits=0
spaces=0
spl=0
for i in sen:
  if(i.isalpha()):
    letters=letters+1
  elif(i.isdigit()):
      digits=digits+1
  elif(i.isspace()):
      spaces=spaces+1
  else:
      spl=spl+1
print(letters)
print(digits)
print(spaces)
print(spl)
      

