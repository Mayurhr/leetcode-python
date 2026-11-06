class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        morse_alphabet=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        seen_transformation=set()
        for word in words:
            morse_word=[]
            for char in word:
                index=ord(char)-ord('a')
                morse_word.append(morse_alphabet[index])
            seen_transformation.add("".join(morse_word))
        return len(seen_transformation)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna