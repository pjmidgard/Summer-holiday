# @Author Jurijus Pacalovas
# User #Password #seach #find #block


username = input("Enter username:")
print("Username is: " + username)


# Python program to check validation of password 
# Module of regular expression is used with search() 

import re 

password = "R@m@_f0rtu9e$"

flag = 0

while True:   

    if (len(password)<8): 

        flag = -1

        break

    elif not re.search("[a-z]", password): 

        flag = -1

        break

    elif not re.search("[A-Z]", password): 

        flag = -1

        break

    elif not re.search("[0-9]", password): 

        flag = -1

        break

    elif not re.search("[_@$]", password): 

        flag = -1

        break

    elif re.search("\s", password): 

        flag = -1

        break

    else: 

        flag = 0

        print("Valid Password") 

        break

  

if flag ==-1: 

    print("Not a Valid Password") 



l, u, p, d = 0, 0, 0, 0

s = "R@m@_f0rtu9e$"

if (len(s) >= 8): 

    for i in s: 

  

        # counting lowercase alphabets  

        if (i.islower()): 

            l+=1            

  

        # counting uppercase alphabets 

        if (i.isupper()): 

            u+=1            

  

        # counting digits 

        if (i.isdigit()): 

            d+=1            

  

        # counting the mentioned special characters 

        if(i=='@'or i=='$' or i=='_'): 

            p+=1           

if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(s)): 

    print("Valid Password") 

else: 

    print("Invalid Password")


x = s.find("welcome")

print(x)


if username!=s:

    #### opening the video ####
    import subprocess
    import pyautogui
    import time

    subprocess.Popen(["C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",])
    time.sleep(3)
    pyautogui.write('www.youtube.com/watch?v=DLzxrzFCyOs', interval = 0.5)
    pyautogui.hotkey('enter')


    #### stops moving mouse to (1,0) after video has been opened
    executing = False

 
