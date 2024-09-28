import numpy as np
import matplotlib.image as mpimg
from os import getcwd
from pathlib import Path
from sys import argv

name: list[str] = [
    "hero",
    "warrior",
    "priest",
    "mage",
    "martial",
    "merchant",
    "gadabout",
    "thief",
    "sage",
]

direction: list[str] = ["up", "right", "down", "left"]


# Character size is 16x24 pixels
# Sprite Sheet is in 17x9 characters
def read_image(path: Path):
    image: np.ndarray = mpimg.imread(path)
    Path(getcwd()).joinpath("out").mkdir(parents=True, exist_ok=True)
    splited = np.array_split(image, 9)
    for i, img_lane in enumerate(splited):
        (boy_varient, girl_varient) = np.array_split(img_lane, 2, axis=1)
        Path(getcwd()).joinpath("out").joinpath(name[i]).joinpath("boy").mkdir(
            parents=True, exist_ok=True
        )
        Path(getcwd()).joinpath("out").joinpath(name[i]).joinpath("girl").mkdir(
            parents=True, exist_ok=True
        )

        boys = np.array_split(boy_varient, 8, axis=1)
        girls = np.array_split(girl_varient, 8, axis=1)
        current = 0
        for j in range(8):
            if j % 2 == 0:
                current += 1
            mpimg.imsave(
                Path(getcwd())
                .joinpath("out")
                .joinpath(name[i])
                .joinpath("boy")
                .joinpath(f"{direction[current-1]}{((j%2)+1)}.bmp"),
                boys[j],
            )
            mpimg.imsave(
                Path(getcwd())
                .joinpath("out")
                .joinpath(name[i])
                .joinpath("girl")
                .joinpath(f"{direction[current-1]}{((j%2)+1)}.bmp"),
                girls[j],
            )


def main():
    if len(argv) != 2:
        raise Exception("Error (FATAL): Missing Argument")
    location: Path = Path(getcwd()).joinpath(argv[1])
    read_image(location)


if __name__ == "__main__":
    main()
