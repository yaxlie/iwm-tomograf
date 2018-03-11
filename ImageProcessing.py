class Pixel:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        pass

class PProcessing:
    def __init__(self):
        pass

    # Rysowanie odcinka algorytmem Bresenhama
    def bresenhamLine(self, x1, y1, x2, y2):
        line = []

        # zmienne pomocnicze
        # int d, dx, dy, ai, bi, xi, yi;
        # int x = x1, y = y1;

        x = x1
        y = y1

        # ustalenie kierunku rysowania
        if (x1 < x2):
            xi = 1
            dx = x2 - x1
        else:
            xi = -1
            dx = x1 - x2

        # ustalenie kierunku rysowania
        if (y1 < y2):
            yi = 1
            dy = y2 - y1
        else:
            yi = -1
            dy = y1 - y2

        # pierwszy piksel
        # --------glVertex2i(x, y)
        line.append(Pixel(x, y))

        # oś wiodąca OX
        if (dx > dy):
            ai = (dy - dx) * 2;
            bi = dy * 2;
            d = bi - dx;
            # pętla po kolejnych x
            while (x != x2):
                # test współczynnika
                if (d >= 0):
                    x += xi
                    y += yi
                    d += ai
                else:
                    d += bi
                    x += xi
                    # --------glVertex2i(x, y)
                line.append(Pixel(x, y))

            # oś wiodąca OY
        else:
            ai = (dx - dy) * 2
            bi = dx * 2
            d = bi - dy
            # pętla kolejnych y
            while (y != y2):
                # test współczynnika
                if (d >= 0):
                    x += xi
                    y += yi
                    d += ai
                else:
                    d += bi
                    y += yi
                    # --------glVertex2i(x, y)
                line.append(Pixel(x, y))
        return  line