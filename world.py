
class World():

    def __init__(self):
        self.objects = []

    def add_object(self, object):
        self.objects.append(object)

    def remove_object(self, object):
        self.objects.remove(object)
        del object

    def extend_objects(self, object_list):
        self.objects.extend(object_list)

world = World()
