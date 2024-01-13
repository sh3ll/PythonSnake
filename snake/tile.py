class Tile:
    def __init__(self, tile_size, coord):
        self.x = coord * tile_size
        self.y = coord * tile_size
        self.tile_x = (coord * tile_size) + tile_size
        self.tile_y = (coord * tile_size) + tile_size