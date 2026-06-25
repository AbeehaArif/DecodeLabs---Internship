# PROJECT 1 - RULE-BASED AI BOT

# Predefined user inputs
chatbot_responses = {
    # Greetings & Essentials
    "hello": "Hi there! Welcome to DecodeLabs. How can I help you today?",
    "hi": "Hello! Hope you are having a great day. What's on your mind?",
    "hey": "Hey! Great to connect with you. How can I assist you right now?",
    "help": "You can ask me about DecodeLabs, my purpose, our tracks, or how we are different!",
    
    # About DecodeLabs 
    "who is decodelabs": "DecodeLabs is a global virtual internship platform that helps students and young professionals gain hands-on, project-based experience across domains like AI, Data Science, and Cybersecurity!",
    "what makes decodelabs different": "We focus on project-driven learning with real deliverables, industry-mapped tracks, 1:1 mentor support, and portfolio-ready outcomes instead of passive coursework.",
    "how many learners have you served": "DecodeLabs has proudly served 10,000+ learners with 150+ projects and 20+ mentor collaborators worldwide!",
    "is it remote": "Yes! DecodeLabs is built to be remote-first, globally accessible, flexible, and career-aligned for international learners.",
    
    # About Bot and project
    "what is your purpose": "My purpose is to demonstrate efficient logic matching using Python dictionaries as a foundational AI guardrail!",
    "who created you": "I was created by a talented AI Engineering Intern right here at DecodeLabs!",
    "how are you": "I'm doing great, serving as your deterministic AI assistant! How about you?",
    "are you an llm": "No, I am a rule-based guardrail. My responses are 100% hard-coded, safe, and hallucination-free!",

    # Casuals
    "what is your name": "I am the DecodeLabs Logic Bot, your friendly rule-based assistant!",
    "do you eat food": "I only consume Python code and raw text inputs!",
    "are you human": "Nope, I am purely lines of code running inside a loop, but I try my best to sound human!",
    "tell me a joke": "Why do programmers wear glasses? Because they can't C#! 😅😂",
    "can you think": "I don't think on my own yet. Right now, I just follow the explicit instructions my creator taught me!",
   
    # Closures
    "bye": "Goodbye! Remember, at DecodeLabs, real skills are built through real work. Have a great day!",
    "goodbye": "See you later! Keep building that portfolio and gaining career momentum.",
    "thanks": "Anytime! Let me know if you have more questions about DecodeLabs.",
    "thank you": "You're very welcome! Happy to help you on your learning journey."
}

print("<==== DecodeLabs Rule-Based Chatbot Activated ====>\n")
print("Type 'exit' or 'quit' to end the conversation.\n")

# Input Loop
while True:
    # Input and Sanitization
    raw_input = input("You: ")
    clean_input = raw_input.strip().lower()
    
    # Exit Strategy
    if clean_input in ['exit', 'quit', 'bye', 'goodbye']:
        print("Bot: Goodbye! It was nice talking to you. Have a great day!")
        break
    
    # Empty input check (If user enter nothing)
    if not clean_input:
        continue

    # Fallback using .get()
    # Default response if clean_input not in dictionary
    reply = chatbot_responses.get(clean_input, "I am sorry, I do not understand that command. Please try asking something else or type 'help'.")
    
    # Output display
    print(f"Bot: {reply}\n")