
import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables in a file called .env

load_dotenv(override=True)
api_key = os.getenv('GROQ_API_KEY')

# Check the key

if not api_key:
    print("No API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!")
elif not api_key.startswith("gsk_"):
    print("An API key was found, but it doesn't start sk-proj-; please check you're using the right key - see troubleshooting notebook")
elif api_key.strip() != api_key:
    print("An API key was found, but it looks like it might have space or tab characters at the start or end - please remove them - see troubleshooting notebook")
else:
    print("API key found and looks good so far!")


groqai = Groq()
message = "Hello, Groq! This is my first ever message to you! Hi!"
response = groqai.chat.completions.create(model="meta-llama/llama-4-scout-17b-16e-instruct", messages=[{"role":"user", "content":message}])
print(response.choices[0].message.content)