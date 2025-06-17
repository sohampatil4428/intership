i=0
mark=[]
for i in range (0,5):
    p=int(input(f"enter the mark{i+1}:"))
    if i<0 or i>100:
        print("invalid mark")
    mark.append(p)

fail=0
for m in mark:
    if m<40:
        fail+=1
if fail>2:
    print(f"fail")
elif fail>0:
    print("ATKT")
else:
    print("pass")
    sum=sum(mark)
    print(f"sum :{sum}")
    per=sum/5
    print(f"per :{per}")
    if per >= 75:
        print("a+")
    elif per >=90:
        print("b+")
    else:
        print("c+")


    



