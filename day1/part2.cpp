#include <bits/stdc++.h>
using namespace std;

int calculate_fuel(int mass){
    int fuel=max(mass/3-2,0);
    if (fuel==0){
        return 0;
    } else {
        return fuel+calculate_fuel(fuel);
    }
}

int main(int argc, const char *argv[])
{
    string line;
    ifstream input ("input2.txt");
    int ans=0;
    if (input.is_open()) {
        while (getline (input, line)) {
            int curr_mass=stoi(line);
            ans+=calculate_fuel(curr_mass);
        }
        input.close();
    }
    cout << ans << endl;

    
    return 0;
}
