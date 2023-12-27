# alliance
An intelligent, AI-driven model router ⚡ Powered by [Gorilla](https://github.com/ShishirPatil/gorilla)

**The `alliance` model router package enables natural language AI routing for your workflows over popular LLM endpoints**. 

Simply instaniate the `alliance` object and pass in your prompts with a description of your input and what `alliance` should optimize for.

`alliance` picks the best endpoint to process your input based on the requirements.

No more hardcoded conditional logic or guessing which model is cost efficent or is faster for your use case. The `alliance` object will handle this for you.

```python
from alliance import Alliance

client = Alliance("keep costs down while optimizing for conversation with image generation capabilities", verbose=True)

client.call("Hi! Can you generate an image of a dog and name it for me?")
```

```
DEBUG: selected {some api endpoint}
OUTPUT: This is Leo!
```
![DALL·E 2023-12-26 22 16 08 - create a dog for me](https://github.com/cybertheory/alliance/assets/27149047/4e2d9901-5635-4217-97c3-dc287cf1902b)

## What is Model Routing
After utilizng LLMs for a while you will notice many models sitting behind endpoints are optimized for certain usecases. In order to optimize costs and limited resources for any input it is essential to have some sort of intelligent model routing. 'alliance' offers model routing over all the most popular and some obscure LLMs allowing for one request to be made and utilizing the perfect AI model for the job without any extra work.

## Route Caching
Yes, `alliance` does query the Gorilla LLM everytime it routes. Don't worry about being rate-limited or extra-costs. All routes made by the `alliance` client are cached and stored for future reference. These cached routes are refreshed periodically at much lower rates.

## `alliance_cli`
The `alliance_cli` is a convenience package to help you configure your APIKEYS for different services, so `alliance` can start accessing endpoints and returning generated content from the get go.

**If deploying to external runtimes and set environment variables for api_keys please use `alliance configure --gitignore false ` to set up a _keys.txt file in the correct format with your env variables**

## Config
`alliance` does require an api-key to be provided for every supported service. These can be managed with the `alliance_cli` . **In an ideal world, we would have done this for you automatically and this is under development**  

