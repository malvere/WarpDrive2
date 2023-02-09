import subprocess as sp

import gen_warp

for i in range(5):
    print(f"Attempt N: {i+1}\n")
    wkey, limit = gen_warp.gen()
    if limit <= 1000:
        pass
    else:
        print(f"Limit = {limit}")
        print(f"Key = {wkey}")
        sp.Popen(["chmod", "+x", "./sc.sh"])
        proc = sp.Popen(["./sc.sh", f"{wkey}"])
        proc.wait()
        break
