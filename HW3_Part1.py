import threading
import shutil
from pathlib import Path


images = ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'heic', 'tiff', 'ico', 'webp', 'JPG']
videos = ['mp4', 'avi', 'mov', 'mkv', 'flv', 'wmv', 'webm', '3gp', 'm4v', 'ts', 'ogg']
documents = ['pdf', 'doc', 'docx', 'ppt', 'pptx', 'xls', 'xlsx', 'rtf']
audios = ['mp3', 'wav', 'flac', 'aac', 'ogg', 'wma', 'm4a']
text_documents = ['txt', 'rtf', 'odt',  'md']
archives = ["zip", "gz", "tar", "dmg"]
python_learn = ["ipynb"]

class Way:
    def __init__(self, path):
        self.path = Path(path)

    def recursive_func(self, recursive):

        for i in recursive.iterdir():

            if i.is_dir():
                self.recursive_func(i)
            elif i.is_file():
                if i.suffix[1:].lower() in images:
                    self.image(i)
                elif i.suffix[1:].lower() in videos:
                    self.video(i)
                elif i.suffix[1:].lower() in documents:
                    self.documents(i)
                elif i.suffix[1:].lower() in audios:
                    self.audio(i)
                elif i.suffix[1:].lower() in text_documents:
                    self.text(i)
                elif i.suffix[1:].lower() in archives:
                    self.archive(i)
                elif i.suffix[1:].lower() in python_learn:
                    self.python_files(i)
                else:
                    self.unknown(i)

    def image(self, file):
        image = self.path/'IMAGES'
        image.mkdir(parents=True, exist_ok=True)
        shutil.move(file, image/file.name)

    def video(self, file):
        videos = self.path/'VIDEOS'
        videos.mkdir(parents=True, exist_ok=True)
        shutil.move(file, videos/file.name)

    def documents(self, file):
        document = self.path/"DOCUMENTS"
        document.mkdir(parents=True, exist_ok=True)
        shutil.move(file, document/file.name)

    def audio(self, file):
        audio = self.path/"AUDIOS"
        audio.mkdir(parents=True, exist_ok=True)
        shutil.move(file, audio/file.name)

    def text(self, file):
        texts = self.path/"TEXTS"
        texts.mkdir(parents=True, exist_ok=True)
        shutil.move(file, texts/file.name)

    def unknown(self, files):
        unknowns = self.path/"UNKNOWN"
        unknowns.mkdir(parents=True, exist_ok=True)
        shutil.move(files, unknowns/files.name)

    def archive(self, files):
        archives = self.path/"ARCHIVES"
        archives.mkdir(parents=True, exist_ok=True)
        shutil.move(files, archives/files.name)

    def python_files(self, files):
        pyth = self.path/"PYTHON LEARN"
        pyth.mkdir(parents=True, exist_ok=True)
        shutil.move(files, pyth/files.name)

    def delete_empty_folders_recursive(self):
        for item in self.path.iterdir():
            if item.is_dir():
                subfolder = Way(item)
                subfolder.delete_empty_folders_recursive()
        if not any(self.path.iterdir()):
            try:
                self.path.rmdir()
            except OSError:
                pass

def process_directory(source):
    way = Way(source)
    way.recursive_func(way.path)
    way.delete_empty_folders_recursive()

def main():
    source_paths = ["/Users/artemzhuravlev/Desktop/Домашні завдання GoIT/Home_works_web/HW_WEB_03/Files"]

    threads = []
    for source_path in source_paths:
        source = Path(source_path)
        thread = threading.Thread(target=process_directory, args=(source,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()