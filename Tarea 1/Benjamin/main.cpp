#include <iostream>
#include <stdlib.h>
#include "cqueue.h"

using namespace std;

int main() {
	cqueue Q;

	Q.enQueue(2, 1);
	int arr[2];
	Q.deQueue(arr);
	cout << arr[0] << endl;
	return 0;
}