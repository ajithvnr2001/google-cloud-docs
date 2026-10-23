---
url: https://docs.cloud.google.com/architecture/infra-reliability-guide/
title: Google Cloud infrastructure reliability guide \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:53.405747+00:00
---

# Google Cloud infrastructure reliability guide  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/infra-reliability-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Google Cloud infrastructure reliability guide Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-09-23 UTC

Reliable infrastructure is a critical requirement for workloads in the cloud. As a cloud architect, to design reliable infrastructure for your workloads, you need a good understanding of the reliability capabilities of your cloud provider of choice. This document describes the building blocks of reliability in Google Cloud (zones, regions, and location-scoped resources) and the availability levels that they provide. This document also provides guidelines for assessing the reliability requirements of your workloads, and presents architectural recommendations for building and managing reliable infrastructure in Google Cloud.

This document is divided into the following parts:

  * Overview of reliability (this part)
  * [Building blocks of reliability in Google Cloud](https://docs.cloud.google.com/architecture/infra-reliability-guide/building-blocks)
  * [Assess the reliability requirements for your cloud workloads](https://docs.cloud.google.com/architecture/infra-reliability-guide/requirements)
  * [Design reliable infrastructure for your workloads in Google Cloud](https://docs.cloud.google.com/architecture/infra-reliability-guide/design)
  * [Manage traffic and load for your workloads in Google Cloud](https://docs.cloud.google.com/architecture/infra-reliability-guide/traffic-load)
  * [Manage and monitor your Google Cloud infrastructure](https://docs.cloud.google.com/architecture/infra-reliability-guide/manage-and-monitor)



If you've read this guide previously and want to see what's changed, see the [Release notes](https://docs.cloud.google.com/architecture/release-notes).

## Overview of reliability

An application or workload is reliable when it meets your current objectives for availability and resilience to failures.

Availability (or uptime) is the percentage of time that an application is usable. For example, for an application that has an availability target of 99.99%, the total downtime must not exceed 8.64 seconds during a 24-hour period. Sometimes, availability is measured as the proportion of requests that the application serves successfully during a given period. For example, for an application that has an availability target of 99.99%, for every 100,000 requests received, not more than ten requests can fail. Availability is often expressed as the number of nines in the percentage. For example, 99.99% availability is expressed as "4 nines".

Depending on the purpose of the application, you might have different sets of indicators for how reliable the application is. The following are examples of such reliability indicators:

  * For applications that serve content, availability, latency, and throughput are important reliability indicators. They indicate whether the application can respond to requests, how long the application takes to respond to requests, and how many requests the application can process successfully in a given period.
  * For databases and storage systems, latency, throughput, availability, and durability (how well data is protected against loss or corruption), are indicators of reliability. They indicate how long the system takes to read or write data, and whether data can be accessed on demand.
  * For big data and analytics workloads such as data processing pipelines, consistent pipeline performance (throughput and latency) is essential to ensure freshness of the data products, and is an important reliability indicator. It indicates how much data can be processed, and how long it takes for the pipeline to progress from data ingestion to data processing.
  * Most applications have data correctness as an essential reliability indicator.



For further guidelines to define the reliability objectives for your applications, see [Assess the reliability requirements for your cloud workloads](https://docs.cloud.google.com/architecture/infra-reliability-guide/requirements).

**Note:** Planning for disaster recovery (DR) is related to reliability, and DR is essential for business continuity. For detailed guidance about DR planning, see the [Disaster recovery planning guide](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide).

## Factors that affect application reliability

The reliability of an application that's deployed in Google Cloud depends on the following factors:

  * The internal design of the application.
  * The secondary applications or components that the application depends on.
  * Google Cloud infrastructure resources such as compute, networking, storage, databases, and security that the application runs on, and how the application uses the infrastructure.
  * Infrastructure capacity that you provision, and how the capacity scales.
  * The DevOps processes and tools that you use to build, deploy, and maintain the application, its dependencies, and the Google Cloud infrastructure.



These factors are summarized in the following diagram:

![Application reliability dependencies.](https://docs.cloud.google.com/static/architecture/images/infra-reliability-guide/dependencies.svg)

As shown in the preceding diagram, the reliability of an application that's deployed in Google Cloud depends on multiple factors. The focus of this guide is the reliability of the Google Cloud infrastructure.

## What's next

  * [Building blocks of reliability in Google Cloud](https://docs.cloud.google.com/architecture/infra-reliability-guide/building-blocks)
  * [Assess the reliability requirements for your cloud workloads](https://docs.cloud.google.com/architecture/infra-reliability-guide/requirements)
  * [Design reliable infrastructure for your workloads in Google Cloud](https://docs.cloud.google.com/architecture/infra-reliability-guide/design)
  * [Manage traffic and load for your workloads in Google Cloud](https://docs.cloud.google.com/architecture/infra-reliability-guide/traffic-load)
  * [Manage and monitor your Google Cloud infrastructure](https://docs.cloud.google.com/architecture/infra-reliability-guide/manage-and-monitor)



## Contributors

Authors: 

  * [Nir Tarcic](https://www.linkedin.com/in/nirtarcic) | Cloud Lifecycle SRE UTL
  * [Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer



Other contributors: 

  * [Alok Kumar](https://www.linkedin.com/in/alok-kumar-0a51159) | Distinguished Engineer
  * [Andrew Fikes](https://www.linkedin.com/in/andrew-fikes) | Engineering Fellow, Reliability
  * [Chris Heiser](https://www.linkedin.com/in/christopher-heiser) | SRE TL
  * [David Ferguson](https://www.linkedin.com/in/davidsferguson) | Director, Site Reliability Engineering
  * [Joe Tan](https://www.linkedin.com/in/joe-tan-378a55a8) | Senior Product Counsel
  * [Krzysztof Duleba](https://www.linkedin.com/in/kduleba) | Principal Engineer
  * [Narayan Desai](https://www.linkedin.com/in/nldesai) | Principal SRE
  * [Sailesh Krishnamurthy](https://www.linkedin.com/in/saileshkrishnamurthy) | VP, Engineering
  * [Steve McGhee](https://www.linkedin.com/in/stevemcghee) | Reliability Advocate
  * [Sudhanshu Jain](https://www.linkedin.com/in/sudhanshujain) | Product Manager
  * [Yaniv Aknin](https://www.linkedin.com/in/yanivaknin) | Software Engineer



[ Next Building blocks of reliability  arrow_forward  ](https://docs.cloud.google.com/architecture/infra-reliability-guide/building-blocks)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-23 UTC."],[],[]] 
