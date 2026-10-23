---
url: https://docs.cloud.google.com/network-connectivity/docs/router/concepts/best-practices/
title: Best practices for Cloud Router \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:28.772478+00:00
---

# Best practices for Cloud Router  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/router/concepts/best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Router ](https://docs.cloud.google.com/network-connectivity/docs/router)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Best practices for Cloud Router

When working with Cloud Router, use the following best practices.

  * If your on-premises Border Gateway Protocol (BGP) router supports [Bidirectional Forwarding Detection (BFD)](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd), enable it on your on-premises BGP device and on the Cloud Router to provide a high-availability network link that can respond faster to link failures. 
  * If your peer router supports it, consider enabling [MD5 authentication](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/use-md5-authentication) on your BGP sessions. By default, BGP sessions are unauthenticated. 
  * Enable graceful restart on your on-premises BGP device. With graceful restart, traffic between networks isn't disrupted in the event of a Cloud Router or on-premises BGP device failure as long as the BGP session is re-established within the graceful restart period. 
  * If graceful restart is not supported or enabled on your device, configure two on-premises BGP devices with one tunnel each to provide redundancy. If you don't configure two separate on-premises devices, Cloud VPN tunnel traffic can be disrupted in the event of a Cloud Router or an on-premises BGP device failure. 
  * To ensure that you don't exceed Cloud Router [quotas](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#quotas), use Cloud Monitoring to create [alerting policies](https://docs.cloud.google.com/monitoring/alerts). For example, you can use the metrics for learned routes to create alerting policies for the [unique Cloud Router dynamic route prefixes quotas](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#from-own-region-limit). 
  * If appropriate, you can manually configure [custom learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes) and apply them to a BGP session. Dynamic routes created from custom learned routes are programmed and withdrawn just like dynamic routes that are BGP received. 



## What's next

  * To become familiar with Cloud Router terminology, see [Key terms](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/key-terms).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
