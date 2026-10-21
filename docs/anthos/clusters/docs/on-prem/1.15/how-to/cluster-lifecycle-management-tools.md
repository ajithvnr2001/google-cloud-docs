---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/cluster-lifecycle-management-tools/
title: Choose a tool to manage cluster lifecycle \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:11:50.736231+00:00
---

# Choose a tool to manage cluster lifecycle  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/cluster-lifecycle-management-tools/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Choose a tool to manage cluster lifecycle Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/cluster-lifecycle-management-tools)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/cluster-lifecycle-management-tools)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



Google Distributed Cloud provides you a choice of tools to create clusters and manage the cluster lifecycle operations (update, upgrade, and delete):

  * The command-line tool `gkectl`, which you run on your admin workstation in your on-premises data center. You create a [configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file) that describes the cluster network, load balancing, and other cluster features. You specify this file on the command line to `gkectl`.
  * The Google Cloud console, Google Cloud CLI, or [Terraform](https://www.terraform.io), which you can run from any computer that has network connectivity to the GKE On-Prem API. These standard tools use the [GKE On-Prem API](https://docs.cloud.google.com/anthos/clusters/docs/on-prem-api/reference/rest), which runs on Google Cloud infrastructure. Collectively, the standard tools are referred to as the _GKE On-Prem API clients_. To manage the lifecycle of your clusters, the GKE On-Prem API must store metadata about your cluster's state in Google Cloud, in the Google Cloud region that you specify when creating the cluster. This metadata lets the API manage the cluster lifecycle and doesn't include workload-specific data.



No matter which tool you use to create clusters, the information that you gather and provide to the tool, such as the IP addresses of cluster node machines and load balancer VIPs, is the same.

This selection lets you choose the best tool for your use case and environment. For example:

  * For your first installations in a development environment, you might want to use the Google Cloud console because the user interface provides additional guidance and help.
  * If your organization already uses the gcloud CLI or Terraform to manage other Google Cloud resources, you will probably want to use these tools for Google Distributed Cloud as well.
  * If your organization has regulatory requirements or restrictions, you might need to limit your reliance on Google Cloud and use `gkectl` on your admin workstation to create clusters and manage cluster lifecycle.



In 1.15.3 and later, if you create a cluster with `gkectl`, you can enroll it at cluster creation time by setting [gkeOnPremAPI.enabled](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#gkeOnPremAPI-section) to `true` in the cluster configuration file. You can also [enroll the cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/enroll-cluster) after it is created, which lets you use the GKE On-Prem API clients.

## Limitations with the GKE On-Prem API clients

The `gkectl` tool is the most mature as far as features that it supports. We recommend that you review the functionality for the GKE On-Prem API clients when making a choice. The following list shows the features that are not supported by the GKE On-Prem API clients. Check this list from time to time as the GKE On-Prem API clients evolve.

  * Creating and upgrading admin clusters
  * Secret management and rotation
  * Certificate rotation
  * Authentication
  * Usage metering
  * Application level logging and monitoring
  * Advanced networking
  * Private registry
  * Seesaw load balancer
  * Windows node pools



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
