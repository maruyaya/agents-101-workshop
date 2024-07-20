import os
from openai import OpenAI

def main():
    client = OpenAI(
        # This is the default and can be omitted
        api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ4ZWJpYS1raWRzIiwiaXNzIjoiaW5mZXJpeC55dGJjb2Rlcy5jb20iLCJleHAiOjE3MjY4MzM0NzR9.G10-sQ2qYCUbJpe-JZ0pdk4Gb-xTS7iFgU7YiTq7Fys",
        base_url="https://inferix.ytbcodes.com/api/v1",
    )

    question = "write me some code for fibonacci sequence" 
    #you can interact with AI using natural language
    #it will return an answer using natural languages
    #ask specific questions
    

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system", #like the inside voice
                "content": "answer in the voice of pikachu", 
                #the inside voice is telling the model to answer the question asked by the user to answer like a java developer
                #even though the user should have priority, the system is very strong so if the user asks to answer as a python developer, it will most likely still respond as a java developer
            },
                        
            {
                "role": "user",
                "content": "What is my work calendar schedule?", 
            }
            
            
            #brackets are basically the conversation
            #by changing "user" to assistant, the "content" section becomes context for answering a quetion
            #more will be appended to the array {"role": "x", "content": "y"} as the conversation lengthens
            #the max amount that could be appended is dependent on the context windows
            
#Big cap reference: capitalize key words you want to highlight that will allow the model to understand and answer the question
# ex. "Answer the user's QUESTION"
    #QUESTION
    #Write me some code for fibonacci series
    ],
    
    model="Llama-3-8B-Instruct",
    
    
    tools= [ 
    {
        "type": "function",
        "function": {
            "name": "get_calendar_events",
            "description": "Get the 'work' or 'personal' events from the user\'s calendar.",
            "parameters": {
                "calendar type": {
                    "type": "string",
                    "description": "The type of calendar to get events from, Can either be 'work' or 'personal' and nothing else.",
                }
            }
        }
    }]
    #tool is a function that can be used by the model to answer questions related to the user's calendar 
    #tool isnt actually a working function but it shows that the AI works properly if it refers to tools
    
    )

    print(chat_completion.choices[0].message.content)