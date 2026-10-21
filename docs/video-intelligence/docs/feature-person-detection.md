---
url: https://docs.cloud.google.com/video-intelligence/docs/feature-person-detection/
title: Detecting people \u00a0|\u00a0 Video Intelligence API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:54:39.495433+00:00
---

# Detecting people  |  Video Intelligence API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-intelligence/docs/feature-person-detection/

Starting on September 14, 2026, Video Intelligence API is officially deprecated and will no longer be supported. You can continue using Video Intelligence API until September 14, 2027, when it will be shut down. We recommend migrating to [Gemini family of models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Intelligence API ](https://docs.cloud.google.com/video-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/video-intelligence/docs/annotate-video-command-line)



Send feedback 

#  Detecting people Stay organized with collections  Save and categorize content based on your preferences. 

Video Intelligence can detect the presence of humans in a video file and track the bounding box of individual people across the video or video segment.

## Person detection

To detect people in a video, send a video annotation request to Video Intelligence, and include the `PERSON_DETECTION` flag. The annotation request returns details about each person detected in the video, including video segment locations where the person is detected. The annotation request can also provide bounding boxes too.

Additionally, person detection can detect the location of specific body parts as "landmarks," such as `nose`, `left_shoulder`, or `right_shoulder`. Furthermore, person detection can detect other characteristics including clothing color, and clothing type. Specific characteristics that person detection can recognize are provided in the following table.

Characteristic or landmark | Possible values  
---|---  
Body parts | `nose`, `left_eye`, `right_eye`, `left_ear`, `right_ear`, `left_shoulder`, `right_shoulder`, `left_elbow`, `right_elbow`, `left_wrist`, `right_wrist`, `left_hip`, `right_hip`, `left_knee`, `right_knee`, `left_ankle`, `right_ankle`  
Upper clothing color | `UpperCloth:Black`, `UpperCloth:Blue`, `UpperCloth:Brown`, `UpperCloth:Gray`, `UpperCloth:Green`, `UpperCloth:MultiColor`, `UpperCloth:Orange`, `UpperCloth:Purple`, `UpperCloth:Red`, `UpperCloth:White`, `UpperCloth:Yellow`  
Upper clothing type | `UpperCloth:Coat`, `UpperCloth:Dress`, `UpperCloth:Jacket`, `UpperCloth:Shirt`, `UpperCloth:Suit`, `UpperCloth:Sweater`, `UpperCloth:T-Shirt`, `UpperCloth:TankTop`  
Upper clothing pattern | `UpperCloth:Floral`, `UpperCloth:Graphics`, `UpperCloth:Plaid`, `UpperCloth:Plain`, `UpperCloth:Spotted`, `UpperCloth:Striped`  
Sleeve length | `UpperCloth:LongSleeve`, `UpperCloth:ShortSleeve`, `UpperCloth:NoSleeve`  
Lower clothing type | `LowerCloth:LongPants`, `LowerCloth:ShortPants`, `LowerCloth:LongSkirt`, `LowerCloth:ShortSkirt`  
  
Check out the [ Video Intelligence API visualizer](https://zackakil.github.io/video-intelligence-api-visualiser/#Person%20Detection) to see this feature in action.

For an example, see [Person detection](https://docs.cloud.google.com/video-intelligence/docs/people-detection). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
