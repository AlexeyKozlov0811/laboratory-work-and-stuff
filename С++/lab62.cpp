#include "pch.h"
//#include "stdafx.h"
#include <windows.h>
#include <iostream>

using namespace std;

bool block = false;
bool RCtrl = false, LAlt = false, F2 = false;
char vkStr[16] = "";

LRESULT CALLBACK LLKeyProc(int nCode, WPARAM wParam, LPARAM lParam)
{
	if (nCode == HC_ACTION)
	{
		DWORD vk = ((LPKBDLLHOOKSTRUCT)lParam)->vkCode;
		KBDLLHOOKSTRUCT *p = (KBDLLHOOKSTRUCT *)lParam;
		vkStr[0] = p->vkCode;
		if (block == true && (vk == 0x57))
		{
			return 1;
		}
		if (vk == 0x1b)
		{
			PostQuitMessage(0);
		}		
		cout << vkStr << " - " << vk << endl;
		if (vk == 0xA3 && wParam == WM_KEYDOWN) 
		{
			RCtrl = true;
		}
		if (vk == 0xA3 && wParam == WM_KEYUP) 
		{
			RCtrl = false;
		}
		if (vk == 0xA4 && wParam == WM_KEYDOWN) 
		{
			LAlt = true;
		}
		if (vk == 0xA4 && wParam == WM_KEYUP) 
		{
			LAlt = false;
		}
		if (vk == 0x71 && wParam == WM_KEYDOWN) 
		{
			F2 = true;
		}
		if (vk == 0x71 && wParam == WM_KEYUP) 
		{
			F2 = false;
		}

		if (RCtrl == true && LAlt == true && F2 == true) 
		{
			block = !block;
			switch (block)
			{
			case true:
				cout << "Клавіша „w“ заблокована " << endl;
				cout << "\a";
				RCtrl = false;
				LAlt = false;
				F2 = false;
				break;

			case false:
				cout << "Клавіша „w“ розблокована " << endl;
				break;
			}

		}


	}
	return CallNextHookEx(NULL, nCode, wParam, lParam);
}

int main()
{
	SetConsoleCP(1251);
	SetConsoleOutputCP(1251);
	HHOOK hook = SetWindowsHookEx(WH_KEYBOARD_LL, LLKeyProc, GetModuleHandle(NULL), 0);
	cout << "Right Ctrl + Left Alt + F2 - блокування або розблокування клавіши „w“" << endl << "Esc - вихід" << endl;
	if (hook)
	{
		while (WaitMessage())
		{
			MSG msg = { 0 };
			while (PeekMessage(&msg, NULL, 0, 0, PM_NOREMOVE))
			{
				/*  Beep(500, 300);*/
				if (msg.message == WM_QUIT)
				{
					UnhookWindowsHookEx(hook);
					return 0;
				}
				TranslateMessage(&msg);
				DispatchMessage(&msg);
			}
		}
	}
	return 0;
}