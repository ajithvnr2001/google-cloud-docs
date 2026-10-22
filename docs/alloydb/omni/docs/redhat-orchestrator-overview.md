---
url: https://docs.cloud.google.com/alloydb/omni/docs/redhat-orchestrator-overview/
title: The RPM orchestrator \u00a0|\u00a0 AlloyDB Omni \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:43:02.757434+00:00
---

# The RPM orchestrator  |  AlloyDB Omni  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/docs/redhat-orchestrator-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/omni/docs/overview)



Send feedback 

#  The RPM orchestrator Stay organized with collections  Save and categorize content based on your preferences. 

AlloyDB Omni provides an orchestration platform to deploy and manage AlloyDB Omni in non-Kubernetes environments, such as on Red Hat Enterprise Linux (RHEL) and compatible systems that use Red Hat Package Manager (RPM) packages. This deployment option is intended for organizations with significant investments in virtual machine (VM) infrastructure and established operational practices built around tools like Ansible.

The RPM orchestrator deployment option lets enterprises install, configure, and manage AlloyDB Omni instances using standard RPM packages. This approach runs directly on Linux VMs or bare-metal servers without requiring a containerization layer like Docker or an orchestration system like Kubernetes.

## Use cases

The RPM orchestrator deployment option supports the following use cases:

  * Enterprises with VM infrastructure: supports companies where Kubernetes is not standard, or environments with strict security postures, regulatory requirements, or application dependencies that prefer standard VM deployments.
  * Simplified operations: automates database deployment, configuration, and lifecycle management using familiar tools, for example, Ansible.
  * High availability (HA) and disaster recovery (DR): sets up resilient AlloyDB Omni clusters with automated failover and recovery mechanisms.
  * Hybrid environments: provides consistent database operations across on-premises data centers and cloud VMs.
  * Legacy system integration: integrates with existing applications and systems designed for non-containerized environments.



You can also pair your RPM orchestrator deployment with the optional [AlloyDB Omni web user interface](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/install-web-ui) (`alloydbomni_ui`), a self-managed web console that provides observability dashboards for cluster instances, system telemetry charts, database sizes, active database flags, columnar engine statistics, and query insights.

## Get started

  * To get started with this deployment option, [request access using the sign-up form](https://forms.gle/zxuHekMtV67Bw9Av9).
  * Learn more about the [RPM orchestrator deployment option](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/overview).
  * [Install AlloyDB Omni using the RPM orchestrator](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/install-orchestrator).
  * [Install the web UI using the RPM orchestrator](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/install-web-ui).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
