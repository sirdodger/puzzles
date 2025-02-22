from __future__ import annotations
import sys

class TreeNode:

    SEP = "-"
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    @classmethod
    def parse(cls, traversal: str) -> TreeNode | None:
        """Parse a tree from a string where dashes in the string represent
        the depth of the node.  (Always bias towards filling left children
        before right children.)"""
        tree_stack = []
        val_list = []
        depth = 0

        # Add a dash to the end of the input to trigger one last node creation
        # for end of string.
        for c in (traversal + cls.SEP):

            if c == cls.SEP:
                # Handle transition from number to dash
                if val_list:
                    node = TreeNode(val=int("".join(val_list)))
                    
                    # Do not attempt to pop when adding the root node
                    if len(tree_stack) != 0:

                        # Pop back up to the correct parent depth
                        for _ in range(len(tree_stack) - depth):
                            tree_stack.pop()

                        # Get the parent node off the stack
                        parent = tree_stack[-1]
                        if not parent.left:
                            parent.left = node
                        else:
                            parent.right = node
                    
                    # Add new node to stack
                    tree_stack.append(node)

                    # Reset state tracking
                    val_list = []
                    depth = 0

                # Increase depth for each dash
                depth +=1

            else:
                # Append digit to number
                val_list.append(c)
                
        # Return root node
        return tree_stack[0] if tree_stack else None

    @classmethod
    def serialize(cls, node: self, depth=0) -> str:
        l = cls.serialize(node=node.left, depth=depth + 1) if node.left else ""
        r = cls.serialize(node=node.right, depth=depth + 1) if node.right else ""
        return f"{"-" * depth}{node.val}{l}{r}"


if __name__ == "__main__":
    tree = TreeNode.parse(traversal=sys.argv[1])
    print(TreeNode.serialize(tree))
