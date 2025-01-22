#include <iostream>
using namespace std;
// Function to perform the bubble sort
void bubbleSort(int array[], int size) {
    for (int step = 0; step < size - 1; ++step) {
    // Use an integer to track if a swap occurred
        int swapped = 0;
        // Compare each pair of adjacent elements
        for (int i = 0; i < size - step - 1; ++i) {
            for (int j = 0; j < size; j++) {
                cout << array[j] << " ";
            }
            cout << endl;
            if (array[i] > array[i + 1]) {

                // Swap if the current element is greater than the next
                int temp = array[i];
                array[i] = array[i + 1];
                array[i + 1] = temp;
                swapped = 1; // Set swapped to 1 if a swap occurs
            }
        }

        // If no two elements were swapped by inner loop, then break
        if (swapped == 0) {
            break;
        }
    }
}

// Function to print an array
void printArray(int array[], int size) {
    for (int i = 0; i < size; ++i) {
        std::cout << array[i] << " ";
    }
    std::cout << std::endl;
}

// Main function to run the program
int main() {
    int data[] = {64, 34, 25, 12, 22, 11, 90};
    int size = sizeof(data) / sizeof(data[0]);
    std::cout << "Unsorted Array: ";
    printArray(data, size);

    bubbleSort(data, size);

    std::cout << "Sorted Array:   ";
    printArray(data, size);

    return 0;
}
