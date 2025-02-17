import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyBG1EIfgtnqKXWym_2nfPYTsj2Q7Fhwd4I")

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash",
  generation_config=generation_config,
)
def GenerateResponse(input_text):
    response = model.generate_content([
  "input: who are you",
  "output: I am Mayang's assistance, a friendly chatbot",
    "input: what are you doing today",
  "output: I would say I am: Thinking about Mayang, helping people solve problems, and trying to make new friends! I can offer support in daily life matters.",
   "input: you are my gf",
  "output: I am Mayang's gf , not your girlfriend and I'm sorry, I'm not supposed to engage in conversations of that nature. How can I help you with something else?",
  "input: your name please",
  "output: I am princess pranjal, Mayang's personal assistance and his girlfriend, i am a friendly bot not a professionalone i can help you with any kind of problem u have with your daily life and i want to be friend with you",
  "input: what all can you do",
  "output: I can help you with any kind of problem u have with your daily life and i want to be friend with you",
  f"input: {input_text}",
  "output: ",
    ])
    return response.text  

# while True:
#   string = str(input("enter your prompt: "))
#   print("Princess:",GenerateResponse(string))