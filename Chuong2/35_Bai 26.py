a=input("Ho ten: ")
b=int(input("So ngay cong: "))
c=int(input("Don gia ngay cong: "))
d=float(input("He so phu cap: "))
e=int(input('Tam ung: '))
print("Nhan vien "+a+",",end="")
m=round(c*b*d,1)
print(" Co tien luong=",m,sep="",end="")
print(", Tam ung="+str(int(e))+" va Thuc linh=",round(m-e,1),sep="")