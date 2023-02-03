#include <iostream>

double add(double, double);

int main() {

	int a, b;

	std::cout<<"Enter 2 doubles: "<<std::endl;
	std::cin>>a>>b;

	std::cout<<"\n";

	std::cout<<"The sum of "<<a<< " and "<<b<<" is "<<add(a,b)<<std::endl;

}

double add(double a, double b) {

	return a + b;
  
}
