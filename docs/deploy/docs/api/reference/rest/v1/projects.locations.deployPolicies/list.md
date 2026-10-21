---
url: https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies/list/
title: Method: projects.locations.deployPolicies.list \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:15:01.025961+00:00
---

# Method: projects.locations.deployPolicies.list  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Reference ](https://docs.cloud.google.com/deploy/docs/api)



Send feedback 

#  Method: projects.locations.deployPolicies.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Lists DeployPolicies in a given project and location.

### HTTP request

Choose a location:

global asia-south1 asia-south2 us-central1 us-east1 us-east4 us-east5 us-east7 us-south1 us-west1 us-west2 us-west3 us-west4

  
`GET https://clouddeploy.googleapis.com/v1/{parent=projects/*/locations/*}/deployPolicies`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent, which owns this collection of deploy policies. Format must be `projects/{projectId}/locations/{location_name}`.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` The maximum number of deploy policies to return. The service may return fewer than this value. If unspecified, at most 50 deploy policies will be returned. The maximum value is 1000; values above 1000 will be set to 1000.  
`pageToken` |  `string` A page token, received from a previous `deployPolicies.list` call. Provide this to retrieve the subsequent page.When paginating, all other provided parameters match the call that provided the page token.  
`filter` |  `string` Filter deploy policies to be returned. See <https://google.aip.dev/160> for more details. All fields can be used in the filter.  
`orderBy` |  `string` Field to sort by. See <https://google.aip.dev/132#ordering> for more details.  
  
### Request body

The request body must be empty.

### Response body

The response object from `deployPolicies.list`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "deployPolicies": [
        {
          object ([DeployPolicy](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies#DeployPolicy))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`deployPolicies[]` |  `object (`[DeployPolicy](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies#DeployPolicy)`)` The `DeployPolicy` objects.  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
`unreachable[]` |  `string` Locations that could not be reached.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `clouddeploy.deployPolicies.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
