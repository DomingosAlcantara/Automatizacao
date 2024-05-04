from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from time import sleep
import json
from pathlib import Path

# servico = Service(ChromeDriverManager().install())

# navegador = webdriver.Chrome(service=servico)

credenciais_previas = {
    "usuario": 80891950,
    "senha": "Lucia24@@Keven20",
}

atalhos = {
    "VisualizaçãoTXT": "listFav_8AB53D70_EFEF_431C_8CDB_CFE996BF71FF_APP_P554801W_W554801WC_ECT0001_50",
    "botaoAdicionar": "hc_Add",
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


def acesso_previo(navegador: webdriver.Chrome, credenciais: dict) -> None:
    navegador.find_element(By.ID, "username").send_keys(credenciais["usuario"])
    navegador.find_element(By.ID, "password").send_keys(credenciais["senha"])
    navegador.find_element(By.CLASS_NAME, "botao-principal").click()


def abrir_site(navegador: webdriver.Chrome, site: str) -> None:
    navegador.get(site)


def carregar_driver(navegador: webdriver.Chrome) -> None:  # type: ignore
    """
    Args:
        navegador: instancia do navegador

    Return:
        Function
    """
    def interno(credenciais: dict) -> None:  # type: ignore
        """
        Args:
            credenciais: dados do usuario para acesso ao site

        Returns:
            None
        """
        navegador.find_element(By.ID, "User").send_keys(credenciais["usuario"])
        navegador.find_element(By.ID, "Password").send_keys(
            credenciais["senha"])
        navegador.find_element(By.CLASS_NAME, "buttonstylenormal").click()
    return interno


def visualizar_arquivo_importado(navegador: webdriver.Chrome) -> None:
    """_summary_

    Args:
        navegador (webdriver.Chrome): _description_

    Returns:
        function: _description_
    """
    def interno(list_opcoes: list) -> None:
        """_summary_

        Args:
            list_opcoes (list): _description_
        """
        for _, opcao in enumerate(list_opcoes):
            print(opcao)
            element = WebDriverWait(navegador, 60).until(
                EC.visibility_of_element_located((By.ID, opcao))
            )
            if element.is_enabled():
                print("Elemento visivel")
                navegador.find_element(By.ID, opcao).click()
            sleep(5)
    return interno


if __name__ == "__main__":
    opcoes = atalhos.values()
    drivers = webdriver.Chrome()
    drivers.maximize_window()
    abrir_site(drivers, ERP)
    acessar_site = carregar_driver(drivers)
    acessar_visualizacao = visualizar_arquivo_importado(drivers)
    acesso_previo(drivers, credenciais_previas)
    sleep(2)
    acessar_site(carregar_credenciais(credencials_path))  # type: ignore
    acessar_visualizacao(opcoes)  # type: ignore
    sleep(5)
