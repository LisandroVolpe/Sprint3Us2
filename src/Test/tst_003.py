import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import TimeoutException

class Test_001(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # Puedes cambiar 'Chrome' por el navegador de tu elección
        self.driver.maximize_window()

    def test_grimoldi(self):
        self.driver.get("https://www.grimoldi.com/")
        
        time.sleep(2)
        # Encuentra el #login
        login_sector = self.driver.find_element(By.ID, "loginSector")

        
        login_btn = self.driver.find_element(By.CLASS_NAME, "loginUsuarioBtn")
        login_btn.click()

        
        time.sleep(2)
        
        
    
        login_link = self.driver.find_element(By.CSS_SELECTOR, "#loginSector > div > ul.loginUsuario > li.liLogin > a")
        login_link.click()
        
        time.sleep(2)
        

        #Datos inicio de sesion
        username_input = self.driver.find_element(By.ID, "UserName")
        password_input = self.driver.find_element(By.ID, "Password")

        username_input.send_keys("lichivolpe@gmail.com")
        password_input.send_keys("Testtest11")
        
        aceptar_btn = self.driver.find_element(By.CLASS_NAME, "boton")
        aceptar_btn.click()
        
        time.sleep(15)
        
        close_btn = self.driver.find_element(By.ID, "btnNoIdWpnPush")
        close_btn.click()
        
        #Buscador
        search_button = self.driver.find_element(By.ID, "btnDivBusqueda")
        search_button.click()

        #Buscar vans
        search_input = self.driver.find_element(By.ID, "textoBusqueda")
        search_input.send_keys("llavero")

        search_input.send_keys(Keys.RETURN)
        
        time.sleep(5)
        
        #elegir llavero
        elegir_btn = self.driver.find_element(By.ID, "slider29838")
        elegir_btn.click()
        
        talle_btn = self.driver.find_element(By.ID, "121")
        talle_btn.click()
        
        time.sleep(2)
        
        cant_dd = self.driver.find_element(By.ID, "cantidadSeleccionada")
        
        time.sleep(2)
        
        #seleccionar dropdown
        select = Select(cant_dd)

        select.select_by_value("3")
        
        
        comprar_btn = self.driver.find_element(By.ID, "comprar")
        comprar_btn.click()
        
        time.sleep(2)
         
        continuar_btn = self.driver.find_element(By.ID, "linkContinuar")
        continuar_btn.click()
        
        #volver a home
        time.sleep(2)
        home_btn = self.driver.find_element(By.ID, "sectorBanner_22972")
        home_btn.click()
        
        time.sleep(2)
        
        #buscar 
        search_button = self.driver.find_element(By.ID, "btnDivBusqueda")
        search_button.click()

        search_input = self.driver.find_element(By.ID, "textoBusqueda")
        search_input.send_keys("sandalias")
        search_input.send_keys(Keys.RETURN)
        
        time.sleep(2)
        
        medias_btn = self.driver.find_element(By.ID, "slider30234")
        medias_btn.click()
        
        talle_m_btn = self.driver.find_element(By.ID, "75")
        talle_m_btn.click()
        
        time.sleep(4)
        
        cant_dd = self.driver.find_element(By.ID, "cantidadSeleccionada")
        
        time.sleep(3)
        
        #drpodown
        select = Select(cant_dd)

        select.select_by_value("2")
        
        time.sleep(3)
        
        comprar_btn = self.driver.find_element(By.ID, "comprarEmergente")
        comprar_btn.click()
        
        time.sleep(4)
        
        continuar_btn = self.driver.find_element(By.ID, "linkContinuar")
        continuar_btn.click()
        
        #carrito
        Carrito_link = self.driver.find_element(By.CSS_SELECTOR, "#loginSector > div > ul.compraList > li > ul > li.carrito > a")
        Carrito_link.click()
        
        time.sleep(4)
        
        vaciar_btn = self.driver.find_element(By.ID, "btnVaciarCarro")
        vaciar_btn.click()
        
        
        
    
        time.sleep(10)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()