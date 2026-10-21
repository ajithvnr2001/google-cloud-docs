---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/architecture/hybrid-environment/
title: Reference architecture: Hybrid environment for Google Kubernetes Engine clusters \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:36:49.416311+00:00
---

# Reference architecture: Hybrid environment for Google Kubernetes Engine clusters  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/architecture/hybrid-environment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)



Send feedback 

#  Reference architecture: Hybrid environment for Google Kubernetes Engine clusters Stay organized with collections  Save and categorize content based on your preferences. 

_This content was last updated in December 2024 and includes support for Google Distributed Cloud version 1.31._

This page is for Cloud architects who want to design and build a a hybrid environment for Google Kubernetes Engine clusters. The complete reference architecture is provided as PDFs at the bottom of this page and shows you how to appropriately plan, deploy, and configure the required components for a GKE hybrid environment. This reference architecture shows you how to integrate Google Cloud-based services with on-premises deployments of Google Distributed Cloud software only on VMware or bare metal.

The following architecture diagram provides an overview of a complete GKE deployment in a hybrid environment that's explained in detail in the reference architecture:

![A GKE hybrid deployment architecture diagram with multiple services that run in Google Cloud connecting to on-premises clusters and applications](https://docs.cloud.google.com/static/kubernetes-engine/enterprise/docs/images/hybrid-environment-architecture-overview.svg)

In the previous diagram, Google Cloud-based services help you manage logging and monitoring data, store container images, and provide configuration management. On-premises components that run in your own data center like physical or virtual servers and clusters, identity solutions, and load balancers complete the hybrid approach.

The diagram also shows some different user personas who interact with the services, such as application developers, application operators, platform developers and operators, and network operators. Each of the personas has access to the resources that they need:

To get maximum value from this reference architecture, you should already be familiar with basic GKE concepts. If you're new to, GKE, then get started with [Start learning about GKE](https://docs.cloud.google.com/kubernetes-engine/docs/learn).

You should also be familiar with basic Kubernetes concepts. For more information, see [Kubernetes basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/), and the [Google Kubernetes Engine (GKE) documentation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview).

This reference architecture focuses on the following aspects of an GKE hybrid environment that uses Google Distributed Cloud on VMware or bare metal:

  * Architecture and components
  * Example reference deployments
  * Design prerequisites, including Google Cloud regions and sites, on-premises setup, and networking.
  * Design considerations for availability, security and compliance, scale and limits, observability, Git-ops based configuration management, and more.
  * Implementation details like logging and monitoring, permissions, and others.



## Get the reference architecture

The reference architecture is published in two parts - the first part explains the architecture, reference deployments, and design prerequisites and considerations, and the second part provides the implementation details. To read the reference architecture, select one of the following PDF links:

  * [Part 1 - Architecture, reference deployments, design prerequisites and considerations (PDF)](https://docs.cloud.google.com/static/kubernetes-engine/enterprise/docs/architecture/hybrid-environment-reference-architecture-part-1.pdf)
  * [Part 2 - Implementation details (PDF)](https://docs.cloud.google.com/static/kubernetes-engine/enterprise/docs/architecture/hybrid-environment-reference-architecture-part-2.pdf)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
