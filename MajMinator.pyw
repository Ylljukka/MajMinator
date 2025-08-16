"""
    Convertisseur automatique majuscule /minuscule lorsqu'une combinaison de touche est pressé.
    
    
    Création :          REYNAUD Thomas          2025-08-16
    Modification :      xxxxxx  xxxx            xx/xx/xxxx
"""

import keyboard
import pyperclip
import time

# Met dans le presse papier puis on le transforme dedans.
def flip_case():
    keyboard.press('ctrl')
    keyboard.press('c')
    keyboard.release('c')
    keyboard.release('ctrl')   
    time.sleep(0.05)
    
    text = pyperclip.paste()  
    if not text:
        return
           
    toggled = text.swapcase()         
    pyperclip.copy(toggled)           
    
    time.sleep(0.05)
    keyboard.press('ctrl')
    keyboard.press('v')
    keyboard.release('v')
    keyboard.release('ctrl')         


keyboard.add_hotkey('ctrl+u', flip_case)

# garde le script en écoute
keyboard.wait()  


