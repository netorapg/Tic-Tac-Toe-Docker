# jogo_da_velha.py

def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def checar_vitoria(tabuleiro, jogador):
    # Verificar linhas, colunas e diagonais
    for i in range(3):
        if all([cell == jogador for cell in tabuleiro[i]]):  # Linha
            return True
        if all([tabuleiro[j][i] == jogador for j in range(3)]):  # Coluna
            return True
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:  # Diagonal 1
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:  # Diagonal 2
        return True
    return False

def checar_empate(tabuleiro):
    return all([cell != " " for linha in tabuleiro for cell in linha])

def jogar():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"

    while True:
        exibir_tabuleiro(tabuleiro)
        try:
            linha = int(input(f"Jogador {jogador_atual}, escolha a linha (0, 1, 2): "))
            coluna = int(input(f"Jogador {jogador_atual}, escolha a coluna (0, 1, 2): "))
            if tabuleiro[linha][coluna] != " ":
                print("Essa posição já está ocupada. Tente novamente.")
                continue
            tabuleiro[linha][coluna] = jogador_atual
        except (ValueError, IndexError):
            print("Entrada inválida! Insira números entre 0 e 2.")
            continue

        if checar_vitoria(tabuleiro, jogador_atual):
            exibir_tabuleiro(tabuleiro)
            print(f"Parabéns! Jogador {jogador_atual} venceu!")
            break
        elif checar_empate(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print("Empate!")
            break

        # Alternar jogadores
        jogador_atual = "O" if jogador_atual == "X" else "X"

if __name__ == "__main__":
    jogar()
