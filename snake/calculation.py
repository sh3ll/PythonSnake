class Window:

    rows = 25
    cols = 25
    tile_size = 25

    def size(size, number):
        return size * number
    
    def windowcenter(screen, window):
        return int((screen / 2) - (window / 2))