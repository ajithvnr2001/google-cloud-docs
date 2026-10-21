---
url: https://docs.cloud.google.com/healthcare-api/docs/best-practices-network-latency/
title: Network latency best practices \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:16:22.980832+00:00
---

# Network latency best practices  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/best-practices-network-latency/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)



Send feedback 

#  Network latency best practices Stay organized with collections  Save and categorize content based on your preferences. 

This document lists best practices for using the Cloud Healthcare API. The guidelines in this page are designed for greater efficiency, accuracy, and optimal response times from the service.

## Understanding latency performance

The performance of the Cloud Healthcare API is measured by the latency between:

  1. When you send a request to the Cloud Healthcare API.
  2. When you receive a full response to the request.



Latency comprises three components:

  * Round-trip time (RTT)
  * Server processing latency
  * Server throughput



The geographical distance between you and the server you are making requests to can have a significant impact on RTT and server throughput. The measured inter-region latency and throughput for Google Cloud networks can be found in a [live dashboard](https://lookerstudio.google.com/c/u/0/reporting/fc733b10-9744-4a72-a502-92290f608571/page/70YCB). The dashboard shows the performance a client can expect from different locations when making requests to Cloud Healthcare API servers.

## Measuring latency performance

The following tools and dashboards provide ways to measure the performance of requests to and from Cloud Healthcare API servers:

  * **Google Cloud console latency metrics** : You can view the server-side latency of Cloud Healthcare API requests in the [Google Cloud console](https://console.cloud.google.com/apis/api/healthcare.googleapis.com/metrics). For more information, see [Google Cloud metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp).

  * **Cloud Logging custom metrics** : You can [create distribution metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics/distribution-metrics) using Logging. Distribution metrics let you configure and understand end-to-end latency in your applications. You can also monitor and report on any custom-defined latency measurements.

  * **Chrome network panel** : You can [inspect network activity in Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools/network) to view the performance details of an HTTP request sent from a browser.




## Reducing request latency

This section describes various methods of reducing the latency of requests sent to the Cloud Healthcare API.

### Sending requests to the closest regional location

To get the best RTT and server throughput performance, send requests from the client to the closest Cloud Healthcare API regional location. See [Regions](https://docs.cloud.google.com/healthcare-api/docs/concepts/regions) for a list of available regions.

### Sending warmup requests

When a client sends requests to a Cloud Healthcare API server for the first time during a session, the client performs TCP handshakes with the server to establish connections for HTTP requests. Any subsequent requests can continue to use these established connections, allowing the client to avoid the TCP overhead typically associated with a request. This results in better performance when sending requests.

### Sending requests concurrently with HTTP/1.1 or HTTP/2

To obtain the best performance for a series of requests, send the requests concurrently. Use the following guidelines when sending concurrent requests:

  * When sending concurrent requests, try to find an ideal number for the number of concurrent requests. The ideal number depends on several factors including your hardware and network capabilities and how many requests are being sent. Conduct tests to find the ideal number.
  * Send requests from the client using HTTP/2 whenever possible. HTTP/2 provides better performance than HTTP/1.1 because HTTP/2 requires only one TCP connection when sending multiple requests sequentially or concurrently. As a result, you can avoid TCP handshake overhead.
  * If it's not possible to use HTTP/2, use HTTP/1.1 with a persistent connection. You can avoid TCP handshake overhead if warmup requests have already been sent. Using a persistent connection might require you to manage an optimized connection with a connection pool for your HTTP library.

For example, to set a connection pool with 20 concurrent requests using the [Google HTTP client library for Java](https://github.com/googleapis/google-http-java-client), your code would include the following:
        
        PoolingHttpClientConnectionManager cm = new PoolingHttpClientConnectionManager();
        // Support 20 concurrent requests.
        cm.setDefaultMaxPerRoute(20);
        cm.setMaxTotal(100);
        HTTP_CLIENT = HttpClients.custom().setConnectionManager(cm).build();
        

To set a connection pool with 20 concurrent requests using Node.js, your code would include the following:
        
        require('http').globalAgent.maxSockets = 20
        




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
