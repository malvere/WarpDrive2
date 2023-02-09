import aiofiles
import aiohttp


class Config:
    def __init__(self, fileName):
        self.url = "https://cf-warp.maple3142.net/warp.conf"
        self.fileName = f"warp/cert/{fileName}"

    async def __get_data(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url, allow_redirects=True) as resp:
                # async with aiofiles.open(self.fileName, "wb") as config:
                return await resp.read()

    async def __edit(self, config_data: bytes):
        fdata = config_data.decode("utf-8")
        fdata = fdata.replace("engage.cloudflareclient.com:2408", "162.159.193.5:2408")
        fdata = fdata.replace("DNS = 1.1.1.1", "DNS = 8.8.8.8")
        return fdata

    async def get(self):
        data = await self.__get_data()
        conf = bytes(await self.__edit(data), "utf-8")
        async with aiofiles.open(self.fileName, "wb") as f:
            await f.write(conf)
            return f
