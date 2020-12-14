start=int(input("請輸入加總開始值?"))
end=int(input("請輸入加總終止值?"))
step=int(input("請輸入遞增值?"))
sum=0
for i in range(start,end,step):
    sum=sum+i
    print("i為",i,"時，累加結果為",sum)
cars = ["Toyata", "Honda"]
for i in cars:
    print(i)
names = ["Allen", "James", "Tom", "Jack"]
for i in names:
    print("Welcome to class!",i)
sheet=["牛奶","蛋","咖啡豆"]
for i in range(0,len(sheet)):
    print(i,sheet[i])
numbers = [123, 456, 789]
for i in numbers:
    print(i)
numbers = [123, 456, 789]
for i in range(0, len(numbers)):
    print(i, numbers[i])
for i in range(1,10):
    for j in range(1,10):
        print(i, '*', j, '=', i*j, '\t', sep='',end='')

names = ["廖挺均", "黃鑫凱", "郭星暘", "陳霆維","張宗棨","李世杰"]
dessert = ["巧克力", "抹茶", "芋頭蛋糕", "紅茶", "鬆餅", "奶凍捲"]
for i in range(len(names)):
    print("Hi,my name is",names[i],".My favorite dessert is",dessert[i])
    
start=int(input("請輸入加總開始值?"))
end=int(input("請輸入加總終止值?"))
step=int(input("請輸入遞增值?"))
sum=0
for i in range(start,end,step):
    sum=i*i
    print("i為",i,"時，累加結果為",sum)