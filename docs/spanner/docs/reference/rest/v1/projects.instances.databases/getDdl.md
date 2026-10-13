---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/getDdl/
title: Method: projects.instances.databases.getDdl \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:05.308153+00:00
---

# Method: projects.instances.databases.getDdl  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/getDdl/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  Method: projects.instances.databases.getDdl Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Returns the schema of a Cloud Spanner database as a list of formatted DDL statements. This method does not show pending schema updates, those may be queried using the `Operations` API.

### HTTP request

Choose a location:

global europe-west8 me-central2 us-central1 us-central2 us-east1 us-east4 us-east5 us-south1 us-west1 us-west2 us-west3 us-west4 us-west8 us-east7

  
`GET https://spanner.googleapis.com/v1/{database=projects/*/instances/*/databases/*}/ddl`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`database` |  `string` Required. The database whose schema we wish to get. Values are of the form `projects/<project>/instances/<instance>/databases/<database>` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `database`:

  * `spanner.databases.getDdl`

  
  
### Request body

The request body must be empty.

### Response body

The response for `[databases.getDdl](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/getDdl#google.spanner.admin.database.v1.DatabaseAdmin.GetDatabaseDdl)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "statements": [
        string
      ],
      "protoDescriptors": string
    }  
  
Fields  
---  
`statements[]` |  `string` A list of formatted DDL statements defining the schema of the database specified in the request.  
`protoDescriptors` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Proto descriptors stored in the database. Contains a protobuf-serialized [google.protobuf.FileDescriptorSet](https://github.com/protocolbuffers/protobuf/blob/main/src/google/protobuf/descriptor.proto). For more details, see protobuffer [self description](https://developers.google.com/protocol-buffers/docs/techniques#self-description).A base64-encoded string.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.admin`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-12 UTC."],[],[]] 
