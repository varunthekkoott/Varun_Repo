import sys
import pygame
from tiles import Tile
from settings import tile_size, screen_width, player_speed, player_gravity
from player import Player
from sys import exit

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)

        self.world_shift = 0

    def setup_level(self, layout):
        self.player = pygame.sprite.GroupSingle()
        self.tiles = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size

                if (row_index == (len(layout) - 1)) and cell == " ":
                    tile = Tile((x, y), tile_size, "Waves")
                    self.tiles.add(tile)

                if cell == "X":
                    # Finding the positions of the Following Cells
                    top = ((row_index - 1, col_index) if row_index != 0 else (row_index, col_index))
                    bottom = ((row_index + 1, col_index) if row_index != (len(layout) - 1) else (row_index, col_index))
                    left = ((row_index, col_index - 1) if col_index != 0 else (row_index, col_index))
                    right = ((row_index, col_index + 1) if col_index != len(row) - 1 else (row_index, col_index))

                    # Checking Whether They are Empty
                    if layout[top[0]][top[1]] == " ":
                        top = True

                    else:
                        top = False

                    if layout[bottom[0]][bottom[1]] == " ":
                        bottom = True

                    else:
                        bottom = False

                    if layout[left[0]][left[1]] == " ":
                        left = True

                    else:
                        left = False

                    if layout[right[0]][right[1]] == " ":
                        right = True

                    else:
                        right = False

                    # Plaing Soil in Last Row
                    if (row_index == (len(layout) - 1)):
                        tile = Tile((x, y), tile_size, "Soil")
                        self.tiles.add(tile)
                        continue

                    # Placing the appropriate Tile
                    if top and left and not (bottom or right):
                        tile = Tile((x, y), tile_size, "LGrass")
                    elif top and right and not (bottom or left):
                        tile = Tile((x, y), tile_size, "RGrass")
                    elif bottom and not top and not left and not right:
                        tile = Tile((x, y), tile_size, "BSoil")
                    elif left and not top and not bottom and not right:
                        tile = Tile((x, y), tile_size, "LSoil")
                    elif right and not top and not bottom and not left:
                        tile = Tile((x, y), tile_size, "RSoil")
                    elif top and bottom and not left and not right:
                        tile = Tile((x, y), tile_size, "IslandM")
                    elif top and bottom and left and not right:
                        tile = Tile((x, y), tile_size, "IslandL")
                    elif top and bottom and not left and right:
                        tile = Tile((x, y), tile_size, "IslandR")
                    elif not top and not left and right and bottom:
                        tile = Tile((x, y), tile_size, "BRSoil")
                    elif not top and left and not right and bottom:
                        tile = Tile((x, y), tile_size, "LRSoil")
                    elif (top and not (left and right and bottom)):
                        tile = Tile((x, y), tile_size, "Grass")
                    elif top and bottom and left and right:
                        tile = Tile((x, y), tile_size, "Grass")
                    else:
                        tile = Tile((x, y), tile_size, "Soil")

                    self.tiles.add(tile)

                elif cell == "P":
                    self.player.add(Player((x, y - 10)))

    def scroll_x(self):

        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < int(screen_width / 5) and direction_x < 0:
            self.world_shift = player_speed
            player.speed = 0
        elif player_x > int(screen_width / 5) * 4 and direction_x > 0:
            self.world_shift = -(player_speed)
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = player_speed

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y >= 0:
                    if sprite.type == "Waves":
                        pygame.quit()
                        sys.exit()

                    else:
                        player.rect.bottom = sprite.rect.top
                        player.direction.y = 0
                        player.current_double_jumps = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
            else:
                player.gravity = player_gravity

    def run(self, space_key):
        # Tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw((self.display_surface))
        self.scroll_x()
        # Player
        self.player.draw((self.display_surface))
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.sprite.update(space_key)
