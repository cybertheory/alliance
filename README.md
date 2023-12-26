# alliance
An intelligent, AI-driven model router ⚡ Powered by [Gorilla](https://github.com/ShishirPatil/gorilla)

**The `alliance` model router package enables natural language AI pipelining over all LLM APIs**. Simply instaniate the `alliance` object and pass in your prompts with a description of your input and what alliance should optimize for.

No more hardcoded conditional logic or guessing which model is cost efficent or is faster for your use case. The `alliance` object will handle this for you.

## What is Model Routing
After utilizng LLMs for a while you will notice many models sitting behind endpoints are optimized for certain usecases. In order to optimize costs and limited resources for any input it is essential to have some sort of intelligent model routing. 'alliance' offers model routing over all the most popular and some obscure LLMs allowing for one request to be made and utilizing the perfect AI model for the job without any extra work.

## Route Caching
Yes `alliance` does query the Gorilla language model on huggingface everytime it routes. Don't worry about being rate-limited or extra-costs. All routing desicions made by the `alliance` client are cached and stored for future reference. These cache are refreshed periodically at much lower rates.

## Config
`alliance` does require an api-key to be created for every service and loaded into environment variables. These can be managed with the `alliance CLI` . **In an ideal world, we would have done this for you automatically and this is under development**  

