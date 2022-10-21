class Node:

    """A class implementing a node in a linked list."""

    def __init__(self, cargo):
        """
        (self) -> NoneType
        Create a Node with cargo and whose next element is next.
        """
        self.cargo = cargo
        self.next = None


class LinkedList:
    """A class that implements a linked list."""

    def __init__(self):
        """
        (self) -> NoneType
        Create an empty linked list.
        """
        self.length = 0
        self.head = None

    def __str__(self):
        """
        (self) -> str
        Print out the entire linked list from head (left) to tail (right).
        """
        if self.head is not None:

            string = ''
            on = self.head

            while on is not None:
                string += on.__str__() + ' --> '
                on = on.next
            else:
                string += on.__str__()

            return string
        else:
            return 'empty list'

    def add_to_head(self, cargo):
        """
        (self, object) -> NoneType
        Add cargo to the front of the list.
        """
        node = Node(cargo)
        node.next = self.head
        self.head = node
        self.length += 1

    def add_to_tail(self, cargo):
        """
        (self, object) -> NoneType
        Add cargo to the tail of the list.
        """
        on = self.head

        while on.next is not None:
            on = on.next

        on.next = Node(cargo)

    def get_at_index(self, index):
        """
        (self, object) -> NoneType
        Add a new node at certain index.
        """
        on = self.head

        while on and index != 0:
            on = on.next
            index -= 1

        if on is not None:
            return on.cargo
        else:
            return False

    def delete_by_cargo(self, cargo):
        """
        (self, object) -> NoneType
        Remove all nodes with certain cargo value.
        """
        on = self.head

        while on is not None and on.next is not None:

            if on.next.cargo == cargo:
                on.next = on.next.next

            on = on.next


class BinaryTree:

    """A Node class used by a binary tree class."""

    def __init__(self, root=None):
        """
        (self) -> NoneType
        Create an empty binary tree.
        """
        self.root = root

    def print_tree(self):
        """
        (self) -> NoneType
        Prints tree level by level.
        """
        level = [self.root]

        while len(level) > 0:

            level_next = []

            for node in level:

                print(node.cargo, " ", end="")

                if node.left is not None:
                    level_next.append(node.left)
                if node.right is not None:
                    level_next.append(node.right)

            print('\n')
            level = level_next


class BinarySearchTree:
    """A Node class used by a binary search tree class."""

    def __init__(self, root=None):
        """
        (self) -> NoneType
        Create an empty binary tree.
        """
        self.root = root
        if not self.is_valid():
            print('This is not a valid binary search tree.')

    def print_tree(self):
        """
        (self) -> NoneType
        Prints tree level by level.
        """
        level = [self.root]

        while len(level) > 0:

            level_next = []

            for node in level:

                print(node, " ", end="")

                if node.left is not None:
                    level_next.append(node.left)
                if node.right is not None:
                    level_next.append(node.right)

            print('\n')
            level = level_next

    def is_valid(self):
        """
        (self) -> NoneType
        Checks if self.root is a valid binary search tree.
        """
        on = self.root
        stack = []
        prev = None

        while len(stack) > 0 or on is not None:

            while on is not None:
                stack.append(on)
                on = on.left

            on = stack.pop()

            if prev is not None and on.cargo <= prev.cargo:
                return False

            prev = on
            on = on.right

        return True

    def find(self, cargo):
        """
        (self, number) -> bool
        Checks if cargo value is in the tree.
        """
        on = self.root

        while on is not None:

            if cargo > on.cargo:
                on = on.right

            elif cargo < on.cargo:
                on = on.left

            else:
                return True

        return False
