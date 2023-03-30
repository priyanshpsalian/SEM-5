// #include <cstdlib>
// #include <iostream>
// #include <math.h>
#include <bits/stdc++.h>
using namespace std;

int main(int argc, char **argv)
{

    int data_bits[20], m, r = 0, parity; // m = no. of data bits, r = no. of redundant bits

    cout << "Enter the size of data bits: ";
    cin >> m;

    // finding no. of redundant bits
    while (pow(2, r) < m + r + 1)
    {
        r++;
    }

    cout << "Enter the data bit: ";
    for (int i = 1; i <= m; i++)
        cin >> data_bits[i];

    int hamming[m + r], j = 0, k = 1;

    // finding positions of redundant bits.
    for (int i = 1; i <= m + r; i++)
    {

        if (i == pow(2, j))
        {
            hamming[i] = -1; //-1 is initial value of redundant bits
            j++;
        }
        else
        {
            hamming[i] = data_bits[k];
            k++;
        }
    }

    k = 0;
    int x, min, max = 0;
    // finding parity bit
    for (int i = 1; i <= m + r; i = pow(2, k))
    {
        k++;
        parity = 0;
        j = i;
        x = i;
        min = 1;
        max = i;
        while (j <= m + r)
        {
            for (x = j; max >= min && x <= m + r; min++, x++)
            {
                if (hamming[x] == 1)
                    parity = parity + 1;
                ;
            }
            j = x + i;
            min = 1;
        }

        // checking for even parity
        if (parity % 2 == 0)
        {
            hamming[i] = 0;
        }
        else
        {
            hamming[i] = 1;
        }
    }

    cout << "\nHamming code is: ";
    for (int i = 1; i <= m + r; i++)
        cout << hamming[i] << " ";

    return 0;
}