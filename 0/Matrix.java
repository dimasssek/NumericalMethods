package ru.university.second.zero;


import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Matrix {
    private double[][] matrix;
    private double[] xVector, startVector;
    private double res = Double.MIN_VALUE;
    private static double EPSILON;
    private final static double DELTA = Math.pow(10, -12);
    private int n;
    public Matrix(String inputPath, double EPSILON) throws NullPointerException {
        try(FileReader inputFile = new FileReader(inputPath)) {
            BufferedReader buffer = new BufferedReader(inputFile);
            String numLine = buffer.readLine();
            String[] numArr = numLine.split(" ");
            int size = numArr.length;
            double[][] matrix = new double[size][size];
            do {
                for ( int i = 0; i < size; i++ ) {
                    for ( int j = 0; j < size; j++ ){
                        matrix[i][j] = Double.parseDouble(numArr[j]);
                    }
                    numLine = buffer.readLine();
                    if ( numLine != null )
                        numArr = numLine.split(" ");
                }
                double tmpVector[] = new double[size];
                for ( int i = 0; i < size; i++ )
                    tmpVector[i] = Double.parseDouble(numArr[i]);
                this.startVector = tmpVector;
            } while ( buffer.ready() );
            this.matrix = matrix;
            this.n = size;
            this.EPSILON = EPSILON;
        }
        catch ( IOException e ){
            System.out.println("Something went wrong with an input file.");
            throw new RuntimeException();
        }
    }
    public double[] lambdaVector(double[] y, double[] x){
        double[] l = new double[n];
        for (int i = 0; i < n; i++) {
            if ( Math.abs(x[i]) > DELTA )
                l[i] = y[i] / x[i];
        }
        return l;
    }
    private boolean checkLambda(double[] l, double[] lPrev){
        for (int i = 0; i < n; i++) {
            if ( Math.abs(l[i] - lPrev[i]) > EPSILON )
                return false;
        }
        return true;
    }
    private double[] matrix_vector(double[][] m, double[] v){ // умножение матрицы на вектор
        double res[] = new double[n];
        for ( int i = 0; i < n; i ++) {
            res[i] = 0;
            for ( int j = 0; j < n; j++ )
                res[i] += m[i][j] * v[j];
        }
        return res;
    }
    private double vectorScalar(double[] v){
        double res = 0;
        for ( int i = 0; i < n; i++ )
            res += v[i] * v[i];
        return res;
    }
    private double[] normDivision(double[] v){
        double[] x = new double[n];
        double norm = Math.sqrt(vectorScalar(startVector));
        if ( Math.abs(norm) < DELTA ){
            System.out.println("Норма вектора равна нулю! Произошло деление на 0!");
            System.exit(0);
        }
        else {
            for (int i = 0; i < n; i++)
                x[i] = v[i] / norm;
        }
        return x;
    }
    private double[] randomVector(){
        double[] x = new double[n];
        for (int i = 0; i < n; i++) {
            x[i] = (Math.random() * 30) - 15; // диапазон от -15 до 15
        }
        return x;
    }
    private void printVector(double[] x){
        System.out.print("[ ");
        for (int i = 0; i < n; i++) {
            System.out.print(x[i] + ", ");
        }
        System.out.print("]");
    }
    private void check(double[] x, double l){
        double[] v1 = matrix_vector(matrix, x);
        double[] v2 = new double[n];
        for (int i = 0; i < n; i++) {
            v2[i] = l*x[i];
        }
        printVector(v1);
        System.out.println();
        printVector(v2);
        double[] v3 = new double[n];
        for (int i = 0; i < n; i++) {
            v3[i] = Math.abs(v1[i] - v2[i]);
        }
        System.out.println();
        printVector(v3);
    }
    public void powerMethod(){
        xVector = normDivision(startVector); // шаг 1
        double[] lPrevVector = randomVector(); // задаю произвольный лямбда(0) вектор
        for ( int k = 1; ; k++ ){
            double[] ykVector = matrix_vector(matrix, xVector);   // шаг 2
            double[] xkVector = normDivision(ykVector);           // шаг 3
            double[] lkVector = lambdaVector(ykVector, xVector);  // шаг 4
            if ( checkLambda(lkVector, lPrevVector) ){            // шаг 5
                for (int i = 0; i < n; i++) {
                    res += lkVector[i];
                }
                res /= n;
                System.out.println("Старшее собственное число: " + res);
                System.out.println("Старший собственный вектор: ");
                printVector(xkVector);
                check(xkVector, res);
                break;
            }
            xVector = xkVector;
            lPrevVector = lkVector;
        }
    }
    /*
    private void printMatrix(){
        for ( int i = 0; i < n; i++ ) {
            for (int j = 0; j < n; j++)
                System.out.print(matrix[i][j] + " ");
            System.out.println();
        }
    }
     */

}
