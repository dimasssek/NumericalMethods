package ru.university.one;

import java.util.Scanner;

import static java.lang.Math.abs;

public class MainApp {
    public static void main(String[]args){

        System.out.println("Введите размерность матрицы коэффициентов:");
        Scanner sc=new Scanner(System.in);
        int rank=sc.nextInt();
        double[][] matrix=new double[rank][rank];
        double[] result=new double[rank];
        double[][] matrix2=new double[rank][rank];
        double[] result2=new double[rank];
        System.out.println("Введите матрицу коэффициентов:");
        for(int i=0;i<rank; i++)
            for (int j=0;j<rank;j++) {
                matrix[i][j]=sc.nextDouble();
                matrix2[i][j]=matrix[i][j];
                }

        System.out.println("Введите столбец свободных членов:");
        for (int k=0;k<rank;k++) {
            result[k] = sc.nextDouble();
            result2[k]=result[k];
        }

        for(int i=0;i<rank; i++) {
            if(matrix[i][i]==0) {
            boolean isMatrixCompatible=false;
            for(int j=i+1;j<rank; j++) {
                if(matrix[j][i]!=0) {
                isMatrixCompatible=true;
                for(int k=0;k<rank; k++) {
                    double tempNumber=matrix[i][k];
                    matrix[i][k]=matrix[j][k];
                    matrix[j][k]=tempNumber;
                }
                double t=result[j];
                result[j]=result[i];
                result[i]=t;
                break;
                }
            }
            if(!isMatrixCompatible) {
                System.out.println("Система не совместна!");
                System.exit(0);
            }
            }

            for(int j=i+1;j<rank; j++) {
                double ratio=matrix[j][i]/matrix[i][i];
                result[j]-=result[i]*ratio;
                for(int k=i;k<rank; k++)
                    matrix[j][k]-=ratio*matrix[i][k];
            }
        }
        for(int i=rank-1;i>=0;i--) {
            for(int j=i+1;j<rank; j++)
                result[i]-=result[j]*matrix[i][j];
            result[i]/=matrix[i][i];
        }

        System.out.println("\nОтвет:");
        for(int i=0;i<rank; i++)
            System.out.println("x" + (i + 1) + " = " + result[i] + " ");

        double[] errors=new double[rank];
        System.out.println("Проверка:");
        for(int i=0;i<rank; i++) {
            double res = 0.0;
            for (int j = 0; j < rank; j++) {
                res += result[j] * matrix2[i][j];
            }
                System.out.println("b" + (i + 1)+ " = " + res);
                errors[i] = abs(result2[i] - res);
            }
        System.out.println("\nВектор погрешностей:");
        for(int i=0;i<rank; i++)
            System.out.println(errors[i]);
    }
}

/*
3 2 -5 -1
2 -1 3 13
1 2 -1 9

4 2 1 1
7 8 9 1
9 1 3 2
*/
