# Toml Edit

import sys

file = f"{sys.argv[-1]}_Warp.toml"
newdata = []
with open(f"cert/{file}", "r") as f:
    fdata = f.readlines()
    for line in fdata:
        if line.startswith("license_key ="):
            line = f"license_key = '{sys.argv[-1]}'\n"
            newdata.append(line)
        else:
            newdata.append(line)

with open(f"cert/{file}", "w") as f:
    f.writelines(newdata)
