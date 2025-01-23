#include <iostream>
#include <stack>
#include <string>

using namespace std;

// Function to return precedence of operators
int precedence(char op) {
    if (op == '+' || op == '-') {
        return 1;
    } else if (op == '*' || op == '/') {
        return 2;
    }
    return 0;
}

// Function to perform the conversion from infix to postfix
string infixToPostfix(const string& infix) {
    stack<char> stack;
    string postfix;

    for (char c : infix) {
        // If the character is an operand, add it to the output
        if (isalnum(c)) {
            postfix += c;
        }
        // If the character is '(', push it to the stack
        else if (c == '(') {
            stack.push(c);
        }
        // If the character is ')', pop and output from the stack
        // until an '(' is encountered
        else if (c == ')') {
            while (!stack.empty() && stack.top() != '(') {
                postfix += stack.top();
                stack.pop();
            }
            stack.pop(); // pop '('
        }
        // If an operator is encountered
        else {
            while (!stack.empty() && precedence(stack.top()) >= precedence(c)) {
                postfix += stack.top();
                stack.pop();
            }
            stack.push(c);
        }
    }

    // Pop all the remaining elements from the stack
    while (!stack.empty()) {
        postfix += stack.top();
        stack.pop();
    }

    return postfix;
}

int main() {
    string infix = "A*(B+C)/D";
    string postfix = infixToPostfix(infix);
    cout << "Infix expression: " << infix << endl;
    cout << "Postfix expression: " << postfix << endl;
    return 0;
}
