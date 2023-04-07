def addCategory(self,functions):
        functions = self.callable(functions)
        self.startController("#operations-categories-controller-addCategory .opblock-summary-control")
        self.tryControllerWithArgument("{\"name\":\"example\"}",".body-param__text")
        for function in functions:
            function()
        #eğer fonksiyonlar burada 
        self.stopController("#operations-categories-controller-addCategory .opblock-summary-control")

def test_addCategory_repeat(self):
        self.deleteCategories(())
        self.addCategory(())#başarılı şekilde çalışıyor
        self.addCategory(
            (
            lambda:self.result("400"),
            lambda:self.makeErrormessage(),
            lambda:self.stopController("#operations-categories-controller-addCategory .opblock-summary-control"),#kapatılması gereken şey burada kapatılıyor
            lambda:self.printErrormessage(),
            lambda:self.driver.save_screenshot(f"{self.folderPath}/ {self.testTime}-test-retrofitSelenium-addCategory-Repeat.png"),
            return
            )
        )