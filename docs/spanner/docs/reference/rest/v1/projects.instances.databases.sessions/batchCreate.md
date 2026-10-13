---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/batchCreate/
title: Method: projects.instances.databases.sessions.batchCreate \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:10.513790+00:00
---

# Method: projects.instances.databases.sessions.batchCreate  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/batchCreate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  Method: projects.instances.databases.sessions.batchCreate Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Creates multiple new sessions.

This API can be used to initialize a session cache on the clients. See <https://goo.gl/TgSFN2> for best practices on session cache management.

### HTTP request

Choose a location:

global europe-west8 me-central2 us-central1 us-central2 us-east1 us-east4 us-east5 us-south1 us-west1 us-west2 us-west3 us-west4 us-west8 us-east7

  
`POST https://spanner.googleapis.com/v1/{database=projects/*/instances/*/databases/*}/sessions:batchCreate`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`database` |  `string` Required. The database in which the new sessions are created. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `database`:

  * `spanner.sessions.create`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "sessionTemplate": {
        object ([Session](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions#Session))
      },
      "sessionCount": integer
    }  
  
Fields  
---  
`sessionTemplate` |  `object (`[Session](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions#Session)`)` Parameters to apply to each created session.  
`sessionCount` |  `integer` Required. The number of sessions to be created in this batch call. At least one session is created. The API can return fewer than the requested number of sessions. If a specific number of sessions are desired, the client can make additional calls to `sessions.batchCreate` (adjusting `[sessionCount](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/batchCreate#body.request_body.FIELDS.session_count)` as necessary).  
  
### Response body

The response for `[sessions.batchCreate](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/batchCreate#google.spanner.v1.Spanner.BatchCreateSessions)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "session": [
        {
          object ([Session](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions#Session))
        }
      ]
    }  
  
Fields  
---  
`session[]` |  `object (`[Session](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions#Session)`)` The freshly created sessions.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.data`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-12 UTC."],[],[]] 
