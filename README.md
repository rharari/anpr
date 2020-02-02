# ANPR - Automatic number plate recognition

Identify a vehicle license plate using image processing. 

The chalenge is identify which region of the image is the plate and after apply an ocr over this region.

The purpose of this sample is not explain how to implement an OCR but how to find the plate for a given image.


## Steps to achieve the goal

1. Load the image and convert to grey scale

2. Apply a gaussian filter to remove noise

3. Apply more filters to transform to B&W and remove dark spots

4. Find the edges of relevant regions of the image

5. Apply OCR over these regions and get the plate number and get a collection of text.

6. Iterate over this collection of text to check if this is a car plate or other info like
   a sticker, advertising or other text in some region of the image.

If you are working with fixed camera you can also check the position (x,y) of each region
and avoid unecessary OCR processing since usually the plate is located in the same position
in all vehicles.

## What you need

- python 2.7 ~ 3.x (used v 3.7.6)
- some python libs (see bellow)

### Install python libs

```
pip3 install sklearn
pip3 install matplotlib
```


### Run

```
% python3 anpr.py
```



## Expected Result

#### Original Image

![img1](https://github.com/rharari/anpr/blob/master/result/img1.png)


#### Image converted to greyscale 

![img2](https://github.com/rharari/anpr/blob/master/result/img2.png)


#### Noise reduction

![img3](https://github.com/rharari/anpr/blob/master/result/img3.png)


#### Remove small dark spots and connect small bright cracks

![img4](https://github.com/rharari/anpr/blob/master/result/img4.png)


#### Clear objects connected to the label image border

![img5](https://github.com/rharari/anpr/blob/master/result/img5.png)


#### Cropped regions

![result1](https://github.com/rharari/anpr/blob/master/result/result1.png)


![result2](https://github.com/rharari/anpr/blob/master/result/result2.png)

and...

#### The Plate !

![result3](https://github.com/rharari/anpr/blob/master/result/result3.png)

## Testing with OCR

After pushing the image plate region to this free OCR https://www.newocr.com/ received the text:
MUIEPSD - \o/ 


![result3](https://github.com/rharari/anpr/blob/master/result/ocr_result.png)



## Other techniques

You can try other filters or adjust the parameters to achieve a better accuracy and performance.

![other1](https://github.com/rharari/anpr/blob/master/result/other1.png)

![other2](https://github.com/rharari/anpr/blob/master/result/other2.png)

![other3](https://github.com/rharari/anpr/blob/master/result/other3.png)

