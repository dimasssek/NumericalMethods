import static java.lang.Math.*;

public class MainApp3 {
    public static void main(String[] args) {
        double x1 = dichotomy(-4.3, 6.2, 1e-5);
        System.out.println("x = " + x1);
    }



    public static double func(double x) {
        //return x*x-3; -5; 5
        //return sin(x); 3.14; 4
        //return log(x*x);
        return (x-(3/2))*(x-(3/2));
    }

    public static double dichotomy(double a, double b, double eps) {
        if (func(a) * func(b) > 0) {
            if (func(0) == 0 && (a <= 0 && b >= 0))
                return 0;
            System.out.println("Корней нет на интервале");
            System.exit(1);
        }
        double x0 = (a + b) / 2;
        while (abs(a - b) > eps) {
            if (func(a) * func(x0) > 0)
                a = x0;
            else
                b = x0;
            x0 = (a + b) / 2;
        }
        return x0;
    }
}
