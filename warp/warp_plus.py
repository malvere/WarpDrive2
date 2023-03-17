# %% WGCF
import asyncio
import subprocess as sp

from envars import WGCF_BIN
from warp import async_wg as agw


class WGCF:
    """
    Generates Warp+ WireGuards.conf
    license is optional: if not passed, new key will be generated

    :param filename:
    :param license
    """

    def __init__(self, filename, license=None) -> None:
        self.filename = filename
        self.license = license
        self.wgcf = WGCF_BIN
        self.cwd = "./warp/"
        self.warp: agw.WarpLicense

    def start(self):
        """
        Main sequence
        """
        self.get_toml()
        self.edit_toml()
        self.update_toml()
        self.get_conf()
        self.edit_conf()

    async def get_license(self) -> agw.WarpLicense:
        if self.license == None:
            for i in range(5):
                print(f"Attempt: {i+1}")
                # warp: agw.WarpLicense = asyncio.run(agw.gen())
                warp: agw.WarpLicense = await agw.gen()
                if warp.check_limit():
                    print(f"Key: {warp.key}\nLimit: {warp.limit}")
                    self.warp = warp
                    return warp
                else:
                    pass
        else:
            print("Detected existing license key")
            warp = agw.WarpLicense(key=self.license, limit="12096606")
            self.warp = warp
            return warp

    def get_toml(self):
        print(f"\n{'-'*10} Running Shell CMDs{'-'*10}\n")
        sp.run(
            [f"chmod +x {self.wgcf}"],
            shell=True,
            cwd=self.cwd,
        )
        sp.run(
            [f"./{self.wgcf} register --accept-tos --config cert/{self.filename}.toml"],
            shell=True,
            cwd=self.cwd,
        )
        print(f"\n{'-'*10} {self.filename}.toml generated {'-'*10}\n")

    def edit_toml(self):
        print(f"\n{'-'*10} Editing {self.filename}.toml {'-'*10}\n")
        newdata = []
        with open(f"warp/cert/{self.filename}.toml", "r") as f:
            fdata = f.readlines()
            for line in fdata:
                if line.startswith("license_key ="):
                    line = f"license_key = '{self.warp.key}'\n"
                    newdata.append(line)
                else:
                    newdata.append(line)
        with open(f"warp/cert/{self.filename}.toml", "w") as f:
            f.writelines(newdata)
            print(f"\n{'-'*10} {self.filename}.toml edited successfully {'-'*10}\n")
            return f

    def update_toml(self):
        print(f"\n{'-'*10} Updating {self.filename}.toml {'-'*10}\n")
        sp.run(
            [f"./{self.wgcf} update --config cert/{self.filename}.toml"],
            shell=True,
            cwd=self.cwd,
        )

    def get_conf(self):
        print(f"\n{'-'*10} {self.filename}.conf {'-'*10}\n")

        sp.run(
            [f"./{self.wgcf} generate -p cert/{self.filename}.conf --config cert/{self.filename}.toml"],
            shell=True,
            cwd=self.cwd,
        )
        print(f"\n{'-'*10} {self.filename}.conf generated {'-'*10}\n")
        pass

    def edit_conf(self):
        print(f"\n{'-'*10} Editing {self.filename}.conf {'-'*10}\n")
        with open(f"warp/cert/{self.filename}.conf", "r") as f:
            fdata = f.read()
            fdata = fdata.replace("engage.cloudflareclient.com:2408", "162.159.193.2:2408")
        with open(f"warp/cert/{self.filename}.conf", "w") as f:
            f.write(fdata)
            print(f"\n{'-'*10} {self.filename}.toml edited successfully {'-'*10}\n")
            return f
