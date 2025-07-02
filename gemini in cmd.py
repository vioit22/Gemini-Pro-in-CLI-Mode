import google.generativeai as genai
from logging import root
root= input("Gemini for cmd! Click enter to continue...")
API_KEY = "AIzaSyC5NPQagI_OeOtdVEceRMx92gswMiq6vAk"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.5-pro")
chat = model.start_chat()
print("Welcome to Gemini for cmd! Developed by Vio IT.")
while True:
    user_input = input("You: ")
    
    if user_input.lower() == 'exit':
        break
    response = chat.send_message(user_input)
    print(f"Gemini: {response.text}")
input("Press Enter to confirm exit and close the program.")