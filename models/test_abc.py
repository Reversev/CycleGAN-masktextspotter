from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys

if sys.version > '3':
    from abc import ABC, abstractmethod
else:
    from abc import ABCMeta, abstractmethod

if sys.version > '3':
    class MyBase(ABC):
        @abstractmethod
        def func(self):
            '''Implement in subclass'''
else:
    class MyBase():
        __metaclass__ = ABCMeta

        @abstractmethod
        def func(self):
            '''Implement in subclass'''


class MyClass(MyBase):
    def func(self):
        con = "%s %s" % (self.__class__.__name__, sys._getframe().f_code.co_name)
        print(con)


obj = MyClass()
obj.func()
