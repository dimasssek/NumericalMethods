import static java.lang.Float.NaN;
import static java.lang.Math.*;

public class MainApp3 {
    public static void main(String[] args) {
        double x1 = dichotomy(-6.2, 4.5, 1e-5);
        System.out.println("x = " + x1);
    }


    public static double dfunc(double x) {
        //return 2 * x;
        //return cos(x)-sin(x);
        //return 2*x*cos(x);
        //return 2/x;
        return 2 * x - 4;
    }

    public static double func(double x) {
        //return x * x;
        //return sin(x)+cos(x); //-5, 6
        //return sin(x*x); //-3, 4,
        //return log(x*x); //0; 10
        return (x - 2) * (x - 2); //-6.2, 4,
    }

    public static double dichotomy(double a, double b, double eps) {
        double x0;
        if (func(a) * func(b) > 0) {
            x0 = ddichotomy(-6.2, 4.5, 1e-5);
            if (x0 == NaN)
                System.out.println("Корней нет на интервале");
            return x0;
        }
        x0 = (a + b) / 2;
        while (abs(a - b) > eps) {
            if (func(a) * func(x0) > 0)
                a = x0;
            else
                b = x0;
            x0 = (a + b) / 2;
        }
        return x0;
    }


    public static double ddichotomy(double a, double b, double eps) {
        if (dfunc(a) * dfunc(b) > 0) {
            System.out.println("Корней нет на интервале");
            System.exit(1);
        }
        double x0 = (a + b) / 2;
        while (abs(a - b) > eps) {
            if (dfunc(a) * dfunc(x0) > 0)
                a = x0;
            else
                b = x0;
            x0 = (a + b) / 2;
        }
        return x0;
    }
}
