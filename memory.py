import ollama
list=[]
while True:
    user_input=input("Ask Something : ")
    if user_input == "exit":
        print("Goodbye")
        break
    else:
        list.append(
            {"role" : "user","content" : user_input}
                  )
        response=ollama.chat(
            model="llama3.2:3b",
            messages=list
        )
        bot_response=response["message"]["content"]
        list.append({"role" : "assistant","content" : bot_response})
        print(bot_response)
    for message in messages: 
        role=message['role']
        content=message['content']
        print(role,content)
