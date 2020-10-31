# BrainFuck Interpreter

## BrainFuck语法

语言由8种符号组成，含义如下：

    > 指针向右移动一格
    < 指针向左移动一格
    + 使指针当前格数值加一
    - 使指针当前格数值减一
    [ 当指针当前指向值为 0 时，程序跳转到与之对应的 ] 之后；否则程序正常向下执行
    ] 程序跳转回与之对应的 [ 处
    . 把当前指针指向格中的值按 ASCII 表输出到终端
    , 从终端读取 1 byte 的数据，存储其 ASCII 值到当前格

## BrainFuck示例

用BrainFuck写的`hello world`程序：

    ++++++++++
    [
        >+++++++
        >++++++++++
        >+++
        >+
        <<<<-
    ]
    >++.
    >+.
    +++++++..
    +++.
    >++.
    <<+++++++++++++++.
    >.
    +++.
    ------.
    --------.
    >+.
    >.

## 使用

    $ ./main.py -c '+++++[>+++++++++++++<-]>.'
    A

    $ ./main.py -f hello.bf
    Hello World!

## 测试

doctest

    $ python interpreter.py

unittest

    $ python interpreter_test.py

