---
url: https://docs.cloud.google.com/healthcare-api/docs/resources/public-datasets/nih-chest/
title: NIH Chest X-ray dataset \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:14:07.332571+00:00
---

# NIH Chest X-ray dataset  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/resources/public-datasets/nih-chest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Resources ](https://docs.cloud.google.com/healthcare-api/docs/resources)



Send feedback 

#  NIH Chest X-ray dataset Stay organized with collections  Save and categorize content based on your preferences. 

The [NIH Chest X-ray dataset](https://nihcc.app.box.com/v/ChestXray-NIHCC) consists of 100,000 de-identified images of chest x-rays. The images are in PNG format.

The data is provided by the NIH Clinical Center and is available through the NIH download site: <https://nihcc.app.box.com/v/ChestXray-NIHCC>

You can also access the data via Google Cloud, as described in Google Cloud data access.

## License and attribution

There are no restrictions on the use of the NIH chest x-ray images. However, the dataset has the following attribution requirements:

  * Provide a link to the NIH download site: <https://nihcc.app.box.com/v/ChestXray-NIHCC>

  * Include a citation to the CVPR 2017 paper:

> Xiaosong Wang, Yifan Peng, Le Lu, Zhiyong Lu, Mohammadhadi Bagheri, Ronald Summers, ChestX-ray8: Hospital-scale Chest X-ray Database and Benchmarks on Weakly-Supervised Classification and Localization of Common Thorax Diseases, IEEE CVPR, pp. 3462-3471, 2017

  * Acknowledge that the NIH Clinical Center is the data provider




## Google Cloud data access

You can get the NIH chest x-ray images from Cloud Storage, BigQuery, or using the Cloud Healthcare API.

### Cloud Storage

The NIH chest x-ray data is available in the following Cloud Storage bucket:
    
    
    gs://gcs-public-data--healthcare-nih-chest-xray

[Go to the NIH chest x-ray dataset in Cloud Storage](https://console.cloud.google.com/storage/browser/gcs-public-data--healthcare-nih-chest-xray)

The bucket includes paths to the original PNG files, as well as to DICOM instances:

PNG (provided by NIH):
    
    
    gs://gcs-public-data--healthcare-nih-chest-xray/png/FILENAME.png

DICOM (provided by Google):
    
    
    gs://gcs-public-data--healthcare-nih-chest-xray/dicom/FILENAME.dcm

The Cloud Storage bucket uses the "Requester Pays" model for billing. Your Google Cloud project will be billed for the charges associated with accessing the NIH data. For more information, see [Requester Pays](https://docs.cloud.google.com/storage/docs/requester-pays).

### BigQuery

The NIH chest x-ray data is available in the `chc-nih-chest-xray` Google Cloud project in BigQuery. [Go to the NIH chest x-ray dataset in BigQuery](https://console.cloud.google.com/bigquery?project=chc-nih-chest-xray&p=chc-nih-chest-xray&page=project)

For information about accessing public data in BigQuery, see [BigQuery public datasets](https://docs.cloud.google.com/bigquery/public-data).

### Cloud Healthcare API

The NIH chest x-ray data is available in the following DICOM store hierarchy in Cloud Healthcare API:

**Project:** `chc-nih-chest-xray`   
**Dataset:** `nih-chest-xray`   
**DICOM store:** `nih-chest-xray`

To request access to the NIH chest x-ray dataset, complete [this form](https://services.google.com/fb/forms/cloudhealthcarepublicdatasetaccess/).

[Go to the NIH chest x-ray dataset in the Cloud Healthcare API DICOM Studio](https://console.cloud.google.com/healthcare/dicom-studio/workbench?project=chc-nih-chest-xray)

For more information, see the [DICOM overview](https://docs.cloud.google.com/healthcare-api/docs/concepts/dicom) and [Using the DICOMweb Standard](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicomweb).

#### Data viewers

You can also use the viewers that are integrated with the Cloud Healthcare API:

**eUnity** : https://demo.eunity.app

**IMS CloudVue** : https://cloudvue.imstsvc.com

### Additional Labels

To access expert labels for a subset of the NIH ChestX-ray14 dataset, complete the following form. After you have completed the form, you can download the labels.

[Go to the Google Form to get the labels](https://forms.gle/bmYPtLy4qsJahVKFA)

The labels were collected as part of two independent studies, and are described in the following papers:

  * [Chest Radiograph Interpretation with Deep Learning Models](https://pubs.rsna.org/doi/10.1148/radiol.2019191293)
  * [Deep Learning for Distinguishing Normal versus Abnormal Chest Radiographs and Generalization to Two Unseen Diseases Tuberculosis and COVID-19](https://www.nature.com/articles/s41598-021-93967-2)



There are two sets of labels, each associated with one of the studies. The first set of labels is associated with [the study published in _Radiology_](https://pubs.rsna.org/doi/10.1148/radiol.2019191293) and focuses on four chest x-ray findings: airspace opacity, pneumothorax, nodule/mass, and fracture. The second set of labels is associated with [the study published in _Scientific Reports_](https://www.nature.com/articles/s41598-021-93967-2) and includes all 14 findings released in the [original dataset](https://www.nih.gov/news-events/news-releases/nih-clinical-center-provides-one-largest-publicly-available-chest-x-ray-datasets-scientific-community), and a normal/abnormal label.

#### Four findings expert labels

In the [_Radiology_ paper](https://pubs.rsna.org/doi/10.1148/radiol.2019191293), the set of labels focused on four findings (airspace opacity, pneumothorax, nodule/mass, and fracture) and encompassed both validation and test sets. The final labels for each image were assigned via adjudicated review by three radiologists. Each image was first reviewed independently by three radiologists. For the test set, radiologists were selected at random for each image from a cohort of 11 American Board of Radiology certified radiologists. For the validation set, the three radiologists were selected from a cohort of 13 individuals, including board-certified radiologists and radiology residents.

If all readers were in agreement after the initial review, then that label became final. For images with label disagreements, images were returned for additional review. Anonymous labels and any notes from the previous rounds were also available during each iterative review. Adjudication proceeded until consensus, or up to a maximum of five rounds. For the small number of images for which consensus was not reached, the majority vote label was used.

Information available at the time of the radiologist review included only patient age and image view (anterior-posterior (AP) versus posterior-anterior (PA)). Additional clinical information was not available. For nodule/mass and pneumothorax, the possible labels were: "present", "absent", or "hedge" (meaning uncertain if present or absent). For opacity and fracture, the possible label values were only "present" or "absent".

The labels are in the directory `four_findings_expert_labels`. In `individual_readers.csv`, each row corresponds to the label for each of the four conditions provided by a single reader for a single image. Each image ID and the corresponding adjudication result is repeated across multiple rows (one row per reader). The reader ID is provided for stable linking across images. A cell value of `YES` means "present", `NO` means "absent", and `HEDGE` means "uncertain".

In `validation_labels.csv` and `test_labels.csv`, the metadata provided as part of the NIH Chest x-ray dataset has been augmented with four columns, one for the adjudicated label for each of the four conditions: fracture, pneumothorax, airspace opacity, and nodule/mass. There are 1,962 unique image IDs in the test set and 2,412 unique image IDs in the validation set for a total of 4,374 images with adjudicated labels. Only `YES` and `NO` appear in the adjudication label columns. If a column value is missing, then the image was not included in the adjudicated image set.

When using these labels, include the following citation:

> Anna Majkowska, Sid Mittal, David F. Steiner, Joshua J. Reicher, Scott Mayer McKinney, Gavin E. Duggan, Krish Eswaran, PoHsuan Cameron Chen, Yun Liu, Sreenivasa Raju Kalidindi, Alexander Ding, Greg S. Corrado, Daniel Tse, Shravya Shetty, Chest Radiograph Interpretation Using Deep Learning Models: Assessment Using Radiologist Adjudicated Reference Standards and Population-Adjusted Evaluation, Radiology, 2019.

For more information on the License and Attribution of the NIH Chest x-ray dataset, see the **License and attribution** section above.

#### All findings expert labels

In the [_Scientific Reports_ paper](https://www.nature.com/articles/s41598-021-93967-2), the set of labels focused on all 14 findings released in the [original dataset](https://www.nih.gov/news-events/news-releases/nih-clinical-center-provides-one-largest-publicly-available-chest-x-ray-datasets-scientific-community), and as a normal/abnormal label. The set of labels only contained images from the test set. These images are identical to the images included in the `Four Findings Expert Labels` test split, restricted to chest x-rays with PA view (810 images out of the 1,962 images).

The same five American Board of Radiology certified radiologists independently reviewed each image. Each radiologist was first asked whether the image contained any potentially actionable clinical finding (normal/abnormal label), and if so, to select which of the 14 conditions were present. Information available at the time of radiologist review included only patient age and image view (AP versus PA). Additional clinical information was not available.

The labels are in the directory `all_findings_expert_labels`. In `test_individual_readers.csv`, each row corresponds to a single radiologist's labels for a single image. This means that each image ID and patient ID is repeated across multiple rows (five rows per image, one row per reader). Each row also contains a reader ID so that the radiologists can be distinguished. Because there are a total of 810 images in this set, `test_individual_readers.csv` contains 4,050 rows with 810 unique image IDs. `test_individual_readers.csv` also contains a total of 19 columns. In addition to image ID, patient ID, and reader ID, there is a column for normal/abnormal, a column for each of the 14 findings, and a column for `Other` indicating other abnormal findings are present (outside of the 14 specified). A cell value of `YES` means "present" and `NO` means "absent".

`test_labels.csv` contains the ground truth labels used to evaluate the deep learning system in the [_Scientific Reports_ paper](https://www.nature.com/articles/s41598-021-93967-2). Each row contains the ground truth labels for a single image ID, and each image ID only appears in a single row, for a total of 810 rows. `test_labels.csv` has the same columns as `test_individual_readers.csv`, but without a "reader ID" column. To obtain these labels, three of the five radiologists who labeled this set were chosen at random to be the "ground truth radiologists" (the other two were used as points of comparison). These "ground truth radiologists" have reader IDs of "4343882785", "4343883593", and "4343883996". A majority vote was used to determine the final label for the normal/abnormal label and the final label for each particular finding. The final label for the `Other` column was determined to be `YES` if a majority of radiologists selected that a finding outside of the 14 was present, or if a majority of radiologists indicated that the image was abnormal, but no single finding had a majority of radiologists indicate was present.

When using these labels, include the following citation:

> Zaid Nabulsi, Andrew Sellergren, Shahar Jamshy, Charles Lau, Eddie Santos, Atilla P. Kiraly, Wenxing Ye, Jie Yang, Sahar Kazemzadeh, Jin Yu, Raju Kalidindi, Mozziyar Etemadi, Florencia Garcia Vicente, David Melnick, Greg S. Corrado, Lily Peng, Krish Eswaran, Daniel Tse, Neeral Beladia, Yun Liu, Po-Hsuan Cameron Chen, Shravya Shetty, Deep Learning for Distinguishing Normal versus Abnormal Chest Radiographs and Generalization to Two Unseen Diseases Tuberculosis and COVID-19, Scientific Reports, 2021\. https://doi.org/10.1038/s41598-021-93967-2

For more information on the License and Attribution of the NIH Chest x-ray dataset, see License and attribution.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
