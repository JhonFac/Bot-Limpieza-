from ast import If
import time
from selenium import webdriver
# import chromedriver_binary
# from selenium.common.exceptions import ElementNotVisibleException
# from selenium.common.exceptions import ElementNotSelectableException
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait ,Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from pathlib import Path
from platform import platform
import random


# from ObtenerIP import get_my_ip
# import requests
# ip=get_my_ip()

BASEDIR = Path('.').absolute()

class bot():

    def openChrome(self):

        if 'Windows' in platform():
            print('The operating system is Windows\nWe will look for "chromedriver.exe"')

            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--incognito")
            self.browser = webdriver.Chrome(ChromeDriverManager().install())

        else:
            print('The operating system is Linux\nWe will look for "chromedriver"')
            path = BASEDIR / 'driver/chromedriver'
            print('aqui abrimos chrome')
            # options = webdriver.ChromeOptions()
            # options.add_argument("--incognito")
            self.browser = webdriver.Remote('http://selenium:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME
            )

        self.browser.get('http://www.google.com')

    def saveLog(self, linck, keyword, start_time, i):
        try:
            final_time = datetime.now()
            time_difference = (final_time - start_time).seconds
            f = open ('LogActividades.txt','a')
            f.write('---------------- '+final_time.strftime("%x %H:%M")+' --------------\n'+str(time_difference)+' ,'+ str(i)+", Eduardo Behrentz " + str(keyword)+", Linck:"+linck+"\n")
            f.close()
            print (final_time.strftime("%x %H:%M") #'',
            +',', str(time_difference)
            + ",Eduardo Behrentz " + str(keyword)
            + "," + str(1))
        except:
            pass


    def loops(self):
        self.openChrome()
        #self.browser.save_screenshot('screenshot inicial.png')

        keywords = ["uniandes","Perfil", "Vicerrector","aire", "",
        "Google Schoolar Citations","Semana.com", "Columnas", "Artículos"
        "Ingeniería" "El Tiempo","Palabras", "Donaciones", "Medio ambiente"]


        forceUrl = [
            "https://scholar.google.com/citations?user=EO95t_sAAAAJ&hl=en",
            "https://www.portafolio.co/negocios/empresas/la-pandemia-no-freno-las-donaciones-a-uniandes-563711",
            "https://twitter.com/uniandes/status/1289761841405599745?lang=es",
            "https://encuentroresponsable.com/speaker/eduardo-behrentz-valencia/",
            "https://www.semana.com/autor/ebehrentz/",
            'https://www.eduardobehrentz.com/cierro-el-ciclo-en-uniandes/',
            'https://www.eduardobehrentz.com/la-historia-de-eduarado-behrentz/'
        ]

        urlexcept = [
            "https://www.eluniandino.com "    
        ]

        print("""
        listo, iniciamos..!!
        """)

        indice = 0
        start_time = datetime.now()

        for i in range (1,1000000):
            try:
                for keyword in keywords:
                    for p in range (1,2):
                        try:
                            final_time = datetime.now()
                            print(final_time.strftime("%H:%M"))
                            search = self.browser.find_element_by_name('q')
                            search.send_keys("Eduardo Behrentz " + keyword)
                            

                            search.send_keys(Keys.RETURN) # hit return after you enter search text
                            time.sleep(2) # sleep for 3 seconds so you can see the results
                            try:
                                WebDriverWait(self.browser,15).until(EC.presence_of_element_located((By.ID,"xjs"))) 
                            except Exception:
                                WebDriverWait(self.browser,15).until(EC.presence_of_element_located((By.ID,"rcnt"))) 
                            print('forzado')
                            forzado=True  # variable para forzar busqueda
                            # self.browser.save_screenshot("screenshot1.png")

                            if forzado==True:

                                pages=len(forceUrl)
                                num=random.randint(0, pages-1)
                                print(forceUrl[num])
                                linck=forceUrl[num]
                                # self.browser.save_screenshot("screenshot.png")
                                self.browser.get(linck)

                            else:
                                try:
                                    linck=self.browser.find_element_by_xpath('//*[@id="rso"]/div/div[1]/div/div[1]/a').get_attribute('href')
                                except Exception:
                                    linck=self.browser.find_element_by_xpath('//*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div/div/div/div[1]/div/a').get_attribute('href')

                                print(linck)    
                                salir=False

                                for url in urlexcept:
                                    if linck.startswith(url):
                                        salir=True
                                        break

                                if salir==True:
                                    continue
                                time.sleep(3)

                                print(f"screenshot {i}-{keyword}-{p}.png    -------------------------------------------------------------")

                                try:
                                    self.browser.find_element_by_xpath(f"//*[@id='rso']/div[{p}]/div/div[1]/div/div/div[1]/div").click()
                                except:
                                    # pass
                                    try:
                                        self.browser.find_element_by_xpath(f"//*[@id='rso']/div[{p}]/div/div[1]/div").click()
                                    except Exception:
                                        pass

                            self.saveLog(linck, keyword, start_time, i)
                            time.sleep(2)

                            y=0
                            t='100'
                            print('en pagina')

                            try:
                                while True:
                                    self.browser.execute_script(f"window.scrollTo(0, {t})") 
                                    time.sleep(1)
                                    y=y+200
                                    t=str(y)
                                    # self.browser.save_screenshot("screenshot3.png")
                                    if y>4000:
                                        break
                            except Exception:
                                pass

                            indice+=1

                            print(F'listo {p}')
                            self.browser.get('http://www.google.com.co')

                            time.sleep(2)

                        except Exception:
                            print('error, salta de linck')
                            self.browser.get('http://www.google.com.co')
                            time.sleep(2)

                        linck=''

            except (ConnectionRefusedError,IndexError, ConnectionError, ConnectionResetError, ConnectionAbortedError, Exception):
              
                print('termino ciclo..!')
                try:
                    print('error')
                    self.browser.quit()
                    self.openChrome()
                    #self.browser.save_screenshot("error 1.png")
                except Exception:
                    pass              

    def init(self):

        try:

            self.loops()

        except (ConnectionRefusedError,IndexError, ConnectionError, ConnectionResetError, ConnectionAbortedError):
            print('salio..!')
            exit()

if __name__ == '__main__':
    """ entry point app """
    time.sleep(10)
    b=bot()
    b.init()


