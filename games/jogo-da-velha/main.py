import os,sys
import random
from colorama import  Fore,Style ,Style
from random import  randint
from time import sleep
 
 
jogar_novament ="s" # determina se quer jogar novamente apos ter decarado o vencedor ou perdedor
 
 #o tabuleiro contem 9 jogadas (se estes todso forem preechidos sem nemhum vencedor declararei o jogo como enpatre)
jogadas=0 #nr de jogadas o max =9 limitada
maxJogadas=9 #nove casas no maximo
USER=0
CPU=1
who_plays =randint(USER,CPU) # 1=cpu e 2=pessoaFisica

verificar_vitoria=False #

# matrix do jogo com tres linhas e tres colunas
# e cada posicoa esta vazio
tabuleiro = [
    ['  ','  ','  '],
    ['  ','  ', '  '],
    ['  ','  ','  '],
]

# fucoa resposael por limpar e desenhar atela
def tela():
    global tabuleiro
    global jogadas
    os.system('clear')
    print("\033[33;1m\t0    \t1  \t2 \033[m")
    print("\033[32m\t=================\t\033[m")
    for i in range(len(tabuleiro)):
        x='x'
        if '0' in tabuleiro[i]:
            x='\033[32m H \033[m'
        else:
            x='\033[31m N \033[m'']'
        print(f"  \033[31;1m {i} \033[m: \033[36m{tabuleiro[i][0]}\033[m |   {tabuleiro[i][1]}    |{tabuleiro[i][2]}  ")
        print("\033[32m\t-----------------\t\033[m")
    print(f'\033[34mJOGADAS:\033[m\033[32;1m{jogadas}\033[m')

def jogador_joga():
    global jogadas
    global verificar_vitoria
    global maxJogadas
    global who_plays 
    global USER
    global CPU
    
    # 
    if who_plays ==USER and jogadas < maxJogadas:
        print('\033[38m User :\033m')
        while True:
            try:
                
                row =int(input('\033[31;1mrow \ (h)  :\033[m'))
                col =int(input('\033[33;1m col \ (v) :\033[m'))
                if tabuleiro[row][col].strip() !='':
                    print('\033[32m Linha in valida ja foi preechida\033[m')
                else:
                    tabuleiro[row][col] = '\033[32m x \033[m'
            # vou passar o jogo para cpu e incrementar o nr d jogadas
                    who_plays=CPU
                    jogadas +=1
                    break
            except  IndexError as erroIndex:
                print(f'\033[36m ( digite apenas 0 ,1 e 2 \033[m ')
            except ValueError as e:
                print('\033[33;1m DIGITE APENAS NUMEROS \033[m')
            
def cpu_plays():
    global jogadas
    global who_plays 
    global verificar_vitoria
    global maxJogadas
    global USER
    global CPU
    
    if who_plays==CPU:
        print('[ CPU ] loading ...',end='')
        sleep(randint(0, 2))
        print('\003[36m;1 Done !')
        sys.stdout.flush()
        print()
        row=randint(0,2)
        col=randint(0,2)
        print(f'CPU => Col {row} COL :{col}')
        sleep(2)
        if tabuleiro[row][col].strip() !='':
            print('\033[32m Linha in valida ja foi preechida\033[m')
        else:
            tabuleiro[row][col] = '\033[34m U \033[m'
            who_plays=USER
            jogadas +=1
            
def verificar_vitoria():
    global tabuleiro
    global jogadas
    for i in range(len(tabuleiro)):
        for r in tabuleiro[i]:
            if r.strip() !='':
                print(r)
                print('game over !')
                r=input('Reset all ?')
                if 'y' in r.lower():
                    tabuleiro = [
                        ['  ','  ','  '],
                        ['  ','  ', '  '],
                        ['  ','  ','  '],
                    ]
                    jogadas=0
                    
        
    
def main():
    while True:
        # verificar_vitoria()
        tela()
        sleep(1)
        jogador_joga()
        cpu_plays()
        # if 'y' in input('play again ?'): break

if __name__ == '__main__':
    main()
    