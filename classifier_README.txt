Classifier README

08/05/2025: 
Use ‘img_distributor.Rmd’ in Stringmatch repo to create training set for the classifier. Make sure the right paths are selected in:
- dir_path (line 19)
- selected_base_dir (line 42)
- path_to_dest_files (line 125). This section is not needed and can be skipped.
- path_to_sel_files (line 205).
- second to last section is for checking repeated files across folders and should not be necessary.
- last section is for aggregating all or selected unclassified PNG files in a single folder to classify using the UW classifier.

Classified images (training library) will land in ‘Desktop/uw_classifier/training_dataset’.  This is a temporary directory.

The final set of curated imagery is contained in the ‘training_library’ folder.

From ‘training_library’ select categories that require augmentation based on number of files (e.g. < 500) and copy-paste these folders to ‘augmented_categories’. All other classes not requiring augmentation can be copy-pasted to ‘training_dataset_augmented’.

Run ‘dataAugmentation.py’ to augment classes in ‘augmented_categories’. 

After augmentation migrate folders in ‘augmented_categories’ to ‘training_dataset_augmented’. The folder ‘augmented_categories’ should be empty after the file migration.

Then run ‘RandomImageSelection_1,2,py’ to randomly select images from the training library contained in ‘training_dataset_augmented’. Randomized and balanced training set will be contained in the ‘randomized_balanced’ folder - This is the final training set that will be used in ‘ResNet-‘ routines under the ‘Algorithm’ folder.


 