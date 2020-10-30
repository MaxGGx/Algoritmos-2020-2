#ifndef QUEUE_H
#define QUEUE_H
#define SIZE 50

class cqueue {
private:
	int front;
	int rear;
	int items[SIZE][2];
public:
	cqueue();
	~cqueue();
	bool isFull();
	bool isEmpty();
	void enQueue(int, int);
	void deQueue(int *);
};

#endif