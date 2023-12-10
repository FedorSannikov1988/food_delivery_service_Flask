from pathlib import Path, \
                    PurePath


class WorkingWithFiles:
    def __init__(self, path_to_file: Path):
        self.__path_to_file = path_to_file

    def delete_file(self) -> None:
        file_path = Path(self.__path_to_file)

        if file_path.exists():
            file_path.unlink()

    @staticmethod
    def generating_path_file_in_folder__user_photos(name_file: str) -> Path:
        return PurePath.joinpath(Path.cwd(), 'user_photos', name_file)
