#include<iostream>
#include<list>
using namespace std;

int main()
{
    int num;
    short leftD;
    list<int> list1;

    cout<<"Enter a positive integer\n";
    cin>>num;
    do{
        leftD=num%10;
        list1.emplace_back(leftD);
        num=num/10;
    }while(num>0);

    cout<<"The left most number is\t:"<<leftD;
    cout<<"Here is a list of the digits:\t";

    for(int x : list1)
    {
        cout<<x<<" ";
    }

    cout<<"\n";

    return 0;
}
