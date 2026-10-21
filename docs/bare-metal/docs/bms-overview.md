---
url: https://docs.cloud.google.com/bare-metal/docs/bms-overview/
title: Bare Metal Solution overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:53:36.395383+00:00
---

# Bare Metal Solution overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bare-metal/docs/bms-overview/

The availability of Bare Metal Solution is transitioning to a specialized, allowlist-only model. If you are an existing customer, please contact your Google account team to explore the value of migrating to new [Oracle and Google Cloud strategic partnership offerings](https://docs.cloud.google.com/bare-metal/docs/explore-oracle-partnership-offerings). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Bare Metal ](https://docs.cloud.google.com/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/bare-metal/docs/bms-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Bare Metal Solution overview

Bare Metal Solution provides a secure environment in which you can run your specialized workloads on high-performance, bare-metal servers.

Use Bare Metal Solution to run:

  * Third-party virtualization software.
  * Applications that require direct, low-level access to the server.

**Note:** For bare metal compute instances, see [Bare metal instances on Compute Engine](https://docs.cloud.google.com/compute/docs/instances/bare-metal-instances).

## What Google Cloud provides in a Bare Metal Solution environment

Bare Metal Solution is a managed solution that provides purpose-built bare-metal servers in regional extensions that are connected to Google Cloud by a managed, high-performance connection with a low-latency network fabric.

![Bare-metal servers are shown in a regional extension that is colocated
with a Google Cloud data center](https://docs.cloud.google.com/static/bare-metal/docs/images/bms-architecture-2.svg)

With Bare Metal Solution, Google Cloud provides and manages the core infrastructure, the network, the physical and network security, and hardware monitoring capabilities in an environment from which you can access all of the Google Cloud services. The core infrastructure includes secure, controlled-environment facilities, and power.

The Bare Metal Solution also includes the provisioning and maintenance of custom, sole-tenancy servers with local SAN, and smart hands support.

The network, which is managed by Google Cloud, includes a low-latency Partner Interconnect connection into the customer Bare Metal Solution environment.

The available Google Cloud services include private API access, management tools, support, and billing.

![The elements in the preceding text are shown in the diagram](https://docs.cloud.google.com/static/bare-metal/docs/images/bms-elements-2.svg)

To review the service-level agreement, see the [Bare Metal Solution - Service Level Agreement (SLA)](https://cloud.google.com/bare-metal/sla).

## Your responsibilities in a Bare Metal Solution environment

You are responsible for the software, applications, and data that you use and store in the Bare Metal Solution environment. Your responsibilities include:

  * Data, including: 
    * Security and encryption
    * Backups
  * Software and applications, including: 
    * Installation
    * Configuration
    * Upgrades and patching
  * Operating system and any hypervisor, including: 
    * Configuration changes
    * Upgrades and patching
  * Server clusters, including: 
    * Installation
    * Configuration
    * Maintenance
  * Databases, including: 
    * Installation
    * Configuration
    * Migration
    * Administration
    * Upgrades and patching
  * Licensing
  * Security, including: 
    * Application security
    * OS patching and security updates
    * Network transport encryption, if needed between your Google Cloud environment and your Bare Metal Solution environment
  * Application and OS logging and monitoring
  * Configuring the interactive serial console on your Bare Metal Solution server
  * Application or workload maintenance
  * Backups, including backup security encryption
  * Support for your applications, as per your ISV agreements



You are responsible for the licensing of all of your software. Bare Metal Solution uses a bring-your-own-license (BYOL) model.

The OS and any hypervisor software are included in the software that you are responsible for. Google Cloud installs the initial OS or hypervisor for you. After your Bare Metal Solution server is delivered to you, you are responsible for the configuration and management of your OS, including applying updates and security patches and obtaining support.

[Our technical support](https://docs.cloud.google.com/bare-metal/docs/bms-support#bms-support-scope) primarily focuses on infrastructure-related issues. We don't provide support for issues related to OS, drivers, and compatibility. For the best assistance with these issues, we recommend contacting your OS vendor directly. They have the most in-depth knowledge to help you troubleshoot.

As a part of your responsibility for the security and compliance of your software and applications, you are responsible for applying the latest available security patches and software updates.

Finally, you need to design and implement your solutions for incident and operations management, change management, Identity and Access Management (IAM), backup and recovery, high-availability, and disaster recovery.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
