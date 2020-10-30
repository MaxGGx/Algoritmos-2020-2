#include <iostream>
#include "alist.h"

using namespace std;

alist::alist() {
	length = 0;
}

alist::~alist() {}

bool alist::isFull() {
	if (length == MAX_SIZE) return true;
	return false;
}

void alist::append(int x, int y) {
	if (isFull()) {
		cout << "Lista Llena" << endl;
		return;
	}

	array[length][0] = x;
	array[length][1] = y;
	length++;
}

bool alist::isIn(int x, int y) {
	int i;
	for (i = 0; i < length; i++) {
		if (array[i][0] == x && array[i][1] == y) return true;
	}
	return false;
}