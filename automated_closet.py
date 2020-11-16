import os
import random

import tkinter as tk
from PIL import Image, ImageTk

from tkinter import filedialog

#set your own working directory
#os.chdir("/Users/farihatanjin/Downloads")

#formatting
WINDOW_TITLE = 'Welcome to your closet!'
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1400
IMG_HEIGHT = 320
IMG_WIDTH = 200
TOP_HEIGHT = 280
TOP_WIDTH = 230
COLOR = '#F0C4B4'


# dynamically open folders and make a list, while ignoring any hidden files that start with "."

TOPS_CASUAL = [str("outfits/casual/tops/") + file for file in os.listdir("outfits/casual/tops/") if not file.startswith('.')]
TOPS_PROFESSIONAL = [str("outfits/professional/tops/") + file for file in os.listdir("outfits/professional/tops/") if not file.startswith('.')]
TOPS_WFH =[str("outfits/wfh/tops/") + file for file in os.listdir("outfits/wfh/tops/") if not file.startswith('.')]

BOTTOMS_CASUAL = [str("outfits/casual/bottoms/") + file for file in os.listdir("outfits/casual/bottoms/") if not file.startswith('.')]
BOTTOMS_PROFESSIONAL = [str("outfits/professional/bottoms/") + file for file in os.listdir("outfits/professional/bottoms/") if not file.startswith('.')]
BOTTOMS_WFH = [str("outfits/wfh/bottoms/") + file for file in os.listdir("outfits/wfh/bottoms/") if not file.startswith('.')]

ALL_TOPS = TOPS_CASUAL + TOPS_PROFESSIONAL + TOPS_WFH
ALL_BOTTOMS = BOTTOMS_CASUAL + BOTTOMS_PROFESSIONAL + BOTTOMS_WFH

class WardrobeApp:

    def __init__(self, root):
        self.root = root

        # collecting all the clothes
        self.top_images = ALL_TOPS
        self.bottom_images = ALL_BOTTOMS

        # first pictures for top and bottom
        self.tops_image_path = self.top_images[0]
        self.bottom_image_path = self.bottom_images[0]

        # creating 2 frames
        self.tops_frame = tk.Frame(self.root, bg=COLOR)
        self.bottoms_frame = tk.Frame(self.root, bg=COLOR)

        # adding top
        self.top_image_label = self.create_photo2(self.tops_image_path, self.tops_frame)
        self.top_image_label.pack(side=tk.TOP)


        # addng bottom
        self.bottom_image_label = self.create_photo(self.bottom_image_path, self.bottoms_frame)
        self.bottom_image_label.pack(side=tk.BOTTOM)


        self.create_background()

    def create_background(self):
        # title and resize the window
        self.root.title(WINDOW_TITLE)
        self.root.geometry('{0}x{1}'.format(WINDOW_WIDTH, WINDOW_HEIGHT))

        # create buttons
        self.create_buttons()

        # add the initial clothes onto the screen
        self.tops_frame.pack(fill=tk.BOTH, expand=tk.YES)
        self.bottoms_frame.pack(fill=tk.BOTH, expand=tk.YES)

    def create_buttons(self):

# buttons for browsing closet
        top_prev_button = tk.Button(self.tops_frame, text="Prev Top", highlightbackground='#97CEC8', command=self.get_prev_top)
        top_prev_button.pack(side=tk.LEFT)

        top_next_button = tk.Button(self.tops_frame, text="Next Top", highlightbackground='#97CEC8', command=self.get_next_top)
        top_next_button.pack(side=tk.RIGHT)

        bottom_prev_button = tk.Button(self.bottoms_frame, text="Prev Bottom", highlightbackground='#97CEC8', command=self.get_prev_bottom)
        bottom_prev_button.pack(side=tk.LEFT)

        bottom_next_button = tk.Button(self.bottoms_frame, text="Next Bottom", highlightbackground='#97CEC8', command=self.get_next_bottom)
        bottom_next_button.pack(side=tk.RIGHT)

#upload your own images
        upload_top_button = tk.Button(root, text="Upload top", highlightbackground='#97CEC8', command= lambda: self.open_image(self.top_image_label))
        upload_top_button.pack(side=tk.TOP)

        upload_bottom_button = tk.Button(root, text="Upload bottom", highlightbackground='#97CEC8', command= lambda: self.open_image(self.bottom_image_label))
        upload_bottom_button.pack(side=tk.BOTTOM)

#outfit generator buttons
        create_outfit_button = tk.Button(self.tops_frame, highlightbackground='#97CEC8',  text="Generate Random Outfit", command=self.create_outfit)
        create_outfit_button.pack(side=tk.TOP, pady=14)

        create_casual_button = tk.Button(self.tops_frame, highlightbackground='#97CEC8', text="Generate Casual Outfit", command=self.create_casual)
        create_casual_button.pack(side=tk.TOP)

        create_professional_button = tk.Button(self.bottoms_frame, highlightbackground='#97CEC8', text="Generate Professional Outfit", command=self.create_professional)
        create_professional_button.pack(side=tk.TOP, pady=4)

        create_wfh_button = tk.Button(self.bottoms_frame, highlightbackground='#97CEC8', text="Generate WFH outfit", command=self.create_wfh)
        create_wfh_button.pack(side=tk.TOP,pady=3)


