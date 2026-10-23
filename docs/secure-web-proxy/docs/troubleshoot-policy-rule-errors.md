---
url: https://docs.cloud.google.com/secure-web-proxy/docs/troubleshoot-policy-rule-errors/
title: Troubleshoot policy and rule errors \u00a0|\u00a0 Secure Web Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:37:37.526149+00:00
---

# Troubleshoot policy and rule errors  |  Secure Web Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-web-proxy/docs/troubleshoot-policy-rule-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Secure Web Proxy ](https://docs.cloud.google.com/secure-web-proxy/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart)



Send feedback 

#  Troubleshoot policy and rule errors Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to diagnose and resolve common errors related to Secure Web Proxy policies and rules.

## Secure Web Proxy gateway doesn't have an associated policy

If your Secure Web Proxy gateway isn't associated with a policy, then all outbound HTTP and HTTPS traffic is blocked, leading to `403 Forbidden` errors or connection resets. This occurs because Secure Web Proxy follows a `deny-all` posture by default and the gateway doesn't have any associated rules to evaluate or authorize requests. As a result, all outbound traffic is blocked until you create an explicit `allow` rule.

To resolve this issue, [create a security policy](https://docs.cloud.google.com/secure-web-proxy/docs/create-a-policy) with the [appropriate rules](https://docs.cloud.google.com/secure-web-proxy/docs/configure-rules) and associate them with your Secure Web Proxy gateway.

## Parallel rule creation failures

Creating Secure Web Proxy rules in parallel (adding multiple rules simultaneously) isn't supported and can result in `409 Conflict` or `Resource busy` errors. To make sure that your Secure Web Proxy instance is successfully deployed, you must create the rules sequentially (one after another).

## Connections terminate after five minutes of inactivity

If client applications experience connection resets or unexpected terminations on persistent connections (such as streaming sessions, database connections, or WebSockets) through Secure Web Proxy, then these connections might be exceeding the stream idle timeout.

Secure Web Proxy enforces a default, non-configurable stream idle timeout (`stream_idle_timeout`) of five minutes (300 seconds). If the client and destination don't exchange data for five minutes, Secure Web Proxy resets or closes the connection.

To prevent connections from closing due to stream inactivity, configure your client or backend application to send keepalive probes or heartbeats (such as TCP keepalives, HTTP ping frames, or periodic health requests) at intervals under five minutes. For example, you can send a probe every one to two minutes.

## What's next

  * [Troubleshoot next-hop deployment errors](https://docs.cloud.google.com/secure-web-proxy/docs/troubleshoot-next-hop-deployment-errors)
  * [Troubleshoot TLS inspection errors](https://docs.cloud.google.com/secure-web-proxy/docs/troubleshoot-tls-inspection-errors)
  * [Secure Web Proxy release notes](https://docs.cloud.google.com/secure-web-proxy/docs/release-notes)
  * [Secure Web Proxy support](https://docs.cloud.google.com/secure-web-proxy/docs/getting-support)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
