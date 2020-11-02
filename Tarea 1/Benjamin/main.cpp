#include <iostream>
#include <stdlib.h>
#include <string>
#include <string.h>
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
	int casos;
	string buff;

	cin >> buff;
	casos = stoi(buff);

	int i;
	for (i = 0; i < casos; i++) {
		int n = 0, m = 0;
		char **grid;
		string total = "";

		if (i == 0) cin >> buff;
		while (buff[0] == 'L' || buff[0] == 'W') {
			if (m == 0) m = buff.length();
			total += buff;
			total += "S";
			n++;
			cin >> buff;
		}
		total = total.substr(0, total.length() - 1);

		grid = (char **)malloc(n * sizeof(char *));
		int j;
		for (j = 0; j < n; j++) grid[j] = (char *)malloc((m + 1) * sizeof(char));

		size_t pos = 0;
		string del = "S", token;
		j = 0;
		while ((pos = total.find(del)) != string::npos) {
			token = total.substr(0, pos);
			strcpy(grid[j], token.c_str());
			total.erase(0, pos + del.length());
			j++;
		}
		strcpy(grid[j], total.c_str());

		do {
			if (buff[0] != 'L' && buff[0] != 'W') {
				int x1 = stoi(buff);
				cin >> buff;
				cout << Lagunas(grid, n, m, x1, stoi(buff)) << endl;
			}
			else break;
		} while (cin >> buff && (buff[0] != 'L' || buff[0] != 'W'));

		for (j = 0; j < n; j++) free(grid[j]);
		free(grid);
		cout << endl;
	}
	return 0;
}