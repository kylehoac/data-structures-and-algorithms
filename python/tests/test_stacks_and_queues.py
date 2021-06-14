import pytest
from code_challenges.stacks_and_queues.stacks_and_queues import Stack, Queue, Node
from code_challenges.stacks_and_queues.invalid_error import InvalidOperationError


def test_is_stack():
    assert Stack()

def test_push():
    stack = Stack()
    stack.push('1')
    actual = stack.top.value
    expected = '1'
    assert actual == expected

def test_push_many():
    stack = Stack()
    stack.push('1')
    stack.push('2')
    stack.push('3')
    actual = stack.top.value
    expected = '3'
    assert actual == expected

def test_pop():
    stack = Stack()
    stack.push('1')
    stack.push('2')
    stack.push('3')
    stack.pop()
    actual = stack.top.value
    expected = '2'
    assert actual == expected

def test_pop_till_empty():
    stack = Stack()
    stack.push('1')
    stack.push('2')
    stack.push('3')
    stack.pop()
    stack.pop()
    stack.pop()
    actual = stack.is_empty()
    expected = True
    assert actual == expected

def test_peek():
    stack = Stack()
    stack.push('1')
    stack.push('2')
    stack.push('3')
    stack.push('4')
    stack.peek()
    actual = stack.top.value
    expected = '4'
    assert actual == expected

def test_empty_stack():
    stack = Stack()
    assert stack.is_empty()

def test_peek_on_empty():
    new_stack = Stack()
    with pytest.raises(InvalidOperationError) as e:
        new_stack.peek()

def test_enqueue():
    queue = Queue()
    queue.enqueue('1')
    actual = queue.tail.value
    expected = '1'
    assert actual == expected

def test_enqueue_multiple():
    queue = Queue()
    queue.enqueue('1')
    queue.enqueue('2')
    queue.enqueue('3')
    actual = queue.tail.value
    expected = '3'
    assert actual == expected

def test_dequeue():
    queue = Queue()
    queue.enqueue('1')
    queue.enqueue('2')
    queue.enqueue('3')
    queue.enqueue('4')
    queue.dequeue()
    actual = queue.front.value
    expected = '2'
    assert actual == expected

def test_dequeue_empty():
    queue = Queue()
    queue.enqueue('1')
    queue.enqueue('2')
    queue.enqueue('3')
    queue.enqueue('4')
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    actual = queue.is_empty()
    expected = True
    assert actual == expected

def test_new_queue():
    queue = Queue()
    actual = Queue().front
    expected = None
    assert actual == expected
