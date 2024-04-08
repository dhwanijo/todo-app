import zipfile
import pathlib

def make_archive(filepath, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed_new.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for file in filepath:
            file = pathlib.Path(file)
            archive.write(file, arcname=file.name)

if __name__ == "__main__":
    make_archive(filepath=["bonus.py", "bonus2.1.py"], dest_dir="dest")

