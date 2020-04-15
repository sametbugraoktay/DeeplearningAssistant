import webbrowser
import requests



    
def openBrowser():
        url = 'http://google.com/'
        safari_path = 'open -a /Applications/Safari.app %s'
        webbrowser.get(safari_path).open(url)
        
def openTranslate():
        
        base_url = "https://translate.google.com/#view=home&op=translate&sl=auto&tl=en&text="
  
        
        word = input("Çevrilecek metni giriniz: ") 
  
       
        complete_url = base_url + word 
        chrome_path = 'open -a /Applications/Safari.app %s'
        webbrowser.get(chrome_path).open(complete_url)
       

def exchangeDolar():
        url = 'https://api.exchangerate-api.com/v4/latest/USD'
        response = requests.get(url)
        data = response.json()
        #return("Dolar Kuru:",data["rates"]["TRY"])
        
        return "Dolar Kuru:{}".format(str(data["rates"]["TRY"]))
        
def exchangeEuro():

        
        url = 'https://api.exchangerate-api.com/v4/latest/EUR'

        
        response = requests.get(url)
        data = response.json()

        
        
        return ("Euro Kuru:",data["rates"]["TRY"])
        
def maps():
        url = 'https://www.google.com/maps'
        chrome_path = 'open -a /Applications/Safari.app %s'
        webbrowser.get(chrome_path).open(url)

def weather():

        api_key = "500e672810df08e00eeee00572f02112"
  
        
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
  
        
        city_name = input("Şehir ismi giriniz : ") 
  
       
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
  
        
        response = requests.get(complete_url) 
  
        # json method of response object  
        # convert json format data into 
        # python format data 
        x = response.json() 
  
        # Now x contains list of nested dictionaries 
        # Check the value of "cod" key is equal to 
        # "404", means city is found otherwise, 
        # city is not found 
        if x["cod"] != "404": 
  
            # store the value of "main" 
            # key in variable y 
            y = x["main"] 
  
            # store the value corresponding 
            # to the "temp" key of y 
            current_temperature = y["temp"] 
  
    
           
            return ("Sıcaklık: " + current_temperature-272.5) 
  
   
        