import java.util.ArrayList;
import java.util.List;

public class foo2 {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>>[] dp = new List[target + 1];
        
        for (int i = 0; i <= target; i++)
            dp[i] = new ArrayList<>();
        
        dp[0].add(new ArrayList<>());
        
        
        for (int candidate: candidates) {
            for (int j = candidate; j <= target; j++) {                
                for (List<Integer> comb: dp[j - candidate]) {
                    List<Integer> newComb = new ArrayList(comb);
                    newComb.add(candidate);
                    dp[j].add(newComb);
                }                    
            }
        }
        return dp[target];
    }

    public static void main(String[] args){
        var f = new foo2();

        System.out.println(f.combinationSum(new int[]{2,3,6,7}, 7));
     
        System.out.println(f.combinationSum(new int[]{2,3,5}, 8));

        System.out.println(f.combinationSum(new int[]{2}, 1));
    }

}