import os
import sys

from pathlib import Path

sys.path.append(os.environ['PWD'])

from cv_project import CVProject  # noqa: E402


if __name__ == '__main__':
    image_dir = Path(sys.argv[1])
    image_pattern = sys.argv[2]

    detector = CVProject()

    for image_path in image_dir.glob(image_pattern):
        print(detector(str(image_path)))
