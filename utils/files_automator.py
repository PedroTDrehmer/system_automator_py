import datetime
import os
import json
import shutil
from PIL import ImageGrab
from utils.variables import Paths


def alterar_valor_json(nome, chave, novo_status):
    with open(Paths.PATH_JSON, encoding='utf-8-sig') as arquivo:
        conteudo = json.load(arquivo)
    for empresa in conteudo:
        if empresa["nome"] == nome:
            empresa[chave] = novo_status
    with open(Paths.PATH_JSON, 'w') as arquivo:
        json.dump(conteudo, arquivo, indent=4)
    print('JSON ALTERADO')


def criar_pasta(nome, tipo):
    path_criar_pasta = f"{Paths.PATH_DRIVE}\\{data_mes_ano()}\\{nome}\\{tipo}"
    if not os.path.exists(path_criar_pasta):
        try:
            os.makedirs(path_criar_pasta)
            print(f'PASTA CRIADA - {nome}')
        except FileNotFoundError:
            pass
    else:
        print(f'PASTA JA EXISTE - {nome}')


def ultimo_arquivo_baixado():
    files_download = os.listdir(Paths.PATH_DOWNLOAD)
    files_download = sorted(files_download, key=lambda x: os.path.getmtime(os.path.join(Paths.PATH_DOWNLOAD, x)))
    if files_download:
        ultimo_arquivo = os.path.join(Paths.PATH_DOWNLOAD, files_download[-1])
        print(f'ARQUIVO BAIXADO - {ultimo_arquivo}')
        return ultimo_arquivo


def mover_renomear(nome, tipo):
    path_mover_renomear = f"{Paths.PATH_DRIVE}\\{data_mes_ano()}\\{nome}\\{tipo}\\SEFAZ BA.xlsx"
    ultimo_arquivo = ultimo_arquivo_baixado()
    if ultimo_arquivo != '':
        caminho_destino = path_mover_renomear
        diretorio = os.path.dirname(ultimo_arquivo)
        novo_caminho = os.path.join(diretorio, nome)
        os.rename(ultimo_arquivo, novo_caminho)
        shutil.move(novo_caminho, caminho_destino)
        print('MOVER RENOMEAR')


def capture_screenshot(nome, tipo):
    path_capture_screenshot = f"{Paths.PATH_DRIVE}\\{data_mes_ano()}\\{nome}\\{tipo}\\SEFAZ BA.png"
    screenshot = ImageGrab.grab()
    screenshot.save(path_capture_screenshot)
    print("SCREENSHOT")


def deletar():
    for files in os.listdir(Paths.PATH_DOWNLOAD):
        path = os.path.join(Paths.PATH_DOWNLOAD, files)
        try:
            shutil.rmtree(path)
        except OSError:
            os.remove(path)
    print('ARQUIVOS DELETADOS')


def task_kill():
    chrome = "chrome.exe"
    os.system(f"taskkill /F /IM {chrome}")
    print('TASKKILL')


def data_inicial():
    # Primeiro Dia do Mês Passado
    now = datetime.datetime.now()
    past_month = now.month - 1 if now.month != 1 else 12
    year_of_past_month = now.year - 1 if past_month == 12 else now.year
    full_date = f"{year_of_past_month}{str(past_month).zfill(2)}01" + "000000"
    data = datetime.datetime.strptime(full_date, "%Y%m%d%H%M%S").strftime("%d/%m/%Y")
    return data


def data_final():
    # Ultimo Dia do Mês Passado
    now = datetime.datetime.now()
    first_day_of_month = now.replace(day=1)
    last_day_of_previous_month = first_day_of_month - datetime.timedelta(days=1)
    data = last_day_of_previous_month.strftime("%d/%m/%Y")
    return data


def data_mes_ano():
    # Mês Passado e Ano
    now = datetime.datetime.now()
    past_month = now.month - 1 if now.month != 1 else 12
    year_of_past_month = now.year - 1 if past_month == 12 else now.year
    full_date = f"{year_of_past_month}{past_month:02d}"
    data = datetime.datetime.strptime(full_date, "%Y%m").strftime("%m.%Y")
    return data
