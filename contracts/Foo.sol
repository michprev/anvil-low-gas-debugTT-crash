contract Bar {

}

contract Foo {
    constructor(address a) {

    }

    function foo(uint x) external {
        if (x == 0)
            this.foo{gas: 1000}(1);
        new Bar();
    }
}