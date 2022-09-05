package ru.chislaki;

import java.util.ArrayList;
import java.util.List;

public class Equation implements Gauss<Double, Equation>{

    private List<Double> equation = new ArrayList<Double>();

    @Override
    public void addEquation(Equation item) {

    }

    @Override
    public void mul(Double coefficient) {

    }

    @Override
    public Double findCoefficient(Double a, Double b) {
        if (a==0.0) return 1.0;
        return -b/a;
    }

    @Override
    public Double at(int index) {
        return equation.get(index);
    }

    @Override
    public int size() {
        return equation.size();
    }

    public List<Double> getEquation() {
        return equation;
    }
}
