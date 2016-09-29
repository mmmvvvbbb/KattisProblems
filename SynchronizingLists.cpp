#include <iostream>
#include <list>
using namespace std;


struct ognum{
    int value;
    int pos;
};
bool cmp(ognum a, ognum b){
    return a.value < b.value;
};
list<ognum> list1;
list<int> list2;
int main()
{
    int a, b, num;
    while(cin >> a){
        b = a;
        ognum l;
        for(int i = 0; i < b; i++){
            cin >> l.value;
            l.pos = i;
            list1.push_back(l); 
        }
        
        for(int i = 0; i < b; i++){
            cin >> num;
            list2.push_back(num); 
        }
        
        list2.sort();
        list1.sort(cmp);
        int foo [b];
        for(ognum i : list1){
            foo[i.pos] = list2.front();
            list2.pop_front();
        }
        list1.clear();
        list2.clear();
        for(int i : foo){
            cout << i << endl;
        }
        cout << endl;
        if(a == 0){
            break;
        }
    }
}
