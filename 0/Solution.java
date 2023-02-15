package ru.university.second.zero;

import java.util.Scanner;

public class Solution {
    private static String inputPath = "D:\\IntelliJ_IDEA_Projects\\Chislaki\\ZeroProject\\src\\ru\\university\\second\\zero\\inputFile.txt";
    public static void main(String[] args) {
        System.out.println("Введите приближение: ");
        Scanner sc = new Scanner(System.in);
        double eps = sc.nextDouble();
        Matrix test = new Matrix(inputPath, eps);
        test.powerMethod();
    }
}
