#!/usr/bin/env python
# coding: utf-8

# In[102]:


class TreeNode:
    def __init__(self,item=None):
        self.item=item
        self.left=None
        self.right=None
    

    
class BinaryTree():
    def __init__(self, root):
        self.root=TreeNode(root)

    def __len__(self):
        return self.len_aux(self.root)
    
    def len_aux(self,current):
        if current is None:
            return 0
        else:
            return 1+self.len_aux(current.left)+self.len_aux(current.right)

    
    def leaf_finder(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.item
        return self.leaf_finder(root.left) + self.leaf_finder(root.right)

    def sum_leaves(self):
        return self.leaf_finder(self.root)
        
    def insert(self, value):
        self.root = self.insert_aux(self.root, value)

    def insert_aux(self, node, value):
        if node is None:
            return TreeNode(value)
        if value < node.item:
            node.left = self.insert_aux(node.left, value)
        elif value > node.item:
            node.right = self.insert_aux(node.right, value)
        else:
            print(f"Node with value {value} already exists in the tree.")
        return node
        
    def printTree(self):
        self.printTree_aux(self.root)
        
    def printTree_aux(self, node, level=0): # Idea for how to print it came from https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
        if node is not None:
            self.printTree_aux(node.right, level + 1)
            if level == 0:
                print(' ' * 4 * level + '-> ' + str(node.item))
            else:
                print(' ' * 4 * level + '-> ' + str(node.item))
            self.printTree_aux(node.left, level + 1)     
        

    def propersearch(self, target):
        return self.propersearch_aux(self.root, target)
        
    def propersearch_aux(self, node, target):
        if node is None or node.item == target:
            return node
        if node.item < target:
            return self.propersearch_aux(node.right, target) 
        else:
            return self.propersearch_aux(node.left, target)
            
    def searchAll(self, target):
        return self.searchAll_aux(self.root, target)
        
    def searchAll_aux(self, node, target):
        if node is None:
            return None
        if node.item == target:
            return node
        found_left = self.searchAll_aux(node.left, target)
        found_right = self.searchAll_aux(node.right, target)
        if found_left:
            return found_left
        else:
            return found_right
    

#Binary tree with just nodes being inputed making
bt=BinaryTree(25)
bt.root.left=TreeNode(20)
bt.root.right=TreeNode(22)
bt.root.left.left=TreeNode(10)
bt.root.right.left=TreeNode(19)
bt.root.right.right=TreeNode(8)

#print("The size of the binary tree is : ", bt.__len__())
#print("The sum of the leaves is : ", bt.sum_leaves())
#bt.printTree()


betterbt = BinaryTree(25)
betterbt.insert(4)
betterbt.insert(23)
betterbt.insert(57)
betterbt.insert(12)
betterbt.insert(65)
betterbt.insert(42)
betterbt.insert(1)
betterbt.insert(41)
betterbt.insert(2)
betterbt.insert(32)
betterbt.insert(82)
betterbt.insert(3)

#print("The size of the binary tree is : ", betterbt.__len__())
#print("The sum of the leaves is : ", betterbt.sum_leaves())

betterbt.printTree()

print(betterbt.propersearch(3))  
print(betterbt.searchAll(1))     



# In[111]:



class binaryPlant(): # Binary tree but has no requirement initialization requirement of having a first TreeNode
    def __init__(self):
        self.root=None
    
    def insert(self,item):
        if self.root is None:
            self.root=TreeNode(item)
        else:
            self._insert(item,self.root)
    
    def _insert(self,item,currentNode):
        if item < currentNode.item:
            if currentNode.left is None:
                currentNode.left=TreeNode(item)
            else:
                self._insert(item,currentNode.left)
        elif item > currentNode.item:
            if currentNode.right is None:
                currentNode.right=TreeNode(item)
            else:
                self._insert(item,currentNode.right)
        else:
            print("Item is already existed in the tree")
    
    def print_preorder(self):
        self._print_preorder_aux(self.root)
        
    def _print_preorder_aux(self,current):
        if current is not None:
            print(current.item)
            self._print_preorder_aux(current.left)
            self._print_preorder_aux(current.right)
    
    def printTree(self):
        self.printTree_aux(self.root)
        
    def printTree_aux(self, node, level=0): # Idea for how to print it came from https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
        if node is not None:
            self.printTree_aux(node.right, level + 1)
            if level == 0:
                print(' ' * 4 * level + '-> ' + str(node.item))
            else:
                print(' ' * 4 * level + '-> ' + str(node.item))
            self.printTree_aux(node.left, level + 1)     
        

    def propersearch(self, target):
        return self.propersearch_aux(self.root, target)
        
    def propersearch_aux(self, node, target):
        if node is None or node.item == target:
            return node
        if node.item < target:
            return self.propersearch_aux(node.right, target) 
        else:
            return self.propersearch_aux(node.left, target)
            
    def searchAll(self, target):
        return self.searchAll_aux(self.root, target)
        
    def searchAll_aux(self, node, target):
        if node is None:
            return None
        if node.item == target:
            return node
        found_left = self.searchAll_aux(node.left, target)
        found_right = self.searchAll_aux(node.right, target)
        if found_left:
            return found_left
        else:
            return found_right
    
    
bp = binaryPlant()
bp.insert(24)
bp.insert(4)
bp.insert(3)
bp.insert(25)
bp.insert(13)
bp.insert(6)
bp.insert(45)
bp.insert(16)
bp.insert(67)
bp.print_preorder()

bp.printTree()

print(bp.propersearch(3))  
print(bp.searchAll(1))     




# In[ ]:




