---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/yaml_listener/EventHandler/
title: google.appengine.api.yaml_listener.EventHandler \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:57:03.754028+00:00
---

# google.appengine.api.yaml_listener.EventHandler  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/yaml_listener/EventHandler/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.yaml_listener.EventHandler Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/yaml_listener.py#L46-L81) Handler interface for parsing YAML files. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type) Implement this interface to define specific YAML event handling class. Implementing classes instances are passed to the constructor of `EventListener` to act as a receiver of YAML parse events.

## Methods

### `Alias`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/yaml_listener.py#L65-L66)
    
    
    Alias(
        event, loader
    )
    

Handles alias event.

### `DocumentEnd`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/yaml_listener.py#L62-L63)
    
    
    DocumentEnd(
        event, loader
    )
    

Handles end of document event.

### `DocumentStart`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/yaml_listener.py#L59-L60)
    
    
    DocumentStart(
        event, loader
    )
    

Handles start of document event.

### `MappingEnd`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/yaml_listener.py#L80-L81)
    
    
    MappingEnd(
        event, loader
    )
    

Handles end of mapping event.

### `MappingStart`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/yaml_listener.py#L77-L78)
    
    
    MappingStart(
        event, loader
    )
    

Handles start of mapping event.

### `Scalar`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/yaml_listener.py#L68-L69)
    
    
    Scalar(
        event, loader
    )
    

Handles scalar event.

### `SequenceEnd`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/yaml_listener.py#L74-L75)
    
    
    SequenceEnd(
        event, loader
    )
    

Handles end of sequence event.

### `SequenceStart`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/yaml_listener.py#L71-L72)
    
    
    SequenceStart(
        event, loader
    )
    

Handles start of sequence event.

### `StreamEnd`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/yaml_listener.py#L56-L57)
    
    
    StreamEnd(
        event, loader
    )
    

Handles end of stream event.

### `StreamStart`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/yaml_listener.py#L53-L54)
    
    
    StreamStart(
        event, loader
    )
    

Handles start of stream event. Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2025-06-16 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
