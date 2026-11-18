class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        boolean[][] visited = new boolean[grid.length][grid[0].length];
        
        int max = 0;

        for(int i = 0;i < grid.length;i++){
            for(int j = 0; j < grid[0].length;j++){
                if(grid[i][j] == 1 && !visited[i][j]){
                    visited[i][j] = true;
                    max = Math.max(dfs(grid,i,j,visited),max);
                }

            }
        }
        return max;
    }
    private int dfs(int[][] grid, int row, int col, boolean[][]visited){
        int r;
        int c;
        int[][] directions = {{1,0},{-1,0},{0,1},{0,-1}};
        int area = 1;
        for(int[] d: directions){
            r = row +d[0];
            c = col + d[1];

            if(
                r<grid.length && 
                r>=0 &&
                c<grid[0].length &&
                c>=0 &&
                grid[r][c] == 1 &&
                !visited[r][c]
            ){
                visited[r][c] = true;
                area+= dfs(grid,r,c,visited);
            }
        }

        return area;
    }
}
