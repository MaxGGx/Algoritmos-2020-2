#ifndef LIST_H
#define LIST_H
#define MAX_SIZE 100

/*
Clase alist:
Lista simplificada basada en arreglo de largo MAX_SIZE (redefinible en casos de prueba grandes),
almacena par de coordenadas (x, y)
Private:
	int length: largo de la lista
	int **array: arreglo donde se guardan las coordenadas
Public:
	alist(): constructor de la clase,
		pide memoria en el heap para arreglo items (MAX_SIZE * 2)
	~alist(): destructor de la clase,
		libera la memoria pedida
	bool isFull(): chequea si la cola esta llena

	void append(int, int): recibe un par de coordenadas
		y los almacena al final de la lista

	bool isIn(int, int): chequea si el par de coordenadas dadas
		estan en la lista
*/

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