from cx_Freeze import setup, Executable

base = "win32GUI"

# Liste des fichiers à inclure
include_files = ['A.png']

setup(
    name="AYD",
    version="0.1",
    description="Téléchargez vos vidéos YouTube",
    executables=[Executable("ayd.py", base=base)],
    options={
        'build_exe': {
            'include_files': include_files
        }
    }
)
