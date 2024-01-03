import requests

wallets = []

for wallet in wallets:
    response = requests.get(f"https://geteligibleuserrequest-xqbg2swtrq-uc.a.run.app/?address={wallet}")
    if response.status_code == 200 and response.text.strip():
        try:
            rsp_json = response.json()
            amount = float(rsp_json.get("amount", 0))
            if amount == 0:
                print(f"{wallet} is not eligible")
            else:
                print(f"{wallet} amount: {amount}")
        except ValueError:
            print(f"{wallet} parsing response to json error")
    else:
        print(f"{wallet} is not eligible")
