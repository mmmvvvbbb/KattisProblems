import java.util.*;

public class Birds {
    public static void main(String[] args){
        Scanner reader = new Scanner(System.in);
        int length = reader.nextInt();
        int seperateL = reader.nextInt();
        ArrayList<Integer> birds = new ArrayList<>();
        birds.add(6 - seperateL);
        birds.add(length - 6 + seperateL);
        int temp = reader.nextInt();
        for(int i = 0; i<temp; i++){
            birds.add(reader.nextInt());
        }
        Collections.sort(birds);
        int high;
        int low = 6 - seperateL;
        int output = 0;
        for(int i : birds){
            high = i;
            while(high - low >= 2 * seperateL){
                output++;
                low += seperateL;
            }
            low = high;
        }
        System.out.println(output);     
    }
}
