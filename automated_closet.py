import os
import random

import tkinter as tk
from PIL import Image, ImageTk

os.chdir("/Users/farihatanjin/Downloads")

WINDOW_TITLE = 'Welcome to your closet!'
WINDOW_WIDTH = 220
WINDOW_HEIGHT = 500
IMG_HEIGHT = 300
IMG_WIDTH = 300
BEIGE_COLOR_HEX = '#E3C396'


# dynamically open folders and make a list, while ignoring any hidden files that start with "."
# just add any image file into these folders and they will magically appear in your wardrobe!
# for fun, try to expand this wardrobe to support shoes!
WARM_TOPS_CASUAL = [str("outfit/warm/casual/tops/") + file for file in os.listdir("outfit/warm/casual/tops/") if not file.startswith('.')]
WARM_TOPS_PROFESSIONAL = [str("outfit/warm/professional/tops/") + file for file in os.listdir("outfit/warm/professional/tops/") if not file.startswith('.')]
WARM_TOPS_WFH =[str("outfit/warm/WFM/tops/") + file for file in os.listdir("outfit/warm/WFM/tops/") if not file.startswith('.')]

COLD_TOPS_CASUAL = [str("outfit/cold/casual/tops/") + file for file in os.listdir("outfit/cold/casual/tops/") if not file.startswith('.')]
COLD_TOPS_PROFESSIONAL = [str("outfit/cold/professional/tops/") + file for file in os.listdir("outfit/cold/professional/tops/") if not file.startswith('.')]
COLD_TOPS_WFH = [str("outfit/cold/wfh/tops/") + file for file in os.listdir("outfit/cold/wfh/tops/") if not file.startswith('.')]

COLD_BOTTOMS_CASUAL = [str("outfit/cold/casual/bottoms/") + file for file in os.listdir("outfit/cold/casual/bottoms/") if not file.startswith('.')]
COLD_BOTTOMS_PROFESSIONAL = [str("outfit/cold/professional/bottom/") + file for file in os.listdir("outfit/cold/professional/bottom/") if not file.startswith('.')]
COLD_BOTTOMS_WFH = [str("outfit/cold/wfh/bottom/") + file for file in os.listdir("outfit/cold/wfh/bottom/") if not file.startswith('.')]

WARM_BOTTOMS_CASUAL = [str("outfit/warm/casual/bottom/") + file for file in os.listdir("outfit/warm/casual/bottom/") if not file.startswith('.')]
WARM_BOTTOMS_PROFESSIONAL = [str("outfit/warm/professional/bottoms/") + file for file in os.listdir("outfit/warm/professional/bottoms/") if not file.startswith('.')]
WARM_BOTTOMS_WFH = [str("outfit/warm/WFM/bottom/") + file for file in os.listdir("outfit/warm/WFM/bottom/") if not file.startswith('.')]



#WARM_SHOES_CASUAL = [str("outfit/warm/shoes/casual/") + file for file in os.listdir("outfit/warm/shoes/casual/") if not file.startswith('.')]
#WARM_SHOES_PROFESSIONAL = [str("outfit/warm/shoes/professional/") + file for file in os.listdir("outfit/warm/shoes/professional/") if not file.startswith('.')]
#WARM_SHOES_WFH = [str("outfit/warm/shoes/WFH/") + file for file in os.listdir("outfit/warm/shoes/WFH/") if not file.startswith('.')]

#COLD_SHOES_CASUAL = [str("outfit/cold/shoes/casual/") + file for file in os.listdir("outfit/cold/shoes/casual/") if not file.startswith('.')]
#COLD_SHOES_PROFESSIONAL = [str("outfit/cold/shoes/professional/") + file for file in os.listdir("outfit/cold/shoes/professional/") if not file.startswith('.')]
#COLD_SHOES_WFH = [str("outfit/cold/shoes/WFH/") + file for file in os.listdir("outfit/cold/shoes/WFH/") if not file.startswith('.')]


ALL_TOPS = WARM_TOPS_CASUAL + WARM_TOPS_PROFESSIONAL + WARM_TOPS_WFH + COLD_TOPS_CASUAL + COLD_TOPS_PROFESSIONAL + COLD_TOPS_WFH
ALL_BOTTOMS = WARM_BOTTOMS_CASUAL + WARM_BOTTOMS_PROFESSIONAL + WARM_BOTTOMS_WFH + COLD_BOTTOMS_CASUAL + COLD_BOTTOMS_PROFESSIONAL + COLD_BOTTOMS_WFH
#ALL_SHOES =  WARM_SHOES_CASUAL + WARM_SHOES_PROFESSIONAL + WARM_SHOES_WFH + COLD_SHOES_CASUAL + COLD_SHOES_PROFESSIONAL + COLD_SHOES_WFH

