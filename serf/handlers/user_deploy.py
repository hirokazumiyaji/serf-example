# coding: utf-8
from __future__ import absolute_import, unicode_literals, print_function

from logging import getLogger

logger = getLogger('serf_{}'.format(__name__))


def main(self_name, *args):
    arg_string = ','.join(args)
    logger.info('name:%s\targs:%s', self_name, arg_string) 
