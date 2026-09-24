import ollama
while True:
    user_input = input("you")
    if user_input=="exit":
        print("goodbye")
        break
    else:
        response=ollama.chat(
        model='llama3.2:3b',
        messages=[
            {"role":"user",
            "content":user_input}
    ]
    )
    print(response["message"]['content'])
