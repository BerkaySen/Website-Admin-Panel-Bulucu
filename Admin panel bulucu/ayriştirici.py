mvct = open("admin_liste.txt","r")
eklnck=open("eklenecekler.txt","r")
eklenecek = ("eklenecekler.txt","w")

for i in mvct:
    print(i)
    for c in eklenecek:
        if(i == c):
            print(c)
            eklnck