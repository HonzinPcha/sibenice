import random
import sys
from tisk_sibenice import tisk_hlavicky, tisk_faze_sibenice

def vyber_slovo(seznam_slov):
   return random.choice(seznam_slov)

def inicializace_pole(pismeno):
   return ["_" for _ in range(len(pismeno))]

def vypis_pole(pole):
   for znak in pole:
       print(znak, end=" ")
   print()

def hra():
   seznam_slov = ["praxe", "pocitac", "programovani", "soue", "it"]
   slovo = vyber_slovo(seznam_slov)
   pole = inicializace_pole(slovo)
   pocet_chyb = 0
   hadane_pismeno = ""

   tisk_hlavicky()
   vypis_pole(pole)

   while "_" in pole and pocet_chyb < 6:
       hadane_pismeno = input("Hádej písmeno: ").lower()

       if hadane_pismeno.isalpha() and len(hadane_pismeno) == 1:
           if hadane_pismeno in slovo:
               for i in range(len(slovo)):
                   if slovo[i] == hadane_pismeno:
                       pole[i] = hadane_pismeno
           else:
               pocet_chyb += 1

           tisk_hlavicky()
           tisk_faze_sibenice(pocet_chyb)
           vypis_pole(pole)
       else:
           print("Zadej jedno platné písmeno!")

   if "_" not in pole:
       print("Gratuluji, uhodl(a) jsi slovo!")
   else:
       print("Bohužel jsi prohrál(a). Hledané slovo bylo:", slovo)

   nova_hra = input("Chceš začít novou hru? (ano/ne): ").lower()
   if nova_hra == "ano":
       hra()
   else:
       sys.exit(0)

if __name__ == "__main__":
   hra()