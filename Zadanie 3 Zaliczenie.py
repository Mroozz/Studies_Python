#include <iostream>
#include <Windows.h>
#include <time.h>
#include <stdio.h>

using namespace std;
int liczba[6]; 
float liczba_gracza[6];
int main()
{
	cout << "Witaj w losowaniu lotto!" << endl;
	cout << "Pamietaj wybrac liczbe od 1 do 49 :) " << endl;

	for (int i = 0; i < 6; i++) 
	{
		cout << endl << "Wytypuj swoja " << i + 1 << "  liczbe ";
		cin >> liczba_gracza[i];
	}
	cout << "Za 3 sekundy nastapi zwolnienie blokady!" << endl;
	Sleep(3000);
	cout << endl;
	srand(time(NULL));
	for (int i = 1; i <= 6; i++)
	{
		liczba[6] = rand() % 49 + 1;
		Sleep(1000);
		cout << liczba[6] << "\a" << endl;
	}
	getchar(); getchar();

	return 0;

}