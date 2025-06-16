#Programa que gera a letra da canção muito popular entre os programadores: 99 bugs no software, pegue um deles e conserte... Tecle "CTRL+F5" 100 bugs no software, pegue um deles e conserte... Vamos fazer mais um café!

def cancao():
    for i in range(99, 251):
        print(f"{i} bugs no software, pegue um deles e conserte...")
        if i == 250:
            print(f'Tecle "Ctrl+F5"')
            print(f"Vamos fazer mais um café!")
        else:
            print(f'Tecle "Ctrl+F5"')
        
cancao()