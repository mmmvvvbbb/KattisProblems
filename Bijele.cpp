#include <iostream>
#include <array>
using namespace std;
int main()
{
    int arr[6] = {1,1,2,2,2,8}; 
    int j;  
    for(int i = 0; i < 6; i++){
        cin >> j;
        cout << (arr[i] - j) << " ";
    }
}
