

'''
1- The first function get_list_sorted(main_path , answer) takes the full path of the target image folder, 
and takes the user's answer, in order to arrange the images in ascending or descending order. In the entered folder

2- The second function best_image(path_image) takes the full path of the target image folder and then returns the best image in terms
of resolution and it takes only one parameter, which is the full path of the folder containing the images

3- The third function (lowest_image) takes the full path of the target image folder and then returns the lowest image in 
terms of resolution and it takes only one parameter, which is the full path of the folder containing the images It 
works in contrast to the best_image function


4- Fifth function: (get_bytes) Returns the size of the image in the device's memory, takes the full path of the target image

5- The sixth function: (check_path) It checks the image folder if the entered path is a folder and not a file. In this case, the full path
will be returned, otherwise an error message will be returned.

6- The seventh function: (get_list) It returns a list containing all the images ending with the extension 
".png", ".jpg", ".jpeg" and at the same time it is an unordered list

7- The eighth function: (calculate_selected_photos) It counts the number of images that end with the required extension, it takes the full
path of the folder for the images in addition to the name of the extension required for the calculation

8- The ninth function: (similarity_check) Its task is to check the similarity of the images, and it takes the first parameter as the 
path of the first image, and the second parameter is the path of the second image.

'''


from PIL import Image
from scipy.spatial.distance import dice
import os
import sys
import shutil


class ImageProcessing:
    """ Arrange the images in ascending or descending order """
    def __init__(self):
        self.condition_answer = False
        self.picture_dictionary = dict()
        self.list_pixels = list()
        self.list_names = list()

    def check_path(self,path):
        """ Check the full path """
        try:
            if os.path.isfile(path):
                return "Error Please enter the correct folder path and not the file path : {}".format(path)
            elif os.path.isdir(path):
                return path

            else:
                return "The path is incorrect or may not exist :{}".format(path)
        except Exception as erro_path:
            return erro_path
        except AttributeError as error:
            return error

   
    def get_list(path_img):
        """ Returns the list of all images at random, and in unordered """
        condition = False 
        if os.path.isdir(path_img):
            condition = True
        else:
            condition = False

        if condition == True:
            images = list(filter(lambda x: x.endswith((
                                                            ".JPG" , ".PNG" , ".GIF" , ".WEBP" ,
                                                            ".TIFF" , ".PSD" , ".RAW" , ".BMP",
                                                            ".HEIF" , ".INDD" , ".JPEG", ".SVG",
                                                            ".AI" , ".EPS" , ".PDF"



                                                            )), os.listdir(path)))
            return images
        return "The path is wrong, please check it correctly : {}".format(path_img)



    def get_list_sorted(self, path, answer):
        """ arrange photos take Full Path And take an answer (True) , (False)"""
        self.picture_temp , self.list_result = dict(),list()

        if not isinstance(answer, (bool)):
            self.condition_answer = False
        else:
            self.condition_answer = True

        if self.condition_answer == False:
            return "Please enter a Boolean value {} or {}".format(True, False)
        self.list_image = list(filter(lambda x: x.endswith((
                                                            ".JPG" , ".PNG" , ".GIF" , ".WEBP" ,
                                                            ".TIFF" , ".PSD" , ".RAW" , ".BMP",
                                                            ".HEIF" , ".INDD" , ".JPEG", ".SVG",
                                                            ".AI" , ".EPS" , ".PDF"



                                                            )), os.listdir(path)))

        for name in self.list_image:
            with Image.open(path + '\\' + name) as image :
                width , height = image.size
                self.picture_dictionary[name] = sum([width,height])


        self.list_names = sorted(self.picture_dictionary.keys(),reverse=answer)
        self.list_pixels = sorted(self.picture_dictionary.values(),reverse=answer)

        for (name,size) in zip(self.list_names,self.list_pixels):
            self.picture_temp[name] = size

        self.picture_dictionary = self.picture_temp

        for (name) in self.picture_dictionary.keys():
           self.list_result.append(name)
        return False if len(self.list_result) < 1 else self.list_result


    def best_image(self,path):
        """ Get Best Image """
        self.picture_best = dict()
        self.list_best = list(filter(lambda x: x.endswith((
                                                            ".JPG" , ".PNG" , ".GIF" , ".WEBP" ,
                                                            ".TIFF" , ".PSD" , ".RAW" , ".BMP",
                                                            ".HEIF" , ".INDD" , ".JPEG", ".SVG",
                                                            ".AI" , ".EPS" , ".PDF"



                                                            )), os.listdir(path)))

        for name_best in self.list_best:
            with Image.open(path + '\\' + name_best) as image :
                width , height = image.size
                self.picture_best[name_best] = sum([width,height])

        self.best_name , self.best_size = '',0
        for (name,size) in self.picture_best.items():
            if (self.best_size < size):
                self.best_size = size
                self.best_name = name 

        if (self.best_size) > 0 and (self.best_name) in self.picture_best.keys():
            print([self.best_name , self.best_size , path])
            print("\n")
            return (f"name Image :{self.best_name}\ntotal dimensions :{self.best_size} Pixel\nLocation :{path}")


    def lowest_image(self,path):
        """ Return the lowest image """
        self.picture_lowest = dict()
        #self.list_lowest = list(filter(lambda x: x.endswith((".png", ".jpg", ".jpeg")), os.listdir(path)))
        self.list_lowest = list(filter(lambda x: x.endswith((
                                                            ".JPG" , ".PNG" , ".GIF" , ".WEBP" ,
                                                            ".TIFF" , ".PSD" , ".RAW" , ".BMP",
                                                            ".HEIF" , ".INDD" , ".JPEG", ".SVG",
                                                            ".AI" , ".EPS" , ".PDF"



                                                            )), os.listdir(path)))

        for name_lowest in self.list_lowest:
            with Image.open(path + '\\' + name_lowest) as image :
                width , height = image.size
                self.picture_lowest[name_lowest] = sum([width,height])

        self.name_lowest , self.size_lowest = '', list(self.picture_lowest.values())[0]

        for (name,size) in self.picture_lowest.items():
            if (size < self.size_lowest):
                self.size_lowest = size
                self.name_lowest = name
        if (self.size_lowest) > 0 and (self.name_lowest) in self.picture_lowest.keys():
            return [self.name_lowest , self.size_lowest , path]
           

    def get_bytes(self,path_mg):
        """ Returns the size of the image in the device's memory get full path image"""
        if not os.path.exists(path_mg):
            return "The path is wrong, please check it correctly : {}".format(path_mg)
        self.bytes_image = os.path.getsize(path_mg)

        if self.bytes_image <=1 :
            return "Error Bytes"
        return "Image size in device memory : {}".format(self.bytes_image)


    def calculate_selected_photos(self,path , stretch):
        """ Count the number of images ending in the extension (PNG, JPEG , JPG)"""
        try :
            if not os.path.exists(path):
                if not os.path.isdir(path):
                    raise Exception("Please check the image path is correct :{}".format(path))
            return len(list(filter(lambda count :count.endswith((stretch)),os.listdir(path))))

        except FileNotFoundError as error :
            return error
        raise NotADirectoryError("Invalid Path")

    def similarity_check(self,path_image_one , path_image_two):
        """ Similarity check if the two images are the same """
        try :
            if not os.path.exists(path_image_one) or not os.path.exists(path_image_two):
                raise FileNotFoundError("The path is wrong Please check the path is correct")
            self.img1 = Image.open(path_image_one)
            self.img2 = Image.open(path_image_two)

            if list(self.img1.getdata()) != list(self.img2.getdata()):
                return "No match" 
            return "There is a match"
        except Exception as er :
            return er

