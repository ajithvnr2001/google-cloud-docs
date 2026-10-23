---
url: https://docs.cloud.google.com/spanner/docs/latency-points/
title: Latency points in a Spanner request \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:21.626009+00:00
---

# Latency points in a Spanner request  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/latency-points/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Latency points in a Spanner request Stay organized with collections  Save and categorize content based on your preferences. 

This page gives an overview of the high-level components involved in a Spanner request and how each component can affect latency.

## Spanner API requests

The high-level components that are used to make a Spanner API request include:

  * [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries), which provide a layer of abstraction on top of gRPC, and handle server communication details, such as session management, transactions, and retries.

  * The Google Front End (GFE), which is an infrastructure service that's common to all Google Cloud services, including Spanner. The GFE verifies that all Transport Layer Security (TLS) connections are stopped and applies protections against Denial of Service attacks. To learn more about the GFE, see [ Google Front End Service](https://docs.cloud.google.com/docs/security/infrastructure/design#google-frontend-service).

  * The Spanner API frontend (AFE), which performs various checks on the API request (including authentication, authorization, and quota checks) , and maintains sessions and transaction states.

  * The Spanner database, which executes reads and writes to the database.




When you make a remote procedure call to Spanner, the Spanner client libraries prepare the API request. Then, the API request passes through both the GFE and the Spanner AFE before reaching the Spanner database.

By measuring and comparing the request latencies between different components and the database, you can determine which component is causing the problem. These latencies include client end-to-end, GFE, Spanner API request, and query latencies.

![Spanner architecture diagram.](https://docs.cloud.google.com/static/spanner/docs/images/latency_breakdown.png)

The following sections explain each type of latency you see in the previous diagram.

## Direct connectivity

Application traffic that meets certain criteria can be routed directly to Spanner, bypassing the Google Front End (GFE) and optimizing performance. Direct connectivity can be turned on for applications that satisfy the following criteria:

  * Running on Compute Engine or Google Kubernetes Engine.
  * Use the [**global endpoint**](https://docs.cloud.google.com/spanner/docs/endpoints).
  * In a network configured with routes and firewall rules that allow egress traffic to reach `34.126.0.0/18` and `2001:4860:8040::/42`.
  * Uses the client library versions: 
    * **Java** : 6.111.0 or later.
    * **Go** : 1.88.0 or later.
  * The credentials you use for the applications have the [`spanner.databases.get`](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databases.get) permission.



This feature can be enabled by setting the `GOOGLE_SPANNER_ENABLE_DIRECT_ACCESS` environment variable to `true` or through your client library configuration ( [`setEnableDirectAccess(true)`](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.Builder#com_google_cloud_spanner_SpannerOptions_Builder_setEnableDirectAccess_boolean_) in Java, [`ClientConfig.EnableDirectAccess`](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest#cloud_google_com_go_spanner_ClientConfig) in Go, or connection property `enableDirectAccess=true` in the [JDBC driver](https://docs.cloud.google.com/spanner/docs/getting-started/jdbc)).

To verify if Spanner direct connectivity is being used, monitor the usage labels in your [client-side metrics](https://docs.cloud.google.com/spanner/docs/client-side-metrics-descriptions).

## End-to-end latency

End-to-end latency is the length of time (in milliseconds) between the first byte of the Spanner API request that the client sends to the database (through both the GFE and the Spanner API front end), and the last byte of response that the client receives from the database.

![Spanner architecture diagram for end-to-end latency.](https://docs.cloud.google.com/static/spanner/docs/images/client-round-trip-latency.png)

The [ `spanner.googleapis.com/client/operation_latencies`](https://docs.cloud.google.com/spanner/docs/client-side-metrics-descriptions#operation-latencies) metric provides the time between the first byte of the API request sent to the last byte of the response received. This includes retries performed by the client library.

For more information, see [View and manage client-side metrics](https://docs.cloud.google.com/spanner/docs/view-manage-client-side-metrics).

**Note:** You can also use OpenTelemetry to capture and visualize end-to-end latency. For more information, see [Capture custom client-side metrics using OpenTelemetry](https://docs.cloud.google.com/spanner/docs/capture-custom-metrics-opentelemetry).

## GFE latency

Google Front End (GFE) latency is the length of time (in milliseconds) between when the Google network receives a remote procedure call from the client and when the GFE receives the first byte of the response. This latency doesn't include any TCP/SSL handshake.

![Spanner architecture diagram for GFE latency.](https://docs.cloud.google.com/static/spanner/docs/images/google-front-end-latency.png)

Every response from Spanner (REST or gRPC) includes a header that contains the total time between the GFE and the backend (the Spanner service) for the request and the response. This helps to differentiate better the source of the latency between the client and the GFE.

The [`spanner.googleapis.com/client/gfe_latencies`](https://docs.cloud.google.com/spanner/docs/client-side-metrics-descriptions#gfe-latencies) metric captures and exposes GFE latency for Spanner requests.

For more information, see [View and manage client-side metrics](https://docs.cloud.google.com/spanner/docs/view-manage-client-side-metrics).

**Note:** You can also use OpenTelemetry to capture and visualize GFE latency. For more information, see [Capture custom client-side metrics using OpenTelemetry](https://docs.cloud.google.com/spanner/docs/capture-custom-metrics-opentelemetry).

## Spanner API request latency

Spanner API request latency is the length of time (in seconds) from when the Spanner AFE receives the first byte of a request to when the Spanner API frontend sends the last byte of a response. The latency includes the time needed for processing API requests in both the Spanner backend and the API layer. However, this latency doesn't include network or reverse-proxy overhead between Spanner clients and servers.

![Spanner architecture diagram for Spanner API request latency.](https://docs.cloud.google.com/static/spanner/docs/images/cloud-spanner-API-request-latency.png)

The `spanner.googleapis.com/api/request_latencies` metric captures and exposes Spanner AFE latency for Spanner requests. For more information, see [Spanner metrics](https://docs.cloud.google.com/spanner/docs/metrics).

## Query latency

Query latency is the length of time (in milliseconds) that it takes to run SQL queries in the Spanner database.

![Spanner architecture diagram for query latency.](https://docs.cloud.google.com/static/spanner/docs/images/query-latency.png)

Query latency is available for the [executeSql](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.v1#ExecuteSqlRequest) API.

If the [`QueryMode`](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.v1#querymode) parameter is set to `WITH_STATS` or `WITH_PLAN_AND_STATS`, then Spanner's [`ResultSetStats`](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.v1#resultsetstats) are available in the responses. `ResultSetStats` includes the elapsed time for running queries in the Spanner database.

To capture and visualize query latency, see [Capture query latency with OpenTelemetry](https://docs.cloud.google.com/spanner/docs/capture-custom-metrics-opentelemetry#capture-query-latency).

## What's next

  * Learn how to [identify latency points](https://docs.cloud.google.com/spanner/docs/identify-latency-point) in Spanner components.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
