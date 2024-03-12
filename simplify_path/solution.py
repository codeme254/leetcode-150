class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        Simplifies an absolute unix path to a canonical path

        Args:
          path: input path
        
        Returns:
          canonical version of the absolute unix path passed in
        """
        if path == "":
            return "/"
        
        canonical_path = "/"
        for i in range(0, len(path)):
            if path[i] == "/":
                if i == len(path)-1:
                    continue
                elif canonical_path[len(canonical_path)-1] == "/":
                    continue
                else:
                    canonical_path += path[i]
            elif path[i] == ".":
                period_count = 0
                for j in range(i, len(path)):
                    if path[j] == ".":
                        period_count += 1
                    else:
                        break
                if period_count <= 2:
                    continue
                else:
                    canonical_path += ("."*period_count)
            else:
                canonical_path += path[i]
        return canonical_path

s = Solution()
print(s.simplifyPath("/home/"))
print(s.simplifyPath("/../"))
print(s.simplifyPath("/.../"))
print(s.simplifyPath("/home//foo/"))