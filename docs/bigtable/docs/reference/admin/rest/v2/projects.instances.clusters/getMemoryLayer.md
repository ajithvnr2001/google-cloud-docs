---
url: https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.clusters/getMemoryLayer/
title: Method: projects.instances.clusters.getMemoryLayer \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:21:04.502420+00:00
---

# Method: projects.instances.clusters.getMemoryLayer  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.clusters/getMemoryLayer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Reference ](https://docs.cloud.google.com/bigtable/docs/apis)



Send feedback 

#  Method: projects.instances.clusters.getMemoryLayer Stay organized with collections  Save and categorize content based on your preferences. 

Gets information about the memory layer of a cluster.

### HTTP request

`GET https://bigtableadmin.googleapis.com/v2/{name=projects/*/instances/*/clusters/*/memoryLayer}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The unique name of the requested cluster's memory layer. Values are of the form `projects/{project}/instances/{instance}/clusters/{cluster}/memoryLayer`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `bigtable.memoryLayers.get`

  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[MemoryLayer](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/MemoryLayer)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/bigtable.admin`
  * `https://www.googleapis.com/auth/bigtable.admin.cluster`
  * `https://www.googleapis.com/auth/bigtable.admin.instance`
  * `https://www.googleapis.com/auth/cloud-bigtable.admin`
  * `https://www.googleapis.com/auth/cloud-bigtable.admin.cluster`
  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-30 UTC."],[],[]] 
