import cat_service
import os
import platform
import subprocess

def main():
    print_header()
    folder = get_or_create_folder()
    print(f'Created {folder}')
    get_pictures(folder)
    print('Got pictures, now displaying')
    show_pictures(folder)

def print_header():
    print('---------------------------')
    print('       LOLCAT APP')
    print('---------------------------')
    print()

def get_or_create_folder():
    base_folder = os.path.abspath(os.path.dirname(__file__))
    folder = 'cat_pics'
    full_path = os.path.join(base_folder, folder)
    print(f'Creating or getting {full_path}')
    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        os.mkdir(full_path)
    return full_path

def get_pictures(folder):
    num_pic = int(input("How many cat pictures do you want? "))
    for i in range(1, num_pic+1):
        name = f'lolcat_{i}'
        print(f'Getting {name}')
        cat_service.get_cat(folder, name)
    
def show_pictures(folder):
    print(f'Opening {platform.system()} file explorer')
    if platform.system() == 'Windows':
        subprocess.call(['explorer', 'folder'])
    elif platform.system() == 'Linux':
        subprocess.call(['xdg-open', 'folder'])
    elif platform.system() == 'Darwin':
        subprocess.call(['open', 'folder'])
    else:
        print(f'{platform.system()} not supported')

if __name__ == "__main__":
    main()