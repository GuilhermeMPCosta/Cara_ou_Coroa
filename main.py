import random

vetor=["Cara","Coroa"]
x="1" 
player=bot=0
while x=="1":
    truelado="".join(random.choice(vetor))
    lado=input('Cara ou Coroa:')
    if lado.upper() == truelado.upper() :
        print("Voce ganhou")
        player+=1
        x=input("Digite 1 para contnuar jogando ou 0 para sair: ")
    else:
        print("Voce perdeu")
        bot+=1
        x=input("Digite 1 para contnuar jogando ou 0 para sair: ")
    if x=="1":
        print("==============Placar==============")
        print("Player: {0}".format(player))
        print("Adversario: {0}".format(bot))
        print("==================================")
        if x==10:
            x=1
    else:
        exit        
print("Player: {0}".format(player))
print("Adversario: {0}".format(bot))
print("Saindo do jogo")    