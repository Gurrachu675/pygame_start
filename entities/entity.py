class EntityComponent:
    def_init_(self):
        self.components = {}

def add_component(self, component):
    self.components[type(component)] = component 
