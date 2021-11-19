#include<iostream>
#include<string>
using namespace std;
int add(int x , char y){

    return x +y ;

}
int main(){

    int a;
    char b;
    cin>>a>>b;
    int c = add(a,b);
    cout<<c<<endl;
}
