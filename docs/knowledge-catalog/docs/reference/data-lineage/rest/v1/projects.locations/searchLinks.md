---
url: https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations/searchLinks/
title: Method: projects.locations.searchLinks \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:13:08.627213+00:00
---

# Method: projects.locations.searchLinks  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations/searchLinks/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Reference ](https://docs.cloud.google.com/knowledge-catalog/docs/reference)



Send feedback 

#  Method: projects.locations.searchLinks Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Link
    * JSON representation
  * DependencyInfo
    * JSON representation
  * Try it!



Retrieve a list of links connected to a specific asset. Links represent the data flow between **source** (upstream) and **target** (downstream) assets in transformation pipelines. Links are stored in the same project as the Lineage Events that create them.

You can retrieve links in every project where you have the `datalineage.events.get` permission. The project provided in the URL is used for Billing and Quota.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west15europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-central2us-east1us-east4us-east5us-east7us-south1us-west1us-west2us-west3us-west4us-west8useu

  
`POST https://datalineage.googleapis.com/v1/{parent}:searchLinks`

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The project and location you want search in. It takes the form `projects/{project}/locations/{location}`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "pageSize": integer,
      "pageToken": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "source": {
        object ([EntityReference](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations.processes.runs.lineageEvents#EntityReference))
      },
      "target": {
        object ([EntityReference](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations.processes.runs.lineageEvents#EntityReference))
      },
      "sources": {
        object ([MultipleEntityReference](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/MultipleEntityReference))
      },
      "targets": {
        object ([MultipleEntityReference](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/MultipleEntityReference))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`pageSize` |  `integer` Optional. The maximum number of links to return in a single page of the response. A page may contain fewer links than this value. If unspecified, at most 10 links are returned.Maximum value is 100; values greater than 100 are reduced to 100.  
`pageToken` |  `string` Optional. The page token received from a previous `SearchLinksRequest` call. Use it to get the next page.When requesting subsequent pages of a response, remember that all parameters must match the values you provided in the original request.  
The asset for which you want to retrieve links. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`source` |  `object (`[EntityReference](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations.processes.runs.lineageEvents#EntityReference)`)` Optional. Send asset information in the **source** field to retrieve all links that lead from the specified asset to downstream assets.  
`target` |  `object (`[EntityReference](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations.processes.runs.lineageEvents#EntityReference)`)` Optional. Send asset information in the **target** field to retrieve all links that lead from upstream assets to the specified asset.  
`sources` |  `object (`[MultipleEntityReference](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/MultipleEntityReference)`)` Optional. Send a list of asset information in the **sources** field to retrieve all links that lead from the specified assets to downstream assets. This field is similar to the `source` `[source](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations/searchLinks#body.request_body.FIELDS.source)` field but allows providing multiple entities. All entities within the `MultipleEntityReference` must have the same `fullyQualifiedName`.  
`targets` |  `object (`[MultipleEntityReference](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/MultipleEntityReference)`)` Optional. Send a list of asset information in the **targets** field to retrieve all links that lead from upstream assets to the specified assets. This field is similar to the `target` `[target](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations/searchLinks#body.request_body.FIELDS.target)` field but allows providing multiple entities. All entities within the `MultipleEntityReference` must have the same `fullyQualifiedName`.  
End of mutually exclusive fields.  
  
### Response body

Response message for `[locations.searchLinks](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations/searchLinks#google.cloud.datacatalog.lineage.v1.Lineage.SearchLinks)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "links": [
        {
          object ([Link](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations/searchLinks#Link))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`links[]` |  `object (`[Link](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations/searchLinks#Link)`)` The list of links for a given asset. Can be empty if the asset has no relations of requested type (source or target).  
`nextPageToken` |  `string` The token to specify as `pageToken` in the subsequent call to get the next page. Omitted if there are no more pages in the response.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `datalineage.locations.searchLinks`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## Link

Links represent the data flow between **source** (upstream) and **target** (downstream) assets in transformation pipelines.

Links are created when LineageEvents record data transformation between related assets.

JSON representation  
---  
      
    
    {
      "name": string,
      "source": {
        object ([EntityReference](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations.processes.runs.lineageEvents#EntityReference))
      },
      "target": {
        object ([EntityReference](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations.processes.runs.lineageEvents#EntityReference))
      },
      "startTime": string,
      "endTime": string,
      "dependencyInfo": [
        {
          object ([DependencyInfo](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations/searchLinks#DependencyInfo))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Output only. Immutable. The name of the link. Format: `projects/{project}/locations/{location}/links/{link}`.  
`source` |  `object (`[EntityReference](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations.processes.runs.lineageEvents#EntityReference)`)` The pointer to the entity that is the **source** of this link.  
`target` |  `object (`[EntityReference](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations.processes.runs.lineageEvents#EntityReference)`)` The pointer to the entity that is the **target** of this link.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The start of the first event establishing this link.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The end of the last event establishing this link.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`dependencyInfo[]` |  `object (`[DependencyInfo](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations/searchLinks#DependencyInfo)`)` Optional. The dependency info of the link (applies only to column level links).  
  
## DependencyInfo

Dependency info describes how one entity depends on another.

JSON representation  
---  
      
    
    {
      "dependencyType": enum ([DependencyType](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations.processes.runs.lineageEvents#DependencyType))
    }  
  
Fields  
---  
`dependencyType` |  `enum (`[DependencyType](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations.processes.runs.lineageEvents#DependencyType)`)` The type of dependency.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-21 UTC."],[],[]] 
