---
url: https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.processorTypes
title: REST Resource: projects.locations.processorTypes \u00a0|\u00a0 Document AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:49:19.025687+00:00
---

# REST Resource: projects.locations.processorTypes  |  Document AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.processorTypes

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI ](https://docs.cloud.google.com/document-ai/docs)
  * [ Reference ](https://docs.cloud.google.com/document-ai/docs/reference)



Send feedback 

#  REST Resource: projects.locations.processorTypes Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: ProcessorType

A processor type is responsible for performing a certain document understanding task on a certain type of document.

JSON representation  
---  
      
    
    {
      "name": string,
      "type": string,
      "category": string,
      "availableLocations": [
        {
          object ([LocationInfo](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.processorTypes#LocationInfo))
        }
      ],
      "allowCreation": boolean,
      "launchStage": enum ([LaunchStage](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/LaunchStage)),
      "sampleDocumentUris": [
        string
      ]
    }  
  
Fields  
---  
`name` |  `string` The resource name of the processor type. Format: `projects/{project}/processorTypes/{processor_type}`  
`type` |  `string` The processor type, such as: `OCR_PROCESSOR`, `INVOICE_PROCESSOR`.  
`category` |  `string` The processor category, used by UI to group processor types.  
`availableLocations[]` |  `object (`[LocationInfo](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.processorTypes#LocationInfo)`)` The locations in which this processor is available.  
`allowCreation` |  `boolean` Whether the processor type allows creation. If true, users can create a processor of this processor type. Otherwise, users need to request access.  
`launchStage` |  `enum (`[LaunchStage](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/LaunchStage)`)` Launch stage of the processor type  
`sampleDocumentUris[]` |  `string` A set of Cloud Storage URIs of sample documents for this processor.  
  
## LocationInfo

The location information about where the processor is available.

JSON representation  
---  
      
    
    {
      "locationId": string
    }  
  
Fields  
---  
`locationId` |  `string` The location ID. For supported locations, refer to [regional and multi-regional support](https://docs.cloud.google.com/document-ai/docs/regions).  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.processorTypes/get)`

|  Gets a processor type detail.  
  
### `[list](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.processorTypes/list)`

|  Lists the processor types that exist.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
