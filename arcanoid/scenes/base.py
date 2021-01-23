class BaseScene:
    def __init__(self, game):
        self.game = game
        self.objects = []

    def on_activate(self):
        pass

    def process_event(self, event):
        for current_object in self.objects:
            current_object.process_event(event)

    def process_logic(self):
        for current_object in self.objects:
            current_object.process_logic()

    def process_draw(self):
        for current_object in self.objects:
            current_object.process_draw()

    def on_deactivate(self):
        pass
