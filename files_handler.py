import time
from PIL import ImageGrab
import json
import os
import shutil


class FilesHandler:

    def __init__(self):
        self.path_json = r"src/json/empresas_dominio.json"
        self.path_download = r"C:\\Users\\Nexxo\\Downloads"
        self.path_drive = r"G:\\Drives compartilhados\\Departamento Fiscal\\zRoboCND"
        

    def criar_pasta(self, data, nome):
        path_pasta = f"{self.path_drive}\\{data}\\{nome}"
        if not os.path.exists(path_pasta):
            try:
                os.makedirs(path_pasta)
                print("PASTA CRIADA")
            except FileNotFoundError:
                pass
        else:
            print("PASTA JA EXISTE")

        
    def capture_screenshot(self, data, nome):
        path_screen = f"{self.path_drive}\\{data}\\{nome}\\CND FEDERAL.png"
        screenshot = ImageGrab.grab()
        screenshot.save(path_screen)
        print("SCREENSHOT")


    def ultimo_arquivo_baixado(self):
        files_download = os.listdir(self.path_download)
        files_download = sorted(files_download, key=lambda x: os.path.getmtime(os.path.join(self.path_download, x)))

        if files_download:
            ultimo_arquivo = os.path.join(self.path_download, files_download[-1])
            print(f"ARQUIVO BAIXADO - {ultimo_arquivo}")
            return ultimo_arquivo


    def mover_renomear(self, data, nome):
        path_destino = f"{self.path_drive}\\{data}\\{nome}\\CND FEDERAL.pdf"
        ultimo_arquivo = self.ultimo_arquivo_baixado()
        if ultimo_arquivo != "":
            caminho_destino = path_destino
            diretorio = os.path.dirname(ultimo_arquivo)
            novo_caminho = os.path.join(diretorio, nome)
            os.rename(ultimo_arquivo, novo_caminho)
            shutil.move(novo_caminho, caminho_destino)
            time.sleep(1)
            print("MOVER RENOMEAR")


    def deletar(self):
        for files in os.listdir(self.path_download):
            path = os.path.join(self.path_download, files)
            try:
                shutil.rmtree(path)
            except OSError:
                os.remove(path)
        time.sleep(1)
        print("ARQUIVOS DELETADOS")


    def alterar_valor_json(self, id, chave, novo_status):
        caminho_arquivo = self.path_json
        with open(caminho_arquivo, encoding="utf-8-sig") as arquivo:
            conteudo = json.load(arquivo)
        for empresa in conteudo:
            if empresa["id"] == id:
                empresa[chave] = novo_status
        with open(caminho_arquivo, "w") as arquivo:
            json.dump(conteudo, arquivo, indent=4)
        print("JSON ALTERADO")
