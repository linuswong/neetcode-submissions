class Solution {
    /**
     * @param {number[]} coins
     * @param {number} amount
     * @return {number}
     */
    coinChange(coins: number[], amount: number): number {
        let dp: number[] = Array(amount + 1).fill(amount+1);
        dp[0] = 0;

        for(let i = 1;i<amount + 1;i++){
            for(let c = 0 ;c<coins.length;c++){
                if(coins[c]<=i){
                    dp[i] = Math.min(dp[i], 1+dp[i-coins[c]])
                }
            }
        }
        return dp[amount] <= amount ? dp[amount]: -1;
    }
        



    //     let res:number = 0;
    //     let resDiv:number = 0;

    //     coins.sort()

    //     let amt = amount;
    //     for(let i = coins.length; i--;i>-1){
    //         let temp:number  = Math.floor(amt/coins[i]);
    //         amt -= (coins[i]*temp);
    //         res += temp;
    //         if (amount % coins[i] == 0){
    //             resDiv = resDiv > amount/coins[i] || resDiv == 0 ?  amount/coins[i]: resDiv;
    //         }
    //         console.log("Temp: "+temp);
    //         console.log("Amount: "+amt);
    //         console.log("coins[i]: "+coins[i]);
    //         console.log("resDiv: "+ resDiv);
    //     }
        
    //     console.log("res: "+res);
    //     if(resDiv!=0){
    //         return amt == 0  ? Math.min(res,resDiv) : -1;
    //     }
    //     return amt == 0  ? res : -1;
    // }
}
