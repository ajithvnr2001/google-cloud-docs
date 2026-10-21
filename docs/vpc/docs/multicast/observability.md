---
url: https://docs.cloud.google.com/vpc/docs/multicast/observability/
title: Observability for Cloud Multicast \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:27:44.485441+00:00
---

# Observability for Cloud Multicast  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/multicast/observability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Cloud Multicast ](https://docs.cloud.google.com/vpc/docs/multicast)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/multicast/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Observability for Cloud Multicast

**GA with allowlist:** Access to Cloud Multicast is available to select Google Cloud customers. If you are interested, submit an [access request form](https://forms.gle/G6o6wXTBqijoEHs26). 

This page describes the observability features that you can use to monitor Cloud Multicast.

## Overview

For an overview of the observability features that are available for Cloud Multicast and in which project, see the following table.

Feature | Description | Applicable projects1  
---|---|---  
Group membership event logs  
in [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview) | You can view logs for multicast group membership events, such as Internet Group Management Protocol (IGMP) join requests. For more information, see [View multicast group membership event logs](https://docs.cloud.google.com/vpc/docs/multicast/view-membership-logs). | 

  * Multicast administrator projects
  * Multicast consumer projects

  
Multicast information  
in [VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/flow-logs) | You can view flow logs that contain additional base and metadata fields for multicast traffic. For more information, see [View flow logs for multicast](https://docs.cloud.google.com/vpc/docs/multicast/view-flow-logs). | 

  * Multicast administrator projects
  * Multicast consumer projects

  
Multicast metrics  
in [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview) | You can view and use metrics for multicast group control messages, the number of active multicast consumers in a group, and multicast domain packet counts and latency distributions. For more information, see [Monitor metrics for multicast](https://docs.cloud.google.com/vpc/docs/multicast/monitor-metrics). | 

  * Multicast administrator projects

  
Service health events  
in [Personalized Service Health](https://docs.cloud.google.com/service-health/docs/overview) | You can use Personalized Service Health to help you identify Cloud Multicast service health events relevant to your projects so you can manage and respond to them efficiently. See Monitor multicast domain availability with Personalized Service Health. | 

  * Multicast administrator projects

  
  
1For multicast domains that use the single VPC network topology, the multicast administrator project is also the multicast consumer project. For multicast domains that use the Network Connectivity Center (NCC) star topology, there can be separate multicast consumer networks in different projects. The multicast producer network is always in the multicast administrator project, regardless of the topology of the multicast domain.

## Monitor multicast domain availability with Personalized Service Health

Information about incidents related to the availability of multicast domain infrastructure is available to multicast administrators and published to Personalized Service Health.

Cloud Multicast incidents are reported through the Virtual Private Cloud (VPC) product name and ID as listed in [Supported Google Cloud products and locations](https://docs.cloud.google.com/service-health/docs/supported-products-locations).

To learn more about Personalized Service Health, including how to view incidents and configure alerts, see the [Personalized Service Health overview](https://docs.cloud.google.com/service-health/docs/overview).

## What's next

  * [View multicast group membership event logs](https://docs.cloud.google.com/vpc/docs/multicast/view-membership-logs)
  * [View flow logs for multicast](https://docs.cloud.google.com/vpc/docs/multicast/view-flow-logs)
  * [Monitor membership metrics for multicast](https://docs.cloud.google.com/vpc/docs/multicast/monitor-metrics)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
