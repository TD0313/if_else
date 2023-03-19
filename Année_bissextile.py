age = int(input("Quel age avez vous ?"))

if age < 18 :
    prix_total = 7
else :
    prix_total = 12

popcorn = int(input("Souhaitez vous du popcorn ? (oui,non)"))

if popcorn == "oui":
    prix_total += 5

print ("Vous devez payer",prix_total,"euros")