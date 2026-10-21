---
url: https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.locations.events/list/
title: Method: projects.locations.events.list \u00a0|\u00a0 Error Reporting \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:45:40.628881+00:00
---

# Method: projects.locations.events.list  |  Error Reporting  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.locations.events/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Error Reporting ](https://docs.cloud.google.com/error-reporting/docs)
  * [ Reference ](https://docs.cloud.google.com/error-reporting/reference)



Send feedback 

#  Method: projects.locations.events.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Lists the specified events.

### HTTP request

Choose an endpoint:

globalusafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://clouderrorreporting.googleapis.com/v1beta1/{projectName=projects/*/locations/*}/events`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`projectName` |  `string` Required. The resource name of the Google Cloud Platform project. Written as `projects/{projectID}` or `projects/{projectID}/locations/{location}`, where `{projectID}` is the [Google Cloud Platform project ID](https://support.google.com/cloud/answer/6158840) and `{location}` is a Cloud region.Examples: `projects/my-project-123`, `projects/my-project-123/locations/global`.For a list of supported locations, see [Supported Regions](https://cloud.google.com/logging/docs/region-support). `global` is the default when unspecified.  
  
### Query parameters

Parameters  
---  
`groupId` |  `string` Required. The group for which events shall be returned. The `groupId` is a unique identifier for a particular error group. The identifier is derived from key parts of the error-log content and is treated as Service Data. For information about how Service Data is handled, see [Google Cloud Privacy Notice](https://cloud.google.com/terms/cloud-privacy-notice).  
`serviceFilter` |  `object (`[ServiceContextFilter](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ServiceContextFilter)`)` Optional. List only ErrorGroups which belong to a service context that matches the filter. Data for all service contexts is returned if this field is not specified.  
`timeRange` |  `object (`[QueryTimeRange](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/QueryTimeRange)`)` Optional. List only data for the given time range. If not set a default time range is used. The field timeRangeBegin in the response will specify the beginning of this time range.  
`pageSize` |  `integer` Optional. The maximum number of results to return per response.  
`pageToken` |  `string` Optional. A `nextPageToken` provided by a previous response.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ListEventsResponse](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ListEventsResponse)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/stackdriver-integration`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
