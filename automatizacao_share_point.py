"""_summary_
"""
# from selenium import webdriver
# from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.webdriver import WebDriver as Chrome

# from selenium.webdriver.common.by import By
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

    def logar_no_shared_point(self, credenciais: dict[str, str]) -> None:
        """_summary_

        Args:
            credenciais (dict[str, str]): _description_
        """
        pass
