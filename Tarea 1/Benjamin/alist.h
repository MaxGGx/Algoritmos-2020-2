#ifndef LIST_H
#define LIST_H
#define MAX_SIZE 80

class alist {
private:
	int length;
	int array[MAX_SIZE][2];
public:
	alist();
	~alist();
	bool isFull();
	void append(int, int);
	bool isIn(int, int);
};

#endif