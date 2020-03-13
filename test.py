#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from signals import *

class B(SObject):
    def proc(self, s):
        print("signal b: member function")

class C(SObject):
    def proc(self, s):
        print("signal c: member function")

def test():
    a = SObject()
    a.signals.register("a")
    a.signals.connect("a",
    lambda s:
        print("signal a: lambda")
    )

    b = B()
    b.signals.register("b")
    b.signals.connect("b",
    lambda s:
        print("signal b: lambda")
    )
    a.signals.redirect("a", "b", b)
    a.signals.once("a", b.proc, b)

    c = C()
    c.signals.register("c")
    a.signals.once("a", c.proc, c)
    a.signals.once("lost", c.proc, c)
    c.drop()

    f = lambda s: print("signal a: function")
    a.signals.connect("a", f)

    a.signals.emit("a")
    a.signals.disconnect("a", f)
    a.signals.emit("a")

if __name__ == "__main__":
    test()
