#include <iostream>
#include <limits>
#include <stdlib.h>
#include <string>

using namespace std;

void Check(int *A, int i, int j, int *max, int *min) {
	int mid = (i + j) / 2;
	int l_min = numeric_limits<int>::max(), l_max = -1, k;

	for (k = i; k <= mid; k++) {
		if (A[k] >= l_max) l_max = A[k];
		if (A[k] <= l_min) l_min = A[k];
	}
	*max += l_max;
	*min += l_min;
	l_min = numeric_limits<int>::max();
	l_max = -1;

	for (k = mid + 1; k <= j; k++) {
		if (A[k] >= l_max) l_max = A[k];
		if (A[k] <= l_min) l_min = A[k];
	}
	*max += l_max;
	*min += l_min;
	l_min = numeric_limits<int>::max();
	l_max = -1;

	for (k = i; k <= j; k++) {
		if (A[k] >= l_max) l_max = A[k];
		if (A[k] <= l_min) l_min = A[k];
	}
	*max += l_max;
	*min += l_min;
}

void DesequilibrioHelp(int *A, int i, int j, int *max, int *min) {
	if (i == j) {
		*max += A[i];
		*min += A[i];
	}
	else {
		int mid = (i + j) / 2;

		DesequilibrioHelp(A, i, mid, max, min);
		DesequilibrioHelp(A, mid + 1, j, max, min);

		Check(A, i, j, max, min);
	}
}

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