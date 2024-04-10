from hash_quad import *
import string

class Concordance:

    def __init__(self):
        self.stop_table = None          # hash table for stop words
        self.concordance_table = None   # hash table for concordance

    def load_stop_table(self, filename):
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        try:
            in_file = open(filename, "r")
        except:
            raise FileNotFoundError() # if the file is invalid

        self.stop_table = HashTable(191) # create hash table
        # for each word in each line that's split, insert it into the stop table
        for line in in_file:
            l_split = line.split()
            for word in l_split:
                self.stop_table.insert(word)

        in_file.close() # close the file

    def load_concordance_table(self, filename):
        """ Read words from input text file (filename) and insert them into the concordance hash table, 
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        (The stop words hash table could possibly be None.)
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
        Starting size of hash table should be 191: self.concordance_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        try:
            in_file = open(filename, "r")
        except:
            raise FileNotFoundError()

        self.concordance_table = HashTable(191)
        line_num = 0
        for line in in_file:
            line_num += 1
            temp = line.replace("\'", "") # replaces the ' for an emtpy string
            for character in string.punctuation:
                temp = temp.replace(character, " ")
            split_line = temp.split() # separate the characters by spaces

            # after getting rid of punctuation, we look at the actual words
            for word in split_line:
                word = word.lower() # changing it to lowercase, everything should be the same
                # glosses over word if it is in the stop_table
                if (self.stop_table.in_table(word) is False) and word.isalpha():
                    # if it is already in the table
                    concord = self.concordance_table.get_value(word)
                    # check, if it is already there, add the line number
                    if concord is not None and concord[len(concord) - 1] != line_num:
                        temp = concord + [line_num]
                        self.concordance_table.insert(word, temp)
                    # if it is none, then just add to the table
                    elif concord is None:
                        self.concordance_table.insert(word, [line_num])

        in_file.close()

    def write_concordance(self, filename):
        """ Write the concordance entries to the output file(filename)
        See sample output files for format."""
        try:
            with open(filename, "w") as f:
                # obtains the keys from the made concordance table
                keys = self.concordance_table.get_all_keys()
                skeys = sorted(keys)
                # for each key that is in the sorted list by alphabetical order
                # we are writing into the file per line of the word : numbers in the lines they appear
                for key in skeys:
                    data = self.concordance_table.get_value(key)
                    string = ""
                    for value in data:
                        string += " " + str(value)
                    f.write(key + ":" + string + "\n")
        finally:
            f.close()