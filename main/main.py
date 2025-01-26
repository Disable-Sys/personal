from wcferry import Wcf,WxMsg
from queue import Empty
import time


status = 0
wcf = Wcf()
wcf.is_login()
wcf.enable_receiving_msg()
while status == 0:
    try:
        print(wcf.get_msg())
        print(wcf.get_msg_types())
        print(WxMsg.__dict__)
    except Empty:
        print("empty")
        time.sleep(1)
