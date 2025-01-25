#include <iostream>
#include <stack>
#include <string>
using namespace std;

class Solution {
public:
    // Returns the corresponding opening bracket for a given closing bracket
    char matchingOpen(char c) {
        if (c == ')') {
            return '(';
        } else if (c == ']') {
            return '[';
        } else { // c == '}'
            return '{';
        }
    }
    
    // Checks if the string s contains valid parentheses
    bool isValid(const string &s) {
        stack<char> st;
        
        for (char current : s) {
            if (current == '(' || current == '[' || current == '{') {
                // Push opening bracket onto the stack
                st.push(current);
            } 
            else if (current == ')' || current == ']' || current == '}') {
                // If there's no opening bracket, return false
                if (st.empty()) {
                    return false;
                }
                // Check if the stack top matches the current closing bracket
                if (st.top() == matchingOpen(current)) {
                    st.pop();
                } else {
                    return false;
                }
            }
        }
        
        // If stack is empty, parentheses are valid
        return st.empty();
    }
};

int main() {
    Solution sol;
    
    // Test cases
    string test1 = "[{()}";   // Valid
    string test2 = "[-]";       // Invalid
    string test3 = "{[(]}";   // Valid
    string test4 = "([9])";     // Invalid

    // Print results
    cout << boolalpha;  // Print "true"/"false" instead of "1"/"0"
    cout << "Test1: " << test1 << "  =>  " << sol.isValid(test1) << endl;
    cout << "Test2: " << test2 << "  =>  " << sol.isValid(test2) << endl;
    cout << "Test3: " << test3 << "  =>  " << sol.isValid(test3) << endl;
    cout << "Test4: " << test4 << "  =>  " << sol.isValid(test4) << endl;

    return 0;
}
