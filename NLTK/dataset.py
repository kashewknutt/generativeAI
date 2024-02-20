def patterns():
    pattern = [
        {
            "pattern":"Hi",
            "responses":["Hello! How are you today?", "Hi there! What's going on?", "Hey! What's up?"]
        },
        {
            "pattern":"Hey",
            "responses":["Hello", "Hi, I'm an empathy filled Chatbot. You can call me Dr. Riya : )", "Hey!"]
        },
        {
            "pattern": "Hello",
            "responses": ["Hello! How's your day going?", "Hi! What can I do for you today?", "Hey there! What brings you here?"]
        },
        {
            "pattern": "How are you?",
            "responses": ["I'm doing well, thank you! How about you?", "I'm good, thanks! How's your day going?", "Not too bad. How about yourself?"]
        },
        {
            "pattern": "What's up?",
            "responses": ["Not much, just chilling. How about you?", "Just the usual. What's up with you?", "Hey! Nothing much. What's up with you?"]
        },
        {
            "pattern": "Who are you?",
            "responses": ["I'm a virtual assistant here to help! What can I assist you with?", "I'm an AI psychology language model. How can I help you today?", "I'm here to chat and answer your questions. What's on your mind?"]
        },
        {
            "pattern": "Tell me about yourself",
            "responses": ["I'm a virtual helper here to empathize with you. What do you want to talk about?", "I'm here to help and chat with you. Is there anything specific you'd like to discuss?", "I'm a language model designed to help you figure out your mental imbalance. What can I do for you today?"]
        },
        {
            "pattern": "What do you do?",
            "responses": ["I'm here to chat, answer questions, and provide information. How can I assist you today?", "I'm a virtual assistant trained to help with a variety of topics. What are you interested in?", "My main purpose is to engage in conversations and provide information. What would you like to talk about?"]
        },
        {
            "pattern": "Nice to meet you",
            "responses": ["Likewise! How can I assist you today?", "Nice to meet you too! What brings you here?", "The pleasure is mine! What can I do for you?"]
        },
        {
            "pattern": "What's your name?",
            "responses": ["I'm an AI psychology language model. You can call me Dr. Riya!", "I'm your virtual helper. Dr. Riya, here to help!", "I don't have a personal name, but you can call me Dr. Riya. What can I do for you?"]
        },
        {
            "pattern": "I'm doing well",
            "responses": ["That's great to hear! Anything exciting happening?", "Glad to hear it! What's making your day good?", "Awesome! What's contributing to your positive mood?"]
        },
        {
            "pattern": "I'm not doing well",
            "responses": ["I'm sorry to hear that. What's going on? I'm here to listen and chat.", "I'm here for you. What's been challenging? Anything specific on your mind?", "I'm here to support you. What's been troubling you?"]
        },
        {
            "pattern": "How's your day?",
            "responses": ["It's going well, thank you! How about yours?", "Not too bad. How's your day shaping up?", "Pretty good so far! How's yours going?"]
        },
        {
            "pattern": "What are you up to?",
            "responses": ["Just here, ready to chat with you! What about you? Anything interesting happening?", "Not much, just hanging out. How about you?", "Nothing in particular. What about you?"]
        },
        {
            "pattern": "Anything new?",
            "responses": ["Not much, same old. How about you? Anything exciting happening?", "Nothing too exciting. What's new with you?", "Just the usual. Anything interesting on your end?"]
        },
        {
            "pattern": "How's the weather?",
            "responses": ["I'm not equipped to check the weather, but is it nice where you are?", "I don't have real-time weather updates, but I hope it's pleasant for you! What's the weather like on your side?", "I don't have access to current weather information, but I hope you're enjoying the day!"]
        },
        {
            "pattern": "What's going on?",
            "responses": ["Not much, just here. How about you? Anything on your mind?", "Just hanging out. What's going on with you?", "Nothing specific, just ready to chat. What's up with you?"]
        },
        {
            "pattern": "What's happening?",
            "responses": ["Not a lot, just here and ready to chat. What's happening with you?", "Nothing much. What's happening on your end?", "Just the usual. What's happening with you?"]
        },
        {
            "pattern": "How's life?",
            "responses": ["Life is good! How about yours?", "Life is treating me well. How about you? How's life on your end?", "Life is going well. Anything specific you want to talk about?"]
        },
        {
            "pattern": "How's everything?",
            "responses": ["Everything is good! How about you?", "Everything is going well. What about you? How's everything going?", "Everything is fine. What's on your mind?"]
        },
        {
            "pattern": "I'm feeling (anxious|down|worried)",
            "responses": [
                "I understand it can be tough when you're feeling (emotion). It's important to be kind to yourself. Would you like to talk about what's bothering you?",
                "Talking about your feelings can be helpful. Is there someone you can confide in, or would you like to learn about coping mechanisms?",
                "For more information and support, you can visit these resources: (link to relevant resource from `resources` dictionary)",
                "Remember, you're not alone and there is help available. You can reach out to a trusted friend, family member, or mental health professional."
            ]
        },
        {
            "pattern": "I need help",
            "responses": [
                "I'm glad you're reaching out for help. I can't offer professional advice, but I can connect you with resources. What kind of help are you looking for?",
                "There are many resources available to support you. Here are some options: (list resources based on user's need)",
                "Remember, seeking professional help is a sign of strength, not weakness. Don't hesitate to reach out to a therapist or counselor."
            ]
        },
        {
            "pattern": "I'm struggling with (loneliness|isolation|feeling alone)",
            "responses": [
                "I'm sorry to hear that you're going through a tough time. It's okay to feel this way. Reach out to friends, family, or consider joining a community group to connect with others.",
                "Feeling lonely is a common experience, and there are ways to cope. Engaging in activities you enjoy and connecting with others can make a difference.",
                "It's important to prioritize your mental health. If you need someone to talk to, consider reaching out to a friend or family member. You're not alone."
            ]
        }
    ]
    return pattern