"""palindrome_list.py module yesss!!"""
from arraystack import ArrayStack


class Palindrome:
    """Represents Palindrome class."""

    def read_file(self, path):
        """Reads data from file and returns a list with data."""
        read_data = []
        with open(path, 'r') as words_path:
            for line in words_path:
                line = line.split(' ')[0].strip()
                read_data.append(line)
        return read_data

    def find_palindromes(self, read_path, write_file):
        """Finds all palindromes from read_path file, return a list with them
        and writes into file."""
        all_palindromes = []
        words = self.read_file(read_path)

        for word in words:
            palindrome = True
            pal_stack = ArrayStack()

            for ind in range(len(word) // 2):
                pal_stack.push(word[ind])

            for ind in range((len(word) + 1) // 2, len(word)):
                if word[ind] != pal_stack.pop():
                    palindrome = False

            if palindrome:
                if word != '':
                    all_palindromes.append(word)

        self.write_to_file(write_file, all_palindromes)
        return all_palindromes

    def write_to_file(self, write_file: str, data: list):
        """Write all of the data to a file"""
        with open(write_file, 'w') as final_file:
            final_file.write("\n".join(data))
