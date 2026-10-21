---
url: https://docs.cloud.google.com/vision-ai/docs/person-vehicle-model/
title: Person/vehicle detector guide \u00a0|\u00a0 Agent Platform Vision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:46.472562+00:00
---

# Person/vehicle detector guide  |  Agent Platform Vision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/person-vehicle-model/

Vertex AI Vision is deprecated as of June 15, 2026 and reaches End of Life on September 30, 2026. To migrate, see the [Cloud Vision API](https://docs.cloud.google.com/vision/docs), [Agent Platform serverless training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview), or [Agent Platform models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/vision-ai/docs/cloud-environment)



Send feedback 

#  Person/vehicle detector guide Stay organized with collections  Save and categorize content based on your preferences. 

![person vehicle detector model card in console](https://docs.cloud.google.com/static/vision-ai/docs/images/person-vehicle-detector-card.png)

The **Person/vehicle detector** model lets you detect and count people or vehicles* in video frames. The model accepts a video stream as input and outputs a [protocol buffer](https://developers.google.com/protocol-buffers/docs/overview) with the count of detected people and vehicles detected in each frame. The model runs at six FPS.

* Cars, buses, trucks, bicycles, motorcycles and ambulances.

## Model output

The Person/vehicle detector model shows the number of people and vehicles detected in the current processed frame. Below is the [protocol buffer](https://developers.google.com/protocol-buffers/docs/overview) definition of the model output. The frequency of the output stream is constant: one frame per second.
    
    
    // The prediction result proto for Person/Vehicle Detection.
    message OccupancyCountingPredictionResult {
    
     // Current timestamp.
     google.protobuf.Timestamp current_time = 1;
    
     // The entity info for annotations from the model.
     message Entity {
       // Label id.
       int64 label_id = 1;
       // Human readable string of the label.
       string label_string = 2;
     }
    
     // Identified box contains location and the entity of the object.
     message IdentifiedBox {
       // An unique id for this box.
       int64 box_id = 1;
       // Bounding Box in the normalized coordinates.
       message NormalizedBoundingBox {
         // Min in x coordinate.
         float xmin = 1;
         // Min in y coordinate.
         float ymin = 2;
         // Width of the bounding box.
         float width = 3;
         // Height of the bounding box.
         float height = 4;
       }
       // Bounding Box in the normalized coordinates.
       NormalizedBoundingBox normalized_bounding_box = 2;
       // Confidence score associated with this box.
       float score = 3;
       // Entity of this box.
       Entity entity = 4;
     }
    
     // A list of identified boxes.
     repeated IdentifiedBox identified_boxes = 2;
    
     // The statistics info for annotations from the model.
     message Stats {
       // The object info and count for annotations from the model.
       message ObjectCount {
         // Entity of this object.
         Entity entity = 1;
         // Count of the object.
         int32 count = 2;
       }
       // Counts of the full frame.
       repeated ObjectCount full_frame_count = 1;
     }
    
     // Detection statistics.
     Stats stats = 3;
    }

## Best practices and limitations

  * Avoid unusual camera viewpoints (for example, a top-down view) where people and vehicles appear differently from a standard or common view of them. The detection quality can be largely impacted by unusual views.
  * Ensure that people and vehicles are fully or mostly visible. The detection quality can be affected by partial occlusion by other objects.
  * The Person/vehicle detector has a minimal detectable object size. This size is approximately 2% with respect to the size of the camera view. Ensure that the target people and vehicles are not too far away from the camera. These key objects' viewable sizes must be sufficiently large.
  * Areas of interest must have proper lighting.
  * Ensure the video source camera lens is clean.
  * Ensure entities (other than people or cars) don't obstruct any part of the camera's field of view.
  * The following factors might degrade the model's performance. Consider these factors when you source data: 
    * Poor lighting conditions.
    * Crowdedness and object occlusions.
    * Uncommon viewpoints.
    * Small object sizes.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
