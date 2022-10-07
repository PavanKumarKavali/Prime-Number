def prime(n):
  i=1
  count=0
  while(i<=n):
    if n%i==0:
      count+=1
  if count==2:
    print(n,"is Prime")
  else:
    print(n,"is not Prime")

n=int(input("Enter a Number:"))
prime(n)
