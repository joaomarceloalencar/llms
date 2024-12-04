import ollama 

response = ollama.chat(
    model="llama3.2",
    messages = [
    {
        'role': 'user',
        'content': 'Why is the sky blue?',
    }],
)

print(response)
print(response['message']['content'])