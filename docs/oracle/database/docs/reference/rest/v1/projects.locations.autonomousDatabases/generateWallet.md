---
url: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases/generateWallet/
title: Method: projects.locations.autonomousDatabases.generateWallet \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:40.589074+00:00
---

# Method: projects.locations.autonomousDatabases.generateWallet  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases/generateWallet/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Reference ](https://docs.cloud.google.com/oracle/database/docs/apis)



Send feedback 

#  Method: projects.locations.autonomousDatabases.generateWallet Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * GenerateType



Generates a wallet for an Autonomous Database.

### HTTP request

Choose a location:

global asia-northeast2 asia-south2 asia-south1 australia-southeast2 europe-west8 northamerica-northeast2

  
`POST https://oracledatabase.googleapis.com/v1/{name=projects/*/locations/*/autonomousDatabases/*}:generateWallet`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the Autonomous Database in the following format: projects/{project}/locations/{location}/autonomousDatabases/{autonomousDatabase}.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "type": enum ([GenerateType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases/generateWallet#GenerateType)),
      "isRegional": boolean,
      "password": string
    }  
  
Fields  
---  
`type` |  `enum (`[GenerateType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases/generateWallet#GenerateType)`)` Optional. The type of wallet generation for the Autonomous Database. The default value is SINGLE.  
`isRegional` |  `boolean` Optional. True when requesting regional connection strings in PDB connect info, applicable to cross-region Data Guard only.  
`password` |  `string` Required. The password used to encrypt the keys inside the wallet. The password must be a minimum of 8 characters.  
  
### Response body

The response for `AutonomousDatabase.GenerateWallet`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "archiveContent": string
    }  
  
Fields  
---  
`archiveContent` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Output only. The base64 encoded wallet files.A base64-encoded string.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/oracle-database`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `oracledatabase.autonomousDatabases.generateWallet`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## GenerateType

The type of wallet generation.

Enums  
---  
`GENERATE_TYPE_UNSPECIFIED` | Default unspecified value.  
`ALL` | Used to generate wallet for all databases in the region.  
`SINGLE` | Used to generate wallet for a single database.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
