import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

def main():
  client = OpenAI(
    base_url=os.getenv('BASE_URL'),
    api_key=os.getenv('OPENAI_API_KEY')
  )

  completion = client.chat.completions.create(
    model='',
    messages=[

    ],
    temperature=0.5,
    tools=[
      {
        'type':'function',
        'function':{
          'name':'',
          'description':'',
          'parameters':[
          
          ],
          'strict':True
        }
      }
    ]
  )
