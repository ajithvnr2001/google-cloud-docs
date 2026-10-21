---
url: https://docs.cloud.google.com/vision-ai/docs/occupancy-analytics-model/
title: Occupancy analytics guide \u00a0|\u00a0 Agent Platform Vision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:27:05.495937+00:00
---

# Occupancy analytics guide  |  Agent Platform Vision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/occupancy-analytics-model/

Vertex AI Vision is deprecated as of June 15, 2026 and reaches End of Life on September 30, 2026. To migrate, see the [Cloud Vision API](https://docs.cloud.google.com/vision/docs), [Agent Platform serverless training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview), or [Agent Platform models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/vision-ai/docs/cloud-environment)



Send feedback 

#  Occupancy analytics guide Stay organized with collections  Save and categorize content based on your preferences. 

![Icon depicting the Occupancy analytics model card.](https://docs.cloud.google.com/static/vision-ai/docs/images/occupancy-analytics-card.png)

The **Occupancy analytics** model lets you count people or vehicles given specific inputs you add in video frames. Compared with the Person Vehicle Detector model, advanced features are provided in the Occupancy Analytics model. These features are active zones counting, line crossing counting, and dwelling detection.

  * Active zones let users count people or vehicles in specific user-defined zones.
  * Line crossing provides the ability to count the direction in which an object crosses a particular line.
  * Dwell time detection builds on active zones and provides the ability to detect whether or not objects have remained in a zone for a minimal amount of time.



The model accepts a video stream as input and outputs a [protocol buffer](https://developers.google.com/protocol-buffers/docs/overview) with a count of detected people and vehicles in each frame. The model runs at six FPS.

## Use case: Smart city traffic analytics

The following video shows how you can use Gemini Enterprise Agent Platform Vision to create, build, and deploy an occupancy analytics application.

This application uses a model that counts cars that cross lines in intersections that the user specifies in the Google Cloud console. Additionally, the application uses a person blur model to protect the identity of anyone that appears in the video feed sources.

The application sends analyzed data to a Gemini Enterprise Agent Platform Vision's Media Warehouse for media storage, and also to BigQuery to store structured data in a table. The warehouse lets you search stored data on criteria from the models, such as number of vehicles or people. The table data in BigQuery lets you query the data for analytic information.

## Model output

Person Vehicle Detection shows the number of people and vehicles detected in the current processed frame. The type of count is based on user-provided annotation input. The raw detection and tracking results are also in the output. The following is the [protocol buffer](https://developers.google.com/protocol-buffers/docs/overview) definition of the processor output. The frequency of the output stream is constant: three frames per second.
    
    
    // The prediction result proto for Person/Vehicle Detection.
    message OccupancyCountingPredictionResult {
    
     // Current timestamp.
     google.protobuf.Timestamp current_time = 1;
    
     // The entity info for annotations from the processor.
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
    
       // A unique id to identify a track. It must be consistent across frames.
       // It only exists if tracking is enabled.
       int64 track_id = 5;
     }
    
     // A list of identified boxes.
     repeated IdentifiedBox identified_boxes = 2;
    
     // The statistics info for annotations from the processor.
     message Stats {
       // The object info and count for annotations from the processor.
       message ObjectCount {
         // Entity of this object.
         Entity entity = 1;
         // Count of the object.
         int32 count = 2;
       }
    
       // Counts of the full frame.
       repeated ObjectCount full_frame_count = 1;
    
       // Message for Crossing line count.
       message CrossingLineCount {
         // Line annotation from the user.
         StreamAnnotation annotation = 1;
         // The direction that follows the right hand rule.
         repeated ObjectCount positive_direction_counts = 2;
         // The direction that is opposite to the right hand rule.
         repeated ObjectCount negative_direction_counts = 3;
       }
    
       // Crossing line counts.
       repeated CrossingLineCount crossing_line_counts = 2;
    
       // Message for the active zone count.
       message ActiveZoneCount {
         // Active zone annotation from the user.
         StreamAnnotation annotation = 1;
         // Counts in the zone.
         repeated ObjectCount counts = 2;
       }
    
       // Active zone counts.
       repeated ActiveZoneCount active_zone_counts = 3;
     }
    
     // Detection statistics.
     Stats stats = 3;
    
     // The track info for annotations from the processor.
     message TrackInfo {
       // A unique id to identify a track. It must be consistent across frames.
       string track_id = 1;
       // Start timestamp of this track.
       google.protobuf.Timestamp start_time = 2;
     }
    
     // The dwell time info for annotations from the processor.
     message DwellTimeInfo {
       // A unique id to identify a track. It must be consistent across frames.
       string track_id = 1;
       // The unique id for the zone in which the object is dwelling/waiting.
       string zone_id = 2;
       // The beginning time when a dwelling object has been identified in a zone.
       google.protobuf.Timestamp dwell_start_time = 3;
       // The end time when a dwelling object has exited in a zone.
       google.protobuf.Timestamp dwell_end_time = 4;
     }
    
     // Track related information. All the tracks that are live at this timestamp.
     // It only exists if tracking is enabled.
     repeated TrackInfo track_info = 4;
    
     // Dwell time related information. All the tracks that are live in a given
     // zone with a start and end dwell time timestamp
     repeated DwellTimeInfo dwell_time_info = 5;
    }

## Best practices and limitations

  * Avoid unusual camera viewpoints (for example, a top-down view) where people and vehicles appear differently from a standard or common view of them. The detection quality can be largely impacted by unusual views.
  * Ensure that people and vehicles are fully or mostly visible. The detection quality can be affected by partial occlusion by other objects.
  * The person vehicle detector has a minimal detectable object size. This size is approximately 2% with respect to the size of the camera view. Ensure that the target people and vehicles aren't too far away from the camera. These key objects' viewable sizes must be sufficiently large.
  * Areas of interest must have proper lighting.
  * Ensure the video source camera lens is clean.
  * Ensure entities (other than people or cars) don't obstruct any part of the camera's field of view.
  * The following factors might degrade the model's performance. Consider these factors when you source data: 
    * Poor lighting conditions.
    * Crowdedness and object occlusions.
    * Uncommon or less common viewpoints.
    * Small object sizes.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
