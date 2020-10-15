#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:xuchu
@file:zkTest.py
@time:2020/10/09
"""
import time

from kazoo.client import KazooClient
from config.config import Config


if __name__ == '__main__':
    cli = KazooClient(hosts=Config.get_yaml().get("zk_hosts"))
    cli.start()

    # @cli.DataWatch("/ww")
    # def www(data, stat, event):
    #     print("观察者触发", data, stat, event)

    # cli.create("/ww", b"create ww")
    # cli.close()
    while True:
        cli.set("/ww", b'123')
        print(cli.get("/ww"))
        time.sleep(3)
