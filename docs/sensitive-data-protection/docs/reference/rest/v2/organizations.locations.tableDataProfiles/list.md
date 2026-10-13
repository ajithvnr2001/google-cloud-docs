---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.tableDataProfiles/list/
title: Method: organizations.locations.tableDataProfiles.list \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:25.748154+00:00
---

# Method: organizations.locations.tableDataProfiles.list  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.tableDataProfiles/list/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Reference ](https://docs.cloud.google.com/sensitive-data-protection/docs/apis)



Send feedback 

#  Method: organizations.locations.tableDataProfiles.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Lists table data profiles for an organization.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4useuin

  
`GET https://dlp.googleapis.com/v2/{parent=organizations/*/locations/*}/tableDataProfiles`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Resource name of the organization or project, for example `organizations/433245324/locations/europe` or `projects/project-id/locations/asia`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `dlp.tableDataProfiles.list`

  
  
### Query parameters

Parameters  
---  
`pageToken` |  `string` Page token to continue retrieval.  
`pageSize` |  `integer` Size of the page. This value can be limited by the server. If zero, server returns a page of max size 100.  
`orderBy` |  `string` Comma-separated list of fields to order by, followed by `asc` or `desc` postfix. This list is case insensitive. The default sorting order is ascending. Redundant space characters are insignificant. Only one order field at a time is allowed.Examples: * `project_id asc` * `table_id` * `sensitivity_level desc`Supported fields are:

  * `project_id`: The Google Cloud project ID.
  * `dataset_id`: The ID of a BigQuery dataset.
  * `table_id`: The ID of a BigQuery table.
  * `sensitivity_level`: How sensitive the data in a table is, at most.
  * `data_risk_level`: How much risk is associated with this data.
  * `profile_last_generated`: When the profile was last updated in epoch seconds.
  * `last_modified`: The last time the resource was modified.
  * `resource_visibility`: Visibility restriction for this resource.
  * `row_count`: Number of rows in this resource.

  
`filter` |  `string` Allows filtering.Supported syntax:

  * Filter expressions are made up of one or more restrictions.
  * Restrictions can be combined by `AND` or `OR` logical operators. A sequence of restrictions implicitly uses `AND`.
  * A restriction has the form of `{field} {operator} {value}`.
  * Supported fields: 
    * `project_id`: The Google Cloud project ID
    * `dataset_id`: The BigQuery dataset ID
    * `table_id`: The ID of the BigQuery table
    * `sensitivity_level`: HIGH|MODERATE|LOW
    * `data_risk_level`: HIGH|MODERATE|LOW
    * `resource_visibility`: PUBLIC|RESTRICTED
    * `status_code`: an RPC status code as defined in <https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto>
    * `profile_last_generated`: Date and time the profile was last generated
  * The operator must be `=` or `!=`. The `profile_last_generated` filter also supports `<` and `>`.

The syntax is based on <https://google.aip.dev/160>.Examples:

  * `project_id = 12345 AND status_code = 1`
  * `project_id = 12345 AND sensitivity_level = HIGH`
  * `project_id = 12345 AND resource_visibility = PUBLIC`
  * `profile_last_generated < "2025-01-01T00:00:00.000Z"`

The length of this field should be no more than 500 characters.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ListTableDataProfilesResponse](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ListTableDataProfilesResponse)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
