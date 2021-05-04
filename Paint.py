from Widgets import *


def display_list(output, painting):
    print("Executed")
    # Clear Screen
    output.blit_background()

    # Draw
    for i in painting.cleaned_list:
        pygame.draw.circle(output.base.window, i[1], i[0], i[2])
    return


def show_cur_canvas(output, painting, file_system):
    img = file_system.get_cur()
    if img is not None:
        painting.clear()
        output.set_bg_canvas(img)
        output.blit_background()
    return


def show_next_canvas(output, painting, file_system):
    img = file_system.get_next()
    if img is not None:
        painting.clear()
        output.set_bg_canvas(img)
        output.blit_background()
    return


def paint_loop(output, painting, file_system, buttons, color_buttons):
    output.blit_background()
    show_cur_canvas(output, painting, file_system)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                full_quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    full_quit()

                if event.key == pygame.K_RETURN:
                    painting.cleanlist()
                    print(painting.cleaned_list)

                if event.key == pygame.K_BACKSPACE:
                    painting.undo_mode = True

            if event.type == pygame.KEYUP:

                if event.key == pygame.K_BACKSPACE:
                    painting.undo_mode = False

                if event.key == pygame.K_s:
                    file_system.save_img(output.paint_canvas)
                    show_next_canvas(output, painting, file_system)

        # Draw Everything
        output.blit_menu()

        for button in buttons:
            button.display_button()

        for color_button in color_buttons:
            color_button.display_color()

        # Update Function
        painting.perform_functions()
        painting.mouse_actions()

        # Delay framerate
        output.base.clock.tick(output.base.FPS)

        # Update Screen
        pygame.display.update()
