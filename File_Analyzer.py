#Michael Hart
#5/8/2019

# Create the class called FileAnalyzer.
class FileAnalyzer:
    
    # Create the constructor for FileAnalyzer.
    def __init__(self, filename):
        
        # Set the filename argument as self.filename.
        self.filename = filename
        
        # Open the filename.
        file = open(filename)
        
        # Do readlines on the file.
        file_contents = file.readlines()
        
        
        # Create self.linecount to keep track of the number of lines.
        self.line_count = 0
        
        # Create self.word_count to keep track of the number of words.
        self.word_count = 0
        
        # Iterate through the lines of file_list and add one to self.line_count 
        # for each line.
        for line_index in range(0, len(file_contents)):
            
            self.line_count += 1
            
            # Split the file contents at the current line index into the 
            # variable current_line.
            current_line = file_contents[line_index].split()
            
            self.word_count += len(current_line)
            
        
    # Create the method filename to return the name of the file.    
    def get_filename(self):
        ' returns the file name '
        return self.filename
    
    # Create the method get_number_of_lines to return the number of lines.
    def get_number_of_lines(self):
        ' returns the number of lines in the file '
        return self.line_count
    
    # Create the method get_number_of_words to return the number of words.
    def get_number_of_words(self):
        ' returns the number of words in the file '
        return self.word_count