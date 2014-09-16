import shutil
import os
import zipfile
import sys

class ZipReplace:
    '''unzipping the compressed file
        zipping up the new files
        find and replace
    '''
    def __init__(self, filename, search_string, replace_string):
        self.filename = filename
        self.search_string = search_string
        self.replace_string = replace_string
        self.temp_directory = "unzipped-%s" % filename

    def unzip_replace_zip(self):
        'the manager method'
        self.unzip()
        self.find_replace()
        self.zip()
        print 'All done!'

    def unzip(self):
        if not self.temp_directory:
            os.mkdir(self.temp_directory)

        file_handler = open(self.filename, 'rb')
        zip = zipfile.ZipFile(file_handler)
        try:
            zip.extractall(self.temp_directory)
        finally:
            file_handler.close()
        #try:
         #   zip.extractall(self.temp_directory)
        #finally:
         #   zip.close()

    def find_replace(self):
        for filename in os.listdir(self.temp_directory):
            with open(self.__full_filename(filename)) as file:
                contents = file.read()
                contents = contents.replace(
                    self.search_string, self.replace_string)
                with open(
                        self.__full_filename(filename), "w") as file:
                    file.write(contents)

    def zip(self):
        file = zipfile.ZipFile(self.filename, 'w')
        for filename in os.listdir(self.temp_directory):
            file.write(
                self.__full_filename(filename), filename)
        shutil.rmtree(self.temp_directory)

    def __full_filename(self, filename):
           return os.path.join(self.temp_directory, filename)


if __name__ == '__main__':
    user_input_from_cl = sys.argv[1:4]
    ZipReplace(*user_input_from_cl).unzip_replace_zip()
    zipR = ZipReplace(*user_input_from_cl)
