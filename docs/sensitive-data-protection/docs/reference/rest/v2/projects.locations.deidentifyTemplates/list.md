---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.deidentifyTemplates/list/
title: Method: projects.locations.deidentifyTemplates.list \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:33.796641+00:00
---

# Method: projects.locations.deidentifyTemplates.list  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.deidentifyTemplates/list/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Reference ](https://docs.cloud.google.com/sensitive-data-protection/docs/apis)



Send feedback 

#  Method: projects.locations.deidentifyTemplates.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Lists DeidentifyTemplates. See <https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates-deid> to learn more.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4useuin

  
`GET https://dlp.googleapis.com/v2/{parent=projects/*/locations/*}/deidentifyTemplates`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Parent resource name.The format of this value varies depending on the scope of the request (project or organization) and whether you have [specified a processing location](https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location):

  * Projects scope, location specified: `projects/{projectId}/locations/{locationId}`
  * Projects scope, no location specified (defaults to global): `projects/{projectId}`
  * Organizations scope, location specified: `organizations/{org_id}/locations/{locationId}`
  * Organizations scope, no location specified (defaults to global): `organizations/{org_id}`

The following example `parent` string specifies a parent project with the identifier `example-project`, and specifies the `europe-west3` location for processing data:
    
    
    parent=projects/example-project/locations/europe-west3
    

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `dlp.deidentifyTemplates.list`

  
  
### Query parameters

Parameters  
---  
`pageToken` |  `string` Page token to continue retrieval. Comes from the previous call to `deidentifyTemplates.list`.  
`pageSize` |  `integer` Size of the page. This value can be limited by the server. If zero server returns a page of max size 100.  
`orderBy` |  `string` Comma-separated list of fields to order by, followed by `asc` or `desc` postfix. This list is case insensitive. The default sorting order is ascending. Redundant space characters are insignificant.Example: `name asc,updateTime, createTime desc`Supported fields are:

  * `createTime`: corresponds to the time the template was created.
  * `updateTime`: corresponds to the time the template was last updated.
  * `name`: corresponds to the template's name.
  * `displayName`: corresponds to the template's display name.

  
`locationId` |  `string` Deprecated. This field has no effect.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ListDeidentifyTemplatesResponse](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ListDeidentifyTemplatesResponse)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
