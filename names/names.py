import time
# class BinarySearchTree:
#   def __init__(self, value):
#     self.value = value
#     self.left = None
#     self.right = None

#   def insert(self, value):
#     if value < self.value: # is current node less than new node?
#       if not self.left: # if not left child node
#         self.left = BinarySearchTree(value) # insert new node
#       else:
#         self.left.insert(value)
#     else:
#       if not self.right:
#         self.right = BinarySearchTree(value)
#       else:
#         self.right.insert(value)
      

#   def contains(self, target):
#     if target == self.value:
#       return True
#     else:
#       if target < self.value:
#         if self.left:
#           return self.left.contains(target)
#       else:
#         if self.right:
#           return self.right.contains(target)

#   def get_max(self):
#     if not self.right:
#       return self.value
#     else: 
#       return self.right.get_max()

#   def for_each(self, cb):
#     cb(self.value)
#     if self.left:
#       self.left.for_each(cb)
#     if self.right:
#       self.right.for_each(cb)

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
for i in names_1: 
    if i in names_2:
        duplicates.append(i)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

