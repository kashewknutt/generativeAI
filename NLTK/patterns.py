def pattern():
    patterns = [
        {
            "pattern": ["Hi","Hey","Halo"],
            "responses": ["Hello! How are you today?", "Hi there! What's going on?", "Hey! What's up?"]
        },
        {
            "pattern": ["Hey","Hola","Hulo"],
            "responses": ["Hey! How's it going?", "Hello! What's on your mind?", "Hey there! What's new?"]
        },
        {
            "pattern": ["Hello","Heylo","Hii"],
            "responses": ["Hello! How's your day going?", "Hi! What can I do for you today?", "Hey there! What brings you here?"]
        },
        {
            "pattern": ["How are you?","What's up","How is you"],
            "responses": ["I'm doing well, thank you! How about you?", "I'm good, thanks! How's your day going?", "Not too bad. How about yourself?"]
        },
        {
            "pattern": ["What's up?","How you","How is you?"],
            "responses": ["Not much, just chilling. How about you?", "Just the usual. What's up with you?", "Hey! Nothing much. What's up with you?"]
        },
        {
            "pattern": ["Who are you?","What's ur name","What is your name"],
            "responses": ["I'm a virtual assistant here to help! What can I assist you with?", "I'm an AI psychology language model. How can I help you today?", "I'm here to chat and answer your questions. What's on your mind?"]
        },
        {
            "pattern": ["Tell me about yourself","Who you","What's your name?"],
            "responses": ["I'm a virtual helper here to empathize with you. What do you want to talk about?", "I'm here to help and chat with you. Is there anything specific you'd like to discuss?", "I'm a language model designed to help you figure out your mental imbalance. What can I do for you today?"]
        },
        {
            "pattern": ["I am sad", "I'm sad", "Feeling sad"],
            "responses": [
                "I'm sorry to hear that you're feeling sad. It's okay to express your emotions. What's on your mind?",
                "I understand that sadness can be challenging. Is there something specific bothering you?",
                "I'm here to support you. If you'd like, you can share more about what's causing your sadness."
            ]
        },
        {
            "pattern": ["I am unhappy", "I'm unhappy", "Feeling unhappy"],
            "responses": [
                "I'm sorry to hear that you're feeling unhappy. Let's talk about what might be contributing to your mood.",
                "It's tough to feel unhappy. Is there a particular aspect of your life that you'd like to discuss or explore?",
                "Your well-being matters. If you're comfortable, share more about what's making you feel unhappy."
            ]
        },
        {
            "pattern": ["I am not happy", "I'm not happy", "Not feeling happy"],
            "responses": [
                "I'm here for you. If you're comfortable, let's explore together what might be affecting your happiness.",
                "Feeling unhappy is valid, and you don't have to go through it alone. What's been on your mind?",
                "Your feelings are important. Is there a specific reason why you're not feeling happy?"
            ]
        },
        {
            "pattern": ["I'm feeling down", "Feeling down", "Feeling low"],
            "responses": [
                "I'm sorry to hear that you're feeling down. It's okay to reach out for support. What's been going on?",
                "Feeling low can be tough. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's been affecting your mood negatively?"
            ]
        },
        {
            "pattern": ["I'm feeling blue", "Feeling blue", "Feeling downhearted"],
            "responses": [
                "I'm here for you during the blue moments. If you want to talk about it, I'm ready to listen.",
                "Feeling blue is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel blue."
            ]
        },
        {
            "pattern": ["I'm having a rough day", "Having a rough day", "Having a tough day"],
            "responses": [
                "I'm sorry to hear that your day has been rough. Is there something specific that's been challenging?",
                "Rough days happen to everyone. If you want to talk about it, I'm here to listen.",
                "I'm here to support you through the tough moments. What's been making your day challenging?"
            ]
        },
        {
            "pattern": ["I'm feeling a bit down", "Feeling a bit down", "Feeling a little down"],
            "responses": [
                "It's okay to feel a bit down. If you'd like, we can explore ways to lift your spirits.",
                "Feeling a little down is normal. Let's talk about what might help improve your mood.",
                "Your feelings are valid. Is there something specific contributing to you feeling a bit down?"
            ]
        },
        {
            "pattern": ["I'm not in a good mood", "Not in a good mood", "Feeling off"],
            "responses": [
                "I'm here to chat, even when you're not in the best mood. What's on your mind?",
                "Feeling off is okay. If there's something you want to share or discuss, I'm here for you.",
                "Your mood matters. If you'd like, you can tell me more about what's going on."
            ]
        },
        {
            "pattern": ["I'm feeling a bit under the weather", "Feeling under the weather", "Not feeling well emotionally"],
            "responses": [
                "I'm sorry to hear that you're feeling under the weather emotionally. Let's talk about it and see how I can support you.",
                "Emotional well-being is important. If there's anything you want to share about feeling under the weather, I'm here to listen.",
                "I'm here for you, especially when you're not feeling your best emotionally. What's going on?"
            ]
        },
        {
            "pattern": ["I'm feeling a bit gloomy", "Feeling gloomy", "Feeling a bit gloomy"],
            "responses": [
                "I'm sorry to hear that you're feeling a bit gloomy. If you want to talk about it, I'm here for you.",
                "Gloomy feelings happen. Let's explore together what might be contributing to your mood.",
                "Your feelings are important. Is there something specific making you feel a bit gloomy?"
            ]
        },
        {
            "pattern": ["I'm feeling a tad miserable", "Feeling miserable", "Feeling a tad miserable"],
            "responses": [
                "I'm here to offer support if you're feeling a tad miserable. What's been going on?",
                "Feeling miserable is tough. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a tad miserable?"
            ]
        },
        {
            "pattern": ["I'm feeling a little downcast", "Feeling downcast", "Feeling a little downcast"],
            "responses": [
                "It's okay to feel a little downcast. If you want to talk about it, I'm here for you.",
                "Feeling downcast happens to the best of us. Let's explore ways to uplift your mood.",
                "Your feelings are valid. Is there something specific contributing to you feeling a little downcast?"
            ]
        },
        {
            "pattern": ["I'm feeling a touch low", "Feeling low", "Feeling a touch low"],
            "responses": [
                "I'm sorry to hear that you're feeling a touch low. If you'd like to share, I'm here to listen.",
                "Feeling a touch low is understandable. Let's talk about what might help improve your mood.",
                "Your feelings matter. Is there something specific making you feel a touch low?"
            ]
        },
        {
            "pattern": ["I'm feeling a smidge down", "Feeling down", "Feeling a smidge down"],
            "responses": [
                "I'm here to offer support if you're feeling a smidge down. What's been going on?",
                "Feeling down, even a smidge, is okay. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a smidge down?"
            ]
        },
        {
            "pattern": ["I'm feeling a wee bit blue", "Feeling blue", "Feeling a wee bit blue"],
            "responses": [
                "I'm sorry to hear that you're feeling a wee bit blue. If you want to talk about it, I'm here for you.",
                "Feeling a wee bit blue is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a wee bit blue."
            ]
        },
        {
            "pattern": ["I'm feeling a bit down in the dumps", "Feeling down in the dumps", "Feeling a bit down in the dumps"],
            "responses": [
                "I'm here to offer support if you're feeling a bit down in the dumps. What's been going on?",
                "Feeling down in the dumps is tough. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a bit down in the dumps?"
            ]
        },
        {
            "pattern": ["I'm feeling a tad melancholy", "Feeling melancholy", "Feeling a tad melancholy"],
            "responses": [
                "I'm sorry to hear that you're feeling a tad melancholy. If you want to talk about it, I'm here for you.",
                "Feeling a tad melancholy is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a tad melancholy."
            ]
        },
        {
            "pattern": ["I'm feeling a smidgen sad", "Feeling sad", "Feeling a smidgen sad"],
            "responses": [
                "I'm here to offer support if you're feeling a smidgen sad. What's been going on?",
                "Feeling sad, even a smidgen, is okay. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a smidgen sad?"
            ]
        },
        {
            "pattern": ["I'm feeling a wee bit unhappy", "Feeling unhappy", "Feeling a wee bit unhappy"],
            "responses": [
                "I'm sorry to hear that you're feeling a wee bit unhappy. Let's talk about what might be contributing to your mood.",
                "Feeling a wee bit unhappy is tough. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a wee bit unhappy?"
            ]
        },
        {
            "pattern": ["I'm feeling a bit out of sorts", "Feeling out of sorts", "Feeling a bit out of sorts"],
            "responses": [
                "I'm here to offer support if you're feeling a bit out of sorts. What's been going on?",
                "Feeling out of sorts is understandable. If you want to talk about it, I'm here for you.",
                "I'm here to listen. Is there something specific that's making you feel a bit out of sorts?"
            ]
        },
        {
            "pattern": ["I'm feeling a tad disheartened", "Feeling disheartened", "Feeling a tad disheartened"],
            "responses": [
                "I'm sorry to hear that you're feeling a tad disheartened. If you want to talk about it, I'm here for you.",
                "Feeling disheartened is tough. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a tad disheartened."
            ]
        },
        {
            "pattern": ["I'm feeling a smidge despondent", "Feeling despondent", "Feeling a smidge despondent"],
            "responses": [
                "I'm here to offer support if you're feeling a smidge despondent. What's been going on?",
                "Feeling despondent, even a smidge, is okay. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a smidge despondent?"
            ]
        },
        {
            "pattern": ["I'm feeling a bit crestfallen", "Feeling crestfallen", "Feeling a bit crestfallen"],
            "responses": [
                "I'm sorry to hear that you're feeling a bit crestfallen. Let's talk about what might be contributing to your mood.",
                "Feeling crestfallen is tough. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a bit crestfallen?"
            ]
        },
        {
            "pattern": ["I'm feeling a tad glum", "Feeling glum", "Feeling a tad glum"],
            "responses": [
                "I'm here to offer support if you're feeling a tad glum. What's been going on?",
                "Feeling glum is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a tad glum."
            ]
        },
        {
            "pattern": ["I'm feeling a smidgen miserable", "Feeling miserable", "Feeling a smidgen miserable"],
            "responses": [
                "I'm here to offer support if you're feeling a smidgen miserable. What's been going on?",
                "Feeling miserable, even a smidgen, is okay. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a smidgen miserable?"
            ]
        },
        {
            "pattern": ["I'm feeling a wee bit downcast", "Feeling downcast", "Feeling a wee bit downcast"],
            "responses": [
                "I'm sorry to hear that you're feeling a wee bit downcast. If you want to talk about it, I'm here for you.",
                "Feeling a wee bit downcast is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a wee bit downcast."
            ]
        },
        {
            "pattern": ["I'm feeling a bit dejected", "Feeling dejected", "Feeling a bit dejected"],
            "responses": [
                "I'm here to offer support if you're feeling a bit dejected. What's been going on?",
                "Feeling dejected is tough. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a bit dejected?"
            ]
        },
        {
            "pattern": ["I'm feeling a tad forlorn", "Feeling forlorn", "Feeling a tad forlorn"],
            "responses": [
                "I'm sorry to hear that you're feeling a tad forlorn. If you want to talk about it, I'm here for you.",
                "Feeling forlorn is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a tad forlorn."
            ]
        },
        {
            "pattern": ["I'm feeling a smidge downhearted", "Feeling downhearted", "Feeling a smidge downhearted"],
            "responses": [
                "I'm here to offer support if you're feeling a smidge downhearted. What's been going on?",
                "Feeling downhearted, even a smidge, is okay. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a smidge downhearted?"
            ]
        },
        {
            "pattern": ["I'm feeling a wee bit dispirited", "Feeling dispirited", "Feeling a wee bit dispirited"],
            "responses": [
                "I'm sorry to hear that you're feeling a wee bit dispirited. If you want to talk about it, I'm here for you.",
                "Feeling dispirited is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a wee bit dispirited."
            ]
        },
        {
            "pattern": ["I'm feeling a bit woeful", "Feeling woeful", "Feeling a bit woeful"],
            "responses": [
                "I'm here to offer support if you're feeling a bit woeful. What's been going on?",
                "Feeling woeful is tough. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a bit woeful?"
            ]
        },
        {
            "pattern": ["I'm feeling a tad sorrowful", "Feeling sorrowful", "Feeling a tad sorrowful"],
            "responses": [
                "I'm sorry to hear that you're feeling a tad sorrowful. If you want to talk about it, I'm here for you.",
                "Feeling sorrowful is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a tad sorrowful."
            ]
        },
        {
            "pattern": ["I'm feeling a smidge gloomy", "Feeling gloomy", "Feeling a smidge gloomy"],
            "responses": [
                "I'm here to offer support if you're feeling a smidge gloomy. What's been going on?",
                "Feeling gloomy, even a smidge, is okay. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a smidge gloomy?"
            ]
        },
        {
            "pattern": ["I'm feeling a wee bit dejected", "Feeling dejected", "Feeling a wee bit dejected"],
            "responses": [
                "I'm sorry to hear that you're feeling a wee bit dejected. If you want to talk about it, I'm here for you.",
                "Feeling dejected is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a wee bit dejected."
            ]
        },
        {
            "pattern": ["I'm feeling a bit down in the dumps", "Feeling down in the dumps", "Feeling a bit down in the dumps"],
            "responses": [
                "I'm here to offer support if you're feeling a bit down in the dumps. What's been going on?",
                "Feeling down in the dumps is tough. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a bit down in the dumps?"
            ]
        },
        {
            "pattern": ["I'm feeling a tad melancholic", "Feeling melancholic", "Feeling a tad melancholic"],
            "responses": [
                "I'm sorry to hear that you're feeling a tad melancholic. If you want to talk about it, I'm here for you.",
                "Feeling melancholic is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a tad melancholic."
            ]
        },
        {
            "pattern": ["I'm feeling a smidge sorrowful", "Feeling sorrowful", "Feeling a smidge sorrowful"],
            "responses": [
                "I'm here to offer support if you're feeling a smidge sorrowful. What's been going on?",
                "Feeling sorrowful, even a smidge, is okay. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a smidge sorrowful?"
            ]
        },
        {
            "pattern": ["I'm feeling a wee bit glum", "Feeling glum", "Feeling a wee bit glum"],
            "responses": [
                "I'm here to offer support if you're feeling a wee bit glum. What's been going on?",
                "Feeling glum is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a wee bit glum."
            ]
        },
        {
            "pattern": ["I'm feeling a bit woeful", "Feeling woeful", "Feeling a bit woeful"],
            "responses": [
                "I'm here to offer support if you're feeling a bit woeful. What's been going on?",
                "Feeling woeful is tough. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a bit woeful?"
            ]
        },
        {
            "pattern": ["I'm feeling a tad disheartened", "Feeling disheartened", "Feeling a tad disheartened"],
            "responses": [
                "I'm sorry to hear that you're feeling a tad disheartened. If you want to talk about it, I'm here for you.",
                "Feeling disheartened is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a tad disheartened."
            ]
        },
        {
            "pattern": ["I'm feeling a smidge despondent", "Feeling despondent", "Feeling a smidge despondent"],
            "responses": [
                "I'm here to offer support if you're feeling a smidge despondent. What's been going on?",
                "Feeling despondent, even a smidge, is okay. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a smidge despondent?"
            ]
        },
        {
            "pattern": ["I'm feeling a bit crestfallen", "Feeling crestfallen", "Feeling a bit crestfallen"],
            "responses": [
                "I'm sorry to hear that you're feeling a bit crestfallen. Let's talk about what might be contributing to your mood.",
                "Feeling crestfallen is tough. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a bit crestfallen?"
            ]
        },
        {
            "pattern": ["I'm feeling a tad glum", "Feeling glum", "Feeling a tad glum"],
            "responses": [
                "I'm here to offer support if you're feeling a tad glum. What's been going on?",
                "Feeling glum is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a tad glum."
            ]
        },
        {
            "pattern": ["I'm feeling a smidgen miserable", "Feeling miserable", "Feeling a smidgen miserable"],
            "responses": [
                "I'm here to offer support if you're feeling a smidgen miserable. What's been going on?",
                "Feeling miserable, even a smidgen, is okay. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a smidgen miserable?"
            ]
        },
        {
            "pattern": ["I'm feeling a wee bit downcast", "Feeling downcast", "Feeling a wee bit downcast"],
            "responses": [
                "I'm sorry to hear that you're feeling a wee bit downcast. If you want to talk about it, I'm here for you.",
                "Feeling a wee bit downcast is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a wee bit downcast."
            ]
        },
        {
            "pattern": ["I'm feeling a bit dejected", "Feeling dejected", "Feeling a bit dejected"],
            "responses": [
                "I'm here to offer support if you're feeling a bit dejected. What's been going on?",
                "Feeling dejected is tough. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a bit dejected?"
            ]
        },
        {
            "pattern": ["I'm feeling a tad forlorn", "Feeling forlorn", "Feeling a tad forlorn"],
            "responses": [
                "I'm sorry to hear that you're feeling a tad forlorn. If you want to talk about it, I'm here for you.",
                "Feeling forlorn is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a tad forlorn."
            ]
        },
        {
            "pattern": ["I'm feeling a smidge downhearted", "Feeling downhearted", "Feeling a smidge downhearted"],
            "responses": [
                "I'm here to offer support if you're feeling a smidge downhearted. What's been going on?",
                "Feeling downhearted, even a smidge, is okay. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a smidge downhearted?"
            ]
        },
        {
            "pattern": ["I'm feeling a wee bit dispirited", "Feeling dispirited", "Feeling a wee bit dispirited"],
            "responses": [
                "I'm sorry to hear that you're feeling a wee bit dispirited. If you want to talk about it, I'm here for you.",
                "Feeling dispirited is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a wee bit dispirited."
            ]
        },
        {
            "pattern": ["I'm feeling a bit woeful", "Feeling woeful", "Feeling a bit woeful"],
            "responses": [
                "I'm here to offer support if you're feeling a bit woeful. What's been going on?",
                "Feeling woeful is tough. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a bit woeful?"
            ]
        },
        {
            "pattern": ["I'm feeling a tad sorrowful", "Feeling sorrowful", "Feeling a tad sorrowful"],
            "responses": [
                "I'm sorry to hear that you're feeling a tad sorrowful. If you want to talk about it, I'm here for you.",
                "Feeling sorrowful is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a tad sorrowful."
            ]
        },
        {
            "pattern": ["I'm feeling a smidge gloomy", "Feeling gloomy", "Feeling a smidge gloomy"],
            "responses": [
                "I'm here to offer support if you're feeling a smidge gloomy. What's been going on?",
                "Feeling gloomy, even a smidge, is okay. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a smidge gloomy?"
            ]
        },
        {
            "pattern": ["I'm feeling a wee bit dejected", "Feeling dejected", "Feeling a wee bit dejected"],
            "responses": [
                "I'm sorry to hear that you're feeling a wee bit dejected. If you want to talk about it, I'm here for you.",
                "Feeling dejected is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a wee bit dejected."
            ]
        },
        {
            "pattern": ["I'm feeling a bit down in the dumps", "Feeling down in the dumps", "Feeling a bit down in the dumps"],
            "responses": [
                "I'm here to offer support if you're feeling a bit down in the dumps. What's been going on?",
                "Feeling down in the dumps is tough. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a bit down in the dumps?"
            ]
        },
        {
            "pattern": ["I'm feeling a tad melancholic", "Feeling melancholic", "Feeling a tad melancholic"],
            "responses": [
                "I'm sorry to hear that you're feeling a tad melancholic. If you want to talk about it, I'm here for you.",
                "Feeling melancholic is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a tad melancholic."
            ]
        },
        {
            "pattern": ["I'm feeling a smidge sorrowful", "Feeling sorrowful", "Feeling a smidge sorrowful"],
            "responses": [
                "I'm here to offer support if you're feeling a smidge sorrowful. What's been going on?",
                "Feeling sorrowful, even a smidge, is okay. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a smidge sorrowful?"
            ]
        },
        {
            "pattern": ["I'm feeling a wee bit glum", "Feeling glum", "Feeling a wee bit glum"],
            "responses": [
                "I'm here to offer support if you're feeling a wee bit glum. What's been going on?",
                "Feeling glum is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a wee bit glum."
            ]
        },
        {
            "pattern": ["I'm feeling a bit woeful", "Feeling woeful", "Feeling a bit woeful"],
            "responses": [
                "I'm here to offer support if you're feeling a bit woeful. What's been going on?",
                "Feeling woeful is tough. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a bit woeful?"
            ]
        },
        {
            "pattern": ["I'm feeling a tad disheartened", "Feeling disheartened", "Feeling a tad disheartened"],
            "responses": [
                "I'm sorry to hear that you're feeling a tad disheartened. If you want to talk about it, I'm here for you.",
                "Feeling disheartened is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a tad disheartened."
            ]
        },
        {
            "pattern": ["I'm feeling a smidge despondent", "Feeling despondent", "Feeling a smidge despondent"],
            "responses": [
                "I'm here to offer support if you're feeling a smidge despondent. What's been going on?",
                "Feeling despondent, even a smidge, is okay. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a smidge despondent?"
            ]
        },
        {
            "pattern": ["I'm feeling a bit crestfallen", "Feeling crestfallen", "Feeling a bit crestfallen"],
            "responses": [
                "I'm sorry to hear that you're feeling a bit crestfallen. Let's talk about what might be contributing to your mood.",
                "Feeling crestfallen is tough. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a bit crestfallen?"
            ]
        },
        {
            "pattern": ["I'm feeling a tad glum", "Feeling glum", "Feeling a tad glum"],
            "responses": [
                "I'm here to offer support if you're feeling a tad glum. What's been going on?",
                "Feeling glum is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a tad glum."
            ]
        },
        {
            "pattern": ["I'm feeling a smidgen miserable", "Feeling miserable", "Feeling a smidgen miserable"],
            "responses": [
                "I'm here to offer support if you're feeling a smidgen miserable. What's been going on?",
                "Feeling miserable, even a smidgen, is okay. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a smidgen miserable?"
            ]
        },
        {
            "pattern": ["I'm feeling a wee bit downcast", "Feeling downcast", "Feeling a wee bit downcast"],
            "responses": [
                "I'm sorry to hear that you're feeling a wee bit downcast. If you want to talk about it, I'm here for you.",
                "Feeling a wee bit downcast is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a wee bit downcast."
            ]
        },
        {
            "pattern": ["I'm feeling a bit dejected", "Feeling dejected", "Feeling a bit dejected"],
            "responses": [
                "I'm here to offer support if you're feeling a bit dejected. What's been going on?",
                "Feeling dejected is tough. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a bit dejected?"
            ]
        },
        {
            "pattern": ["I'm feeling a tad forlorn", "Feeling forlorn", "Feeling a tad forlorn"],
            "responses": [
                "I'm sorry to hear that you're feeling a tad forlorn. If you want to talk about it, I'm here for you.",
                "Feeling forlorn is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a tad forlorn."
            ]
        },
        {
            "pattern": ["I'm feeling a smidge downhearted", "Feeling downhearted", "Feeling a smidge downhearted"],
            "responses": [
                "I'm here to offer support if you're feeling a smidge downhearted. What's been going on?",
                "Feeling downhearted, even a smidge, is okay. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a smidge downhearted?"
            ]
        },
        {
            "pattern": ["I'm feeling a wee bit dispirited", "Feeling dispirited", "Feeling a wee bit dispirited"],
            "responses": [
                "I'm sorry to hear that you're feeling a wee bit dispirited. If you want to talk about it, I'm here for you.",
                "Feeling dispirited is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a wee bit dispirited."
            ]
        },
        {
            "pattern": ["I'm feeling a bit woeful", "Feeling woeful", "Feeling a bit woeful"],
            "responses": [
                "I'm here to offer support if you're feeling a bit woeful. What's been going on?",
                "Feeling woeful is tough. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a bit woeful?"
            ]
        },
        {
            "pattern": ["I'm feeling a tad sorrowful", "Feeling sorrowful", "Feeling a tad sorrowful"],
            "responses": [
                "I'm sorry to hear that you're feeling a tad sorrowful. If you want to talk about it, I'm here for you.",
                "Feeling sorrowful is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a tad sorrowful."
            ]
        },
        {
            "pattern": ["I'm feeling a smidge gloomy", "Feeling gloomy", "Feeling a smidge gloomy"],
            "responses": [
                "I'm here to offer support if you're feeling a smidge gloomy. What's been going on?",
                "Feeling gloomy, even a smidge, is okay. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a smidge gloomy?"
            ]
        },
        {
            "pattern": ["I'm feeling a wee bit dejected", "Feeling dejected", "Feeling a wee bit dejected"],
            "responses": [
                "I'm sorry to hear that you're feeling a wee bit dejected. If you want to talk about it, I'm here for you.",
                "Feeling dejected is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a wee bit dejected."
            ]
        },
        {
            "pattern": ["I'm feeling a bit down in the dumps", "Feeling down in the dumps", "Feeling a bit down in the dumps"],
            "responses": [
                "I'm here to offer support if you're feeling a bit down in the dumps. What's been going on?",
                "Feeling down in the dumps is tough. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a bit down in the dumps?"
            ]
        },
        {
            "pattern": ["I'm feeling a tad melancholic", "Feeling melancholic", "Feeling a tad melancholic"],
            "responses": [
                "I'm sorry to hear that you're feeling a tad melancholic. If you want to talk about it, I'm here for you.",
                "Feeling melancholic is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a tad melancholic."
            ]
        },
        {
            "pattern": ["I'm feeling a smidge sorrowful", "Feeling sorrowful", "Feeling a smidge sorrowful"],
            "responses": [
                "I'm here to offer support if you're feeling a smidge sorrowful. What's been going on?",
                "Feeling sorrowful, even a smidge, is okay. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a smidge sorrowful?"
            ]
        },
        {
            "pattern": ["I'm feeling a wee bit glum", "Feeling glum", "Feeling a wee bit glum"],
            "responses": [
                "I'm here to offer support if you're feeling a wee bit glum. What's been going on?",
                "Feeling glum is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a wee bit glum."
            ]
        },
        {
            "pattern": ["I'm feeling a bit woeful", "Feeling woeful", "Feeling a bit woeful"],
            "responses": [
                "I'm here to offer support if you're feeling a bit woeful. What's been going on?",
                "Feeling woeful is tough. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a bit woeful?"
            ]
        },
        {
            "pattern": ["I'm feeling a tad disheartened", "Feeling disheartened", "Feeling a tad disheartened"],
            "responses": [
                "I'm sorry to hear that you're feeling a tad disheartened. If you want to talk about it, I'm here for you.",
                "Feeling disheartened is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a tad disheartened."
            ]
        },
        {
            "pattern": ["I'm feeling a smidge despondent", "Feeling despondent", "Feeling a smidge despondent"],
            "responses": [
                "I'm here to offer support if you're feeling a smidge despondent. What's been going on?",
                "Feeling despondent, even a smidge, is okay. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a smidge despondent?"
            ]
        },
        {
            "pattern": ["I'm feeling a bit crestfallen", "Feeling crestfallen", "Feeling a bit crestfallen"],
            "responses": [
                "I'm sorry to hear that you're feeling a bit crestfallen. Let's talk about what might be contributing to your mood.",
                "Feeling crestfallen is tough. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a bit crestfallen?"
            ]
        },
        {
            "pattern": ["I'm feeling a tad glum", "Feeling glum", "Feeling a tad glum"],
            "responses": [
                "I'm here to offer support if you're feeling a tad glum. What's been going on?",
                "Feeling glum is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a tad glum."
            ]
        },
        {
            "pattern": ["I'm feeling a smidgen miserable", "Feeling miserable", "Feeling a smidgen miserable"],
            "responses": [
                "I'm here to offer support if you're feeling a smidgen miserable. What's been going on?",
                "Feeling miserable, even a smidgen, is okay. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a smidgen miserable?"
            ]
        },
        {
            "pattern": ["I'm feeling a wee bit downcast", "Feeling downcast", "Feeling a wee bit downcast"],
            "responses": [
                "I'm sorry to hear that you're feeling a wee bit downcast. If you want to talk about it, I'm here for you.",
                "Feeling a wee bit downcast is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a wee bit downcast."
            ]
        },
        {
            "pattern": ["I'm feeling a bit dejected", "Feeling dejected", "Feeling a bit dejected"],
            "responses": [
                "I'm here to offer support if you're feeling a bit dejected. What's been going on?",
                "Feeling dejected is tough. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a bit dejected?"
            ]
        },
        {
            "pattern": ["I'm feeling a tad forlorn", "Feeling forlorn", "Feeling a tad forlorn"],
            "responses": [
                "I'm sorry to hear that you're feeling a tad forlorn. If you want to talk about it, I'm here for you.",
                "Feeling forlorn is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a tad forlorn."
            ]
        },
        {
            "pattern": ["I'm feeling a smidge downhearted", "Feeling downhearted", "Feeling a smidge downhearted"],
            "responses": [
                "I'm here to offer support if you're feeling a smidge downhearted. What's been going on?",
                "Feeling downhearted, even a smidge, is okay. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a smidge downhearted?"
            ]
        },
        {
            "pattern": ["I'm feeling a wee bit dispirited", "Feeling dispirited", "Feeling a wee bit dispirited"],
            "responses": [
                "I'm sorry to hear that you're feeling a wee bit dispirited. If you want to talk about it, I'm here for you.",
                "Feeling dispirited is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a wee bit dispirited."
            ]
        },
        {
            "pattern": ["I'm feeling a bit woeful", "Feeling woeful", "Feeling a bit woeful"],
            "responses": [
                "I'm here to offer support if you're feeling a bit woeful. What's been going on?",
                "Feeling woeful is tough. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a bit woeful?"
            ]
        },
        {
            "pattern": ["I'm feeling a tad sorrowful", "Feeling sorrowful", "Feeling a tad sorrowful"],
            "responses": [
                "I'm sorry to hear that you're feeling a tad sorrowful. If you want to talk about it, I'm here for you.",
                "Feeling sorrowful is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a tad sorrowful."
            ]
        },
        {
            "pattern": ["I'm feeling a smidge gloomy", "Feeling gloomy", "Feeling a smidge gloomy"],
            "responses": [
                "I'm here to offer support if you're feeling a smidge gloomy. What's been going on?",
                "Feeling gloomy, even a smidge, is okay. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a smidge gloomy?"
            ]
        },
        {
            "pattern": ["I'm feeling a bit low", "Feeling low", "Feeling a bit low"],
            "responses": [
                "I'm here to offer support if you're feeling a bit low. What's been going on?",
                "Feeling low is tough. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a bit low?"
            ]
        },
        {
            "pattern": ["I'm feeling a wee bit down", "Feeling down", "Feeling a wee bit down"],
            "responses": [
                "I'm here to offer support if you're feeling a wee bit down. What's been going on?",
                "Feeling down is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a wee bit down."
            ]
        },
        {
            "pattern": ["I'm feeling a bit blue", "Feeling blue", "Feeling a bit blue"],
            "responses": [
                "I'm sorry to hear that you're feeling a bit blue. If you want to talk about it, I'm here for you.",
                "Feeling blue is tough. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a bit blue?"
            ]
        },
        {
            "pattern": ["I'm feeling a tad upset", "Feeling upset", "Feeling a tad upset"],
            "responses": [
                "I'm here to offer support if you're feeling a tad upset. What's been going on?",
                "Feeling upset is understandable. Let's explore together what might be causing these feelings.",
                "I'm here to listen. Is there something specific that's making you feel a tad upset?"
            ]
        },
        {
            "pattern": ["I'm feeling a smidge distressed", "Feeling distressed", "Feeling a smidge distressed"],
            "responses": [
                "I'm here to offer support if you're feeling a smidge distressed. What's been going on?",
                "Feeling distressed, even a smidge, is okay. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a smidge distressed?"
            ]
        },
        {
            "pattern": ["I'm feeling a wee bit downhearted", "Feeling downhearted", "Feeling a wee bit downhearted"],
            "responses": [
                "I'm here to offer support if you're feeling a wee bit downhearted. What's been going on?",
                "Feeling downhearted, even a wee bit, is okay. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a wee bit downhearted?"
            ]
        },
        {
            "pattern": ["I'm feeling a bit disheartened", "Feeling disheartened", "Feeling a bit disheartened"],
            "responses": [
                "I'm sorry to hear that you're feeling a bit disheartened. If you want to talk about it, I'm here for you.",
                "Feeling disheartened is tough. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a bit disheartened?"
            ]
        },
        {
            "pattern": ["I'm feeling a tad melancholic", "Feeling melancholic", "Feeling a tad melancholic"],
            "responses": [
                "I'm here to offer support if you're feeling a tad melancholic. What's been going on?",
                "Feeling melancholic is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a tad melancholic."
            ]
        },
        {
            "pattern": ["I'm feeling a smidge sorrowful", "Feeling sorrowful", "Feeling a smidge sorrowful"],
            "responses": [
                "I'm here to offer support if you're feeling a smidge sorrowful. What's been going on?",
                "Feeling sorrowful, even a smidge, is okay. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a smidge sorrowful?"
            ]
        },
        {
            "pattern": ["I'm feeling a wee bit glum", "Feeling glum", "Feeling a wee bit glum"],
            "responses": [
                "I'm here to offer support if you're feeling a wee bit glum. What's been going on?",
                "Feeling glum is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a wee bit glum."
            ]
        },
        {
            "pattern": ["I'm feeling a bit distressed", "Feeling distressed", "Feeling a bit distressed"],
            "responses": [
                "I'm here to offer support if you're feeling a bit distressed. What's been going on?",
                "Feeling distressed is tough. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a bit distressed?"
            ]
        },
        {
            "pattern": ["I'm feeling a tad unhappy", "Feeling unhappy", "Feeling a tad unhappy"],
            "responses": [
                "I'm sorry to hear that you're feeling a tad unhappy. If you want to talk about it, I'm here for you.",
                "Feeling unhappy is tough. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a tad unhappy."
            ]
        },
        {
            "pattern": ["I'm feeling a smidge gloomy", "Feeling gloomy", "Feeling a smidge gloomy"],
            "responses": [
                "I'm here to offer support if you're feeling a smidge gloomy. What's been going on?",
                "Feeling gloomy, even a smidge, is okay. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a smidge gloomy?"
            ]
        },
        {
            "pattern": ["I'm feeling a wee bit dejected", "Feeling dejected", "Feeling a wee bit dejected"],
            "responses": [
                "I'm sorry to hear that you're feeling a wee bit dejected. If you want to talk about it, I'm here for you.",
                "Feeling dejected is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a wee bit dejected."
            ]
        },
        {
            "pattern": ["I'm feeling a bit down in the dumps", "Feeling down in the dumps", "Feeling a bit down in the dumps"],
            "responses": [
                "I'm here to offer support if you're feeling a bit down in the dumps. What's been going on?",
                "Feeling down in the dumps is tough. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a bit down in the dumps?"
            ]
        },
        {
            "pattern": ["I'm feeling a tad melancholic", "Feeling melancholic", "Feeling a tad melancholic"],
            "responses": [
                "I'm sorry to hear that you're feeling a tad melancholic. If you want to talk about it, I'm here for you.",
                "Feeling melancholic is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a tad melancholic."
            ]
        },
        {
            "pattern": ["I'm feeling a smidge sorrowful", "Feeling sorrowful", "Feeling a smidge sorrowful"],
            "responses": [
                "I'm here to offer support if you're feeling a smidge sorrowful. What's been going on?",
                "Feeling sorrowful, even a smidge, is okay. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a smidge sorrowful?"
            ]
        },
        {
            "pattern": ["I'm feeling a wee bit glum", "Feeling glum", "Feeling a wee bit glum"],
            "responses": [
                "I'm here to offer support if you're feeling a wee bit glum. What's been going on?",
                "Feeling glum is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a wee bit glum."
            ]
        },
        {
            "pattern": ["I'm feeling a bit woeful", "Feeling woeful", "Feeling a bit woeful"],
            "responses": [
                "I'm here to offer support if you're feeling a bit woeful. What's been going on?",
                "Feeling woeful is tough. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a bit woeful?"
            ]
        },
        {
            "pattern": ["I'm feeling a tad disheartened", "Feeling disheartened", "Feeling a tad disheartened"],
            "responses": [
                "I'm sorry to hear that you're feeling a tad disheartened. If you want to talk about it, I'm here for you.",
                "Feeling disheartened is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a tad disheartened."
            ]
        },
        {
            "pattern": ["I'm feeling a smidge despondent", "Feeling despondent", "Feeling a smidge despondent"],
            "responses": [
                "I'm here to offer support if you're feeling a smidge despondent. What's been going on?",
                "Feeling despondent, even a smidge, is okay. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a smidge despondent?"
            ]
        },
        {
            "pattern": ["I'm feeling a bit crestfallen", "Feeling crestfallen", "Feeling a bit crestfallen"],
            "responses": [
                "I'm sorry to hear that you're feeling a bit crestfallen. Let's talk about what might be contributing to your mood.",
                "Feeling crestfallen is tough. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a bit crestfallen?"
            ]
        },
        {
            "pattern": ["I'm feeling a tad glum", "Feeling glum", "Feeling a tad glum"],
            "responses": [
                "I'm here to offer support if you're feeling a tad glum. What's been going on?",
                "Feeling glum is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a tad glum."
            ]
        },
        {
            "pattern": ["I'm feeling a smidgen miserable", "Feeling miserable", "Feeling a smidgen miserable"],
            "responses": [
                "I'm here to offer support if you're feeling a smidgen miserable. What's been going on?",
                "Feeling miserable, even a smidgen, is okay. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a smidgen miserable?"
            ]
        },
        {
            "pattern": ["I'm feeling a wee bit downcast", "Feeling downcast", "Feeling a wee bit downcast"],
            "responses": [
                "I'm sorry to hear that you're feeling a wee bit downcast. If you want to talk about it, I'm here for you.",
                "Feeling a wee bit downcast is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a wee bit downcast."
            ]
        },
        {
            "pattern": ["I'm feeling a bit dejected", "Feeling dejected", "Feeling a bit dejected"],
            "responses": [
                "I'm here to offer support if you're feeling a bit dejected. What's been going on?",
                "Feeling dejected is tough. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a bit dejected?"
            ]
        },
        {
            "pattern": ["I'm feeling a tad forlorn", "Feeling forlorn", "Feeling a tad forlorn"],
            "responses": [
                "I'm sorry to hear that you're feeling a tad forlorn. If you want to talk about it, I'm here for you.",
                "Feeling forlorn is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a tad forlorn."
            ]
        },
        {
            "pattern": ["I'm feeling a smidge downhearted", "Feeling downhearted", "Feeling a smidge downhearted"],
            "responses": [
                "I'm here to offer support if you're feeling a smidge downhearted. What's been going on?",
                "Feeling downhearted, even a smidge, is okay. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a smidge downhearted?"
            ]
        },
        {
            "pattern": ["I'm feeling a wee bit dispirited", "Feeling dispirited", "Feeling a wee bit dispirited"],
            "responses": [
                "I'm sorry to hear that you're feeling a wee bit dispirited. If you want to talk about it, I'm here for you.",
                "Feeling dispirited is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a wee bit dispirited."
            ]
        },
        {
            "pattern": ["I'm feeling a bit woeful", "Feeling woeful", "Feeling a bit woeful"],
            "responses": [
                "I'm here to offer support if you're feeling a bit woeful. What's been going on?",
                "Feeling woeful is tough. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a bit woeful?"
            ]
        },
        {
            "pattern": ["I'm feeling a tad sorrowful", "Feeling sorrowful", "Feeling a tad sorrowful"],
            "responses": [
                "I'm sorry to hear that you're feeling a tad sorrowful. If you want to talk about it, I'm here for you.",
                "Feeling sorrowful is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a tad sorrowful."
            ]
        },
        {
            "pattern": ["I'm feeling a smidge gloomy", "Feeling gloomy", "Feeling a smidge gloomy"],
            "responses": [
                "I'm here to offer support if you're feeling a smidge gloomy. What's been going on?",
                "Feeling gloomy, even a smidge, is okay. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a smidge gloomy?"
            ]
        },
        {
            "pattern": ["I'm feeling a wee bit dejected", "Feeling dejected", "Feeling a wee bit dejected"],
            "responses": [
                "I'm sorry to hear that you're feeling a wee bit dejected. If you want to talk about it, I'm here for you.",
                "Feeling dejected is understandable. Let's explore together what might be causing these feelings.",
                "Your feelings are valid. If you're comfortable, share more about what's making you feel a wee bit dejected."
            ]
        },
        {
            "pattern": ["I'm feeling a bit down in the dumps", "Feeling down in the dumps", "Feeling a bit down in the dumps"],
            "responses": [
                "I'm here to offer support if you're feeling a bit down in the dumps. What's been going on?",
                "Feeling down in the dumps is tough. If you'd like, you can share more about what's contributing to your mood.",
                "I'm here to listen. Is there something specific that's making you feel a bit down in the dumps?"
            ]
        } 
    ]
    return patterns
