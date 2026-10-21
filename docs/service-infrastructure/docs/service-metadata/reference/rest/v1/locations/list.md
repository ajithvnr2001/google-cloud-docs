---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-metadata/reference/rest/v1/locations/list/
title: Method: locations.list \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:45.238711+00:00
---

# Method: locations.list  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-metadata/reference/rest/v1/locations/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  Method: locations.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Lists information about the supported locations for this service. This method can be called in two ways:

  * **List all public locations:** Use the path `GET /v1/locations`.
  * **List project-visible locations:** Use the path `GET /v1/projects/{projectId}/locations`. This may include public locations as well as private or other locations specifically visible to the project.



### HTTP request

  * List public locations:  
`GET https://cloud.googleapis.com/v1/locations`
  * List locations for a specific project:  
`GET https://cloud.googleapis.com/v1/{name=projects/*}/locations`



The URL uses [gRPC Transcoding](https://github.com/googleapis/googleapis/blob/master/google/api/http.proto) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` The resource that owns the locations collection, if applicable.  
  
### Query parameters

Parameters  
---  
`filter` |  `string` A filter to narrow down results to a preferred subset. The filtering language accepts strings like `"displayName=tokyo"`, and is documented in more detail in [AIP-160](https://google.aip.dev/160).  
`pageSize` |  `integer` The maximum number of results to return. If not set, the service selects a default.  
`pageToken` |  `string` A page token received from the `nextPageToken` field in the response. Send that page token to receive the subsequent page.  
`extraLocationTypes[]` |  `string` Optional. A list of special location types to include in addition to the generic Cloud locations. By default, omitting this field means only the generic Cloud locations will be returned in the response. The supported values are: "CLOUD_AI_ZONE"  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ListLocationsResponse](https://docs.cloud.google.com/service-infrastructure/docs/service-metadata/reference/rest/v1/ListLocationsResponse)`.

### Authorization Scopes

  * Calling `**GET /v1/locations (without a project path)**` supports using either an API Key or an OAuth token.
  * Calling`**GET /v1/projects/{project_id}/locations**` requires an OAuth token with the `**cloud.locations.list**` IAM permission on the specified project.



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

### Examples

List all public standard locations (using your API Key):
    
    
    curl -H "X-Goog-Api-Key: YOUR_API_KEY" \  
       "https://cloud.googleapis.com/v1/locations"
    

List all standard locations and AI zones (using OAuth):
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
       -H "X-Goog-User-Project: YOUR_PROJECT_ID" \  
       "https://cloud.googleapis.com/v1/locations?extra_location_types=CLOUD_AI_ZONE"
    

List standard locations and AI zones for a specific project (using OAuth):
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
       -H "X-Goog-User-Project: YOUR_PROJECT_ID" \  
       "https://cloud.googleapis.com/v1/projects/YOUR_PROJECT_ID/locations?extra_location_types=CLOUD_AI_ZONE"
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-26 UTC."],[],[]] 
