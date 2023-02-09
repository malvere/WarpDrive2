import random

import httpx

base_url = "https://api.cloudflareclient.com"
base_headers = {
    "CF-Client-Version": "a-6.19-2791",
    "Host": "api.cloudflareclient.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/3.12.1",
}

keys = (
    "jd1s6G03-64rVC17U-xd97g64m",
    "tN9u71i3-8sCr5I17-o5qK729l",
    "6K49f0Cu-U27B3io1-5N93Qk4R",
    "8o1s09Nx-j94nE12u-0Jfc584l",
    "41zA9b6Q-0r8fW3g4-di9Mb072",
    "51Yk3CF2-956A8WGp-784YiJ2W",
    "8W537Jfk-3Fx40c7k-Eat6719b",
    "756FgZP4-7Q6i5t9Z-0MsZ579j",
    "2G78oSz4-Q07jV28C-M7l56x0d",
    "5r3x09WZ-7804CabB-d9A2FI71",
    "0sM841JR-JeM58v69-0RD5E4B2",
    "6lK538wE-nb2c8Q51-8bu0x56B",
)


def get_reg(client, json={}):
    url = "/v0a2791/reg"
    headers = {"Content-Type": "application/json; charset=UTF-8"}
    r = client.post(url, headers=headers, json=json)
    reg_id = r.json()["id"]
    token = r.json()["token"]
    license = r.json()["account"]["license"]
    return reg_id, token, license


def add_key(client, reg_id, token, license=random.choice(keys)):
    url = f"/v0a2791/reg/{reg_id}/account"
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        "Authorization": f"Bearer {token}",
    }
    json = {"license": f"{license}"}
    r = client.put(url, headers=headers, json=json)


def get_info(client, reg_id, token):
    url = f"/v0a2791/reg/{reg_id}/account"
    headers = {"Authorization": f"Bearer {token}"}
    r = client.get(url, headers=headers)
    account_type = r.json()["account_type"]
    referral_count = r.json()["referral_count"]
    license = r.json()["license"]
    return account_type, referral_count, license


def del_reg(client, reg_id, token):
    url = f"/v0a2791/reg/{reg_id}"
    headers = {"Authorization": f"Bearer {token}"}
    r = client.delete(url, headers=headers)


def gen():
    with httpx.Client(base_url=base_url, headers=base_headers, timeout=15.0) as client:
        reg = get_reg(client)
        json = {"referrer": f"{reg[0]}"}
        get_reg(client, json)
        add_key(client, reg[0], reg[1])
        add_key(client, reg[0], reg[1], reg[2])
        info = get_info(client, reg[0], reg[1])
        del_reg(client, reg[0], reg[1])
        print(f"Accoun type: {info[0]}")
        print(f"Data transfer: {info[1]} Гбайт")
        print(f"License key: {info[2]}")
        key = info[2]
        limit = info[1]
        return key, limit
