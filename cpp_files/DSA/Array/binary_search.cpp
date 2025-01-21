#include <iostream>
using namespace std;

// Function to search for a key in the array
int BinarysearchKey(int arr[], int n, int key) {
    int low = 0;
    int SIZE = n;
    int high = SIZE -1;
    int middle;
    while ( low <= high)
    {
        middle = (low + high )/2;
        if(key = arr[middle])
            return middle;
        else if( key < arr[middle])
            high = middle -1 ;
        else 
            low = middle + 1;
    }
    return -1;
    }// Return -1 if key is not found


int main() {
	// Example array and size
	int arr[] = {3, 5, 7, 9, 11};
	int n = sizeof(arr) / sizeof(arr[0]); // Calculate the size of the array

	// Key to search for
	int key;
	cout << "Enter the key to search: ";
	cin >> key;

	// Call the searchKey function
	int result = BinarysearchKey(arr, n, key);

	// Display the result
	if (result != -1) {
		cout << "Key " << key << " found at index " << result << "." << endl;
	} else {
		cout << "Key " << key << " not found in the array." << endl;
	}

	return 0;
}
