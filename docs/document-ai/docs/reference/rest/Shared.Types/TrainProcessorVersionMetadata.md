---
url: https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/TrainProcessorVersionMetadata/
title: TrainProcessorVersionMetadata \u00a0|\u00a0 Document AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:15:17.296466+00:00
---

# TrainProcessorVersionMetadata  |  Document AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/TrainProcessorVersionMetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI ](https://docs.cloud.google.com/document-ai/docs)
  * [ Reference ](https://docs.cloud.google.com/document-ai/docs/reference)



Send feedback 

#  TrainProcessorVersionMetadata Stay organized with collections  Save and categorize content based on your preferences. 

The metadata that represents a processor version being created.

JSON representation  
---  
      
    
    {
      "commonMetadata": {
        object ([CommonOperationMetadata](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/CommonOperationMetadata))
      },
      "trainingDatasetValidation": {
        object ([DatasetValidation](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/TrainProcessorVersionMetadata#DatasetValidation))
      },
      "testDatasetValidation": {
        object ([DatasetValidation](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/TrainProcessorVersionMetadata#DatasetValidation))
      }
    }  
  
Fields  
---  
`commonMetadata` |  `object (`[CommonOperationMetadata](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/CommonOperationMetadata)`)` The basic metadata of the long-running operation.  
`trainingDatasetValidation` |  `object (`[DatasetValidation](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/TrainProcessorVersionMetadata#DatasetValidation)`)` The training dataset validation information.  
`testDatasetValidation` |  `object (`[DatasetValidation](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/TrainProcessorVersionMetadata#DatasetValidation)`)` The test dataset validation information.  
  
## DatasetValidation

The dataset validation information. This includes any and all errors with documents and the dataset.

JSON representation  
---  
      
    
    {
      "documentErrorCount": integer,
      "datasetErrorCount": integer,
      "documentErrors": [
        {
          object ([Status](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/Status))
        }
      ],
      "datasetErrors": [
        {
          object ([Status](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/Status))
        }
      ]
    }  
  
Fields  
---  
`documentErrorCount` |  `integer` The total number of document errors.  
`datasetErrorCount` |  `integer` The total number of dataset errors.  
`documentErrors[]` |  `object (`[Status](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/Status)`)` Error information pertaining to specific documents. A maximum of 10 document errors will be returned. Any document with errors will not be used throughout training.  
`datasetErrors[]` |  `object (`[Status](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/Status)`)` Error information for the dataset as a whole. A maximum of 10 dataset errors will be returned. A single dataset error is terminal for training.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
