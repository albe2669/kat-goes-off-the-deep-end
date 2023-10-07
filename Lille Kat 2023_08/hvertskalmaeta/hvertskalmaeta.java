import java.util.*;

class hvertskalmaeta {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        String city = s.nextLine();
        Set<String> cities = Set.of("Fjardabyggd", "Mulathing", "Akureyri");
        if (cities.contains(city)) {
            System.out.println("Akureyri");
        } else {
            System.out.println("Reykjavik");  
        }
    }
}
