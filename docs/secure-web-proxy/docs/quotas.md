---
url: https://docs.cloud.google.com/secure-web-proxy/docs/quotas/
title: Quotas and limits \u00a0|\u00a0 Secure Web Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:09:10.670074+00:00
---

# Quotas and limits  |  Secure Web Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-web-proxy/docs/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Secure Web Proxy ](https://docs.cloud.google.com/secure-web-proxy/docs)
  * [ Resources ](https://docs.cloud.google.com/secure-web-proxy/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the quotas and system limits that apply to Secure Web Proxy.

  * _Quotas_ have default values, but you can typically request adjustments.
  * _System limits_ are fixed values that can't be changed.



Google Cloud uses quotas to help ensure fairness and reduce spikes in resource use and availability. A quota restricts how much of a Google Cloud resource your Google Cloud project can use. Quotas apply to a range of resource types, including hardware, software, and network components. For example, quotas can restrict the number of API calls to a service, the number of load balancers used concurrently by your project, or the number of projects that you can create. Quotas protect the community of Google Cloud users by preventing the overloading of services. Quotas also help you to manage your own Google Cloud resources.

The Cloud Quotas system does the following:

  * Monitors your consumption of Google Cloud products and services
  * Restricts your consumption of those resources
  * Provides a way to [request changes to the quota value](https://docs.cloud.google.com/docs/quotas/help/request_increase) and [automate quota adjustments](https://docs.cloud.google.com/docs/quotas/quota-adjuster)



In most cases, when you attempt to consume more of a resource than its quota allows, the system blocks access to the resource, and the task that you're trying to perform fails.

Quotas generally apply at the Google Cloud project level. Your use of a resource in one project doesn't affect your available quota in another project. Within a Google Cloud project, quotas are shared across all applications and IP addresses. 

For more information, see the [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview). 

There are also _system limits_ on Secure Web Proxy resources. System limits can't be changed. 

## Allocation quotas

The following quotas don't reset over time and instead are released when you release the resource.

Usage limit | Value  
---|---  
Secure Web Proxy instances defined per project per region | 5  
URL lists defined per project per region | 10  
Policies defined per project per region | 10  
  
To display quotas for Secure Web Proxy instances for your project, in the Google Cloud console, go to the **Network Services API quotas** page.

[Go to Network Services API quotas](https://console.cloud.google.com/apis/api/networkservices.googleapis.com/quotas)

To display quotas for policies for your project, in the Google Cloud console, go to the **Network Security API quotas** page.

[Go to Network Security API quotas](https://console.cloud.google.com/apis/api/networksecurity.googleapis.com/quotas)

## Usage limits

Secure Web Proxy enforces the following usage limits:

Usage limit | Value  
---|---  
Rules per policy | 500  
CEL regular expression matchers per policy | 5  
Maximum sub-expressions per rule | 5,000  
Maximum entries per URL list | 2,500  
Regular expression length | 100 characters  
Maximum matcher length | 2,048 characters  
  
## System limits

The following system limits apply to Secure Web Proxy.

### Timeouts

Secure Web Proxy enforces the following default timeouts:

Timeout type | Default value | Configurable | Description  
---|---|---|---  
Stream idle timeout (`stream_idle_timeout`) | 5 minutes (300 seconds) | No | Maximum duration that an established TCP connection or stream can remain idle without data flowing between the client and the destination. If neither the client nor the upstream destination transmits data within five minutes, then Secure Web Proxy closes the stream or TCP connection.  
  
## Request a quota increase

To adjust most quotas, use the Google Cloud console. For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
