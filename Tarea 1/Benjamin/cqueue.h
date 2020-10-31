#ifndef QUEUE_H
#define QUEUE_H
#define SIZE 80

class cqueue {
private:
	int front;
	int rear;
	int **items;
public:
	cqueue();
	~cqueue();
	bool isFull();
	bool isEmpty();
	void enQueue(int, int);
	void deQueue(int *);
};

#endif