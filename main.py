def main():
  a=print("Choose Number \n1:- Add \n2:- Substract \n3:- Multiply \n4:- Divide \n5:- Exit")
  i=int(input("Enter Your Choice :- "))
  if i==1:
    f=int(input("First Value :- "))
    l=int(input("Second Value :- "))
    print(f+l,"This Is Answer Of Your problem :)")
    main()
  elif i==2:
    f=int(input("First Value :- "))
    l=int(input("Second Value :- "))
    print(f-l,"This Is Answer Of Your problem :)")
    main()
  elif i==3:
    f=int(input("First Value :- "))
    l=int(input("Second Value :- "))
    print(f*l,"This Is Answer Of Your problem :)")
    main()
  elif i==4:
    f=int(input("First Value :- "))
    l=int(input("Second Value :- "))
    print(f/l,"This Is Answer Of Your problem :)")
    main()
  elif i==5:
    print("Exit")
    exit
  else:
    print("Invalid Choice Make Sure You Enter Correct Choice From Give Above :( ")
main()