---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.DataSchemaDetails.DataType
title: Class DataType (0.5.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:33:55.610030+00:00
---

# Class DataType (0.5.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.DataSchemaDetails.DataType

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DataType (0.5.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.3 (latest)  0.5.2  0.4.0  0.3.0  0.2.0  0.1.10 
    
    
    DataType(value)

Data type of the annotation.
    
    
        - DataSchema.SearchStrategy.NO_SEARCH,
        - DataSchema.SearchStrategy.EXACT_SEARCH. Supports query by
          IntRangeArray.
    FLOAT (2):
        Float type. Allowed search strategies:
    
        - DataSchema.SearchStrategy.NO_SEARCH,
        - DataSchema.SearchStrategy.EXACT_SEARCH. Supports query by
          FloatRangeArray.
    STRING (3):
        String type. Allowed search strategies:
    
        - DataSchema.SearchStrategy.NO_SEARCH,
        - DataSchema.SearchStrategy.EXACT_SEARCH,
        - DataSchema.SearchStrategy.SMART_SEARCH.
    DATETIME (5):
        Supported formats: %Y-%m-%dT%H:%M:%E\ *S%E*\ z
        (absl::RFC3339_full) %Y-%m-%dT%H:%M:%E\ *S
        %Y-%m-%dT%H:%M%E*\ z %Y-%m-%dT%H:%M %Y-%m-%dT%H%E\ *z
        %Y-%m-%dT%H %Y-%m-%d%E*\ z %Y-%m-%d %Y-%m %Y Allowed search
        strategies:
    
        - DataSchema.SearchStrategy.NO_SEARCH,
        - DataSchema.SearchStrategy.EXACT_SEARCH. Supports query by
          DateTimeRangeArray.
    GEO_COORDINATE (7):
        Geo coordinate type. Allowed search strategies:
    
        - DataSchema.SearchStrategy.NO_SEARCH,
        - DataSchema.SearchStrategy.EXACT_SEARCH. Supports query by
          GeoLocationArray.
    PROTO_ANY (8):
        Type to pass any proto as available in annotations.proto.
        Only use internally. Available proto types and its
        corresponding search behavior:
    
        - ImageObjectDetectionPredictionResult, allows SMART_SEARCH
          on display_names and NO_SEARCH.
        - ClassificationPredictionResult, allows SMART_SEARCH on
          display_names and NO_SEARCH.
        - ImageSegmentationPredictionResult, allows NO_SEARCH.
        - VideoActionRecognitionPredictionResult, allows
          SMART_SEARCH on display_name and NO_SEARCH.
        - VideoObjectTrackingPredictionResult, allows SMART_SEARCH
          on display_name and NO_SEARCH.
        - VideoClassificationPredictionResult, allows SMART_SEARCH
          on display_name and NO_SEARCH.
        - OccupancyCountingPredictionResult, allows EXACT_SEARCH on
          stats.full_frame_count.count and NO_SEARCH.
        - ObjectDetectionPredictionResult, allows SMART_SEARCH on
          identified_boxes.entity.label_string and NO_SEARCH.
    BOOLEAN (9):
        Boolean type. Allowed search strategies:
    
        - DataSchema.SearchStrategy.NO_SEARCH,
        - DataSchema.SearchStrategy.EXACT_SEARCH.
    LIST (10):
        List type.
    
        - Each element in the list must be of the exact same data
          schema; otherwise, they are invalid arguments.
        - List level cannot set search strategy. Leaf node level can
          do.
        - Elements cannot be another list (no list of list).
        - Elements can be CUSTOMIZED_STRUCT, and max number of
          layers is 10.
    CUSTOMIZED_STRUCT (6):
        Struct type.
    
        - SearchStrategy:
    
          - Data Schema that's CUSTOMIZED_STRUCT cannot set search
            strategy.
          - Leaf-node elements allow setting search strategy based
            on element's SearchStrategy restriction.
    
        - Nested layer restrictions:
    
          - Data Schema that's CUSTOMIZED_STRUCT allows its fields
            to be of CUSTOMIZED_STRUCT as well, but the overall
            layers restriction is 10.
    

## Enums  
  
---  
**Name** | **Description**  
`DATA_TYPE_UNSPECIFIED` | Unspecified type.  
`INTEGER` | Integer type. Allowed search strategies:  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
