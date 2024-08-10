def የ_አቦ_ሰም_ጨዋታ():
    print("                                                 የ_አቦ_ሰም_ጨዋታ")
    ቁልፍ = "አው"
    አስገባ = input("                                         ለጨዋታው_ዝግጁ_ነክ = አው/አይደለሁም: ")
    a = 0
    b = 1

    if አስገባ != ቁልፍ:
        if a < b:
            print("እሺ")
            a = a + 1
    else:
        print("")
        print("የጨዋታው_ህግ = ተጫዋች_አንድ: አንድ_አይነት")
        print("             ተጫዋች_ሁለት: ልዩ     ")
        print("")
        print("")
        print("             መዳፍ:  ቅ          ")
        print("             አይበሉባ:  ው        ")
        print("")
        print("")
        ኢንፑት = input("ተጫዋች_አንድ: ")
        ቁልፍ_1 = "ቅ"
        ቁልፍ_2 = "ው"
        q = 0
        w = 1

        if ኢንፑት in ቁልፍ_1:
            if q < w:
                q = q + 1
                print("")
                print("ቀጣይ")
                print("")
        else:
            if ኢንፑት in ቁልፍ_2:
                if q < w:
                    q = q + 1
                    print("")
                    print("ቀጣይ")
                    print("")
        ኢንፑት_1 = input("ተጫዋች_ሁለት: ")
        ቁልፍ_3 = "ቅ"
        ቁልፍ_4 = "ው"
        e = 0
        r = 1

        if ኢንፑት_1 in ቁልፍ_3:
            if e < r:
                e = e + 1
                print("")
                print("")
                print("ተጫዋች_አንድ = " + ኢንፑት)
                print("")
                print("ተጫዋች_ሁለት = " + ኢንፑት_1)
                print("")
                print("")

        else:
            if ኢንፑት_1 in ቁልፍ_4:
                if e < r:
                    e = e + 1
                    print("")
                    print("")
                    print("ተጫዋች_አንድ = " + ኢንፑት)
                    print("")
                    print("ተጫዋች_ሁለት = " + ኢንፑት_1)
                    print("")
                    print("")

        if ኢንፑት == ኢንፑት_1:
            print("                                              ተጫዋች_አንድ_አሸንፈዋል")
        else:
            if ኢንፑት != ኢንፑት_1:
                print("                                              ተጫዋች_ሁለት_አሸንፈዋል")



የ_አቦ_ሰም_ጨዋታ()
