# import pyautogui
# from openpyxl import load_workbook
import json
from pathlib import Path
# from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait


class Automatizacao ():
    """_summary_
    """

    def __init__(self, navegador: webdriver.Chrome) -> None:
        self._navegador = navegador
        self._credenciais = None

    def definir_credenciais(self, path_credenciais: Path) -> dict[str, str]:
        """Método para carregar os dados de login

        Args:
            path_credenciais (Path): Caminho onde esta o arquivo com
            as credenciais

        Returns:
            dict: Dicionario com nome de usuario e senha
        """
        with open(path_credenciais / "credenciais.json", "r",
                  encoding="utf-8"
                  ) as file:

            credenciais = json.load(file)

        return credenciais

    def logar(self, credenciais: dict[str, str]) -> None:
        """_summary_

        Args:
            credenciais (dict): _description_
        """
        self._navegador.find_element(By.ID, "User")\
            .send_keys(credenciais["usuario"])

        self._navegador.find_element(By.ID, "Password")\
            .send_keys(credenciais["senha"])

        self._navegador.find_element(By.CLASS_NAME,
                                     "buttonstylenormal").click()

    def abrir_url(self, url: str) -> None:
        """Abre o site informado

        Args:
            url (str): url que deverá ser aberto
        """
        self._navegador.get(url)

    def acessar_opcao_visualizacao(self,)


if __name__ == "__main__":
    ERP = "https://erp.correios.com.br"
    credencials_path = Path(__file__).parent  # .home() / "Credenciais"

    automatizacao = Automatizacao(webdriver.Chrome())
    automatizacao.abrir_url(ERP)
    automatizacao.logar(automatizacao.definir_credenciais(credencials_path))
