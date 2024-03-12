'''
Programação Estruturada
2024.1
12/03/2024

AC5

'''

import random

def main():
    vd_aventureiro = 100
    ataque_aventureiro = random.randint(10, 20)
    defesa_aventureiro = random.randint(1, 5)

    vd_monstro = random.randint(60, 80)
    ataque_monstro = random.randint(20, 30)

    print("aventureiro - ", "Vida:",vd_aventureiro, "ataque:", ataque_aventureiro, "defesa:", defesa_aventureiro)
    print("monstro -", "vida: ", vd_monstro,"ataque:", ataque_monstro)

    rodada = 1
    while vd_aventureiro > 0 or vd_monstro > 0:
        print(rodada)
        vd_monstro -= random.randint(1, ataque_aventureiro)
        if vd_monstro <= 0:
            print("O Mostro Morreu!")
            break
        dn_monstro = random.randint(1, ataque_monstro) - defesa_aventureiro
        if dn_monstro > 0:
            vd_aventureiro -= dn_monstro
        if vd_aventureiro <= 0:
            print("Você Morreu!")
            break

        print("aventureiro - ", "Vida:",vd_aventureiro, "ataque:", ataque_aventureiro, "defesa:", defesa_aventureiro)
        print("monstro -", "vida: ", vd_monstro,"ataque:", ataque_monstro)
        rodada += 1







main()








