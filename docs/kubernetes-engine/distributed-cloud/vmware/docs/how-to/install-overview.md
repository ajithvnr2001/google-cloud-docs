---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/install-overview/
title: Google Distributed Cloud installation overview \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:19:39.017505+00:00
---

# Google Distributed Cloud installation overview  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/install-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Google Distributed Cloud installation overview Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the planning process and the steps for a software-only installation of Google Distributed Cloud for VMware. This is a multi-stage process, during which you need to make decisions about the type of configuration that will meet your organizational needs. You might need to get help from others, such as your network administrator, to set up a vSphere infrastructure and provide you with information you need to complete configuration files.

This page is for Admins, Architects, and Operators who set up, monitor, and manage the tech infrastructure. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Before you begin

Before reading this page, ensure that you're familiar with the following:

  * Kubernetes

    * [Kubernetes cluster](https://kubernetes.io/docs/concepts/overview/components)
    * [Cluster node](https://kubernetes.io/docs/concepts/architecture/nodes/)
    * [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs)
  * VMware

    * [vCenter Server](https://www.vmware.com/products/vcenter-server.html)
    * [vSphere](https://www.vmware.com/products/vsphere.html)
    * [data center](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vcenter-and-host-management.htmle)
    * [host](https://docs.vmware.com/en/VMware-vSphere/index.html)
    * [vSphere Cluster](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-resource-management.html)
    * [resource pool](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-resource-management.html)
    * [datastore](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-storage.html)



## Overview of installation steps

These are the primary steps involved in an installation of Google Distributed Cloud:

  1. Plan your installation.

  2. Set up your vSphere environment.

  3. Set up Cloud resources, including a Google Cloud project and service accounts.

  4. Create an admin workstation. The admin workstation is a machine that has the tools you need to create clusters.

  5. From your admin workstation, create an admin cluster. An admin cluster is a point of management for a set of user clusters that run your workloads.

  6. Create one or more user clusters.

  7. Deploy a workload on a user cluster.




## 1\. Plan your installation

Google Distributed Cloud provides a way for you to create [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview) clusters in a [vSphere environment](https://docs.vmware.com/en/VMware-vSphere/index.html) on your own premises.

Your workloads run on user clusters, and user clusters are managed by an admin cluster. The following diagram shows an admin cluster that manages two user clusters. User cluster 1 has eight nodes, and user cluster 2 has five nodes. The user clusters shown in the diagram have Controlplane V2 enabled, which means that the control plane for a user cluster runs in the user cluster itself.

[ ![Diagram of an admin cluster and two user clusters](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/vmware/docs/images/diagram-install-overview.svg)](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/vmware/docs/images/diagram-install-overview.svg) Architecture with two user clusters (Click to enlarge)

The preceding diagram illustrates these points:

  * A user cluster has _control-plane nodes_ and _worker nodes_. The Kubernetes control plane runs on the control-plane nodes, and your workloads run on the worker nodes.

  * The Kubernetes control-plane components for a cluster run on one or more nodes in the cluster itself.

  * The admin workstation is a machine that is separate from the clusters.




### Plan your user clusters

Think ahead about how many user clusters you intend to create and how many nodes you want each user cluster to have. For example, you might want to create separate clusters for different departments in your organization. Certain clusters might need to support heavy customer traffic, and other clusters might need to support only light internal traffic.

Think about which of your workloads need to be highly available. Then decide which of your user clusters need to have a high availability (HA) control plane and which clusters would function adequately with a non-HA control plane. An HA control plane requires three nodes, and a non-HA control plane requires only one node.

### Plan your network and load balancing

Read about the [load balancing options](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/setup-load-balance) for your installation and decide which kind of load balancer would work best for you. Depending on which option you choose, you might have to set up your load balancer before you create your clusters.

Read about the options for [connecting to Google](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/connect-on-prem-gcp), and decide which kind of connection is best for you.

## 2\. Set up your vSphere environment

Obtain the [required vSphere licenses](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vsphere-requirements#license_requirements).

Set up a physical network that has a machine to run [vCenter Server](https://www.vmware.com/products/vcenter-server.html) and several machines to run the [ESXi hypervisor](https://www.vmware.com/products/esxi-and-esx.html). Install vCenter Server on a physical machine, and install ESXi on several physical machines. These physical machines are called _hosts_.

Set up physical [storage](https://www.vmware.com/products/cloud-infrastructure/vsphere) for your vSphere environment.

### Plan your IP addresses

Decide how you want your cluster nodes to get their IP addresses. The options are:

  * From a DHCP server that you provide.
  * From a list of static IP addresses that you provide.



In either case, ensure that enough IP addresses are available for your cluster nodes and virtual IP addresses (VIPs) that need to be configured on your load balancer. For more information, see [Plan your IP addresses](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/plan-ip-addresses).

### Set up your vSphere object hierarchy

Use your instance of vCenter Server to create one or more [vSphere data centers](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vcenterhost.doc/GUID-7FDFBDBE-F8AC-4D00-AE5E-3F14D7472FAF.html). Recall that a vSphere data center is not the same as a physical building. Sometimes a vSphere data center is called a _virtual data center_. Use your instance of vCenter Server to add vSphere inventory objects to your data centers. These inventory objects include [cluster](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.resmgmt.doc/GUID-487C09CE-8BE2-4B89-BA30-0E4F7E3C66F7.html), [resource pool](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.resmgmt.doc/GUID-60077B40-66FF-4625-934A-641703ED7601.html), [network](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.networking.doc/GUID-35B40B0B-0C13-43B2-BC85-18C9C91BE2D4.html), [datastore](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.storage.doc/GUID-3CC7078E-9C30-402C-B2E1-2542BEE67E8F.html), and [folder](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vcenterhost.doc/GUID-031BDB12-D3B2-4E2D-80E6-604F304B4D0C.html).

**Note:** that the word _cluster_ has two meanings. In some contexts, it refers to a vSphere cluster, which is a vSphere inventory object. In other contexts, it refers to a GKE cluster.

#### Using separate vSphere clusters

Think about whether you want your GKE clusters to be in the same vSphere cluster or in separate vSphere clusters. For example, you could have your admin cluster in one vSphere cluster and your user clusters in a different vSphere cluster. Or you could have each user cluster in its own vSphere cluster.

The following diagram illustrates a vSphere setup you could use if you want to put an admin cluster in one vSphere cluster and a user cluster in a different vSphere cluster:

[ ![Diagram of a data center with two vSphere clusters](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/vmware/docs/images/one-data-center-two-clusters.svg)](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/vmware/docs/images/one-data-center-two-clusters.svg) vSphere setup with one data center and two vSphere clusters (Click to enlarge)

#### Using separate data centers

Another option is to have your GKE clusters in separate data centers.

The following diagram illustrates a vSphere setup you could use if you want to put an admin cluster in one data center and a user cluster in a different data center:

[ ![Diagram of two data centers](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/vmware/docs/images/two-data-centers.svg)](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/vmware/docs/images/two-data-centers.svg) vSphere setup with two data centers (Click to enlarge)

For more information about setting up your vSphere environment, see:

  * [vSphere requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vsphere-requirements)
  * [CPU, RAM, and storage requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cpu-ram-storage)
  * [Proxy and firewall rules](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/firewall-rules)



## 3\. Set up Google Cloud resources

Before you create your admin workstation, you need to install the Google Cloud CLI, create a Google Cloud project, and create service accounts. For instructions, see:

  * [Install the Google Cloud CLI](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cloud-sdk). The Google Cloud CLI is a set of tools to create and manage Google Cloud resources.

  * [Create Google Cloud projects](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/multiple-gcp-projects) A Google Cloud project provides a way of organizing your Google Cloud resources. You must have at least one Google Cloud project. When you create a user cluster, you must register the cluster to a [fleet](https://docs.cloud.google.com/anthos/fleet-management/docs), which requires that you specify a fleet host project.

  * [Create service accounts](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts). Google Distributed Cloud uses Google Cloud [service accounts](https://docs.cloud.google.com/iam/docs/understanding-service-accounts) with specific permissions to download cluster components from Google Cloud, register clusters to a fleet, and perform other tasks.




## 4\. Create an admin workstation

The admin workstation is a machine that you use to create and manage clusters. The admin workstation can be a VM in your vSphere environment, or it can be a machine that is separate from your vSphere environment.

For instructions on how to create an admin workstation, see [Create an admin workstation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-workstation).

## 5\. Create an admin cluster

The admin cluster manages one or more user clusters. You must create an admin cluster before you create user clusters to run your workloads. For more information, see [Create an admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-cluster).

### Enroll the cluster in the GKE On-Prem API

Optionally, enroll your admin cluster in the GKE On-Prem API. Enrolling your admin cluster in the GKE On-Prem API lets you use standard tools—the Google Cloud console, Google Cloud CLI, or [Terraform](https://www.terraform.io/)—to upgrade user clusters that the admin cluster manages. The GKE On-Prem API stores cluster state metadata in Google Cloud. This metadata lets the API manage the user cluster lifecycle and doesn't include workload-specific data. The standard tools use the GKE On-Prem API to manage the user cluster lifecycle, and collectively are referred to as the _GKE On-Prem API clients_. Enrolling your admin cluster also lets you run `gcloud` commands to [get information about your admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/enroll-cluster#get_cluster_information).

Google Distributed Cloud provides the following ways to enroll your admin cluster in the GKE On-Prem API:

  * Before the cluster is created: Include the `gkeOnPremAPI` section in the [admin cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#gkeOnPremAPI-section).

  * After the cluster is created: Use the gcloud CLI to [enroll the cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/enroll-cluster).




## 6\. Create user clusters

After you create an admin cluster, you can create one or more user clusters. You can create user clusters by using standard tools—the console, gcloud CLI, or Terraform—or by running `gkectl` on your admin workstation. For more information about using the standard tools, see [Choose a tool to manage cluster lifecycle](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cluster-lifecycle-management-tools).

  * To create a user cluster using a standard tool, see _Create a user cluster_ ([Console](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster#console) | [gcloud-cli](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster#gcloud-cli) | [Terraform](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster#terraform)). When you create a user cluster using a standard tool, the cluster is automatically enrolled in the GKE On-Prem API.

  * To create a user cluster using `gkectl`, follow the instructions in _Create a user cluster_ ([gkectl](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster#gkectl)). Optionally, you can enroll your user cluster in the GKE On-Prem API. Google Distributed Cloud provides the following ways to enroll your user cluster in the GKE On-Prem API if you use `gkectl` to create the cluster:

    * Before the cluster is created: Include the `gkeOnPremAPI` section in the [user cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#gkeOnPremAPI-section).

    * After the cluster is created: Use the gcloud CLI to [enroll the cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/enroll-cluster).




## 7\. Deploy a workload on a user cluster

To learn how to create a Deployment, a Service and an Ingress on a user cluster, see:

  * [Deploy an application](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/deploy-first-app)

  * [Create a Service and an Ingress](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-service-ingress)




## What's next?

Start the installation process by [setting up your on-premises infrastructure](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vsphere-requirements).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
