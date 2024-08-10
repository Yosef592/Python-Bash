print("                                                            የመገመት ጨዋታ")
print("                                                      የጨዋታ ህግ = 5 እድል ለመገመት")
jo="አው"
yo=""
a=0
b=1
c=False
while yo!=jo and not(c):
    if a<b:
        yo=input("                                                  ለጨዋታው ዝግጁ ነህ/ሽ = አው/አይደለሁም: ")
        a=a+1
    else:
        c=True
if c:
    print("እሺ")
else:
    key = "እሺ"
    gas = " "
    gb=0
    gm=5
    gw=False

    while gas!=key and not (gw):
        if gb<gm:
            gas=input("ግምትክን/ሽን አስገባ/ቢ: ")
            gb=gb+1
        else:
            gw=True
    if gw:
        print("ግምቱን አላገኘህም/ሽም")
    else:
         print("ግምቱን አግኝተሀል/ሻል")

print("                                                  አዘጋጅ yosef alex  የተዘጋጀበት ቀን 7/24/2023")