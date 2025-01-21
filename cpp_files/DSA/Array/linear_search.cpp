#include <iostream>
using namespace std;

// Function to search for a key in the array
int searchKey(int arr[], int n, int key) {
    for (int i = 0; i < n; i++) { // Loop through each element in the array
        if (arr[i] == key) {     // Check if the current element matches the key
            return i;            // Return the index if key is found
        }
    }
    return -1;                   // Return -1 if key is not found
}

int main() {
    // Example array and size
    int arr[] = {3, 5, 7, 9, 11};
    int n = sizeof(arr) / sizeof(arr[0]); // Calculate the size of the array

    // Key to search for
    int key;
    cout << "Enter the key to search: ";
    cin >> key;

    // Call the searchKey function
    int result = searchKey(arr, n, key);

    // Display the result
    if (result != -1) {
        cout << "Key " << key << " found at index " << result << "." << endl;
    } else {
        cout << "Key " << key << " not found in the array." << endl;
    }

    return 0;
}
