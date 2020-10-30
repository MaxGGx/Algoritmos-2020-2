#include <iostream>
#include "cqueue.h"

using namespace std;

cqueue::cqueue() {
	front = -1;
	rear = -1;
}

cqueue::~cqueue() {}

bool cqueue::isFull() {
	if (front == 0 && rear == SIZE - 1) return true;
	if (front == rear + 1) return true;
	return false;
}

bool cqueue::isEmpty() {
	if (front == -1) return true;
	return false;
}

void cqueue::enQueue(int x, int y) {
	if (isFull()) {
		cout << "Cola Llena" << endl;
		return;
	}

	if (front == -1) front = 0;
	rear = (rear + 1) % SIZE;
	items[rear][0] = x;
	items[rear][1] = y;
}

void cqueue::deQueue(int *arr) {
	if (isEmpty()) {
		cout << "Cola Vacia" << endl;
		return;
	}

	arr[0] = items[front][0];
	arr[1] = items[front][1];
	if (front == rear) {
		front = -1;
		rear = -1;
	}
	else front = (front + 1) % SIZE;
}