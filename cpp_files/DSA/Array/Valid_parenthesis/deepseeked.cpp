#include <iostream>  // for std::cout, std::cin
#include <string>    // for std::string, std::getline

using namespace std;

class Solution {
public:
    bool isValid(const string &s) {
        string stack; // Use a string to simulate a stack

        // Manually written for loop using an index
        for (int i = 0; i < s.size(); i++) {
            char current = s[i]; // Get the current character

            // If it's an opening bracket, push it onto the stack
            if (current == '(' || current == '[' || current == '{') {
                stack.push_back(current);
            }
            // If it's a closing bracket, check if it matches the top of the stack
            else if (current == ')' || current == ']' || current == '}') {
                // If the stack is empty, there's no matching opening bracket
                if (stack.empty()) {
                    return false;
                }
                // Check if the top of the stack is the correct matching bracket
                char top = stack.back();
                if ((current == ')' && top == '(') ||
                    (current == ']' && top == '[') ||
                    (current == '}' && top == '{')) {
                    stack.pop_back(); // Remove the top element
                } else {
                    return false;
                }
            }
        }

        // After the loop, check if there are unclosed brackets
        return stack.empty();
    }
};

int main() {
    Solution sol;
    string input;

    // Prompt the user to enter a string
    cout << "Enter a string containing brackets (e.g., '()[]{}'): ";
    getline(cin, input); // Use getline to read the entire input, including spaces

    // Use boolalpha to print true/false instead of 1/0
    cout << boolalpha;

    // Check if the input string is valid and print the result
    cout << "Is the string valid? " << sol.isValid(input) << endl;

    return 0;
}