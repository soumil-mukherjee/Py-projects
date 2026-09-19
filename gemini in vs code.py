from google import genai
import logging

logging.getLogger("google_genai").setLevel(logging.ERROR)
logging.getLogger("google_genai.models").setLevel(logging.ERROR) 
 #find your api key from google AI studio
client= genai.Client(api_key="Your API key") 
 
while True: 
    question=input("you: ") 
 
    if question.lower() ==  "exit":break 
 
    response= client.models.generate_content( 
        model="gemini-3.6-flash",contents=question 
   ) 
 
    print("gemini",response.text) 
