import pygame


def main():
    pix_size = 10
    dim_x = 106
    dim_y = 17
    pos_array = []
    black = (0, 0, 0)
    white = (255, 255, 255)

    pygame.init()

    surf = pygame.display.set_mode(size=(dim_x * pix_size, dim_y * pix_size))
    surf.fill(black)

    running = True
    press_precedent = (0, 0, 0)

    print("Welcome to Tupper's self-referential formula calculator!")
    print("Just draw a shape, pixel by pixel and hit Enter to calculate the k value where this shape is found")
    print("This was inspired from the 2015 Numberphile video 'The Everything Formula'")
    while running:
        if (pygame.mouse.get_pressed()) == (1, 0, 0):
            if press_precedent != pygame.mouse.get_pressed():
                pos = pygame.mouse.get_pos()
                try:
                    pos_array.index((int(pos[0] / 10) * 10, int(pos[1] / 10) * 10))
                except ValueError:
                    pygame.draw.rect(surf, white,
                                     pygame.Rect((int(pos[0] / 10) * 10, int(pos[1] / 10) * 10), (pix_size, pix_size)))
                    pos_array.append((int(pos[0] / 10) * 10, int(pos[1] / 10) * 10))
                else:
                    pygame.draw.rect(surf, black,
                                     pygame.Rect((int(pos[0] / 10) * 10, int(pos[1] / 10) * 10), (pix_size, pix_size)))
                    pos_array.remove((int(pos[0] / 10) * 10, int(pos[1] / 10) * 10))

        press_precedent = pygame.mouse.get_pressed()

        if pygame.key.get_pressed()[13]:
            print("Calcul de la valeur k")

            bin_list = list(dim_x * dim_y * '0')

            k = 0
            for coord in pos_array:
                bin_list[int(dim_y * abs((int(coord[0] / 10)) - dim_x + 1) + (int(coord[1]) / 10))] = '1'
            bin_list.reverse()
            k = int("".join(bin_list), 2)
            k *= dim_y
            print(k)
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()


if __name__ == "__main__":
    main()
