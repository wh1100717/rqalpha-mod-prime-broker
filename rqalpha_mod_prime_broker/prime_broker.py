# -*- coding: utf-8 -*-
#
# Copyright 2017 wh1100717
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import six
import zmq
import time


class PrimeBroker(object):
    def __init__(self, config):
        self._config = config
        self._trades = {}

    def start(self):
        # 初始化数据源连接
        self._connect_data_source()
        # 初始化交易端连接
        self._connect_trader()

        for request in range(10):
            print("Sending request %s …" % request)
            self._trades['test'].send(b"Hello")

            #  Get the reply.
            message = self._trades['test'].recv_string()
            print("Received reply %s [ %s ]" % (request, message))

    def _connect_data_source(self):
        pass

    def _connect_trader(self):
        context = zmq.Context()
        for key, zmq_url in six.iteritems(self._config['traders']):
            socket = context.socket(zmq.REQ)
            socket.connect(zmq_url)
            self._trades[key] = socket


class TradeServer(object):
    def __init__(self, port):
        context = zmq.Context()
        self._socket = context.socket(zmq.REP)
        self._socket.bind("tcp://*:" + port)

    def start(self):
        while True:
            message = self._socket.recv_string()

            time.sleep(1)

            self._socket.send_string(message + "World")
