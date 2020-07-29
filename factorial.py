# num = int(input("Enter a number :"))
# factorial = 1
# for i in range (1, num+1):
#     factorial = factorial * i
# print("factorial is :" , factorial)
 # factorialแบบแรก   for loop 



# import functools
# num = int(input("Enter a number : "))
# lis = range(1,num+1)
# factorial = functools.reduce(lambda a,b: a*b , lis)
# print ("factorial is : " , factorial)
 #a คือ ค่าแรก b คือค่อต่อไป a*b และให้ a เก็บเป็นค่าปัจจุบัน แล้วทดไปตำแหน่งต่อไป เพื่อ * กับ b ต่อ 



# num = int(input( "enter :"))
# def re(n):
#     if n == 1:
#         return n
#     else :
#         return n * re(n-1)
# factorial = re(num)
# print("factorial is :" , factorial)
 #จะส่ง ลงมาเป็นทอดๆ เหมือนต้นไม้ และไล่กลับขึ้นไปเรื่อยจนถึง 1และ ส่งค่ารวมลงมา



# import math
# num = int(input("enter :"))
# factorial = math.factorial(num)
# print("factorial is : " , factorial )
 #ใช้ import math ดึงออกมา และ ใช้ factorial ที่มีให้อยู่แล้ว มาใช้เลย