#ifndef LIST_H
#define LIST_H
#define MAX_SIZE 100

class alist {
private:
	int length;
	int **array;
public:
	alist();
	~alist();
	bool isFull();
	void append(int, int);
	bool isIn(int, int);
};

#endif