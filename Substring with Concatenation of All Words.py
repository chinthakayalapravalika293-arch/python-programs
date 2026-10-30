from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        if total_len > len(s):
            return []

        # Required frequency of each word
        target = Counter(words)

        result = []

        # Try each possible starting offset
        for offset in range(word_len):
            left = offset
            right = offset
            current = Counter()

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word not in target:
                    # Invalid word: reset the window
                    current.clear()
                    left = right
                    continue

                current[word] += 1

                # If this word occurs too many times,
                # shrink the window from the left
                while current[word] > target[word]:
                    left_word = s[left:left + word_len]
                    current[left_word] -= 1
                    left += word_len

                # If the window contains all words
                if right - left == total_len:
                    result.append(left)

                    # Move forward to look for another window
                    left_word = s[left:left + word_len]
                    current[left_word] -= 1
                    left += word_len

        return result