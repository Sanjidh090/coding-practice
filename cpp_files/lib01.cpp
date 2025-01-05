#include <iostream>
#include <fstream>
#include <string>

using namespace std;

class Account {
private:
    string name;
    int accountNumber;
    double balance;

public:
    Account(const string &name, int accountNumber, double initialBalance)
        : name(name), accountNumber(accountNumber), balance(initialBalance) {}

    void deposit(double amount) {
        balance += amount;
        ofstream logFile("transactions.log", ios::app); // Ensure file is opened in append mode
        logFile << "Deposited: " << amount << ", New Balance: " << balance << endl;
        logFile.close() ;// Explicitly closing the file
    }

    void withdraw(double amount) {
        if (balance >= amount) {
            balance -= amount;
            ofstream logFile("transactions.log", ios::app);
            logFile << "Withdrew: " << amount << ", New Balance: " << balance << endl;
        } else {
            ofstream logFile("transactions.log", ios::app);
            logFile << "Failed Withdrawal of " << amount << " (Insufficient funds)" << endl;
            logFile.close(); // Ensure the file is closed in each scenario
        }
    }

    // It might be useful to add a function to display account details or check the balance
    void displayAccountDetails() {
        cout << "Account Holder: " << name << endl;
        cout << "Account Number: " << accountNumber << endl;
        cout << "Current Balance: $" << balance << endl;
    }
};

int main() {
    Account myAccount("John Doe", 123456, 1000.00);
    myAccount.deposit(500);
    myAccount.withdraw(200);
    myAccount.withdraw(1500); // This should log an insufficient funds message
    myAccount.displayAccountDetails(); // Optional: display account details after transactions

    return 0;
}
