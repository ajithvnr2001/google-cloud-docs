---
url: https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workspaces/fetchBranches/
title: Method: projects.locations.repositories.workspaces.fetchBranches \u00a0|\u00a0 Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:42:25.236378+00:00
---

# Method: projects.locations.repositories.workspaces.fetchBranches  |  Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workspaces/fetchBranches/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Dataform ](https://docs.cloud.google.com/dataform)
  * [ Reference ](https://docs.cloud.google.com/dataform/docs/authentication)



Send feedback 

#  Method: projects.locations.repositories.workspaces.fetchBranches Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * BranchFilter
  * BranchMetadata
    * JSON representation
  * Try it!



Fetches branches in a workspace.

### HTTP request

Choose a location:

global africa-south1 asia-east1 asia-east2 asia-northeast1 asia-northeast2 asia-northeast3 asia-south1 asia-south2 asia-southeast1 asia-southeast2 australia-southeast1 australia-southeast2 europe-central2 europe-north1 europe-southwest1 europe-west1 europe-west10 europe-west12 europe-west2 europe-west3 europe-west4 europe-west6 europe-west8 europe-west9 me-central1 me-central2 me-west1 northamerica-northeast1 northamerica-northeast2 southamerica-east1 southamerica-west1 us-central1 us-east1 us-east4 us-east5 us-south1 us-west1 us-west2 us-west3 us-west4

  
`GET https://dataform.googleapis.com/v1beta1/{name=projects/*/locations/*/repositories/*/workspaces/*}:fetchBranches`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The workspace resource name. Format: `projects/{project}/locations/{location}/repositories/{repository}/workspaces/{workspace}`  
  
### Query parameters

Parameters  
---  
`filter` |  `enum (`[BranchFilter](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workspaces/fetchBranches#BranchFilter)`)` Optional. Filter for the returned list.  
`pageSize` |  `integer` Optional. Maximum number of branches to return. The server may return fewer items than requested. If unspecified, the server picks an appropriate default. The maximum value is `1000`; values above `1000` are coerced to `1000`.  
`pageToken` |  `string` Optional. Page token received from a previous `workspaces.fetchBranches` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `workspaces.fetchBranches`, with the exception of `pageSize`, must match the call that provided the page token.  
  
### Request body

The request body must be empty.

### Response body

Response message for `workspaces.fetchBranches` method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "branches": [
        {
          object ([BranchMetadata](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workspaces/fetchBranches#BranchMetadata))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`branches[]` |  `object (`[BranchMetadata](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workspaces/fetchBranches#BranchMetadata)`)` The branches in the workspace.  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/bigquery`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `dataform.workspaces.fetchBranches`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## BranchFilter

Filter for the returned list.

Enums  
---  
`BRANCH_FILTER_UNSPECIFIED` | Default value. If unspecified, `LOCAL_ONLY` is used.  
`LOCAL_ONLY` | Returns local branches.  
`REMOTE_ONLY` | Returns remote branches.  
`ALL` | Returns all branches.  
  
## BranchMetadata

Contains metadata about a branch.

JSON representation  
---  
      
    
    {
      "branchName": string,
      "lastCommit": {
        object ([CommitLogEntry](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/CommitLogEntry))
      }
    }  
  
Fields  
---  
`branchName` |  `string` The branch name.  
`lastCommit` |  `object (`[CommitLogEntry](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/CommitLogEntry)`)` The last commit on the branch.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-17 UTC."],[],[]] 
