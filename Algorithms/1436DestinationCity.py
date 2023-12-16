from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # Solution 1
        """
        cities = {f: t for f, t in paths}
        key = paths[0][0]
        while key in cities:
            key = cities[key]
        return key
        """
        # Solution 2
        cities = {f for f, _ in paths}
        for i in range(len(paths)):
            if paths[i][1] not in cities:
                return paths[i][1]
