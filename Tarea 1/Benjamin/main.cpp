#include <iostream>
#include <stdlib.h>
#include "cqueue.h"
#include "alist.h"

using namespace std;

int main() {
	cqueue Q;
	Q.enQueue(2, 1);
	int arr[2];
	Q.deQueue(arr);
	cout << arr[0] << endl;

	alist L;
	L.append(2, 1);
	if (L.isIn(2, 1)) cout << "Esta" << endl;
	else cout << "No esta" << endl;
	if (L.isIn(1, 1)) cout << "Esta" << endl;
	else cout << "No esta" << endl;
	return 0;
}