#create photo bottom
    def create_photo(self, image, frame):
        top_image_file = Image.open(image)
        image = top_image_file.resize((IMG_WIDTH, IMG_HEIGHT), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(frame, image=photo, anchor=tk.CENTER)
        image_label.image = photo

        return image_label

#create photo for tops with different height, width than bottoms
    def create_photo2(self, image, frame):
        top_image_file = Image.open(image)
        image = top_image_file.resize((TOP_WIDTH, TOP_HEIGHT), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(frame, image=photo, anchor=tk.CENTER)
        image_label.image = photo

        return image_label

    def update_photo(self, new_image, image_label):
        new_image_file = Image.open(new_image)
        if (image_label == self.top_image_label):
            image = new_image_file.resize((TOP_WIDTH, TOP_HEIGHT), Image.ANTIALIAS)
        else:
            image = new_image_file.resize((IMG_WIDTH, IMG_HEIGHT), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)

        image_label.configure(image=photo)
        image_label.image = photo

    def _get_next_item(self, current_item, category, increment=True):
        """ Gets the Next Item In a Category depending on if you hit next or prev
        Args:
            current_item, str
            category, list
            increment, boolean
        """
        item_index = category.index(current_item)
        final_index = len(category) - 1
        next_index = 0

        if increment and item_index == final_index:
            next_index = 0  # cycle back to the beginning
        elif not increment and item_index == 0:
            next_index = final_index  # cycle back to the end
        else:
            incrementor = 1 if increment else -1
            next_index = item_index + incrementor

        next_image = category[next_index]

        # reset the image object
        if current_item in self.top_images:
            image_label = self.top_image_label
            self.tops_image_path = next_image
        else:
            image_label = self.bottom_image_label
            self.bottom_image_path = next_image

        # update the photo
        self.update_photo(next_image, image_label)

    def get_next_top(self):
        self._get_next_item(self.tops_image_path, self.top_images, increment=True)

    def get_prev_top(self):
        self._get_next_item(self.tops_image_path, self.top_images, increment=False)

    def get_prev_bottom(self):
        self._get_next_item(self.bottom_image_path, self.bottom_images, increment=False)

    def get_next_bottom(self):
        self._get_next_item(self.bottom_image_path, self.bottom_images, increment=True)

#function for generating random outfits
    def create_outfit(self):
        # randomly select an outfit

        self.top_images = ALL_TOPS
        self.bottom_images = ALL_BOTTOMS


        new_top_index = random.randint(0, len(self.top_images)-1)
        new_bottom_index = random.randint(0, len(self.bottom_images)-1)

        # add the clothes onto the screen
        self.update_photo(self.top_images[new_top_index], self.top_image_label)
        self.update_photo(self.bottom_images[new_bottom_index], self.bottom_image_label)

#casual outfit generator
    def create_casual(self):

        #change image accordingly
        self.top_images = TOPS_CASUAL
        self.bottom_images = BOTTOMS_CASUAL

        #random number generator
        new_top_index = random.randint(0, len(self.top_images) - 1)
        new_bottom_index = random.randint(0, len(self.bottom_images) - 1)

        # add the clothes onto the screen
        self.update_photo(self.top_images[new_top_index], self.top_image_label)
        self.update_photo(self.bottom_images[new_bottom_index], self.bottom_image_label)


#professional outfit generator
    def create_professional(self):
        self.top_images = TOPS_PROFESSIONAL
        self.bottom_images = BOTTOMS_PROFESSIONAL

        new_top_index = random.randint(0, len(self.top_images) - 1)
        new_bottom_index = random.randint(0, len(self.bottom_images) - 1)

        # add the clothes onto the screen
        self.update_photo(self.top_images[new_top_index], self.top_image_label)
        self.update_photo(self.bottom_images[new_bottom_index], self.bottom_image_label)

#work from home outfit generator
    def create_wfh(self):

        self.top_images = TOPS_WFH
        self.bottom_images = BOTTOMS_WFH

        new_top_index = random.randint(0, len(self.top_images) - 1)
        new_bottom_index = random.randint(0, len(self.bottom_images) - 1)

        # add the clothes onto the screen
        self.update_photo(self.top_images[new_top_index], self.top_image_label)
        self.update_photo(self.bottom_images[new_bottom_index], self.bottom_image_label)

#function for uploading own image
    def open_image(self, image_label):
        # Select the Imagename  from a folder


        x = self.openfilename()
        self.update_photo(x, image_label)


    def openfilename(self):
        # open file dialog box to select image
        # The dialogue box has a title "Open"
        filename = filedialog.askopenfilename(title='select item')
        return filename


if __name__ == '__main__':
    root = tk.Tk()
    app = WardrobeApp(root)

    root.mainloop()

