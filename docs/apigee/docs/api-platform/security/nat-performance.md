---
url: https://docs.cloud.google.com/apigee/docs/api-platform/security/nat-performance/
title: Performance considerations for Apigee Cloud NAT \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:22:17.399263+00:00
---

# Performance considerations for Apigee Cloud NAT  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/security/nat-performance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Performance considerations for Apigee Cloud NAT Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Southbound traffic between Apigee and a target backend with a public IP address uses [Cloud NAT](https://cloud.google.com/nat/docs/overview) to translate the private IP address of the Apigee instance into a public IP address. Each Apigee instance has its own Cloud NAT gateway. This topic explains the factors that impact Apigee performance when using Cloud NAT.

## Overview

Each new TCP session formed between an Apigee instance and a target backend must be mapped to a unique 4-tuple that includes the following: 

  * The NAT IP address 
  * The NAT port 
  * The backend IP address 
  * The backend port 



There are three key factors that determine the transactions per second (TPS) that Cloud NAT can support in an Apigee instance: 

  1. The number of NAT IPs allocated (dynamically or statically) 
  2. The number of unique backend IP address and port combinations configured 
  3. Whether or not connection reuse is allowed by the target backend



This topic explains how each of these factors impacts Apigee performance when using Cloud NAT and describes how to calculate the number of static IPs that may be required to support anticipated traffic. 

## NAT IP Allocations

The number of NAT IPs allocated will vary depending on the use of _ephemeral_ or _static_ IPs in the NAT configuration. See the **NAT IP addresses per gateway** in the [Cloud NAT Limits](https://docs.cloud.google.com/nat/quota#limits) for more information. 

### Ephemeral IPs

In the default NAT configuration using ephemeral IPs, the IPs are automatically allocated as needed to provide unique source ports for connections to target backends. 

### Static IPs

If static IPs are required so that the IPs can be allow-listed for the target backend, the IPs are manually reserved for an Apigee instance. 

## Unique Backend IP and Port Combinations

You can increase TPS by increasing the number of unique target backend IP and port combinations. The same NAT IP and source port can be used for each of the target backend IPs and ports. This achieves the same result as adding more NAT IPs without requiring additional IPs that must be allow-listed. 

To create a unique target backend IP and port pair, the IP _or****_ the port must be different. For example, it is possible to have a single load balancer with one IP address, but listening on 4 different ports, to make 4 unique backend IP and port combinations for Apigee. 

**Note** : If the backend is a Network Load Balancer (NLB) at another Cloud Provider, make sure it supports concurrent usage of the same NAT IP and source port against multiple IP addresses of that NLB. You might need to disable features like "cross-zone load balancing" or "client IP address preservation" to make it work. Otherwise, you might encounter variety of connectivity errors related to connection reuse. Please reach out to the relevant Cloud Provider for assistance.

## Connection Reuse

Reusing HTTP connections also increases the efficient use of NAT by removing the need to open a new TCP connection. Target backends can use this feature by setting the **`Connection` **header to**`keep-alive` **in the response, which is the default setting for HTTP/1.1. The target backend server can also set `connection timeout` and `max reuse` parameters to improve efficiency.

While connection reuse can theoretically be supported by enabling **`keep-alive`** in the response, in practice, connection reuse depends on the following: 

  * If the Apigee instance has an existing connection to the target backend 
  * If the existing connection has pending responses 
  * If the existing connection is near the end of its lifecycle



Each of these factors will affect the extent to which the target backend can reuse connections. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
