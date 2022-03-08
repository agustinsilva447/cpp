#include <iostream>

int main()
{
 	/* This is a multi-line comment.
    This line will be ignored.
    So will this one. */

	int a = 5, b = 6;		// copy initialization
	int c(7), d(8);			// direct initialization
	int e{9}, f{10};	// brace initialization (preferred)

	std::cout << "Hello world!\n";                 // std::cout lives in the iostream library
	std::cout << "It is very nice to meet you!\n"; // this is much easier to read
	std::cout << "Yeah!\n";                        // don't you think so?
}