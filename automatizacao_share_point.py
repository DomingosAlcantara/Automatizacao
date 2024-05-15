# type ignore
"""_summary_
"""
# from selenium import webdriver
# from selenium.webdriver import ActionChains, Keys
from time import sleep
from selenium.webdriver.chrome.webdriver import WebDriver as Chrome

from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
from automatizacao import Automatizacao


class AutomatizacaoSharedPoint(Automatizacao):
    """_summary_

    Args:
        Automatizacao (_type_): _description_
    """

    def __init__(self, navegador: Chrome) -> None:
        super().__init__(navegador)

    def abrir_aba_shared_point(self, url) -> None:
        """_summary_
        """
        self._navegador.switch_to.new_window('tab')
        self._navegador.get(url)

    def selecionar_campo_email(self, campo, dado="") -> None:
        """_summary_

        Args:
            campo (_type_): _description_
            dado (str, optional): _description_. Defaults to "".
        """
        if (dado):
            self._navegador.find_element(By.CSS_SELECTOR, campo)\
                .send_keys(dado)
        else:
            self._navegador.find_element(By.CSS_SELECTOR, campo).click()

    def informar_dados(self, elementos: tuple[str, str], dado: str) -> None:
        """_summary_

        Args:
            id_campo (str): _description_
        """
        sleep(self._tempo_de_espera)
        campo, botao = elementos
        self.selecionar_campo_email(campo, dado)

        # def inserir_dados(dado: str) -> None:
        #     """_summary_

        #     Args:
        #         email (str): _description_
        #     """
        #     self._navegador.find_element(By.CSS_SELECTOR, campo)\
        #         .send_keys(dado)

        self._navegador.find_element(By.CSS_SELECTOR, botao).click()
