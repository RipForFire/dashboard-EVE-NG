# Importing python modules
import os

# Importing 3rd party modules
from werkzeug.utils import secure_filename

# Importing local modules

path = '/opt/unetlab/addons/qemu'

def get_data():
    data = []
    folders = os.listdir(path)

    # Get files in folder
    for folder in folders:
        files = os.listdir(path + '/' + folder, )
        folder_data = {'folder': folder, 'files': files}
        data.append(folder_data)

    return data

def rename_folder(folder, new_name):
    os.rename(path + '/' + folder, path + '/' + new_name)
    return

def rename_file(folder, file, new_name):
    os.rename(path + '/' + folder + '/' + file, path + '/' + folder + '/' + new_name)
    return

def delete_folder(folder):
    os.rmdir(path + '/' + folder)
    return
    
def delete_file(folder, file):
    os.remove(path + '/' + folder + '/' + file)
    return

def upload_file(folder, file):
    filename = secure_filename(file.filename)
    file_save_path = path + '/' + folder + '/' + filename
    file.save(file_save_path)
    return

def create_folder(folder):
    os.makedirs(path + '/' + folder)
    return

def fix_perms():
    os.system('/opt/unetlab/wrappers/unl_wrapper -a fixpermissions')
    return

def drive(size, folder):
    os.system('/opt/qemu/bin/qemu-img create -f qcow2 ' + path + '/' + folder + '/virtioa.qcow2 ' + size + 'G')
    return