---
url: https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.adapter.v1
title: Package google.spanner.adapter.v1 \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:25.196778+00:00
---

# Package google.spanner.adapter.v1  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.adapter.v1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  Package google.spanner.adapter.v1 Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[Adapter](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.adapter.v1#google.spanner.adapter.v1.Adapter)` (interface)
  * `[AdaptMessageRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.adapter.v1#google.spanner.adapter.v1.AdaptMessageRequest)` (message)
  * `[AdaptMessageResponse](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.adapter.v1#google.spanner.adapter.v1.AdaptMessageResponse)` (message)
  * `[CreateSessionRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.adapter.v1#google.spanner.adapter.v1.CreateSessionRequest)` (message)
  * `[Session](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.adapter.v1#google.spanner.adapter.v1.Session)` (message)



## Adapter

Cloud Spanner Adapter API

The Cloud Spanner Adapter service allows native drivers of supported database dialects to interact directly with Cloud Spanner by wrapping the underlying wire protocol used by the driver in a gRPC stream.

AdaptMessage  
---  
` rpc AdaptMessage(`[AdaptMessageRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.adapter.v1#google.spanner.adapter.v1.AdaptMessageRequest)`) returns (`[AdaptMessageResponse](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.adapter.v1#google.spanner.adapter.v1.AdaptMessageResponse)`) ` Handles a single message from the client and returns the result as a stream. The server will interpret the message frame and respond with message frames to the client.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.data`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
CreateSession  
---  
` rpc CreateSession(`[CreateSessionRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.adapter.v1#google.spanner.adapter.v1.CreateSessionRequest)`) returns (`[Session](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.adapter.v1#google.spanner.adapter.v1.Session)`) ` Creates a new session to be used for requests made by the adapter. A session identifies a specific incarnation of a database resource and is meant to be reused across many `AdaptMessage` calls.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.data`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
  
## AdaptMessageRequest

Message sent by the client to the adapter.

Fields  
---  
`name` |  `string` Required. The database session in which the adapter request is processed. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `spanner.databases.adapt`

  
`protocol` |  `string` Required. Identifier for the underlying wire protocol.  
`payload` |  `bytes` Optional. Uninterpreted bytes from the underlying wire protocol.  
`attachments` |  `map<string, string>` Optional. Opaque request state passed by the client to the server.  
  
## AdaptMessageResponse

Message sent by the adapter to the client.

Fields  
---  
`payload` |  `bytes` Optional. Uninterpreted bytes from the underlying wire protocol.  
`state_updates` |  `map<string, string>` Optional. Opaque state updates to be applied by the client.  
`last` |  `bool` Optional. Indicates whether this is the last `[AdaptMessageResponse](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.adapter.v1#google.spanner.adapter.v1.AdaptMessageResponse)` in the stream. This field may be optionally set by the server. Clients should not rely on this field being set in all cases.  
  
## CreateSessionRequest

The request for [CreateSessionRequest][Adapter.CreateSessionRequest].

Fields  
---  
`parent` |  `string` Required. The database in which the new session is created. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `spanner.sessions.create`

  
`session` |  `[Session](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.adapter.v1#google.spanner.adapter.v1.Session)` Required. The session to create.  
  
## Session

A session in the Cloud Spanner Adapter API.

Fields  
---  
`name` |  `string` Identifier. The name of the session. This is always system-assigned.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-01 UTC."],[],[]] 
