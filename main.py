import pygame
from constants import *


class Game:
    def __init__(self):
        self._stop = False
        self._window = pygame.display.set_mode((WIDTH, HEIGHT))
        self._units = set()
        self._show_grid = True
        self._scale = 1
        self._cam_shift = [0, 0]
        self._pause = False
        self._make_step = False

        pygame.display.set_caption(CAPTION)

    def _draw_grid(self):
        for x in range(1, int(WIDTH / CELL_SIZE / self._scale) + 1):
            pygame.draw.line(
                self._window,
                GRID_COLOR,
                (x * CELL_SIZE * self._scale, 0),
                (x * CELL_SIZE * self._scale, HEIGHT),
                1
            )

        for y in range(1, int(HEIGHT / CELL_SIZE / self._scale) + 1):
            pygame.draw.line(
                self._window,
                GRID_COLOR,
                (0, y * CELL_SIZE * self._scale),
                (WIDTH, y * CELL_SIZE * self._scale),
                1
            )

    def _draw_units(self):
        for unit in self._units:
            pygame.draw.rect(
                self._window,
                UNIT_COLOR,
                [
                    unit[0] * CELL_SIZE * self._scale + self._cam_shift[0] * CELL_SIZE * self._scale,
                    unit[1] * CELL_SIZE * self._scale + self._cam_shift[1] * CELL_SIZE * self._scale,
                    CELL_SIZE * self._scale,
                    CELL_SIZE * self._scale
                ]
            )

    def _draw(self):
        self._window.fill((50, 50, 50))

        self._draw_units()

        if self._show_grid and not self._scale < 0.3:
            self._draw_grid()

        pygame.display.update()

    def _get_number_of_neighbors(self, position: tuple[int, int]) -> int:
        neighbors = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                if x == 0 and y == 0:
                    continue
                if (position[0] + x, position[1] + y) in self._units:
                    neighbors += 1
        return neighbors

    def _get_empty_cells_near(self, position: tuple[int, int]) -> set:
        empties = set()
        for x in range(-1, 2):
            for y in range(-1, 2):
                if x == 0 and y == 0:
                    continue

                intended_position = x + position[0], y + position[1]

                if intended_position in self._units:
                    continue

                empties.add(intended_position)

        return empties

    def _update_units_state(self):
        print("step")
        to_add = set()
        to_remove = set()

        for unit in self._units:
            num_of_neighbors = self._get_number_of_neighbors(unit)

            if num_of_neighbors < 2 or num_of_neighbors > 3:
                to_remove.add(unit)

            empties = self._get_empty_cells_near(unit)

            for empty in empties:
                if empty in to_add:
                    continue
                if self._get_number_of_neighbors(empty) == 3:
                    to_add.add(empty)

        for unit in to_remove:
            self._units.remove(unit)

        for unit in to_add:
            self._units.add(unit)

        self._make_step = False

    def _update(self):
        self._handle_events()

        if not self._pause or self._make_step:
            self._update_units_state()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._stop = True

            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_g:
                        self._show_grid = not self._show_grid
                    case pygame.K_UP:
                        self._cam_shift[1] += 1
                    case pygame.K_DOWN:
                        self._cam_shift[1] -= 1
                    case pygame.K_LEFT:
                        self._cam_shift[0] += 1
                    case pygame.K_RIGHT:
                        self._cam_shift[0] -= 1
                    case pygame.K_SPACE:
                        self._pause = not self._pause

                    case pygame.K_e:
                        self._make_step = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    self._scale += 0.1
                elif event.button == 5:
                    self._scale -= 0.1
                elif event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    unit_pos = (
                        mouse_pos[0] // (CELL_SIZE * self._scale),
                        mouse_pos[1] // (CELL_SIZE * self._scale)
                    )

                    if unit_pos not in self._units:
                        self._units.add(unit_pos)
                    else:
                        self._units.remove(unit_pos)

    def run(self):
        while not self._stop:
            self._update()
            self._draw()


if __name__ == '__main__':
    game = Game()
    game.run()
