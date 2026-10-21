---
url: https://docs.cloud.google.com/media-cdn/docs/troubleshooting-origins/
title: Troubleshoot origins \u00a0|\u00a0 Media CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:18:22.225809+00:00
---

# Troubleshoot origins  |  Media CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/media-cdn/docs/troubleshooting-origins/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Media CDN ](https://docs.cloud.google.com/media-cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/media-cdn/docs/overview)



Send feedback 

#  Troubleshoot origins Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve issues with [origins](https://docs.cloud.google.com/media-cdn/docs/origins) when you configure them to work with Media CDN.

## Troubleshoot origin connectivity

If you are receiving HTTP 50x errors, such as HTTP 502 (Gateway Timeout) or HTTP 500 (Internal Server Error), consider the following:

  * Test that the origin hostname can be resolved with [Google Public DNS](https://dns.google/), and that the resolved IP addresses match expectations. If you recently changed your DNS records, resolvers might still have the old address in their caches.

  * If your origin _only_ supports HTTP/1.1 and does not support HTTP/2, configure the `protocol` field on the origin to use `HTTP` or `HTTPS` instead of `HTTP2`. Media CDN does not fall back to HTTP/1.1 connections unless specified.

  * Check that [request logs in Cloud Logging](https://docs.cloud.google.com/media-cdn/docs/logging) contain the correct origin IP address.

  * Check that the origin has a valid (publicly trusted) and unexpired SSL (TLS) certificate.

  * HTTP/2 Trailers are not supported, and requests to an origin server don't include the "TE" request header. Trailers included in a response are not cached or returned to the client.




## Troubleshooting origin failover

If an origin failover isn't behaving as expected, consider the following:

  * Ensure that the appropriate host header rewrite is configured on your failover origin.

  * Ensure that your primary origin is configured with sufficient `maxAttemptsTimeout`, `maxAttempts`, and `timeouts` to accommodate origin redirects and failovers. Origin redirects count as separate connection attempts against the `maxAttempts` setting.




## What's next

  * Read about [origin connectivity and shielding](https://docs.cloud.google.com/media-cdn/docs/origins)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
