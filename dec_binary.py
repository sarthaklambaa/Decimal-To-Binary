dec_num = int(input("Enter the number: "))
list=[]
while dec_num!=0:
    remainder = dec_num%2
    list.append(remainder)
    dec_num=dec_num//2

empty_str = ""
for ans in list:
    new_str = str(ans)
    empty_str = new_str + empty_str
print(empty_str) 

