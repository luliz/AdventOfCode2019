#include <bits/stdc++.h>
using namespace std;

int main(int argc, const char *argv[])
{
    string line;
    ifstream input ("input1.txt");
    int ans=0;
    if (input.is_open()) {
        while (getline (input, line)) {
            int curr_mass=stoi(line);
            int curr_fuel=curr_mass/3-2;
            ans+=curr_fuel;
        }
        input.close();
    }
    cout << ans << endl;

    
    return 0;
}
