#include <iostream>
using namespace std;
int main(){
    string name, ID;
    cout<<"What is your name? "<<endl;
    cin>>name;
    cout<<"Hello "<<name<<endl;
    cout<<"What is your student ID? "<<endl;
    cin>>ID;
    cout<<"Your ID is "<<ID<<endl;





    float var1;
    float var2;
    cout<<"enter var1: "<<endl;
    cin>>var1;
    cout<<"enter var2: "<<endl;
    cin>>var2;
    float sum = var1 + var2;
    float diff = var1 - var2;
    float prod = var1 * var2;
    cout<<"var1: "<<var1<<endl;
    cout<<"var2: "<<var2<<endl;
    cout<<"sum: "<<sum<<endl;
    cout<<"diff: "<<diff<<endl;
    cout<<"prod: "<<prod<<endl;




    cout<<"Enter your name: "<<endl;
    cin>>name;
    cout<<"Enter your lab grade: "<<endl;
    float lab;
    cin>>lab;
    cout<<"Enter your midterm grade: "<<endl;
    float midterm;
    cin>>midterm;
    cout<<"Enter your final grade: "<<endl;
    float final;
    cin>>final;
    cout<<"Name: "<<name<<endl;
    cout<<"Lab grade: "<<lab<<endl;
    cout<<"Midterm grade: "<<midterm<<endl;
    cout<<"Final grade: "<<final<<endl;
    float lastScore = lab * 0.25 + midterm * 0.35 + final * 0.4;
    cout<<"Last score: "<<lastScore<<endl;




    cout<<""<<endl<<""<<endl<<""<<endl<<""<<endl<<"*"<<endl;

    return 0;
}