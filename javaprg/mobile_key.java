import java.util.ArrayList;

public class mobile_key {
    public static void main(String[] args) {
        int[] key = {2,3,4,5,6,7,8,9};
        String[] val={"abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
        String digit="23";
        ArrayList<String> li = get_charValue_from_num_Keypad(val,digit);
        System.out.println(li);
    }
    public static ArrayList<String> get_charValue_from_num_Keypad(String[] str,String digit){
        String[] charval=new String[digit.length()];
        int c=0;
        for(int i=0;i<digit.length();i++){
            charval[c++]=digit.charAt(i)+"";
        }
        for (int i = 0; i < charval.length; i++) {
            for (int j = i+1; j < charval.length; j++) {
               li.add(charval[i])
            }
        }
        ArrayList<String> list = new ArrayList<>();

    }
}
