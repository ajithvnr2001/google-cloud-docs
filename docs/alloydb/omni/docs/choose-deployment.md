---
url: https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment/
title: Choose your AlloyDB Omni deployment option \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:54:38.138397+00:00
---

# Choose your AlloyDB Omni deployment option  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/omni/docs/overview)



Send feedback 

#  Choose your AlloyDB Omni deployment option Stay organized with collections  Save and categorize content based on your preferences. 

To start using AlloyDB Omni, first choose the deployment option that best meets your infrastructure needs. The available options are containers, the container orchestrator, the RPM orchestrator, and RPM. To help you choose, this page explains recommended use cases for each available deployment option and provides links to more information.

In the Google Cloud console, you can also explore and compare these deployment options on the **AlloyDB Omni** landing page under the **Deployment options** tab, which provides tailored setup paths, codelabs, and demos:

[Go to AlloyDB Omni](https://console.cloud.google.com/alloydb/omni)

## AlloyDB Omni using containers

Choose the container deployment option if you need one or more of the following. For more information, see [AlloyDB Omni using containers overview](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/overview).

  * Single application database: when you need a high-performance database dedicated to a single application.
  * Development and testing: for setting up a database environment on a developer's laptop or in a testing environment.
  * Non-Kubernetes environments: when your infrastructure doesn't use Kubernetes or when you don't need the complexity of a container orchestrator.
  * Offline operations: for applications that must continue to function even when they are disconnected from the internet.
  * Low-latency requirements: when you need to place the database geographically close to your users to achieve the fastest possible response times.



To start using AlloyDB Omni using containers, see [Plan your installation](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/plan-installation) and [Install AlloyDB Omni using containers](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/deploy-vm).

## AlloyDB Omni using the container orchestrator

Choose the container orchestrator deployment option if you need one or more of the following capabilities. For more information, see [AlloyDB Omni using the container orchestrator overview](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/overview).

  * Automated provisioning and API-driven lifecycle management.
  * Configurable high availability to fine tune failover mechanisms.
  * Sidecar support for integrating enterprise backup or monitoring agents.
  * Variable read pools for scaling read-only operations.
  * Load balancing with server-side connection pooling (PgBouncer).
  * Platform support and marketplace availability for Google Distributed Cloud and OpenShift.
  * Cross-region disaster recovery to create standby databases in remote clusters, data centers, and regions.



To start using AlloyDB Omni using the container orchestrator, see [AlloyDB Omni availability reference architecture](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/database-availability-reference-architecture-overview) and [Install AlloyDB Omni using the container orchestrator](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/deploy-kubernetes).

## AlloyDB Omni using RPM

Choose the RPM deployment option if you have an environment where containerization isn't preferred or where deep integration with the host operating system is required. For more information, see [AlloyDB Omni using RPM overview](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/overview).

Common use cases include the following:

  * Modernizing legacy applications: upgrade existing PostgreSQL workloads running on Linux servers to AlloyDB Omni using RPM to gain performance and manageability improvements without replatforming to containers.
  * Edge computing: deploy high-performance databases in remote data centers where resource constraints or operational models favor direct operating system (OS) installation.
  * Development and testing: give developers a powerful, local database instance that mirrors the production AlloyDB for PostgreSQL environment, enabling consistent testing and rapid iteration.
  * Regulated environments: run workloads in strictly controlled environments where using container runtimes might be restricted by security policies.



For more information, see [Plan your installation](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/plan-installation-linux) and [Install AlloyDB Omni using RPM](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/deploy-vm). [Sign up to request access to this deployment option](https://forms.gle/zxuHekMtV67Bw9Av9).

## AlloyDB Omni using the RPM orchestrator

Choose the RPM orchestrator deployment option if your organization has significant investments in virtual machine (VM) infrastructure and established operational practices built around tools like Ansible. For more information, see the [RPM orchestrator deployment overview](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/overview).

Common use cases include the following:

  * Enterprises with VM infrastructure: supports companies where Kubernetes isn't standard, or environments with strict security postures, regulatory requirements, or application dependencies that prefer standard VM deployments.
  * Simplified operations: automates database deployment, configuration, and lifecycle management using familiar tools, for example, Ansible.
  * High availability and disaster recovery: sets up resilient AlloyDB Omni clusters with automated failover and recovery mechanisms.
  * Hybrid environments: provides consistent database operations across on-premises data centers and cloud VMs.
  * Legacy system integration: integrates with existing applications and systems designed for non-containerized environments.



To start using the RPM orchestrator deployment option, see [Install the AlloyDB Omni RPM orchestrator](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/install-orchestrator).

## AlloyDB Omni web user interface

You can pair the optional web UI with any of the AlloyDB Omni deployment options.

The web UI is packaged in two formats to match your deployment choice:

  * Docker container image (`ALLOYDB_OMNI_UI_IMAGE_TAG`): for containerized environments, including containers and the container orchestrator.
  * Linux RPM package (`alloydbomni_ui`): for non-containerized VM or bare-metal environments, including RPM and the RPM orchestrator.



## What's next

[Manage AlloyDB Omni subscriptions in the Google Cloud console](https://console.cloud.google.com/alloydb/omni/subscriptions).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
