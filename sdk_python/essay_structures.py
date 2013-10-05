class essay:
    
    def __init__(self, text):
        self.children = {}
        self.name = "My Essay"
        self.text = text
        self.subcount = 0

    def add_child(self, level, text):
        self.children[self.subcount] = essay_component( level, text )
        self.subcount += 1

    def __str__(self):
        total_string = ""
        for key, value in self.children.items():
            total_string += str( (key, value) )
        return total_string

class essay_component:
    
    def __init__(self, level, text):
        self.text = text
        self.level = level
        self.children = []
        
        if level == 1:
            self.get_sentences()

    def get_sentences(self):
        split_line = self.text.split(".")
        for sentence in split_line:
            self.children.append( essay_component( 2, sentence ) ) 
        print str(self.children)

    def __str__(self):
        total_string = ""
        if len(self.children) > 0:
            for child in self.children:
                total_string += child
        else:
            total_string += self.text
        print total_string
        return total_string
