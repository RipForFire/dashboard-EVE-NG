# Importing python modules

# Importing 3rd party modules
from flask import Flask, render_template, request, redirect, url_for

# Importing local modules
import functions.file_mgmt as file_mgmt

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html', data=file_mgmt.get_data())

@app.route('/rename/folder', methods=['POST'])
def rename_folder():
    folder = request.form['folder']
    new_name = request.form['new_name']
    file_mgmt.rename_folder(folder, new_name)
    return redirect(url_for('hello'))

@app.route('/rename/file', methods=['POST'])
def rename_file():
    folder = request.form['folder']
    file = request.form['file']
    new_name = request.form['new_name']
    file_mgmt.rename_file(folder, file, new_name)
    return redirect(url_for('hello'))

@app.route('/delete/folder', methods=['POST'])
def delete_folder():
    folder = request.form['folder']
    file_mgmt.delete_folder(folder)
    return redirect(url_for('hello'))

@app.route('/delete/file', methods=['POST'])
def delete_file():
    folder = request.form['folder']
    file = request.form['file']
    file_mgmt.delete_file(folder, file)
    return redirect(url_for('hello'))

@app.route('/upload', methods=['POST'])
def upload():
    folder = request.form.get('folder')
    file = request.files['file']
    file_mgmt.upload_file(folder, file)
    return redirect(url_for('hello'))

@app.route('/create', methods=['POST'])
def create():
    folder = request.form['folder']
    file_mgmt.create_folder(folder)
    return redirect(url_for('hello'))

@app.route('/fix', methods=['POST'])
def fix():
    file_mgmt.fix_perms()
    return redirect(url_for('hello'))

if __name__ == '__main__':
    app.run(debug=True)
