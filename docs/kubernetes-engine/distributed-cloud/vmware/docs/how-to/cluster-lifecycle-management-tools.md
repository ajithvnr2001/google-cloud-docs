---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cluster-lifecycle-management-tools/
title: Choose a tool to manage cluster lifecycle \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:53.233006+00:00
---

# Choose a tool to manage cluster lifecycle  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cluster-lifecycle-management-tools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Choose a tool to manage cluster lifecycle Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud provides you a choice of tools to create clusters and manage the cluster lifecycle operations (update, upgrade, and delete):

  * The command-line tool `gkectl`, which you run on your admin workstation in your on-premises data center. You create a [configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest) that describes the cluster network, load balancing, and other cluster features. You specify this file on the command line to `gkectl`.
  * The Google Cloud console, Google Cloud CLI, or [Terraform](https://www.terraform.io), which you can run from any computer that has network connectivity to the GKE On-Prem API. These standard tools use the [GKE On-Prem API](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api-overview), which runs on Google Cloud infrastructure. Collectively, the standard tools are referred to as the _GKE On-Prem API clients_. To manage the lifecycle of your clusters, the GKE On-Prem API must store metadata about your cluster's state in Google Cloud, in the Google Cloud region that you specify when creating the cluster. This metadata lets the API manage the cluster lifecycle and doesn't include workload-specific data.



No matter which tool you use to create clusters, the information that you gather and provide to the tool, such as the IP addresses of cluster node machines and load balancer VIPs, is the same.

This selection lets you choose the best tool for your use case and environment. For example:

  * For your first installations in a development environment, you might want to use the Google Cloud console because the user interface provides additional guidance and help.
  * If your organization already uses the gcloud CLI or Terraform to manage other Google Cloud resources, you will probably want to use these tools for Google Distributed Cloud as well.
  * If your organization has regulatory requirements or restrictions, you might need to limit your reliance on Google Cloud and use `gkectl` on your admin workstation to create clusters and manage cluster lifecycle.



If you create a cluster with `gkectl`, it will be enrolled with the GKE On-Prem API by default. You can also [enroll the cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/enroll-cluster) after it is created, which lets you use the GKE On-Prem API clients.

## Limitations with the GKE On-Prem API clients

The `gkectl` tool is the most mature as far as features that it supports. We recommend that you review the capabilities for the GKE On-Prem API clients when making a choice. The following features aren't supported by the GKE On-Prem API clients:

  * Secret management and rotation
  * Certificate rotation
  * Authentication
  * Usage metering
  * Application level logging and monitoring
  * Advanced networking
  * Windows node pools



The following list describes additional limitations with the GKE On-Prem API clients:

  * The gcloud CLI isn't supported for any admin cluster lifecycle operation. You can use `gkectl`, the console, the gcloud CLI, or Terraform to create admin clusters.

  * The `gkectl` command-line tool is the only tool available for upgrading, updating, and deleting admin clusters.

  * Only `gkectl` and Terraform support using a [private registry](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/private-registry).

  * The kind of load balancer for an admin cluster and its user clusters must be the same. The only exception is if the admin cluster uses Seesaw, then the user clusters can use MetalLB. If you want your admin and user clusters to use different kinds of load balancers, you must create the clusters using `gkectl`. 

  * When you create a user cluster using the Google Cloud console, all the [`vCenter` settings](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#vcenter-section) are inherited from the admin cluster. If you need a user cluster to have different `vCenter` settings from its admin cluster, use the gcloud CLI, Terraform, or `gkectl` to create the user cluster. 




## Advanced cluster limitations

When you create a cluster, whether Google Distributed Cloud creates an advanced cluster or a non-advanced cluster by default depends on the version, as follows:

  * Version 1.32 or lower: a non-advanced cluster is created by default.
  * Version 1.33 or higher: an advanced cluster is created default.



Only Terraform and the `gkectl` command-line tool have the ability to change the default behavior. To change the default behavior, do the following:

  * `gkectl`: include the `enableAdvancedCluster` boolean field in your cluster configuration file. For example, to create an advanced cluster with a 1.32 version, specify `enableAdvancedCluster: true` in your cluster configuration file.

  * Terraform: include the `enable_advanced_cluster` boolean field in your configuration file (typically called `main.tf`). For example, to create an advanced cluster with a 1.32 version, add `enable_advanced_cluster = true` to `main.tf`.




Only the `gkectl` command-line tool is supported in the following cases:

  * When upgrading a non-advanced cluster to an advanced cluster.
  * When upgrading a cluster from 1.32 to 1.33.



For more information, see [Update or upgrade a cluster to an advanced cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/update-or-upgrade-to-adv-cluster).

The GKE On-Prem API clients have limitations on the create, upgrade, update, and delete operations, as captured in the following table. Only the `gkectl` command-line tool is supported for all operations, with the exception of admin cluster delete. Deleting an admin cluster is a special case, which involves deleting Google Cloud resources, load balancer resources, the VM, and vSphere data disk. For more information, see [Deleting an admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/deleting-an-admin-cluster).

Use the following drop-down menus to filter the table by client and cluster type:

Select a clientConsolegcloud CLITerraformSelect a cluster typeNon-advanced user clusterNon-advanced admin clusterAdvanced user clusterAdvanced admin cluster

The following table shows what cluster operations are supported for the selected client:

Client | Cluster type | Operation | Supported / Version  
---|---|---|---  
Terraform | Non-advanced user cluster | Create | 1.32 or lower  
Terraform | Non-advanced user cluster | Upgrade and stay non-advanced | 1.32 or lower  
Terraform | Non-advanced user cluster | Upgrade to advanced | No  
Terraform | Non-advanced user cluster | Update configuration | Yes  
Terraform | Non-advanced user cluster | Delete | Yes  
Terraform | Advanced user cluster | Create | 1.33.200 or higher  
Terraform | Advanced user cluster | Upgrade | 1.33.200 or higher  
Terraform | Advanced user cluster | Update configuration | Yes  
Terraform | Advanced user cluster | Delete | Yes  
Terraform | Non-advanced admin cluster | Create | 1.32 or lower  
Terraform | Non-advanced admin cluster | Upgrade and stay non-advanced | No  
Terraform | Non-advanced admin cluster | Upgrade to advanced | No  
Terraform | Non-advanced admin cluster | Update configuration | Yes  
Terraform | Non-advanced admin cluster | Delete | No  
Terraform | Advanced admin cluster | Create | 1.33.200 or higher  
Terraform | Advanced admin cluster | Upgrade | No  
Terraform | Advanced admin cluster | Update configuration | Yes  
Terraform | Advanced admin cluster | Delete | No  
Console | Non-advanced user cluster | Create | 1.32 or lower  
Console | Non-advanced user cluster | Upgrade and stay non-advanced | 1.32 or lower  
Console | Non-advanced user cluster | Upgrade to advanced | No  
Console | Non-advanced user cluster | Update configuration | Yes  
Console | Non-advanced user cluster | Delete | Yes  
Console | Advanced user cluster | Create | 1.33.200 or higher  
Console | Advanced user cluster | Upgrade | 1.33.200 or higher  
Console | Advanced user cluster | Update configuration | Yes  
Console | Advanced user cluster | Delete | Yes  
Console | Non-advanced admin cluster | Create | 1.32 or lower  
Console | Non-advanced admin cluster | Upgrade and stay non-advanced | No  
Console | Non-advanced admin cluster | Upgrade to advanced | No  
Console | Non-advanced admin cluster | Update configuration | No  
Console | Non-advanced admin cluster | Delete | No  
Console | Advanced admin cluster | Create | 1.33.200 or higher  
Console | Advanced admin cluster | Upgrade | No  
Console | Advanced admin cluster | Update configuration | No  
Console | Advanced admin cluster | Delete | No  
gcloud CLI | Non-advanced user cluster | Create | 1.32 or lower  
gcloud CLI | Non-advanced user cluster | Upgrade and stay non-advanced | 1.32 or lower  
gcloud CLI | Non-advanced user cluster | Upgrade to advanced | No  
gcloud CLI | Non-advanced user cluster | Update configuration | Yes  
gcloud CLI | Non-advanced user cluster | Delete | Yes  
gcloud CLI | Advanced user cluster | Create | 1.33.200 or higher  
gcloud CLI | Advanced user cluster | Upgrade | 1.33.200 or higher  
gcloud CLI | Advanced user cluster | Update configuration | Yes  
gcloud CLI | Advanced user cluster | Delete | Yes  
gcloud CLI | Non-advanced admin cluster | Create | No  
gcloud CLI | Non-advanced admin cluster | Upgrade and stay non-advanced | 1.32 and lower  
gcloud CLI | Non-advanced admin cluster | Upgrade to advanced | No  
gcloud CLI | Non-advanced admin cluster | Update configuration | No  
gcloud CLI | Non-advanced admin cluster | Delete | No  
gcloud CLI | Advanced admin cluster | Create | No  
gcloud CLI | Advanced admin cluster | Upgrade | 1.33.200 and higher  
gcloud CLI | Advanced admin cluster | Update configuration | No  
gcloud CLI | Advanced admin cluster | Delete | No  
  
Check on these limitations from time to time as the GKE On-Prem API clients evolve.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
