import os
import json
import shutil
from PIL import ImageGrab

class FilesHandler:

    def __init__(self, data, nome):
        self.path_json = r"src/json/empresas_ecac.json"
        self.path_download = r"C:\\Users\\Nexxo\\Downloads"
        self.path_drive = r"G:\\Drives compartilhados\\Departamento Fiscal\\zRoboECAC"
        self.path_criar_pasta = f"{self.path_drive}\\{data}\\{nome}"
        self.path_capture_screenshot = f"{self.path_drive}\\{data}\\{nome}\\CND FEDERAL.png"
        self.path_mover_renomear = f"{self.path_drive}\\{data}\\{nome}\\Relatorio Fiscal Ecac.pdf"


    
    def criar_pasta(self):
        if not os.path.exists(self.path_criar_pasta):
            try:
                os.makedirs(self.path_criar_pasta)
                print('PASTA CRIADA')
            except FileNotFoundError:
                pass
        else:
            print('PASTA JA EXISTE')


    
    def capture_screenshot(self):
        screenshot = ImageGrab.grab()
        screenshot.save(self.path_capture_screenshot)
        print("SCREENSHOT")



    def ultimo_arquivo_baixado(self):
        files_download = os.listdir(self.path_download)
        files_download = sorted(files_download, key=lambda x: os.path.getmtime(os.path.join(self.path_download, x)))

        if files_download:
            ultimo_arquivo = os.path.join(self.path_download, files_download[-1])
            print(f'ARQUIVO BAIXADO - {ultimo_arquivo}')
            return ultimo_arquivo



    def mover_renomear(self, data, nome):
        ultimo_arquivo = self.ultimo_arquivo_baixado()
        if ultimo_arquivo != '':
            caminho_destino = self.path_mover_renomear
            diretorio = os.path.dirname(ultimo_arquivo)
            novo_caminho = os.path.join(diretorio, nome)
            os.rename(ultimo_arquivo, novo_caminho)
            shutil.move(novo_caminho, caminho_destino)
            print('MOVER RENOMEAR')
     


    def deletar(self):
        for files in os.listdir(self.path_download):
            path = os.path.join(self.path_download, files)
            try:
                shutil.rmtree(path)
            except OSError:
                os.remove(path)
        print('ARQUIVOS DELETADOS')



    def alterar_valor_json(self, nome, chave, novo_status):
        with open(self.path_json, encoding='utf-8-sig') as arquivo:
            conteudo = json.load(arquivo)
        for empresa in conteudo:
            if empresa["nome"] == nome:
                empresa[chave] = novo_status
        with open(self.path_json, 'w') as arquivo:
            json.dump(conteudo, arquivo, indent=4)
        print('JSON ALTERADO')