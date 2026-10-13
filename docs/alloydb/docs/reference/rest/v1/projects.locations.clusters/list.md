---
url: https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters/list/
title: Method: projects.locations.clusters.list \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:30:14.497707+00:00
---

# Method: projects.locations.clusters.list  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Reference ](https://docs.cloud.google.com/alloydb/docs/reference/rest)



Send feedback 

#  Method: projects.locations.clusters.list Stay organized with collections  Save and categorize content based on your preferences. 

Lists Clusters in a given project and location.

### HTTP request

Choose a location:

global us-central2 us-east7 northamerica-northeast1 northamerica-northeast2 northamerica-south1 southamerica-east1 southamerica-west1 us-central1 us-east1 us-east4 us-east5 us-south1 us-west1 us-west2 us-west3 us-west4 europe-central2 europe-southwest1 europe-north1 europe-north2 europe-west1 europe-west2 europe-west3 europe-west4 europe-west6 europe-west8 europe-west9 europe-west10 europe-west12 asia-east1 asia-east2 asia-northeast1 asia-northeast2 asia-northeast3 asia-south1 asia-south2 asia-southeast1 asia-southeast2 australia-southeast1 australia-southeast2 me-central1 me-central2 me-west1 africa-south1

  
`GET https://alloydb.googleapis.com/v1/{parent=projects/*/locations/*}/clusters`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The name of the parent resource. For the required format, see the comment on the Cluster.name field. Additionally, you can perform an aggregated list operation by specifying a value with the following format: * projects/{project}/locations/- Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `alloydb.clusters.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`pageToken` |  `string` A token identifying a page of results the server should return.  
`filter` |  `string` Optional. Filtering results  
`orderBy` |  `string` Optional. Hint for how to order the results  
  
### Request body

The request body must be empty.

### Response body

Message for response to listing Clusters

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "clusters": [
        {
          object ([Cluster](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters#Cluster))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`clusters[]` |  `object (`[Cluster](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters#Cluster)`)` The list of Cluster  
`nextPageToken` |  `string` A token identifying a page of results the server should return.  
`unreachable[]` |  `string` Locations that could not be reached.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/alloydb.readonly`
  * ` https://www.googleapis.com/auth/alloydb`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-19 UTC."],[],[]] 
