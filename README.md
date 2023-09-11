# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Raspberry_Pi_Assignment_Template](#raspberry_pi_assignment_template)
* [Raspberry_Pi_Launch Pad part 1](#Launch_Pad_Part:1)
* [Onshape_Assignment_Template](#onshape_assignment_template)

&nbsp;

## Raspberry_Pi_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Evidence 

Pictures / Gifs of your work should go here. You need to communicate what your thing does. 

### Wiring

This may not be applicable to all assignments. Anything where you wire something up, include the wiring diagram here. The diagram should be clear enough that I can recreate the wiring from scratch. 

### Code
Give me a link to your code. [Something like this](https://github.com/millerm22/Engineering_4_Notebook/blob/main/Raspberry_Pi/hello_world.py). Don't make me hunt through your folders, give me a nice link to click to take me there! Remember to **COMMENT YOUR CODE** if you want full credit. 


### Test Link

[Hyperlink text](http://www.google.com)      

### Test Image

![Picture Name Here](images/images.jpg)  

### Test GIF

![Picture Name Here](images/200w.gif)  

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;
## Launch_Pad_Part:1
### Assignment Description

The purpose of this assignment is to create a countdown from ten for a rocket launch. You need to use a Raspeberry Pi pico and VS Code.

### Evidence 
<img src="https://github.com/VeganPorkChop/Engineering-4_Notebook/assets/91289762/449f416f-f686-4f36-bb11-58b909ea0816" 
     width="500" 
     height="500" />
<img src="https://github.com/VeganPorkChop/Engineering-4_Notebook/assets/91289762/df4820ab-2d22-4d23-8442-0d9be207b481" 
     width="500" 
     height="500" />
### Wiring
<img src="https://github.com/VeganPorkChop/Engineering-4_Notebook/assets/91289762/f2f76f33-a8ff-4e6f-9666-02360abc213f" 
     width="500" 
     height="500" />

### Code
<details open>
<summary>Launch_Pad_Part:1 Code</summary>
<br>
```py
import board
import time
import digitalio

while True:
    for x in range(10, -1 ,-1):
        time.sleep(1)
        print(x)
        if x == 0:
            print('LAUNCH')
```
</details>

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;
## Onshape_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Part Link 

[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021). Don't forget to turn on link sharing in your Onshape document so that others can see it. 

### Part Image

Take a nice screenshot of your Onshape document. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;

## Media Test

Your readme will have various images and gifs on it. Upload a test image and test gif to make sure you've got the process figured out. Pick whatever image and gif you want!

### Test Link

### Test Image

### Test GIF
