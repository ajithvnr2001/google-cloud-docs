---
url: https://docs.cloud.google.com/iap/docs/tcp-forwarding-overview/
title: TCP forwarding overview \u00a0|\u00a0 Identity-Aware Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:27:20.674993+00:00
---

# TCP forwarding overview  |  Identity-Aware Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iap/docs/tcp-forwarding-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Identity-Aware Proxy ](https://docs.cloud.google.com/iap/docs)
  * [ Guides ](https://docs.cloud.google.com/iap/docs/quickstarts)



Send feedback 

#  TCP forwarding overview Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how Identity-Aware Proxy (IAP) handles TCP forwarding. To learn how to grant principals access to tunneled resources and how to create tunnels that route TCP traffic, see [Using IAP for TCP forwarding](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding).

## Introduction

IAP's TCP forwarding feature lets you control who can access administrative services like SSH and RDP on your backends from the public internet. The TCP forwarding feature prevents these services from being openly exposed to the internet. Instead, requests to your services must pass authentication and authorization checks before reaching their target resource.

Exposing administrative services directly to the internet when running workloads in the cloud introduces risk. Forwarding TCP traffic with IAP lets you reduce that risk by allowing only authorized users to access these sensitive services.

Because this feature is specifically aimed at administrative services, it doesn't support load-balanced targets.

**Note:** Administrative services, as defined here, are services that are typically used to administer a machine, such as RDP, SSH, and MySQL's admin interface.

Calling the IAP TCP forwarding service isn't supported on mobile devices.

## How IAP's TCP forwarding works

IAP's TCP forwarding feature lets users connect to arbitrary TCP ports on Compute Engine instances. For general TCP traffic, IAP creates a listening port on the local host that forwards all traffic to a specified instance. IAP then wraps all traffic from the client in HTTPS. Users can access the interface and port if they pass the authentication and authorization checks of the target resource's Identity and Access Management (IAM) policy.

![](https://docs.cloud.google.com/iap/images/iap-tcp-forwarding-diagram.png)

When you establish an SSH connection using [`gcloud compute ssh`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssh), the command wraps the SSH connection inside HTTPS and forwards it to the remote instance without requiring a listening port on the local host.

Enabling IAP on an administrative resource doesn't automatically block direct requests to the resource. IAP only blocks TCP requests that aren't from IAP TCP forwarding IPs to relevant services on the resource.

TCP forwarding with IAP doesn't require a public, routable IP address assigned to your resource. Instead, it uses internal IPs.

## What's next

  * Learn how to connect to [TCP ports on instances](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding) and grant principals access to tunneled resources.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
