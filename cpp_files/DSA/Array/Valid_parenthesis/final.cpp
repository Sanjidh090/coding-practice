#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    bool isValid(const string &s) {
        int balance1 = 0, balance2 = 0, balance3 = 0; // Counters for each type of bracket

        for (char current : s) {
            if (current == '(') {
                balance1++;
            } else if (current == ')') {
                if (balance1 == 0) return false;
                balance1--;
            } else if (current == '[') {
                balance2++;
            } else if (current == ']') {
                if (balance2 == 0) return false;
                balance2--;
            } else if (current == '{') {
                balance3++;
            } else if (current == '}') {
                if (balance3 == 0) return false;
                balance3--;
            }
        }

        // Check if all counters are zero
        return balance1 == 0 && balance2 == 0 && balance3 == 0;
    }
};

int main() {
    Solution sol;
    string input;

    cout << "Enter a string containing brackets (e.g., '()[]{}'): ";
    getline(cin, input);

    cout << boolalpha;
    cout << "Is the string valid? " << sol.isValid(input) << endl;

    return 0;
}