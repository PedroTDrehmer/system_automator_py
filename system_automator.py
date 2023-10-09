import datetime
import os
import time
import pyautogui


class SystemAutomator:

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


    def clique_imagem(self, imagem, attempts=30):
        for i in range(attempts):
            imagem_encontrada = self.buscar_imagem(imagem)
            
            if imagem_encontrada is not False:
                self.clique(imagem_encontrada)
                print(f"CLIQUE IMAGEM: {imagem} - TRUE")
                break
            else:
                time.sleep(2)
                print(f"CLIQUE IMAGEM: {imagem} - FALSE")
            if i == attempts -1:
                print("Limite de tentativas atingido")
        

    def clique_imagem_tempo(self, imagem):
        for _ in range(3):
            imagem_encontrada = self.buscar_imagem(imagem)
            if imagem_encontrada is not False:
                self.clique(imagem_encontrada)
                return
            time.sleep(2)
        raise pyautogui.ImageNotFoundException


    def aguardar_imagem(self, imagem, tentativas=0):
        if tentativas == 0:
            while True:
                resultado_busca = self.buscar_imagem(imagem)
                if resultado_busca == False:
                    print("AGUARDAR IMAGEM - TRUE")
                    time.sleep(2)
                else:
                    return True
        else:
            for tentativa in range(tentativas):
                print("AGUARDAR IMAGEM, TENTATIVA: {tentativa}")
                resultado_busca = self.buscar_imagem(imagem)
                if resultado_busca == False:
                    time.sleep(2)
                else:
                    return True
            return False
    

    def task_kill(self):
        chrome = "chrome.exe"
        os.system(f"taskkill /F /IM {chrome}")
        print("Task-Kill")


    def data_inicial(self):
        # Primeiro Dia do Mês Passado
        now = datetime.datetime.now()
        past_month = now.month - 1 if now.month != 1 else 12
        year_of_past_month = now.year - 1 if past_month == 12 else now.year
        full_date = f"{year_of_past_month}{str(past_month).zfill(2)}01" + "000000"
        data_inicial = datetime.datetime.strptime(full_date, "%Y%m%d%H%M%S").strftime("%d/%m/%Y")
        return data_inicial


    def data_final(self):
        # Ultimo Dia do Mês Passado
        now = datetime.datetime.now()
        first_day_of_month = now.replace(day=1)
        last_day_of_previous_month = first_day_of_month - datetime.timedelta(days=1)
        data_inicial = last_day_of_previous_month.strftime("%d/%m/%Y")
        return data_inicial


    def data_mes_ano(self):
        # Mês Passado e Ano
        now = datetime.datetime.now()
        past_month = now.month - 1 if now.month != 1 else 12
        year_of_past_month = now.year - 1 if past_month == 12 else now.year
        full_date = f"{year_of_past_month}{past_month:02d}"
        data_inicial = datetime.datetime.strptime(full_date, "%Y%m").strftime("%m.%Y")
        return data_inicial