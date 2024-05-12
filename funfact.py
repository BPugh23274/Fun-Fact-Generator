# import the following modules 
import json 
import requests 
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *

#Function that gets the fun fact
def get_fun_fact(_): 
    # Clear the above screen 
    clear() 
    put_html("<p align=""left""><h2>Fun Fact Generator</h2></p>") 

    #Url where useless facts are obtained (JSON file)
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    #Calls GET function 
    response = requests.request("GET",url)
    #Converts json file to something readable in python object (text among other things)
    data = json.loads(response.text)
    #Pulling text from the data output
    useless_fact = data['text'] 
    # Put the facts in the violet colour 
    style(put_text(useless_fact), 'color:violet; font-size: 30px') 
    # Put the click me button 
    put_buttons( 
        [dict(label='Press Me!', value='outline-success',  color='outline-success')], onclick=get_fun_fact)



if __name__ == '__main__': 
    #Put a heading "Fun Fact Generator" 

    put_html("<p align=""left""><h2>Fun Fact Generator</h2></p>") 

      

    #hold the session for long time 

    #Put a Click me button 

    put_buttons( 

        [dict(label='Press Me', value='outline-success',  

              color='outline-success')], onclick=get_fun_fact)  
            
hold()