import java.util.*;

public class Cups {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        String s = in.next();
        int pos = 1;
        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == 'A'){
                if(pos == 1) pos = 2;
                else if(pos == 2) pos = 1;
            } else if(s.charAt(i) == 'B') {
                if(pos == 2) pos = 3;
                else if(pos == 3) pos = 2;
            } else {
                if(pos == 1) pos = 3;
                else if(pos == 3) pos = 1;
            }
        }
        System.out.println(pos);

    }
}
