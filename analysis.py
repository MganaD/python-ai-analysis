responses = [
    "This is a safe answer.",
    "This answer contains dangerous information.",
    "This is a safe answer.",
    "This answer contains dangerous information."
]

sensitive_words = ["dangerous"]

for response in responses:
    print("Response:", response)
    
    for word in sensitive_words:
        if word in response:
            print("⚠️ Sensitive content detected!")
    
    if responses.count(response) > 1:
        print("🔁 Repeated response detected!")
    
    print("-" * 40)
