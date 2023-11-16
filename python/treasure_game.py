row1 =["1","2","3"]
row2 =["7","6","5"]
row3 =["8","4","4"]
#list integration
m=[row1,row2,row3]
print(f"{row1}\n{row2}")
#getting input
pos=input("The number of position you want to treasure:")
#positioning by spilt,string to int 
hori=int(pos[0])
ver=int(pos[1])
#nameing  treasure place
m[hori-1][ver-1]="X"
print(f"{row1}\n{row2}")

