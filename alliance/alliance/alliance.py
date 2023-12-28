from template import Template
import openai
import urllib.parse

class Alliance:
    
    def __init__(self, optimizer, caching=True):
        self.optimizer = optimizer
        self.caching = caching
    
    def route(self, input):
        if isinstance(input, str):
            prompt = f"{self.optimizer}\n{input}"

        elif isinstance(input, Template):
            prompt = f"{self.optimizer}\n{input.render()}"

class AllianceAgent:

    def __init__(self):
        # Import Chat completion template and set-up variable
        openai.api_base = "http://zanino.millennium.berkeley.edu:8000/v1"
        # Alternate mirrors
        # openai.api_base = "http://34.132.127.197:8000/v1"

    # Report issues
    def raise_issue(self, e, model, prompt):
        issue_title = urllib.parse.quote("[bug] Hosted Gorilla: <Issue>")
        issue_body = urllib.parse.quote(f"Exception: {e}\nFailed model: {model}, for prompt: {prompt}")
        issue_url = f"https://github.com/ShishirPatil/gorilla/issues/new?assignees=&labels=hosted-gorilla&projects=&template=hosted-gorilla-.md&title={issue_title}&body={issue_body}"
        print(f"An exception has occurred: {e} \nPlease raise an issue here: {issue_url}")

    # Query Gorilla server
    def get_gorilla_response(self, prompt, model="gorilla-7b-hf-v1"):
        try:
            completion = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
            )
            return completion.choices[0].message.content
        except Exception as e:
            self.raise_issue(e, model, prompt)