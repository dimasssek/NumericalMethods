package ru.university.one.ReflectionMethod;

import java.util.Scanner;

import static java.lang.Math.abs;

public class MainApp1 {
    public static void main(String[] args) {

        System.out.println("Введите размерность матрицы коэффициентов:");
        Scanner sc = new Scanner(System.in);
        int rank = sc.nextInt();
        double[][] matrix = new double[rank][rank];
        double[] result = new double[rank];

        System.out.println("Введите матрицу коэффициентов:");
        for (int i = 0; i < rank; i++)
            for (int j = 0; j < rank; j++) {
                matrix[i][j] = sc.nextDouble();
            }

        System.out.println("Введите столбец свободных членов:");
        for (int k = 0; k < rank; k++) {
            result[k] = sc.nextDouble();
        }

        double [] x=iteration(matrix,result,rank);
        double[] errors = new double[rank];

        System.out.println("\nОтвет:");
        for(int i=0;i<rank; i++)
            System.out.println("x" + (i + 1) + " = " + x[i] + " ");

        System.out.println("Проверка:");
        for (int i = 0; i < rank; i++) {
            double res = 0.0;
            for (int j = 0; j < rank; j++) {
                res += x[j] * matrix[i][j];
            }
            System.out.println("b" + (i + 1) + " = " + res);
            errors[i] = abs(result[i] - res);
        }
        System.out.println("\nВектор погрешностей:");
        for (int i = 0; i < rank; i++)
            System.out.println(errors[i]);
    }

    public static double[] iteration(double[][] a, double[] y, int n) {
        double [] res=new double[n];
        for (int i=0;i<n;i++)
            res[i]=y[i]/a[i][i];

        double eps=0.001;
        double[] xn=new double[n];

        do{
            for (int i=0;i<n;i++) {
                xn[i]=y[i]/a[i][i];
                for (int j=0;j<n;j++)
                {
                    if (i==j)
                        continue;
                    else
                        xn[i]-= a[i][j] / a[i][i] * res[j];
                }
            }

            boolean flag=true;
            for (int i=0;i<n-1;i++){
                if (abs(xn[i]-res[i])>eps) {
                    flag=false;
                    break;
                }
            }

            for (int i = 0; i < n; i++) {
                res[i] = xn[i];
            }
            if (flag)
                break;
        }while(true);
        return res;
    }
}

/*
*
32 2 1 3 1
1 8 3 1 3
1 2 16 3 1
1 2 3 56 1
1 2 1 3 32
* 43 14 -3 169 -19


1 -1 3 1
4 -1 5 4
2 -2 4 1
1 -4 5 -1
* 5 4 6 3



4 1 1
1 6 -1
1 2 5
* 9 10 20
* */
