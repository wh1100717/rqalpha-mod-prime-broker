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

import click

from rqalpha import cmd_cli

__config__ = {
    "traders": {
        "test": "tcp://127.0.0.1:15555",
    },
}


@cmd_cli.command()
def pb():
    from .prime_broker import PrimeBroker
    prime_broker = PrimeBroker(__config__)
    prime_broker.start()


@cmd_cli.command()
@click.option("-p", "--port")
def trade_server(port):
    from .prime_broker import TradeServer
    trade_server = TradeServer(port)
    trade_server.start()
