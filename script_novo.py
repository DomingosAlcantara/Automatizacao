# import pyautogui
# from openpyxl import load_workbook
import json
from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# credenciais = {
# "usuario": "",
# "senha": ""
# }

atalhos = {
    "VisualizaçãoTXT": "listFav_8AB53D70_EFEF_431C_8CDB_CFE996BF71FF_APP_P554801W_W554801WC_ECT0001_50",
    "botaoAdicionar": "C0_53",  # "outer0_53",  # "hc_Add",
    "botaoImportar": "jdehtmlImportData0_1",
    "importar_area_transferencia": "clipBoardSettings",
    "colar": "impOption",
    "primeira_celula_da_grade": "PG_0.0",
    "interface_via_midia_magnetica": "listFav_55EDEAD5_18FC_4EA3_85E1_B6068D6032CC_UBE_R584801W__ECT0001_60",
}

ERP = "https://erp.correios.com.br"
credencials_path = Path(__file__).parent  # .home() / "Credenciais"


def carregar_credenciais(file_path: Path) -> dict:
    """
        Args:
            file_path: Caminho do arquivo que contem as credenciais de acesso
        Return:
            dict:
    """
    with open(file_path / "credenciais.json", "r", encoding="utf-8") as file:
        credenciais = json.load(file)
    return credenciais


def buscar_elementos(navegador: webdriver.Chrome, tag: str) -> list[WebElement]:
    return navegador.find_elements(By.ID, tag)


def abrir_site(navegador: webdriver.Chrome, site: str) -> None:
    navegador.get(site)


def carregar_driver(navegador: webdriver.Chrome) -> None:
    """_summary_

    Args:
        navegador (webdriver): instancia do navegador

    Returns:
            Function: Função interna para acesso ao site
    """
    def interno(credenciais: dict) -> None:  # type: ignore
        """_summary_

        Args:
            credenciais (dict): dados do usuario para acesso ao site
        """
        navegador.find_element(By.ID, "User").send_keys(credenciais["usuario"])
        navegador.find_element(By.ID, "Password")\
            .send_keys(credenciais["senha"])
        navegador.find_element(By.CLASS_NAME, "buttonstylenormal").click()
        # navegador.find_element(By.CSS_SELECTOR
    return interno


def visualizar_arquivo_importado(navegador: webdriver.Chrome) -> None:
    """
        _summary_

        Args:
            navegador (webdriver.Chrome): instancia do navegador
    """
    def interno(list_opcoes: list[str]):
        for opcao in list_opcoes:
            element = WebDriverWait(navegador, 60).until(
                EC.visibility_of_element_located((By.ID, opcao))
            )
            try:
                navegador.find_element(By.ID, opcao).click()
                print(f"O elemento: {opcao} foi alcançado")
            except TimeoutError:
                print(f"O Item {opcao} não pode ser alcançado")
                break
            sleep(5)
    return interno


def visualizar_elementos(navegador: webdriver.Chrome, opcao: str) -> None:
    return navegador.find_element()


if __name__ == "__main__":
    opcoes = list(atalhos.values())

    drivers = webdriver.Chrome()
    drivers.maximize_window()
    acessar_site = carregar_driver(drivers)
    acessar_visualizacao = visualizar_arquivo_importado(drivers)
    sleep(15)

    abrir_site(drivers, ERP)
    acessar_site(carregar_credenciais(credencials_path))  # type:ignore
    acessar_visualizacao(opcoes)  # type:ignore
