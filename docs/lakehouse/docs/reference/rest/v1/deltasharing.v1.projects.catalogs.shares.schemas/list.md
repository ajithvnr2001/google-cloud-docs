---
url: https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/deltasharing.v1.projects.catalogs.shares.schemas/list/
title: Method: deltasharing.v1.projects.catalogs.shares.schemas.list \u00a0|\u00a0 BigLake API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:43:37.934637+00:00
---

# Method: deltasharing.v1.projects.catalogs.shares.schemas.list  |  BigLake API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/deltasharing.v1.projects.catalogs.shares.schemas/list/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ BigLake API ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Reference ](https://docs.cloud.google.com/lakehouse/docs/quotas)



#  Method: deltasharing.v1.projects.catalogs.shares.schemas.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * DeltaSharingSchema
    * JSON representation



Gets a list of Delta Sharing schemas available in the upstream SAP BDC source.

### HTTP request

`GET https://biglake.googleapis.com/deltasharing/v1/{parent=projects/*/catalogs/*/shares/*}/schemas`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The name of the share. Format: projects/{project}/catalogs/{catalog}/shares/{delta_sharing_share}  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of schemas to return. The service may return fewer than this value. If unspecified, at most 100 schemas will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` Optional. A page token, received from a previous `schemas.list` call.  
  
### Request body

The request body must be empty.

### Response body

Response message for the schemas.list method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "deltaSharingSchemas": [
        {
          object ([DeltaSharingSchema](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/deltasharing.v1.projects.catalogs.shares.schemas/list#DeltaSharingSchema))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`deltaSharingSchemas[]` |  `object (`[DeltaSharingSchema](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/deltasharing.v1.projects.catalogs.shares.schemas/list#DeltaSharingSchema)`)` The Delta Sharing schemas from the specified share.  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/bigquery`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## DeltaSharingSchema

Represents a Delta Sharing Schema.

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name. Format: projects/{project}/catalogs/{catalog}/shares/{delta_sharing_share}/schemas/{delta_sharing_schema}  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-28 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-28 UTC."],[],[]] 
