---
url: https://docs.cloud.google.com/vision-ai/docs/ppe-detector-model/
title: Personal protective equipment (PPE) detector guide \u00a0|\u00a0 Agent Platform Vision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:21.545534+00:00
---

# Personal protective equipment (PPE) detector guide  |  Agent Platform Vision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/ppe-detector-model/

Vertex AI Vision is deprecated as of June 15, 2026 and reaches End of Life on September 30, 2026. To migrate, see the [Cloud Vision API](https://docs.cloud.google.com/vision/docs), [Agent Platform serverless training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview), or [Agent Platform models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/vision-ai/docs/cloud-environment)



Send feedback 

#  Personal protective equipment (PPE) detector guide Stay organized with collections  Save and categorize content based on your preferences. 

![person blur model card in console](https://docs.cloud.google.com/static/vision-ai/docs/images/ppe-detector-card.png)

The **Personal Protective Equipment (PPE) Detector** model helps you verify the presence of equipment that limits exposure to hazards in a workplace or community environment.

The model detects people and the PPE items (gloves, masks, and helmets) on a specific person. The model detects the PPE items, and if the items cover the corresponding human body parts. The model reports this coverage information as a coverage score ranging from [0, 1]. The model accepts a video stream as input. The model outputs detection results as a [protocol buffer](https://developers.google.com/protocol-buffers) that you can view in BigQuery. The model runs at one FPS.

The PPE detection operator has three control parameters you can set:

  * check_box **Head coverings** : The operator outputs head coverage-related PPE item information. Set this value in the Google Cloud console, or set `enableHeadCoverageDetection` to true in the [`PersonalProtectiveEquipmentDetectionConfig`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1alpha1/ApplicationConfigs#personalprotectiveequipmentdetectionconfig).
  * check_box **Face coverings** : The operator outputs face coverage-related PPE item information. Set this value in the Google Cloud console, or set `enableFaceCoverageDetection` to true in the [`PersonalProtectiveEquipmentDetectionConfig`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1alpha1/ApplicationConfigs#personalprotectiveequipmentdetectionconfig).
  * check_box **Hand coverings** : The operator outputs hand coverage-related PPE item information. Set this value in the Google Cloud console, or set `enableHandsCoverageDetection` true in the [`PersonalProtectiveEquipmentDetectionConfig`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1alpha1/ApplicationConfigs#personalprotectiveequipmentdetectionconfig).



## PPE detector model app specifications

Use the following instructions to create a PPE detector model in the Google Cloud console.

###  Console 

**Create an app in the Google Cloud console**

  1. To create a PPE detector app, follow instructions in [Build an application](https://docs.cloud.google.com/vision-ai/docs/build-app).

[Go to the Applications tab](https://console.cloud.google.com/ai/vision-ai/applications)




**Add a PPE detector model**

  1. When you add model nodes, select the **PPE detector** from the list of pre-trained models.

  2. Set the types of PPE you want to detect in the options menu.




**Add a BigQuery connector**

  1. To use the output, connect the app to a **BigQuery** connector.

For information about using the **BigQuery** connector, see [Connect and store data to BigQuery](https://docs.cloud.google.com/vision-ai/docs/connect-bigquery). For BigQuery pricing information, see the [BigQuery pricing](https://cloud.google.com/bigquery/pricing) page.




**View output results in BigQuery**

After the model outputs data to BigQuery, view output annotations in the BigQuery dashboard.

If you didn't specify a BigQuery path, you can view the system-created path in the Agent Platform Vision schema**Studio** page.

  1. In the Google Cloud console, open the BigQuery page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. Select arrow_drop_down**Expand** next to the target project, dataset name, and application name.

![Select app table in BigQuery](https://docs.cloud.google.com/static/vision-ai/docs/images/bq-view-app-table.png)

  3. In the table detail view, click **Preview**. View results in the **annotation** column. For a description of the output format, see model output.




The application stores results in chronological order. The oldest results are the beginning of the table, while the most recent results are added to the end of the table. To check the latest results, click the page number to go to the last table page.

## Model output

The model output includes a timestamp, the detection boxes, object labels that correspond to the boxes, and confidence scores from that object. The rate of the output stream is one frame per second.

The model output is a [protocol buffer](https://developers.google.com/protocol-buffers) format that includes information on the video frame and PPE detection prediction result. The goal of the model is to check whether people are properly wearing protective equipment. As a result, the model focuses on detecting people and the PPE the person wears. The model output focuses on person detection. For each person that is detected, the model lists the PPE around the person and the coverage score of each piece of equipment.

In the protocol buffer example that follows, note the following.

  * Current time - The timestamp notes the time the inference result is made.
  * Detected persons - The main detection result that includes one person-identified box, multiple PPE-identified boxes, and a coverage score for each body part.
  * Person identified box - The bounding box, confidence score, and person entity.
  * PPE identified box - The bounding box, confidence score, and PPE entity.



### Sample annotation output JSON object
    
    
    {
      "**currentTime** ": "2022-11-10T21:02:13.499255040Z",
      "**detectedPersons** ": [
        {
          "personId": "0",
          "**detectedPersonIdentifiedBox** ": {
            "boxId": "0",
            "normalizedBoundingBox": {
              "xmin": 0.486749,
              "ymin": 0.35927793,
              "width": 0.048630536,
              "height": 0.21746585
            },
            "confidenceScore": 0.31775203,
            "personEntity":{
              "personEntityId":"0"
            }
          },
          "**detected_ppe_identified_boxes** ": {
            "normalized_bounding_box": {
              "xmin": 0.07268746,
              "ymin": 0.80575824,
              "width": 0.22973709,
              "height": 0.18754286
            },
            "confidence_score": 0.45171335,
            "ppe_entity": {
              "ppe_label_string": "Glove",
              "ppe_supercategory_label_string": "Hand Coverage"
            }
          },
          "**detected_ppe_identified_boxes** ":{
            "normalized_bounding_box":{
              "xmin": 0.35457548,
              "ymin": 0.016402662,
              "width": 0.31828704,
              "height": 0.18849815
            },
            "confidence_score": 0.44129524,
            "ppe_entity":{
              "ppe_label_string": "Helmet",
              "ppe_supercategory_label_string": "Head Coverage"
              }
          }
        }
      ]
    }

### Protocol buffer definition
    
    
    // Output format for Personal Protective Equipment Detection Operator
    message PersonalProtectiveEquipmentDetectionOutput {
     // Current timestamp
     protobuf.Timestamp current_time = 1;
    
     // The entity info for annotations from person detection prediction result
     message PersonEntity {
    
       // Entity id
       int64 person_entity_id = 1;
     }
    
     // The entity info for annotations from PPE detection prediction result
     message PPEEntity {
       // Label id
       int64 ppe_label_id = 1;
       // Human readable string of the label (Examples: helmet, glove, mask)
       string ppe_label_string = 2;
       // Human readable string of the super category label (Examples: head_cover,
       // hands_cover, face_cover)
       string ppe_supercategory_label_string = 3;
       // Entity id
       int64 ppe_entity_id = 4;
     }
    
     // Bounding Box in the normalized coordinates
     message NormalizedBoundingBox {
       // Min in x coordinate
       float xmin = 1;
       // Min in y coordinate
       float ymin = 2;
       // Width of the bounding box
       float width = 3;
       // Height of the bounding box
       float height = 4;
     }
    
     // PersonIdentified box contains the location and the entity info of the
     // person
     message PersonIdentifiedBox {
       // An unique id for this box
       int64 box_id = 1;
       // Bounding Box in the normalized coordinates
       NormalizedBoundingBox normalized_bounding_box = 2;
       // Confidence score associated with this box
       float confidence_score = 3;
       // Person entity info
       PersonEntity person_entity = 4;
     }
    
     // PPEIdentified box contains the location and the entity info of the PPE
     message PPEIdentifiedBox {
       // An unique id for this box
       int64 box_id = 1;
       // Bounding Box in the normalized coordinates
       NormalizedBoundingBox normalized_bounding_box = 2;
       // Confidence score associated with this box
       float confidence_score = 3;
       // PPE entity info
       PPEEntity ppe_entity = 4;
     }
    
     // Detected Person contains the detected person and their associated
     // PPE and their protecting information
     message DetectedPerson {
       // The id of detected person
       int64 person_id = 1;
       // The info of detected person identified box
       PersonIdentifiedBox detected_person_identified_box = 2;
       // The info of detected person associated ppe identified boxes
       repeated PPEIdentifiedBox detected_ppe_identified_boxes = 3;
    
       // Coverage score for each body part
    
    
       // Coverage score for face
       optional float face_coverage_score = 4;
       // Coverage score for eyes
       optional float eyes_coverage_score = 5;
       // Coverage score for head
       optional float head_coverage_score = 6;
       // Coverage score for hands
       optional float hands_coverage_score = 7;
       // Coverage score for body
       optional float body_coverage_score = 8;
       // Coverage score for feet
       optional float feet_coverage_score = 9;
     }
    
     // A list of DetectedPersons
     repeated DetectedPerson detected_persons = 2;
    }
    

## Best practices and limitations

To get the best results when you use the PPE detector, consider the following when you source data and use the model.

### Source data recommendations

Recommended: When possible, have detection subjects stand still and face the camera.

Sample image data the PPE detector is able to process correctly:

![sample image of a person facing the camera with face covering](https://docs.cloud.google.com/static/vision-ai/docs/images/ppe-detector-good-example1_ani-kolleshi.jpg)_Image source:[Ani Kolleshi](https://unsplash.com/photos/7jjnJ-QA9fY) on [Unsplash](https://unsplash.com/)._ |  ![sample image of a person facing the camera with face covering](https://docs.cloud.google.com/static/vision-ai/docs/images/ppe-detector-good-example3_ahsanization.jpg)_Image source:[Ahsanization](https://unsplash.com/photos/UTO8escGF3M) on [Unsplash](https://unsplash.com/)._ |  ![sample image of a person facing the camera with face covering](https://docs.cloud.google.com/static/vision-ai/docs/images/ppe-detector-good-example2_anastasiia-chepinska.jpg)_Image source:[Anastasiia Chepinska](https://unsplash.com/photos/eGjHhmC_3ww) on [Unsplash](https://unsplash.com/)._  
---|---|---  
  
Not recommended: Avoid image data where the key PPE items are too small in the frame.

Sample image data the PPE detector isn't able to process correctly:

![sample image of PPE items that are too small to be detected](https://docs.cloud.google.com/static/vision-ai/docs/images/ppe-detector-bad-example1_josue-isai-ramos-figueroa.jpg)_Image source:[Josue Isai Ramos Figueroa](https://unsplash.com/photos/qvBYnMuNJ9A) on [Unsplash](https://unsplash.com/)._  
---  
  
Not recommended: Avoid image data that show the key PPE items from an uncommon point-of-view or irregular angles.

Sample image data the PPE detector isn't able to process correctly:

![sample image of a PPE item that is shown at too uncommon of an angle to be detected](https://docs.cloud.google.com/static/vision-ai/docs/images/ppe-detector-bad-example2_niclas-moser.png)_Image source:[Niclas Moser](https://unsplash.com/photos/e7L48HNLIxs) on [Unsplash](https://unsplash.com/)._  
---  
  
### Limitations

  * **Resolution** : The recommended maximum input video resolution is 1920 x 1080, and the recommended minimum resolution is 160 x 120.
  * **Minimum detectable object size** : The model ignores any object in the scene that occupy less than 5% of the frame size.
  * **Lighting** : Video lighting should be normal. Extreme brightness or darkness in video data can cause lower detector performance.
  * **PPE item placement** : The PPE model focuses on analyzing if people are properly using PPE items. As a result, if someone is not wearing a PPE item, the model ignores the item.
  * **PPE item type** : The model focuses on construction protective equipment and _not_ medical PPE items. Therefore, the detector might not work well in medical centers or hospitals.
  * **Custom PPE types** : The PPE model doesn't support customer-defined PPE items. The model supports detection of helmets, masks, and gloves.



This list is not meant to be exhaustive, and these limitations and functionality are subject to future product modifications.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
