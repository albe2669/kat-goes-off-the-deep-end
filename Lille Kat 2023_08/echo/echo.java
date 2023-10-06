import java.util.Scanner;

class echo {
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        String word = s.next();
        int i = 0;
        
        while( i < 3) {
            System.out.print(word + " ");
            i = i + 1;
        }   
    }
}
