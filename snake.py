import consts


class Snake:

    dx = {'UP': 0, 'DOWN': 0, 'LEFT': -1, 'RIGHT': 1}
    dy = {'UP': -1, 'DOWN': 1, 'LEFT': 0, 'RIGHT': 0}

    def __init__(self, keys, game, pos, color, direction):
        self.keys = keys
        self.cells = [pos]
        self.game = game
        self.game.add_snake(self)
        self.color = color
        self.direction = direction
        game.get_cell(pos).set_color(color)

    def get_head(self):
        return self.cells[-1]

    def val(self, x):
        if x < 0:
            x += self.game.size

        if x >= self.game.size:
            x -= self.game.size

        return x

    def next_move(self):
        head = self.get_head()

        next_x = self.val(head[0] + self.dx[self.direction])
        next_y = self.val(head[1] + self.dy[self.direction])
        next_head = self.game.get_cell((next_x, next_y))

        if next_head.color == consts.fruit_color:
            self.cells.append((next_x, next_y))
            self.game.get_cell(self.get_head()).set_color(self.color)

        elif next_head.color == consts.back_color:
            last_cell = self.cells[0]
            self.game.get_cell(last_cell).set_color(consts.back_color)
            self.cells.remove(last_cell)
            self.cells.append((next_x, next_y))
            self.game.get_cell(self.get_head()).set_color(self.color)
        else:
            self.game.kill(self)




    def handle(self, keys):
        for key in keys:
            if key in self.keys:
                if (self.direction in ["UP", "DOWN"]) and (self.keys[key] in ["LEFT", "RIGHT"]):
                    self.direction = self.keys[key]
                elif (self.direction in ["LEFT", "RIGHT"]) and (self.keys[key] in ["UP", "DOWN"]):
                    self.direction = self.keys[key]

