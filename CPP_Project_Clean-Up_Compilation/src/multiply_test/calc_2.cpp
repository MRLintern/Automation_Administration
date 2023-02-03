#include <iostream>

double multiply(double, double);

int main() {

	int a, int b;

	std::cout<<"Enter 2 numbers: ";
	std::cin>>a>>b;

	std::cout<<"\n";

	std::cout<<"Multiplying "<<a<<" and "<<b<<" is "<<multiply(a,b)<<std::endl;


}

double multiply(double a, double b) {

	return a*b;

}
