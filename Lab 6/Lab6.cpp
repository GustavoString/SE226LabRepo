
#include <iostream>
using namespace std;

float h_recursive(int n) {
    if(n==1) {
        return 1;
    }
    return  1 / (float)n + h_recursive(n-1);
}

float h_recursive() {
    cout<<"Enter an integer value for n: ";
    int n;
    cin>>n;

    if(n==1) {
        return 1;
    }
    return  1 / (float)n + h_recursive(n-1);
}

int main(){
    cout<<"Enter an integer value for n: ";
    int n;
    cin>>n;
    cout<<"Hn for the entered value: "<<h_recursive(n)<<endl;

    cout<<h_recursive();


    return 0;
}
