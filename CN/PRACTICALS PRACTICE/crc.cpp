/*
Cyclic redundancy check (CRC):
error-detecting codes which are additional data added to a given digital message to help us detect if any error has occurred during transmission of the message.
Basic approach used for error detection is the use of redundancy bits, where additional bits are added to facilitate detection of errors.

*/

#include <iostream>

using namespace std;

string xorfun(string encoded, string crc) // Bitwise XOR operation
{
    int crclen = crc.length();

    for (int i = 0; i <= (encoded.length() - crclen);) // performing bitwise xor operation
    {                                                  // " 0 xor 0 = 0"     " 1 xor 1 = 0 "
        for (int j = 0; j < crclen; j++)               // " 0 xor 1 = 1 "    " 1 xor 0 = 1"
        {
            encoded[i + j] = encoded[i + j] == crc[j] ? '0' : '1'; // if encoded bit and crc bit are same , then replace it with zero
        }
        for (; i < encoded.length() && encoded[i] != '1'; i++)
            ;
    }

    return encoded;
}

int main()
{
    string data, crc, encoded = "";
    cout << endl
         << "-----------Sender Side --------------" << endl;
    cout << "Enter Data bits: " << endl;
    cin >> data; // data bits need to be transmitted

    cout << "Enter Generator: " << endl;
    cin >> crc; // crc - genearator polynomial ( agreed by sender & reciever)

    encoded += data; // encoded bits are initialized to data bits

    int datalen = data.length();
    int crclen = crc.length();

    for (int i = 1; i <= (crclen - 1); i++)
        encoded += '0'; // appending length of (generator polinomial -1) number of zeros to encoded bits

    encoded = xorfun(encoded, crc); // performing bitwise xor to obtain

    cout << "Checksum generated is: ";
    cout << encoded.substr(encoded.length() - crclen + 1) << endl
         << endl; // data bits + checksum bit is what going to be sent to reciever
    cout << "Message to be Transmitted over network: ";
    cout << data + encoded.substr(encoded.length() - crclen + 1); // this is the message going to be sent to the Reciever

    cout << endl
         << "---------------Reciever Side-----------------" << endl;

    cout << "Enter the message recieved: " << endl;
    string msg; // Reciever enters the recieved message
    cin >> msg;

    msg = xorfun(msg, crc); // bitwise xor is performed between recieved bits and the generator crc bits

    for (char i : msg.substr(msg.length() - crclen + 1)) // after performing xor , if the last few bits are zero then there's no error in transmission
        if (i != '0')
        {
            cout << "Error in communication " << endl; // if bits not zero ; ERROR IN TRANSMISSION
            return 0;
        }

    cout << "No Error !" << endl; // else NO ERROR
    return 0;
}