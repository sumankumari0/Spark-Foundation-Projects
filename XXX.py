movies=[]
noview=[]
for i in range (4):
  x=input().split(", ")
  movies.append(x)
for i in range (4):
  x=input().split(" ")
  noview.append(x)
x=[]
sum=0
norm=int(input())
for i in range (4):
  z=(int(movies[i][2])/int(noview[i][0]))*norm
  x.append(z)
  sum+=z

mean=sum/4

for i in x:
  if i<mean:
    print(round(i-mean,4))