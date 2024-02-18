def pattern():
    patterns = [
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
    ]
    return patterns