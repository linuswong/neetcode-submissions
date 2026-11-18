class Solution {
    /**
     * @param {string[]} words
     * @returns {string}
     */
    foreignDictionary(words: string[]): string {
        const adj = new Map<string, Set<string>>();

        // Initialize every unique character
        for (const word of words) {
            for (const c of word) {
                if (!adj.has(c)) {
                    adj.set(c, new Set<string>());
                }
            }
        }

        // Build the directed graph
        for (let i = 0; i < words.length - 1; i++) {
            const w1 = words[i];
            const w2 = words[i + 1];
            const minLen = Math.min(w1.length, w2.length);

            // Invalid prefix ordering
            if (
                w1.length > w2.length &&
                w1.substring(0, minLen) === w2.substring(0, minLen)
            ) {
                return "";
            }

            for (let j = 0; j < minLen; j++) {
                if (w1[j] !== w2[j]) {
                    adj.get(w1[j]).add(w2[j]);
                    break;
                }
            }
        }

        // true = currently visiting, false = fully processed
        const visit = new Map<string, boolean>();
        const res: string[] = [];

        const dfs = (c: string): boolean => {
            if (visit.has(c)) {
                return visit.get(c);
            }

            visit.set(c, true);

            for (const nei of adj.get(c)!) {
                if (dfs(nei)) {
                    return true;
                }
            }

            visit.set(c, false);
            res.push(c);
            return false;
        };

        // Run DFS on every character
        for (const c of adj.keys()) {
            if (dfs(c)) {
                return "";
            }
        }

        res.reverse();
        return res.join("");
    }
}