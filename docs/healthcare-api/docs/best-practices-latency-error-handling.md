---
url: https://docs.cloud.google.com/healthcare-api/docs/best-practices-latency-error-handling/
title: Request latency and error handling best practices \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:09:24.569895+00:00
---

# Request latency and error handling best practices  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/best-practices-latency-error-handling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Request latency and error handling best practices Stay organized with collections  Save and categorize content based on your preferences. 

This page describes best practices for optimizing request latency and handling errors in the Cloud Healthcare API. Implement these practices as you plan and design your system architecture.

Google provides a service-level agreement (SLA) that defines the expected uptime of the Cloud Healthcare API service and how clients can handle errors. For more information, see [Cloud Healthcare Service Level Agreement (SLA)](https://cloud.google.com/healthcare/sla).

## Implement retry logic and timeouts

To handle delays and errors caused by failed requests, implement appropriate retry logic and timeouts. When setting the timeout duration, allow sufficient time to do the following:

  * Let the Cloud Healthcare API process the request.
  * Determine if the error originated from the service or the client.



You can retry some errors, but others are non-retryable and persist across multiple retries. For example, if the request data is incorrectly formatted, the server responds with a `400 Bad Request` status code. The request won't succeed until you fix the data.

To handle these situations, you need to plan for final error states.

For more information on retry logic and timeouts, see [Retry failed requests](https://docs.cloud.google.com/healthcare-api/docs/best-practices-data-throughput#retry-failed).

## Handle errors at multiple layers

When middleware interacts with the Cloud Healthcare API, implement retry logic and timeouts in the client and middleware. If a client encounters errors past its retry limit, you must be able to identify if the error occurred in the client, the middleware, or the underlying Cloud Healthcare API service. This is especially important when planning for final error states.

Consider the following scenario:

  1. The middleware receives a `500 Internal Server Error` error from the Cloud Healthcare API when sending a request.
  2. The middleware layer retries the request five more times, reaching its limit, and then stops retrying.
  3. The client receives a final `500 Internal Server Error` error.



It's important to understand that the error originated in the Cloud Healthcare API, not the middleware. To simplify debugging, provide this information in the error returned to the client.

The following diagram shows a scenario where a middleware proxy receives `500 Internal Server Error` errors when forwarding a request from a client to the Cloud Healthcare API. The client and proxy both implement error handling and retries.

![Diagram of where to handle errors in the client/middleware/server stack.](https://docs.cloud.google.com/static/healthcare-api/images/errors-client-middleware-server.svg)**Figure 1.** The layers where you need to implement retry logic and timeouts are the **Client** and the **Proxy**.

Figure 1 shows the following steps:

  1. The client sends a valid request to the Cloud Healthcare API through a middleware proxy.
  2. The proxy forwards the request to the Cloud Healthcare API.
  3. The Cloud Healthcare API returns a `500 Internal Server Error` error to the proxy. The proxy retries the request five more times until its retry limit is reached. 
  4. The proxy returns the final error state, `500 Internal Server Error`, to the client. 

Using the recommendations shown earlier, you can debug the final error state by having the proxy return the following error to the client: 
         
         Error with underlying FHIR store in Cloud Healthcare API after 5 retries: 500 Internal Server Error

Add any more information about the error returned from the Cloud Healthcare API. 




Sometimes, the client or proxy receives `500 Internal Server Error` errors past their retry limits and can't retry again. In this case, a human might need to intervene to diagnose if the error came from the proxy or the Cloud Healthcare API.

## Choose which errors to retry

Depending on your system's architecture, you can retry certain errors and ignore others. The following is a non-exhaustive list of retryable Cloud Healthcare API error codes:

  * `408 Request Timeout`
  * `425 Too Early`
  * `429 Too Many Requests`
  * `500 Internal Server Error`
  * `502 Bad Gateway`
  * `503 Service Unavailable`
  * `504 Gateway Timeout`



These errors typically don't occur at the same frequency, and some might never occur.

### System architecture effects

Your system's architecture influences how and when you retry errors.

For example, in a direct client-to-server architecture, a client that receives a `401 UNAUTHENTICATED` error from the Cloud Healthcare API can re-authenticate and retry its request.

Suppose a system has a middleware layer between the client and the Cloud Healthcare API. If the client authenticated correctly and an expired [authentication token](https://docs.cloud.google.com/docs/authentication/tokens) caused the issue, then the middleware must [refresh the token](https://docs.cloud.google.com/docs/authentication/token-types#refresh-tokens) and retry the request.

After analyzing final error states, you can adjust the errors your client retries based on your findings.

## Plan for final error states

Even after implementing retry logic and timeouts, a client or middleware might receive errors until their retries are exhausted. The last error returned before retries and timeouts are exhausted is the _final error state_. You might encounter a final error state for data consistency errors.

Sometimes, a final error state requires human intervention. Try to implement a solution to resolve the final error state for a request. Otherwise, log the final error state so a human can review it.

Consider the following when planning how to handle final error states:

  * Whether there are processing dependencies that need to stop if a FHIR transaction or bundle can't complete successfully.
  * If many virtual machine (VM) instances start failing permanently, a client must report the requests that failed. After the problem is fixed, the client must retry the requests.
  * Monitoring, alerting systems, and [service-level objectives (SLOs)](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/create-slo) are necessary for ensuring the stability of your system. See [Test and monitor](https://docs.cloud.google.com/healthcare-api/docs/best-practices-data-throughput#test-and) for more information.



## Plan for increased latency

The Cloud Healthcare API is a scalable and performant service, but request latency can still vary for the following reasons:

  * Small differences between requests, even if they seem insignificant, can cause extra processing time.
  * Similar requests might have different latencies. For example, two similar requests that add a record to data storage might have different latencies if one crosses a threshold that triggers an extra task, like allocating more storage.
  * The Cloud Healthcare API handles many requests concurrently. The time when a client sends a request, measured in fractions of a second, might coincide with a time when the Cloud Healthcare API is under heavier load than usual.
  * If a Cloud Healthcare API physical resource, such as a disk, is handling many requests, it needs to complete its queued tasks before handling other requests.
  * Sometimes, the Cloud Healthcare API retries errors on the server-side, which can increase latency for clients.
  * There might be multiple copies of data in different data centers in a regional or multi-regional location. If your requests are routed across multiple data centers, either on the original request or on a retry, there might be increased latency.



### Plan using percentile latency

You can plan for increased latency by analyzing the _percentile latency_ of your requests. The following examples describe the _50th percentile latency_ and the _99th percentile latency_ :

  * The 50th percentile latency is the maximum latency, in seconds, for the fastest 50% of requests. For example, if the 50th percentile latency is 0.5 seconds, then the Cloud Healthcare API processed 50% of requests within 0.5 seconds. The 50th percentile latency is also called the "median latency".
  * The 99th percentile latency is the maximum latency, in seconds, for the fastest 99% of requests. For example, if the 99th percentile latency is two seconds, then the Cloud Healthcare API processed 99% of requests within two seconds.



If you analyze the percentile latency over an interval when the Cloud Healthcare API only processed a few requests, the percentile latency might not be useful or indicative of overall performance because outlier requests can have a large influence.

For example, suppose a process in the Cloud Healthcare API processes 100 requests in 100 minutes. The 99th percentile latency for the 100 minutes would be based on the single slowest request. A latency measurement using a single request isn't sufficient for understanding if there are performance issues.

Gathering a larger request sample over a longer time period, like 24 hours, can provide more insight into the overall behavior of your system. You can use these samples to determine how your system responds to heavy traffic.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
