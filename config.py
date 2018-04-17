import tweepy
import time
import sys
import bot

CONSUMER_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxx'
CONSUMER_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
ACCESS_KEY = 'xxxxxxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
ACCESS_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
count = 0

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

print(".     .       .  .   . .   .   . .    +  . ")
print("  .     .  :     .    .. :. .___---------___. ")
print("       .  .   .    .  :.:. _'.. ....  '.. :-_. . ")
print("    .  :       .  .  .:../:            . .   :.:\. ")
print("        .   . :: +. :.:/: .   .    .        . . .:\ ")
print(" .  :    .     . _ :::/:               .    .  . .:\ ")
print("  .. . .   . - : :.:./.                        .  .:\ ")
print("  .      .     . :..|:                    .  .   . .:| ")
print("    .       . : : ..||        .                . . !:|")
print("  .     . . . ::. ::\(                           . :)/")
print(" .   .     : . : .:.|. ######              .#######::|")
print("  :.. .  :-  : .:  ::|.#######           ..########:|")
print(" .  .  .  ..  .  .. :\ ########          :######## :/")
print("  .        .+ :: : -.:\ ########       . ########.:/")
print("    .  .+   . . . . :.:\. #######       #######..:/")
print("      :: . . . . ::.:..:.\           .   .   ..:/")
print("   .   .   .  .. :  -::::.\.       | |     . .:/")
print("      .  :  .  .  .-:.:.::.\             ..:/ ")
print(" .      -.   . . . .: .:::.:.\.           .:/ ")
print(".   .   .  :      : ....::_:..:\   ___.  :/")
print("   .   .  .   .:. .. .  .: :.:.:\       :/ ")
print("     +   .   .   : . ::. :.:. .:.|\  .:/| ")
print("     .         +   .  .  ...:: ..|  --.:| ")
print(".      . . .   .  .  . ... :..:.. (  ..) ")
print(" .   .       .      :  .   .: ::/  .  .::\ ")
print(" ")


cantidad = input("Ingrese cantidad de tuits a publicar: ")
tiempo = input("Ingrese tiempo entre publicaciones (segundos): ")

while count < cantidad:
    line = bot.generar_palabra()
    count = count + 1
    print("-----------------------")
    print("  .-. ")
    print("|(@ @) ")
    print("\ \-/ tuiteando algo")
    print(" \/ \ ")
    print("  \ /\ ")
    print("  _H_ \ ")
    print(" ")
    print(" ")
    api.update_status(status=line)
    print("Tuit: ", line)
    time.sleep(tiempo)
