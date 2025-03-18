#include <iostream>
auto main() -> signed {
    int a, b;
    std::cin >> a >> b;
    std::cout << (a + b & (b & 1));
    return 0;
}