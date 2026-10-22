---
url: https://docs.cloud.google.com/compute/doubleclick/
title: Compute Engine for Google Ad Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:22:34.475691+00:00
---

# Compute Engine for Google Ad Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/doubleclick/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Resources ](https://docs.cloud.google.com/compute/docs/resources)



Send feedback 

#  Compute Engine for Google Ad Manager Stay organized with collections  Save and categorize content based on your preferences. 

Compute Engine lets you use virtual machine (VMs) instances hosted on Google's infrastructure for your real-time bidding logic. The service provides a great experience for hosting bidding logic for [Google Ad Manager](https://www.google.com/doubleclick/networks/scaled-media-buying.html), but you can use it to host bidders for other exchanges too.

This feature allows users who are currently hosting bidder logic on physical infrastructure to be able to host the same logic in the Google Cloud, on virtual machines provided by Google. Compute Engine offers many advantages for hosting your bidder logic:

  * In general, Google Ad Manager customers using Compute Engine should experience significantly lower latency during bid computation. Depending on where you are bidding, you should create your virtual machine instances in the corresponding regions:

Desired bidding location | Compute Engine region to host your instances  
---|---  
North America (West Coast)  | `us-west1`  
North America (Central)  | `us-central1`  
North America (East Coast)  | `us-east4, us-east1`  
Europe  | `europe-west1`  
Asia Pacific | `asia-east1`  
Tokyo, Japan | `asia-northeast1`  
  * Using Compute Engine allows you to place your bidding logic close to other Google Cloud services that can be used to augment your bidding logic.

  * Benefit from all of the standard Compute Engine features, including:

    * Start fast-booting, customizable [virtual machine instances](https://docs.cloud.google.com/compute/docs/instances) that are consistently high performance.
    * Choose from a variety of Linux and Windows OS [images](https://docs.cloud.google.com/compute/docs/images).
    * Pick the [block storage](https://docs.cloud.google.com/compute/docs/disks) option that best fits the price, performance, and durability requirements of your workload or application.
    * Expose your virtual machine instances to the Internet safely through an easily configurable [firewall](https://docs.cloud.google.com/compute/docs/networking#firewalls).
    * Manage your instances and infrastructure through a simple [REST API](https://docs.cloud.google.com/compute/docs/reference/latest), robust [command-line tool](https://docs.cloud.google.com/compute/docs/gcloud-compute), or a simple yet powerful web-based [Google Cloud console](https://console.cloud.google.com/).



## Sign up

To sign up for Compute Engine for Google Ad Manager, you must have:

  * Enabled [Compute Engine](https://docs.cloud.google.com/compute/docs/quickstart).
  * Signed up for a [Google Ad Manager account](https://support.google.com/google-ads/answer/7459399), if you want to use Google Ad Manager.



Users of Google Ad Manager and Compute Engine should experience lower latency when you bid to a Google Ad Manager bidding location (described above). There are no additional steps to enable Compute Engine for Google Ad Manager.

## Pricing

Standard [Compute Engine rates](https://cloud.google.com/compute/all-pricing) apply.

## Getting started

After you have Compute Engine and Google Ad Manager accounts, you can start using the service by:

  * Following one of the [Compute Engine getting started guides](https://docs.cloud.google.com/compute/docs/quickstart).
  * Reading about features such as [persistent disks](https://docs.cloud.google.com/compute/docs/disks), [images](https://docs.cloud.google.com/compute/docs/images), and [load balancing](https://docs.cloud.google.com/compute/docs/load-balancing).
  * Reviewing the [API reference](https://docs.cloud.google.com/compute/docs/reference/latest).
  * Familiarizing yourself with typical [real time bidding architecture](https://docs.cloud.google.com/solutions/architecture/realtimebidding).
  * Exploring our sample [real time bidder solution for Google Cloud](https://docs.cloud.google.com/solutions/real-time-bidder-solution-for-google-cloud-platform).



Google also offers an open-source real-time bidding infrastructure software that you can use to create your own bidding logic. For more information, see [Open Bidder](https://developers.google.com/authorized-buyers/rtb/open-bidding).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
