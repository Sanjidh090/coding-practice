#include <iostream>
using namespace std;

int main()
{
    int arr[] = {10, 20, 60, 20, 50, 50};
    int key = 20;
    bool found = false;

    for(int i = 0; i < 6; i++)  // Iterate over all elements
    {
        if (arr[i] == key)
        {
            cout << key << " is present at index " << i << endl;
            arr[i] = 0;
            found = true;
        }
    }

    if (!found)
    {
        cout << key << " is not present" << endl;
    }
    
    return 0;
}
