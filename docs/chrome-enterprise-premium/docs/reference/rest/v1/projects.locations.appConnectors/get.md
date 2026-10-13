---
url: https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.appConnectors/get/
title: Method: projects.locations.appConnectors.get \u00a0|\u00a0 Chrome Enterprise Premium \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:36:08.307649+00:00
---

# Method: projects.locations.appConnectors.get  |  Chrome Enterprise Premium  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.appConnectors/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Chrome Enterprise Premium ](https://docs.cloud.google.com/chrome-enterprise-premium/docs)
  * [ Reference ](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference)



Send feedback 

#  Method: projects.locations.appConnectors.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Gets details of a single AppConnector.

### HTTP request

`GET https://beyondcorp.googleapis.com/v1/{name=projects/*/locations/*/appConnectors/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. BeyondCorp AppConnector name using the form: `projects/{projectId}/locations/{locationId}/appConnectors/{appConnectorId}` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `beyondcorp.appConnectors.get`

  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[AppConnector](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.appConnectors#AppConnector)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-02 UTC."],[],[]] 
