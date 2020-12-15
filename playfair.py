import numpy as np
list1=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I','J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
list2=[]
jadval=[]
def encode():
    counter=0
    display=""
    text=str(input("enter text: "))
    next_before=int(input("next or before(1/2):"))
    numbers=int(input("How many number: "))
    text=text.upper()
    for x in text:
        if x==" ":
            continue
        else:
            list2.append(x)
    len_list2=len(list2)
    if len_list2%2!=0:
        len_list2-=1
    for x in range(0,len_list2,2):
        if list2[x]==list2[x+1]:
            counter+=1
    len_list2=len(list2)+counter
    if len_list2%2!=0:
        list2.append("X")
    for x in range(0,len_list2,2):
        if list2[x]=="J" and "J" not in jadval:
            list2[x]="I"
        if list2[x]=="I" and "I" not in jadval:
            list2[x]="J"
        if list2[x+1]=="J" and "J" not in jadval:
            list2[x+1]="I"
        if list2[x+1]=="I" and "I" not in jadval:
            list2[x+1]="J"
        if list2[x]!=list2[x+1]:
            z=np.where(arr==list2[x])
            satrz=z[0][0]
            stonz=z[1][0]
            if satrz+numbers>4:
                satrz-=5
            if stonz+numbers>4:
                stonz-=5
            z1=np.where(arr==list2[x+1])
            satrz1=z1[0][0]
            stonz1=z1[1][0]
            if satrz1+numbers>4:
                satrz1-=5
            if stonz1+numbers>4:
                stonz1-=5
            if z[0][0]==z1[0][0]:
                if next_before==1:
                    display=display+" "+arr[satrz][stonz+numbers]+arr[satrz1][stonz1+numbers]
                    
                else:
                    display=display+" "+arr[satrz][stonz-numbers]+arr[satrz1][stonz1-numbers]
            elif z[1][0]==z1[1][0]:
                if next_before==1:
                    display=display+" "+arr[satrz+numbers][stonz]+arr[satrz1+numbers][stonz1]
                else:
                    display=display+" "+arr[satrz-numbers][stonz]+arr[satrz1-numbers][stonz1]
            else:
                display=display+" "+arr[satrz][stonz1]+arr[satrz1][stonz]
        else:
            list2.insert(x+1,"X")
            z=np.where(arr==list2[x])
            satrz=z[0][0]
            stonz=z[1][0]
            if satrz+numbers>4:
                satrz-=5
            if stonz+numbers>4:
                stonz-=5
            z1=np.where(arr==list2[x+1])
            satrz1=z1[0][0]
            stonz1=z1[1][0]
            if satrz1+numbers>4:
                satrz1-=5
            if stonz1+numbers>4:
                stonz1-=5
            if z[0][0]==z1[0][0]:
                if next_before==1:
                    display=display+" "+arr[satrz][stonz+numbers]+arr[satrz1][stonz1+numbers]
                else:
                    display=display+" "+arr[satrz][stonz-numbers]+arr[satrz1][stonz1-numbers]
            elif z[1][0]==z1[1][0]:
                if next_before==1:
                    display=display+" "+arr[satrz+numbers][stonz]+arr[satrz1+numbers][stonz1]
                else:
                    display=display+" "+arr[satrz-numbers][stonz]+arr[satrz1-numbers][stonz1]
            else:
                display=display+" "+arr[satrz][stonz1]+arr[satrz1][stonz]
    print(display)
def decode():
    display=""
    text=str(input("enter text: "))
    next_before=int(input("next or before(1/2):"))
    numbers=int(input("How many: "))
    text=text.upper()
    for x in text:
        if x==" ":
            continue
        else:
            list2.append(x)
    len_list2=len(list2)
    for x in range(0,len_list2,2):
        if list2[x]=="J" and "J" not in jadval:
            list2[x]="I"
        if list2[x]=="I" and "I" not in jadval:
            list2[x]="J"
        if list2[x+1]=="J" and "J" not in jadval:
            list2[x+1]="I"
        if list2[x+1]=="I" and "I" not in jadval:
            list2[x+1]="J"
        if list2[x]!=list2[x+1]:
            z=np.where(arr==list2[x])
            satrz=z[0][0]
            stonz=z[1][0]
            if satrz+numbers>4:
                satrz-=5
            if stonz+numbers>4:
                stonz-=5
            z1=np.where(arr==list2[x+1])
            satrz1=z1[0][0]
            stonz1=z1[1][0]
            if satrz1+numbers>4:
                satrz1-=5
            if stonz1+numbers>4:
                stonz1-=5
            if z[0][0]==z1[0][0]:
                if next_before==2:
                    display=display+arr[satrz][stonz+numbers]+arr[satrz1][stonz1+numbers]
                    
                else:
                    display=display+arr[satrz][stonz-numbers]+arr[satrz1][stonz1-numbers]
            elif z[1][0]==z1[1][0]:
                if next_before==2:
                    display=display+arr[satrz+numbers][stonz]+arr[satrz1+numbers][stonz1]
                else:
                    display=display+arr[satrz-numbers][stonz]+arr[satrz1-numbers][stonz1]
            else:
                display=display+arr[satrz][stonz1]+arr[satrz1][stonz]
        else:
            list2.insert(x+1,"X")
            z=np.where(arr==list2[x])
            satrz=z[0][0]
            stonz=z[1][0]
            if satrz+numbers>4:
                satrz-=5
            if stonz+numbers>4:
                stonz-=5
            z1=np.where(arr==list2[x+1])
            satrz1=z1[0][0]
            stonz1=z1[1][0]
            if satrz1+numbers>4:
                satrz1-=5
            if stonz1+numbers>4:
                stonz1-=5
            if z[0][0]==z1[0][0]:
                if next_before==2:
                    display=display+arr[satrz][stonz+numbers]+arr[satrz1][stonz1+numbers]
                else:
                    display=display+arr[satrz][stonz-numbers]+arr[satrz1][stonz1-numbers]
            elif z[1][0]==z1[1][0]:
                if next_before==2:
                    display=display+arr[satrz+numbers][stonz]+arr[satrz1+numbers][stonz1]
                else:
                    display=display+arr[satrz-numbers][stonz]+arr[satrz1-numbers][stonz1]
            else:
                display=display+arr[satrz][stonz1]+arr[satrz1][stonz]
    print(display)
while True:
    ramz=int(input("encode or decode (1/2): "))
    key_word=input("Enter Key word: ")
    key_word=key_word.upper()
    for x in key_word:
        if x==" ":
            continue
        elif x=="I" or x=="J":
            if "I" not in jadval and "J" not in jadval:
                jadval.append(x)
        elif x not in jadval:
                jadval.append(x)
    for y in list1:
        if y=="I" or y=="J":
            if "I" not in jadval and "J" not in jadval:
                jadval.append(y)
        elif y not in jadval:
            jadval.append(y)
    arr=np.array(jadval)
    arr=arr.reshape(5,5)
    print(arr)
    if ramz==1:
        encode()
    else:
        decode()
    question=input("do you want continue(n/y): ")
    if question=="n":
        break
    else:
        list2=[]
        jadval=[]
        continue