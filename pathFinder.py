import sys
import os

def main(argv):
    """Create a json containing all the relative path of file with ext"""
    if len(argv) <= 1 or argv[0] == 'help':
        print('To search: folderPath objType1 objType2 objType3...')

    path = argv[0]
    result = []
    for root, _, files in os.walk(path):
        for name in files:
            for ext in argv[1:]:
                if name.endswith(ext):
                    name_trim = os.path.splitext(name)[0]
                    relative_directory = os.path.relpath(root, path)
                    relative_file_path = os.path.join(relative_directory, name_trim)
                    result.append('{{ "{0}" , @"{1}" }},'.format(name_trim, relative_file_path))


    target = open("image_path.json", 'w')
    target.truncate()
    target.write("{\n")
    for line in result:
        target.write(line + "\n")
    target.write("}\n")
    target.close()

main(sys.argv[1:])
