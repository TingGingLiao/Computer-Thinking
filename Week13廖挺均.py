a=range(10)
print(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9])
b=range(0,10,2)
print(b[0],b[1],b[2],b[3],b[4])
c=range(5,11,2)
print(c[0],c[1],c[2])
d=range(0,-10,-1)
print(d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7],d[8],d[9])
for i in range(0,-10,-1):
    print(i)
for i in range(5):
    print("Hello")
sum=0
for i in range(0,11,2):
    sum=sum+i
print("Total is",sum)
sum=0
for i in range(3,13,3):
    sum=sum+i
print("Total is",sum)
project_title="對話機器人"
name_list=["廖挺均","黃鑫凱","陳霆維","郭星暘","張宗啓","李世杰"]
number_list=["A109260024","A109260006","A109260014","A109260016","A109260032","A109260066"]
duty_list=["撰寫程式","構思對話內容","操作並報告"]
load_list=["20%","15%","15%","15%","15%","15%"]
print(name_list[0])
print(number_list[0])
print(duty_list[0:2])
print(load_list[0])