---
url: https://docs.cloud.google.com/recommender/docs/reference/rest/v1/folders.locations.insightTypes.insights/list/
title: Method: folders.locations.insightTypes.insights.list \u00a0|\u00a0 Recommender \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:35:39.680329+00:00
---

# Method: folders.locations.insightTypes.insights.list  |  Recommender  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recommender/docs/reference/rest/v1/folders.locations.insightTypes.insights/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Recommender ](https://docs.cloud.google.com/recommender/docs)
  * [ Reference ](https://docs.cloud.google.com/recommender/docs/apis)



Send feedback 

#  Method: folders.locations.insightTypes.insights.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions



Lists insights for the specified Cloud Resource. Requires the recommender.*.list IAM permission for the specified insight type.

### HTTP request

`GET https://recommender.googleapis.com/v1/{parent=folders/*/locations/*/insightTypes/*}/insights`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The container resource on which to execute the request. Acceptable formats:

  * `projects/[PROJECT_NUMBER]/locations/[LOCATION]/insightTypes/[INSIGHT_TYPE_ID]`
  * `projects/[PROJECT_ID]/locations/[LOCATION]/insightTypes/[INSIGHT_TYPE_ID]`
  * `billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION]/insightTypes/[INSIGHT_TYPE_ID]`
  * `folders/[FOLDER_ID]/locations/[LOCATION]/insightTypes/[INSIGHT_TYPE_ID]`
  * `organizations/[ORGANIZATION_ID]/locations/[LOCATION]/insightTypes/[INSIGHT_TYPE_ID]`

LOCATION here refers to GCP Locations: <https://cloud.google.com/about/locations/> INSIGHT_TYPE_ID refers to supported insight types: <https://cloud.google.com/recommender/docs/insights/insight-types>.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of results to return from this request. Non-positive values are ignored. If not specified, the server will determine the number of results to return.  
`pageToken` |  `string` Optional. If present, retrieves the next batch of results from the preceding call to this method. `pageToken` must be the value of `nextPageToken` from the previous response. The values of other method parameters must be identical to those in the previous call.  
`filter` |  `string` Optional. Filter expression to restrict the insights returned. Supported filter fields:

  * `stateInfo.state`
  * `insightSubtype`
  * `severity`
  * `targetResources`

Examples:

  * `stateInfo.state = ACTIVE OR stateInfo.state = DISMISSED`
  * `insightSubtype = PERMISSIONS_USAGE`
  * `severity = CRITICAL OR severity = HIGH`
  * `targetResources : //compute.googleapis.com/projects/1234/zones/us-central1-a/instances/instance-1`
  * `stateInfo.state = ACTIVE AND (severity = CRITICAL OR severity = HIGH)`

The max allowed filter length is 500 characters.(These expressions are based on the filter language described at <https://google.aip.dev/160>)  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ListInsightsResponse](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/ListInsightsResponse)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permissions on the `parent` resource:

  * `recommender.commitmentUtilizationInsights.list`
  * `recommender.computeAddressIdleResourceInsights.list`
  * `recommender.computeDiskIdleResourceInsights.list`
  * `recommender.computeFirewallInsights.list`
  * `recommender.computeImageIdleResourceInsights.list`
  * `recommender.iamPolicyInsights.list`
  * `recommender.iamServiceAccountInsights.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
