---
url: https://docs.cloud.google.com/bigtable/docs/connection-pools/
title: Connection pools \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:29:12.188744+00:00
---

# Connection pools  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/connection-pools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Connection pools

This topic describes how connection pools work in Bigtable, the impacts that connection pool size can have on an application that uses Bigtable, and when you might want to change the default connection pool settings.

After you read this page, if you determine that you should change your connection pool size, see [Configuring connection pools](https://docs.cloud.google.com/bigtable/docs/configure-connection-pools) to learn how to determine the optimal size and how to change it. The number of connections in each pool is configurable in your code only when you use the Go, C++, or Java client libraries for Cloud Bigtable.

## How connection pools work

A _connection pool_ , also known as a _channel pool_ , is a cache of database connections that are shared and reused to improve connection latency and performance. Connections are used in a round robin system.

When you use Bigtable, you create a single data client per application process. Each client has one connection pool. Each connection pool contains some number of gRPC connections, which can each handle up to 100 concurrent streams. Requests sent through these connections pass through Google middleware, which then routes them to your table. The middleware layer is made up of many load-balanced instances, and each request is routed through the middleware instance that has the most availability.

You can think of a _connection_ (or channel) like a highway that has up to 100 lanes, and each lane (stream) can only contain one car (request) at any given time. The limit of 100 concurrent streams per gRPC connection is enforced in Google's middleware layer, and you are not able to reconfigure this number.

A connection automatically refreshes itself once every hour. Additionally, if a connection has not seen a request in five minutes, the middleware automatically deletes the connection and doesn't recreate it until an additional connection is needed.

Behind the scenes, each channel has a single subchannel. Each subchannel has an HTTP2 connection that uses TCP to convert requests to bytes and send them through the middleware and then to your table. This process is handled seamlessly by the Bigtable service, and you don't need to configure anything to make it happen.

![Connection pools and traffic](https://docs.cloud.google.com/static/bigtable/img/connection-pools-traffic.svg)

## How connection pools affect performance

Ideally, you should have enough gRPC connections to handle your requests without any buffering. However, you should not have so many connections that they are frequently dropped because of lack of use.

### Not enough connections

If a connection pool does not have enough connections to handle your traffic, the middleware starts to buffer and queue requests. This buffering slows down the traffic, reducing the number of requests per second and increasing latency as the requests back up.

### Too many connections

If a pool has too many connections, meaning some of the connections are idle, the middleware disconnects the idle connections. Then when new requests come through that require them, these connections are reestablished. This means that when traffic increases, requests can encounter a server-side cache miss, causing extra work and latency. If this happens frequently because of varying traffic levels, this activity can manifest as a perceived spike in tail latency on the client side.

**Note:** In most cases, you cannot control the refresh cadence. However, If this tail latency is a concern and you need predictable latency at a low rate of queries per second (QPS), and you are using the [Cloud Bigtable client library for Java](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/overview), you are able to configure the refresh settings using the `BigtableDataSettings.Builder` class. If you are using the [Cloud Bigtable client library for Go](https://godoc.org/cloud.google.com/go/bigtable), see the [Connection Refresh Example](https://github.com/GoogleCloudPlatform/cloud-bigtable-examples/tree/master/go/connection-refresh) on GitHub.

## When to change the default settings

**The default connection pool size is right for most applications, and in most cases there's no need to change it.** Depending on the client library you use in your application, you might not be able to change your connection pool size. The number of connections in each pool is configurable in your code **only when you use the Go, C++, or Java client libraries for Cloud Bigtable**.

As a general rule, an ideal connection pool has at least twice the number of connections that it takes for maximum saturation. This leaves room for traffic fluctuations. For example, if you have 4 connections and they are each handling the maximum number of requests possible (100), you want to bring the number of requests per connection down to a number between 10 and 50, so the ideal connection pool size is at least double that, or a minimum of 8 connections.

Signals that you should consider changing the number of connections in the pool include the following:

### Low throughput combined with spikes in client-side tail latency

If your typical throughput is fairly low, such as less than one request per second per connection, and you observe periodically high tail latency for your application, you might not be sending enough traffic to keep the connections alive. In this case, you might need to lower the number of connections in the pool. See [Configuring connection pools](https://docs.cloud.google.com/bigtable/docs/configure-connection-pools) to learn how to determine the right number.

### Buffered requests

If you observe that requests are stacking up on the client side, this might indicate that you are sending more concurrent requests than the connection pool can handle. [Calculate the optimal number](https://docs.cloud.google.com/bigtable/docs/configure-connection-pools), then change your code if you need to.

To determine whether requests are stacking up, you can use [OpenCensus](https://opencensus.io/guides/grpc/java/#examining-metrics) to look at the difference between the `grpc.io/client/started_rpcs` and `grpc.io/client/completed_rpcs` metrics.

### Virtual environment

In some rare cases, the Bigtable client is not able to tell the number of CPUs that the application is running on and allocates connections as if only one CPU is in use. For example, this can happen when you use virtual CPU instances in Kubernetes or Docker. If this is evident, you should configure the number of pools [according to the guidelines](https://docs.cloud.google.com/bigtable/docs/configure-connection-pools) based on your application's QPS and latency.

## What's Next

  * Learn how to [configure connection pools](https://docs.cloud.google.com/bigtable/docs/configure-connection-pools).
  * Read more about [performance](https://docs.cloud.google.com/bigtable/docs/performance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
