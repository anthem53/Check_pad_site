from selenium import webdriver
import chromedriver_autoinstaller
import os
import time
import schedule
from send import send_email;

# Check if chrome driver is installed or not
chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]

currentAddress = os.getcwd()
driver_path = currentAddress +'/%s/chromedriver' % chrome_ver

if os.path.exists(driver_path):
    print(f"chrom driver is installed: {driver_path}")
else:
    print(f"install the chrome driver(ver: {chrome_ver})")
    chromedriver_autoinstaller.install(True)

# Get driver and open url


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--headless")  # Background(CLI) 동작 사용
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-setuid-sendbox')
chrome_options.add_experimental_option('excludeSwitches',['enable-logging'])

driver = webdriver.Chrome(driver_path,options=chrome_options)

def job():
    driver.get("https://pad.neocyon.com/W/notice/list.aspx")
    table = driver.find_element_by_xpath('''//*[@id="list"]''')
    tbody = table.find_element_by_tag_name("tbody")

    post_list = []

    for tr in tbody.find_elements_by_tag_name("tr"):
        
        temp = []
        for td in tr.find_elements_by_tag_name("td"):
            temp.append(td.get_attribute("innerText"))
        post_list.append(" ".join(temp))

    result = "\n".join(post_list)


    try:
        isUpdated = False
        with open("result.txt","r", encoding="uft-8") as file:
            a = "".join(file.readlines())
            if a == result:
                print("There is no update. pass.")
                
            else :
                print("Call update issue to target")
                isUpdated = True
                send_email(a,result)
        if isUpdated == True:
            os.remove("result.txt")
            with open("result.txt","w",encoding="utf-8") as file:
                file.write(result)
                print("Update Complete.")
                
                
                ## call function
    except FileNotFoundError:
        print("First, if there is no file.")
        with open("result.txt","w", encoding='utf-8') as file:
            a = file.write(result)


def test():
    print("스케쥴 테스트")


def execute():    
    schedule.every(30).minutes.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    job()