---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/FeatureValueDestination/
title: FeatureValueDestination \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:29:47.335613+00:00
---

# FeatureValueDestination  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/FeatureValueDestination/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  FeatureValueDestination Stay organized with collections  Save and categorize content based on your preferences. 

A destination location for feature values and format.

Fields  
  
`destination` `Union type`  
  
The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`bigqueryDestination` `object (`[BigQueryDestination](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/BigQueryDestination)`)` Output in BigQuery format. `[BigQueryDestination.output_uri](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/BigQueryDestination#FIELDS.output_uri)` in `[FeatureValueDestination.bigquery_destination](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/FeatureValueDestination#FIELDS.bigquery_destination)` must refer to a table. | `tfrecordDestination` `object (`[TFRecordDestination](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/FeatureValueDestination#TFRecordDestination)`)` Output in TFRecord format.Below are the mapping from feature value type in Featurestore to feature value type in TFRecord:
    
    
    value type in Featurestore                 | value type in TFRecord
    DOUBLE, DOUBLE_ARRAY                       | FLOAT_LIST
    INT64, INT64_ARRAY                         | INT64_LIST
    STRING, STRING_ARRAY, BYTES                | BYTES_LIST
    true -> byte_string("true"), false -> byte_string("false")
    BOOL, BOOL_ARRAY (true, false)             | BYTES_LIST
    

| `csvDestination` `object (`[CsvDestination](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/FeatureValueDestination#CsvDestination)`)` Output in CSV format. Array feature value types are not allowed in CSV format. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
    
      // destination
      "bigqueryDestination": {
        object ([BigQueryDestination](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/BigQueryDestination))
      },
      "tfrecordDestination": {
        object ([TFRecordDestination](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/FeatureValueDestination#TFRecordDestination))
      },
      "csvDestination": {
        object ([CsvDestination](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/FeatureValueDestination#CsvDestination))
      }
      // Union type
    }  
  
## TFRecordDestination

The storage details for TFRecord output content.

Fields  
  
`gcsDestination` `object (`[GcsDestination](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/CustomJobSpec#GcsDestination)`)` Required. Google Cloud Storage location. | JSON representation  
---  
      
    
    {
      "gcsDestination": {
        object ([GcsDestination](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/CustomJobSpec#GcsDestination))
      }
    }  
  
## CsvDestination

The storage details for CSV output content.

Fields  
  
`gcsDestination` `object (`[GcsDestination](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/CustomJobSpec#GcsDestination)`)` Required. Google Cloud Storage location. | JSON representation  
---  
      
    
    {
      "gcsDestination": {
        object ([GcsDestination](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/CustomJobSpec#GcsDestination))
      }
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
