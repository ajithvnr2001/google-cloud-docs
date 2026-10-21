---
url: https://docs.cloud.google.com/video-intelligence/docs/feature-label-detection/
title: Analyze videos for labels \u00a0|\u00a0 Video Intelligence API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:29:57.939597+00:00
---

# Analyze videos for labels  |  Video Intelligence API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-intelligence/docs/feature-label-detection/

Starting on September 14, 2026, Video Intelligence API is officially deprecated and will no longer be supported. You can continue using Video Intelligence API until September 14, 2027, when it will be shut down. We recommend migrating to [Gemini family of models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Intelligence API ](https://docs.cloud.google.com/video-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/video-intelligence/docs/annotate-video-command-line)



Send feedback 

#  Analyze videos for labels Stay organized with collections  Save and categorize content based on your preferences. 

The Video Intelligence API can identify entities shown in video footage using the [LABEL_DETECTION](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos/annotate#feature) feature and annotate these entities with labels (tags). This feature identifies objects, locations, activities, animal species, products, and more.

Label detection differs from [Object tracking](https://docs.cloud.google.com/video-intelligence/docs/object-tracking). Unlike object tracking, label detection provides labels for the entire frame (without bounding boxes).

For example, for a video of a train at a crossing, the Video Intelligence API returns labels such as "train", "transportation", "railroad crossing", and so on. Each label includes a time segment with the time offset (timestamp) for the entity's appearance from the beginning of the video. Each annotation also contains additional information including an entity id that you can use to find more information about the entity in the [Google Knowledge Graph Search API](https://developers.google.com/knowledge-graph/).

Each entity returned can also include associated category entities in the `categoryEntities` field. For example the "Terrier" entity label has a category of "Dog". Category entities have a hierarchy. For example, the "Dog" category is a child of the "Mammal" category in the hierarchy. For a list of the common category entities that the Video Intelligence uses, see [entry-level-categories.json](https://docs.cloud.google.com/static/video-intelligence/docs/entry-level-categories.json).

The analysis can be compartmentalized as follows: 

  * Segment level:  
User-selected segments of a video can be specified for analysis by stipulating beginning and ending timestamps for the purposes of annotation (see [VideoSegment](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos/annotate#videosegment)). Entities are then identified and labeled within each segment. If no segments are specified, the whole video is treated as one segment. 

  * Shot level:   
Shots (also known as a _scene_) are automatically detected within every segment (or video). Entities are then identified and labeled within each scene. For details, see Shot change detection
  * Frame level:   
Entities are identified and labeled within each frame (with one frame per second sampling). 



To detect labels in a video, call the [`annotate`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos/annotate) method and specify [`LABEL_DETECTION`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos#Feature) in the `features` field.

See [Analyzing Videos for Labels](https://docs.cloud.google.com/video-intelligence/docs/analyze-labels) and [Label Detection Tutorial](https://docs.cloud.google.com/video-intelligence/docs/label-tutorial).

# Video Intelligence API Visualizer

Check out the [ Video Intelligence API visualizer](https://zackakil.github.io/video-intelligence-api-visualiser/#Label%20Detection) to see this feature in action.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
