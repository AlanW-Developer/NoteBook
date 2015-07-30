# Little Notebook

class Note:
    """ A Note """

    note_number = 1
    note_count = 0
    search_count = 0

    def __init__(self, title="", memo="", id="", tag=""):
        """ initial attributes of the note"""
        self.title = title
        self.memo = memo
        self.id = id
        self.number= Note.note_number
        self.tag = tag
        Note.note_number += 1
        self.file = open(self.title+".txt","w")
        a = self.file.write(self.title + "\n\n" + self.memo)
        self.file.close()


    def __str__(self):
        """ gives string of initial atrributes"""
        return self.memo

    def modify_memo(self):
        """modifies a memo"""
        a = False
        while not a:
            i = input("Modify a memo. Enter 'a' for append"
                      ", 'r' for rewrite or 'e' for exit.\n> ").lower()
            if i == 'a':
                ammend = input("Enter Memo additions:\n> ")
                self.file = open(self.title+".txt", mode = "a")
                a = self.file.write(ammend)
                self.file.close()
                self.memo += "\n" + k
                print("Your memo has been updated")
                a = True

            elif i =='r':
                rewrite = input("Enter new Memo:\n>")
                self.file = open(self.title+".txt", mode = "w")
                a = self.file.write(rewrite)
                self.file.close()
                self.memo = rewrite
                print("Your memo has been updated")
                a = True

            elif i =='e':
                a = True

            else:
                print("That is not a valid option")

    def modify_tag(self, new_tag=""):
        """modifies a tag"""
        new_tag = input(str("Type in the new tag that you would like\n>"))
        print("Your tag has been updated from: \"{0}\""
              " to \"{1}\"".format(i, self.tag))
        self.tag = new_tag

    def show_note(self):
        print("Memo:{0}\t{1}".format(self.memo, self.id))

    def search_note(self, a):
        if a in self.memo:
            print("{0}\n"
                  "note no. {1}".format(self.memo, self.number))
            Note.search_count += 1  # used to track the number of successful searches
        else:
            return None


class NoteBook:
    """The Notebook"""

    def __init__(self):
        self.note_book = []

    def __str__(self):
        return "Your notebook has {0} notes".format(len(self.note_book))

    def add_note(self, *args):
            self.note_book.extend(args)

    def show_notes(self):
        for note in self.note_book:
            print(note)

    def search(self, question ="What would you like to search? "):
        i = input(question)
        self.count = 0
        for note in self.note_book:
            note.search_note(i)
        print(Note.search_count)
        if note.count == 0:
            print("0 results found")
        Note.search_count = 0   # resets the search count to 0


		
		
# Testing code for the classes and functions
"""
n1 = Note(title="day1", memo= "The first day I had learnt how to print \"Hello World\"")
n2 = Note(title="day2", memo="The second day I learnt to code how to open and close files")
n3 = Note(title="day3", memo="Today I had learnt how to incorporate the search function into my program")
notebook1 = NoteBook()
notebook1.add_note(n1, n2, n3)
n1.modify_memo()
"""