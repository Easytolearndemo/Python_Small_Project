sum=0
while(True):
  n=input("Enter the price:")
  if(n!='q'):
    sum=sum+int(n)
    print(f"Amount:{sum}")

  else:
    print(f"your total amount{sum}.Thanks for comming")
    break
