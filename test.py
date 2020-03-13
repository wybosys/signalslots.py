#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from signals import *

def test():
    a = SObject()
    a.signals.register("a")
    a.signals.connect("a",
        lambda s:
            print("signal a: lambda")
        )
    
    a.signals.emit("a")    

if __name__ == "__main__":
    test()
