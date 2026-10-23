---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.datasets/export/
title: Method: datasets.export \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:58:48.102915+00:00
---

# Method: datasets.export  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.datasets/export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: datasets.export Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.datasets.export

Exports data from a Dataset.

### Endpoint

post  `https://{service-endpoint}/v1beta1/{name}:export`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`name` `string` Required. The name of the Dataset resource. Format: `projects/{project}/locations/{location}/datasets/{dataset}`

### Request body

The request body contains data with the following structure: | Fields  
  
`exportConfig` `object (`[ExportDataConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.datasets/export#ExportDataConfig)`)` Required. The desired output location.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `aiplatform.datasets.export`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## ExportDataConfig

Describes what part of the Dataset is to be exported, the destination of the export and how to export. | Fields  
  
`annotationsFilter` `string` An expression for filtering what part of the Dataset is to be exported. Only Annotations that match this filter will be exported. The filter syntax is the same as in `[ListAnnotations](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.datasets.dataItems.annotations/list#google.cloud.aiplatform.v1beta1.DatasetService.ListAnnotations)`. | `destination` `Union type`  
  
The destination of the output. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`gcsDestination` `object (`GcsDestination`)` The Google Cloud Storage location where the output is to be written to. In the given directory a new directory will be created with name: `export-data-<dataset-display-name>-<timestamp-of-export-call>` where timestamp is in YYYY-MM-DDThh:mm:ss.sssZ ISO-8601 format. All export output will be written into that directory. Inside that directory, annotations with the same schema will be grouped into sub directories which are named with the corresponding annotations' schema title. Inside these sub directories, a schema.yaml will be created to describe the output format. End of mutually exclusive fields. | `split` `Union type`  
  
The instructions how the export data should be split between the training, validation and test sets. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`fractionSplit` `object (`[ExportFractionSplit](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.datasets/export#ExportFractionSplit)`)` Split based on fractions defining the size of each set. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
      "annotationsFilter": string,
    
      // destination
      "gcsDestination": {
        object (GcsDestination)
      }
      // Union type
    
      // split
      "fractionSplit": {
        object ([ExportFractionSplit](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.datasets/export#ExportFractionSplit))
      }
      // Union type
    }  
  
## ExportFractionSplit

Assigns the input data to training, validation, and test sets as per the given fractions. Any of `trainingFraction`, `validationFraction` and `testFraction` may optionally be provided, they must sum to up to 1. If the provided ones sum to less than 1, the remainder is assigned to sets as decided by Agent Platform. If none of the fractions are set, by default roughly 80% of data is used for training, 10% for validation, and 10% for test.

Fields  
  
`trainingFraction` `number` The fraction of the input data that is to be used to train the Model. | `validationFraction` `number` The fraction of the input data that is to be used to validate the Model. | `testFraction` `number` The fraction of the input data that is to be used to evaluate the Model. | JSON representation  
---  
      
    
    {
      "trainingFraction": number,
      "validationFraction": number,
      "testFraction": number
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
