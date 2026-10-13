---
url: https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.collections/delete/
title: Method: projects.locations.collections.delete \u00a0|\u00a0 Document AI Warehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:50:45.413129+00:00
---

# Method: projects.locations.collections.delete  |  Document AI Warehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.collections/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI Warehouse ](https://docs.cloud.google.com/document-warehouse/docs)



Send feedback 

#  Method: projects.locations.collections.delete Stay organized with collections  Save and categorize content based on your preferences. 

Deletes a collection.

### HTTP request

`DELETE https://contentwarehouse.googleapis.com/v1/{name}`

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the collection to delete. It takes the form `projects/{project}/locations/{location}/collections/{collection}`.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body is empty.

### Authorization Scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `contentwarehouse.collections.delete`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-08 UTC."],[],[]] 
