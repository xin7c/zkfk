#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:xuchu
@file:kafkaConsumer.py
@time:2020/10/12
"""
import time
import logging

from kafka import KafkaConsumer, TopicPartition
from json import loads

topic = 'xx5'


def consumerAction():
    consumer = KafkaConsumer(
        topic,  # topic
        group_id="group_id_xuchu",
        bootstrap_servers=['10.61.153.83:9092',
                           '10.61.153.83:9093',
                           '10.61.153.83:9094'],  # bootstrap server
        # api_version=(0, 11, 3),
        auto_offset_reset='earliest',
        # consumer_timeout_ms=5000,
        # key_deserializer=bytes.decode,
        value_deserializer=bytes.decode,
        enable_auto_commit=True,
        # value_deserializer=lambda x: loads(x.decode('utf-8'))
    )
    consumer.partitions_for_topic(topic)
    print(consumer.topics())
    # print(consumer.position(TopicPartition(topic=u'xx5', partition=0)))
    consumer.subscribe(topics=['xx5'])
    logging.basicConfig(level=logging.INFO)
    logging.info('Receiving message...')
    # 手动拉取消息
    # while True:
    #     msg = consumer.poll(timeout_ms=5)  # 从kafka获取消息
    #     print(msg)
    #     time.sleep(1)

    for message in consumer:
        recv = f"#主题{message.topic}" \
               f"#分区{message.partition}" \
               f"#偏移量{message.offset}" \
               f"#key={message.key}" \
               f"#value={message.value}"
        time.sleep(0.5)
        logging.info(recv)


if __name__ == '__main__':
    consumerAction()
