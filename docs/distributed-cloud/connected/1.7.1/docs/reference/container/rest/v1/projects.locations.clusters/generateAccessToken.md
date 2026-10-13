---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs/reference/container/rest/v1/projects.locations.clusters/generateAccessToken/
title: Method: projects.locations.clusters.generateAccessToken \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:14:23.111821+00:00
---

# Method: projects.locations.clusters.generateAccessToken  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs/reference/container/rest/v1/projects.locations.clusters/generateAccessToken/




#  Method: projects.locations.clusters.generateAccessToken Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Generates an access token for a Cluster.

### HTTP request

`GET https://edgecontainer.googleapis.com/v1/{cluster=projects/*/locations/*/clusters/*}:generateAccessToken`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`cluster` |  `string` Required. The resource name of the cluster. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `cluster`:

  * `edgecontainer.clusters.get`

  
  
### Request body

The request body must be empty.

### Response body

An access token for a cluster.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "accessToken": string,
      "expireTime": string
    }  
  
Fields  
---  
`accessToken` |  `string` Output only. Access token to authenticate to k8s api-server.  
`expireTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. Timestamp at which the token will expire.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-24 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]] 
