from pyglet import gl
import shared


class Obstacle(object):
    def __init__(self, x, y, width, height):
        # right now we restrict obstacles to rectangles, eventually extend to polys using triangle fans
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.shape = None

    def add_to_default_batch(self):
        if self.y < 50:
            self.height += self.y-50
            self.y = 50
        if self.width < shared.STEP_SIZE or self.height < shared.STEP_SIZE:
            self.delete()
            return
        self.shape = shared.batch.add(4, gl.GL_QUADS, None,
                                      ('v2f', (self.x, self.y,
                                       self.x + self.width, self.y,
                                       self.x + self.width, self.y + self.height,
                                       self.x, self.y + self.height)))

    def collides_with(self, x, y):
        return self.x+self.width > x > self.x and self.y+self.height > y > self.y

    def delete(self):
        if self.shape is not None:
            self.shape.delete()
        if self in shared.obstacles:
            shared.obstacles.remove(self)