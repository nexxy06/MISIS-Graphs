import time


class AVLNode:
    def __init__(self, key, height=1, left=None, right=None):
        self.key = key
        self.height = height
        self.left = left
        self.right = right


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if not root:
            return AVLNode(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        # Левый перевес
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # Правый перевес
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # Левый-Правый случай
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Правый-Левый случай
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def delete(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def get_min_value_node(self, root):
        if root is None or root.left is None:
            return root
        return self.get_min_value_node(root.left)

    def pre_order(self, root):
        if not root:
            return
        print(f"{root.key} ", end="")
        self.pre_order(root.left)
        self.pre_order(root.right)


def test_avl_tree():
    tree = AVLTree()
    root = None

    # Вставка узлов
    keys = [10, 20, 30, 40, 50, 25]
    for key in keys:
        root = tree.insert(root, key)

    print("Дерево после вставок:")
    tree.pre_order(root)
    print("\n")

    # Удаление узлов
    keys_to_delete = [10, 20]
    for key in keys_to_delete:
        root = tree.delete(root, key)

    print("Дерево после удалений:")
    tree.pre_order(root)
    print("\n")


test_avl_tree()


def performance_test_avl_tree():
    tree = AVLTree()
    root = None

    # Вставка узлов
    start_time = time.time()
    for key in range(1, 10001):
        root = tree.insert(root, key)
    end_time = time.time()
    print(f"Время выполнения вставки 10000 узлов: {end_time - start_time:.6f} секунд")

    # Удаление узлов
    start_time = time.time()
    for key in range(1, 10001):
        root = tree.delete(root, key)
    end_time = time.time()
    print(f"Время выполнения удаления 10000 узлов: {end_time - start_time:.6f} секунд")


performance_test_avl_tree()
