import zipfile

def archive_extract(archive_path, dest_dir):
    with zipfile.ZipFile(archive_path, 'r') as extract:
        extract.extractall(dest_dir)


if __name__ == "__main__":
    archive_extract("compressed.zip", "../files/extracted")