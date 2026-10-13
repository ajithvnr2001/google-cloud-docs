---
url: https://docs.cloud.google.com/artifact-registry/docs/reference/rest/v1/projects.locations.repositories/list/
title: Method: projects.locations.repositories.list \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:19:30.157475+00:00
---

# Method: projects.locations.repositories.list  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/reference/rest/v1/projects.locations.repositories/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Reference ](https://docs.cloud.google.com/artifact-registry/docs/apis)



Send feedback 

#  Method: projects.locations.repositories.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Examples
  * Try it!



Lists repositories.

### HTTP request

Choose a location:

global africa-south1 asia-east1 asia-east2 asia-northeast1 asia-northeast2 asia-northeast3 asia-south1 asia-south2 asia-southeast1 asia-southeast2 australia-southeast1 australia-southeast2 europe-central2 europe-north1 europe-southwest1 europe-west1 europe-west10 europe-west12 europe-west2 europe-west3 europe-west4 europe-west6 europe-west8 europe-west9 me-central1 me-west1 northamerica-northeast1 northamerica-northeast2 southamerica-east1 southamerica-west1 us-central1 us-east1 us-east4 us-east5 us-south1 us-west1 us-west2 us-west3 us-west4 me-central2 us-east7 us eu

  
`GET https://artifactregistry.googleapis.com/v1/{parent=projects/*/locations/*}/repositories`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The name of the parent resource whose repositories will be listed. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `artifactregistry.repositories.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` The maximum number of repositories to return. Maximum page size is 1,000.  
`pageToken` |  `string` The nextPageToken value returned from a previous list request, if any.  
`filter` |  `string` Optional. An expression for filtering the results of the request. Filter rules are case insensitive. The fields eligible for filtering are:

  * `name`

Examples of using a filter:To filter the results of your request to repositories with the name `my-repo` in project `my-project` in the `us-central` region, append the following filter expression to your request:

  * `name="projects/my-project/locations/us-central1/repositories/my-repo"`

You can also use wildcards to match any number of characters before or after the value:

  * `name="projects/my-project/locations/us-central1/repositories/my-*"`
  * `name="projects/my-project/locations/us-central1/repositories/*repo"`
  * `name="projects/my-project/locations/us-central1/repositories/*repo*"`

  
`orderBy` |  `string` Optional. The field to order the results by.  
  
### Request body

The request body must be empty.

### Response body

The response from listing repositories.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "repositories": [
        {
          object ([Repository](https://docs.cloud.google.com/artifact-registry/docs/reference/rest/v1/projects.locations.repositories#Repository))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`repositories[]` |  `object (`[Repository](https://docs.cloud.google.com/artifact-registry/docs/reference/rest/v1/projects.locations.repositories#Repository)`)` The repositories returned.  
`nextPageToken` |  `string` The token to retrieve the next page of repositories, or empty if there are no more repositories to return.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-14 UTC."],[],[]] 
