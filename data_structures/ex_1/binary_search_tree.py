class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def DFSUtil(self, v, visited):
 
        # Mark the current node as visited and print it
        visited[v]= True
        print(v)
 
        # Recur for all the vertices adjacent to
        # this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

  def depth_first_for_each(self, cb):
    V = len(self.graph)  #total vertices
        # Mark all the vertices as not visited
    visited =[False]*(V)
 
        # Call the recursive helper function to print
        # DFS traversal starting from all vertices one
        # by one
    for i in range(V):
        if visited[i] == False:
            self.DFSUtil(i, visited) 

  def breadth_first_for_each(self, cb):
    pass

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
