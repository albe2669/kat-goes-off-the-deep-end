import java.util.*;

class hradgreining {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        String DNA = s.nextLine();
        
        if (DNA.contains("COV")) {
            System.out.print("Veikur!");
        } else {
            System.out.print("Ekki veikur!");
        }
    }
}
