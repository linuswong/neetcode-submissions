class Solution {
    /**
     * @param {number[]} temperatures
     * @return {number[]}
     */
    dailyTemperatures(temperatures: number[]): number[] {
        let res = Array(temperatures.length).fill(0);

        let stack = [];

        for (let i = 0; i<temperatures.length; i++){
            while(stack.length!==0 && temperatures[stack[stack.length-1]] < temperatures[i]){
                let temp = stack.pop();
                res[temp] = i-temp;
                
            }
            stack.push(i);
        }
        
        return res;


        // let res = Array(temperatures.length).fill(0);
        // for(let i = 0; i < temperatures.length-1;i++){
        //     for(let j = i+1; j < temperatures.length;j++){
        //         if(temperatures[i]<temperatures[j]){
        //             res[i] = j-i;
        //             break
        //         }
        // }
        // }
        // return res;

    }
}
