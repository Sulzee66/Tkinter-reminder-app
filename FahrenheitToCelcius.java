import java.util.Scanner;

public class FahrenheitToCelcius {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Fahrenheit to celcius(1) or  Celcius to Fahrenheit(2)");   //prompting the user for the type of conversion
        int choice = sc.nextInt();
        
        if (choice == 1) {
            System.out.println("Enter temperature in Fahrenheit:"); //collects the temperature in fahrenheit
            double fahrenheit = sc.nextDouble();
            double celcius = (fahrenheit - 32) * 5/9;//converts the temperature in fahrenheit to celcius
            System.out.println(fahrenheit+" fahrenheit is equal to "+celcius+" celcius");
        } else if (choice == 2) {
            System.out.println("Enter temperature in Celcius:");    ////collects the temperature in celcius
            double celcius = sc.nextDouble();
            double fahrenheit = (celcius * 9/5) + 32;   ////converts the temperature in celcius to fahrenheit
            System.out.println(celcius+" celcius is equal to "+fahrenheit+" fahrenheit");
        } else {
            System.out.println("Invalid choice. Please try again.");
        }
    }
}