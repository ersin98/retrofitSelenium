from msilib.schema import ServiceControl
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import datetime
from datetime import date
import openpyxl 
from selenium.webdriver.support.ui import WebDriverWait as pagewait
from selenium.webdriver.support.expected_conditions import staleness_of
from globalConstants import GlobalConstants as GC

class Test_Localhost:
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        now = datetime.now()
        self.folderPath = str(now.strftime("%d-%b-%Y")) #str(date.today())
        self.testTime=str(now.strftime("%H.%M")) #.%S
        Path(self.folderPath).mkdir(exist_ok=True)
        self.driver.get("http://localhost:8080/swagger-ui/index.html#/")
        self.vars = {}
    def teardown_method(self):
        self.vars = {}
        self.driver.quit()


        

    def errormessage(self):
        self.driver.get("https://translate.google.com/?hl=tr")
        self.page_loaded()
        self.driver.find_element(By.CSS_SELECTOR, ".MOkH4e").click()
        self.driver.find_element(By.CSS_SELECTOR, ".er8xn").click()
        self.driver.find_element(By.CSS_SELECTOR, ".er8xn").click()
        self.driver.find_element(By.CSS_SELECTOR, ".QFw9Te").click()
        self.driver.find_element(By.CSS_SELECTOR, ".er8xn").send_keys(self.vars["message"])
        self.driver.find_element(By.CSS_SELECTOR, ".MOkH4e").click()
        sleep(1)
        self.driver.save_screenshot(f"{self.folderPath}/ {self.testTime}-test-sauce-çeviri.png")
    def çeviri(self):
        self.vars["message"] = self.driver.find_element(By.CSS_SELECTOR, ".microlight:nth-child(3) .hljs-attr").text
        self.errormessage
    def page_loaded(self):
        old_page = self.driver.find_element_by_tag_name('html')
        yield
        pagewait(self.driver, 30).until(staleness_of(old_page))
    def getData(excelFileName,sheetName):
        excelFile = openpyxl.load_workbook("data/"+excelFileName)
        selectedSheet = excelFile[sheetName]
        header = {}
        for column in range(1, selectedSheet.max_column + 1):
            header[selectedSheet.cell(row=1, column=column).value] = column
        data = []
        for row in range(2, selectedSheet.max_row + 1):
            row_data = []
            for column in header.values():
                cell_value = selectedSheet.cell(row=row, column=column).value or ""
                row_data.append(cell_value)
            if len(data) > 1:
                data.append(tuple(row_data))
            else:
                data.append(cell_value)
        return data
    def result(self,resultNumer):
        self.waitForElementVisible((By.CSS_SELECTOR,".live-responses-table .response > .response-col_status"))
        assert self.driver.find_element(By.CSS_SELECTOR, ".live-responses-table .response > .response-col_status").text == resultNumer
    def waitForElementVisible(self,locator,timeout=10):
        WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))


#Controller
    def startController(self,opblockSummaryControl):
        self.waitForElementVisible((By.CSS_SELECTOR, opblockSummaryControl))
        self.driver.find_element(By.CSS_SELECTOR, opblockSummaryControl).click()
        self.waitForElementVisible((By.CSS_SELECTOR, ".try-out__btn"))
        self.driver.find_element(By.CSS_SELECTOR, ".try-out__btn").click()

    def tryControllerWithArgument(self,keys):
        self.waitForElementVisible((By.CSS_SELECTOR, ".body-param__text"))
        bodyParam = self.driver.find_element(By.CSS_SELECTOR, ".body-param__text")
        bodyParam.click()
        bodyParam.clear()
        bodyParam.send_keys(keys)
        self.driver.find_element(By.CSS_SELECTOR, ".execute").click()

    def tryController(self):
        self.driver.find_element(By.CSS_SELECTOR, ".execute").click()

    def stopController(self,opblockSummaryControl):
        self.waitForElementVisible((By.CSS_SELECTOR, opblockSummaryControl))
        self.driver.find_element(By.CSS_SELECTOR, ".btn-clear").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        self.driver.find_element(By.CSS_SELECTOR, opblockSummaryControl).click()
    def callable(self, functions):
        if callable(functions):#eğer fonksiyon tekse fonksiyonu fonksiyon listesine çeviriyoruz
            functions = (functions,)
            return functions
        return functions





#events
    def deleteCategories(self,functions):
        functions = self.callable(functions)
        self.startController(GC.controllerDeleteCategories)
        self.tryController()
        for function in functions:
            function()
        self.stopController(GC.controllerDeleteCategories)

    def addCategory(self,functions):
        functions = self.callable(functions)
        self.startController(GC.controllerAddCategory)
        self.tryControllerWithArgument("{\"name\":\"example\"}")
        for function in functions:
            function()
        self.stopController(GC.controllerAddCategory)
    
    def getCategories(self,functions):
        functions = self.callable(functions)
        self.startController(GC.controllerGetCategories)
        self.tryController()
        for function in functions:
            function()
        self.stopController(GC.controllerGetCategories)

    











#tests
    def test_deleteCategories(self):
        self.deleteCategories(
            (
            lambda: self.result(GC.ok),
            lambda: self.driver.save_screenshot(f"{self.folderPath}/ {self.testTime}-test-retrofitSelenium-deleteCategories.png")
            )
        )

    def test_addCategory(self):
        self.deleteCategories(())
        self.addCategory(
            (
            lambda:self.result(GC.created),
            lambda:self.driver.save_screenshot(f"{self.folderPath}/ {self.testTime}-test-retrofitSelenium-addCategory.png")
            )
        )
    @pytest.mark.parametrize("name", getData("category_send_keys.xlsx","CreateCategoryRequest"))
    def test_addCategory_invalid(self,name):
        self.deleteCategories(())
        self.startController(GC.controllerAddCategory)
        self.tryControllerWithArgument("{"+ f"\"name\":\"{name}\""+"}")
        self.driver.save_screenshot(f"{self.folderPath}/ {self.testTime}-test-retrofitSelenium-addCategory-invalid.png")
        self.result(GC.badRequest)
        self.stopController(GC.controllerAddCategory)

    def test_addCategory_repeat(self):
        self.deleteCategories(())
        self.addCategory(())
        self.addCategory(
            (
            lambda:self.result(GC.badRequest)
            )
        )
    def test_getCategories(self):
        self.getCategories((
            lambda:self.result(GC.ok),
            lambda:self.driver.save_screenshot(f"{self.folderPath}/ {self.testTime}-test-retrofitSelenium-getCategories.png")
        ))
        
    
