class OpenAddressing:
    def __init__(self):
        self.list = [None]*2
        self.length = 0

    def hash(self, value, size):
        return value % size

    def rehash(self, desired_size):
        new_list = [None] * desired_size
        for i in range(len(self.list)):
            value = self.list[i]
            if value is None:
                continue
            hash = self.hash(value, desired_size)
            j = hash
            while new_list[j] is not None:
                j += 1
                if j >= desired_size:
                    j = 0
                if j == hash:
                    print("Error, you shouldn't get here")
                    break
            new_list[j] = value
        self.list = new_list


    def add(self, value):
        if  self.length >= len(self.list):
            self.rehash(len(self.list)*2)
        hash = self.hash(value, len(self.list))
        j = hash
        while self.list[j] is not None:
            j += 1
            if j >= len(self.list):
                j = 0
            if j == hash:
                print("Error, you shouldn't get here")
                break
        self.list[j] = value
        self.length += 1

    def contains(self, value):
        hash = self.hash(value, len(self.list))
        j = hash
        while self.list[j] is not None and self.list[j] != value:
            j += 1
            if j >= len(self.list):
                j = 0
            if j == hash:
                return False
        if self.list[j] is None:
            return False
        return True

    def size(self):
        return self.length
    
    def remove(self, value):
        to_rehash = self.asList()
        to_rehash.remove(value)
        new_list = [None] * len(self.list)
        for i in range(len(to_rehash)):
            v = self.list[i]
            if v is None:
                continue
            hash = self.hash(v)
            j = hash
            while to_rehash[j] is not None:
                j += 1
                if j >= len(to_rehash):
                    j = 0
                if j == hash:
                    print("Couldn't rehash in remove")
                    break
            new_list[j] = v
        self.list = new_list

    def asList(self):
        return self.list.copy()

open_addressing = OpenAddressing()
open_addressing.add(8)
open_addressing.add(88)
open_addressing.add(888)

print(open_addressing.contains(8))
print(open_addressing.contains(88))
print(open_addressing.contains(888))
print(open_addressing.contains(1))
