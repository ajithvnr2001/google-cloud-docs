---
url: https://docs.cloud.google.com/iap/docs/concepts-best-practices/
title: Best practices \u00a0|\u00a0 Identity-Aware Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T07:11:50.829264+00:00
---

# Best practices  |  Identity-Aware Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iap/docs/concepts-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Identity-Aware Proxy ](https://docs.cloud.google.com/iap/docs)
  * [ Guides ](https://docs.cloud.google.com/iap/docs/quickstarts)



Send feedback 

#  Best practices Stay organized with collections  Save and categorize content based on your preferences. 

This page describes best practices for using Identity-Aware Proxy (IAP).

## Caching

  * Don't use a third-party CDN in front of your application. CDNs may cache content and serve cached pages to unauthenticated users. 
    * If you have large, non-sensitive resources that you want to serve from a CDN, use a separate domain such as `images.yourapp.com` for these resources. Use the CDN with that domain and add the `Cache-control: private` HTTP response header to all objects that should only be served to authenticated users.



## Securing your app

To properly secure your app, you must use [signed headers](https://docs.cloud.google.com/iap/docs/signed-headers-howto) for [App Engine standard environment](https://docs.cloud.google.com/appengine/docs/standard), Compute Engine, and GKE applications. 

## Configuring your firewall

  * Make sure all requests to Compute Engine or GKE are routed through the load balancer: 
    * [Configure a firewall rule to allow health checking](https://docs.cloud.google.com/load-balancing/docs/health-checks) and make sure that all traffic to your Virtual Machine (VM) is from a Google Front End (GFE) IP. 
    * For additional protection, check the source IP of requests in your app to make sure they're from the same IP range that the firewall rule allows. 
  * In the Google Cloud console, IAP displays an error or warning if your firewall rules appear to be set up incorrectly. The IAP Google Cloud console doesn't detect which VM is used for each service, so the firewall analysis doesn't include advanced features like non-default networks and firewall rule tags. To bypass this analysis, enable IAP through the `gcloud compute backend-services update` command. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
