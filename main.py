import pyttsx3 # pip install pyttsx3
import webbrowser as wb
from time import sleep as wait
import sys

r = pyttsx3.init()
r.say("Hello Boss! Welcome to the computer!")
r.runAndWait()

wait(2)

r.say("Opening your favourite websites!")
r.runAndWait()

wait(3)

wb.open("https://youtube.com/")
wb.open("https://discord.com/channels/@me")
wb.open("https://instagram.com/")

r.say("Bye Sir! Have a nice day!")
wait(1)
r.say("I have to go! Open me when you turn your computer on!")
r.runAndWait()

sys.exit()