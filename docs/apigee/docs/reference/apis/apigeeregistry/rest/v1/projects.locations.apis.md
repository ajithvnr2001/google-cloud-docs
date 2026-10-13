---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigeeregistry/rest/v1/projects.locations.apis
title: REST Resource: projects.locations.apis \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:57:19.061345+00:00
---

# REST Resource: projects.locations.apis  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigeeregistry/rest/v1/projects.locations.apis

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)



Send feedback 

#  REST Resource: projects.locations.apis Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** You are viewing the legacy Apigee Registry API documentation which is no longer supported. For the latest API hub functionality, it's recommended to use the [Apigee API hub APIs](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest).

  * Resource: Api
    * JSON representation
  * Methods



## Resource: Api

A top-level description of an API. Produced by producers and are commitments to provide services.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "createTime": string,
      "updateTime": string,
      "availability": string,
      "recommendedVersion": string,
      "recommendedDeployment": string,
      "labels": {
        string: string,
        ...
      },
      "annotations": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`name` |  `string` Resource name.  
`displayName` |  `string` Human-meaningful name.  
`description` |  `string` A detailed description.  
`createTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. Creation timestamp.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`updateTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. Last update timestamp.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`availability` |  `string` A user-definable description of the availability of this service. Format: free-form, but we expect single words that describe availability, e.g., "NONE", "TESTING", "PREVIEW", "GENERAL", "DEPRECATED", "SHUTDOWN".  
`recommendedVersion` |  `string` The recommended version of the API. Format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}`  
`recommendedDeployment` |  `string` The recommended deployment of the API. Format: `projects/{project}/locations/{location}/apis/{api}/deployments/{deployment}`  
`labels` |  `map (key: string, value: string)` Labels attach identifying metadata to resources. Identifying metadata can be used to filter list operations.Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores, and dashes. International characters are allowed. No more than 64 user labels can be associated with one resource (System labels are excluded).See <https://goo.gl/xmQnxf> for more information and examples of labels. System reserved label keys are prefixed with `apigeeregistry.googleapis.com/` and cannot be changed.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`annotations` |  `map (key: string, value: string)` Annotations attach non-identifying metadata to resources.Annotation keys and values are less restricted than those of labels, but should be generally used for small values of broad interest. Larger, topic- specific metadata should be stored in Artifacts.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigeeregistry/rest/v1/projects.locations.apis/create)`

|  Creates a specified API.  
  
### `[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigeeregistry/rest/v1/projects.locations.apis/delete)`

|  Removes a specified API and all of the resources that it owns.  
  
### `[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigeeregistry/rest/v1/projects.locations.apis/get)`

|  Returns a specified API.  
  
### `[getIamPolicy](https://docs.cloud.google.com/apigee/docs/reference/apis/apigeeregistry/rest/v1/projects.locations.apis/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigeeregistry/rest/v1/projects.locations.apis/list)`

|  Returns matching APIs.  
  
### `[patch](https://docs.cloud.google.com/apigee/docs/reference/apis/apigeeregistry/rest/v1/projects.locations.apis/patch)`

|  Used to modify a specified API.  
  
### `[setIamPolicy](https://docs.cloud.google.com/apigee/docs/reference/apis/apigeeregistry/rest/v1/projects.locations.apis/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/apigee/docs/reference/apis/apigeeregistry/rest/v1/projects.locations.apis/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
