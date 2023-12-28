class Template:
    def __init__(self, template):
        self._value = template
        self._template = template
    
    # populate value of template in place with args without returning value
    def populate(self, **args):
        pass
    
    # return value of template with args filled in, no change to value
    def render(self, **args):
        pass

    # return value of template
    def render(self):
        pass
