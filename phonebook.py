contact={}
print('''
  1.create new contact
  2.search contact
  3.display full contact list
  4.delete no.
  ''')
while True :
 choice=int(input("enter 1 to start"))
 if choice ==1:
     name=input("enter a name : ")
     number=int(input("enter number :"))

     contact[name]=number
     print(contact)
 elif choice==2:
    search_contact=input("enter a contact :")
    if search_contact in contact :
       print("your contact :",contact[name])
    else :
       print("number is not found ")
 elif choice==3:
    print("your contact list :",contact)
 elif choice==4:
    del_contact=input("enter your number to delete :")
    if del_contact in contact :
       print("do you want to delete no.")
       confirm=int(input("enter your choice :"))
       if confirm == 1:
        contact.pop(del_contact) 
        print("your no. is deleted")
       else:
          print("ok your no. is deleted.")
    else :
       print("your contact is not found")
  
 else:
    break    
    