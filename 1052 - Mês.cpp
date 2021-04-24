#include <iostream>
using namespace std;
#define MAX 12
#define MAX_STRING 100

int main()
{
    int num;
    cin >> num;
    char months[MAX][MAX_STRING] = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"};
    cout <<months[num-1] << endl;
    return 0;
}
