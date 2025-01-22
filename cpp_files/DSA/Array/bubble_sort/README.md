# Special Bubble Sort Implementation in C++

This repository contains a C++ implementation of the Bubble Sort algorithm with a unique twist on the traditional method. This version not only uses an integer instead of a boolean to monitor swap occurrences but also provides a step-by-step display of the array's state after each comparison, making it highly educational for understanding how values are swapped during the sorting process.

## Description

Bubble sort is a simple sorting algorithm that works by repeatedly stepping through the list, comparing adjacent items, and swapping them if they are in the wrong order. The algorithm continues until no swaps are needed, indicating that the list is sorted. This implementation enhances understanding by visually showing the array's state at each comparison step.

## Features

- **Step-by-Step Visualization**: Outputs the array at each comparison, allowing users to visually track the sorting progress.
- **Swapping Indicator**: Uses an integer (`swapped`) instead of a boolean to indicate whether any swaps have occurred, optimizing the process by potentially stopping early if the array becomes sorted before all passes are completed.
- **Optimized and Educational**: An excellent resource for teaching and understanding how bubble sort works, especially with the visual aid of seeing the array change after each swap.

## Compilation and Execution

You can compile and run this program if you have a C++ compiler (like GCC or Clang) installed. Use the following commands in your terminal:

```bash
g++ -o BubbleSort BubbleSort.cpp
./BubbleSort
