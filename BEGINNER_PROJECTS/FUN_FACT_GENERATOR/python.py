import json
import requests
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *

def start(_):
    clear()

    put_html(
        '<p align="left">'
        '<h2><img src="https://em-content.zobj.net/source/microsoft-teams/337/grinning-face_1f600.png" width="7%"> Fun Fact Generator</h2>'
        '</p>'
    )

    url = "https://uselessfacts.jsph.pl/random.json?language=en"


    response = requests.get(url)
    data = json.loads(response.text)
    fact=data['text']
    style(put_text(fact),'color:blue; font-size: 30px')

    put_buttons(
        [dict(label='click me',value='outline-success',color='outline-success')],onclick=start
    )


if __name__ == '__main__':
    # Put a heading "Fun Fact Generator"
    put_html(
        '<p align="left">'
        '<h2><img src="https://em-content.zobj.net/source/microsoft-teams/337/grinning-face_1f600.png" width="7%"> Fun Fact Generator</h2>'
        '</p>'
    )
    
    # Hold the session for a long time and put the "Click me" button
    put_buttons(
        [dict(label='Click me', value='outline-success', color='outline-success')],
        onclick=start
    )
    hold()