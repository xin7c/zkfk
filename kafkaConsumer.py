#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:xuchu
@file:kafkaConsumer.py
@time:2020/10/12
"""
import time
import logging
import threading
from kafka import KafkaConsumer, TopicPartition
from json import loads
from functools import wraps

topic = 'xx5'
host = "10.61.158.29"

def logger(param):
    """ fcuntion from logger meta """

    def wrap(function):
        """ logger wrapper """

        @wraps(function)
        def _wrap(*args, **kwargs):
            """ wrap tool """
            print("当前模块 {}".format(param))
            print("全部args参数参数信息, {}".format(str(args)))
            print("全部kwargs参数信息, {}".format(str(kwargs)))
            return function(*args, **kwargs)
        return _wrap
    return wrap

@logger('consumerAction')
def consumerAction(arg):
    consumer = KafkaConsumer(
        topic,  # topic
        group_id="group_id_xuchu",
        bootstrap_servers=[f'{host}:9092',
                           f'{host}:9093',
                           f'{host}:9094'],  # bootstrap server
        # api_version=(0, 11, 3),
        auto_offset_reset='earliest',
        # consumer_timeout_ms=5000,
        # key_deserializer=bytes.decode,
        value_deserializer=bytes.decode,
        enable_auto_commit=True,
        client_id='xuchu-mac'
        # value_deserializer=lambda x: loads(x.decode('utf-8'))
    )
    consumer.partitions_for_topic(topic)
    print(consumer.topics())
    print(consumer.subscription())
    # print(consumer.position(TopicPartition(topic=u'xx5', partition=0)))
    consumer.subscribe(topics=[topic])
    logging.basicConfig(level=logging.INFO)
    logging.info('Receiving message...')
    # 手动拉取消息
    # while True:
    #     msg = consumer.poll(timeout_ms=5)  # 从kafka获取消息
    #     print(msg)
    #     time.sleep(1)
    for message in consumer:
        recv = f"#主题{message.topic} " \
               f"#分区{message.partition} " \
               f"#偏移量{message.offset} " \
               f"#key={message.key} " \
               f"#value={message.value} "
        time.sleep(0.5)
        logging.info(f"线程[{threading.currentThread().ident}] -->" + recv)


if __name__ == '__main__':
    threads = []
    for i in range(1):
        t = threading.Thread(target=consumerAction, args=("参数",))
        threads.append(t)
    for t in threads:
        t.setDaemon(True)
        t.start()

    t.join()
    # consumerAction()
