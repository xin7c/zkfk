#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:xuchu
@file:kafkaProducer.py
@time:2020/10/12
"""
import time
from json import dumps
import arrow
from kafka import KafkaProducer

topic = "xx5"
host = "10.61.158.29"


def conn_kafka():
    producer = KafkaProducer(bootstrap_servers=[f'{host}:9092',
                                                f'{host}:9093',
                                                f'{host}:9094'],
                             compression_type='gzip')  # 连接kafka
    # print(producer.bootstrap_connected())

    utc = arrow.now().ctime()
    msg = f"{utc}".encode('utf-8')  # 发送内容,必须是bytes类型
    # 第1个参数为topic名称，必须指定
    # key:键，必须是字节字符串，可以不指定（但key和value必须指定1个），默认为None
    # value:值，必须是字节字符串，可以不指定（但key和value必须指定1个），默认为None
    # partition:指定发送的partition，由于kafka默认配置1个partition，固为0
    # 如果一个有效的partition属性数值被指定，那么在发送记录时partition属性数值就会被应用。
    # 如果没有partition属性数值被指定，而一个key属性被声明的话，一个partition会通过key的hash而被选中。
    # 如果既没有key也没有partition属性数值被声明，那么一个partition将会被分配以轮询的方式。
    future = producer.send(topic=topic,
                           value=msg,
                           # key=b"xuchu"
                           )
    result = future.get(timeout=60)  # future.get等待单条消息发送完成或超时
    print(result)
    print(future.is_done)

    producer.close()


if __name__ == '__main__':
    for i in range(1000):
        conn_kafka()
        time.sleep(0.5)
