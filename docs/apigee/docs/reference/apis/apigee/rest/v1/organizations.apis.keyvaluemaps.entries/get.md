---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.keyvaluemaps.entries/get/
title: Method: organizations.apis.keyvaluemaps.entries.get \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:23.985500+00:00
---

# Method: organizations.apis.keyvaluemaps.entries.get  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.keyvaluemaps.entries/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Method: organizations.apis.keyvaluemaps.entries.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Get the key value entry value for a key value map scoped to an organization, environment, or API proxy.

**Note** : Supported for Apigee hybrid 1.8.x and higher.

### HTTP request

`GET https://apigee.googleapis.com/v1/{name=organizations/*/apis/*/keyvaluemaps/*/entries/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Scope as indicated by the URI in which to fetch the key value map entry/value. Use **one** of the following structures in your request:

  * `organizations/{organization}/apis/{api}/keyvaluemaps/{keyvaluemap}/entries/{entry}`.
  * `organizations/{organization}/environments/{environment}/keyvaluemaps/{keyvaluemap}/entries/{entry}`
  * `organizations/{organization}/keyvaluemaps/{keyvaluemap}/entries/{entry}`.

If the KeyValueMap is under an API Proxy resource that has the `space` attribute set, IAM permissions are checked against the Space resource path. To learn more, read the [Apigee Spaces Overview](https://cloud.google.com/apigee/docs/api-platform/system-administration/spaces/apigee-spaces-overview). Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `apigee.keyvaluemapentries.get`

  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[KeyValueEntry](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.keyvaluemaps.entries#KeyValueEntry)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
