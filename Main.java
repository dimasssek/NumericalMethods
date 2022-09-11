import java.util.Scanner;

class Main {
    public static void main(String[] args) {

        /* Ввод данных */

        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int m = s.nextInt();
        double[][] A = new double[100][100];
        double[] b = new double[100];
        for (int i = 0; i < n; i++) {
            A[i] = new double[100];
            for (int j = 0; j < m; j++) {
                A[i][j] = s.nextDouble();
            }
            b[i] = s.nextDouble();
        };
        double ans = b[0];

        /* Метод Гаусса */

        int N  = n;
        for (int p = 0; p < N; p++) {

            int max = p;
            for (int i = p + 1; i < N; i++) {
                if (Math.abs(A[i][p]) > Math.abs(A[max][p])) {
                    max = i;
                }
            }
            double[] temp = A[p];
            A[p] = A[max];
            A[max] = temp;
            double t = b[p];
            b[p] = b[max];
            b[max] = t;

            if (Math.abs(A[p][p]) <= 1e-10) {
                System.out.println("Система не совместна");
                return;
            }

            for (int i = p + 1; i < N; i++) {
                double alpha = A[i][p] / A[p][p];
                b[i] -= alpha * b[p];
                for (int j = p; j < N; j++) {
                    A[i][j] -= alpha * A[p][j];
                }
            }
        }

        // Обратный проход

        double[] x = new double[N];
        for (int i = N - 1; i >= 0; i--) {
            double sum = 0.0;
            for (int j = i + 1; j < N; j++) {
                sum += A[i][j] * x[j];
            }
            x[i] = (b[i] - sum) / A[i][i];
        }

        /* Вывод результатов */

        if (n < m) {
            System.out.print("Бесконечно много решений");
        } else {
            for (int i = 0; i < N; i++) {
                System.out.println(x[i]);
            }
            double p=0.0;
            for (int i=0;i<n;i++)
            {
                p+=A[0][i]*x[i];
            }
            System.out.println("Погрешность составляет: " + (ans-p) + " ");
        }

    }
}

/*
Examples:
3 2 -5 -1
2 -1 3 13
1 2 -1 9

4 2 1 1
7 8 9 1
9 1 3 2



 */
