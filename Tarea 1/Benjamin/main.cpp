#include <iostream>
#include <stdlib.h>
#include "cqueue.h"
#include "alist.h"

using namespace std;

/*
x mide desde arriba hacia abajo: 1-n
y mide desde izquierda hacia derecha: 1-m

FUNCION AUXILIAR
bool checkCoor(int, int, int, int)
Recibe el tamano del mapa (n, m) y un par de coordenadas (x, y)
Chequea si las coordenadas dadas estan dentro de los limites del mapa
*/

bool checkCoor(int n, int m, int x, int y) {
	if (x >= n || x < 0) return false;
	if (y >= m || y < 0) return false;
	return true;
}

/*
ALGORITMO PRINCIPAL
int Lagunas(char **, int, int, int, int) 
Recibe el mapa (grid), su tamano (n, m) y las coordenadas de la primera
casilla de agua (x1, y1)
Encola dicha casilla y la marca como revisada (la agrega a la lista), luego
mientras exista un par de coordenadas en la cola, revisa la 8 casillas adyacentes:
Si son agua, las encola para iterar en ellas posteriormente y las marca como revisadas,
suma al contador total y termina la iteracion actual
*/

int Lagunas(char **grid, int n, int m, int x1, int y1) {
	int fin = 1;
	x1--;
	y1--;
	cqueue Q;
	alist L;
	Q.enQueue(x1, y1);
	L.append(x1, y1);

	while (!Q.isEmpty()) {
		int temp[2];
		Q.deQueue(temp);
		int x = temp[0], y = temp[1];
		//OXX
		//XWX
		//XXX
		if (checkCoor(n, m, x - 1, y - 1) && !L.isIn(x - 1, y - 1))  //Coordenada Valida && No revisada antes
			if (grid[x - 1][y - 1] == 'W') {                         //Es una casilla de agua
				L.append(x - 1, y - 1);   //Se agrega a los revisados
				Q.enQueue(x - 1, y - 1);  //Se encola para siguiente iteracion
				fin++;
			}
		//XOX
		//XWX
		//XXX
		if (checkCoor(n, m, x - 1, y) && !L.isIn(x - 1, y))
			if (grid[x - 1][y] == 'W') {
				L.append(x - 1, y);
				Q.enQueue(x - 1, y);
				fin++;
			}
		//XXO
		//XWX
		//XXX
		if (checkCoor(n, m, x - 1, y + 1) && !L.isIn(x - 1, y + 1))
			if (grid[x - 1][y + 1] == 'W') {
				L.append(x - 1, y + 1);
				Q.enQueue(x - 1, y + 1);
				fin++;
			}
		//XXX
		//OWX
		//XXX
		if (checkCoor(n, m, x, y - 1) && !L.isIn(x, y - 1))
			if (grid[x][y - 1] == 'W') {
				L.append(x, y - 1);
				Q.enQueue(x, y - 1);
				fin++;
			}
		//XXX
		//XWO
		//XXX
		if (checkCoor(n, m, x, y + 1) && !L.isIn(x, y + 1))
			if (grid[x][y + 1] == 'W') {
				L.append(x, y + 1);
				Q.enQueue(x, y + 1);
				fin++;
			}
		//XXX
		//XWX
		//OXX
		if (checkCoor(n, m, x + 1, y - 1) && !L.isIn(x + 1, y - 1))
			if (grid[x + 1][y - 1] == 'W') {
				L.append(x + 1, y - 1);
				Q.enQueue(x + 1, y - 1);
				fin++;
			}
		//XXX
		//XWX
		//XOX
		if (checkCoor(n, m, x + 1, y) && !L.isIn(x + 1, y))
			if (grid[x + 1][y] == 'W') {
				L.append(x + 1, y);
				Q.enQueue(x + 1, y);
				fin++;
			}
		//XXX
		//XWX
		//XXO
		if (checkCoor(n, m, x + 1, y + 1) && !L.isIn(x + 1, y + 1))
			if (grid[x + 1][y + 1] == 'W') {
				L.append(x + 1, y + 1);
				Q.enQueue(x + 1, y + 1);
				fin++;
			}
	}

	return fin;
}

int main() {
	/*char test[6][3] = {
		{'W', 'L', 'L'},
		{'L', 'L', 'L'},
		{'L', 'W', 'L'},
		{'W', 'L', 'W'},
		{'L', 'W', 'W'},
		{'L', 'L', 'L'}
	};*/
	char **test = (char **)malloc(6 * sizeof(char *));
	int i;
	for (i = 0; i < 6; i++) test[i] = (char *)malloc(3 * sizeof(char));
	test[0][0] = 'W'; test[0][1] = 'L'; test[0][2] = 'L';
	test[1][0] = 'L'; test[1][1] = 'L'; test[1][2] = 'L';
	test[2][0] = 'L'; test[2][1] = 'W'; test[2][2] = 'L';
	test[3][0] = 'W'; test[3][1] = 'L'; test[3][2] = 'W';
	test[4][0] = 'L'; test[4][1] = 'W'; test[4][2] = 'W';
	test[5][0] = 'L'; test[5][1] = 'L'; test[5][2] = 'L';

	cout << Lagunas(test, 6, 3, 1, 1) << endl;
	cout << Lagunas(test, 6, 3, 3, 2) << endl;

	for (i = 0; i < 6; i++) free(test[i]);
	free(test);
	return 0;
}