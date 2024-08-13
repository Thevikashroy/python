public class query {
    public static void main(String[] args) {
        int[] arr={3,9,100,5,6,-2,3};
        int[] qer={13,5,6,9,3};
        for (int i = 0; i < qer.length; i++) {
            for (int j = 0; j < arr.length; j++) {
                if(arr[j]==qer[i]){
                   System.out.print("true"+" "+arr[i]+"  ");
                }else{
                    System.out.print("false"+" "+arr[i]+"  ");
                }
            }
            System.out.println( 

            );
        }
    }
}
