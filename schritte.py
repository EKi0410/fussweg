import time


print("-----------------"); time.sleep(0.5)
print("|  Willkommen!  |"); time.sleep(0.5)
print("-----------------\n\n"); time.sleep(0.5)
time.sleep(1)

#Variablen
#Faktor 1= <194cm
#Faktor 2= >194cm 
#Schrittweite = (Schritte x Schrittlänge) / 100
#Erdumfang 40k km
körpergroße=input
faktor1=0.45
faktor2=0.47
play="y"

while play=="y":

 print("\n\n")
 print("|Bitte gebe die geforderten Angaben ein|\n\n"); time.sleep(0.5)


 körpergroße=eval(input("Deine Körpergröße in CM ->  "))
 print("\n\n")

 if körpergroße<194:
  schrittlange=körpergroße*faktor1
 else: schrittlange=körpergroße*faktor2

 alter=eval(input("Dein Alter ->  ")); time.sleep(0.5)
 print("\n\n")

 aktivitat=input("Hast du einen Bürojob? y/n ->  "); time.sleep(0.5)
 print("\n\n")


 if aktivitat=="y":
  schritte= 6000
 else: schritte= 2500

 schrittweite=(schritte*schrittlange)/100

 altermonate=alter*12

 Erdumrundungen=(schrittweite*altermonate)/40000

 print("---------------------"); time.sleep(0.5)
 print("|  Deine Statistik  |"); time.sleep(0.5)
 print("---------------------\n\n"); time.sleep(0.5)


 print(f"Deine Körpergröße: {körpergroße} cm \n"); time.sleep(0.5)
 print(f"Dein Alter: {alter} Jahre \n"); time.sleep(0.5)
 print(f"Deine Schrittlänge: ~{schrittlange} cm \n"); time.sleep(0.5)
 print(f"Schritte pro Tag: ~{schritte} \n"); time.sleep(0.5)
 print(f"Schritte letztes Jahr: ~{schritte*12} \n"); time.sleep(0.5)
 print(f"Kilometer letztes Jahr: ~{schrittweite*12} km \n")
 print(f"Schritte Gesamt: ~{schritte*altermonate} \n"); time.sleep(0.5)
 print(f"Kilometer Gesamt: ~{schrittweite*altermonate} km \n"); time.sleep(0.5)
 print(f"Erdumrundungen: ~{Erdumrundungen}x \n\n"); time.sleep(0.5)

 play=input("Möchtest du das Programm erneut starten? [Y] [N] ->  ")



