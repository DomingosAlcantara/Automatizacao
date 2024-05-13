"""_summary_
"""
# from selenium import webdriver
# from selenium.webdriver import ActionChains, Keys
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

    # type ignore
    def informar_senha(self, elementos: tuple[str, str]) -> None:
        """_summary_

        Args:
            email (str): _description_
        """
        def inserir_senha(senha: str) -> None:
            """_summary_

            Args:
                senha (str): _description_
            """
            self._navegador.find_element(By.NAME, elementos[0])\
                .send_keys(senha)

        self._navegador.find_element(By.ID, elementos[1]).click()

        return inserir_senha

    # type ignore
    def informar_email(self, elementos: tuple[str, str]) -> None:
        """_summary_

        Args:
            id_campo (str): _description_
        """
        def inserir_email(email: str) -> None:
            """_summary_

            Args:
                email (str): _description_
            """
            self._navegador.find_element(By.CSS_SELECTOR, elementos[0])\
                .send_keys(email)

        self._navegador.find_element(By.CSS_SELECTOR, elementos[1]).click()

        return inserir_email
