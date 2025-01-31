#include <iostream>
using namespace std;

class Solution {
public:
    int* deleteDuplicates(int* head, int size, int& newSize) {
        static int unique[100]; // Assuming a max size of 100 for simplicity
        newSize = 0;
        
        for (int i = 0; i < size; ++i) {
            bool isDuplicate = false;
            for (int j = 0; j < newSize; ++j) {
                if (head[i] == unique[j]) {
                    isDuplicate = true;
                    break;
                }
            }
            if (!isDuplicate) {
                unique[newSize++] = head[i];
            }
        }
        
        return unique; // Return updated array
    }
};

int main() {
    Solution sol;
    int nums[] = {4, 2, 2, 1, 3, 4, 5};
    int size = sizeof(nums) / sizeof(nums[0]);
    int newSize;
    
    int* result = sol.deleteDuplicates(nums, size, newSize);
    
    cout << "Updated list: ";
    for (int i = 0; i < newSize; ++i) {
        cout << result[i] << " ";
    }
    cout << endl;
    
    return 0;
}
