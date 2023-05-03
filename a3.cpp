#include <iostream>
#include <iomanip>
#include <stdlib.h>
#include <math.h>
#include <fstream>
using namespace std;
double f1(double x, double y, double z) {
    //return 2 * z - y;
    //return 2 * y - z;
    //return log(y + 2 * pow(sin(x / 2), 2)) - z / 2;
    return 4 * y - 2 * z + sin(x);
}
double f2(double x, double y, double z) {
    //return 4 * z - 3 * y + exp(3 * x) / (exp(2 * x) + 1);
    //return y + 2 * exp(x);
    //return (4 - y * y) * cos(x) - 2 * x * pow(sin(x), 2) - pow(cos(x), 3);
    return 2 * y - z - 2 * cos(x);
}
int main()
{
    setlocale(LC_ALL, "rus");
    int i, j;
    double a, b, h;
    cout << "Введите границы" << endl;
    cin >> a >> b;
    cout << "Введите величину шага " << endl;
    cin >> h;
    int n = (b - a) / h + 1;
    double* x, * y, * del, * z;
    x = new double[n + 1];
    y = new double[n + 1];
    del = new double[n + 1];
    z = new double[n + 1];
    fstream file1, file2;
    file1.open("file1.txt");
    file2.open("file2.txt");
    x[0] = a;
    cout << "Введите начальные значения функций " << endl;
    cin >> y[0] >> z[0];
    for (i = 1; i <= n - 1; i++)
    {
        x[i] = a + i * h;
        if (i <= 3)
        {

            double k1 = h * f1(x[i - 1], y[i - 1], z[i - 1]);
            double l1 = h * f2(x[i - 1], y[i - 1], z[i - 1]);

            double k2 = h * f1(x[i - 1] + h / 2, y[i - 1] + k1 / 2, z[i - 1] + l1 / 2);
            double l2 = h * f2(x[i - 1] + h / 2, y[i - 1] + k1 / 2, z[i - 1] + l1 / 2);

            double k3 = h * f1(x[i - 1] + h / 2, y[i - 1] + k2 / 2, z[i - 1] + l2 / 2);
            double l3 = h * f2(x[i - 1] + h / 2, y[i - 1] + k2 / 2, z[i - 1] + l2 / 2);

            double k4 = h * f1(x[i - 1] + h, y[i - 1] + k3, z[i - 1] + l3);
            double l4 = h * f2(x[i - 1] + h, y[i - 1] + k3, z[i - 1] + l3);


            y[i] = y[i - 1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6;
            z[i] = z[i - 1] + (l1 + 2 * l2 + 2 * l3 + l4) / 6;
            cout << x[i] << " " << y[i] << " " << z[i] << endl;

            /*double k2 = (f(x[i - 1] + h / 2, y[i - 1] + (h / 2 * k1)));
            double k3 = f(x[i - 1] + h, y[i - 1] - (h * k1) + (2 * h * k2));
            y[i] = y[i-1]+ h/6*(k1 + 4*k2 + k3);
            cout << k1 << " " << k2 << " " << k3 << " "<<y[i] << endl;
            del[i] = 0;
            */
        }
        else
        {
            z[i] = z[i - 1] + h / 12 * (23 * f2(x[i - 1], y[i - 1], z[i - 1]) - 16 * f2(x[i - 2], y[i - 2], z[i - 2]) + 5 * f2(x[i - 3], y[i - 3], z[i - 3]));
            y[i] = y[i - 1] + h / 12 * (23 * f1(x[i - 1], y[i - 1], z[i - 1]) - 16 * f1(x[i - 2], y[i - 2], z[i - 2]) + 5 * f1(x[i - 3], y[i - 3], z[i - 3]));
        }
        file1 << y[i] << endl;
        file2 << z[i] << endl;
        // cout << i << " " << x[i] << " " << y[i] << " " << del[i] << " " << f(x[i], y[i]) << endl;
    };
    file1.close();
    file2.close();
    system("pause");
    return 0;
}
