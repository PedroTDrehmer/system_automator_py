import time
import pyautogui


class ImageAutomator:

    def buscar_imagem(self, imagem):
        caminho_imagem = "src/img/" + imagem + ".png"
        posicao = pyautogui.locateOnScreen(caminho_imagem, region=(0, 0, pyautogui.size().width, pyautogui.size().height), grayscale=True, confidence=0.9)
        if posicao is not None:
            return posicao
        else:
            return False


    def clique(self, posicao=""):
        if posicao is not None:
            centro_x = posicao.left + posicao.width / 2
            centro_y = posicao.top + posicao.height / 2
            pyautogui.click(centro_x, centro_y)


    def clique_imagem(self, imagem):
        imagem_encontrada = self.buscar_imagem(imagem)
        if imagem_encontrada is not False:
            self.clique(imagem_encontrada)
            print(f"CLIQUE IMAGEM - TRUE - {imagem}")
            return True
        else:
            time.sleep(1)
            print(f"CLIQUE IMAGEM - FALSE - {imagem}")
            return False


    def clique_imagem_tentativas(self, imagem, tentativas):
        for i in range(tentativas):
            imagem_encontrada = self.buscar_imagem(imagem)
            if imagem_encontrada is not False:
                self.clique(imagem_encontrada)
                print(f"CLIQUE IMAGEM - TRUE - {imagem}")
                return True
            else:
                time.sleep(1)
                print(f"CLIQUE IMAGEM - FALSE - {imagem}")


    def verificar_imagem(self, imagem, tentativas):
        for tentativa in range(tentativas):
            print(f'VERIFICANDO IMAGEM - {imagem}')
            resultado_busca = self.buscar_imagem(imagem)
            if resultado_busca == False:
                time.sleep(1)
                print(f'TENTATIVA - {tentativa} - FALSE')
            else:
                print(f'VERIFICAR IMAGEM - {imagem} - TRUE')
                return True
        return False


    def verificar_imagens(self, imagens):
        for imagem in imagens:
            if self.buscar_imagem(imagem):
                print('verificar_imagem - TRUE')
                return True
            else:
                time.sleep(1)
                return False


    def aguardar_imagem(self, imagem, tentativas=0):
        if tentativas == 0:
            while True:
                resultado_busca = self.buscar_imagem(imagem)
                if resultado_busca == False:
                    print(f'AGUARDANDO IMAGEM - {imagem}')
                    time.sleep(2)
                else:
                    print(f'IMAGEM ENCONTRADA - {imagem}')
                    return True
        else:
            for tentativa in range(tentativas):
                print(f"AGUARDAR IMAGEM, TENTATIVA: {tentativa}")
                resultado_busca = self.buscar_imagem(imagem)
                if resultado_busca == False:
                    time.sleep(2)
                else:
                    return True
            return False


    def aguardar_imagens(self, imagens):
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
