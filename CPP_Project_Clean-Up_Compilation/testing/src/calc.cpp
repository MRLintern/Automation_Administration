#include <iostream>
#include "calc.hpp"

int main() {

	//numbers for user to enter
	double a, b;

	std::cout<<"Enter two numbers: "; std::cin>>a>>b;

	//call functions for answers to maths problems
	std::cout<<"Addition of those numbers is: "<<add(a,b)<<std::endl;
	std::cout<<"Subtraction of those two numbers is: "<<subtract(a,b)<<std::endl;
	std::cout<<"Multiplication of those two numbers is: "<<multiply(a,b)<<std::endl;
	std::cout<<"Division of those two numbers is: "<<division(a,b)<<std::endl;

}

//--function definitions--//

double add(double a, double b) {

	return a + b;
}

double subtract(double a, double b) {

	return a - b;
}

double multiply(double a, double b) {

	return a * b;
}

double division(double a, double b) {

	return a / b;

}
