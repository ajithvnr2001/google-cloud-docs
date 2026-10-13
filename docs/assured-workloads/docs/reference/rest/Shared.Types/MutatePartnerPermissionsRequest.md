---
url: https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/MutatePartnerPermissionsRequest/
title: MutatePartnerPermissionsRequest \u00a0|\u00a0 Assured Workloads \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:38:33.759901+00:00
---

# MutatePartnerPermissionsRequest  |  Assured Workloads  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/MutatePartnerPermissionsRequest/

The names for some Assured Workloads control packages have changed. For information about the name change, see [Control package renaming notice](https://docs.cloud.google.com/assured-workloads/docs/overview#name-change). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads/docs)
  * [ Reference ](https://docs.cloud.google.com/assured-workloads/docs/apis)



Send feedback 

#  MutatePartnerPermissionsRequest Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Request of updating permission settings for a partner workload.

JSON representation  
---  
      
    
    {
      "name": string,
      "partnerPermissions": {
        object ([PartnerPermissions](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/PartnerPermissions))
      },
      "updateMask": string,
      "etag": string
    }  
  
Fields  
---  
`name` |  `string` Required. The `name` field is used to identify the workload. Format: organizations/{org_id}/locations/{locationId}/workloads/{workload_id}  
`partnerPermissions` |  `object (`[PartnerPermissions](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/PartnerPermissions)`)` Required. The partner permissions to be updated.  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Required. The list of fields to be updated. E.g. updateMask { paths: "partnerPermissions.data_logs_viewer"}This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
`etag` |  `string` Optional. The etag of the workload. If this is provided, it must match the server's etag.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-30 UTC."],[],[]] 
