import pygame


class SurfaceInfo:
    """
    A class to store information about a surface.

    Attributes:
    - image_path (str): The path to the image file.
    - coordinates (Tuple[int, int]): The coordinates to place the image.
    - size (Tuple[int, int]): The size of the image.
    """

    def __init__(self, image_path, coordinates, size):
        self.image_path = image_path
        self.coordinates = coordinates
        self.size = size


def recreate_surface(surface_info):
    """
    Recreate a surface based on the provided SurfaceInfo.

    Parameters:
    - surface_info (SurfaceInfo): Information needed to recreate the surface.

    Returns:
    Tuple[pygame.Surface, pygame.Rect]: A tuple containing the resized surface and its rect object.
    """
    loaded_image = pygame.image.load(surface_info.image_path)
    bg_img_rect = loaded_image.get_rect()
    bg_img_rect.topleft = surface_info.coordinates
    resized_image = pygame.transform.scale(loaded_image, surface_info.size)
    return resized_image, bg_img_rect
