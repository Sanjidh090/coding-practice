class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: list
        :rtype: list
        """
        head = sorted(head)  # Sort the list first
        for i in range(len(head)-1,-1,-1):  # Iterate in reverse
            if head[i] in head[i+1:]:  # Check for duplicates
                del head[i]  # Remove duplicate
        return head  # Return updated list


# Test the function
head = [1, 1, 2, 3, 3,4,5,6,6]
solution = Solution()
new_head = solution.deleteDuplicates(head)

# Print the output
print("Updated List:", new_head)
