import openai
import speech_recognition as sr
import pyttsx3

openai.api_key = "YOUR_API_KEY"

def generate_response(prompt):
  completions = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
  )

  message = completions.choices[0].text
  return message.strip()

def speak(text):
  engine = pyttsx3.init()
  engine.say(text)
  engine.runAndWait()

def listen():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    print("Listening...")
    audio = r.listen(source)
  try:
    text = r.recognize_google(audio)
    return text
  except Exception as e:
    print(e)
    return ""

def main():
  while True:
    user_input = listen()
    response = generate_response(user_input)
    speak(response)

if __name__ == "__main__":
  main()
