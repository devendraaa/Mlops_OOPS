class employe:
    #special method/magic / duder = constructer
    def __init__(self):
        self.id = 123
        self.designation = 'SEO'
        self.salary =  50000 


    def Travel(self, destination):
        print(f"employe is travel to {destination}")
# create a obj or instance of a class
sam = employe()

sam.Travel("kerala")

print(sam.designation)