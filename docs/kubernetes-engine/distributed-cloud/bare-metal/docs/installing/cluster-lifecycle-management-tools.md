---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools/
title: Choose a tool to manage cluster lifecycle \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:26.275209+00:00
---

# Choose a tool to manage cluster lifecycle  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/cluster-lifecycle-management-tools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Choose a tool to manage cluster lifecycle Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud provides you a choice of tools to create clusters and manage the cluster lifecycle operations (update, upgrade, and delete):

  * The command-line tool `bmctl`, which you run on your admin workstation in your on-premises data center. You create a [configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref) that describes the cluster network, load balancing, and other cluster features. You specify this file on the command line to `bmctl`. You can also run `kubectl` on your admin workstation to upgrade and update clusters and to delete user clusters.
  * The Google Cloud console, Google Cloud CLI, or [Terraform](https://www.terraform.io), which you can run from any computer that has network connectivity to the [GKE On-Prem API](https://docs.cloud.google.com/anthos/clusters/docs/on-prem-api/reference/rest). These standard tools use the GKE On-Prem API, which runs on Google Cloud infrastructure. Collectively, the standard tools are referred to as the _GKE On-Prem API clients_. To manage the lifecycle of your clusters, the GKE On-Prem API must store metadata about your cluster's state in Google Cloud, in the Google Cloud region that you specify when creating the cluster. This metadata lets the API manage the cluster lifecycle and doesn't include workload-specific data.



No matter which tool you use to create clusters, the information that you gather and provide to the tool, such as the IP addresses of cluster node machines and load balancer VIPs, is the same.

This selection lets you choose the best tool for your use case and environment. For example:

  * For your first installations in a development environment, you might want to use the console because the user interface provides additional guidance and help.
  * If your organization already uses the gcloud CLI or Terraform to manage other Google Cloud resources, you will probably want to use these tools for Google Distributed Cloud as well.
  * If your organization has regulatory requirements or restrictions, you might need to limit your reliance on Google Cloud and use `bmctl` on your admin workstation to create clusters and manage cluster lifecycle.



If you create a cluster with `bmctl`, you can [enroll the cluster with the GKE On-Prem API](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/enroll-cluster) after the cluster is created, which lets you also use the GKE On-Prem API clients.

## Limitations with the GKE On-Prem API clients

The `bmctl` tool was shipped with the first release of Google Distributed Cloud, and it is the most mature as far as features that it supports. We recommend that you review the functionality for the GKE On-Prem API clients when making a choice. The following list summarizes current limitations. Check this list from time to time as the GKE On-Prem API clients evolve.

  * Admin and user clusters are the only supported cluster types

  * The latest minor or patch versions aren't available in the GKE On-Prem API until 7 to 10 days after the release

  * The following advanced networking features aren't supported:

    * [IPv4/IPv6 dual-stack networking](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/dual-stack-networking)
    * [IPv4 flat mode network model](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/flat-network)



## What's next

  * `bmctl`

    * [Cluster configuration field reference](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref#cluster_configuration_fields)
  * gcloud CLI

    * [`gcloud container bare-metal clusters`](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters)

    * [`gcloud container bare-metal node-pools`](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/node-pools)

    * [`gcloud container bare-metal admin-clusters`](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/admin-clusters)

  * Terraform

    * [`google_gkeonprem_bare_metal_cluster`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gkeonprem_bare_metal_cluster)

    * [`google_gkeonprem_bare_metal_node_pool`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gkeonprem_bare_metal_node_pool)

    * [`google_gkeonprem_bare_metal_admin_cluster`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gkeonprem_bare_metal_admin_cluster)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
