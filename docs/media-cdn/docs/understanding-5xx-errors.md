---
url: https://docs.cloud.google.com/media-cdn/docs/understanding-5xx-errors/
title: Understanding 5xx Errors \u00a0|\u00a0 Media CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:46:56.731810+00:00
---

# Understanding 5xx Errors  |  Media CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/media-cdn/docs/understanding-5xx-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Media CDN ](https://docs.cloud.google.com/media-cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/media-cdn/docs/overview)



Send feedback 

#  Understanding 5xx Errors Stay organized with collections  Save and categorize content based on your preferences. 

This page describes HTTP `5xx` errors in Media CDN, why some of these errors are expected, and how to differentiate normal background noise from service disruptions.

## What are `5xx` Errors?

HTTP `5xx` status codes indicate that a server—either the Media CDN edge server itself or the backend origin server—failed to fulfill a valid request. Because Media CDN acts as a proxy between your end users and content storage, a `5xx` status code usually indicates a communication breakdown between the CDN edge and the upstream origin, or a structural configuration failure.

## Why a small number of `5xx` errors are expected

Media CDN operates on globally distributed infrastructure that uses Google's edge network. In massive-scale distributed systems, achieving a continuous 0% error rate is technically impractical due to transient internet routing behaviors. Instead, a low background rate of `5xx` status codes is normal and doesn't typically indicate a problem with the overall health of the service.

The following reasons explain why some `5xx` status codes are expected:

  * **Highly distributed system:** Media CDN consists of several caching layers (external nodes in ISP networks, edge caches in Google points of presence (POPs), and long-tail edge caches) across thousands of locations. Because of the large number of components and network paths, transient, isolated issues such as a momentary network blip or a single machine becoming temporarily overloaded can occur.
  * **Transient network conditions:** The internet is dynamic. Minor, short-lived network congestion or latency spikes between caching tiers can occasionally cause internal requests to time out, resulting in a `5xx` status code.
  * **Load balancing and failover:** Although Media CDN is designed to be highly resilient and automatically routes around unhealthy components, the detection and failover process is not instantaneous. A brief spike in `5xx` status codes might occur during these transitions.
  * **Internal timeouts:** In a multi-tiered caching architecture, Media CDN fetches content through several layers. Occasional timeouts between these internal layers can occur, especially under heavy load or during cache fills from distant origins, resulting in a `5xx` status code.



## Understanding normal error thresholds

The key factors are the ratio and duration of the status codes.

  * **Ratio:** A very low percentage of `5xx` status codes compared to the total request volume is generally acceptable. Media CDN targets a Monthly Uptime Percentage of >= 99.95% as detailed in the [Media CDN SLA](https://cloud.google.com/media-cdn/sla). This target indicates that although the service is designed for high availability, it isn't expected to be 100% error-free. An error rate of less than 0.05% is often within normal operational tolerances.
  * **Duration:** Occasional, short-lived spikes are less concerning than sustained error rates of `5xx` status codes.



## When to investigate and take action

We recommend that you investigate or contact support if you observe any of the following patterns:

  * **Sustained errors:** `5xx` status codes that persist over a significant period.
  * **High ratio:** Status code rates that affect user experience (for example, consistently greater than 0.1%).
  * **Specific patterns:** Status codes that are concentrated on particular content, user agents, or geographic regions.
  * **Correlation with deployments:** Status codes that start immediately after a configuration change.



## Monitoring

Use [Cloud Monitoring](https://docs.cloud.google.com/media-cdn/docs/monitor) to track Media CDN performance and status code rates. Analyzing trends and filtering by response code helps you distinguish normal background noise from potential issues that require investigation.

## Summary

Although Media CDN strives for maximum availability, the inherent complexity and scale of the platform mean that a small fraction of requests might result in a `5xx` status code. This behavior is a normal characteristic of large-scale distributed systems. Focus on the overall trends, ratios, and any persistent error conditions.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
