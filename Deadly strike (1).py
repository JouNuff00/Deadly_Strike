print('\nSEJA BEM-VINDO AO DEADLY STRIKE!\nESCOLHA OS ATRIBUTOS A SEGUIR PARA CADA PERSONAGEM:\n')
armas = [
    {'arma': 'Espada da Vingança', 'dano': 5},
    {'arma': 'Lâmina da Caos', 'dano': 7},
    {'arma': 'Espada do Sacrifício', 'dano': 6}, 
    {'arma': 'Martelo da Justiça', 'dano': 12},
    {'arma': 'Machado do Abismo', 'dano': 9}, 
    {'arma': 'Foice do Esquecimento', 'dano': 7},
    {'arma': 'Lança da Ruína', 'dano': 10}, 
    {'arma': 'Foice da Morte', 'dano': 14}
]

armaduras = [
    {'armadura': 'Armadura do Dragão Negro', 'PV': 20},
    {'armadura': 'Armadura da Vingança', 'PV': 25},
    {'armadura': 'Couraça do Guerreiro Fantasma', 'PV': 30},
    {'armadura': 'Armadura do Guardião da Fortaleza', 'PV': 45},
    {'armadura': 'Armadura da Escuridão Eterna', 'PV': 25},
    {'armadura': 'Armadura do Cavaleiro da Lua Negra', 'PV': 35},
    {'armadura': 'Armadura de Ferro', 'PV': 40},
    {'armadura': 'Armadura da Sentinela Celestial', 'PV': 100}
]

classes = [
    {'classe': 'Guerreiro' , 'habilidade': 'Impulso de fúria', 'descrição': 'Ataque único e poderoso que tira causa 35 pontos de dano. O uso é perdido se o usuário não acertar o ataque.'},
    {'classe': 'Mago', 'habilidade': 'Escudo mágico', 'descrição': 'É escudo protetor que envolve o jogador deixando-o imune ataques e precisa ser atingido 3 vezes para ser quebrado.'},
    {'classe': 'Samurai', 'habilidade': 'Katana sangrenta' , 'descrição': 'Imbui a arma com sangue, dobrando o poder de ataque nos próximos 5 golpes, o uso de cada golpe é perdido se o usuário não acertar o ataque.'},
    {'classe': 'Sacerdote', 'habilidade': 'Cura Milagrosa', 'descrição': 'Cura 1/3 dos pontos de vida.'}
]

  
def impulso(dano,habilidade_do_jogador):
    dano = 35
    habilidade_do_jogador = False
    return dano,habilidade_do_jogador


def escudo(dano,golpes_adversario,jogador,atacante,rodada,rodada_da_habilidade,habilidade_do_jogador):
    
    if rodada > rodada_da_habilidade and jogador != atacante:
        golpes_adversario += 1   

    if golpes_adversario<3:
        dano = 0
    else:
        habilidade_do_jogador = False
    return dano,golpes_adversario,habilidade_do_jogador
    
def katana(dano,rodada,rodada_da_habilidade,habilidade_do_jogador):
    if rodada < rodada_da_habilidade + 5:
        dano = 2*dano       
    else:
        habilidade_do_jogador = False
    return dano,habilidade_do_jogador
        
               
def cura(pv_inicial,pv,habilidade_do_jogador):
    if pv + pv_inicial/3 > pv_inicial:
       pv = pv_inicial
    else:
        pv += pv_inicial/3
    pv = round(pv)
    habilidade_do_jogador = False
    return pv,habilidade_do_jogador

import random

# solicita a escolha das armas e armaduras dos jogadores

print('\nARMAS DISPONÍVEIS  /  DANO  :\n')

for i in range(len(armas)):
    arma = armas[i]['arma']
    dano = armas[i]['dano']
    print(f'[{i}]   {arma}:  {dano}')


print('\n\nARMADURAS DISPONÍVEIS  /  PV  :\n')

for i in range(len(armaduras)):
    armadura = armaduras[i]['armadura']
    pv = armaduras[i]['PV']
    print(f'[{i}]   {armadura}:  +{pv}')


print('\n\nCLASSES DISPONÍVEIS  /  HABILIDADE  :\n')

for i in range(len(classes)):
    classe = classes[i]['classe']
    habilidade = classes[i]['habilidade']
    descrição = classes[i]['descrição']
    print(f'[{i}]   {classe}: {habilidade} - {descrição}')



#Atributos de cada jogador

#Jogador 1
arma_jogador1 = int(input("\nSelecione a arma do jogador 1: "))
forca_jogador1 = armas[arma_jogador1]['dano']

armadura_jogador1 = int(input("Selecione a armadura do jogador 1: "))
pv_inicial_jogador1 = 100 + armaduras[armadura_jogador1]['PV']

classe_jogador1 = int(input("Selecione a classe do jogador 1: "))
habilidade_jogador1 = classes[classe_jogador1]['habilidade']
classe_jogador1 = classes[classe_jogador1]['classe']



#Jogador 2
arma_jogador2 = int(input("\nSelecione a arma do jogador 2: "))
forca_jogador2 = armas[arma_jogador2]['dano']

armadura_jogador2 = int(input("Selecione a armadura do jogador 2: "))
pv_inicial_jogador2 = 100 + armaduras[armadura_jogador2]['PV']

