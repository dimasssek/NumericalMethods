//https://intuit.ru/studies/courses/2260/156/lecture/27239?page=3
#include <iostream>
#include <cmath>
#include <math.h>
#include <algorithm>
using namespace std;

double f11(double x) {
	return sin(x * x);
}

double f11p(double x) {
	return 2 * x * cos(x * x);
}

double f12(double x) {
	return x * x;
}

double f12p(double x) {
	return 1;
}

double f13(double x) {
	return -x;
}

double f13p(double x) {
	return -1;
}

double f21(double y) {
	return y * y;
}

double f21p(double x) {
	return 2 * x;
}

double f22(double x) {
	return x;
}

double f22p(double x) {
	return 1;
}

double f23(double x) {
	return -x;
}

double f23p(double x) {
	return -1;
}


double f31(double z) {
	return -z;
}

double f31p(double x) {
	return -1;
}


double f32(double x) {
	return x;
}

double f32p(double x) {
	return 1;
}

double f33(double x) {
	return x * x;
}

double f33p(double x) {
	return 2 * x;
}


double((*func[3][3]))(double x);
double((*funcp[3][3]))(double x);


// Условие окончания
bool converge(double xk[3], double xkp[3], int n, double eps)
{
	double norm = 0;
	for (int i = 0; i < n; i++) {
		norm = max(xk[i] - xkp[i], norm);
	}
	return norm < eps;
}

double okr(double x, double eps)
{
	int i = 0;
	double neweps = eps;
	while (neweps < 1)
	{
		i++;
		neweps *= 3;
	}
	int okr = pow(double(3), i);
	x = int(x * okr + 0.5) / double(okr);

	return x;
}

double matrYakob[3][3];

void inversion()
{
	int N = 3;
	double temp;

	double** E = new double* [N];

	for (int i = 0; i < N; i++)
		E[i] = new double[N];

	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
		{
			E[i][j] = 0.0;

			if (i == j)
				E[i][j] = 1.0;
		}

	for (int k = 0; k < N; k++)
	{
		temp = matrYakob[k][k];

		for (int j = 0; j < N; j++)
		{
			matrYakob[k][j] /= temp;
			E[k][j] /= temp;
		}

		for (int i = k + 1; i < N; i++)
		{
			temp = matrYakob[i][k];

			for (int j = 0; j < N; j++)
			{
				matrYakob[i][j] -= matrYakob[k][j] * temp;
				E[i][j] -= E[k][j] * temp;
			}
		}
	}

	for (int k = N - 1; k > 0; k--)
	{
		for (int i = k - 1; i >= 0; i--)
		{
			temp = matrYakob[i][k];

			for (int j = 0; j < N; j++)
			{
				matrYakob[i][j] -= matrYakob[k][j] * temp;
				E[i][j] -= E[k][j] * temp;
			}
		}
	}

	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			matrYakob[i][j] = E[i][j];

	for (int i = 0; i < N; i++)
		delete[] E[i];

	delete[] E;
}

void enterYkob(double x[3]) {

	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			if (i == j) {
				matrYakob[i][j] = funcp[i][j](x[i]);
			}
			else {
				matrYakob[i][j] = 0;
			}
		}
	}


	inversion();

}

int main()
{
	setlocale(LC_ALL, ".1251");

	func[0][0] = f11;	func[0][1] = f12;   func[0][2] = f13;
	func[1][0] = f21;	func[1][1] = f22;	func[1][2] = f23;
	func[2][0] = f31;	func[2][1] = f32;	func[2][2] = f33;

	funcp[0][0] = f11p;	funcp[0][1] = f12p;   funcp[0][2] = f13p;
	funcp[1][0] = f21p;	funcp[1][1] = f22p;	 funcp[1][2] = f23p;
	funcp[2][0] = f31p;	funcp[2][1] = f32p;	 funcp[2][2] = f33p;


	double eps = 0.0001, x[3], p[3];
	int n = 3, i, j, m = 0;



	/*
	Ход метода, где:
	a[n][n] - Матрица коэффициентов
	x[n], p[n] - Текущее и предыдущее решения
	Все перечисленные массивы вещественные и
	должны быть определены в основной программе,
	также в массив x[n] следует поместить начальное
	приближение столбца решений (например, все нули)
	*/

	x[0] = .001;	 x[1] = .001;  x[2] = .001;
	double varp[3];

		double sum[3];
		do {
			enterYkob(x);
			for (int i = 0; i < n; i++)
				p[i] = x[i];
			for (int i = 0; i < n; i++)
			{
				double var = 0;
				for (int j = 0; j < n; j++) {
					var += matrYakob[i][j] * func[i][j](p[j]);
				}

				x[i] = (p[i] - var);
			}
			
		} while (!converge(x, p, 3, eps));



		cout << "Решение системы:" << endl << endl;
		for (i = 0; i < n; i++) {
			cout << "x" << i << " = " << okr(x[i], eps) << "" << endl;
		}
		cout << endl;
		for (int i = 0; i < n; i++) {
			double sum = 0;
			for (int j = 0; j < n; j++) {
				sum += func[i][j](x[j]);
			}
			cout << "b" << i << " = " << sum << endl;
		}


	return 0;
}
