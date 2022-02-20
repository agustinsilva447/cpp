#include <iostream>

int main()
{
	//char, short, int, long, float, double, bool
	unsigned int variable = 8;
	std::cout << variable << std::endl;
	variable = 20;
	std::cout << variable << std::endl;
	char a = 'A';
	std::cout << a << std::endl;
	char b = 65;
	std::cout << b << std::endl;
	short c = 65;
	std::cout << c << std::endl;
	short d = 'A';
	std::cout << d << std::endl;
	float variable2 = 5.5f;
	std::cout << variable2 << std::endl;
	double variable3 = 5.5;
	std::cout << variable3 << std::endl;
	bool variable4 = true;
	std::cout << variable4 << std::endl;
	bool variable5 = false;
	std::cout << variable5 << std::endl;
	
	std::cout << sizeof(variable5) << std::endl;
	std::cin.get();
}