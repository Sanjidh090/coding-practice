#include <iostream>  // for std::cout
#include <stack>     // for std::stack
#include <string>    // for std::string

using namespace std;

class Solution {
public:
    char matchingOpen(char c) {
        if (c == ')') {
            return '(';
        } else if (c == ']') {
            return '[';
        } else { // c == '}'
            return '{';
        }
    }

    bool isValid(const string &s) {
        stack<char> st;

        // Using a traditional for loop with indexing
        for (int i = 0; i < s.size(); i++) {
            char current = s[i];

            // If it's an opening bracket, push it onto the stack
            if (current == '(' || current == '[' || current == '{') {
                st.push(current);
            }
            // If it's a closing bracket, we need to match it with the top of the stack
            else if (current == ')' || current == ']' || current == '}') {
                // If the stack is empty, there's no matching opening bracket
                if (st.empty()) {
                    return false;
                }
                // Check if the top of the stack is the correct matching bracket
                if (st.top() == matchingOpen(current)) {
                    st.pop();
                } else {
                    return false;
                }
            }
            // Otherwise (if current is neither opening nor closing), we do nothing
        }

        // After the loop, check if there are unclosed brackets
        return st.empty();
    }
};

int main() {
    Solution sol;
    
    // Test strings
    string test1 = "[{()}";   // Some sample brackets
    string test2 = "[-]";     
    string test3 = "{[(]}";
    string test4 = "([9])";

    // Use boolalpha to print true/false instead of 1/0
    cout << boolalpha;
    
    cout << "Test1: " << test1 << " => " << sol.isValid(test1) << endl;
    cout << "Test2: " << test2 << " => " << sol.isValid(test2) << endl;
    cout << "Test3: " << test3 << " => " << sol.isValid(test3) << endl;
    cout << "Test4: " << test4 << " => " << sol.isValid(test4) << endl;

    return 0;
}
