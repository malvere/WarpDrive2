import httpx

headers = {
    "CF-Client-Version": "a-6.11-2223",
    "Host": "api.cloudflareclient.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/3.12.1",
}


def licence():
    with httpx.Client(base_url="https://api.cloudflareclient.com/v0a2223", headers=headers) as client:
        r = client.post("/reg")
        id = r.json()["id"]
        license = r.json()["account"]["license"]
        token = r.json()["token"]

        r = client.post("/reg")
        id2 = r.json()["id"]
        token2 = r.json()["token"]

        headers_get = {"Authorization": f"Bearer {token}"}
        headers_get2 = {"Authorization": f"Bearer {token2}"}
        headers_post = {
            "Content-Type": "application/json; charset=UTF-8",
            "Authorization": f"Bearer {token}",
        }

        json = {"referrer": f"{id2}"}
        client.patch(f"/reg/{id}", headers=headers_post, json=json)

        client.delete(f"/reg/{id2}", headers=headers_get2)

        json = {"license": "Pjx17R84-v4qz5L01-1muQ405F"}
        client.put(f"/reg/{id}/account", headers=headers_post, json=json)

        json = {"license": f"{license}"}
        client.put(f"/reg/{id}/account", headers=headers_post, json=json)

        r = client.get(f"/reg/{id}/account", headers=headers_get)
        account_type = r.json()["account_type"]

        client.delete(f"/reg/{id}", headers=headers_get)

        return f"{license}"
