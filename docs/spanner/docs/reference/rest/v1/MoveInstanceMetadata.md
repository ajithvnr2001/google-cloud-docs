---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/MoveInstanceMetadata/
title: MoveInstanceMetadata \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:19.530276+00:00
---

# MoveInstanceMetadata  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/MoveInstanceMetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  MoveInstanceMetadata Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Metadata type for the operation returned by `[instances.move](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances/move#google.spanner.admin.instance.v1.InstanceAdmin.MoveInstance)`.

JSON representation  
---  
      
    
    {
      "targetConfig": string,
      "progress": {
        object (OperationProgress)
      },
      "cancelTime": string
    }  
  
Fields  
---  
`targetConfig` |  `string` The target instance configuration where to move the instance. Values are of the form `projects/<project>/instanceConfigs/<config>`.  
`progress` |  `object (`OperationProgress`)` The progress of the `[instances.move](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances/move#google.spanner.admin.instance.v1.InstanceAdmin.MoveInstance)` operation. `progressPercent` is reset when cancellation is requested.  
`cancelTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time at which this operation was cancelled.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-04 UTC."],[],[]] 
