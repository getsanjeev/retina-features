# Blood Vessel Segmentation and Microaneurysm Detection for Diabetic Retinopathy

In this project, we extract features namely blood vessels and microaneurysms for the purpose of analysing fundus images to detect signs of retinal tissue damage.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for you to test the algorithms on your own fundus images.

### Preprocessing
___
The main idea is to use ImageMagick's convert tool to trim off the blank space to the sides of the images, then pad them so that they are all 256x256. Thus the eye is always centered with edges against the edges of the image.

And also to create multiple versions of each image varying by hue and contrast and white balance.
#### Prerequisites

You must have ImageMagick's convert tool and GNU Parallel installed in order to run this.
```
$ sudo apt install imagemagick
```
```
$ sudo apt install parallel
```
These are available in all the major linux repositories.

#### Usage
Run `prep_image.sh` on each image to prepare the image variations and resized images. 

- [x] **NOTE:**  Make sure "Allow executing file as a program" is checked in the prep_image.sh Properties.

Assuming that your train and test images are in folders `train/` and `test/` respectively and the file `prep_image.sh` lies in your project's root directory, run the following command:

```
$ ls train/*.jpeg test/*.jpeg | parallel ./prep_image.sh
```

This will preprocess all the images into `processed/<variation>/train/` and `processed/<variation>/test/` .
