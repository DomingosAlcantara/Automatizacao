# import pyautogui
# from openpyxl import load_workbook
import json
from pathlib import Path
from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Automatizacao ():
    """_summary_
    """

    def __init__(self, navegador: Chrome,
                 tempo_de_espera: int = 5) -> None:
        self._navegador = navegador
        self._credenciais = None
        self._tempo_de_espera = tempo_de_espera

    def definir_credenciais(self, path_credenciais: Path) \
            -> dict[dict[str, str], dict[str, str]]:
        """Método para carregar os dados de login

        Args:
            path_credenciais (Path): Caminho onde esta o arquivo com
            as credenciais

        Returns:
            tuple: Dicionario com nome de usuario e senha
        """
        with open(path_credenciais / "credenciais.json", "r",
                  encoding="utf-8"
                  ) as file:

            credenciais = json.load(file)

        return credenciais

    def logar(self, credenciais: tuple[str, str]) -> None:
        """_summary_

        Args:
            credenciais (tuple): _description_
        """
        usuario, senha = credenciais
        self._navegador.find_element(By.ID, "User")\
            .send_keys(usuario)

        self._navegador.find_element(By.ID, "Password")\
            .send_keys(senha)

        self._navegador.find_element(By.CLASS_NAME,
                                     "buttonstylenormal").click()

    def abrir_url(self, url: str) -> None:
        """Abre o site informado

        Args:
            url (str): url que deverá ser aberto
        """
        self._navegador.maximize_window()
        self._navegador.get(url)

    def elemento_esta_visivel(self, elemento: str) -> bool:
        """_summary_

        Args:
            elemento (str): _description_

        Returns:
            bool: _description_
        """
        element = WebDriverWait(self._navegador, 60).until(
            EC.visibility_of_element_located((By.ID, elemento))
        )

        return element.is_displayed()

    def acessar_opcao_visualizacao(self, opcao: str) -> None:
        """_summary_

        Args:
            opcao (str): _description_
        """
        sleep(self._tempo_de_espera)
        try:
            if self.elemento_esta_visivel(opcao):
                self._navegador.find_element(By.ID, opcao).click()
        except TimeoutError:
            print(f"O Item {opcao} não pode ser alcançado")

    def adicionar(self) -> None:
        """_summary_
        """
        sleep(self._tempo_de_espera)
        ActionChains(self._navegador).key_down(Keys.CONTROL)\
            .key_down(Keys.ALT).send_keys("A").key_up(Keys.CONTROL)\
            .key_up(Keys.ALT).perform()

    def importar(self) -> None:
        """_summary_
        """
        sleep(self._tempo_de_espera)
        ActionChains(self._navegador).key_down(Keys.CONTROL)\
            .key_down(Keys.SHIFT).send_keys("I").key_up(Keys.CONTROL)\
            .key_up(Keys.SHIFT).perform()

    def importar_da_area_de_transferencia(self) -> None:
        """_summary_
        """
        sleep(self._tempo_de_espera)
        for _ in range(5):
            ActionChains(self._navegador).send_keys(Keys.TAB).perform()

        ActionChains(self._navegador).send_keys(Keys.ARROW_DOWN).perform()

    def colar_da_area_de_transferencia(self) -> None:
        """_summary_
        """
        sleep(self._tempo_de_espera)
        ActionChains(self._navegador).send_keys(Keys.TAB)\
            .send_keys(Keys.ARROW_DOWN).perform()

    def informar_campos(self) -> None:
        """_summary_
        """
        ActionChains(self._navegador).send_keys(Keys.TAB)\
            .send_keys("A").perform()
        ActionChains(self._navegador).send_keys(Keys.TAB)\
            .send_keys("1").perform()

    def selecionar_campo_na_grade(self) -> None:
        """_summary_
        """
        ActionChains(self._navegador).send_keys(Keys.TAB).send_keys(Keys.TAB)\
            .perform()

    def sair(self) -> None:
        self._navegador.quit()
