Follow these steps:

1. Download data from CPICS and store them in cpics_img

2. Aggregate raw, unclassified images in unclassified_dataset/unclassified using unclassified_selector.py > set environment to 'feat_ext'.

3. If using 'cpics_img' in local machine, upload 'unclassified_dataset/unclassified' to Holocron using terminal: rsync -avz /Users/enrique.montes/Desktop/uw_classifier/unclassified_dataset enrique.montes@holocron.aoml.noaa.gov:/home/enrique.montes@CNS.local/plankton_imaging

4. On the VSCode terminal run conda activate zoop_env

5. Run data_cleaner.py in /home/enrique.montes@CNS.local/plankton_imaging/spc_uw_zoocam/Classifier/data_cleaner.py

6. Run Image_Classification.py in /home/enrique.montes@CNS.local/plankton_imaging/spc_uw_zoocam/Classifier/. Select CONFIDENCE_THRESHOLD value

7. On the VSCode terminal run conda deactivate and then conda activate feat_ext

8. Run getmajorandminoraxis2025_9_EM.py in /home/enrique.montes@CNS.local/plankton_imaging/deep_features/

9. Run ecotaxa_table.ipynb in /plankton_imaging/ > select 'feat_ext' as Python environment