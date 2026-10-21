---
url: https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns/
title: Build hybrid and multicloud architectures using Google Cloud \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:35:44.003463+00:00
---

# Build hybrid and multicloud architectures using Google Cloud  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Build hybrid and multicloud architectures using Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-10-24 UTC

This architecture guide provides practical guidance on planning and architecting your hybrid and multicloud environments using Google Cloud. This document is the first of three documents in the set. It examines the opportunities and considerations associated with these architectures from a business and technology point of view. It also analyzes and discusses many proven hybrid and multicloud architecture patterns.

The document set for hybrid and multicloud architecture patterns consists of these parts:

  * Build hybrid and multicloud architectures: discusses planning a strategy for architecting a hybrid and multicloud setup with Google Cloud (this article).
  * [Hybrid and multicloud architecture patterns](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices): discusses common architecture patterns to adopt as part of a hybrid and multicloud strategy.
  * [Hybrid and multicloud secure networking architecture patterns](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns): discusses hybrid and multicloud networking architecture patterns from a networking perspective.



You can read each of these architecture articles independently, but for the most benefit, we recommend reading them in sequence before making an architectural decision.

The rapid pace of change in market demands has increased the requirements and expectations that are placed on enterprise IT, such as dynamic scale, increased performance for optimized user experience, and security. Many enterprise-level companies find it challenging to meet these demands and expectations using only traditional infrastructure and processes. IT departments are also under pressure to improve their cost effectiveness, making it difficult to justify additional capital investments in data centers and equipment.

A hybrid cloud strategy that uses public cloud computing capabilities provides a pragmatic solution. By using the public cloud, you can extend the capacity and capabilities of your computing platforms without up-front capital investment costs.

By adding one or more public cloud based solutions, like Google Cloud, to your existing infrastructure, you not only preserve your existing investments, but you also avoid committing yourself to a single cloud vendor. Also, by using a hybrid strategy, you can modernize applications and processes incrementally as resources permit.

To help you plan for your architectural decision and hybrid or multicloud strategy planning, there are several potential challenges and design considerations that you should consider. This multi-part architecture guide highlights both the potential benefits of various architectures and the potential challenges.

**Note:** This guide doesn't discuss multicloud architectures that use SaaS products, like customer relationship management (CRM) systems or email, alongside a cloud service provider (CSP).

## Overview of hybrid cloud and multicloud

Because workloads, infrastructure, and processes are unique to each enterprise, each hybrid cloud strategy must be adapted to your specific needs. The result is that the terms _hybrid cloud_ and _multicloud_ are sometimes used inconsistently.

Within the context of this Google Cloud architecture guide, the term _hybrid cloud_ describes an architecture in which workloads are deployed across multiple computing environments, one based in the public cloud, and at least one being private—for example, an on-premises data center or a colocation facility.

The term _multicloud_ describes an architecture that combines at least two public CSPs. As illustrated in the following diagram, sometimes this architecture includes a private computing environment (that might include the use of a private cloud component). That arrangement is called a hybrid and multicloud architecture.

![Diagram of the three architectures discussed in this series: hybrid, multicloud, and mix of hybrid and multicloud architectures.](https://docs.cloud.google.com/static/architecture/images/hybrid-multicloud-patterns/architectures.svg)

**Note:** The term _hybrid and multicloud_ refers to any combination of the three architectures displayed in the preceding diagram. However, where possible this series attempts to be specific when discussing architecture patterns.

## Contributors

Author: [Marwan Al Shawi](https://www.linkedin.com/in/marwanalshawi) | Partner Customer Engineer

Other contributors: 

  * [Saud Albazei](https://www.linkedin.com/in/albazei) | Customer Engineer, Application Modernization
  * [Anna Berenberg](https://www.linkedin.com/in/annaberenberg) | Engineering Fellow
  * [Marco Ferrari](https://www.linkedin.com/in/ferrarimark) | Cloud Solutions Architect
  * [Victor Moreno](https://www.linkedin.com/in/vimoreno) | Product Manager, Cloud Networking
  * [Johannes Passing](https://www.linkedin.com/in/johannespassing) | Cloud Solutions Architect
  * [Mark Schlagenhauf](https://www.linkedin.com/in/mark-schlagenhauf-63b98) | Technical Writer, Networking
  * [Daniel Strebel](https://www.linkedin.com/in/danistrebel) | EMEA Solution Lead, Application Modernization
  * [Ammett Williams](https://www.linkedin.com/in/ammett) | Developer Relations Engineer



[ Next Drivers, considerations, strategy, and patterns  arrow_forward  ](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns/drivers)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-10-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-10-24 UTC."],[],[]] 