classe_jogador2 = int(input("Selecione a classe do jogador 2: "))
habilidade_jogador2 = classes[classe_jogador2]['habilidade']
classe_jogador2 = classes[classe_jogador2]['classe']


#While para rounds
vitorias_jogador1 = 0
vitorias_jogador2 = 0
_round = 1


while vitorias_jogador1 < 2 and vitorias_jogador2 < 2:

    print(f'\n***************ROUND {_round}*****************\n')

    # define a ordem de ataque dos jogadores
    ordem_ataque = [1, 2]

    #Conta os golpes para ativar as habilidades
    golpes_jogador1 = 0
    ativar_habilidade_jogador1 = False
    golpes_jogador2 = 0
    ativar_habilidade_jogador2 = False

    # inicia a partida
    pv_jogador1 = pv_inicial_jogador1
    pv_jogador2 = pv_inicial_jogador2
    rodada = 1

    while pv_jogador1 > 0 and pv_jogador2 > 0:
        print(f'\nRodada {rodada}:')

        dano_jogador1 = forca_jogador1
        dano_jogador2 = forca_jogador2

        #Verifica se  a habildade pode ser ativada
        if golpes_jogador1 == 10:
            ativar_habilidade_jogador1 = True
            golpes_jogador1 = 0
            print(f'\nO Jogador 1 ativou sua habilidade especial de {classe_jogador1}, {habilidade_jogador1}.')
            rodada_da_habilidade_jogador1 = rodada
        elif golpes_jogador2 == 10:
            ativar_habilidade_jogador2 = True
            golpes_jogador2 = 0
            rodada_da_habilidade_jogador2 = rodada
            print(f'\nO Jogador 2 ativou sua habilidade especial de {classe_jogador2}, {habilidade_jogador2}.')

        if ativar_habilidade_jogador1 == True:

            if classe_jogador1 == 'Guerreiro':
                dano_jogador1,ativar_habilidade_jogador1 = impulso(dano_jogador1,ativar_habilidade_jogador1)
            elif classe_jogador1 == 'Mago':
                if rodada == rodada_da_habilidade_jogador1:
                    contador_de_golpes1 = 0
                dano_jogador2,contador_de_golpes1,ativar_habilidade_jogador1 = escudo(dano_jogador2,contador_de_golpes1,1,atacante,rodada,rodada_da_habilidade_jogador1,ativar_habilidade_jogador1)
            elif classe_jogador1 == 'Samurai':
                dano_jogador1,ativar_habilidade_jogador1 = katana(dano_jogador1,rodada,rodada_da_habilidade_jogador1,ativar_habilidade_jogador1)
            elif classe_jogador1 == 'Sacerdote':
                pv_jogador1,ativar_habilidade_jogador1 = cura(pv_inicial_jogador1,pv_jogador1,ativar_habilidade_jogador1)
                

        if ativar_habilidade_jogador2 == True:

            if classe_jogador2 == 'Guerreiro':
                dano_jogador2,ativar_habilidade_jogador2 = impulso(dano_jogador2,ativar_habilidade_jogador2)
            elif classe_jogador2 == 'Mago':
                if rodada == rodada_da_habilidade_jogador2:
                    contador_de_golpes2 = 0
                dano_jogador1,contador_de_golpes2,ativar_habilidade_jogador2 = escudo(dano_jogador1,contador_de_golpes2,2,atacante,rodada,rodada_da_habilidade_jogador2,ativar_habilidade_jogador2)
            elif classe_jogador2 == 'Samurai':
                dano_jogador2,ativar_habilidade_jogador2 = katana(dano_jogador2,rodada,rodada_da_habilidade_jogador2,ativar_habilidade_jogador2)
            elif classe_jogador2 == 'Sacerdote':
                pv_jogador2,ativar_habilidade_jogador2 = cura(pv_inicial_jogador2,pv_jogador2,ativar_habilidade_jogador2)
            
        

        # define o jogador que vai atacar
        atacante = random.choice(ordem_ataque)

        # Um dos dois acerta o ataque
        if atacante == 1:
            print(f'\nJogador 1 acertou o ataque causando {dano_jogador1} de dano em Jogador 2.')
            pv_jogador2 -= dano_jogador1
            golpes_jogador1 += 1

        elif atacante == 2:
            print(f'\nJogador 2 acertou o ataque causando {dano_jogador2} de dano em Jogador 1.')
            pv_jogador1 -= dano_jogador2
            golpes_jogador2 += 1

    
        # exibe os pontos de vida dos jogadores
        print(f"Jogador 1: {pv_jogador1} pontos de vida / Habilidade = {golpes_jogador1}0%")
        print(f"Jogador 2: {pv_jogador2} pontos de vida / Habilidade = {golpes_jogador2}0%")

        
        # verifica se algum jogador venceu
        if pv_jogador1 <= 0:
            vitorias_jogador1 += 1
            print(f"\nO JOGADOR 1 VENCEU O {_round}° ROUND")

        elif pv_jogador2 <= 0:
            vitorias_jogador2 += 1
            print(f"\nO JOGADOR 2 VENCEU O {_round}° ROUND")
        
        rodada += 1
    
    _round += 1

if vitorias_jogador1 == 2:
    print('\n******************  O JOGADOR 1 É O GRANDE CAMPEÃO FINAL  ******************')
elif vitorias_jogador2 == 2:
    print('\n******************  O JOGADOR 2 É O GRANDE CAMPEÃO FINAL  ******************\n')
        

