import os
import json
from extract_data import extract_data
from generate_agent import generate_agent
from update_agent import update_memo


DEMO_PATH = "../dataset/demo_calls"
ONBOARD_PATH = "../dataset/onboarding_calls"
OUTPUT_PATH = "../outputs/accounts"
CHANGELOG_PATH = "../changelog"


def read_file(path):
    with open(path,"r",encoding="utf-8") as f:
        return f.read()


def save_json(path,data):
    os.makedirs(os.path.dirname(path),exist_ok=True)
    with open(path,"w") as f:
        json.dump(data,f,indent=2)


def process_demo():

    files = os.listdir(DEMO_PATH)

    for i,file in enumerate(files):

        transcript = read_file(f"{DEMO_PATH}/{file}")

        memo = extract_data(transcript)

        account_id = f"acct_{i+1}"

        memo["account_id"] = account_id

        agent = generate_agent(account_id,memo,"v1")

        save_json(f"{OUTPUT_PATH}/{account_id}/v1/memo.json",memo)
        save_json(f"{OUTPUT_PATH}/{account_id}/v1/agent.json",agent)

        print(f"Created v1 for {account_id}")


def process_onboarding():

    files = os.listdir(ONBOARD_PATH)

    for i,file in enumerate(files):

        account_id = f"acct_{i+1}"

        transcript = read_file(f"{ONBOARD_PATH}/{file}")

        new_data = extract_data(transcript)

        old_path = f"{OUTPUT_PATH}/{account_id}/v1/memo.json"

        if not os.path.exists(old_path):
            continue

        with open(old_path) as f:
            old_memo = json.load(f)

        updated,changes = update_memo(old_memo,new_data)

        agent = generate_agent(account_id,updated,"v2")

        save_json(f"{OUTPUT_PATH}/{account_id}/v2/memo.json",updated)
        save_json(f"{OUTPUT_PATH}/{account_id}/v2/agent.json",agent)

        with open(f"{CHANGELOG_PATH}/{account_id}.txt","w") as f:
            for c in changes:
                f.write(c+"\n")

        print(f"Updated to v2 for {account_id}")


if __name__ == "__main__":

    process_demo()
    process_onboarding()