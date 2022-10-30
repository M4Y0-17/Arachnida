# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scorpion.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: amayo-ca <amayo-ca@student.42barc...>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/08/29 18:14:12 by amayo-ca          #+#    #+#              #
#    Updated: 2022/08/29 18:49:05 by amayo-ca         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from PIL import Image
from PIL.ExifTags import TAGS
import tkinter
from tkinter import CENTER, ttk, filedialog, Label
import os
import colorama
from colorama import Fore


ventana = tkinter.Tk()

def banner():

	bcn ='''42Barcelona'''
	
	banner_tool = ''' __                      _             
/ _\ ___ ___  _ __ _ __ (_) ___  _ __  
\ \ / __/ _ \| '__| '_ \| |/ _ \| '_ \ 
_\ \ (_| (_) | |  | |_) | | (_) | | | |
\__/\___\___/|_|  | .__/|_|\___/|_| |_|
                  |_|                  '''
	by ='''                                 by M4Y0  '''
	print("")
	print(Fore.MAGENTA + bcn)
	print(Fore.YELLOW + banner_tool)
	print(Fore.CYAN + by)
	print(Fore.RESET)


def metadata_img(imgdir):

	image = Image.open(imgdir)

	# extracting the exif metadata
	exifdata = image.getexif()
	i = 5
	print("\n")
	# looping through all the tags present in exifdata
	for tagid in exifdata:
		i = i + 1
		# getting the tag name instead of tag id
		tagname = TAGS.get(tagid, tagid)
		# passing the tagid to get its respective value
		value = exifdata.get(tagid)
		# printing the final result
		print(f"{tagname:25}: {value}")

		#Label(ventana, text = str({tagname})[2:-2] + ":").grid(padx=5, pady=5, row=i, column=2)
		#solution = Label(ventana, text = str({value})[1:-1]).grid(padx=5, pady=5, row=i, column=3)
		#solution = Label(ventana, text = str({value})[2:-2]).column("1", anchor = CENTER)
	print("\n---------------------------------------------------------------------------------------------")

def exif_remove(filename):

	try:
		image = Image.open(filename)
		image.save(filename)
		print("\nMetadata Removed")
	except:
		print("\nPlease select a file\n")
		return None


def filebrowser():

	filename = filedialog.askopenfilename(initialdir = os.environ["HOME"], title = "Select File", filetypes = [('img files', '.jpg .jpeg .png .gif .bmp')])
	print("\nFile: ", filename)
	main(filename)


def main(filename):

	ventana.title('Scorpion')
	ventana.geometry("250x200")

	button_explore = ttk.Button(ventana, text = "Browse Files", command = filebrowser)
	button_explore.grid(column = 3, row = 2)

	button_delete = ttk.Button(ventana, text = "Delete Metadata", command = lambda: exif_remove(filename))
	button_delete.grid(column = 3, row = 3)

	button_meta = ttk.Button(ventana, text = "Show Metadata", command = lambda: metadata_img(filename))
	button_meta.grid(column = 4, row = 3)

	ventana.mainloop()


if __name__ == '__main__':
	banner()
	main(None)
