#include <iostream>
#include <string>
using namespace std;

int main() {
    string name;
    cout << "Name: ";
    cin >> name;

    for (int i = 1; i <= 3; i++) {
        cout << "Hello, " << name << "! Round " << i << endl;
    }

    return 0;
}
