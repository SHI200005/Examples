#include <iostream>

using namespace std;

int add_numbers(int a, int b) {
    return a + b;
}

int main() {
    int x = 10;
    int y = 5;
    
    // 设置一个错误，y的值应该为负数
    y = -y;
    
    cout << "Result: " << add_numbers(x, y) << endl;
    
    return 0;
}
