---
url: https://docs.cloud.google.com/cluster-director/docs/create/process-overview/
title: Cluster creation process overview \u00a0|\u00a0 Cluster Director \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:25:06.261728+00:00
---

# Cluster creation process overview  |  Cluster Director  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-director/docs/create/process-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Director ](https://docs.cloud.google.com/cluster-director/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-director/docs/overview)



Send feedback 

#  Cluster creation process overview Stay organized with collections  Save and categorize content based on your preferences. 

This document helps you understand the components that you need to configure before or when you create a cluster to meet the requirements of your workload. To get AI-powered assistance when you plan and design your cluster infrastructure, see [Design and optimize clusters with Compute Advisor](https://docs.cloud.google.com/cluster-director/docs/create/design-with-gemini).

## Cluster creation process

Creating a cluster involves configuring compute, storage, and networking resources, as well as the Slurm orchestrator. The following process is to help you pick the configurations that best fits your workload needs:

  1. Configure compute resources

  2. Configure storage resources

  3. Configure networking resources

  4. Optional: Configure data protection

  5. Configure the Slurm orchestrator




### Configure compute resources

You must choose the type and number of Compute Engine instances that you want to create in your cluster. You must consider the following:

  * **Machine series** : you must choose the machines series and types that you want to create in your cluster. Each cluster partition can use a different machine series. Each compute instance in your cluster serves as a node. For each type of node, we recommend the following machine series:

    * **Compute nodes** : based on your workload, use one of the following machine series:

      * **Foundational model training and inference** : A4X machine series

      * **Large model training, fine-tuning, and inference** : A4 or A3 Ultra machine series

      * **Mainstream model inference, fine tuning, and serving inference** : A3 Mega machine series

      * **General purpose high performance computing (HPC)** : N2 machine series

    * **Controller nodes** : N2 machine series

    * **Login nodes** : C4A or N2 machine series

  * **Location** : based on the locations where your chosen machine series are available, you must select the region and zone where you want to deploy your cluster. For more information, review the [regions and zones where machine series are available](https://docs.cloud.google.com/compute/docs/regions-zones#available).

  * **Consumption option** : you must choose the _consumption option_ that you want to use to get and use compute resources. Each option affects the availability, obtainability, and pricing of a compute resource. For more information, see [Choose a consumption option](https://docs.cloud.google.com/cluster-director/docs/choose-consumption-option).




### Configure storage resources

You must define the storage that your cluster uses:

  * **Shared file system for`/home` directory**: a [Filestore instance](https://docs.cloud.google.com/filestore/docs/overview) or [Managed Lustre instance](https://docs.cloud.google.com/managed-lustre/docs/overview) is required for the shared `/home` directory in a Slurm cluster. When you create a cluster, you can do one of the following:

    * Let Cluster Director create a new Filestore or Managed Lustre instance with pre-configured settings.

    * Use an existing Filestore or Managed Lustre instance on the same VPC network as your cluster.

If you use the [Dynamic tier](https://docs.cloud.google.com/managed-lustre/docs/performance-tiers#dynamic_tier) for Managed Lustre, then your cluster must use an existing VPC network that has the `dynamic_tier_capacity` quota allocated.

  * **Additional storage** : for large-scale AI workloads that require more storage, you can add other solutions—for example, [Cloud Storage buckets](https://docs.cloud.google.com/storage/docs/introduction).


**Note:** You can use both new and existing storage resources in the same cluster. If you use an existing Filestore or Managed Lustre instance, then the instance must be on the same VPC network as your cluster. Each storage resource that you define must specify either a new resource configuration or an existing resource configuration, not both. 

### Configure networking resources

You must define the networking resources that your cluster uses. To do so, choose one of the following options:

  * Create a new VPC network

  * Use an existing VPC or Shared VPC network




#### Create a new VPC network

If you want the cluster to use a new VPC network, then Cluster Director creates the network on your behalf. Cluster Director automatically configures the necessary firewall rules to let you connect to your cluster.

#### Use an existing VPC or Shared VPC network

To use an existing VPC or Shared VPC network in your cluster, you must configure the network and subnetwork as follows:

  * You must enable Private Google Access in your network. For instructions, see [Private Google Access configuration](https://docs.cloud.google.com/vpc/docs/configure-private-google-access).

  * You must configure firewall rules that allow the following:

    * [SSH connections to VMs](https://docs.cloud.google.com/firewall/docs/using-firewalls#common-use-cases-allow-ssh)

    * [Internal ingress connections among VMs](https://docs.cloud.google.com/firewall/docs/using-firewalls#common-use-cases-allow-internal)

  * You must configure the subnetwork as follows:

    * The subnetwork must allow health checks by using the TCP protocol and port `8319`. For more information, see [Use health checks](https://docs.cloud.google.com/load-balancing/docs/health-checks).

    * The subnetwork must have a firewall rule that allows Identity-Aware Proxy (IAP) to access the VMs by using the TCP protocol on port `22`. For more information, see [Prepare your project for IAP TCP forwarding](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding#preparing_your_project_for_tcp_forwarding).

    * The subnetwork can't overlap with the following IPv4 address ranges:

      * `10.20.1.0/28`

      * `10.0.0.0/17`

      * `192.168.64.0/18`

      * `192.168.128.0/18`

  * If you want to use a Shared VPC network, then you must also do the following:

    * [Configure private services access](https://docs.cloud.google.com/vpc/docs/configure-private-services-access).

    * Enable the Cloud DNS API in the network's host project.

    * Grant the following IAM roles either at the host project level or the subnetwork level:

      * **Grant access to all subnets in the host project:**

        * The [Compute Network User (`roles/compute.networkUser`) role](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkUser) to the [Google APIs Service Agent](https://docs.cloud.google.com/iam/docs/service-account-types#google-apis-service-agent)

        * The [Hypercompute Shared VPC Service Agent (`roles/hypercomputecluster.sharedVpcServiceAgent`) role](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.sharedVpcServiceAgent) to the Cluster Director Service Agent (`service-PROJECT_NUMBER@gcp-sa-hypercomputecluster.iam.gserviceaccount.com`)

      * **Grant access to specific subnets** : use this option if your organization's policies require more granular control. Grant the following IAM roles:

        * The [Compute Network User (`roles/compute.networkUser`) role](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkUser) on the subnetwork to the [Google APIs Service Agent](https://docs.cloud.google.com/iam/docs/service-account-types#google-apis-service-agent) and Cluster Director Service Agent (`service-PROJECT_NUMBER@gcp-sa-hypercomputecluster.iam.gserviceaccount.com`)

        * The [Compute Network Viewer (`roles/compute.networkViewer`) role](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkViewer) on the network's host project to the Cluster Director Service Agent (`service-PROJECT_NUMBER@gcp-sa-hypercomputecluster.iam.gserviceaccount.com`)

        * A custom role that includes the `dns.managedZones.get`, `dns.managedZones.list`, `dns.networks.bindPrivateDNSZone`, and `dns.networks.targetWithPeeringZone` permissions on the network's host project to the Cluster Director Service Agent (`service-PROJECT_NUMBER@gcp-sa-hypercomputecluster.iam.gserviceaccount.com`)

For more information about setting up a Shared VPC network, see [Set up Shared VPC](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#set-up-shared-vpc).




### Optional: Configure data protection

If you want to help prevent sensitive data in your cluster from being copied to unauthorized sources, then use VPC Service Controls. Otherwise, skip this section. [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) lets you control communication to and among services that Google manages. To use Cluster Director with VPC Service Controls, you must create a security boundary around your resources. Google then creates a service perimeter to manage this boundary.

To create a service perimeter, follow the instructions on [Create a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters) and specify the following configurations:

  * **Perimeter resources (`perimeterResources`)**: include the project in which you want to create your cluster. If you want to use an existing Shared VPC network in your cluster, then you must also include the host project of that network.

  * **Restricted services (`restrictedServices`)**: include the following APIs:

    * Compute Engine API (`compute.googleapis.com`)

    * Filestore API (`file.googleapis.com`)

    * Hypercompute Cluster API (`hypercomputecluster.googleapis.com`)

    * Cloud Logging API (`logging.googleapis.com`)

    * Google Cloud Managed Lustre API (`lustre.googleapis.com`)

    * Cloud Monitoring API (`monitoring.googleapis.com`)




After you create the service perimeter, it can take up to 30 minutes for the changes to take effect. After that time, the service perimeter applies to any cluster that you create in your project.

### Configure the Slurm orchestrator

For the final step, you must configure the Slurm orchestrator. To configure the orchestrator, you define the following components:

  * **Login and controller nodes** : you must define the machine series and boot disk options for the login and controller nodes. These nodes manage the cluster and let you connect to it. Controller nodes require standalone boot disks. For login nodes, you can specify [standalone boot disks or storage pools](https://docs.cloud.google.com/cluster-director/docs/storage#boot-disk-storage) if your selected machine series supports Hyperdisk.

  * **Partitions and nodesets** : you must define how you want to group your compute resources. Each partition can contain one or more nodesets, letting you create different pools of resources for different types of jobs. For each nodeset, you must specify the minimum and maximum number of compute instances. For node boot disks, you can specify [standalone boot disks or storage pools](https://docs.cloud.google.com/cluster-director/docs/storage#boot-disk-storage).

**Important:** If you use A4X VMs in a nodeset, then the total number of VMs in the nodeset must be a multiple of 18. This total is the sum of the static node count and the dynamic node count. Because Compute Engine provisions A4X capacity in indivisible sub-blocks for creating 18 VMs, any remaining capacity is unusable.



## What's next

  * [Try out Cluster Director](https://docs.cloud.google.com/cluster-director/docs/create/quickstart)

  * [Choose a consumption option](https://docs.cloud.google.com/cluster-director/docs/choose-consumption-option)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
