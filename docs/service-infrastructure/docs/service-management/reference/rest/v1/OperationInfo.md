---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/OperationInfo/
title: OperationInfo \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:30.470398+00:00
---

# OperationInfo  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/OperationInfo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  OperationInfo Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



A message representing the message types used by a long-running operation.

Example:
    
    
    rpc Export(ExportRequest) returns (google.longrunning.Operation) {
      option (google.longrunning.operation_info) = {
        responseType: "ExportResponse"
        metadataType: "ExportMetadata"
      };
    }
    

JSON representation  
---  
      
    
    {
      "responseType": string,
      "metadataType": string
    }  
  
Fields  
---  
`responseType` |  `string` Required. The message name of the primary return type for this long-running operation. This type will be used to deserialize the LRO's response.If the response is in a different package from the rpc, a fully-qualified message name must be used (e.g. `google.protobuf.Struct`).Note: Altering this value constitutes a breaking change.  
`metadataType` |  `string` Required. The message name of the metadata type for this long-running operation.If the response is in a different package from the rpc, a fully-qualified message name must be used (e.g. `google.protobuf.Struct`).Note: Altering this value constitutes a breaking change.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
