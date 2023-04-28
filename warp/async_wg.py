# import asyncio
import random
from dataclasses import dataclass

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
    "9Hp70f6w-081fe4dq-b4sR37t6",
    "9Hp70f6w-081fe4dq-b4sR37t6",
    "l57X16JH-90Y26Wgc-W81A2OX3",
    "E61v45SL-1Kw5X8d6-239N0xXW",
    "4J8tR6a1-Gy3189FZ-89K5vZ7f",
    "25Kga49l-h913Xq4K-IJ2B036N",
    "8W537Jfk-3Fx40c7k-Eat6719b",
    "756FgZP4-7Q6i5t9Z-0MsZ579j",
    "2G78oSz4-Q07jV28C-M7l56x0d",
    "5r3x09WZ-7804CabB-d9A2FI71",
    "0sM841JR-JeM58v69-0RD5E4B2",
    "6lK538wE-nb2c8Q51-8bu0x56B",
)


@dataclass
class WarpLicense:
    key: str
    limit: str

    def check_limit(self) -> bool:
        if self.limit < 1000:
            return False
        else:
            return True


async def get_reg(client: httpx.AsyncClient, json={}):
    url = "/v0a2791/reg"
    headers = {"Content-Type": "application/json; charset=UTF-8"}
    r = await client.post(url, headers=headers, json=json)
    reg_id = r.json()["id"]
    token = r.json()["token"]
    license = r.json()["account"]["license"]
    return reg_id, token, license


async def add_key(
    client: httpx.AsyncClient,
    reg_id,
    token,
    license=random.choice(keys),
):
    url = f"/v0a2791/reg/{reg_id}/account"
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        "Authorization": f"Bearer {token}",
    }
    json = {"license": f"{license}"}
    r = await client.put(url, headers=headers, json=json)


async def get_info(client: httpx.AsyncClient, reg_id, token):
    url = f"/v0a2791/reg/{reg_id}/account"
    headers = {"Authorization": f"Bearer {token}"}
    r = await client.get(url, headers=headers)
    account_type = r.json()["account_type"]
    referral_count = r.json()["referral_count"]
    license = r.json()["license"]
    return account_type, referral_count, license


async def del_reg(client: httpx.AsyncClient, reg_id, token):
    url = f"/v0a2791/reg/{reg_id}"
    headers = {"Authorization": f"Bearer {token}"}
    r = await client.delete(url, headers=headers)


async def gen() -> WarpLicense:
    """
    Generates 12PB Warp key
    Based on @Saito.alex's script, rewritten with asyncio
    Original scrip: https://4pda.to/forum/index.php?showtopic=929115&st=1240#entry113636360
    """
    async with httpx.AsyncClient(base_url=base_url, headers=base_headers, timeout=15.0) as client:
        reg = await get_reg(client)
        json = {"referrer": f"{reg[0]}"}
        await get_reg(client, json)
        await add_key(client, reg[0], reg[1])
        await add_key(client, reg[0], reg[1], reg[2])
        info = await get_info(client, reg[0], reg[1])
        await del_reg(client, reg[0], reg[1])
        print(f"Accoun type: {info[0]}")
        print(f"Data transfer: {info[1]} Гбайт")
        print(f"License key: {info[2]}")
        key = info[2]
        limit = info[1]
        return WarpLicense(key=key, limit=limit)
