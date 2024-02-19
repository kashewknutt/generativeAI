def pattern():
    patterns = [
        {
            "pattern": "Hi",
            "responses": ["Hello! How are you today?", "Hi there! What's going on?", "Hey! What's up?"]
        },
        {
            "pattern": "Hey",
            "responses": ["Hey! How's it going?", "Hello! What's on your mind?", "Hey there! What's new?"]
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
                "I'm sorry to hear that you're going through a tough time. Loneliness can be challenging. How can I support you right now?",
                "Feeling alone can be really hard. It's okay to reach out for companionship. Is there anything specific on your mind that you'd like to share?",
                "You're not alone in feeling this way. If you're comfortable, sharing your thoughts and emotions can be a relief. I'm here to listen."
            ]
        },
        {
            "pattern": "I can't handle (stress|pressure|overwhelm)",
            "responses": [
                "It sounds like you're dealing with a lot right now. It's okay to feel overwhelmed. What are some things that usually help you relax?",
                "Managing stress can be tough. Is there anything specific causing the pressure, or do you just need a listening ear right now?",
                "Take a moment for yourself. It's alright to ask for support when things feel too much. How can I assist you in navigating through this stress?"
            ]
        },
        {
            "pattern": "I feel like a failure",
            "responses": [
                "I'm really sorry to hear that you're feeling this way. Remember, everyone faces challenges, and setbacks don't define your worth. What's been going on?",
                "Feeling like a failure can be disheartening. It's important to acknowledge your efforts and not be too hard on yourself. Can you share more about what's on your mind?",
                "You're not alone in feeling this way. Let's explore together the strengths and resilience you have within you. What's been going on that's making you feel like a failure?"
            ]
        },
        {
            "pattern": "I'm having a hard time (forgiving myself|letting go)",
            "responses": [
                "Forgiving oneself can be a difficult journey. It's okay to feel this way. What do you think might help you in the process of forgiving yourself?",
                "Letting go of the past can be challenging, but it's a process. Is there a specific incident or thought that's making it hard for you to move forward?",
                "Remember, everyone makes mistakes. You deserve compassion, especially from yourself. If you're comfortable, share more about what's troubling you."
            ]
        },
        {
            "pattern": "I feel overwhelmed by (responsibilities|workload|expectations)",
            "responses": [
                "It sounds like you have a lot on your plate. It's okay to feel overwhelmed. How can I assist you in breaking down these tasks?",
                "Dealing with high expectations can be challenging. What specific aspects are causing you stress, and is there a way to prioritize or delegate?",
                "You're not alone in feeling this way. Let's explore together some strategies to manage the workload. What aspects are particularly challenging for you?"
            ]
        },
        {
            "pattern": "I'm struggling to (find motivation|stay focused|stay positive)",
            "responses": [
                "Finding motivation can be tough, especially during challenging times. What usually brings you joy or a sense of purpose?",
                "Staying focused can be a struggle. Are there specific distractions or thoughts hindering your concentration that we can address together?",
                "Maintaining a positive outlook is important. Let's explore together some positive aspects or activities that might help lift your spirits. What usually brings you a sense of joy?"
            ]
        },
        {
            "pattern": "I'm feeling (lost|directionless|unsure about the future)",
            "responses": [
                "Feeling lost is a common experience, especially when considering the future. What aspects are causing uncertainty, and how can we work together to bring clarity?",
                "Uncertainty about the future can be overwhelming. It's okay not to have all the answers. What are some small steps we can take to explore your interests and goals?",
                "You're not alone in feeling uncertain. Let's navigate this together. What specific concerns or questions do you have about the future?"
            ]
        },
        {
            "pattern": "I'm dealing with (grief|loss|heartbreak)",
            "responses": [
                "I'm so sorry to hear about your pain. Dealing with grief is a complex process. How can I provide support during this difficult time?",
                "Grieving is a unique journey for everyone. Is there anything specific you'd like to share about the person or situation you're mourning?",
                "You don't have to go through this alone. Let's talk about your feelings and memories. How can I be here for you during this time of grief?"
            ]
        },
        {
            "pattern": "I'm having trouble (setting boundaries|saying no)",
            "responses": [
                "Setting boundaries is important for your well-being. What situations or relationships are challenging your ability to establish boundaries?",
                "It's okay to say no when needed. Let's discuss the specific situations where setting boundaries feels difficult, and how we can approach them together.",
                "Establishing boundaries is a skill that takes practice. What areas of your life do you feel could benefit from clearer boundaries, and how can I support you in setting them?"
            ]
        },
        {
            "pattern": "I'm experiencing (self-doubt|insecurity|low self-esteem)",
            "responses": [
                "Feeling unsure about yourself is something many people go through. What specific thoughts or situations trigger your self-doubt, and how can we address them together?",
                "You are worthy and capable. Let's explore the roots of your self-doubt and work on building a more positive self-image. What strengths and achievements can we celebrate?",
                "Remember, you are not defined by your doubts. What positive qualities or accomplishments do you often overlook, and how can we highlight them together?"
            ]
        },
        {
            "pattern": "I'm having a hard time (letting people in|trusting others)",
            "responses": [
                "Building trust can take time, and it's okay to be cautious. What specific concerns or experiences make it challenging for you to trust others?",
                "Opening up to others can be difficult, especially if trust has been broken before. How can we work together to create a safe space for you to share your thoughts and feelings?",
                "You deserve meaningful connections. Let's explore ways to gradually build trust in relationships. What qualities or actions from others would help you feel more secure?"
            ]
        },
        {
            "pattern": "I feel like I'm (burned out|exhausted|running on empty)",
            "responses": [
                "Burnout is a real challenge, and your well-being is important. What aspects of your life or work are contributing to this feeling of exhaustion?",
                "Taking care of yourself is crucial. What self-care activities or habits can we incorporate to help replenish your energy and prevent burnout?",
                "You're not alone in experiencing burnout. Let's discuss ways to balance your responsibilities and prioritize your well-being. What aspects of your life could use more support or adjustments?"
            ]
        },
        {
            "pattern": "I'm feeling (disconnected|unseen|unheard)",
            "responses": [
                "Feeling disconnected is tough. What aspects of your relationships or environment make you feel unseen, and how can we work together to address them?",
                "Your feelings are valid, and it's important to be heard. Is there a specific situation or conversation where you felt unheard that we can explore together?",
                "You matter, and your experiences are significant. Let's discuss ways to foster connections and ensure that your voice is acknowledged. What steps can we take to help you feel more connected?"
            ]
        },
        {
            "pattern": "I'm dealing with (an illness|health challenges)",
            "responses": [
                "I'm sorry to hear that you're facing health challenges. How can I offer support and assistance during this time?",
                "Dealing with illness can be emotionally and physically draining. Is there anything specific you'd like to share about your experience or concerns?",
                "You don't have to face this alone. Let's discuss ways to navigate through the challenges of illness together. What support or information would be most helpful for you right now?"
            ]
        },
        {
            "pattern": "I've been feeling really anxious lately. It's affecting my daily life.",
            "responses": [
                "I'm sorry to hear that you're experiencing anxiety. It's important to acknowledge your feelings. Is there a specific trigger, or would you like to discuss coping strategies?",
                "Anxiety can be challenging. Taking deep breaths or trying mindfulness exercises might help. What else is on your mind?"
            ]
        },
        {
            "pattern": "I've been feeling down and unmotivated for weeks.",
            "responses": [
                "I'm sorry you're feeling this way. It's essential to reach out for support. Have you considered talking to a friend or seeking professional help?",
                "Feeling down is tough. Let's explore activities that usually bring you joy. If it persists, considering professional assistance is a good option."
            ]
        },
        {
            "pattern": "I've been feeling so lonely lately. It's hard to connect with others.",
            "responses": [
                "Loneliness can be challenging. Connecting with friends or joining social activities might help. Is there something specific making it hard for you to connect?",
                "Feeling alone is tough, but you're not alone in this. Let's discuss ways to foster connections. What interests or hobbies could you explore?"
            ]
        },
        {
            "pattern": "Work has been overwhelming, and I'm feeling a lot of stress.",
            "responses": [
                "I'm sorry to hear about the stress at work. Identifying specific stressors and finding ways to manage them is crucial. What aspects are causing the most pressure?",
                "Work-related stress is common. Prioritizing tasks and incorporating breaks can help. What strategies have you tried, and what do you find challenging?"
            ]
        },
        {
            "pattern": "I often doubt my abilities and feel like I'm not good enough.",
            "responses": [
                "Self-doubt is something many people experience. Let's explore your strengths and achievements. What positive qualities do you often overlook?",
                "Feeling unsure about yourself is common. Acknowledging your accomplishments and setting realistic goals can boost confidence. What achievements are you proud of?"
            ]
        },
        {
            "pattern": "I recently lost someone close, and I'm struggling with grief.",
            "responses": [
                "I'm so sorry for your loss. Grieving is a unique journey. Is there anything specific you'd like to share about the person you're mourning?",
                "Dealing with grief is challenging. Sharing memories and expressing your feelings can be therapeutic. How would you like to remember your loved one?"
            ]
        },
        {
            "pattern": "I find it hard to say no, and I'm struggling with setting boundaries.",
            "responses": [
                "Setting boundaries is important for your well-being. Let's discuss specific situations where saying no feels difficult. What challenges do you face in this area?",
                "Establishing boundaries is a skill that takes practice. What situations or relationships make it challenging for you to set clear boundaries?"
            ]
        },
        {
            "pattern": "I feel burned out and exhausted from work and responsibilities.",
            "responses": [
                "Burnout is a real challenge. Taking breaks and incorporating self-care activities are essential. What aspects of your life could use more support or adjustments?",
                "Your well-being is important. Let's explore ways to balance your responsibilities and prioritize self-care. What activities usually help you relax?"
            ]
        },
    ]
    return patterns