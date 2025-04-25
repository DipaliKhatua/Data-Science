# # ai_engine.py

# from transformers import AutoModelForCausalLM, AutoTokenizer
# import torch
# import json

# # Load the pre-trained GPT-2 model and tokenizer
# model_name = "gpt2" 
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForCausalLM.from_pretrained(model_name)

# # Read all users from data
# def load_user_data(user_id):
#     with open("data/users.json", "r") as f:
#         users = json.load(f)
#     for user in users:
#         if str(user["id"]) == str(user_id):  # Ensure type consistency
#             return user
#     return None

# # Create a prompt based on the user’s personality
# def generate_persona_prompt(user, message):
#     intro = f"You are {user['name']}, a person who loves {', '.join(user['interests'])}.\n"
#     bio = f"Bio: {user['bio']}\n"
#     writing_style = "\n".join(user["writing_samples"])
#     prompt = (
#         f"{intro}{bio}Here are some things you’ve said:\n"
#         f"{writing_style}\n\n"
#         f"Now respond to the following message in your style:\n"
#         f"User: {message}\n{user['name']}:"
#     )
#     return prompt

# # Generate AI response using the GPT-2 model
# def get_ai_reply(user_id, message):
#     user = load_user_data(user_id)
#     if not user:
#         return "User not found."

#     prompt = generate_persona_prompt(user, message)

#     # Tokenize the input prompt
#     input_ids = tokenizer.encode(prompt, return_tensors="pt")
#     attention_mask = torch.ones(input_ids.shape, dtype=torch.long)  # Fix attention mask warning

#     # Generate the output with sampling enabled
#     output = model.generate(
#         input_ids,
#         attention_mask=attention_mask,
#         max_length=150,
#         num_return_sequences=1,
#         pad_token_id=tokenizer.eos_token_id,
#         no_repeat_ngram_size=2,
#         temperature=0.8,  # Adjust for creativity
#         top_p=0.9,
#         do_sample=True  # Enable sampling
#     )

#     # Decode the output and extract the response part
#     response = tokenizer.decode(output[0], skip_special_tokens=True)
    
#     # Extract only the part after the prompt
#     return response[len(prompt):].strip()

# if __name__ == "__main__":
#     reply = get_ai_reply(user_id=1, message="What's your opinion on AI and poetry?")
#     print("🤖 AI Reply:", reply)


# ai_engine.py
import random

# Example of a simplified user database for testing purposes
users_data = {
    1: {
        "name": "Dipali Khatua",
        "interests": ["AI", "Machine Learning", "Poetry", "Data Engineering"],
        "personality": "Curious, Analytical, and Creative",
        "preferred_tone": "Professional and insightful"
    },
    2: {
        "name": "John Doe",
        "interests": ["Travel", "Photography", "Cooking"],
        "personality": "Easy-going, Adventurous",
        "preferred_tone": "Casual and fun"
    }
}

# Function to generate AI response based on user's profile
def get_ai_reply(user_id, message):
    user = users_data.get(user_id)

    if not user:
        return "Sorry, I couldn't find your persona."

    # Get user details
    name = user['name']
    interests = ", ".join(user['interests'])
    personality = user['personality']
    tone = user['preferred_tone']

    # Generate the AI reply (simple logic for now, can be more sophisticated later)
    responses = [
        f"Hello {name}, you seem to be interested in {interests}. Based on your personality as {personality}, here’s my take on your question: {message}.",
        f"{message}? I believe as a {personality} person like you, the answer could be: {message}. You might also enjoy learning about {interests}.",
        f"As a {personality} individual, {name}, your approach to {message} might be unique. Here's my response: {message}. Let me know what you think about this!",
    ]
    
    # Return a response with some personality
    return random.choice(responses)
