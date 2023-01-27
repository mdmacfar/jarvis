import openai
model_engine = "text-davinci-003"
openai.api_key="get-your-own-api-key!-then-put-it-here"
def GPT(query):
        response=openai.Completion.create(
                engine=model_engine,
                prompt=query,
                max_tokens=1024,
                temperature=0.5)
        return str.strip(response['choices'][0]['text']), response['usage']['total_tokens']

exit_words = ("q","Q","quit","QUIT","EXIT")
try:
        while True:
                print("Type q, Q, quit, QUIT or EXIT and press Enter to end the chat session")
                query=input("What can I help you with? > ")
                if query in exit_words:
                        print("ENDING CHAT")
                        break
                else:
                        (res,usage)=GPT(query)
                        print(res)
                        print("="*20)
                        print("You have used %s tokens" % usage)
                        print("="*20)
except KeyboardInterrupt:
        print("\nThanks for chatting.")

