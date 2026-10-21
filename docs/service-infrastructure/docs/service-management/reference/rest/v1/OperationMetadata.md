---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/OperationMetadata/
title: OperationMetadata \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:30.768812+00:00
---

# OperationMetadata  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/OperationMetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  OperationMetadata Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Step
    * JSON representation



The metadata associated with a long running operation resource.

JSON representation  
---  
      
    
    {
      "resourceNames": [
        string
      ],
      "steps": [
        {
          object ([Step](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/OperationMetadata#Step))
        }
      ],
      "progressPercentage": integer,
      "startTime": string
    }  
  
Fields  
---  
`resourceNames[]` |  `string` The full name of the resources that this operation is directly associated with.  
`steps[]` |  `object (`[Step](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/OperationMetadata#Step)`)` Detailed status information for each step. The order is undetermined.  
`progressPercentage` |  `integer` Percentage of completion of this operation, ranging from 0 to 100.  
`startTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` The start time of the operation.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
  
## Step

Represents the status of one operation step.

JSON representation  
---  
      
    
    {
      "description": string,
      "status": enum ([Status](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/Status))
    }  
  
Fields  
---  
`description` |  `string` The short description of the step.  
`status` |  `enum (`[Status](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/Status)`)` The status code.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
