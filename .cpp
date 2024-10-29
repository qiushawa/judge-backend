#include <iostream>
#include <cstdlib>
#include <string>
#include <windows.h>
#include <ctime>

using namespace std;

int main(){
    int x =GetSystemMetrics(SM_CXSCREEM);
    int y =GetSystemMetrics(SM_CYSCREEM);
    srand(time(0));
    while(1){
        SetCursorPos(999,999);
        return 0;
    }
    return 0;
}