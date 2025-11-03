import java.util.Scanner;
public class prime {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        // int [] arr={1,2,3,4,5,6,7};
        // for(int i=0;i<arr.length;i++){
        //     System.out.println(arr[i]);
        // }
        int [][] arr2= new int[3][4];
        for(int i=0;i<arr2.length;i++){
            for(int j=0;j<arr2[i].length;j++){
                arr2[i][j]=in.nextInt();
            }
        }
        for(int k=0;k<arr2.length;k++){
            for(int h=0;h<arr2[k].length;h++){
                System.out.print(arr2[k][h]+" ");
            }
            System.out.println();
        }
    
       
    }
}
