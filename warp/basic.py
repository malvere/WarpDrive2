import subprocess as sp

from envars import WGCF_BIN


class WGCFBasic:
    def __init__(self, filename) -> None:
        self.filename = filename
        self.wgcf = WGCF_BIN
        self.cwd = "./warp/"

    def start(self):
        """
        Main sequence
        Does not generate keys
        """
        self.get_toml()
        self.get_conf()
        self.edit_conf()

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
        # pass

    def get_conf(self):
        print(f"\n{'-'*10} {self.filename}.conf {'-'*10}\n")

        sp.run(
            [f"./{self.wgcf} generate -p cert/{self.filename}.conf --config cert/{self.filename}.toml"],
            shell=True,
            cwd=self.cwd,
        )
        print(f"\n{'-'*10} {self.filename}.conf generated {'-'*10}\n")
        # pass

    def edit_conf(self):
        print(f"\n{'-'*10} Editing {self.filename}.conf {'-'*10}\n")
        with open(f"warp/cert/{self.filename}.conf", "r") as f:
            fdata = f.read()
            fdata = fdata.replace("engage.cloudflareclient.com:2408", "162.159.193.5:2408")
            fdata = fdata.replace("DNS = 1.1.1.1", "DNS = 8.8.8.8")
        with open(f"warp/cert/{self.filename}.conf", "w") as f:
            f.write(fdata)
            print(f"\n{'-'*10} {self.filename}.toml edited successfully {'-'*10}\n")
            return f
