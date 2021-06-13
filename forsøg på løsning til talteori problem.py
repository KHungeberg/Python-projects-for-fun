# Matematisk problem i python. Vi har at for tallet 142857 så hvis man tager første ciffer fra venstre 
# og sætter de bagpå, så giver det præcis et tal som er 3 gange større. Hvad er det mindste tal som opfylder
# dette kriterie?
import numpy as np
import math as ma

# Tankegang til metode: Lad os definere en funktion som gør tallet til en string og omplacerer det første 
# ciffer. Herefter skal det fortolkes som et helttal, hvilket vi kan gøre med int(). 
# for at bytte om på tal er jeg nødt til at bruge mere en 1 ciffer og det kan jeg trygt da intet tal under 10
# opfylder kriteriet.  

# Når det er mindre så har vi at efter ombytningen skal tallet vi har, være lig med sig selv divideret med 3

# Vi definerer funktionen således: 
    #Vi vil gerne have et heltals input og et heltals output så derfor sørger vi for at få et heltal ud til 
    #sidst. Jeg har sagt at for vores input så skal den forvandle vores heltal til en string og derefter 
    # concatenere på måden som kriteriet er formuleret (første ciffer bagpå). 
    
def byt(x):
    return int(str(x)[1:len(str(x))]+str(x)[0])

k = 142857

print(byt(k)==3*k) # Tjekker at vores funktion virker. 

# Tanken er nu at jeg vil lave en meget stor liste. Umiddelbart vil jeg starte med 100.000 (10^5) pladser. 
# For hver plads i listen vil jeg indsætte 

for i in range(100000):
     if byt(i) == round(i/3):
         print(i)

løs = np.array([41,310,8275,620689,3103448])

bytløs = np.array([14,103,2758,206896,1034483])

print(løs-((bytløs)*3))