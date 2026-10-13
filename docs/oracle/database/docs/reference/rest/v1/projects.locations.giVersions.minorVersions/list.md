---
url: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.giVersions.minorVersions/list/
title: Method: projects.locations.giVersions.minorVersions.list \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:52:03.656158+00:00
---

# Method: projects.locations.giVersions.minorVersions.list  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.giVersions.minorVersions/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Reference ](https://docs.cloud.google.com/oracle/database/docs/apis)



Send feedback 

#  Method: projects.locations.giVersions.minorVersions.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * MinorVersion
    * JSON representation



Lists all the valid minor versions for the given project, location, gi version and shape family.

### HTTP request

Choose a location:

global asia-northeast2 asia-south2 asia-south1 australia-southeast2 europe-west8 northamerica-northeast2

  
`GET https://oracledatabase.googleapis.com/v1/{parent=projects/*/locations/*/giVersions/*}/minorVersions`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent value for the MinorVersion resource with the format: projects/{project}/locations/{location}/giVersions/{giVersion}  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of items to return. If unspecified, a maximum of 50 System Versions will be returned. The maximum value is 1000; values above 1000 will be reset to 1000.  
`pageToken` |  `string` Optional. A token identifying the requested page of results to return. All fields except the filter should remain the same as in the request that provided this page token.  
`filter` |  `string` Optional. An expression for filtering the results of the request. Only shapeFamily and gcp_oracle_zone_id are supported in this format: `shape_family="{shapeFamily}" AND gcp_oracle_zone_id="{gcp_oracle_zone_id}"`.  
  
### Request body

The request body must be empty.

### Response body

The response for `MinorVersion.List`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "minorVersions": [
        {
          object ([MinorVersion](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.giVersions.minorVersions/list#MinorVersion))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`minorVersions[]` |  `object (`[MinorVersion](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.giVersions.minorVersions/list#MinorVersion)`)` The list of MinorVersions.  
`nextPageToken` |  `string` A token identifying a page of results the server should return.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/oracle-database`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `oracledatabase.minorVersions.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## MinorVersion

MinorVersion represents a minor version of a GI. <https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/GiMinorVersionSummary/>

JSON representation  
---  
      
    
    {
      "name": string,
      "gridImageId": string,
      "version": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the MinorVersion resource with the format: projects/{project}/locations/{region}/giVersions/{giVersion}/minorVersions/{minor_version}  
`gridImageId` |  `string` Optional. The ID of the Grid Image.  
`version` |  `string` Optional. The valid Oracle grid infrastructure software version.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
