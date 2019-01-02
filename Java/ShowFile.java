
/**
 * Going to tdisplay a text file.
 * TEST.TXT will be used to show this.
 * 
 * Wayne David Bowser II made this program
 * use java SHoeFIle TEST.TXT in the commpand line
 */
import java.io.*;
public class ShowFile{ 
    public static void main(String args[])
    {
        int i;
        FileInputStream fin;
        //First make sure that the file is specified 
        if(args.length!=1){
            System.out.println("Usage: ShowFile FIle");
            return;
    }
     try{
        fin = new FileInputStream(args[0]);
    } catch (FileNotFoundException exc) {
        System.out.println("File Not Found");
        return;
    }
     try{
    //read bytes until EOF is encountered
    do {
       i= fin.read();
       if(i != -1) System.out.print((char) i);
    } 
    while (i != -1);
    }
    catch(IOException exc){
      System.out.println("Error reading file.");
    }
    finally {
    //close file o the way out of the try block.
     try {
        fin.close();
    }
    catch(IOException exc){
        System.out.println("Error closing file.");
      }
    }
   }
}