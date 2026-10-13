---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.projectDataProfiles/list/
title: Method: projects.locations.projectDataProfiles.list \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:38.992557+00:00
---

# Method: projects.locations.projectDataProfiles.list  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.projectDataProfiles/list/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Reference ](https://docs.cloud.google.com/sensitive-data-protection/docs/apis)



Send feedback 

#  Method: projects.locations.projectDataProfiles.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Lists project data profiles for an organization.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4useuin

  
`GET https://dlp.googleapis.com/v2/{parent=projects/*/locations/*}/projectDataProfiles`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. organizations/{org_id}/locations/{loc_id} Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `dlp.projectDataProfiles.list`

  
  
### Query parameters

Parameters  
---  
`pageToken` |  `string` Page token to continue retrieval.  
`pageSize` |  `integer` Size of the page. This value can be limited by the server. If zero, server returns a page of max size 100.  
`orderBy` |  `string` Comma-separated list of fields to order by, followed by `asc` or `desc` postfix. This list is case insensitive. The default sorting order is ascending. Redundant space characters are insignificant. Only one order field at a time is allowed.Examples: * `projectId` * `sensitivityLevel desc`Supported fields:

  * `projectId`: Google Cloud project ID
  * `sensitivityLevel`: How sensitive the data in a project is, at most
  * `dataRiskLevel`: How much risk is associated with this data
  * `profileLastGenerated`: Date and time (in epoch seconds) the profile was last generated

  
`filter` |  `string` Allows filtering.Supported syntax:

  * Filter expressions are made up of one or more restrictions.
  * Restrictions can be combined by `AND` or `OR` logical operators. A sequence of restrictions implicitly uses `AND`.
  * A restriction has the form of `{field} {operator} {value}`.
  * Supported fields: 
    * `project_id`: the Google Cloud project ID
    * `sensitivity_level`: HIGH|MODERATE|LOW
    * `data_risk_level`: HIGH|MODERATE|LOW
    * `status_code`: an RPC status code as defined in <https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto>
    * `profile_last_generated`: Date and time the profile was last generated
  * The operator must be `=` or `!=`. The `profile_last_generated` filter also supports `<` and `>`.

The syntax is based on <https://google.aip.dev/160>.Examples:

  * `project_id = 12345 AND status_code = 1`
  * `project_id = 12345 AND sensitivity_level = HIGH`
  * `profile_last_generated < "2025-01-01T00:00:00.000Z"`

The length of this field should be no more than 500 characters.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ListProjectDataProfilesResponse](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ListProjectDataProfilesResponse)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
