#include <iostream>
#include <limits>
#include <stdlib.h>
#include <string>

using namespace std;

/*
void Check(int *, int, int, int *, int *)
Recibe el arreglo A, una posicion inicial i, una posicion final j
y los contadores de maximos y minimos.
Recorre la seccion del arreglo dada y busca los maximos y minimos locales.
Luego calcula la cantidad de subarreglos que los incluyen y lo multiplica.
*/

void Check(int *A, int i, int j, int *max, int *min) {
	int mid = (i + j) / 2;
	int l_min = numeric_limits<int>::max(), l_max = -1;
	int pos_min = -1, pos_max = -1;
	int k;

	for (k = i; k <= j; k++) {
		if (A[k] >= l_max) {
			l_max = A[k];
			pos_max = k;
		}
		if (A[k] <= l_min) {
			l_min = A[k];
			pos_min = k;
		}
	}

	int mul1, mul2;
	int flag = 0;
	if (pos_max == i && pos_min == j) {
		mul1 = 1;
		mul2 = 0;
	}
	else if (pos_max <= pos_min) {
		mul1 = pos_max - i;
		mul2 = j - pos_min;
		flag = 1;
	}
	else {
		mul1 = pos_min - i;
		mul2 = j - pos_max;
		flag = 2;
	}

	*max += l_max * (mul1 + mul2);
	*min += l_min * (mul1 + mul2);
}

/*
void DesequilibrioHelp(int, int, int, int *, int *)
Recibe el arreglo A, una posicion inicial i, una posicion final j
y los contadores de maximos y minimos.
Se llama recursivamente con 2 subarreglos de tamano n/2 hasta 
llegar a subarreglos de largo 1, para luego llamar a Check.
*/

void DesequilibrioHelp(int *A, int i, int j, int *max, int *min) {
	if (i == j) return;
	else {
		int mid = (i + j) / 2;

		DesequilibrioHelp(A, i, mid, max, min);
		DesequilibrioHelp(A, mid + 1, j, max, min);

		Check(A, i, j, max, min);
	}
}

/*
int Desequilibrio(int *, int, int)
Funcion "inicial" que instancia los contadores de 
maximos y minimos y llama a DesequilibrioHelp, la que
hara la recursion.
*/

int Desequilibrio(int *A, int i, int j) {
	int *max, *min;
	max = (int *)malloc(sizeof(int));
	min = (int *)malloc(sizeof(int));
	*max = 0;
	*min = 0;
	DesequilibrioHelp(A, i, j, max, min);

	int fin = (*max - *min);
	free(max);
	free(min);
	return fin;
}

int main() {
	int len;
	string buff;
	cin >> buff;
	len = stoi(buff);

	int i;
	int *A = (int *)malloc(len * sizeof(int));
	for (i = 0; i < len; i++) {
		cin >> buff;
		A[i] = stoi(buff);
	}

	cout << Desequilibrio(A, 0, len - 1) << endl;
	free(A);
	return 0;
}