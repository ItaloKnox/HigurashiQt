import os, shutil, platform, glob, requests
from subprocess import call
from sys import argv

# Enables the chapter name as an argument. Example: Himatsubushi
chapterName = argv[1]

if chapterName = 'ConsoleArcs':
    if platform.system() == 'Windows':
        call([r'aria2c', '--file-allocation=none', '--continue=true', '--retry-wait=5', '-m 0', '-x 8', '-s 8', f'https://07th-mod.com/rikachama/Himatsubushi-UI.7z'])
    else:
        call([r'aria2c', '--file-allocation=none', '--continue=true', '--retry-wait=5', '-m 0', '-x 8', '-s 8', f'https://07th-mod.com/rikachama/Himatsubushi-UI_UNIX.7z']) 

# Uses a wildcard to build the starting point for patch installation
for chapterNumber in glob.glob('./HigurashiEp0*_Data'):
    print("Higurashi Data folder found at: " + chapterNumber)

# Checks if the current OS is Windows and uses aria2c to download the right files for the system
def systemUI_download():
    if platform.system() == 'Windows':
        call([r'aria2c', '--file-allocation=none', '--continue=true', '--retry-wait=5', '-m 0', '-x 8', '-s 8', f'https://07th-mod.com/rikachama/{chapterName}-UI.7z'])
    else:
        call([r'aria2c', '--file-allocation=none', '--continue=true', '--retry-wait=5', '-m 0', '-x 8', '-s 8', f'https://07th-mod.com/rikachama/{chapterName}-UI_UNIX.7z'])       

def movies_download():
    if platform.system() == 'Windows':
        call([r'aria2c', '--file-allocation=none', '--continue=true', '--retry-wait=5', '-m 0', '-x 8', '-s 8', f'https://07th-mod.com/rikachama/{chapterName}-Movie.7z'])
    else:
        call([r'aria2c', '--file-allocation=none', '--continue=true', '--retry-wait=5', '-m 0', '-x 8', '-s 8', f'https://07th-mod.com/rikachama/{chapterName}-Movie_UNIX.7z'])       

# Tries backing up vanilla UI files for recovery later. If there is already a backup, it skips.
def backupVanillaUI():
    try:
        os.rename(f'{chapterNumber}/sharedassets0.assets', f'{chapterNumber}/sharedassets0.assets.backup')
        os.rename(f'{chapterNumber}/sharedassets0.assets.resS', f'{chapterNumber}/sharedassets0.assets.resS.backup')
    except FileExistsError:
        pass

# Clean up of some unnecessary folders before installing the files. Cleans up any pre-compilled .mg scripts, then proceeds to remove CG and CGAlt folders.
def cleanVanillaFiles():
    old_CG = f'{chapterNumber}/StreamingAssets/CG'
    old_CGAlt = f'{chapterNumber}/StreamingAssets/CGAlt'

    for mg in glob.glob(f'{chapterNumber}/StreamingAssets/CompiledUpdateScripts/*.mg'):
            os.remove(mg)
    
    if os.path.isdir(old_CG):
        shutil.rmtree(old_CG)
        
    if os.path.isdir(old_CGAlt):
        shutil.rmtree(old_CGAlt)

# Gets the patch list from the server, this file is used by the next function as an input list
def getDownloadList():
    url = f'https://07th-mod.com/installer/{chapterName}.zip'
    r = requests.get(url)
    open(f'{chapterName}.zip', 'wb').write(r.content)

# Downloads the patch using aria2c with the list and several arguments for better download speeds
def aria2c_download():
    arguments = [
        r'aria2c',
        '--file-allocation=none',
        '--continue=true',
        '--retry-wait=5',
        '-m 0',
        '-x 8',
        '-s 8',
        '-j 1',
        f'--input-file={chapterName}.zip',
    ]
    
    call(arguments)
    os.remove(f'{chapterName}.zip')

# Uses 7-zip to extract all the files in the root folder
def extractFiles():
    files = [
        "*-SE.7z",
        "*-CG.7z",
        "*-Voices.7z",
        "*.Voice.and.Graphics.Patch.*.zip",
        "*-UI*.7z",
        "*-BGM.7z",
        "*-CGAlt.7z",
        "*-Movie*.7z",
    ]
    for file in files:
        call([r'7z', 'x', file, '-aoa'])

print("Downloading patch files...")
systemUI_download()
movies_download()
getDownloadList()
aria2c_download()
print("Backing up UI...")
backupVanillaUI()
print("Removing unnecessary folders and files...")
cleanVanillaFiles()
print("Installing patch...")
extractFiles()
print("All done, the patch was successfully installed.")