# -*- coding: utf-8 -*-
import pyttsx
import principal
import unicodedata


def elimina_tildes(cadena):
    s = ''.join((c for c in unicodedata.normalize(
        'NFD', unicode(cadena)) if unicodedata.category(c) != 'Mn'))
    return s.decode()


con_tildes = principal.bot.generar_palabra()
string_acentos = con_tildes.decode('utf-8')
sin_tildes = elimina_tildes(string_acentos)

eng = pyttsx.init()
print(sin_tildes)
text = sin_tildes

listVoices = eng.getProperty('voices')
eng.setProperty('voice', listVoices[20].id)
eng.say(text)
eng.runAndWait()
