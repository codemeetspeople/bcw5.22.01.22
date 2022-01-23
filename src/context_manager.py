class File:
    def __init__(self, file_path, mode):
        self._path = file_path
        self._mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self._path, self._mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        del self.file
        self.file = None


if __name__ == '__main__':
    with File('out.txt', 'w') as file:
        file.write('very important text...')
