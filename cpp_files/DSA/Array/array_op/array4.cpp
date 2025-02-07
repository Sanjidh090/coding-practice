#include <iostream>
using namespace std;

int main() {
    int arr[100] = {18, 30, 15, 70, 12};
    int n = 4;
    int pos = 2; // position to delete (example: deleting the element at index 2, which is 15)
    arr[pos] = 0; // Set the element at the position to delete to 0
    // Shift elements to the left after the deleted position
    for(int i = pos; i < n ; i++){
        arr[i] = arr[i + 1];
    }

    // Reduce the size of the array by 1
    

    // Output the modified array
    for(int i = 0; i < n; i++){
        cout << arr[i] << " ";
    }

    return 0;
}
