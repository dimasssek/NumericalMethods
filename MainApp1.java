package ru.university.one.SimpleIterationMethod;

import java.util.Scanner;

import static java.lang.Math.abs;

public class MainApp1 {
    // private static final double MAX = Math.pow(10, 10);

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

        /*for (int i=0;i<rank;i++) {
        	for (int j=0;j<rank;j++)
        		System.out.print(matrix[i][j]+" ");
        	System.out.print("|" + result[i] + "\n");
        }*/
        for (int i=0;i<rank;i++){
            int j=change(matrix,result, i);
            swap(matrix,result,i, j);
        }

        for (int i=0;i<rank;i++){
            if (!isDiagonalDominance(matrix))
            {
                System.out.println("Матрица не удовлетворяет условию диагонального преобладания");
                System.out.println(toString(matrix,result, rank));
                System.exit(1);
            }
        }


        double [] x=iteration(matrix,result,rank);
        // double[] errors = new double[rank];

        System.out.print(toString(matrix, result, rank));

        System.out.println("\nОтвет:");
        for(int i=0;i<rank; i++)
            System.out.println("x" + (i + 1) + " = " + x[i] + " "+"\n");

        /*System.out.println("Проверка:");
        for (int i = 0; i < rank; i++) {
            double res = 0.0;
            for (int j = 0; j < rank; j++) {
                res += x[j] * matrix[i][j];
            }
            System.out.println("b" + (i + 1) + " = " + res);
            errors[i] = abs(result[i] - res);
        }*/

        double[] errors = errors(matrix, result, rank, x);

        System.out.println("\nВектор погрешностей:");
        for (int i = 0; i < rank; i++)
            System.out.println(errors[i]);

    }

    public static String toString(double matrix[][], double result[], int rank) {
        String s = "";
        for (int i=0;i<rank;i++) {
            for (int j=0;j<rank;j++)
                s += matrix[i][j]+" ";
            s += "|" + result[i] + "\n";
        }
        return s;
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
                    if (i!=j)
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
        }while(true); //maxInArray(errors(a, y, n, res)) < MAX)
        return res;
    }

    public static double[] errors(double matrix[][], double result[], int rank, double[] answer) {
        double[] errors = new double[rank];
        for (int i = 0; i < rank; i++) {
            double res = 0.0;
            for (int j = 0; j < rank; j++) {
                res += answer[j] * matrix[i][j];
            }
            System.out.println("b" + (i + 1) + " = " + res);
            errors[i] = abs(result[i] - res);
        }
        return errors;
    }

    public static double maxInArray(double[] arr) {
        if(arr == null) {
            return 0;
        }
        double max = arr[0];
        for(int i = 0; i < arr.length; ++i) {
            if(max<arr[i])
                max=arr[i];
        }
        return max;
    }

    public static void swap(double[][] a, double[] b, int i1, int j1)
    {
        if (i1==j1)
            return;
        for (int j=0;j<a.length;j++)
        {
            double temp=a[i1][j];
            a[i1][j]=a[j1][j];
            a[j1][j]=temp;
        }
        double temp=b[i1];
        b[i1]=b[j1];
        b[j1]=temp;
    }

    public static int change(double [][] a, double[] b,int j1){
        for (int i=j1;i<a.length;i++) {
            double sum=0;
            for (int j = 0; j < a.length; j++) {
                if (j!=j1)
                    sum+=abs(a[i][j]);
            }
            if (abs(a[i][j1])>=sum) return i;
        }

        double max=Math.abs(a[j1][j1]);
        for (int i=j1+1;i<a.length;i++)
            if (max<abs(a[i][j1]))
                return i;

        return j1;
    }


public static boolean isDiagonalDominance(double [][] a) {
        for (int i=0;i<a.length;i++) {
            double sum = 0.0;
            for (int j = 0; j < a.length; j++)
                if (j!=i)
                    sum+=a[i][j];
            if (abs(a[i][i]) < sum)
                return false;
        }
        return true;
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
