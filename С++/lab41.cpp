#include <time.h>
#include <random>
#include <stdio.h>
#include <iostream>
#include <Windows.h>

using namespace std;
using std::cout;

void matrix(int **arr_1, int n)
{
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			arr_1[i][j] = rand() % 100;
		}
	}
}

void print_matrix(int **arr_1, int n)
{
	
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			arr_1[i][j] = rand() % 100;
			printf("%3d ", arr_1[i][j]);
		}
		cout << endl << endl;
	}
}

void rotate(int **arr_1, int **arr_2, int n)
{
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			arr_2[i][j] = arr_1[n - j - 1][i];
		}
	}
	
}

void print_rotate(int **arr_2, int n)
{
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			printf("%3d ", arr_2[i][j]);
		}
		cout << endl << endl;
	}
}

void main()
{
	SetConsoleCP(1251);
	SetConsoleOutputCP(1251);
	srand(0);
	int choice = -1;
	int n;
	cout << "³���� �������\n������ ��������� ��������� �������: ";
	cin >> n;
	cout << endl;
	int **arr_1;
	int **arr_2;

	arr_1 = new int*[n];
	for (int i = 0; i < n; i++)
		arr_1[i] = new int[n];

	arr_2 = new int*[n];
	for (int i = 0; i < n; i++)
		arr_2[i] = new int[n];

	matrix(arr_1, n);

	while (choice != 0)
	{
		cout << endl;
		cout << "1) ������� ������� �� �����\n2) ������� ����������� �� 90� �� ������������ ������� ������� �� �����\n3) �����\nĳ� - ";
		cin >> choice;
		cout << endl;
		switch (choice) 
		{
			case 1:
			{
				print_matrix(arr_1, n);
				break;
			}
			case 2:
			{
				rotate(arr_1, arr_2, n);
				print_rotate(arr_2, n);
				break;
			}
			default:
			{
				choice=0;
				break;
			}
		}
	}
		delete[]arr_1;
		delete[]arr_2;
		cin.get();
		cin.get();
	
}