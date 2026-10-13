---
url: https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/grpc.lookup.v1
title: Package grpc.lookup.v1 \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:26:27.007740+00:00
---

# Package grpc.lookup.v1  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/grpc.lookup.v1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Reference ](https://docs.cloud.google.com/bigtable/docs/apis)



Send feedback 

#  Package grpc.lookup.v1 Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[RouteLookupService](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/grpc.lookup.v1#grpc.lookup.v1.RouteLookupService)` (interface)
  * `[RouteLookupRequest](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/grpc.lookup.v1#grpc.lookup.v1.RouteLookupRequest)` (message)
  * `[RouteLookupRequest.Reason](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/grpc.lookup.v1#grpc.lookup.v1.RouteLookupRequest.Reason)` (enum)
  * `[RouteLookupResponse](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/grpc.lookup.v1#grpc.lookup.v1.RouteLookupResponse)` (message)



## RouteLookupService

RouteLookup  
---  
` rpc RouteLookup(`[RouteLookupRequest](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/grpc.lookup.v1#grpc.lookup.v1.RouteLookupRequest)`) returns (`[RouteLookupResponse](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/grpc.lookup.v1#grpc.lookup.v1.RouteLookupResponse)`) ` Lookup returns a target for a single key.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/bigtable.data`
  * `https://www.googleapis.com/auth/cloud-bigtable.data`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
  
## RouteLookupRequest

Fields  
---  
`target_type` |  `string` Target type allows the client to specify what kind of target format it would like from RLS to allow it to find the regional server, e.g. "grpc".  
`reason` |  `[Reason](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/grpc.lookup.v1#grpc.lookup.v1.RouteLookupRequest.Reason)` Reason for making this request.  
`stale_header_data` |  `string` For REASON_STALE, the header_data from the stale response, if any.  
`key_map` |  `map<string, string>` Map of key values extracted via key builders for the gRPC or HTTP request.  
`extensions[]` |  `[Any](https://protobuf.dev/reference/protobuf/google.protobuf/#any)` Application-specific optional extensions.  
  
## Reason

Possible reasons for making a request.

Enums  
---  
`REASON_UNKNOWN` | Unused  
`REASON_MISS` | No data available in local cache  
`REASON_STALE` | Data in local cache is stale  
  
## RouteLookupResponse

Fields  
---  
`targets[]` |  `string` Prioritized list (best one first) of addressable entities to use for routing, using syntax requested by the request target_type. The targets will be tried in order until a healthy one is found.  
`header_data` |  `string` Optional header value to pass along to AFE in the X-Google-RLS-Data header. Cached with "target" and sent with all requests that match the request key. Allows the RLS to pass its work product to the eventual target.  
`extensions[]` |  `[Any](https://protobuf.dev/reference/protobuf/google.protobuf/#any)` Application-specific optional extensions.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-08 UTC."],[],[]] 
