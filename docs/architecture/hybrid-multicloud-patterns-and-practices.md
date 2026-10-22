---
url: https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/
title: Hybrid and multicloud architecture patterns \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:04.664140+00:00
---

# Hybrid and multicloud architecture patterns  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Hybrid and multicloud architecture patterns Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-10-24 UTC

This document is the second of three documents in a set. It discusses common hybrid and multicloud architecture patterns. It also describes the scenarios that these patterns are best suited for. Finally, it provides the best practices you can use when deploying such architectures in Google Cloud.

The document set for hybrid and multicloud architecture patterns consists of these parts:

  * [Build hybrid and multicloud architectures](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns): discusses planning a strategy for architecting a hybrid and multicloud setup with Google Cloud.
  * Hybrid and multicloud architecture patterns: discusses common architecture patterns to adopt as part of a hybrid and multicloud strategy (this document).
  * [Hybrid and multicloud secure networking architecture patterns](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns): discusses hybrid and multicloud networking architecture patterns from a networking perspective.



Every enterprise has a unique portfolio of application workloads that place requirements and constraints on the architecture of a hybrid or multicloud setup. Although you must design and tailor your architecture to meet these constraints and requirements, you can rely on some common patterns to define the foundational architecture.

An architecture pattern is a repeatable way to structure multiple functional components of a technology solution, application, or service to create a reusable solution that addresses certain requirements or use cases. A cloud-based technology solution is often made of several distinct and distributed cloud services. These services collaborate to deliver required functionality. In this context, each service is considered a functional component of the technology solution. Similarly, an application can consist of multiple functional tiers, modules, or services, and each can represent a functional component of the application architecture. Such an architecture can be standardized to address specific business use cases and serve as a foundational, reusable pattern.

To generally define an architecture pattern for an application or solution, identify and define the following:

  * The components of the solution or application.
  * The expected functions for each component—for example, frontend functions to provide a graphical user interface or backend functions to provide data access.
  * How the components communicate with each other and with external systems or users. In modern applications, these components interact through well-defined interfaces or APIs. There are a wide range of communication models such as asynchronous and synchronous, request-response, or queue-based.



The following are the two main categories of hybrid and multicloud architecture patterns:

  * [Distributed architecture patterns](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/distributed-patterns): These patterns rely on a distributed deployment of workloads or application components. That means they run an application (or specific components of that application) in the computing environment that suits the pattern best. Doing so lets the pattern capitalize on the different properties and characteristics of distributed and interconnected computing environments.
  * Redundant architecture patterns: These patterns are based on redundant deployments of workloads. In these patterns, you deploy the same applications and their components in multiple computing environments. The goal is to either increase the performance capacity or resiliency of an application, or to replicate an existing environment for development and testing.



When you implement the architecture pattern that you select, you must use a suitable [deployment archetype](https://docs.cloud.google.com/architecture/deployment-archetypes). Deployment archetypes are zonal, regional, multi-regional, or global. This selection forms the basis for constructing application-specific deployment architectures. Each deployment archetype defines a combination of failure domains within which an application can operate. These failure domains can encompass one or more [Google Cloud zones or regions](https://docs.cloud.google.com/architecture/infra-reliability-guide/building-blocks#regions_and_zones), and can be expanded to include your on-premises data centers or failure domains in other cloud providers.

This series contains the following pages:

  * [Distributed architecture patterns](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/distributed-patterns)

    * [Tiered hybrid pattern](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/tiered-hybrid-pattern)
    * [Partitioned multicloud pattern](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/partitioned-multicloud-pattern)

    * [Analytics hybrid and multicloud pattern](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/analytics-hybrid-multicloud-pattern)

    * [Edge hybrid pattern](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/edge-hybrid-pattern)

  * Redundant architecture patterns

    * [Environment hybrid pattern](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/environment-hybrid-pattern)
    * [Business continuity hybrid and multicloud patterns](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/business-continuity-patterns)
    * [Cloud bursting pattern](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/cloud-bursting-pattern)



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



[ Next Distributed architecture patterns  arrow_forward  ](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/distributed-patterns)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-10-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-10-24 UTC."],[],[]] 
