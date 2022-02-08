# class Game:
#     def __init__(self):
#         self._stop = False
#         self._window = pygame.display.set_mode((WIDTH, HEIGHT))
#         self._clock = pygame.time.Clock()
#
#         pygame.display.set_caption(CAPTION)
#
#     def draw(self):
#         self._window.fill((0, 0, 0))
#         pygame.display.update()
#
#     def update(self):
#         self.handle_events()
#
#     def handle_events(self):
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 self._stop = True
#
#     def run(self):
#
#         while not self._stop:
#             self.update()
#             self.draw()
#             print(self._clock.get_fps())
#             self._clock.tick()
#
#
# if __name__ == '__main__':
#     game = Game()
#     game.run()




# class Grid:
#     def __init__(self):
#         self._scale = 2
#         self._units = set()
#         self._show_grid = True
#
#     def get_number_of_neighbors(self, position: tuple[int, int]):
#         number = 0
#         for x in range(-1, 2):
#             for y in range(-1, 2):
#                 if x == 0 and y == 0:
#                     continue
#                 elif (position[0] + x, position[1] + y) in self._units:
#                     number += 1
#         return number
#
#     def draw(self, window):
#         for y in range(HEIGHT // int(CELL_SIZE // self._scale)):
#             for x in range(WIDTH // int(CELL_SIZE // self._scale)):
#                 if (x, y) in self._units:
#                     pygame.draw.rect(
#                         window,
#                         UNIT_COLOR,
#                         [
#                             x * CELL_SIZE / self._scale, y * CELL_SIZE / self._scale,
#                             CELL_SIZE / self._scale, CELL_SIZE / self._scale
#                         ]
#                     )
#
#         if self._show_grid:
#             for x in range(1, WIDTH // int(CELL_SIZE // self._scale)):
#                 pygame.draw.line(
#                     window,
#                     GRID_COLOR,
#                     (x * CELL_SIZE / self._scale, 0),
#                     (x * CELL_SIZE / self._scale, HEIGHT),
#                     1
#                 )
#
#             for y in range(1, HEIGHT // int(CELL_SIZE // self._scale)):
#                 pygame.draw.line(
#                     window,
#                     GRID_COLOR,
#                     (0, y * CELL_SIZE / self._scale),
#                     (WIDTH, y * CELL_SIZE / self._scale),
#                     1
#                 )
#
#     def update(self):
#         to_remove = set()
#         to_add = set()
#
#         for y in range(HEIGHT // int(CELL_SIZE // self._scale)):
#             for x in range(WIDTH // int(CELL_SIZE // self._scale)):
#                 number_of_neighbors = self.get_number_of_neighbors((x, y))
#
#                 # if (x, y) in self._units:
#                 #     if number_of_neighbors < 2:
#                 #         to_remove.add((x, y))
#                 #     elif number_of_neighbors > 3:
#                 #         to_remove.add((x, y))
#                 # else:
#                 #     if number_of_neighbors == 3:
#                 #         to_add.add((x, y))
#
#         for unit in to_add:
#             self._units.add(unit)
#
#         for unit in to_remove:
#             self._units.remove(unit)
#
#         # self.
#
#         print("-------------------")
#
#     def add_unit(self, unit: tuple[int, int]):
#         self._units.add(unit)
#
#     def add_units(self, units: tuple[tuple[int, int]]):
#         self._units.add(units)
