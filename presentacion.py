import random

name = ''
age = None
n = 0
invitar = None
edadRes = ["Enseriate vale!", "Dame un numero!", "NU-ME_RO"]
mayo18 = ["Puedo confier en que me dices la verad", "No se... Tienes cara como de bebé", "Seguro seguro que puedes venir a este sitio???", "No tendras que pedirle permiso a tu mama verdad?", "Creo que esta CI es falsa"]


input()
print("Como te llamas?")
name = input()
print(f"Hola {name}, un placer conocerte!")
input()



while(True):

    print("Debo pedirte porfavor que me digas tu edad")

    try:
        age = input()
        age = int(age)
        if(age < 18):
            print("No permitimos bebes en este establecimiento")
            print("Adios")
            input()
            print("..... ok esto no pasó, regresemos en el tiempo....")
            input()

        else:
            while(n < 3):
                input()
                i = random.randint(0, len(mayo18))
                print(mayo18[i])
                print(f'Que respondes {name}?')
                n = n + 1
                print(n)
            break

    except:
        n = random.randint(0, 2)
        print(edadRes[n])
        print()





print("'Se te hacerca una persona'")
input()
print("'No seas boleta disimula.....'")
input()
print("Hola!")
input()
print("Me invitas algo?")


while(True):
    invitar = input()
    respuestas = ["Yes", "yes", "si", "Si", "s", "No", "no", "n"]
    r = invitar in respuestas
    if (r == False):
        print("No te quedes con la boca abierta!\nDecidete y dile!!!!")
    else:
        break

if(respuestas != "No" or respuestas != "no" or respuestas !="n"):
    print("Y dicen que no quedan personas amables en el mundo!")
    input()
    print("Y hay alguien especial en tu vida???")
else:
    print("Que lastima vale!")
    input()
    print("Será que hay alguien especial por ahí")


alguien_especial = input


while(True):
    alguien_especial = ["Yes", "yes", "si", "Si", "s", "No", "no", "n"]
    if (invitar in respuestas == False):
        print("Haaaa pues! Que te cuesta responder 'si' o 'no'")
    else:
        break