from pathlib import Path
import datetime
import time
import os
import pyautogui
import shutil
import json


class Automator:
    
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
        while True:
            if self.buscar_imagem(imagem) != False:
                imagem_encontrada = self.buscar_imagem(imagem)
                self.clique(imagem_encontrada)
                time.sleep(1)
                print(f"CLIQUE IMAGEM: {imagem} - TRUE")
                break
            else:
                time.sleep(1)
                print(f"CLIQUE IMAGEM: {imagem} - FALSE")
                continue

    
    def clique_imagem_tempo(self, imagem):
        for _ in range(3):
            imagem_encontrada = self.buscar_imagem(imagem)
            if imagem_encontrada is not False:
                self.clique(imagem_encontrada)
                return
            time.sleep(1)
        raise pyautogui.ImageNotFoundException


    def aguardar_imagem(self, imagem, tentativas=0, sleep=1):
        if tentativas == 0:
            while True:
                resultado_busca = self.buscar_imagem(imagem)
                if resultado_busca == False:
                    print("AGUARDAR IMAGEM - TRUE")
                    time.sleep(sleep)
                else:
                    return True
        else:
            for tentativa in range(tentativas):
                print("AGUARDAR IMAGEM, TENTATIVA: {tentativa}")
                resultado_busca = self.buscar_imagem(imagem)
                if resultado_busca == False:
                    time.sleep(sleep)
                else:
                    return True
            return False


    def aguardar_imagens(self, imagens, sleep=1):
        while True:
            for imagem in imagens:
                caminho_imagem = "src/img/" + imagem + ".png"
                result = pyautogui.locateCenterOnScreen(caminho_imagem, region=(0, 0, pyautogui.size().width, pyautogui.size().height), grayscale=True, confidence=0.8)
                if result is None:
                    time.sleep(sleep)
                    continue
                else:
                    PosX, PosY = result
                    return imagem
    

    def criar_pasta(self, nome, data):
        path = f"G:\Drives compartilhados\Departamento Fiscal\zRoboECAC\{nome}\{data}"

        if not os.path.exists(path):
            os.makedirs(path)
            print(f"PASTA {nome} CRIADA")
        else:
            print(f"PASTA {nome} JÁ EXISTE")


    def ultimo_arquivo_baixado(self):
        DownloadsPath = str(Path.home() / "Downloads")
        Files_DownloadsPath = os.listdir(DownloadsPath)
        Files_DownloadsPath = sorted(Files_DownloadsPath, key=lambda x: os.path.getmtime(os.path.join(DownloadsPath, x)))

        if Files_DownloadsPath:
            UltimoArquivo = os.path.join(DownloadsPath, Files_DownloadsPath[-1])
            return UltimoArquivo


    def mover_renomear(self, nome, data):
        ultimo_arquivo = self.ultimo_arquivo_baixado()
        if ultimo_arquivo != '':
            caminho_destino = f"G:\Drives compartilhados\Departamento Fiscal\zRoboECAC\{nome}\{data}\{nome} {data}.pdf"
            diretorio = os.path.dirname(ultimo_arquivo)
            novo_caminho = os.path.join(diretorio, nome)
            os.rename(ultimo_arquivo, novo_caminho)
            shutil.move(novo_caminho, caminho_destino)
            print("MoverRenomear"),


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


    def data_mes(self):
        data_mes = time.strftime("%m")
        return data_mes


    def alterar_valor_json(self, empresa_nome, chave, novo_status):
        caminho_arquivo = r'src/empresas.json'
        with open(caminho_arquivo, encoding='utf-8') as arquivo:
            conteudo = json.load(arquivo)
        for empresa in conteudo:
            if empresa["nome"] == empresa_nome:
                empresa[chave] = novo_status
        with open(caminho_arquivo, 'w') as arquivo:
            json.dump(conteudo, arquivo, indent=4)

    
    def task_kill(self):
        chrome = "chrome.exe"
        os.system(f"taskkill /F /IM {chrome}")
        print("Task-Kill")


    def deletar(self):
        for files in os.listdir(r"C:\Users\Nexxo\Downloads"):
            path = os.path.join(r"C:\Users\Nexxo\Downloads", files)
            try:
                shutil.rmtree(path)
            except OSError:
                os.remove(path)
        print("Arquivo Deletado")