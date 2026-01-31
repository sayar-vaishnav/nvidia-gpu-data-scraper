from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd


class nvidia_GPUs:
    def __init__(self):
        options = Options()
        options.add_argument("--headless=new")   # best for new Chrome
        options.add_argument("--window-size=1920,1080")
        self.driver=webdriver.Chrome()
        self.wait=wait = WebDriverWait(self.driver, 10)

    def open_website(self): 
        url='https://www.nvidia.com/en-us/geforce/graphics-cards/compare/'
        self.driver.get(url) 
        time.sleep(2) 
        print("\n\nWEBSITE IS LAUNCHED SUCCESSFULLY..............\n\n")

    def accept_cookies(self): 
        try:
         # Try common button text
            accept_btn = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="onetrust-accept-btn-handler"]'))
        )
            accept_btn.click()
            print("✅ Cookies accepted\n\n")
        except:
            print("⚠️ No cookie popup found (or already handled)\n\n")

    #---------------EXTRACTION OF 50 SERIES::------------
    def extract_50s(self): 
        gpu_50_names = []
        gpu_50_data = []

        #VIEW FULL SPECS------
        specs_button=self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME,'btn'))
        )
        specs_button.click()
        print("VIEW ALL SPECS BUTTON CLICKED SUCCESSFILLY.....\n\n")

        #EXTRACTION ON NAMES-------
        table_50s=self.wait.until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="compare50SeriesChart"]/div/table'))                                    
        )
        print("50s TABLE LOCATED.....\n\n")
        gpu_50_names_list=table_50s.find_elements(By.CLASS_NAME,'h4')
        time.sleep(2)
        for n in gpu_50_names_list:
            gpu_50_names.append(n.text.strip())
        time.sleep(2)
        print("50s GPU NAMES ARE COLLECTED SUCCESSFULLY........\n\n")

        #EXTRACTION ON ROWS DATA------
        specs_50=[]
        rows_req=table_50s.find_elements(By.TAG_NAME,'tr')[1:]
        for row in rows_req:
            cells=row.find_elements(By.TAG_NAME,'td')
            row_text = [cell.text.strip() for cell in cells]
            specs_50.append(row_text[0])                      #GPU SPECS NAME(core/speed/vram..etc)
            gpu_50_data.append(row_text[1:])               #GPU SPECS DATA 
            time.sleep(1)
        print("50s GPU ROW DATA GATHERED SUCCESSFULLY........\n\n")

        #CONVERT 50 SEIRES GPU TO DATAFRAME------
        nvidia_gpu_50_df=pd.DataFrame(gpu_50_data,columns=gpu_50_names)
        nvidia_gpu_50_df.insert(0,'specs',specs_50)
        nvidia_gpu_50_df.to_csv('/Users/sayar/Desktop/PC BUILDER APP/gpu/nvidia_50.csv',index=False)
        print("CREATED 50 DF SUCCESSFULLY..........\n\n")

    #---------------EXTRACTION OF 40 SERIES::--------------
    def extract_40s(self): 
        gpu_40_names = []
        gpu_40_data = []

        #SELECT SECTION------
        section_40=self.wait.until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="compare-40"]'))
        )
        #VIEW FULL SPECS------
        time.sleep(2)
        full_specs_button_40 = section_40.find_element(By.CLASS_NAME,'btn')
        full_specs_button_40.click()
        print("VIEW ALL SPECS BUTTON CLICKED SUCCESSFILLY.....\n\n")

        #EXTRACTION ON NAMES-------
        table_40s=self.wait.until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="compare40SeriesChart"]/div/table'))
        )
        print("40s TABLE LOCATED.....\n\n")
        gpu_40_names_list=table_40s.find_elements(By.CLASS_NAME,'h4')
        time.sleep(2)
        for n in gpu_40_names_list:
            gpu_40_names.append(n.text.strip())
        time.sleep(2)
        print("40s GPU NAMES ARE COLLECTED SUCCESSFULLY........\n\n")

        #EXTRACTION ON ROWS DATA------
        specs_40=[]
        rows_req=table_40s.find_elements(By.TAG_NAME,'tr')[1:]
        for row in rows_req:
            cells=row.find_elements(By.TAG_NAME,'td')
            row_text = [cell.text.strip() for cell in cells]
            specs_40.append(row_text[0])                      #GPU SPECS NAME(core/speed/vram..etc)
            gpu_40_data.append(row_text[1:])               #GPU SPECS DATA 
            time.sleep(1)
        print("40s GPU ROW DATA GATHERED SUCCESSFULLY........\n\n")

        #CONVERT 40 SEIRES GPU TO DATAFRAME------
        nvidia_gpu_40_df=pd.DataFrame(gpu_40_data,columns=gpu_40_names)
        nvidia_gpu_40_df.insert(0,'specs',specs_40)
        nvidia_gpu_40_df.to_csv('/Users/sayar/Desktop/PC BUILDER APP/gpu/nvidia_40.csv',index=False)
        print("CREATED 40 DF SUCCESSFULLY..........\n\n")
    
    #---------------EXTRACTION OF 30 SERIES::--------------
    def extract_30s(self): 
        gpu_30_names = []
        gpu_30_data = []

        #SELECT SECTION------
        section_30=self.wait.until(
            EC.presence_of_element_located((By.ID,'compare-specs'))
        )
        print("section 30 located..")

        #VIEW FULL SPECS------ 
        btn = section_30.find_element(
           By.XPATH, ".//div[contains(@class,'btn') and normalize-space()='View Full Specs']"
                )

        ActionChains(self.driver).move_to_element(btn).pause(0.3).click(btn).perform()

        #EXTRACTION ON NAMES-------
        table_30s=self.wait.until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="compare30SeriesChart"]/div/table'))
        )
        print("30s TABLE LOCATED.....\n\n")
        gpu_30_names_list=table_30s.find_elements(By.CLASS_NAME,'h4')
        time.sleep(2)
        for n in gpu_30_names_list:
            gpu_30_names.append(n.text.strip())
        time.sleep(2)
        print("30s GPU NAMES ARE COLLECTED SUCCESSFULLY........\n\n")

        #EXTRACTION ON ROWS DATA------
        specs_30=[]
        rows_req=table_30s.find_elements(By.TAG_NAME,'tr')[1:]
        for row in rows_req:
            cells=row.find_elements(By.TAG_NAME,'td')
            row_text = [cell.text.strip() for cell in cells]
            specs_30.append(row_text[0])                      #GPU SPECS NAME(core/speed/vram..etc)
            gpu_30_data.append(row_text[1:])               #GPU SPECS DATA 
            time.sleep(1)
        print("30s GPU ROW DATA GATHERED SUCCESSFULLY........\n\n")

        #CONVERT 40 SEIRES GPU TO DATAFRAME------
        nvidia_gpu_30_df=pd.DataFrame(gpu_30_data,columns=gpu_30_names)
        nvidia_gpu_30_df.insert(0,'specs',specs_30)
        nvidia_gpu_30_df.to_csv('/Users/sayar/Desktop/PC BUILDER APP/gpu/nvidia_30.csv',index=False)
        print("CREATED 30 DF SUCCESSFULLY..........\n\n")
    
    #---------------EXTRACTION OF 20 SERIES::--------------
    def extract_20s(self): 
        gpu_20_names = []
        gpu_20_data = []

        #SELECT SECTION------
        section_20=self.wait.until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="compare-20"]'))
        )
        #VIEW FULL SPECS------
        time.sleep(2)
        full_specs_button_20 = section_20.find_element(By.CLASS_NAME,'btn')
        full_specs_button_20.click()
        print("VIEW ALL SPECS BUTTON CLICKED SUCCESSFILLY.....\n\n")

        #EXTRACTION ON NAMES-------
        table_20s=self.wait.until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="compare20SeriesChart"]/div/table'))
        )
        print("20s TABLE LOCATED.....\n\n")
        gpu_20_names_list=table_20s.find_elements(By.CLASS_NAME,'h4')
        time.sleep(2)
        for n in gpu_20_names_list:
            gpu_20_names.append(n.text.strip())
        time.sleep(2)
        print("20s GPU NAMES ARE COLLECTED SUCCESSFULLY........\n\n")

        #EXTRACTION ON ROWS DATA------
        specs_20=[]
        rows_req=table_20s.find_elements(By.TAG_NAME,'tr')[1:]
        for row in rows_req:
            cells=row.find_elements(By.TAG_NAME,'td')
            row_text = [cell.text.strip() for cell in cells]
            specs_20.append(row_text[0])                      #GPU SPECS NAME(core/speed/vram..etc)
            gpu_20_data.append(row_text[1:])               #GPU SPECS DATA 
            time.sleep(1)
        print("20s GPU ROW DATA GATHERED SUCCESSFULLY........\n\n")

        #CONVERT 40 SEIRES GPU TO DATAFRAME------
        nvidia_gpu_20_df=pd.DataFrame(gpu_20_data,columns=gpu_20_names)
        nvidia_gpu_20_df.insert(0,'specs',specs_20)
        nvidia_gpu_20_df.to_csv('/Users/sayar/Desktop/PC BUILDER APP/gpu/nvidia_20.csv',index=False)
        print("CREATED 20 DF SUCCESSFULLY..........\n\n")

    #---------------EXTRACTION OF 16 SERIES::--------------
    def extract_16s(self): 
        gpu_16_names = []
        gpu_16_data = []

        #SELECT SECTION------
        section_16=self.wait.until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="compare-16"]'))
        )
        #VIEW FULL SPECS------
        time.sleep(2)
        full_specs_button_16 = section_16.find_element(By.CLASS_NAME,'btn')
        full_specs_button_16.click()
        print("VIEW ALL SPECS BUTTON CLICKED SUCCESSFILLY.....\n\n")

        #EXTRACTION ON NAMES-------
        table_16s=self.wait.until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="compare16SeriesChart"]/div/table'))
        )
        print("16s TABLE LOCATED.....\n\n")
        gpu_16_names_list=table_16s.find_elements(By.CLASS_NAME,'h4')
        time.sleep(2)
        for n in gpu_16_names_list:
            gpu_16_names.append(n.text.strip())
        time.sleep(2)
        print("16s GPU NAMES ARE COLLECTED SUCCESSFULLY........\n\n")

        #EXTRACTION ON ROWS DATA------
        specs_16=[]
        rows_req=table_16s.find_elements(By.TAG_NAME,'tr')[1:]
        for row in rows_req:
            cells=row.find_elements(By.TAG_NAME,'td')
            row_text = [cell.text.strip() for cell in cells]
            specs_16.append(row_text[0])                      #GPU SPECS NAME(core/speed/vram..etc)
            gpu_16_data.append(row_text[1:])               #GPU SPECS DATA 
            time.sleep(1)
        print("16s GPU ROW DATA GATHERED SUCCESSFULLY........\n\n")

        #CONVERT 16 SEIRES GPU TO DATAFRAME------
        nvidia_gpu_16_df=pd.DataFrame(gpu_16_data,columns=gpu_16_names)
        nvidia_gpu_16_df.insert(0,'specs',specs_16)
        nvidia_gpu_16_df.to_csv('/Users/sayar/Desktop/PC BUILDER APP/gpu/nvidia_16.csv',index=False)
        print("CREATED 16 DF SUCCESSFULLY..........\n\n")

    def close_website(self):
        print("WEBSITE IS CLOSING.....\n\n")
        self.driver.quit()
        

scrapper=nvidia_GPUs()

start = time.time()

scrapper.open_website()
scrapper.accept_cookies()

nvidia_50_df=scrapper.extract_50s()
nvidia_40_df=scrapper.extract_40s()
nvidia_30_df=scrapper.extract_30s()
nvidia_20_df=scrapper.extract_20s()
nvidia_16_df=scrapper.extract_16s()

scrapper.close_website()

end = time.time()

total_seconds = end - start
minutes = int(total_seconds // 60)
seconds = int(total_seconds % 60)

print(f"✅ Total Time Taken: {minutes} min,  {seconds} sec")

