from shutil import *
from os import *

try:
	inputs = input("Enter a path: ")
	chdir(inputs)
	mkdir("Files")
	mkdir("Videos")
	mkdir("Audios")
	mkdir("Archives")
	mkdir("Images")
	ls = listdir()
	for f in ls:
		if f.endswith('.svg') or f.endswith('.torrent') or f.endswith('.txt') or f.endswith('.doc') or f.endswith('.pdf') or f.endswith('.docx') or f.endswith('.html') or f.endswith('.py') or f.endswith('.pptx') or f.endswith('.exe') or f.endswith('.css') or f.endswith('.pyw') or f.endswith('.lnk') or f.endswith('.rtf') or f.endswith('.md'):
			move(f, "Files")
		elif f.endswith('.m4v') or f.endswith('.mp4'):
			move(f, "Videos")
		elif f.endswith('.mp3') or f.endswith('.m4a'):
			move(f, "Audios")
		elif f.endswith('.zip') or f.endswith('.rar') or f.endswith('.7z') or f.endswith('.tar') or f.endswith('.gz') or f.endswith('.xz') or f.endswith('.iso') or f.endswith('.tar.z'):
			move(f, "Archives")
		elif f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png') or f.endswith('.gif') or f.endswith('.raw') or f.endswith('.psd') or f.endswith('.svg') or f.endswith('.ico') or f.endswith('.eps'):
			move(f, "Images")

	print("\nALL DONE !!!")

except:
	print("ERROR !!!")