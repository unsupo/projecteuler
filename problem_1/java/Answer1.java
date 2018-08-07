
public class Answer1 {
    public static void main(String[] args) {
        System.out.println(multiples(1000, new int[]{3, 5}));
    }

    public static int multiples(int max, int[] mults) {
        int s = 0;
        for (int i = 1; i < max; i++) {
            boolean isMult = false;
            for (int mu : mults)
                if (i % mu == 0)
                    isMult=true;
            if(isMult)
                s+=i;
        }
        return s;
    }
}