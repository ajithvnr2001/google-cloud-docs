---
url: https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.bitbucketServerConfigs.repos/list/
title: Method: projects.locations.bitbucketServerConfigs.repos.list \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:59:20.027045+00:00
---

# Method: projects.locations.bitbucketServerConfigs.repos.list  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.bitbucketServerConfigs.repos/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Reference ](https://docs.cloud.google.com/build/docs/api)



Send feedback 

#  Method: projects.locations.bitbucketServerConfigs.repos.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * BitbucketServerRepository
    * JSON representation
  * Try it!



List all repositories for a given `BitbucketServerConfig`.

This API is experimental.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9europe-west15me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-central2us-east1us-east4us-east5us-east7us-south1us-west1us-west2us-west3us-west4us-west8

  
`GET https://cloudbuild.googleapis.com/v1/{parent=projects/*/locations/*/bitbucketServerConfigs/*}/repos`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Name of the parent resource.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` The maximum number of configs to return. The service may return fewer than this value. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` A page token, received from a previous `ListBitbucketServerRepositoriesRequest` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `ListBitbucketServerConfigsRequest` must match the call that provided the page token.  
  
### Request body

The request body must be empty.

### Response body

RPC response object returned by the repos.list RPC method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "bitbucketServerRepositories": [
        {
          object ([BitbucketServerRepository](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.bitbucketServerConfigs.repos/list#BitbucketServerRepository))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`bitbucketServerRepositories[]` |  `object (`[BitbucketServerRepository](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.bitbucketServerConfigs.repos/list#BitbucketServerRepository)`)` List of Bitbucket Server repositories.  
`nextPageToken` |  `string` A token that can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## BitbucketServerRepository

BitbucketServerRepository represents a repository hosted on a Bitbucket Server.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "browseUri": string,
      "repoId": {
        object ([BitbucketServerRepositoryId](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.bitbucketServerConfigs#BitbucketServerConfig.BitbucketServerRepositoryId))
      }
    }  
  
Fields  
---  
`name` |  `string` The resource name of the repository.  
`displayName` |  `string` Display name of the repository.  
`description` |  `string` Description of the repository.  
`browseUri` |  `string` Link to the browse repo page on the Bitbucket Server instance.  
`repoId` |  `object (`[BitbucketServerRepositoryId](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.bitbucketServerConfigs#BitbucketServerConfig.BitbucketServerRepositoryId)`)` Identifier for a repository hosted on a Bitbucket Server.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-26 UTC."],[],[]] 
