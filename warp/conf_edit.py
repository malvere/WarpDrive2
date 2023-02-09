# WireGuard Config Edit

import sys

file = f"{sys.argv[-1]}_Warp.conf"
with open(f"cert/{file}", "r") as f:
    fdata = f.read()
    fdata = fdata.replace("engage.cloudflareclient.com:2408", "162.159.193.2:2408")
with open(f"cert/{file}", "w") as f:
    f.write(fdata)
