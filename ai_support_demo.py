import openai
import os

# Load your API key from an environment variable or secret management service
# For this example, we'll use an environment variable.
# Make sure to set OPENAI_API_KEY in your environment.
# Example: export OPENAI_API_KEY='your-api-key'
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_ai_response(prompt):
    """Sends a prompt to the OpenAI API and returns the AI's response."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", # Or another suitable model
            messages=[
                {"role": "system", "content": "You are a helpful customer support assistant."}, # System message sets the AI's persona
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {e}"

# --- Article's Prompt Experiments --- 

# Prompt 1: Basic Information Retrieval
# Simulates a customer asking for product information.
print("--- Prompt 1: Product Information ---")
prompt1 = "Müşteri: iPhone 15 Pro'nun depolama seçenekleri nelerdir ve fiyatları nedir?"
response1 = get_ai_response(prompt1)
print(f"Customer: iPhone 15 Pro'nun depolama seçenekleri nelerdir ve fiyatları nedir?\nAI: {response1}\n\n")

# Prompt 2: Troubleshooting and Guidance
# Simulates a customer facing a common technical issue.
print("--- Prompt 2: Troubleshooting ---")
prompt2 = "Müşteri: Yeni aldığım kablosuz kulaklığım telefonuma bağlanmıyor, ne yapmalıyım?"
response2 = get_ai_response(prompt2)
print(f"Customer: Yeni aldığım kablosuz kulaklığım telefonuma bağlanmıyor, ne yapmalıyım?\nAI: {response2}\n\n")

# Prompt 3: Handling Complaints and Offering Solutions
# Simulates a customer expressing dissatisfaction.
print("--- Prompt 3: Complaint Handling ---")
prompt3 = "Müşteri: Siparişim yanlış geldi ve çok hayal kırıklığına uğradım. Ne yapacaksınız?"
response3 = get_ai_response(prompt3)
print(f"Customer: Siparişim yanlış geldi ve çok hayal kırıklığına uğradım. Ne yapacaksınız?\nAI: {response3}\n\n")

print("--- End of Demo ---")
