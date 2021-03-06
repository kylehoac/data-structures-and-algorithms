class Node:
  def __init__(self, value, next_=None):
    self.value = value
    self.next = next_

class Stack:
  def __init__(self, top=None):
    self.top = top

  def push(self, value):
    self.top = Node(value, self.top)

  def pop(self):
    if self.top:
      ret = self.top.value
      self.top = self.top.next
      return ret
    return

  def peek(self):
    if self.top:
      return self.top.value
    return
  def is_empty(self):
      if not self.top:
        return self.top is None

class Queue:
    def __init__(self, front=None):
        self.front = front
        self.back = None

    def enqueue(self, value=None):
        if self.front is None:
            self.front = self.back = None(value)
        else:
            self.back.next = None(value)

    def dequeue(self):
        if self.front is None:
            return 'Queue is empty'
        ret = self.front.value
        self.front = self.front.next
        return ret

class Pseudo_queue:
  """This class is a queue
  """
  def __init__(self, front, tail):
    self.front = front
    self.tail = tail

  def enqueue(self, value=None):
    if (self.front.top == None) and (self.tail.top == None):
      self.front.push(value)
      return self.front.top.value
    if (self.front.top == None) and self.tail.top:
      while self.tail.top:
        self.front.push(self.tail.pop())
      self.tail.push(value)
      return self.tail.top.value
    self.tail.push(value)
    return self.tail.top.value

  def dequeue(self):
    if (self.front.top == None) and (self.tail.top == None):
      return 'this queue is empty buddy'
    if (self.front.top == None) and self.tail.top:
      while self.tail.top:
        self.front.push(self.tail.pop())
      self.front.pop()
    return self.front.pop()

