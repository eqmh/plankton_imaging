# Classifier
Classifier script which uses the trained model.PTH file to classify unclassified images 

# Overview
The classifier was originally created by Michael Stanly with Lynker Analytics and since then has been updated and modified to be more user friendly, although friendly is debatable.
This script requires a few extra steps be completed before being able to run it. 

# Load requirements.txt file in your virtual environment (zoop_env)    
From this repository download the **requirements.txt** file into your working directory. To run this script open the Anaconda Promp, cd into your working directory, activate your venv and then install the requirements file.  
- (base) C:\ > **cd C:\Users\Deana.Crouser\Documents\Algorithm**  
- (base) C:\Users\Deana.Crouser\Documents\Algorithm > **conda activate zoop_env**  
- (zoop_env) C:\Users\Deana.Crouser\Documents\Algorithm > **pip install -r requirements.txt**  

# Update and Run Image_Classification.py
Download Image_Classification.py into your working directory and open in your text editor (I use PyCharm).  
- Update line 19 with direcotry of unclassified images  
- Update line 20 with output direcotry path  
- Update line 21 with location to model PTH file output from the Algorithm and save  

In your virtual environment (zoop_env) run Image_Classficiation.py using the python command    
- (zoop_env) C:\Users\Deana.Crouser\Documents\Algorithm > **python Image_Classficiation.py**

To test your model on images from our system, below is a link to a small subset of unclassified images
- https://drive.google.com/file/d/1I0oGYxj19Zk7xu-ieOWv9I6ptJ40T_S0/view?usp=sharing
