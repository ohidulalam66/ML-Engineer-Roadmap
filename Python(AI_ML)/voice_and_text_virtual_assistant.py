# Voice + Text Virtual Assistant

# Install:
# uv pip install pyttsx3

# Import necessary libraries
import pyttsx3
from datetime import datetime


# Initialize the text-to-speech engine
# engine = pyttsx3.init()



# Define a function to speak text
def speak(text):
    engine = pyttsx3.init("sapi5")
    print("Assistant:", text)
    engine.say(text)
    engine.setProperty("rate", 150)
    engine.setProperty("volume", 1.0)
    engine.runAndWait()
    engine.stop()


# Greeting
print("Hi! Can I help you? I'm your Assistant. Type 'exit' to end.")


# Start chatting loop
while True:

    user_input = input("🧑 YOU: ").strip().lower()

    # Exit
    if user_input == "exit":
        speak("Goodbye! Have a nice day. 👋")
        break

    # Hello
    elif user_input == "hello" or user_input == "hi":
        speak("Hello! How are you?")

    # How are you
    elif  "how are you" in user_input:
        speak(
            "I'm a chatbot; I don't have any emotions. "
            "Still, I am doing well. 🙂"
        )

    # Name
    elif "name" in user_input:
        speak("I'm Spider, your assistant. How can I help you?")

    # Love
    elif (
        "love" in user_input
        or "feel" in user_input
        or "i love you" in user_input
        or "i like you" in user_input
    ):
        speak("You are very romantic 😂, but I cannot be romantic. 😭")

    # Time
    elif "time" in user_input:
        current_time = datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")

    # Date
    elif "date" in user_input:
        today_date = datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {today_date}")

    # Calculator
    elif "calculate" in user_input:

        try:
            expression = user_input.replace("calculate", "").strip()

            result = eval(expression)

            speak(f"The result is {result}")

        except:
            speak("Sorry! I couldn't understand the calculation.")

    # Unknown command
    else:
        speak(
            "I still cannot perform every task. "
            "I am still being built. 😁"
        )