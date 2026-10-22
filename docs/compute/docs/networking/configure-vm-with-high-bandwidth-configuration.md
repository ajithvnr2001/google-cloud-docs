---
url: https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration/
title: Configure per VM Tier_1 networking performance \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:43.355008+00:00
---

# Configure per VM Tier_1 networking performance  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Configure per VM Tier_1 networking performance Stay organized with collections  Save and categorize content based on your preferences. 

Compute Engine lets you select a high-bandwidth per VM Tier_1 networking performance configuration for certain Compute Engine virtual machine (VM) and bare metal instances. Compute instances with Tier_1 networking configurations are especially useful for large, distributed compute workloads with lots of heavy internode communications, such as high performance computing (HPC), machine learning (ML), and deep learning (DL).

Combining these high network throughput instances with high-performance Local SSD storage is beneficial for I/O-intensive, flash-optimized databases.

## Before you begin

  * Review the pricing for per VM Tier_1 networking performance at [Tier_1 higher bandwidth network pricing](https://cloud.google.com/products/compute/pricing/general-purpose#tier-1-higher-bandwidth-network-pricing). 
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




### Required roles

To get the permissions that you need to configure an instance to use per VM Tier_1 networking performance, ask your administrator to grant you the following IAM roles on your project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * [Create Service Accounts ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountCreator) (`roles/iam.serviceAccountCreator`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to configure an instance to use per VM Tier_1 networking performance. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to configure an instance to use per VM Tier_1 networking performance:

  * To create instances: 
    * `compute.instances.create` on the project
    * To use a custom image to create the VM: `compute.images.useReadOnly` on the image
    * To use a snapshot to create the VM: `compute.snapshots.useReadOnly` on the snapshot
    * To use an instance template to create the VM: `compute.instanceTemplates.useReadOnly` on the instance template
    * To assign a [legacy network](https://docs.cloud.google.com/vpc/docs/legacy) to the VM: `compute.networks.use` on the project
    * To specify a static IP address for the VM: `compute.addresses.use` on the project
    * To assign an external IP address to the VM when using a legacy network: `compute.networks.useExternalIp` on the project
    * To specify a subnet for the VM: `compute.subnetworks.use` on the project or on the chosen subnet
    * To assign an external IP address to the VM when using a VPC network: `compute.subnetworks.useExternalIp` on the project or on the chosen subnet
    * To set VM instance metadata for the VM: `compute.instances.setMetadata` on the project
    * To set tags for the VM: `compute.instances.setTags` on the VM
    * To set labels for the VM: `compute.instances.setLabels` on the VM
    * To set a service account for the VM to use: `compute.instances.setServiceAccount` on the VM
    * To create a new disk for the VM: `compute.disks.create` on the project
    * To attach an existing disk in read-only or read-write mode: `compute.disks.use` on the disk
    * To attach an existing disk in read-only mode: `compute.disks.useReadOnly` on the disk
  * To update an instance to include Tier_1 networking: 
    * `compute.instances.update`
    * Permission to use the resources that you want to modify on the instance, forexample `compute.networks.use`
  * To create an instance template with Tier_1 networking: `compute.instanceTemplates.create`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Limitations

  * Compute Engine is the only product area supporting Tier_1 networking.
  * Tier_1 networking is supported with N2, N2D, C2, C2D, C3, C3D, C4, C4A, C4D, M3, and Z3 machine types that have the minimum required vCPUs.
  * For VMs, Tier_1 networking requires the [gVNIC virtual network driver](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#create_a_vm_with_gvnic_support) and a [gVNIC-compatible OS or custom image](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#os-support).
  * [Third generation](https://docs.cloud.google.com/compute/docs/machine-resource#vm_terminology) and later VMs require gVNIC driver version 1.4.2 or later to deliver the highest network bandwidth. Make sure the operating system (OS) image that you use fully supports Tier_1 networking. [Fully supported OS images](https://docs.cloud.google.com/compute/docs/images/os-details#networking-features) include the updated gVNIC driver. You can [update the gVNIC driver](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#manual-gvnic-setup) on images that don't have the latest version.
  * Purchasable stock keeping units (SKUs) for Tier_1 networking are excluded from [committed use discounts](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts).
  * Large C4, C4D, C4N, C3, C3D, Z4D, Z4M, and Z3 instances might encounter NUMA-related bottlenecks when bandwidth is pushed beyond 100 Gbps. Depending on your application architecture, you might need to control for thread and interrupt placement. On Linux, guest OS features such as [Receive Flow Steering (RFS)](https://www.kernel.org/doc/Documentation/networking/scaling.txt) can help address this issue. Verify that your applications are NUMA-tuned to maximize your performance.



## Bandwidth tiers

The egress bandwidth limit represents the maximum possible amount of data per unit of time (for example, gigabits per second, or Gbps) that Google Cloud allows a Compute Engine instance to emit from its network interfaces (NICs). The egress bandwidth includes data transferred to all Persistent Disk and Google Cloud Hyperdisk volumes attached to the instance.

Note the following about bandwidth limits:

  * The default bandwidth limit ranges from 10 Gbps to 400 Gbps, depending on the [machine type](https://docs.cloud.google.com/compute/docs/machine-resource) and instance size.
  * Instances created with a [network-optimized machine type](https://docs.cloud.google.com/compute/docs/network-optimized-machines) or other machine type that provides multiple physical NICs have the highest egress bandwidth limits, such as 400 Gbps for C4N, M4N, Z4D, and Z4M.
  * Tier_1 networking increases the maximum egress bandwidth limit for compute instances. The maximum egress bandwidth limit ranges from 50 Gbps to 200 Gbps, depending on the size and machine type of your instance.
  * The actual egress bandwidth is always less than or equal to the egress bandwidth limit.
  * The bandwidth limits listed in the following tables apply to all network interface types that are supported by the machine type.



To achieve the highest possible egress bandwidth, **all** of the following must be true:

  * The sending and receiving compute instances must be in the same zone.
  * The instances must have NICs in the same VPC network or in VPC networks connected by VPC Network Peering.
  * Packets sent between the instances must use [internal IP address](https://docs.cloud.google.com/vpc/docs/ip-addresses#internal) destinations.
  * The VPC network that is used by the instances uses the highest [maximum transmission unit (MTU)](https://docs.cloud.google.com/vpc/docs/mtu) setting. A higher MTU reduces the packet-header overhead and thus increases payload data throughput.



For a complete discussion about egress and ingress bandwidth limits, see [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).

### General-purpose C4 VMs and bare metal instances

The following table describes the egress bandwidth limits for C4 VMs and bare metal instances. For C4 instances with Local SSD, only machine types with 288 vCPUs support Tier_1 networking.

vCPUs | Internal IP | Tier_1  
Internal IP | External IP | Tier_1  
External IP  
---|---|---|---|---  
2 | 10 Gbps | N/A | 7 Gbps | N/A  
4 | 23 Gbps | N/A | 7 Gbps | N/A  
8 | 23 Gbps | N/A | 7 Gbps | N/A  
16 | 23 Gbps | N/A | 7 Gbps | N/A  
24 | 23 Gbps | N/A | 7 Gbps | N/A  
32 | 23 Gbps | N/A | 7 Gbps | N/A  
48 | 34 Gbps | 50 Gbps | 7 Gbps | 25 Gbps  
96 | 67 Gbps | 100 Gbps | 7 Gbps | 25 Gbps  
144 | 100 Gbps | 150 Gbps | 7 Gbps | 25 Gbps  
192 | 100 Gbps | 200 Gbps | 7 Gbps | 25 Gbps  
288 | 100 Gbps | 200 Gbps | 7 Gbps | 25 Gbps  
  
### General-purpose C4A VMs and bare metal instances

The following table describes the egress bandwidth limits for C4A VMs and bare metal instances.

vCPUs | Internal IP | Tier_1 Internal IP | External IP | Tier_1 External IP  
---|---|---|---|---  
1 | 10 Gbps | N/A | 7 Gbps | N/A  
2 | 10 Gbps | N/A | 7 Gbps | N/A  
4 | 23 Gbps | N/A | 7 Gbps | N/A  
8 | 23 Gbps | N/A | 7 Gbps | N/A  
16 | 23 Gbps | N/A | 7 Gbps | N/A  
32 | 23 Gbps | 50 Gbps | 7 Gbps | 25 Gbps  
48 | 34 Gbps | 50 Gbps | 7 Gbps | 25 Gbps  
64 | 45 Gbps | 75 Gbps | 7 Gbps | 25 Gbps  
72 | 50 Gbps | 100 Gbps | 7 Gbps | 25 Gbps  
  
### General-purpose C4D VMs and bare metal instances

The following table describes the egress bandwidth limits for C4D instances.

vCPUs | Internal IP | Tier_1 Internal IP | External IP | Tier_1 External IP  
---|---|---|---|---  
2 | 10 Gbps | N/A | 7 Gbps | N/A  
4 | 20 Gbps | N/A | 7 Gbps | N/A  
8 | 20 Gbps | N/A | 7 Gbps | N/A  
16 | 20 Gbps | N/A | 7 Gbps | N/A  
32 | 23 Gbps | N/A | 7 Gbps | N/A  
48 | 34 Gbps | 50 Gbps | 7 Gbps | 25 Gbps  
64 | 45 Gbps | 75 Gbps | 7 Gbps | 25 Gbps  
96 | 67 Gbps | 100 Gbps | 7 Gbps | 25 Gbps  
192 | 100 Gbps | 150 Gbps | 7 Gbps | 25 Gbps  
384 | 100 Gbps | 200 Gbps | 7 Gbps | 25 Gbps  
  
### Network-optimized C4N instances

The following table describes the egress bandwidth limits for C4N instances.

**Note:** C4N instances achieve these bandwidth limits automatically under standard networking. Tier_1 networking isn't available on C4N instances.vCPUs | Steady-state internal1 | Maximum for internal IP | Maximum for external IP  
---|---|---|---  
2 | 4 Gbps | Up to 25 Gbps | Up to 7 Gbps  
4 | 8 Gbps | Up to 30 Gbps | Up to 7 Gbps  
8 | 16 Gbps | Up to 40 Gbps | Up to 15 Gbps  
16 | 32 Gbps | Up to 50 Gbps | Up to 25 Gbps  
24 | 50 Gbps | 50 Gbps | 25 Gbps  
48 | 100 Gbps | 100 Gbps | 50 Gbps  
96 | 200 Gbps | 200 Gbps | 100 Gbps  
1922 | 400 Gbps | 400 Gbps | 200 Gbps  
  
1 The consistent and sustainable level of network performance that the instance can maintain over an extended period of time.  
2 To achieve the full throughput for this machine type, you must configure at least 2 network interfaces (vNIC) when you create the instance, with each network interface attached to a different physical NIC (pNIC). The vNIC to pNIC mapping is assigned in a round-robin fashion automatically when you create the instance. 

### General-purpose C3 VMs and bare metal instances

The following table describes the egress bandwidth limits for C3 VMs and bare metal instances.

**Note:** If you are using a C3 bare metal instance, you can maximize network bandwidth performance by disabling sleep states. For more information, see the [troubleshooting documentation](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-performance#bare_metal_instances).vCPUs | Internal IP | Tier_1 Internal IP | External IP | Tier_1 External IP  
---|---|---|---|---  
4 | 23 Gbps | N/A | 7 Gbps | N/A  
8 | 23 Gbps | N/A | 7 Gbps | N/A  
22 | 23 Gbps | N/A | 7 Gbps | N/A  
44 | 32 Gbps | 50 Gbps | 7 Gbps | 25 Gbps  
88 | 62 Gbps | 100 Gbps | 7 Gbps | 25 Gbps  
176 | 100 Gbps | 200 Gbps | 7 Gbps | 25 Gbps  
192 | 100 Gbps | 200 Gbps | 7 Gbps | 25 Gbps  
  
### General-purpose C3D VMs

vCPUs | Internal IP | Tier_1 Internal IP | External IP | Tier_1 External IP  
---|---|---|---|---  
4 | 20 Gbps | N/A | 7 Gbps | N/A  
8 | 20 Gbps | N/A | 7 Gbps | N/A  
16 | 20 Gbps | N/A | 7 Gbps | N/A  
30 | 20 Gbps | 50 Gbps | 7 Gbps | 25 Gbps  
60 | 40 Gbps | 75 Gbps | 7 Gbps | 25 Gbps  
90 | 60 Gbps | 100 Gbps | 7 Gbps | 25 Gbps  
180 | 100 Gbps | 150 Gbps | 7 Gbps | 25 Gbps  
360 | 100 Gbps | 200 Gbps | 7 Gbps | 25 Gbps  
  
### Compute-optimized H4D instances

The following table describes the egress bandwidth limits for H4D instances.

**Note:** H4D instances achieve these bandwidth limits automatically under standard networking. Tier_1 networking isn't available on H4D instances.vCPUs | Internal IP | External IP  
---|---|---  
192 | 200 Gbps | 1 Gbps  
  
### Compute-optimized H3 VMs

The following table describes the egress bandwidth limits for H3 VMs.

**Note:** H3 VMs achieve these bandwidth limits automatically under standard networking. Tier_1 networking isn't available on H3 VMs.vCPUs | Internal IP | External IP  
---|---|---  
88 | 200 Gbps | 1 Gbps  
  
### Compute-optimized C2 VMs

The following table describes the egress bandwidth limits for C2 VMs.

vCPUs | Internal IP | Tier_1 Internal IP | External IP | Tier_1 External IP  
---|---|---|---|---  
4 | 10 Gbps | Not applicable (N/A) | 7 Gbps | N/A  
8 | 16 Gbps | N/A | 7 Gbps | N/A  
16 | 32 Gbps | N/A | 7 Gbps | N/A  
30 | 32 Gbps | 50 Gbps | 7 Gbps | 7 Gbps  
60 | 32 Gbps | 100 Gbps | 7 Gbps | 7 Gbps  
  
### Compute-optimized C2D VMs

The following table describes the egress bandwidth limits for C2D VMs.

vCPUs | Internal IP | Tier_1 Internal IP | External IP | Tier_1 External IP  
---|---|---|---|---  
2 | 10 Gbps | Not applicable (N/A) | 7 Gbps | N/A  
4 | 10 Gbps | N/A | 7 Gbps | N/A  
8 | 16 Gbps | N/A | 7 Gbps | N/A  
16 | 32 Gbps | N/A | 7 Gbps | N/A  
32 | 32 Gbps | 50 Gbps | 7 Gbps | 25 Gbps  
56 | 32 Gbps | 50 Gbps | 7 Gbps | 25 Gbps  
112 | 32 Gbps | 100 Gbps | 7 Gbps | 25 Gbps  
  
### Network and Memory-optimized M4N VMs

The following table describes the egress bandwidth limits for M4N VMs.

**Note:** M4N instances achieve these bandwidth limits automatically under standard networking. Tier_1 networking isn't available on M4N instances.vCPUs | Internal IP | External IP  
---|---|---  
16 | 50 Gbps | 7 Gbps  
28 | 50 Gbps | 7 Gbps  
32 | 57 Gbps | 7 Gbps  
56 | 100 Gbps | 7 Gbps  
64 | 114 Gbps | 7 Gbps  
112 | 200 Gbps | 7 Gbps  
2241 | 400 Gbps | 7 Gbps  
  
1 To achieve the full throughput for this machine type, you must configure at least 2 network interfaces (vNIC) when you create the instance, with each network interface attached to a different physical NIC (pNIC). The vNIC to pNIC mapping is assigned in a round-robin fashion automatically when you create the instance. 

### Memory-optimized M4 VMs

The following table describes the egress bandwidth limits for M4 VMs.

**Note:** M4 instances achieve these bandwidth limits automatically under standard networking. Tier_1 networking isn't available on M4 instances.vCPUs | Internal IP | External IP  
---|---|---  
16 | 16 Gbps | 7 Gbps  
32 | 32 Gbps | 7 Gbps  
56 | 32 Gbps | 7 Gbps  
64 | 32 Gbps | 7 Gbps  
112 | 50 Gbps | 7 Gbps  
224 | 100 Gbps | 7 Gbps  
  
### Memory-optimized M3 VMs

The following table describes the egress bandwidth limits for M3 VMs.

vCPUs | Internal IP | Tier_1 Internal IP | External IP | Tier_1 External IP  
---|---|---|---|---  
32 | 32 Gbps | N/A | 7 Gbps | N/A  
64 | 32 Gbps | 50 Gbps | 7 Gbps | 25 Gbps  
128 | 32 Gbps | 100 Gbps | 7 Gbps | 25 Gbps  
  
### General-purpose N2 VMs

The following table describes the egress bandwidth limits for N2 VMs.

vCPUs | Internal IP | Tier_1 Internal IP | External IP | Tier_1 External IP  
---|---|---|---|---  
2 | 10 Gbps | Not applicable (N/A) | 7 Gbps | N/A  
4 | 10 Gbps | N/A | 7 Gbps | N/A  
8 | 16 Gbps | N/A | 7 Gbps | N/A  
16 | 32 Gbps | N/A | 7 Gbps | N/A  
32 | 32 Gbps | 50 Gbps | 7 Gbps | 25 Gbps  
48 | 32 Gbps | 50 Gbps | 7 Gbps | 25 Gbps  
64 | 32 Gbps | 75 Gbps | 7 Gbps | 25 Gbps  
80 | 32 Gbps | 100 Gbps | 7 Gbps | 25 Gbps  
96 | 32 Gbps | 100 Gbps | 7 Gbps | 25 Gbps  
128 | 32 Gbps | 100 Gbps | 7 Gbps | 25 Gbps  
  
### General-purpose N2 (custom size shapes) VMs

The following table describes the egress bandwidth limits for custom-sized N2 VMs.

vCPUs | Internal IP | Tier_1 Internal IP | External IP | Tier_1 External IP  
---|---|---|---|---  
2, 4, or 6 | 10 Gbps | Not applicable (N/A) | 7 Gbps | N/A  
8, 10, 12, or 14 | 16 Gbps | N/A | 7 Gbps | N/A  
16, 18, 20, 22, 24, 26, 28, or 30 | 32 Gbps | N/A | 7 Gbps | N/A  
32, 36, 40, 44, 48, 52, 56, or 60 | 32 Gbps | 50 Gbps | 7 Gbps | 25 Gbps  
64, 68, 72, or 76 | 32 Gbps | 75 Gbps | 7 Gbps | 25 Gbps  
80 or more | 32 Gbps | 100 Gbps | 7 Gbps | 25 Gbps  
  
### General-purpose N2D VMs

The following table describes the egress bandwidth limits for N2D VMs.

vCPUs | Internal IP | Tier_1 Internal IP | External IP | Tier_1 External IP  
---|---|---|---|---  
2 | 10 Gbps | Not applicable (N/A) | 7 Gbps | N/A  
4 | 10 Gbps | N/A | 7 Gbps | N/A  
8 | 16 Gbps | N/A | 7 Gbps | N/A  
16 | 32 Gbps | N/A | 7 Gbps | N/A  
32 | 32 Gbps | N/A | 7 Gbps | N/A  
48 | 32 Gbps | 50 Gbps | 7 Gbps | 25 Gbps  
64 | 32 Gbps | 50 Gbps | 7 Gbps | 25 Gbps  
80 | 32 Gbps | 50 Gbps | 7 Gbps | 25 Gbps  
96 | 32 Gbps | 100 Gbps | 7 Gbps | 25 Gbps  
128 | 32 Gbps | 100 Gbps | 7 Gbps | 25 Gbps  
224 | 32 Gbps | 100 Gbps | 7 Gbps | 25 Gbps  
  
### General-purpose N2D (custom size shapes) VMs

The following table describes the egress bandwidth limits for custom-sized N2D VMs.

vCPUs | Internal IP | Tier_1 Internal IP | External IP | Tier_1 External IP  
---|---|---|---|---  
2 or 4 | 10 Gbps | Not applicable (N/A) | 7 Gbps | N/A  
8 | 16 Gbps | N/A | 7 Gbps | N/A  
16 or 32 | 32 Gbps | N/A | 7 Gbps | N/A  
48, 64, or 80 | 32 Gbps | 50 Gbps | 7 Gbps | 25 Gbps  
96 | 32 Gbps | 100 Gbps | 7 Gbps | 25 Gbps  
  
### Memory-optimized X4 instances

The following table describes the egress bandwidth limits for X4 bare metal instances.

**Note:** To maximize network bandwidth performance, see the [Troubleshooting documentation](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-performance#bare_metal_instances) for information about disabling sleep states.**Note:** X4 instances achieve these bandwidth limits automatically under standard networking. Tier_1 networking isn't available on X4 instances.vCPUs | Internal IP | External IP  
---|---|---  
960 | 100 Gbps | 7 Gbps  
1440 | 100 Gbps | 7 Gbps  
1920 | 100 Gbps | 7 Gbps  
  
### Storage-optimized Z3 VMs and bare metal instances

The following table describes the egress bandwidth limits for Z3 instances.

**Note:** If you are using a Z3 bare metal instance, you can maximize network bandwidth performance by disabling sleep states. For more information, see the [troubleshooting documentation](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-performance#bare_metal_instances).vCPUs | Internal IP | Tier_1 Internal IP | External IP | Tier_1 External IP  
---|---|---|---|---  
8, 14, 16, or 22 | 23 Gbps | N/A | 7 Gbps | N/A  
32 | 32 Gbps | N/A | 7 Gbps | N/A  
44 | 32 Gbps | 50 Gbps | 7 Gbps | 25 Gbps  
88 | 62 Gbps | 100 Gbps | 7 Gbps | 25 Gbps  
176 | 100 Gbps | 200 Gbps | 7 Gbps | 25 Gbps  
192 | 100 Gbps | 200 Gbps | 7 Gbps | 25 Gbps  
  
### Storage-optimized Z4D VMs and bare metal instances

The following table describes the egress bandwidth limits for Z4D instances.

**Note:** Z4D instances achieve these bandwidth limits automatically under standard networking. Tier_1 networking isn't available on Z4D instances.**Note:** If you are using a Z4D bare metal instance, you can maximize network bandwidth performance by disabling sleep states. For more information, see the [troubleshooting documentation](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-performance#bare_metal_instances).vCPUs | Internal IP | External IP | Number of physical NICs  
---|---|---|---  
8 or 16 | 20 Gbps | 7 Gbps | 1  
32 | 32 Gbps | 7 Gbps | 1  
48 | 50 Gbps | 25 Gbps | 1  
64 | 65 Gbps | 25 Gbps | 1  
96 | 100 Gbps | 25 Gbps | 1  
192 | 200 Gbps | 25 Gbps | 1  
384 | 400 Gbps | 50 Gbps | 2  
  
### Storage-optimized Z4M VMs

The following table describes the egress bandwidth limits for Z4M instances.

**Note:** Z4M instances achieve these bandwidth limits automatically under standard networking. Tier_1 networking isn't available on Z4M instances.vCPUs | Internal IP | External IP | Number of physical NICs  
---|---|---|---  
16 | 32 Gbps | 7 Gbps | 1  
32 | 67 Gbps | 7 Gbps | 1  
48 | 100 Gbps | 25 Gbps | 1  
192 | 400 Gbps | 50 Gbps | 2  
  
## Configure an instance with Tier_1 networking

You can enable Tier_1 networking when creating a compute instance if the instance doesn't use the VirtioNet interface. You can also edit an instance to add or remove Tier_1 networking, provided the instance was created with the gVNIC or IDPF network interface .

Optionally, you can also [enable faster network packet processing with DPDK](https://docs.cloud.google.com/compute/docs/networking/use-dpdk) to run performance-intensive applications on an instance that uses Tier_1 networking.

### Create instances and containers that use Tier_1 networking

Use the Google Cloud console, the Google Cloud CLI or REST to add Tier_1 networking to a new compute instance or [container](https://docs.cloud.google.com/compute/docs/containers).

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select your project.

  3. Click **Create instance**.

  4. Specify a **Name** for your compute instance. For more information, see [Resource naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format).

  5. Select a [region and zone](https://docs.cloud.google.com/compute/docs/regions-zones) that supports the machine type you plan to use.

  6. Select a **Machine configuration** for your instance. To create an instance with Tier_1 networking, you must select a supported machine series and type.

     * Click the **General purpose** tab before selecting N2, N2D, C4, C4A, C4D, C3, or C3D from the **Series** drop-down menu.
     * Click the **Compute optimized** tab before selecting C2 or C2D from the **Series** menu.
     * Click the **Memory optimized** tab before selecting M3 from the **Series** menu.
     * Click the **Storage optimized** tab before selecting Z3 from the **Series** menu.

If you get an error that the machine type is not available in the selected region, change the region to one that supports your chosen machine type.

  7. In the **Machine type** menu, choose a machine type that aligns with the bandwidth tier size requirements.

  8. To select a compatible operating system, in the **Boot disk** section, click **Change** , and then select a supported operating system or use the **Custom Images** tab to select a [custom image](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#create-custom-image).

  9. Optional. In the **Firewall** section, choose your firewall rules.

  10. Expand the **Advanced options** section.

  11. Expand the **Networking** section, and then do the following:

     1. In the **Network interface card** menu, select **gVNIC**.

**Note:** The option **-** in the **Network interface card** menu indicates that the NIC type can be either gVNIC or VirtioNet (VirtIO) depending on the [machine type](https://docs.cloud.google.com/compute/docs/machine-resource#machine_type_comparison). For some machine types, only gVNIC is available for the network interface card. If both gVNIC and VirtIO are available for a VM instance, then choose gVNIC instead of using the default NIC type, which is VirtIO.
     2. In the **Network bandwidth** section, select the **Enable per VM Tier_1 networking performance** checkbox.

     3. If the machine type supports multiple NICs or your instance uses IPv6 addresses, then configure your **Network interfaces**.

  12. Click **Create**.




###  gcloud 

Use the [gcloud compute instances create command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) to create an instance with a [gVNIC virtual network driver](https://docs.cloud.google.com/compute/docs/networking/using-gvnic). Use the `--network-performance-configs` flag and the `--network-interface` flag to configure a network performance setting for an instance. If you don't specify these flags the instance is created with the default network performance configuration.

To create an instance running container images, use the [gcloud compute instances create-with-container command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container).
    
    
    gcloud compute instances create INSTANCE_NAME  \
        --image=OS_IMAGE  \
        --machine-type=MACHINE_TYPE  \
        --network-performance-configs=total-egress-bandwidth-tier=TIER_1  \
        --network-interface=nic-type=GVNIC
    

Replace the following: 

  * INSTANCE_NAME: the name of the instance
  * OS_IMAGE: an image that supports [gVNIC image](https://docs.cloud.google.com/compute/docs/images/os-details#networking)
  * MACHINE_TYPE: a machine type that supports a high-bandwidth configuration



For example:
    
    
    gcloud compute instances create instance-1 \
        --network-performance-configs=total-egress-bandwidth-tier=TIER_1 \
        --network-interface=nic-type=GVNIC \
        --image-family=rocky-linux-8-optimized-gcp \
        --image-project=rocky-linux-cloud \
        --machine-type=n2-standard-32
    

###  REST 

Call the Compute Engine API [instances.insert method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert) to create a compute instance with a high-bandwidth network configuration. In the request body, do the following:

  * Set the `networkPerformanceConfig` parameters to `totalEgressBandwidthTier` and `TIER_1`.
  * Set the `networkInterface` parameters to `nicType` and `GVNIC`.


    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    
    {
      "name": "INSTANCE_NAME",
      "networkPerformanceConfig": {
        "totalEgressBandwidthTier": "TIER_1"
      },
      "networkInterfaces": [
        {
          "nicType": "GVNIC"
        }
      ]
    }
    

Replace the following:

  * PROJECT_ID: your project ID
  * ZONE: the zone where you want to create the instance
  * INSTANCE_NAME: the name of the instance



### Update a compute instance to include Tier_1 networking

Refer to the [Updating instance properties](https://docs.cloud.google.com/compute/docs/instances/update-instance-properties#update) documentation to verify that you are meeting all the requirements to successfully update your compute instance. Use the Google Cloud console, the Google Cloud CLI or REST to update an instance.

You can modify an existing instance to change the network configuration to include or exclude per VM Tier_1 networking performance. Your instance must already have a gVNIC interface associated with it; you can't edit your instance to add a network interface. To update the network configuration, you must stop and restart the instance.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select your project.

  3. Click the name of the instance that you want to modify.

  4. Click stop **Stop** to stop the instance. If there is no **Stop** option, click more_vert **More actions >** stop **Stop**.

  5. Click **Edit**.

  6. If your instance was originally configured with a gVNIC card, select the **Enable per VM Tier_1 networking performance** checkbox to add per VM Tier_1 networking performance, or deselect the checkbox to remove this feature from your instance.

  7. **Save** your changes.

  8. **Restart** your instance.




###  gcloud 

  1. Export your instance's information to a YAML file using the [`gcloud compute instances export` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/export).
         
         gcloud compute instances export INSTANCE_NAME \
            --zone=ZONE --destination=PATH_TO_FILE
         

Replace the following: 

     * INSTANCE_NAME: the name of the instance
     * ZONE: the name of the zone where the instance is located
     * PATH_TO_FILE: the relative path to the YAML file

For example:
           
           gcloud compute instances export instance-1 \
                  --zone=europe-west1-c --destination=test-file.yaml
              

  2. Use the [Cloud Shell Editor](https://docs.cloud.google.com/shell/docs/editor-overview), or the editor of your choice to open the YAML file you created.

  3. In the file, locate the configuration section for `networkPerformanceConfig`. Change the setting for `totalEgressBandwidthTier` as shown in the following example:
         
         networkPerformanceConfig:
          totalEgressBandwidthTier: TIER_1
         

Setting `totalEgressBandwidthTier` to `TIER_1` adds Tier_1 networking. Setting it to `DEFAULT` removes the configuration.

**Tip:** To avoid getting an error such as `"ERROR: (gcloud.compute.instances.update-from-file) Cannot parse YAML: [Expected type  for field value, found True (type )]"`, add quotes (`' '`) around any label values of `yes` or `no` in the exported instance configuration file. This indicates the values are strings, not Boolean values.
  4. Use the [`gcloud compute instance update-from-file` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/update-from-file) to update the instance with the changes in the file.
         
         gcloud compute instances update-from-file INSTANCE_NAME \
              --zone=ZONE \
              --source=PATH_TO_FILE \
              --most-disruptive-allowed-action=RESTART
         

Replace the following:

     * `INSTANCE_NAME`: the name of the instance
     * `ZONE`: the name of the zone where the instance is located
     * `PATH_TO_FILE`: your YAML filename

The `--most-disruptive-allowed-action=RESTART` flag setting automatically restarts your instance with the updated configuration.




###  REST 

Call the [instances.update method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/update) to modify the network configuration.
    
    
    PUT https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/RESOURCE_ID?mostDisruptiveAllowedAction=RESTART
    
    {
      "networkPerformanceConfig":{
          "totalEgressBandwidthTier": "TIER_1"
      },
    ...
    }
    

Setting `totalEgressBandwidthTier` to `TIER_1` adds Tier_1 networking. Setting it to `DEFAULT` removes the configuration.

Replace the following:

  * PROJECT_ID: your project ID
  * ZONE: the zone where your instance resides
  * RESOURCE_ID: the name of your instance



The `mostDisruptiveAllowedAction=RESTART` query parameter automatically restarts your instance with the updated configuration.

### Verify high-bandwidth configuration in a compute instance

Use the Google Cloud console, the Google Cloud CLI or REST to generate a description of an existing compute instance, or an existing instance that runs container images, to verify the instances's bandwidth tier.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select your project and click **Continue**.

  3. Click the instance name to see its configuration details and see if the instance uses per VM Tier_1 networking performance.




###  gcloud 

Use the [`gcloud compute instances describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/describe) to check if your instance uses per VM Tier_1 networking performance.

For example:
    
    
    gcloud compute instances describe INSTANCE_NAME  \
        --format="text(name, networkPerformanceConfig)"
    

The output is similar to the following:
    
    
    name: instance-1
    networkPerformanceConfig.totalEgressBandwidthTier:TIER_1
    

If the output shows the value `DEFAULT`, then Tier_1 networking isn't enabled.

###  REST 

Call the [`instances.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/get) to view the network configuration.
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/RESOURCE_ID
    

Replace the following:

  * PROJECT_ID: your project name
  * ZONE: the zone where your instance resides
  * RESOURCE_ID: the name of your instance



The output should contain the following lines:
    
    
    {
      "name": RESOURCE_ID,
        "description": string,
        ...
        "networkPerformanceConfig": {
            "totalEgressBandwidthTier": "TIER_1"
        },
        ...
      }
    

If the output shows the value `DEFAULT`, then Tier_1 networking is not enabled.

### Create an instance template with Tier_1 networking

Use the Google Cloud console, the Google Cloud CLI or REST to create an instance template with per VM Tier_1 networking performance. Refer to the [Creating an instance template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates) documentation to verify that you are meeting all the requirements to create your instance template.

###  Console 

  1. In the Google Cloud console, go to the **Instance templates** page.

[Go to Instance templates](https://console.cloud.google.com/compute/instanceTemplates/list)

  2. Click **Create instance template**.

  3. Enter values for the following fields, or accept the default values.

  4. Specify a **Name** for your instance template. For more information, see [Resource naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format).

  5. Select a [region and zone](https://docs.cloud.google.com/compute/docs/regions-zones) that supports Tier_1 networking.

  6. Select a **Machine configuration** for your compute instance. To create an instance that uses Tier_1 networking, you must select a supported machine series and machine type.

     * Click the **General purpose** tab before selecting N2, N2D, C4, C4A, C4D, C3, or C3D from the **Series** drop-down menu.
     * Click the **Compute optimized** tab before selecting C2 or C2D from the **Series** menu.
     * Click the **Storage optimized** tab before selecting Z3 from the **Series** menu.
  7. In the **Machine type** menu, choose a machine type that aligns with the bandwidth tier size requirements.

  8. In the **Boot disk** section, click **Change** , and then select a gVNIC-compatible or [custom image](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#create-custom-image).

  9. Optional. In the **Firewall** section, choose your firewall rules.

  10. Expand the **Advanced options** section.

  11. Expand the **Networking** section, and then do the following:

     1. In the **Network interface card** menu, select **gVNIC**.

**Note:** The option **-** in the **Network interface card** menu indicates that the NIC type can be either gVNIC or VirtioNet (VirtIO) depending on the [machine family type](https://docs.cloud.google.com/compute/docs/machine-resource#machine_type_comparison). For some machine family types, only gVNIC is available for the network interface card. If both gVNIC and VirtIO are available for the machine type, then choose gVNIC instead of using the default NIC type, which is VirtIO.
     2. In the **Network bandwidth** section, select the **Enable per VM Tier_1 networking performance** checkbox.

     3. If the machine type supports multiple NICs or the instance uses IPv6 addresses, then configure the **Network interfaces** accordingly.

  12. Click **Create**.




###  gcloud 

Use the [`gcloud compute instance-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create) with both the `--network-performance-configs` and the `--network-interface` flags.
    
    
    gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
        --image=OS_IMAGE \
        --machine-type=MACHINE_TYPE \
        --network-performance-configs=total-egress-bandwidth-tier=TIER_1 \
        --network-interface=nic-type=GVNIC
    

Replace the following:

  * INSTANCE_TEMPLATE_NAME: the name of your instance template
  * OS_IMAGE: an operating system image that supports [gVNIC](https://docs.cloud.google.com/compute/docs/images/os-details#networking)
  * MACHINE_TYPE: a machine type that supports Tier_1 networking, as described in Bandwidth tiers.



For example:
    
    
    gcloud compute instance-templates create instance-template-1 \
        --image-family=rocky-linux-8-optimized-gcp \
        --image-project=rocky-linux-cloud \
        --network-performance-configs=total-egress-bandwidth-tier=TIER_1 \
        --machine-type=n2-standard-32 \
        --network-interface=nic-type=GVNIC
    

###  REST 

Call the [`instanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates/insert). Within the request body, set the `networkPerformanceConfig` parameter to `totalEgressBandwidthTier` and `TIER_1`. Set the `networkInterfaces` parameter to `nicType` and `GVNIC`.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/instanceTemplates
    
    {
      "name": "INSTANCE_TEMPLATE_NAME",
      "properties": {
        "machineType": "zones/ZONE/machineTypes/MACHINE_TYPE",
        ...
        "networkPerformanceConfig": {
            "totalEgressBandwidthTier": "TIER_1"
         },
        "networkInterfaces": [
          {
            "nicType": "GVNIC"
          },
        ...
        ]
      }
    }
    

Replace the following:

  * PROJECT_ID: your project name
  * INSTANCE_TEMPLATE_NAME: a name for the instance template
  * ZONE: the zone where your instance is located
  * MACHINE_TYPE: the machine type of the instance
  * RESOURCE_ID: the name of your instance



## Benchmark a higher bandwidth configuration

You can [run a benchmark test](https://docs.cloud.google.com/compute/docs/networking/benchmarking-higher-bandwidth-vms#performing_the_benchmark) to check your compute instances's performance with per VM Tier_1 networking performance. Be sure to [remove the benchmarking resources](https://docs.cloud.google.com/compute/docs/networking/benchmarking-higher-bandwidth-vms#remove-benchmark-vms) that you create during testing when you are finished to avoid unexpected resource charges.

## What's next

  * Review [per VM Tier_1 networking performance pricing](https://cloud.google.com/products/compute/pricing/general-purpose#tier-1-higher-bandwidth-network-pricing)
  * Learn about the [gVNIC network interface driver](https://docs.cloud.google.com/compute/docs/networking/using-gvnic)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
