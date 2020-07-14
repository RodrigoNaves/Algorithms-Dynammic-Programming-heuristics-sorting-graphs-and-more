# Licensing Information: You are free to use or extend this file for 
# educational purposes provided that (1) you retain this notice, and 
# (2) you provide clear attribution to the University of Melbourne, 
# including a link to https://cis.unimelb.edu.au.
#
# This file was created as part of teaching material for COMP90038


class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

def PreorderTraverse(T):
    Hleft = 0
    Hright = 0
    bal = 0
   
    if T is not None:
        Hleft = Height(T.left)
        Hright = Height(T.right)
        bal = Hleft - Hright
        if bal > 1 or bal < -1:
            print(T.val)
        PreorderTraverse(T.left)
        PreorderTraverse(T.right)
    #if Height(T) > 1:
       # print(T.val)
        
def Height(T):
    if T is None:
        return -1
    else:
        return max(Height(T.left), Height(T.right)) +1
    


def test():
    T = Node(17)
    T.left = Node(33)
    T.left.left = Node(19)
    #T.left.left.right = Node(12)
    T.left.right = Node(16)
    T.left.right.left = Node(38)
    T.left.right.right = Node(31)
    T.left.right.right.left = Node(18)
    T.right = Node(48)
    T.right.left = Node(11)
    T.right.right = Node(14)
    T.right.right.right = Node(20)
    T.right.right.right.right = Node(21)
    T.right.right.right.left = Node(15)
    T.right.right.right.left.left = Node(36)
    T.right.right.right.left.left.left = Node(38)
    PreorderTraverse(T)
    
if __name__ == "__main__":
    test()