---
url: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudExadataInfrastructures/configureExascale/
title: Method: projects.locations.cloudExadataInfrastructures.configureExascale \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:41.467858+00:00
---

# Method: projects.locations.cloudExadataInfrastructures.configureExascale  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudExadataInfrastructures/configureExascale/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Reference ](https://docs.cloud.google.com/oracle/database/docs/apis)



Send feedback 

#  Method: projects.locations.cloudExadataInfrastructures.configureExascale Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions



Configures Exascale for a single Exadata Infrastructure.

### HTTP request

Choose a location:

global asia-northeast2 asia-south2 asia-south1 australia-southeast2 europe-west8 northamerica-northeast2

  
`POST https://oracledatabase.googleapis.com/v1/{name=projects/*/locations/*/cloudExadataInfrastructures/*}:configureExascale`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the Cloud Exadata Infrastructure in the following format: projects/{project}/locations/{location}/cloudExadataInfrastructures/{cloudExadataInfrastructure}.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "totalStorageSizeGb": integer,
      "requestId": string
    }  
  
Fields  
---  
`totalStorageSizeGb` |  `integer` Required. The total storage to be allocated to Exascale in GBs.  
`requestId` |  `string` Optional. An optional ID to identify the request.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.operations#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/oracle-database`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `oracledatabase.cloudExadataInfrastructures.update`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
