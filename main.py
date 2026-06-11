import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse
#The imports.

def command_line_input():
    #Take input from the command line
    parser = argparse.ArgumentParser(description="parse user input")
    parser.add_argument("user_input",type=str,help="enter input")
    parser.add_argument("--verbose",action="store_true",help="verbose output")
    result = parser.parse_args()
    return result

def loading_environmental_variables():
    #In order to load the API key 
    load_dotenv()

    API_KEY = os.environ.get("GEMINI_API_KEY")
    if API_KEY == None:
        raise RuntimeError("Huston, We have a problem.")
    return API_KEY




def printing_information(results,result):
    prompt_tokens = results.usage_metadata.prompt_token_count
    response_tokens = results.usage_metadata.candidates_token_count
    if result.verbose == True:
        print(f"User prompt: {result.user_input}")
        print(f"Prompt tokens: {prompt_tokens}\nResponse tokens: {response_tokens}")
    print(results.text)



result = command_line_input()
#store the questions here
message = [types.Content(role="user",parts=[types.Part(text=result.user_input)])]

API_KEY = loading_environmental_variables()


#Instantiate the agent.
client = genai.Client(api_key=API_KEY)
results =client.models.generate_content(model="gemini-2.5-flash",contents=message)
if results.usage_metadata == None:
    raise RuntimeError("API problem.")


printing_information(results,result)


def main():
    print("Hello from ai-agent!")


if __name__ == "__main__":
    main()
