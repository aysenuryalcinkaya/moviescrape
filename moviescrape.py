from selenium import webdriver
import urllib.request

# WebDriver'ı başlatın (örneğin, Chrome tarayıcı)
driver = webdriver.Chrome(executable_path='path/to/chromedriver')

# İlgili URL'ye gidin
url = 'https://www.fullhdfilmizlesene.pw/film/heart-of-stone/'
driver.get(url)

try:
    # İframe'i bulun
    iframe = driver.find_element('tag name', 'iframe')
    iframe_src = iframe.get_attribute('src')

    # Iframe'deki video sayfasına gidin
    driver.get(iframe_src)

    # Video sayfasındaki video URL'sini alın
    content=driver.page_source
    print(content)

except Exception as e:
    print('Hata oluştu:', str(e))

finally:
    # WebDriver'ı kapatın
    driver.quit()
