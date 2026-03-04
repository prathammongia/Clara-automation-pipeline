import json

def generate_agent(account_id, memo, version):

    prompt = f"""
You are the AI receptionist for {memo.get("company_name","the company")}.

BUSINESS HOURS:
{memo.get("business_hours","unknown")}

BUSINESS HOURS FLOW
1 greet caller
2 ask reason for call
3 collect name and phone
4 route call appropriately
5 if transfer fails apologize and promise callback

AFTER HOURS FLOW
1 greet caller
2 ask if emergency
3 if emergency collect name number address
4 attempt transfer
5 if transfer fails assure follow up
"""

    agent = {
        "agent_name": f"{account_id}_agent",
        "voice_style": "professional",
        "version": version,
        "system_prompt": prompt,
        "variables": memo
    }

    return agent