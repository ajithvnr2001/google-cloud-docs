---
url: https://docs.cloud.google.com/resource-manager/docs/reference/essentialcontacts/rest/v1/organizations.contacts/create/
title: Method: organizations.contacts.create \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:47:52.038620+00:00
---

# Method: organizations.contacts.create  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/reference/essentialcontacts/rest/v1/organizations.contacts/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Reference ](https://docs.cloud.google.com/resource-manager/reference/rest)



Send feedback 

#  Method: organizations.contacts.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Adds a new contact for a resource.

### HTTP request

`POST https://essentialcontacts.googleapis.com/v1/{parent=organizations/*}/contacts`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The resource to save this contact for. Format: organizations/{organization}, folders/{folder} or projects/{project} (where {project} is the project number) Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `essentialcontacts.contacts.create`

  
  
### Request body

The request body contains an instance of `[Contact](https://docs.cloud.google.com/resource-manager/docs/reference/essentialcontacts/rest/v1/folders.contacts#Contact)`.

### Response body

If successful, the response body contains a newly created instance of `[Contact](https://docs.cloud.google.com/resource-manager/docs/reference/essentialcontacts/rest/v1/folders.contacts#Contact)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-18 UTC."],[],[]] 
