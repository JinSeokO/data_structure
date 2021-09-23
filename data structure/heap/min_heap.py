class MinHeap(object):
    def __init__(self):
        self.__queue = list()
        self.__queue.append(None)

    def insert(self, data):
        if len(self.__queue) == 1:
            self.__queue.append(data)
            return True

        self.__queue.append(data)
        insert_index = len(self.__queue) - 1

        while insert_index > 1:
            parent_index = self.parent(insert_index)
            if self.__queue[parent_index] > self.__queue[insert_index]:
                self.swap(insert_index, parent_index)
                insert_index = parent_index
            else:
                break
        return True

    def pop(self):
        last_index = len(self.__queue) - 1
        self.swap(1, last_index)
        data = self.__queue.pop()
        self.min_heapify(1)

        return data

    def min_heapify(self, index):
        last_index = len(self.__queue) - 1
        if last_index < 2:
            return

        left_index = self.left_child(index)
        right_index = self.right_child(index)
        smallest_index = index

        if left_index <= last_index and self.__queue[left_index] < self.__queue[smallest_index]:
            smallest_index = left_index
        if right_index <= last_index and self.__queue[right_index] < self.__queue[smallest_index]:
            smallest_index = right_index

        if smallest_index != index:
            self.swap(index, smallest_index)
            self.min_heapify(smallest_index)

    def swap(self, index, parent_index):
        self.__queue[index], self.__queue[parent_index] = self.__queue[parent_index], self.__queue[index]

    @staticmethod
    def parent(index):
        return index // 2

    @staticmethod
    def left_child(index):
        return index * 2

    @staticmethod
    def right_child(index):
        return index * 2 + 1

    def size(self):
        return len(self.__queue) - 1

    def min(self):
        return self.__queue[1]
