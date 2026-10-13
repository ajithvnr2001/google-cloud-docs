---
url: https://docs.cloud.google.com/cluster-director/docs/reference/rest/v1beta/projects.locations.clusters/list/
title: Method: projects.locations.clusters.list \u00a0|\u00a0 Cluster Director \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:07:39.590531+00:00
---

# Method: projects.locations.clusters.list  |  Cluster Director  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-director/docs/reference/rest/v1beta/projects.locations.clusters/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Director ](https://docs.cloud.google.com/cluster-director/docs)
  * [ Reference ](https://docs.cloud.google.com/cluster-director/docs/apis)



Send feedback 

#  Method: projects.locations.clusters.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Lists Clusters in a given project and location.

### HTTP request

Choose an endpoint:

globalus-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://hypercomputecluster.googleapis.com/v1beta/{parent=projects/*/locations/*}/clusters`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Parent location of the clusters to list, in the format `projects/{project}/locations/{location}`.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Maximum number of clusters to return. The service may return fewer than this value.  
`pageToken` |  `string` Optional. A page token received from a previous `clusters.list` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `clusters.list` must match the call that provided the page token.  
`filter` |  `string` Optional. [Filter](https://google.aip.dev/160) to apply to the returned results.  
`orderBy` |  `string` Optional. How to order the resulting clusters. Must be one of the following strings:

  * `name`
  * `name desc`
  * `createTime`
  * `createTime desc`

If not specified, clusters will be returned in an arbitrary order.  
  
### Request body

The request body must be empty.

### Response body

Response message for `[clusters.list](https://docs.cloud.google.com/cluster-director/docs/reference/rest/v1beta/projects.locations.clusters/list#google.cloud.hypercomputecluster.v1beta.HypercomputeCluster.ListClusters)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "clusters": [
        {
          object ([Cluster](https://docs.cloud.google.com/cluster-director/docs/reference/rest/v1beta/projects.locations.clusters#Cluster))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`clusters[]` |  `object (`[Cluster](https://docs.cloud.google.com/cluster-director/docs/reference/rest/v1beta/projects.locations.clusters#Cluster)`)` Clusters in the specified location.  
`nextPageToken` |  `string` A token that can be sent as `pageToken` to retrieve the next page. If this field is absent, there are no subsequent pages.  
`unreachable[]` |  `string` Locations that could not be reached.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `hypercomputecluster.clusters.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
