
import java.util.*;

public class Hotel {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int a = in.nextInt();
        int b = in.nextInt();
        int[] taken = new int[a];
        if(a == b){
            System.out.print("too late");
            return;
        }else{
            for(int i = 0; i < b; i++){
                taken[in.nextInt() - 1] = 1;
            }   
            for(int i = 0; i < a; i++){
                if(taken[i] == 0){
                    System.out.print(i+1);
                    return;
                }
            }
        }
    }
}
