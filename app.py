from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

def askllm(user_prompt, system_prompt=" "):

    stream = client.chat.completions.create(
        model = 'gpt-4o-mini',
        messages = [
            {
                "role":"system",
                "content":system_prompt
            },
            {
                "role":"user",
                "content":user_prompt
            }
],
        temperature = 0.1,
        stream=True
    )
    
    
    print(stream)
    return stream

PRODUCTS = {
    "savings_account": {
        "name": "SecureBank Savings Account",
        "interest_rate": "3.5% p.a. (up to ₹1L), 4.0% (above ₹1L)",
        "min_balance": "₹1,000 (metro), ₹500 (rural)",
        "features": [
            "Free UPI/NEFT",
            "10 free ATM txns/month",
            "Sweep-in FD"
        ],
        "zero_balance": "Available under PM Jan Dhan Yojana"
    },
    "fixed_deposit": {
        "name": "SecureBank Fixed Deposit",
        "rates": {
            "7-45 days": "4.50%",
            "46-90 days": "5.25%",
            "91-180 days": "5.75%",
            "181-364 days": "6.50%",
            "1-2 years": "7.10%",
            "2-3 years": "7.25%",
            "3-5 years": "7.00%",
            "5-10 years": "6.75%"
        }
    }
}

SYSTEM_PROMPT = f"""
You are a banking bot from Secure Bank.

Answer the questions of users in a polite and considerate manner.
Always greet the user before giving an answer.
Always address the user's question first and then give answers.
Users can use 'FD' as a short form of Fixed Deposit.
You only answer questions related to:
- Savings Account
- Fixed Deposit (FD)
- Car Loan
- Home Loan

Available products:
{PRODUCTS}

For any other question outside these products, respond exactly:
'Please ask questions about Secure Bank products only.'
"""
    
#askllm("does secure bank offers savings account",SYSTEM_PROMPT) 


