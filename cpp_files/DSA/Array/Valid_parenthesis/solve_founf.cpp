#include <iostream>
#include <stack>
#include <string>

using namespace std;

class Solution {
public:
    bool isValid(const string &s) {
        stack<char> st;

        for (int i = 0; i < s.size(); i++) {
            char current = s[i];

            // If it's an opening bracket, push it onto the stack
            if (current == '(' || current == '[' || current == '{') {
                st.push(current);
            }
            // If it's a closing bracket:
            else if (current == ')' || current == ']' || current == '}') {
                // If the stack is empty, there's no opening bracket to match
                if (st.empty()) {
                    return false;
                }

                // Check if the top of the stack matches the current closing bracket
                if ( (current == ')' && st.top() == '(') ||
                     (current == ']' && st.top() == '[') ||
                     (current == '}' && st.top() == '{') ) {
                    st.pop();
                } else {
                    return false;
                }
            }
            // For any other character, we do nothing
        }

        // If the stack is empty at the end, all brackets matched
        return st.empty();
    }
};

int main() {
    Solution sol;
    
    // Test strings
    string test1 = "[{()}";
    string test2 = "[-]";
    string test3 = "{[(]}";
    string test4 = "([9])";

    // boolalpha prints true/false instead of 1/0
    cout << boolalpha;
    
    cout << "Test1: " << test1 << " => " << sol.isValid(test1) << endl;
    cout << "Test2: " << test2 << " => " << sol.isValid(test2) << endl;
    cout << "Test3: " << test3 << " => " << sol.isValid(test3) << endl;
    cout << "Test4: " << test4 << " => " << sol.isValid(test4) << endl;

    return 0;
}
