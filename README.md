<img src="https://user-images.githubusercontent.com/16596327/30457494-28eefde8-99c5-11e7-96ce-19f713a9d989.jpg" align="right" />

# Blood Vessel Segmentation and Microaneurysm Detection for Diabetic Retinopathy

> In this project, we extract features namely blood vessels microaneurysms and exudates for the purpose of analysing fundus images to detect signs of retinal tissue damage.

> For exudates segmentation, Please visit [Retinal Exudates Detection](https://github.com/getsanjeev/retinal-exudates-detection).

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
## Table of Contents

- [Getting Started](#getting-started)
  - [Preprocessing](#preprocessing)
    - [Prerequisites](#prerequisites)
    - [Usage](#usage)
  - [Bloodvessel Segmentation](#bloodvessel-segmentation)
    - [Prerequisites](#prerequisites-1)
    - [Usage](#usage-1)
    - [Sample Output](#sample-output)
  - [Microaneurysm Detection](#microaneurysm-detection)
    - [Prerequisites](#prerequisites-2)
    - [Usage](#usage-2)
    - [Sample Output](#sample-output-1)
- [Documents](#documents)
    - [Poster, Presentation and Report](#documents)
- [Contributing](#contributing)
- [Authors](#authors)
- [License](#license)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for you to test the algorithms on your own fundus images. The [MESSIDOR](http://www.adcis.net/en/Download-Third-Party/Messidor.html) database has been used for demonstration here for which we are grateful.
<br><br>
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

This will preprocess all the images into `processed/<variation>/train/` and `processed/<variation>/test/`.

<br><br>

### Bloodvessel Segmentation
___

#### Prerequisites

The following must be installed and configured:
* [Python](https://www.python.org/downloads/)
* [OpenCV](http://opencv.org/)

Follow the links for source and installation instructions.
#### Usage
Change the `pathFolder` and `destinationFolder` variable in the file `bloodvessels.py` to point to the directory where your images are located.
```
pathFolder = "/home/sherlock/DR/MODEL_1_SVM/Base11/"
destinationFolder = "/home/sherlock/DR/MODEL_1_SVM/Base11Bloodvessels/"
```
Open a terminal and navigate to where the `bloodvessels.py` file is located and run the following command:
```
$ python bloodvessels.py
```
*OR*
```
$ python3 bloodvessels.py
```

For each image in your input folder, this will save one image `<imageName>_Bloodvessel.png` (segmented Bloodvessels).

#### Sample Output
For some image in Base11:

<img src="https://user-images.githubusercontent.com/16596327/30451279-beedb542-99b0-11e7-8f46-a215dbb68695.jpg" width="400">

Following resultant image is generated in the `Destination folder`:

* Bloodvessels.png

<img src="https://user-images.githubusercontent.com/20872683/30469609-ae959b7a-9a0e-11e7-92b7-e2e90a49cc88.png" width="400"> 

<br><br>

### Microaneurysm Detection
___

#### Prerequisites

The following must be installed and configured:
* [Python](https://www.python.org/downloads/)
* [SimpleCV](https://github.com/sightmachine/SimpleCV)

Follow the links for source and installation instructions.
#### Usage
Change the `pathFolder` variable in the file `microaneurysm.py` to point to the directory where your images are located.
```
pathFolder = "/home/utkarsh/SimpleCV/input"
```
- [x] **NOTE:**  Make sure you manually create a file `ma.csv` in the same directory as that of `microaneurysm.py`.
Open a terminal and navigate to where the `microaneurysm.py` file is located and run the following command:
```
$ python microaneurysm.py
```
*OR*
```
$ python3 microaneurysm.py
```
depending upon the version of python for which SimpleCV is configured.

For each image in your input folder, this will save two images `<imageName>_MA.tif` (detected aneurysms in white over black image) and `<imageName>_MAoverlay.tif` (detected aneurysms in white overlaid upon the original image).
Also, the file `ma.csv` will now contain the white pixel count from the `<imageName>_MA.tif` for each image in the input folder.

#### Sample Output
For a single image in the input folder `/home/utkarsh/SimpleCV/input/input.tif`:

<img src="https://user-images.githubusercontent.com/16596327/30451279-beedb542-99b0-11e7-8f46-a215dbb68695.jpg" width="400">

Following two images are generated in the same folder as `microaneurysm.py`:

* input_MA.tif and input_MAoverlay.tif

<img src="https://user-images.githubusercontent.com/16596327/30451295-cb73815c-99b0-11e7-8881-547576e85e11.jpg" width="400">  <img src="https://user-images.githubusercontent.com/16596327/30451296-cb755dce-99b0-11e7-963a-3ceb0de184f7.jpg" width="400">

* The `ma.csv` file looks like:

microaneurysmcount | countvalue
--- | ---
input_microaneurysm.jpg | 2920

## Documents

* [Poster](poster.pdf)
* [Presentation](presentation.pdf)
* [Report](report.pdf)

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

<a href="http://ducic.ac.in/"><img src="https://user-images.githubusercontent.com/16596327/30467922-9d4985ce-9a05-11e7-81aa-9f5348eb40de.png" align="right" width="300"/></a>

* **[Sanjeev Dubey](https://github.com/getsanjeev)** - *getsanjeevdubey@gmail.com*
* **[Utkarsh Mittal](https://github.com/utkarshmttl)** - *utkarshmttl@gmail.com*
* **[Raghav Singh](https://github.com/raghav1875)** - *raghav97singh.rs@gmail.com*

See also the list of [contributors](https://github.com/getsanjeev/classifier-fundus-diabetic-retinopathy/graphs/contributors) who participated in this project.

## License

This project is licensed under the BSD-3-Clause License - see the [LICENSE.md](LICENSE.md) file for details
