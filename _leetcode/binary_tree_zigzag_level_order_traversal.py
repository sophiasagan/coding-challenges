# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root):
        '''
        Return a list of lists, where each levels values are in its own list
        Skip over the null values

        We need some way to keep track of which direction we're goin in 
        - differentiate the level
        - use even vs. odd level to figure out which direction (increment a variable)
        just alternate, keep a flag or something and switch level, starting with right

        stacks
        nested stack, w/ inner stack to separate the levels?
        stack to store the direction we're going
        stack has LIFO
        store currrent and next level in stacks?

        with a normal BFT, we use a queue to store the order of the elements 
        but for zigzag, everyo other level we want to store the elements in reverse order
        could just implement with an array

        PSUEDOCODE:
        put the root in the data structure
        start out with direction flag going left --> right


        at each level: create the subarray for that level
        determine the direction we're goin in - switch the flag
        for each node in that level - each node in our data structure:
            (iterate based on if we're goin lef to righ or right to left)

            pop it off
            store the value in the subarray to return
            queue up the children
                according to the direction our flag didctates
                if we're currently going left --> right:
                    add node left then node.right to the stack (separate data structure)

                if we're going right to left:
                    add node.right then node.left to the next-level stack
                if we're going left to right:
                    add node.left then node.right to the next-level stack
        add the array tot our final resulting array of arrays
        set next level stack to current stack
        '''

        
        if not root: 
            return []
        current_stack = []
        current_stack.append(root)
        zigzag_traversal = []
        # start out with direction flag going left --> right
        # TRUE is left to right, FALSE is right to left
        left_to_right = True
        # keep going until there are no more nodes (both stacks are empty)
        while len(current_stack) > 0: 
            # create the subarray for that level
            level_array = []
            next_stack = []
            while len(current_stack) > 0:  
                current_node = current_stack.pop()
                level_array.append(current_node.val)
                # queue up the children
                # if we're currently going left --> right: 
                if left_to_right:
                    if current_node.left: 
                        next_stack.append(current_node.left)
                    # add node.left, then node.right to the next-level's stack
                    if current_node.right: 
                        next_stack.append(current_node.right)
                # if we're going right --> left: 
                else: 
                    # add node.right then node.left to the next-level's stack
                    if current_node.right: 
                        next_stack.append(current_node.right)
                    if current_node.left: 
                        next_stack.append(current_node.left)
            # add the array to our final resulting array of arrays
            zigzag_traversal.append(level_array)
            # set next-level's stack to be current_stack
            current_stack = next_stack
            # switch the direction flag 
            left_to_right = not left_to_right
        return zigzag_traversal