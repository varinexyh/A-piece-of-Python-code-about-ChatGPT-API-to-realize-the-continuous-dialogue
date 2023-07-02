#Created by Varine.




import openai
openai.organization = "YOUR ORGANIZATION CODE"
#Please insert your organization code, if you don't have one, please look up in the official website of the OpenAI.
api_key = "YOUR_API_KEY"
#Please insert your own API key, just as the progress above.
openai.api_key  = api_key
def askChatGPT(messages):
    MODEL = "gpt-3.5-turbo"
    responce = openai.ChatCompletion.create(
        model =MODEL,
        messages = messages,
        temperature = 0.9
    )
    return responce['choices'][0]['message']['content']
def main():
    messages = [{"role" : "user" , "content" : ""}]
    while 1:
        try:
            text = input('user: ')
            if text == 'quit':
                break

            d = {"role" : "user" , "content" : text}
            messages.append(d)
            text = askChatGPT(messages)
            d = {"role" : "user" , "content" : text}
            print('ChatGPT: ' + text + '\n')
            messages.append(d)
        except:
            messages.pop()
            print('ChatGPT: error\n')
main()

