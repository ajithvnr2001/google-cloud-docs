---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/adaptMessage/
title: Method: projects.instances.databases.sessions.adaptMessage \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:09.978470+00:00
---

# Method: projects.instances.databases.sessions.adaptMessage  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/adaptMessage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  Method: projects.instances.databases.sessions.adaptMessage Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Handles a single message from the client and returns the result as a stream. The server will interpret the message frame and respond with message frames to the client.

### HTTP request

Choose a location:

global europe-west8 me-central2 us-central1 us-central2 us-east1 us-east4 us-east5 us-south1 us-west1 us-west2 us-west3 us-west4 us-west8 us-east7

  
`POST https://spanner.googleapis.com/v1/{name=projects/*/instances/*/databases/*/sessions/*}:adaptMessage`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The database session in which the adapter request is processed. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `spanner.databases.adapt`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "protocol": string,
      "payload": string,
      "attachments": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`protocol` |  `string` Required. Identifier for the underlying wire protocol.  
`payload` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Optional. Uninterpreted bytes from the underlying wire protocol.A base64-encoded string.  
`attachments` |  `map (key: string, value: string)` Optional. Opaque request state passed by the client to the server.  
  
### Response body

Message sent by the adapter to the client.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "payload": string,
      "stateUpdates": {
        string: string,
        ...
      },
      "last": boolean
    }  
  
Fields  
---  
`payload` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Optional. Uninterpreted bytes from the underlying wire protocol.A base64-encoded string.  
`stateUpdates` |  `map (key: string, value: string)` Optional. Opaque state updates to be applied by the client.  
`last` |  `boolean` Optional. Indicates whether this is the last `[AdaptMessageResponse](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/adaptMessage#body.AdaptMessageResponse)` in the stream. This field may be optionally set by the server. Clients should not rely on this field being set in all cases.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.data`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-12 UTC."],[],[]] 
