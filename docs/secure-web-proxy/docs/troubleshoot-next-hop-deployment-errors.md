---
url: https://docs.cloud.google.com/secure-web-proxy/docs/troubleshoot-next-hop-deployment-errors/
title: Troubleshoot next hop deployment errors \u00a0|\u00a0 Secure Web Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:37:10.947943+00:00
---

# Troubleshoot next hop deployment errors  |  Secure Web Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-web-proxy/docs/troubleshoot-next-hop-deployment-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Secure Web Proxy ](https://docs.cloud.google.com/secure-web-proxy/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart)



Send feedback 

#  Troubleshoot next hop deployment errors Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to diagnose and resolve common issues that might occur when you deploy Secure Web Proxy as next hop.

## Default route isn't defined

When you configure the routing for your Secure Web Proxy instance by using either [static routes](https://docs.cloud.google.com/secure-web-proxy/docs/deploy-next-hop#static-routes) or [policy-based routes](https://docs.cloud.google.com/secure-web-proxy/docs/deploy-next-hop#policy-based-routes), you must set up a default route (`0.0.0.0/0`).

If you don't set up a default route, the proxy can't forward traffic to external destinations and the following errors might occur:

  * Connection timeouts - `504 Gateway Timeout`
  * No route to host - `502 Bad Gateway`



## Default static route doesn't have a network tag

When using a default [static route](https://docs.cloud.google.com/secure-web-proxy/docs/deploy-next-hop#static-routes) for your Secure Web Proxy instance, you must assign a [network tag](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags) to that route. Otherwise, you might encounter validation errors.

You must also attach the tag to your client virtual machine (VM) instances to help ensure the traffic is routed to the proxy.

## Non-HTTP and non-HTTPS traffic is blocked

Secure Web Proxy is optimized for web-based traffic; Transmission Control Protocol (TCP) traffic is blocked if it's routed to Secure Web Proxy and there are no TCP proxy rules configured to handle it. This mismatch typically results in `Connection Refused` or `400 Bad Request` errors for protocols like Secure Shell (SSH) and File Transfer Protocol (FTP).

To resolve such types of errors, either create specific [TCP proxy rules](https://docs.cloud.google.com/secure-web-proxy/docs/policies-and-rules-overview#tcp-proxy-rules) to manage the traffic or update your [policy-based routes](https://docs.cloud.google.com/secure-web-proxy/docs/deploy-next-hop#policy-based-routes) to only forward ports such as `80` or `443`. By following any one of these processes, you can help ensure that the TCP traffic bypasses your Secure Web Proxy instance and follows standard Virtual Private Cloud (VPC) routing.

## Secure Web Proxy as next hop gateway fails to deploy

To fix this issue, do the following:

  1. Verify whether an existing Secure Web Proxy instance is deployed as a next hop in the same region. For a Virtual Private Cloud network in a region, you can deploy only one Secure Web Proxy instance as a next hop.

  2. Check your organization's audit logs for policies that might be preventing the creation of Cloud NAT gateways.

  3. Verify that no orphaned auto-generated resources—such as `swg-autogen-router` or `swp-autogen-nat`—exist in the network; if they do, delete the auto-generated router and then redeploy your Secure Web Proxy.




## What's next

  * [Troubleshoot TLS inspection errors](https://docs.cloud.google.com/secure-web-proxy/docs/troubleshoot-tls-inspection-errors)
  * [Secure Web Proxy release notes](https://docs.cloud.google.com/secure-web-proxy/docs/release-notes)
  * [Secure Web Proxy support](https://docs.cloud.google.com/secure-web-proxy/docs/getting-support)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
