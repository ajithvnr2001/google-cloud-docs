---
url: https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/support/faq/
title: Frequently asked questions \u00a0|\u00a0 Network Intelligence Center - Connectivity Tests \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:14:10.355862+00:00
---

# Frequently asked questions  |  Network Intelligence Center - Connectivity Tests  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/support/faq/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Connectivity Tests ](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests)



Send feedback 

#  Frequently asked questions Stay organized with collections  Save and categorize content based on your preferences. 

This document covers commonly asked questions about Connectivity Tests.

## Does Connectivity Tests send a trace packet through my VPC network?

Yes, it does (for supported configurations). The live data plane analysis feature tests connectivity by sending multiple trace packets from the source endpoint to the destination. For details, see the following pages:

  * [What is reachability?](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#what-is-reachability)

  * [How Connectivity Tests works](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#how-it-works)

  * [Supported configurations (live data plane analysis)](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#supported-dynamic-configs)




## Can I test a configuration where I enabled the forwarding functions of my VM instance?

No. The configuration analysis traces a packet based on the configuration of resources in your Google Cloud projects. For virtual machine (VM) instances that use a customized image, Connectivity Tests doesn't have access to the forwarding or routing configurations. However, Connectivity Tests is still helpful in such cases because you can trace connectivity issues to your Cloud NAT gateway VM, for example. Some examples of this type of configuration are a VM acting as a Cloud NAT gateway, or a VM acting as a third-party firewall, such as the Palo Alto Networks VM series. Similarly, live data plane analysis tests reachability only from the source to the forwarding VM.

## Why Connectivity Tests produces multiple traces for a given test?

The Connectivity Tests configuration analysis can show multiple traces in the following situations:

  * The destination is a load balancer. For more information, see [Number of traces in a test to a load balancer](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/test-load-balancers#number-of-traces).
  * ECMP routing is being used. In this case, Connectivity Tests configuration analysis shows a trace for each possible route.
  * The source endpoint has an ambiguous definition. For example, a project can have multiple entities with the same IP address, in different Virtual Private Cloud networks. In this case, Connectivity Tests configuration analysis shows a trace for each source entity.



Live data plane analysis doesn't provide a breakdown into multiple traces.

## What's next

  * [Learn about Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview)
  * [Troubleshoot Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/support/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
