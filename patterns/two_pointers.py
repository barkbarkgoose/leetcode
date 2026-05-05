from typing import List

def find_all_removable_indices(s1, s2) -> List:
    """
    Given two strings s1 and s2, find all indices in s1 whose removal
    would still allow s2 to remain a subsequence of the resulting string.

    Problem Analysis:
    -----------------
    - A "subsequence" means characters must appear in order (not necessarily contiguously)
    - We need to find which characters in s1 are "flexible" - i.e., removable
      without breaking the subsequence relationship with s2

    Example:
        s1 = 'aabbbcd'
        s2 = 'aabbcd'

        s2 is a subsequence of s1 (we can match 'a', 'a', 'b', 'b', 'c', 'd')
        The three 'b's at indices 2, 3, 4 are redundant - we only need one
        Any of these indices can be removed and s2 would still be a subsequence

    Pattern Recognition:
    -------------------
    This is a "subsequence validation" problem. The key insight is that
    an index i is NOT removable if it is the ONLY way to match some character
    in s2. If there are multiple possible matches for a given character,
    the extras are removable.

    Approach:
    ---------
    For each position i in s1, test if s2 is still a subsequence when s1[i]
    is removed. This is a brute-force check but is O(n*m) per position,
    giving O(n^2 * m) total - acceptable for small strings.

    A more sophisticated approach would use forward/backward passes to find
    "mandatory" positions, but the brute-force is clearer and correct.

    Args:
        s1: The longer string (potentially with removable characters)
        s2: The target string that should remain as a subsequence

    Returns:
        List of indices in s1 that can be removed while keeping s2 as subsequence
    """
    n, m = len(s1), len(s2)

    def is_subsequence(sub_s1, sub_s2):
        """
        Check if sub_s2 is a subsequence of sub_s1.

        Common Pattern: Two-pointer subsequence check
        - Use one pointer for each string
        - Advance through s1 looking for matches to s2
        - If we exhaust s2, it's a subsequence; if we exhaust s1 first, it's not

        This is like keeping a finger on one item in a list and scanning for it in the next list, once it's found you move on to the next item in the 1st list and resume scanning the 2nd list from where you found the last match

        We couldn't just compare strings because we explicitly are just checking that s2 exists of characters in s1, in the order they come in but not necessarily all of them at once.
        """
        j = 0
        for i in range(len(sub_s1)):
            if j < len(sub_s2) and sub_s1[i] == sub_s2[j]:
                j += 1
                if j == len(sub_s2):  # Early exit: all chars matched
                    break

        return j == len(sub_s2)

    removables = []
    for i in range(n):
        # Construct new string with index i removed: s1[:i] + s1[i+1:]
        # Check if s2 is still a subsequence of this shortened string
        if is_subsequence(s2, s1[:i] + s1[i+1:]):
            removables.append(i)

    return removables

# ======================================================================
def main(s1_in, s2_in):
    print(find_all_removable_indices(s1_in, s2_in)) # [2, 3, 4]

if __name__ == '__main__':
    s1 = 'aabbbcd'
    s2 = 'aabbcd'

    main(s1, s2)