class WardrobeApp:

    def __init__(self, root):
        self.root = root

        # collecting all the clothes
        self.top_images = ALL_TOPS
        self.bottom_images = ALL_BOTTOMS
       # self.bottom_images = ALL_SHOES


        # first pictures for top and bottom
        self.tops_image_path = self.top_images[0]
     #   self.center_image_path = self.bottom_images[0]
        self.bottom_image_path = self.bottom_images[0]


        # creating 3 frames
        self.tops_frame = tk.Frame(self.root, bg=BEIGE_COLOR_HEX)
     #   self.center_frame = tk.Frame(self.root, bg=BEIGE_COLOR_HEX)
        self.bottoms_frame = tk.Frame(self.root, bg=BEIGE_COLOR_HEX)

        # adding top
        self.top_image_label = self.create_photo(self.tops_image_path, self.tops_frame)
        self.top_image_label.pack(side=tk.TOP)

        # adding bottom
     #   self.center_image_label = self.create_photo(self.center_image_path, self.center_frame)
      #  self.center_image_label.pack(side=tk.RIGHT)

        # addng shoes
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
     #   self.center_frame.pack(fill=tk.BOTH, expand=tk.YES)
        self.bottoms_frame.pack(fill=tk.BOTH, expand=tk.YES)

    def create_buttons(self):
        top_prev_button = tk.Button(self.tops_frame, text="Prev", command=self.get_prev_top)
        top_prev_button.pack(side=tk.LEFT)

        create_outfit_button = tk.Button(self.tops_frame, text="Generate random outfit", command=self.create_outfit)
        create_outfit_button.pack(side=tk.TOP)

        top_next_button = tk.Button(self.tops_frame, text="Next", command=self.get_next_top)
        top_next_button.pack(side=tk.RIGHT)


    #    center_prev_button = tk.Button(self.center_frame, text="Prev", command=self.get_prev_center)
     #   center_prev_button.pack(side=tk.LEFT)

#        center_next_button = tk.Button(self.center_frame, text="Next", command=self.get_next_center)
 #       center_next_button.pack(side=tk.RIGHT)

        bottom_prev_button = tk.Button(self.bottoms_frame, text="Prev", command=self.get_prev_bottom)
        bottom_prev_button.pack(side=tk.LEFT)

        bottom_next_button = tk.Button(self.bottoms_frame, text="Next", command=self.get_next_bottom)
        bottom_next_button.pack(side=tk.RIGHT)

    def create_photo(self, image, frame):
        top_image_file = Image.open(image)
        image = top_image_file.resize((IMG_WIDTH, IMG_HEIGHT), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(frame, image=photo, anchor=tk.CENTER)
        image_label.image = photo

        return image_label

    def update_photo(self, new_image, image_label):
        new_image_file = Image.open(new_image)
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
       # elif current_item in self.center_images:
        #    image_label = self.center_image_label
         #   self.center_image_path = next_image
        else:
            image_label = self.bottom_image_label
            self.bottom_image_path = next_image

        # update the photo
        self.update_photo(next_image, image_label)

    def get_next_top(self):
        self._get_next_item(self.tops_image_path, self.top_images, increment=True)

    def get_prev_top(self):
        self._get_next_item(self.tops_image_path, self.top_images, increment=False)

   # def get_prev_center(self):
            #self._get_next_item(self.center_image_path, self.center_images, increment=False)

   # def get_next_center(self):
          #  self._get_next_item(self.center_image_path, self.center_images, increment=True)

    def get_prev_bottom(self):
        self._get_next_item(self.bottom_image_path, self.bottom_images, increment=False)

    def get_next_bottom(self):
        self._get_next_item(self.bottom_image_path, self.bottom_images, increment=True)

    def create_outfit(self):
        # randomly select an outfit
        new_top_index = random.randint(0, len(self.top_images)-1)
        new_bottom_index = random.randint(0, len(self.bottom_images)-1)

        # add the clothes onto the screen
        self.update_photo(self.top_images[new_top_index], self.top_image_label)
        self.update_photo(self.bottom_images[new_bottom_index], self.bottom_image_label)



if __name__ == '__main__':
    root = tk.Tk()
    app = WardrobeApp(root)

    root.mainloop()


    def create_outfit(self):
        # randomly select an outfit
        new_top_index = random.randint(0, len(self.top_images)-1)
        new_bottom_index = random.randint(0, len(self.bottom_images)-1)

        # add the clothes onto the screen
        self.update_photo(self.top_images[new_top_index], self.top_image_label)
        self.update_photo(self.bottom_images[new_bottom_index], self.bottom_image_label)



if __name__ == '__main__':
    root = tk.Tk()
    app = WardrobeApp(root)

    root.mainloop()
