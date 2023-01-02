#!/usr/bin/python3

"""Defines a class 'Node'"""


class Node:
    """Defines a node of a linked list"""

    def __init__(self, data, next_node=None):
        """
        Initializes a new Node

        Args:
            Data(int): Value of the node
            next_node: Node object next in list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("datamust be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


"""Defines a class 'SinglyLinkedList'"""


class SinglyLinkedList:
    """Defines the structure of a Singlly Linked List"""

    def __init__(self):
        """Initializes a linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new node to the correct numerical position in the linked list

        Args:
            value (Node): New node to be inserted
        """
        new = Node(value)

        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > new.data:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while ((tmp.next_node is not None) and tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        arr = []
        tmp = self.__head
        while tmp is not None:
            arr.append(str(tmp.data))
            tmp = tmp.next_node
        return "\n".join(arr)
