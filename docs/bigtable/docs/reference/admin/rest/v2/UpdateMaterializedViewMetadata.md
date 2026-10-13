---
url: https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/UpdateMaterializedViewMetadata/
title: UpdateMaterializedViewMetadata \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:52:10.895333+00:00
---

# UpdateMaterializedViewMetadata  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/UpdateMaterializedViewMetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Reference ](https://docs.cloud.google.com/bigtable/docs/apis)



Send feedback 

#  UpdateMaterializedViewMetadata Stay organized with collections  Save and categorize content based on your preferences. 

The metadata for the Operation returned by materializedViews.patch.

JSON representation  
---  
      
    
    {
      "originalRequest": {
        object ([UpdateMaterializedViewRequest](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/UpdateMaterializedViewMetadata#UpdateMaterializedViewRequest))
      },
      "startTime": string,
      "endTime": string,
      "requestTime": string,
      "finishTime": string
    }  
  
Fields  
---  
`originalRequest` |  `object (`[UpdateMaterializedViewRequest](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/UpdateMaterializedViewMetadata#UpdateMaterializedViewRequest)`)` The request that prompted the initiation of this materializedViews.patch operation.  
`startTime  
**(deprecated)**` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` This item is deprecated!The time at which this operation was started. DEPRECATED: Use requestTime instead.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime  
**(deprecated)**` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` This item is deprecated!If set, the time at which this operation finished or was canceled. DEPRECATED: Use finishTime instead.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`requestTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time at which the original request was received.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`finishTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time at which the operation failed or was completed successfully.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## UpdateMaterializedViewRequest

Request message for BigtableInstanceAdmin.UpdateMaterializedView.

JSON representation  
---  
      
    
    {
      "materializedView": {
        object ([MaterializedView](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.materializedViews#MaterializedView))
      },
      "updateMask": string
    }  
  
Fields  
---  
`materializedView` |  `object (`[MaterializedView](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.materializedViews#MaterializedView)`)` Required. The materialized view to update.The materialized view's `name` field is used to identify the view to update. Format: `projects/{project}/instances/{instance}/materializedViews/{materializedView}`.  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Optional. The list of fields to update.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-06 UTC."],[],[]] 
