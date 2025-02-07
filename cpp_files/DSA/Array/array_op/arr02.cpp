#include <iostream>
using namespace std;

int main() {   
    // Define the array and its initial size (with one empty slot for insertion).
    int arr[6] = {1, 2, 3, 5, 6}; // Array has space for 6 elements.
    int size = 5; // Initial number of elements in the array.
    
    // Element to insert and position to insert it at.
    int x = 4, pos = 3;

    // Shift elements to the right starting from the last index to make space for the new element.
    for (int i = size; i > pos; i--) {
        arr[i] = arr[i - 1]; // Move elements rightward
    }

    // Insert the new element 'x' at the specified position.
    arr[pos] = x;

    // Increment the size after insertion.
    size++;

    // Print the array after the insertion.
    for (int j = 0; j < size; j++) {
        cout << arr[j] << " "; // Output each element of the array.
    }

    return 0;
}
