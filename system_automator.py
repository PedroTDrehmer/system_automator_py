import datetime
import os
import time
import pyautogui


class SystemAutomator:

    def buscar_imagem(self, imagem):
        caminho_imagem = "src/img/" + imagem + ".png"
        posicao = pyautogui.locateOnScreen(caminho_imagem, region=(0, 0, pyautogui.size().width, pyautogui.size().height), grayscale=True, confidence=0.99)
        if posicao is not None:
            return posicao



    def clique(self, posicao=""):
        if posicao is not None:
            centro_x = posicao.left + posicao.width / 2
            centro_y = posicao.top + posicao.height / 2
            pyautogui.click(centro_x, centro_y)

    

    def verificar_imagem(self, imagem):
        imagem_encontrada = self.buscar_imagem(imagem)
        if imagem_encontrada:
            print('verificar_imagem - TRUE')
            return True
        else:
            print('verificar_imagem - FALSE')
            time.sleep(1)
            return False
            

    
    def clique_imagem(self, imagem):
        while True:
            imagem_encontrada = self.buscar_imagem(imagem)
            if imagem_encontrada:
                print(f'clique_imagem - {imagem} - TRUE')
                self.clique(imagem_encontrada)
                break



    def clique_imagem_tentativas(self, imagem, tentativas):
        for i in range(tentativas):
            imagem_encontrada = self.buscar_imagem(imagem)
            if imagem_encontrada is not False:
                print(f'clique_imagem_tentativas - {i}')
                self.clique(imagem_encontrada)
                return True
            else:
                time.sleep(1)
                return False



    def aguardar_imagem(self, imagem, tentativas=0):
        if tentativas == 0:
            print(f'aguardar_imagem - {imagem}')
            while True:
                resultado_busca = self.buscar_imagem(imagem)
                if resultado_busca:
                    print(f'aguardar_imagem - {imagem} - TRUE')
                    return imagem
                else:
                    time.sleep(2)
                    
        else:
            for i in range(tentativas):
                resultado_busca = self.buscar_imagem(imagem)
                if resultado_busca:
                    print(f'aguardar_imagem - {imagem} - TRUE')
                    return imagem
                else:
                    time.sleep(2)
        


    def aguardar_imagens(self, imagens, tentativas=0):
        if tentativas == 0:
            while True:
                for imagem in imagens:
                    resultado_busca = self.buscar_imagem(imagem)
                    if resultado_busca:
                        print(f'aguardar_imagem - {imagem} - TRUE')
                        return imagem
                    else:
                        print(f'aguardar_imagem - {imagem} - FALSE')
                        time.sleep(2)
        else:
            for i in range(tentativas):
                for imagem in imagens:
                    resultado_busca = self.buscar_imagem(imagem)
                    if resultado_busca:
                        print(f'aguardar_imagem - {imagem} - TRUE')
                        return imagem
                    else:
                        print(f'aguardar_imagem - {imagem} - FALSE')
                        time.sleep(2)
  
    

    def task_kill(self, programa):
        os.system(f"taskkill /F /IM {programa}")



    def data_inicial_mes_ano(self):
        # Primeiro dia do Mes Passado
        now = datetime.datetime.now()
        past_month = now.month - 1 if now.month != 1 else 12
        year_of_past_month = now.year - 1 if past_month == 12 else now.year
        full_date = f"{year_of_past_month}{str(past_month).zfill(2)}01" + "000000"
        data_inicial = datetime.datetime.strptime(full_date, "%Y%m%d%H%M%S").strftime("%d/%m/%Y")
        return data_inicial



    def data_final_mes_ano(self):
        # Ultimo dia do Mes Passado
        now = datetime.datetime.now()
        first_day_of_month = now.replace(day=1)
        last_day_of_previous_month = first_day_of_month - datetime.timedelta(days=1)
        data_final = last_day_of_previous_month.strftime("%d/%m/%Y")
        return data_final



    def data_mes_passado_ano(self):
        now = datetime.datetime.now()
        past_month = now.month - 1 if now.month != 1 else 12
        year_of_past_month = now.year - 1 if past_month == 12 else now.year
        full_date = f"{year_of_past_month}{past_month:02d}"
        data_mes_passado_ano = datetime.datetime.strptime(full_date, "%Y%m").strftime("%m.%Y")
        return data_mes_passado_ano
