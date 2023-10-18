import pyttsx3

engine = pyttsx3.init()

print("Welcome to Robospeaker 1.0 - created by Mansi")
# Text to be converted to speech


text = input("say here:")

# Convert the text to speech
engine.say(text)

 # Play the speech
engine.runAndWait()

while True:
    ch = (input("do you want to continue(yes/no) : "))
    match ch:
        case "yes":
            text = input("say here:")
            engine.say(text)
            engine.runAndWait()

        case "no":
            break
        case _:
            print("Wrong Choice!!!!")

