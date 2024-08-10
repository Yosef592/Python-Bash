ኮድ = input("ኮዶን ያስገቡ: ")
አትም = input("ምን ላትም: ")
መቀጠል = input("ይቀጥላሉ: ")

if ኮድ == "አትም":
    if መቀጠል == "አይ":
        print("                                   መልስ")
        print(" ")
        print(አትም)
    else:
        if መቀጠል == "አው":
            አትም1 = input("ምን ላትም: ")
            መቀጠል1 = input("ይቀጥላሉ: ")
        if መቀጠል1 == "አይ":
            print("                               መልስ")
            print(" ")
            print(አትም)
            print(አትም1)
        else:
            if መቀጠል == "አው":
                አትም2 = input("ምን ላትም: ")
                መቀጠል2 = input("ይቀጥላሉ: ")
            if መቀጠል2 == "አይ":
                print("                               መልስ")
                print(" ")
                print(አትም)
                print(አትም1)
                print(አትም2)
            else:
                if መቀጠል == "አው":
                    አትም3 = input("ምን ላትም: ")
                    መቀጠል = input("ይቀጥላሉ: ")
                if መቀጠል == "አይ":
                    print("                                     መልስ")
                    print(" ")
                    print(አትም)
                    print(አትም1)
                    print(አትም2)
                    print(አትም3)
