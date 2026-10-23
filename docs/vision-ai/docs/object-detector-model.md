---
url: https://docs.cloud.google.com/vision-ai/docs/object-detector-model/
title: Object detector guide \u00a0|\u00a0 Agent Platform Vision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:16.971368+00:00
---

# Object detector guide  |  Agent Platform Vision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/object-detector-model/

Vertex AI Vision is deprecated as of June 15, 2026 and reaches End of Life on September 30, 2026. To migrate, see the [Cloud Vision API](https://docs.cloud.google.com/vision/docs), [Agent Platform serverless training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview), or [Agent Platform models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/vision-ai/docs/cloud-environment)



Send feedback 

#  Object detector guide Stay organized with collections  Save and categorize content based on your preferences. 

![Icon depicting the Object detector model card.](https://docs.cloud.google.com/static/vision-ai/docs/images/object-detector-card.png)

The **Object detector model** can identify and locate more than 500 types of objects in a video. The model accepts a video stream as input and outputs a [protocol buffer](https://developers.google.com/protocol-buffers) with the detection results to BigQuery. The model runs at one FPS. When you create an app that uses the object detector model, you must direct model output to a BigQuery connector to view prediction output.

## Object detector model app specifications

Use the following instructions to create an object detector model in the Google Cloud console.

###  Console 

**Create an app in the Google Cloud console**

  1. To create an object detector app, follow instructions in [Build an application](https://docs.cloud.google.com/vision-ai/docs/build-app).

[Go to the Applications tab](https://console.cloud.google.com/ai/vision-ai/applications)




**Add an object detector model**

  1. When you add model nodes, select the **Object detector** from the list of pre-trained models.



**Add a BigQuery connector**

  1. To use the output, connect the app to a **BigQuery** connector.

For information about using the **BigQuery** connector, see [Connect and store data to BigQuery](https://docs.cloud.google.com/vision-ai/docs/connect-bigquery). For BigQuery pricing information, see the [BigQuery pricing](https://cloud.google.com/bigquery/pricing) page.




**View output results in BigQuery**

After the model outputs data to BigQuery, view output annotations in the BigQuery dashboard.

If you didn't specify a BigQuery path, you can view the system-created path in the Agent Platform Vision schema**Studio** page.

  1. In the Google Cloud console, open the BigQuery page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. Select arrow_drop_down**Expand** next to the target project, dataset name, and application name.

![Select app table in BigQuery.](https://docs.cloud.google.com/static/vision-ai/docs/images/bq-view-app-table.png)

  3. In the table detail view, click **Preview**. View results in the **annotation** column. For a description of the output format, see model output.




The application stores results in chronological order. The oldest results are the beginning of the table, while the most recent results are added to the end of the table. To check the latest results, click the page number to go to the last table page.

## Model output

The model outputs bounding boxes, their object labels, and confidence scores for each video frame. The output also contains a timestamp. The rate of the output stream is one frame per second.

In the [protocol buffer](https://developers.google.com/protocol-buffers) output example that follows, note the following:

  * Timestamp - The timestamp corresponds to the time for this inference result.
  * Identified boxes - The main detection result that includes box identity, bounding box information, confidence score, and object prediction.



### Sample annotation output JSON object
    
    
    {
      "currentTime": "2022-11-09T02:18:54.777154048Z",
      "identifiedBoxes": [
        {
          "boxId":"0",
          "normalizedBoundingBox": {
            "xmin": 0.6963465,
            "ymin": 0.23144785,
            "width": 0.23944569,
            "height": 0.3544306
          },
          "confidenceScore": 0.49874997,
          "entity": {
            "labelId": "0",
            "labelString": "Houseplant"
          }
        }
      ]
    }
    

### Protocol buffer definition
    
    
    // The prediction result protocol buffer for object detection
    message ObjectDetectionPredictionResult {
      // Current timestamp
      protobuf.Timestamp timestamp = 1;
    
      // The entity information for annotations from object detection prediction
      // results
      message Entity {
        // Label id
        int64 label_id = 1;
    
        // The human-readable label string
        string label_string = 2;
      }
    
      // The identified box contains the location and the entity of the object
      message IdentifiedBox {
        // An unique id for this box
        int64 box_id = 1;
    
        // Bounding Box in normalized coordinates [0,1]
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
        // Bounding Box in the normalized coordinates
        NormalizedBoundingBox normalized_bounding_box = 2;
    
        // Confidence score associated with this bounding box
        float confidence_score = 3;
    
        // Entity of this box
        Entity entity = 4;
      }
      // A list of identified boxes
      repeated IdentifiedBox identified_boxes = 2;
    }
    

## Best practices and limitations

To get the best results when you use the object detector, consider the following when you source data and use the model.

### Source data recommendations

Recommended: Make sure the objects in the picture are clear and are not covered or largely obscured by other objects.

Sample image data the object detector is able to process correctly:

![Clearly visible living room objects.](https://docs.cloud.google.com/static/vision-ai/docs/images/object-detector-good-example2_spacejoy.jpg)_Image source:[Spacejoy](https://unsplash.com/photos/umAXneH4GhA) on [Unsplash](https://unsplash.com/)._  
---  
  
Sending the model this image data returns the following object detection information*:

* The annotations in the following image are for illustrative purposes only. The bounding boxes, labels, and confidence scores are manually drawn and not added by the model or any Google Cloud console tool.

![Living room objects with bounding boxes, labels, and confidence score annotations.](https://docs.cloud.google.com/static/vision-ai/docs/images/object-detector-good-example2_spacejoy_ANNOTATED.png)_Image source:[Spacejoy](https://unsplash.com/photos/umAXneH4GhA) on [Unsplash](https://unsplash.com/) (annotations manually added)._

Not recommended: Avoid image data where the key object items are too small in the frame.

Sample image data the object detector isn't able to process correctly:

![Object items that are too small in the frame to be detected.](https://docs.cloud.google.com/static/vision-ai/docs/images/object-detector-bad-example1_bernard-hermant2.jpg)_Image source:[Bernard Hermant](https://unsplash.com/photos/nHRXNv2qeDE) on [Unsplash](https://unsplash.com/) (image cropped)._  
---  
  
Not recommended: Avoid image data that show the key object items partially or fully covered by other objects.

Sample image data the object detector isn't able to process correctly:

![Object items that are partially covered by other objects in the foreground.](https://docs.cloud.google.com/static/vision-ai/docs/images/object-detector-bad-example2_sahin-sezer-dincer-.jpg)_Image source:[Şahin Sezer Dinçer](https://unsplash.com/photos/XuGA_JrIPZU) on [Unsplash](https://unsplash.com/)._  
---  
  
### Limitations

  * **Video resolution** : The recommended maximum input video resolution is 1920 x 1080, and the recommended minimum resolution is 160 x 120.
  * **Lighting** : The model performance is sensitive to lighting conditions. Extreme brightness or darkness might lead to lower detection quality.
  * **Object size** : The object detector has a minimal detectable object size. Make sure the target objects are sufficiently large and visible in your video data.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
