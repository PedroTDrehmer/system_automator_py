import time
import pyautogui


def buscar_imagem(imagem):
    caminho_imagem = "src/img/" + imagem + ".png"
    posicao = pyautogui.locateOnScreen(caminho_imagem, region=(0, 0, pyautogui.size().width, pyautogui.size().height), grayscale=True, confidence=0.9)
    if posicao is not None:
        return posicao
    else:
        return False


def clique(posicao=""):
    if posicao is not None:
        centro_x = posicao.left + posicao.width / 2
        centro_y = posicao.top + posicao.height / 2
        pyautogui.click(centro_x, centro_y)
        return True


def clique_imagem(imagem, tentativas):
    if tentativas == 0:
        while True:
            imagem_encontrada = buscar_imagem(imagem)
            if imagem_encontrada:
                clique(imagem_encontrada)
                print(f'CLIQUE IMAGEM - {imagem} - TRUE')
                return True
    else:
        for tentativa in range(tentativas):
            imagem_encontrada = buscar_imagem(imagem)
            if imagem_encontrada is True:
                clique(imagem_encontrada)
                print(f'CLIQUE IMAGEM - {imagem} - TRUE')
                return True
            else:
                print(f'CLIQUE IMAGEM TENTATIVA - {tentativa}')
                time.sleep(1)
                return False


def verificar_imagem(imagem, tentativas):
    print(f'VERIFICANDO IMAGEM - {imagem}')
    if tentativas == 0:
        while True:
            resultado_busca = buscar_imagem(imagem)
            if resultado_busca == False:
                print(f'VERIFICAR IMAGEM - {imagem} - FALSE')
                time.sleep(1)
            else:
                print(f'VERIFICAR IMAGEM - {imagem} - TRUE')
            return True
    else:
        for tentativa in range(tentativas):
            resultado_busca = buscar_imagem(imagem)
            if resultado_busca == False:
                time.sleep(1)
                print(f'VERIFICAR IMAGEM - {imagem} - {tentativa}')
            else:
                print(f'VERIFICAR IMAGEM - {imagem} - TRUE')
                return True
        return False


def verificar_imagens(imagens, tentativas):
    if tentativas == 0:
        while True:
            for imagem in imagens:
                if buscar_imagem(imagem):
                    print('verificar_imagem - TRUE')
                    return True
                else:
                    time.sleep(1)
                    print(f'VERIFICAR IMAGEM - {imagem}')
                    return False
    else:
        for tentativa in range(tentativas):
            for imagem in imagens:
                if buscar_imagem(imagem):
                    print('verificar_imagem - TRUE')
                    return True
                else:
                    time.sleep(1)
                    print(f'VERIFICAR IMAGEM - {imagem} - {tentativa}')
                    return False


def aguardar_imagem(imagem, tentativas=0):
    if tentativas == 0:
        while True:
            resultado_busca = buscar_imagem(imagem)
            if resultado_busca == False:
                print(f'AGUARDANDO IMAGEM - {imagem}')
                time.sleep(2)
            else:
                print(f'IMAGEM ENCONTRADA - {imagem}')
                return True
    else:
        for tentativa in range(tentativas):
            print(f"AGUARDAR IMAGEM, TENTATIVA: {tentativa}")
            resultado_busca = buscar_imagem(imagem)
            if resultado_busca == False:
                time.sleep(2)
            else:
                return True
        return False


def aguardar_imagens(imagens, tentativas):
    if tentativas == 0:
        while True:
            for imagem in imagens:
                caminho_imagem = "src/img/" + imagem + ".png"
                result = pyautogui.locateCenterOnScreen(caminho_imagem, region=(0, 0, pyautogui.size().width, pyautogui.size().height), grayscale=True, confidence=0.8)
                if result is None:
                    time.sleep(3)
                    continue
                else:
                    PosX, PosY = result
                    return imagem
    else:
        for tentativa in range(tentativas):
            for imagem in imagens:
                caminho_imagem = "src/img/" + imagem + ".png"
                result = pyautogui.locateCenterOnScreen(caminho_imagem, region=(0, 0, pyautogui.size().width, pyautogui.size().height), grayscale=True, confidence=0.8)
                if result is None:
                    time.sleep(1)
                    print(f'AGUARDAR IMAGENS - {tentativa}')
                else:
                    PosX, PosY = result
                    return imagem
