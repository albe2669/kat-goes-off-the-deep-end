import java.util.*;

class MessyList {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int elements = s.nextInt();
         
        ArrayList<Integer> liste = new ArrayList<>(elements);
 
        for(int i = 0; i < elements; i++){
            liste.add(s.nextInt());
        }
        
        
        ArrayList<Integer> liste2 = new ArrayList<>(liste);
        liste2.sort(null);
        
        int fejl = 0;
        for(int i = 0; i < liste.size(); i++) {
            if (liste.get(i) != liste2.get(i)) {
                fejl = fejl + 1;
            }
        }
        System.out.println(fejl);
    }
}
