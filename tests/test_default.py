from woke.testing import *
from pytypes.contracts.Foo import Foo


@default_chain.connect()
def test_default():
    default_chain.set_default_accounts(default_chain.accounts[0])
    a = default_chain.accounts[1]

    foo = Foo.deploy(a)
    tx = foo.foo(0, type=0)
    print(tx.call_trace)
