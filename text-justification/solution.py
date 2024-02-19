from typing import List

class Solution:
    def pad(self, sentence: str, maxWidth: int, is_last: bool):
        """
        Pads a string with empty spaces " "
        Args:
          sentence: the string we want to pad
          maxWidth: the maximum number of characters the sentence can have
          is_last: boolean value indicating whether the sentence is the last
        Returns:
          the padded string
        """
        sentence = sentence.strip()
        if len(sentence) == maxWidth:
            return sentence
        sentence_list = sentence.split(" ")
        spaces_killed = len(sentence_list) - 1
        chars_remaining = maxWidth - len(sentence)
        total_chars_remaining = spaces_killed + chars_remaining

        if is_last:
            return sentence + (chars_remaining * " ")
        
        i = 0
        while total_chars_remaining > 0:
            sentence_list[i] += " "
            i += 1
            if i >= len(sentence_list) - 1:
                i = 0
            total_chars_remaining -= 1
        padded_string = ""
        for sentence in sentence_list:
            padded_string += sentence
        return padded_string
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """
        format text such that each line has exactly 
        maxWidth characters and is fully justified.
        
        Args:
          words: the list of words to be fully justified
          maxWidth: the maximum width per line
        """
        fully_justified = []
        i = 0
        current_sentence = ""
        while i < len(words):
            if len(current_sentence) + len(words[i]) > maxWidth:
                padded_string = self.pad(current_sentence, maxWidth, False)
                fully_justified.append(padded_string)
                current_sentence = ""
            else:
                current_sentence += f'{words[i]} '
                i += 1
        if current_sentence != "":
            fully_justified.append(self.pad(current_sentence, maxWidth, True))
        return fully_justified

s = Solution()
print(s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
print(s.fullJustify(["What","must","be","acknowledgment","shall","be"], 16))
print(s.fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20))
print(s.fullJustify(["Well", "Well", "Well", "Well"], 4))
