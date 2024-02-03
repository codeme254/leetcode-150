class RandomizedSet:

    def __init__(self):
        self.hash_map = {}
        self.list = []

    def insert(self, val: int) -> bool:
        """
        inserts a value into the RandomizedSet
        Args:
            val: value to be inserted to the RandomizedSet
        Returns:
            true if val was inserted successfully
            false if val was not inserted sucessfully
        inserts val only if it does not exist in the RandomizedSet
        """
        # check if val exists in hash_map
        if val in self.hash_map:
            return False
        self.list.append(val)
        self.hash_map[val] = len(self.list)-1
        return True

    def remove(self, val: int) -> bool:
        """
        removes a value from the RandomizedSet
        Args:
            val: the value to be removed from the randomized set
        Returns:
            true upon successful removal
            false when the operation was not successful
        """
        if not val in self.hash_map:
            return False
        # if the set has only one element, clear everything
        if len(self.list) == 1:
            self.hash_map = {}
            self.list = []
            return True
        remove_index = self.hash_map.get(val)
        print(f"The remove index is {remove_index}")
        # swap the last element of the list with the element to be removed
        temp = self.list[remove_index]
        self.list[remove_index] = self.list[len(self.list)-1]
        self.list[len(self.list)-1] = temp
        # update the value of the swapped element in the hash
        self.hash_map[self.list[remove_index]] = remove_index
        self.list.pop()
        del self.hash_map[val]
        return True

    def getRandom(self) -> int:
        import random
        return random.choice(self.list)

s = RandomizedSet()
# s.insert(10)
# s.insert(4)
# s.insert(22)
# s.insert(5)
# s.insert(10)
# print(s.remove(10))

s.insert(3)
s.insert(3)
s.insert(1)
s.remove(3)
s.insert(0)
# s.remove(0)
print(s.hash_map, s.list)
