name_1 = str(input("Enter frist name: "))
name_2 = str(input("Enter last name: "))
age = int(input("Enter age: "))
c_email = str(input("                                   create email: YES/NO = "))

if c_email == "NO":
    print("Ok")
else:
    if c_email == "YES":
            phon = int(input("Enter phon number in (09) = "))
            Pass_1 = int(input("Enter password: "))
            Pass_2 = int(input("config password: "))
            if Pass_2 != Pass_1:
                 print("password is not cracet try agen")
                 Pass_2 = int(input("config password: "))
                 if Pass_2 == Pass_1:
                      print("corect password")
            else:
                 if Pass_2 == Pass_1:
                      print("                                 chose_email")
                      print("1,",name_1,name_2,str(age),"@gmail.com")
                      print("2,",name_1,name_2,'1234@gmail.com')
                      print("3,",name_1,name_2,'1122@gmail.com')
                      print("4,",name_1,name_2,'0000@gmail.com')
                      print("5,",name_1,name_2,'592@gmail.com')
                      print("6,",name_1,name_2,'1037@gmail.com')
                      print("7,",name_1,name_2,'3850@gmail.com')
                      print("# = more")
                      ch_email = input(                  "chose_email: ")
                      if ch_email == "1":
                          print("proses is done")
                          print("your email is : ",name_1,name_2,age,"@gmail.com")
                          print("your pasword is", Pass_2)
                      elif ch_email == "2":
                          print("proses is done")
                          print("your email is : ",name_1,name_2,'1234@gmail.com')
                          print("your pasword is", Pass_2)
                      elif ch_email == "3":
                          print("proses is done")
                          print("your email is : ",name_1,name_2,'1122@gmail.com')
                          print("your pasword is", Pass_2)
                      elif ch_email == "4":
                          print("proses is done")
                          print("your email is : ",name_1,name_2,'0000@gmail.com')
                          print("your pasword is", Pass_2)
                      elif ch_email == "5":
                          print("proses is done")
                          print("your email is : ",name_1,name_2,'592@gmail.com')
                          print("your pasword is", Pass_2)
                      elif ch_email == "6":
                          print("proses is done")
                          print("your email is : ",name_1,name_2,'1037@gmail.com')
                          print("your pasword is", Pass_2)
                      elif ch_email == "7":
                          print("proses is done")
                          print("your email is : ",name_1,name_2,'3850@gmail.com')
                          print("your pasword is", Pass_2)
                      else:
                        if ch_email == "#":
                            ch_email_2 = input("Enter email: ")
                            print("proses is done")
                            print("your email is : ",ch_email_2,"@gmail.com")
                            print("your pasword is", Pass_2)