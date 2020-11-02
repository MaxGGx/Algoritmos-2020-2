#ifndef QUEUE_H
#define QUEUE_H
#define SIZE 80

/*
Clase cqueue:
Cola circular que almacena par de coordenadas (x, y)
basada en arreglo de largo SIZE (redefinible en casos de prueba grandes)
Private:
	int front: posicion de cabeza de la cola
	int rear: posicion de fin de la cola
	int **items: arreglo donde se guardan las coordenadas
Public:
	cqueue(): constructor de la clase,
		pide memoria en el heap para arreglo items (SIZE * 2)

	~cqueue(): destructor de la clase,
		libera la memoria pedida

	bool isFull(): chequea si la cola esta llena

	bool isEmpty(): cheque si la cola esta vacia

	void enQueue(int, int): recibe la coordenadas y las
		encola

	void deQueue(int *): recibe un arreglo de 2 enteros
		y guarda las coordenadas desencoladas
*/

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