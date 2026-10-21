---
url: https://docs.cloud.google.com/spanner/docs/api-libraries-overview/
title: Overview of APIs, client libraries, and ORM drivers \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:36.434822+00:00
---

# Overview of APIs, client libraries, and ORM drivers  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/api-libraries-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  Overview of APIs, client libraries, and ORM drivers Stay organized with collections  Save and categorize content based on your preferences. 

## Available interfaces

You can use one of several programmatic interfaces when interacting with Spanner. These are the available interfaces, in the order that we recommend using them:

  * [Client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries): The Spanner client libraries are available in multiple languages and are built on [gRPC](https://grpc.io/). These client libraries provide a layer of abstraction on top of gRPC and handle the details of session management, transaction execution, retries, and more.
  * [ORM and framework drivers](https://docs.cloud.google.com/spanner/docs/drivers-overview): Google supports open-source Spanner drivers for several popular object-relational mapping libraries (ORMs) and frameworks, such as JDBC. These drivers allow the use of Spanner databases through APIs defined by those frameworks.
  * [RPC API](https://docs.cloud.google.com/spanner/docs/reference/rpc): If a client library or ORM driver is not available for your programming language of choice, use the RPC API, which is built on [gRPC](https://grpc.io/). gRPC offers a number of performance benefits compared with using the REST API, including representing objects in protocol buffer format (which are faster to produce and consume compared with JSON) and persistent connections (which result in less per-request overhead). Read more about these and other benefits in [gRPC Concepts](https://grpc.io/docs/guides/concepts/).
  * [REST API](https://docs.cloud.google.com/spanner/docs/reference/rest): If you're unable to use Spanner's client libraries or the RPC API, use the REST API. Note that some features that are available in the RPC API are not supported in the REST API, as documented below.



## RPC versus REST API

This table compares Spanner features available through its RPC and REST API interfaces.

Feature | Supported in the [RPC API](https://docs.cloud.google.com/spanner/docs/reference/rpc)? | Supported in the [REST API?](https://docs.cloud.google.com/spanner/docs/reference/rest)  
---|---|---  
Cancelling a request |  Yes |  No  
Setting a deadline or timeout on a request |  Yes |  No  
Sending a streaming request |  Yes. see [`ExecuteStreamingSQL`](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.v1#google.spanner.v1.Spanner.ExecuteStreamingSql) and [`StreamingRead`](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.v1#google.spanner.v1.Spanner.StreamingRead). | __Partial.[HTTP Streaming](https://docs.cloud.google.com/apis/docs/http#streaming) is supported but application-level [flow control](https://docs.cloud.google.com/apis/docs/http#flow_control) is not.  
  
## Client libraries features support

The following table lists the client libraries, noting the major Spanner features that each one supports.

Client | [Go](https://pkg.go.dev/cloud.google.com/go/spanner) | [Java](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/overview) | [Node.js](https://googleapis.dev/nodejs/spanner/latest/) | [Python](https://docs.cloud.google.com/python/docs/reference/spanner/latest) | [Ruby](https://googleapis.dev/ruby/google-cloud-spanner/latest/Google/Cloud/Spanner.html) | [C++](https://docs.cloud.google.com/cpp/docs/reference/spanner/latest) | [PHP](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/v0.189.0/spanner/readme) | [C#](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest)  
---|---|---|---|---|---|---|---|---  
[Batch DDL](https://docs.cloud.google.com/spanner/docs/schema-updates#order_of_execution_of_statements_in_batches) |  |  |  |  |  |  |  |   
[Batch DML](https://docs.cloud.google.com/spanner/docs/samples/spanner-dml-batch-update) |  |  |  |  |  |  |  |   
[Configurable leader option](https://docs.cloud.google.com/spanner/docs/modifying-leader-region) |  |  |  |  |  |  |  |   
[Graph queries](https://docs.cloud.google.com/spanner/docs/graph/queries-overview) |  |  |  |  |  |  |  |   
[Interleaved tables](https://docs.cloud.google.com/spanner/docs/schema-and-data-model#parent-child) |  |  |  |  |  |  |  |   
[JSON type](https://docs.cloud.google.com/spanner/docs/working-with-json) |  |  |  |  |  |  |  |   
[Mutations](https://docs.cloud.google.com/spanner/docs/modify-mutation-api) |  |  |  |  |  |  |  |   
[Partitioned DML](https://docs.cloud.google.com/spanner/docs/dml-partitioned) |  |  |  |  |  |  |  |   
[Partitioned read](https://docs.cloud.google.com/spanner/docs/reads#read_data_in_parallel) |  |  |  |  |  |  |  |   
[PostgreSQL interface](https://docs.cloud.google.com/spanner/docs/postgresql-interface) |  |  |  |  |  |  |  |   
[Request priority](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/RequestOptions#Priority) |  |  |  |  |  |  |  |   
[Request tagging](https://docs.cloud.google.com/spanner/docs/introspection/troubleshooting-with-tags) |  |  |  |  |  |  |  |   
[Session labeling](https://docs.cloud.google.com/spanner/docs/sessions) |  |  |  |  |  |  |  |   
[Stale reads](https://docs.cloud.google.com/spanner/docs/reads) |  |  |  |  |  |  |  |   
[Statement hints](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/query-syntax#statement-hints) |  |  |  |  |  |  |  |   
[Client metrics](https://docs.cloud.google.com/spanner/docs/view-manage-client-side-metrics) |  |  |  |  |  |  |  |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
