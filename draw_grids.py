from images_path import *


def draw_3d_grid(surface, grid_width, grid_height, big_box):
    """
    Draw a 3D grid on the specified surface within a given bounding box.

    Parameters:
    - surface: The pygame surface on which to draw the grid.
    - grid_width: The width of each grid cell.
    - grid_height: The height of each grid cell.
    - big_box: A pygame Rect representing the bounding box for the grid.

    Returns:
    None
    """
    for x in range(big_box.left, big_box.right, grid_width):
        pygame.draw.line(surface, GRID_COLOR_DARK, (x, big_box.top), (x, big_box.bottom))
        pygame.draw.line(surface, GRID_COLOR_LIGHT, (x, big_box.bottom),
                         (min(x + grid_width, big_box.right), big_box.bottom))

    for y in range(big_box.top, big_box.bottom, grid_height):
        pygame.draw.line(surface, GRID_COLOR_DARK, (big_box.left, y), (big_box.right, y))
        pygame.draw.line(surface, GRID_COLOR_LIGHT, (big_box.left, y),
                         (big_box.left, min(y + grid_height, big_box.bottom)))


def snap_to_grid(box, grid_width, grid_height, big_box, default_position):
    snapped_x = round((box.x - big_box.left) / grid_width) * grid_width + big_box.left
    snapped_y = round((box.y - big_box.top) / grid_height) * grid_height + big_box.top
    status = True
    # Check if the snapped position is inside the big box
    if (big_box.left <= snapped_x <= big_box.right - box.width and
            big_box.top <= snapped_y <= big_box.bottom):
        is_same_position = True
        rect_pos = pygame.Rect(snapped_x, snapped_y, box.width, box.height)
        for item_key, item_value in CURRENT_POSITION.items():
            if item_value == (rect_pos[0], rect_pos[1]):
                is_same_position = False
                break
        if is_same_position:
            rect_pos = pygame.Rect(snapped_x, snapped_y, box.width, box.height)
        else:
            rect_pos = pygame.Rect(default_position[0], default_position[1], box.width, box.height)
            status = False
        return rect_pos, status
    else:
        rect_pos = pygame.Rect(default_position[0], default_position[1], box.width, box.height)

        return rect_pos, False
