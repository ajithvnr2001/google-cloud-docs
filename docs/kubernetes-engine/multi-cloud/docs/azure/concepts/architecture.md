---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/architecture/
title: GKE on Azure architecture \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:20.940429+00:00
---

# GKE on Azure architecture  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/architecture/

The product described by this documentation, GKE on Azure, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE on Azure ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/architecture)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# GKE on Azure architecture

GKE on Azure is a managed service that helps you provision, operate, and scale Kubernetes clusters in your Azure account.

This page is for Admins and architects and Operators who want to define IT solutions and system architecture in accordance with company strategy and requirements. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Resource management

GKE on Azure uses Azure APIs to provision the resources needed by your cluster, including virtual machines, managed disks, virtual machine scale set, network security groups, and load balancers.

You can create, describe, and delete clusters with the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/container/azure) or [GKE Multi-Cloud API](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/reference/rest).

### Authenticating to Azure

When you set up GKE on Azure, you create an Azure Active Directory (Azure AD) application and service principal with the required permissions. You also create a client certificate that the GKE Multi-Cloud API uses to authenticate as the application's service principal. 

For more information about Azure AD and service principals, see [Application and service principal objects in Azure Active Directory](https://docs.microsoft.com/en-us/azure/active-directory/develop/app-objects-and-service-principals). 

For more information, see [Authentication overview](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/authentication).

### Resources on Google Cloud

GKE on Azure uses a Google Cloud project to store cluster configuration information on Google Cloud.

**Warning:** Soon after you delete a Google Cloud project, any cluster resources in Azure are permanently deleted. To safeguard against the accidental deletion of a Google Cloud project, use [Project liens](https://docs.cloud.google.com/resource-manager/docs/project-liens).

## Fleets and Connect

GKE on Azure registers each cluster with a [Fleet](https://docs.cloud.google.com/anthos/multicluster-management/fleets) when it is created. [Connect](https://docs.cloud.google.com/anthos/multicluster-management/connect/overview) enables access to cluster and workload management features from Google Cloud. A cluster's Fleet membership name is the same as its cluster name.

You can enable features such as Config Management and Cloud Service Mesh within your Fleet.

## Cluster architecture

GKE on Azure provisions clusters using private subnets inside your Azure Virtual Network. Each cluster consists of the following components:

  * **Control plane** : The Kubernetes control plane uses a high-availability architecture with three replicas. Each replica runs all Kubernetes components including `kube-apiserver`, `kube-controller-manager`, `kube-scheduler`, and `etcd`. Each `etcd` instance stores data in an Azure Disk volume, and uses a network interface to communicate with other `etcd` instances. A standard load balancer is used to balance traffic to the Kubernetes API endpoint, `kube-apiserver`.

You can create a control plane in multiple zones, or in a single zone. For more information, see [Create a cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-cluster). 

  * **Node pools** : A node pool is a group of Kubernetes worker nodes with the same configuration, including instance type, disk configuration, and instance profile. All nodes in a node pool run on the same subnet. For high availability, you can provision multiple node pools across different subnets in the same Azure region.




## What's next

  * Complete the [Prerequisites](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/prerequisites).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
