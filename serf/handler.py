#!/usr/bin/python
# coding: utf-8
"""
Serf class is serf event handler class.
Switch the execution method under the handlers module in the event

* tree
event-handler-root
|- handler.py
|- handlers
   |- member_join.py
   |- member_failed.py
   |- member_update.py
   |- member_leap.py
   |- user_deploy.py
   |- query_xxx.py
   |- ...
"""
from __future__ import absolute_import, unicode_literals, print_function

from importlib import import_module
import logging
import os
import sys

logging.basicConfig(filename='/tmp/serf.log',
                    filemode='a',
                    level=logging.DEBUG)
logger = logging.getLogger('serf_{}'.format(__name__))


class Serf(object):

    def __init__(self):
        self.event = os.environ.get('SERF_EVENT', '')
        self.self_name = os.environ.get('SERF_SELF_NAME', '')
        self.user_event = os.environ.get('SERF_USER_EVENT', '')
        self.query_name = os.environ.get('SERF_QUERY_NAME', '')
        self.args = sys.stdin.readlines()

    @property
    def handler_name(self):
        if self.event == 'user':
            return '{}_{}'.format(self.event, self.user_event)
        elif self.event == 'query':
            return '{}_{}'.format(self.event, self.query_name)
        else:
            return self.event.replace('-', '_')

    @property
    def handler(self):
        try:
            handler = import_module('handlers.{}'.format(self.handler_name))
            return handler
        except ImportError:
            return None

    def run(self):
        if self.handler:
            main = getattr(self.handler, 'main')
            if main:
                main(self.self_name, *self.args)


if __name__ == '__main__':
    serf = Serf()
    logger.info('handername:%s\thandler:%s',
                serf.handler_name,
                str(serf.handler))
    serf.run()
