cld: str = "blabla\\basic"
if cld.split("\\")[-1] == "basic":
    conf_path = "warp/cert/warp.conf"
    qr_path = "warp/cert/qr_basic.png"
else:
    conf_path = "warp/cert/WarpPlus.conf"
    qr_path = "warp/cert/qr_plus.png"

print(f"{conf_path}")
