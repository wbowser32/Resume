
/**
 *  GalToLit is supposed to give you a table for converting your gallons to liters
 *
 * @author David Bowser
 */
public class GalToLit {
    public static void main(String arg[]) {
     double gallons, liters;
     int counter;
     
     counter = 0;
     
     for(gallons = 1; gallons <=100; gallons++) {
     liters = gallons * 3.7854; //Converstions
     System.out.println(gallons + " gallons is " +liters + " liters.");
    
    
    counter++;
    if(counter == 10){
     System.out.println();
     counter = 0; //Reset Line Counter
    
    } 
}
}
}
