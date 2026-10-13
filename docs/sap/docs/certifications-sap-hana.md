---
url: https://docs.cloud.google.com/sap/docs/certifications-sap-hana/
title: Certifications for SAP HANA on Google Cloud \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:43:56.311805+00:00
---

# Certifications for SAP HANA on Google Cloud  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/certifications-sap-hana/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Certifications for SAP HANA on Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

SAP certifies a wide range of Google Cloud machine types for use with SAP HANA on Google Cloud. With each machine type, you can have different options for the operating system, CPU platform, block storage, and so forth. SAP also certifies Compute Engine instances for SAP HANA dynamic tiering.

## Certified machine types for SAP HANA

For SAP HANA, SAP certifies only a subset of the machine types that are available from Google Cloud.

From the machine types that SAP certifies for use with SAP HANA, you can choose to create virtual machine (VM) instances or bare metal instances.

Custom configurations of the general-purpose `n1-` and `n2-highmem` machine types are also certified by SAP. For more information, see Certified custom machine types for SAP HANA.

For the operating systems that are certified for use with HANA on each machine type, see Certified operating systems for SAP HANA.

Some machine types are not available in all Google Cloud regions. To check the regional availability of a Compute Engine machine type, see [Available regions & zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).

SAP lists the certified machine types for SAP HANA in the [Certified and supported SAP HANA hardware directory](https://www.sap.com/dmc/exp/2014-09-02-hana-hardware/enEN/#/solutions?filters=iaas;ve:29).

For more information about different Compute Engine machine types and their use cases, see [machine types](https://docs.cloud.google.com/compute/docs/machine-types).

#### Certified Compute Engine machine types for SAP HANA

The following table shows Compute Engine machine types that are certified by SAP for SAP HANA:

**Note:** The prefix in the following machine names changed from "`n1`" to "`m1`" to more clearly identify the machines as members of the memory-optimized machine family: 

  * `n1-megamem-96` is now `**m1** -megamem-96`
  * `n1-ultramem-40` is now `**m1** -ultramem-40`
  * `n1-ultramem-80` is now `**m1** -ultramem-80`
  * `n1-ultramem-160` is now `**m1** -ultramem-160`

The machines themselves did not change and the former names are still supported as aliases for these machines. 

The following table shows all of the Google Cloud machine types that are certified by SAP for production use of SAP HANA.

The table does not include the machine types that SAP certifies for SAP Business One on SAP HANA. For the machine types that SAP certifies for SAP HANA with SAP Business One, see [Certified SAP applications on Google Cloud](https://docs.cloud.google.com/sap/docs/certifications-sap-apps#sap-certified-apps-on-gc).

Machine types | vCPUs | Memory | Operating system | CPU platform | Application type | Notes  
---|---|---|---|---|---|---  
**N1 high-memory, general-purpose machine types**  
`n1-highmem-32` | 32 | 208 GB | RHEL, SUSE  
| Intel Broadwell | OLAP or OLTP | Block storage: Compute Engine Persistent Disk or, for scale up only, Google Cloud NetApp Volumes (the Premium or Extreme service level for the SAP HANA data and log volumes).  
`n1-highmem-64` | 64 | 416 GB | RHEL, SUSE | Intel Broadwell | OLAP or OLTP | Block storage: Compute Engine Persistent Disk or, for scale up only, Google Cloud NetApp Volumes (the Premium or Extreme service level for the SAP HANA data and log volumes).  
`n1-highmem-96` | 96 | 624 GB | RHEL, SUSE | Intel Skylake | OLAP or OLTP | Block storage: Compute Engine Persistent Disk or, for scale up only, Google Cloud NetApp Volumes (the Premium or Extreme service level for the SAP HANA data and log volumes).  
**N2 high-memory, general-purpose machine types**  
`n2-highmem-32` | 32 | 256 GB | RHEL, SUSE | Intel Ice Lake,  
Intel Cascade Lake | OLAP or OLTP | Scale up only.  
Block storage: Compute Engine Persistent Disk or Google Cloud NetApp Volumes (the Premium or Extreme service level for the SAP HANA data and log volumes).   
`n2-highmem-48` | 48 | 384 GB | RHEL, SUSE | Intel Ice Lake,  
Intel Cascade Lake | OLAP or OLTP | Scale up only.  
Block storage: Compute Engine Persistent Disk or Google Cloud NetApp Volumes (the Premium or Extreme service level for the SAP HANA data and log volumes).   
`n2-highmem-64` | 64 | 512 GB | RHEL, SUSE | Intel Ice Lake,  
Intel Cascade Lake | OLAP or OLTP | Scale up only.  
Block storage: Compute Engine Persistent Disk or Google Cloud NetApp Volumes (the Premium or Extreme service level for the SAP HANA data and log volumes).   
`n2-highmem-80` | 80 | 640 GB | RHEL, SUSE | Intel Ice Lake,  
Intel Cascade Lake | OLAP or OLTP | Scale up only.  
Block storage: Compute Engine Persistent Disk, Hyperdisk Extreme, or Google Cloud NetApp Volumes (the Premium or Extreme service level for the SAP HANA data and log volumes).   
`n2-highmem-96` | 96 | 768 GB | RHEL, SUSE | Intel Ice Lake | OLAP or OLTP | Scale up only.  
Block storage: Compute Engine Persistent Disk, Hyperdisk Extreme, or Google Cloud NetApp Volumes (the Premium or Extreme service level for the SAP HANA data and log volumes).   
`n2-highmem-128` | 128 | 864 GB | RHEL, SUSE | Intel Ice Lake | OLAP or OLTP | Scale up only.  
Block storage: Compute Engine Persistent Disk, Hyperdisk Extreme, or Google Cloud NetApp Volumes (the Premium or Extreme service level for the SAP HANA data and log volumes).   
**C3 general-purpose machine types**  
`c3-standard-44` | 44 | 176 GB | RHEL, SUSE | Intel Sapphire Rapids | OLAP or OLTP | Scale up only.  
Block storage: Compute Engine Persistent Disk, Hyperdisk Balanced, or Google Cloud NetApp Volumes (the Premium or Extreme service level for the SAP HANA data and log volumes).   
`c3-highmem-44` | 44 | 352 GB | RHEL, SUSE | Intel Sapphire Rapids | OLAP or OLTP | Scale up only.  
Block storage: Compute Engine Persistent Disk, Hyperdisk Balanced, or Google Cloud NetApp Volumes (the Premium or Extreme service level for the SAP HANA data and log volumes).   
`c3-highmem-88` | 88 | 704 GB | RHEL, SUSE | Intel Sapphire Rapids | OLAP or OLTP | Scale up only.  
Block storage: Compute Engine Persistent Disk, Hyperdisk Extreme, Hyperdisk Balanced, or Google Cloud NetApp Volumes (the Premium or Extreme service level for the SAP HANA data and log volumes).   
`c3-highmem-176` | 176 | 1,408 GB | RHEL, SUSE | Intel Sapphire Rapids | OLAP or OLTP | Scale up only.  
Block storage: Compute Engine Persistent Disk, Hyperdisk Extreme, Hyperdisk Balanced, or Google Cloud NetApp Volumes (the Premium or Extreme service level for the SAP HANA data and log volumes).   
**C3 general-purpose bare metal machine types**  
`c3-highmem-192-metal` | 192 | 1,536 GB | RHEL, SUSE | Intel Sapphire Rapids | OLAP or OLTP | Scale up only.  
Block storage: Hyperdisk Extreme, Hyperdisk Balanced.   
**C4 general-purpose machine types**  
`c4-highmem-32` | 32 | 248 GB | RHEL, SUSE | Intel Emerald Rapids | OLAP or OLTP | Scale up only.  
Block storage: Hyperdisk Balanced or Google Cloud NetApp Volumes (the Premium or Extreme service level for the SAP HANA data and log volumes).  
`c4-highmem-48` | 48 | 372 GB | RHEL, SUSE | Intel Emerald Rapids | OLAP or OLTP | Scale up only.  
Block storage: Hyperdisk Balanced or Google Cloud NetApp Volumes (the Premium or Extreme service level for the SAP HANA data and log volumes).  
`c4-highmem-96` | 96 | 744 GB | RHEL, SUSE | Intel Emerald Rapids | OLAP or OLTP | Scale up only.  
Block storage: Hyperdisk Extreme, Hyperdisk Balanced, or Google Cloud NetApp Volumes (the Premium or Extreme service level for the SAP HANA data and log volumes).  
`c4-highmem-144` | 144 | 1,116 GB | RHEL, SUSE | Intel Granite Rapids | OLAP or OLTP | Scale up only.  
Block storage: Hyperdisk Extreme or Hyperdisk Balanced  
`c4-highmem-192` | 192 | 1,488 GB | RHEL, SUSE | Intel Emerald Rapids | OLAP or OLTP | Scale up only.  
Block storage: Hyperdisk Extreme, Hyperdisk Balanced, or Google Cloud NetApp Volumes (the Premium or Extreme service level for the SAP HANA data and log volumes).  
`c4-highmem-288` | 288 | 2,232 GB | RHEL, SUSE | Intel Granite Rapids | OLAP or OLTP | Scale up only.  
Block storage: Hyperdisk Extreme or Hyperdisk Balanced  
`c4-highmem-288-metal` | 288 | 2,232 GB | RHEL, SUSE | Intel Granite Rapids | OLAP or OLTP | Scale up only.  
Block storage: Hyperdisk Extreme or Hyperdisk Balanced  
**M1 memory-optimized machine types**  
`m1-megamem-96` | 96 | 1,433 GB | RHEL, SUSE | Intel Skylake | OLAP or OLTP | OLAP: scale up, and scale out up to 16 nodes.  
OLTP: scale up only.  
Block storage: Compute Engine Persistent Disk, Hyperdisk Extreme, Hyperdisk Balanced, or, for OLTP scale up only, Google Cloud NetApp Volumes (the Premium or Extreme service level for the SAP HANA data and log volumes).  
`m1-ultramem-40` | 40 | 961 GB | RHEL, SUSE | Intel Broadwell | OLTP only | Scale up only.  
Block storage: Compute Engine Persistent Disk, Hyperdisk Balanced, or Google Cloud NetApp Volumes (the Premium or Extreme service level for the SAP HANA data and log volumes).   
`m1-ultramem-80` | 80 | 1,922 GB | RHEL, SUSE | Intel Broadwell | OLTP only | Scale up only.  
Block storage: Compute Engine Persistent Disk, Hyperdisk Extreme, Hyperdisk Balanced, or Google Cloud NetApp Volumes (the Premium or Extreme service level for the SAP HANA data and log volumes).   
`m1-ultramem-160` | 160 | 3,844 GB | RHEL, SUSE | Intel Broadwell | OLAP or OLTP | 2 TB OLAP workloads certified for scale up and scale out up to 16 nodes. Up to 4 TB OLAP workloads supported with workload based sizing.  
OLTP workloads certified for scale up only.  
Block storage: Compute Engine Persistent Disk, Hyperdisk Extreme, Hyperdisk Balanced, or, for OLTP scale up only, Google Cloud NetApp Volumes (the Premium or Extreme service level for the SAP HANA data and log volumes).  
**M2 memory-optimized machine types**  
`m2-megamem-416` | 416 | 5,888 GB | RHEL, SUSE | Intel Cascade Lake | OLAP or OLTP | OLAP workloads certified for scale up and scale out up to 16 nodes.  
OLTP workloads are certified for scale up, and scale out up to 4 nodes.  
Certification for OLTP scale out includes SAP S/4HANA.  
For scale out with S/4HANA, see [SAP Note 2408419](https://launchpad.support.sap.com/#/notes/2408419).  
Block storage: Compute Engine Persistent Disk, Hyperdisk Extreme, Hyperdisk Balanced, or, for scale up only, [Google Cloud NetApp Volumes (the Premium or Extreme service level for the SAP HANA data and log volumes)](https://docs.cloud.google.com/sap/docs/certifications-sap-hana#gc_netapp_volumes).  
  
`m2-ultramem-208` | 208 | 5,888 GB | RHEL, SUSE | Intel Cascade Lake | OLTP only | Scale up only.  
Block storage: Compute Engine Persistent Disk, Hyperdisk Extreme, Hyperdisk Balanced, or Google Cloud NetApp Volumes (the Premium or Extreme service level for the SAP HANA data and log volumes).   
`m2-ultramem-416` | 416 | 11,776 GB | RHEL, SUSE | Intel Cascade Lake-SP | OLAP or OLTP | OLAP workloads are certified with workload-based sizing for scale up, and scale out up to 16 nodes.  
OLTP workloads are certified for scale up, and scale out up to 4 nodes.  
Certification for OLTP scale out includes SAP S/4HANA.  
Block storage: Compute Engine Persistent Disk, Hyperdisk Extreme, Hyperdisk Balanced, or, for scale up only, Google Cloud NetApp Volumes (the Premium or Extreme service level for the SAP HANA data and log volumes).  
For scale out with S/4HANA, see [SAP Note 2408419](https://launchpad.support.sap.com/#/notes/2408419).  
`m2-hypermem-416` | 416 | 8,832 GB | RHEL, SUSE | Intel Cascade Lake | OLAP or OLTP | OLAP workloads certified for scale up in single node.  
OLTP workloads are certified for scale up, and scale out up to 4 nodes.   
Certification for OLTP scale out includes SAP S/4HANA.  
Block storage: Compute Engine Persistent Disk, Hyperdisk Extreme, Hyperdisk Balanced, or, for scale up only, Google Cloud NetApp Volumes (the Premium or Extreme service level for the SAP HANA data and log volumes).  
For scale out with S/4HANA, see [SAP Note 2408419](https://launchpad.support.sap.com/#/notes/2408419).  
**M3 memory-optimized machine types**  
`m3-ultramem-32` | 32 | 976 GB | RHEL, SUSE | Intel Ice Lake | OLTP only | Scale up only.  
Block storage: Compute Engine Persistent Disk, Hyperdisk Balanced, or Google Cloud NetApp Volumes (the Premium or Extreme service level for the SAP HANA data and log volumes).  
`m3-ultramem-64` | 64 | 1,952 GB | RHEL, SUSE | Intel Ice Lake | OLTP only | Scale up only.  
Block storage: Compute Engine Persistent Disk, Hyperdisk Extreme, Hyperdisk Balanced, or Google Cloud NetApp Volumes (the Premium or Extreme service level for the SAP HANA data and log volumes).  
`m3-ultramem-128` | 128 | 3,904 GB | RHEL, SUSE | Intel Ice Lake | OLAP or OLTP | OLAP workloads are certified with workload-based sizing for scale-up, and scale-out up to 8 nodes. OLTP workloads are certified for scale up. Block storage: Compute Engine Persistent Disk, Hyperdisk Extreme, Hyperdisk Balanced, or Google Cloud NetApp Volumes (the Premium or Extreme service level for the SAP HANA data and log volumes).  
`m3-megamem-64` | 64 | 976 GB | RHEL, SUSE | Intel Ice Lake | OLAP or OLTP | Scale up only.  
Block storage: Compute Engine Persistent Disk, Hyperdisk Extreme, Hyperdisk Balanced, or Google Cloud NetApp Volumes (the Premium or Extreme service level for the SAP HANA data and log volumes).  
`m3-megamem-128` | 128 | 1,952 GB | RHEL, SUSE | Intel Ice Lake | OLAP or OLTP | Scale up, and scale out up to 16 nodes.  
Block storage: Compute Engine Persistent Disk, Hyperdisk Extreme, Hyperdisk Balanced, or Google Cloud NetApp Volumes (the Premium or Extreme service level for the SAP HANA data and log volumes) (scale-up only).  
**M4 memory-optimized machine types**  
`m4-megamem-28` | 28 | 372 GB | RHEL, SUSE | Intel Emerald Rapids | OLAP or OLTP | Scale up only.  
Block storage: Hyperdisk Balanced.  
`m4-megamem-56` | 56 | 744 GB | RHEL, SUSE | Intel Emerald Rapids | OLAP or OLTP | Scale up only.  
Block storage: Hyperdisk Balanced.  
`m4-megamem-112` | 112 | 1,488 GB | RHEL, SUSE | Intel Emerald Rapids | OLAP or OLTP | Scale up only.  
Block storage: Hyperdisk Extreme, Hyperdisk Balanced.  
`m4-megamem-224` | 224 | 2,976 GB | RHEL, SUSE | Intel Emerald Rapids | OLAP or OLTP | Scale up, or scale-out up to 8 nodes  
Block storage: Hyperdisk Extreme, Hyperdisk Balanced.  
`m4-ultramem-56` | 56 | 1,488 GB | RHEL, SUSE | Intel Emerald Rapids | OLAP or OLTP | Scale up only.  
OLAP workloads are certified with workload-based sizing.  
Block storage: Hyperdisk Balanced.  
`m4-ultramem-112` | 112 | 2,976 GB | RHEL, SUSE | Intel Emerald Rapids | OLAP or OLTP | Scale up only.  
OLAP workloads are certified with workload-based sizing.  
Block storage: Hyperdisk Extreme, Hyperdisk Balanced.  
`m4-ultramem-224` | 224 | 5,952 GB | RHEL, SUSE | Intel Emerald Rapids | OLAP or OLTP | Scale up only.  
OLAP workloads are certified with workload-based sizing.  
Block storage: Hyperdisk Extreme, Hyperdisk Balanced.  
`m4-hypermem-16` | 16 | 248 GB | RHEL, SUSE | Intel Emerald Rapids | OLAP or OLTP | Scale up only.  
Block storage: Hyperdisk Balanced.  
`m4-hypermem-32` | 32 | 496 GB | RHEL, SUSE | Intel Emerald Rapids | OLAP or OLTP | Scale up only.  
Block storage: Hyperdisk Balanced.  
`m4-hypermem-64` | 64 | 992 GB | RHEL, SUSE | Intel Emerald Rapids | OLAP or OLTP | OLAP workloads are certified with workload-based sizing for scale-up and scale-out up to 8 nodes. OLTP workloads are certified for scale up. Block storage: Hyperdisk Balanced.  
**M4N memory-optimized machine types**  
`m4n-megamem-28` | 28 | 372 GB | RHEL, SUSE | Intel Emerald Rapids | OLAP or OLTP | Scale up only.  
Block storage: Hyperdisk Balanced, Hyperdisk Extreme.  
`m4n-megamem-56` | 56 | 744 GB | RHEL, SUSE | Intel Emerald Rapids | OLAP or OLTP | Scale up only.  
Block storage: Hyperdisk Balanced, Hyperdisk Extreme.  
`m4n-megamem-112` | 112 | 1,488 GB | RHEL, SUSE | Intel Emerald Rapids | OLAP or OLTP | Scale up only.  
Block storage: Hyperdisk Extreme, Hyperdisk Balanced.  
`m4n-megamem-224` | 224 | 2,976 GB | RHEL, SUSE | Intel Emerald Rapids | OLAP or OLTP | Scale up, or scale-out up to 8 nodes  
Block storage: Hyperdisk Extreme, Hyperdisk Balanced.  
`m4n-ultramem-56` | 56 | 1,488 GB | RHEL, SUSE | Intel Emerald Rapids | OLAP or OLTP | Scale up only.  
OLAP workloads are certified with workload-based sizing.  
Block storage: Hyperdisk Balanced.  
`m4n-ultramem-112` | 112 | 2,976 GB | RHEL, SUSE | Intel Emerald Rapids | OLAP or OLTP | Scale up only.  
OLAP workloads are certified with workload-based sizing.  
Block storage: Hyperdisk Extreme, Hyperdisk Balanced.  
`m4n-ultramem-224` | 224 | 5,952 GB | RHEL, SUSE | Intel Emerald Rapids | OLAP or OLTP | Scale up only.  
OLAP workloads are certified with workload-based sizing.  
Block storage: Hyperdisk Extreme, Hyperdisk Balanced.  
`m4n-hypermem-16` | 16 | 248 GB | RHEL, SUSE | Intel Emerald Rapids | OLAP or OLTP | Scale up only.  
Block storage: Hyperdisk Balanced, Hyperdisk Extreme.  
`m4n-hypermem-32` | 32 | 496 GB | RHEL, SUSE | Intel Emerald Rapids | OLAP or OLTP | Scale up only.  
Block storage: Hyperdisk Balanced, Hyperdisk Extreme.  
`m4n-hypermem-64` | 64 | 992 GB | RHEL, SUSE | Intel Emerald Rapids | OLAP or OLTP | OLAP workloads are certified with workload-based sizing for scale-up and scale-out up to 8 nodes. OLTP workloads are certified for scale up. Block storage: Hyperdisk Balanced, Hyperdisk Extreme.  
**X4 memory-optimized bare metal machine types** **Note** : From December 12, 2025, the naming convention for X4 machine types has changed to clarify the memory they offer. For example, `x4-megamem-960-metal` has changed to `x4-960-16t-metal` because it offers 16 TB of memory. While this naming change is backwards compatible, we recommend that you use the updated names for new deployments.  
`x4-480-6t-metal` | 480 | 6,144 GB | RHEL, SUSE | Intel Sapphire Rapids | OLAP or OLTP |  OLAP workloads are certified with workload-based sizing for scale-up and scale-out up to 8 nodes. OLTP workloads are certified for scale up. Block storage: Hyperdisk Extreme, Hyperdisk Balanced  
`x4-480-8t-metal` | 480 | 8,192 GB | RHEL, SUSE | Intel Sapphire Rapids | OLAP or OLTP |  OLAP workloads are certified with workload-based sizing for scale-up and scale-out up to 8 nodes. OLTP workloads are certified for scale-up and scale-out up to 4 nodes. Block storage: Hyperdisk Extreme, Hyperdisk Balanced  
`x4-960-12t-metal` | 960 | 12,288 GB | RHEL, SUSE | Intel Sapphire Rapids | OLAP or OLTP |  OLAP workloads are certified with workload-based sizing for scale-up and scale-out up to 8 nodes. OLTP workloads are certified for scale-up, and scale-out up to 4 nodes. Block storage: Hyperdisk Extreme, Hyperdisk Balanced  
`x4-960-16t-metal` | 960 | 16,384 GB | RHEL, SUSE | Intel Sapphire Rapids | OLAP or OLTP |  OLTP workloads are certified for scale out up to 4 nodes, and scale up. OLAP workloads are certified for scale out up to 8 nodes, and scale up. Block storage: Hyperdisk Extreme, Hyperdisk Balanced  
`x4-1440-24t-metal` | 1,440 | 24,576 GB | RHEL, SUSE | Intel Sapphire Rapids | OLAP or OLTP |  OLTP workloads are certified for scale out up to 4 nodes, and scale up. OLAP workloads are certified for scale out up to 8 nodes, and scale up. Block storage: Hyperdisk Extreme, Hyperdisk Balanced  
`x4-1920-32t-metal` | 1,920 | 32,768 GB | RHEL, SUSE | Intel Sapphire Rapids | OLAP or OLTP |  OLTP workloads are certified for scale out up to 4 nodes, and scale up. OLAP workloads are certified for scale out up to 8 nodes, and scale up. Block storage: Hyperdisk Extreme, Hyperdisk Balanced  
**X5 memory-optimized bare metal machine types**  
`x5-688-12T-metal` | 688 | 12,288 GB | RHEL, SUSE | Intel Granite Rapids | OLAP or OLTP | Scale-up only. Block storage: Hyperdisk Extreme, Hyperdisk Balanced  
`x5-688-16T-metal` | 688 | 16,384 GB | RHEL, SUSE | Intel Granite Rapids | OLAP or OLTP | Scale-up only. Block storage: Hyperdisk Extreme, Hyperdisk Balanced  
`x5-1376-24T-metal` | 1,376 | 24,576 GB | RHEL, SUSE | Intel Granite Rapids | OLAP or OLTP | Scale-up only. Block storage: Hyperdisk Extreme, Hyperdisk Balanced  
`x5-1376-32T-metal` | 1,376 | 32,768 GB | RHEL, SUSE | Intel Granite Rapids | OLAP or OLTP | Scale-up only. Block storage: Hyperdisk Extreme, Hyperdisk Balanced  
`x5-2064-48T-metal` Note | 2,064 | 49,152 GB | RHEL, SUSE | Intel Granite Rapids | OLAP or OLTP | Scale-up only. Block storage: Hyperdisk Extreme, Hyperdisk Balanced  
  
**Note:** The `x5-2064-48T-metal` machine type is available for use with SAP workloads that SAP manages under the RISE with SAP program. 

### Certified custom machine types for SAP HANA

The following table shows the Compute Engine custom machine types that are certified by SAP for production use of SAP HANA on Google Cloud.

SAP certifies only a subset of the custom machine types that are available from Compute Engine.

Custom machine types are subject to customization rules that are defined by Compute Engine. The rules differ depending on which machine type you are customizing. For complete customization rules, see [Create a VM with a custom machine type](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type).

Base machine type | vCPUs | Memory (GB) | Operating system | CPU platforms  
---|---|---|---|---  
`n1-highmem` | A number of vCPUs from 32 to 64 that is evenly divisible by 2. | 6.5 GB for each vCPU | RHEL, SUSE | Intel Broadwell  
`n2-highmem` (Scale up only) | On Intel Ice Lake, a number of vCPUs from 32 to 80 that is evenly divisible by 4.  
On Intel Cascade Lake, a number of vCPUs from 32 to 80 that is evenly divisible by 4. | Up to 8 GB per vCPU | RHEL, SUSE | Intel Ice Lake,  
Intel Cascade Lake  
  
If the custom machine types that are available from Compute Engine don't meet the memory requirements of your SAP HANA system, then additional options are available through partners that provide managed services. To find a partner that offers managed services for SAP HANA, contact [Google Cloud sales](https://cloud.google.com/contact/?form=SAP).

## Certified operating systems for SAP HANA

The following table shows the Red Hat Enterprise Linux (RHEL) and SUSE Linux Enterprise Server (SLES) operating systems that are certified by SAP for production use with SAP HANA on Google Cloud.

Except where noted in the table, each operating system is supported with SAP HANA on all certified Compute Engine machine types.

For information about the current support status of each operating system and which operating systems are available from Google Cloud, see [Operating system support for SAP HANA on Google Cloud](https://docs.cloud.google.com/sap/docs/sap-hana-os-support).

For information from SAP about which operating systems SAP supports with SAP HANA on Google Cloud, go to [Certified and supported SAP HANA hardware directory](https://www.sap.com/dmc/exp/2014-09-02-hana-hardware/enEN/#/solutions?filters=iaas;ve:29), click the required machine type, and then see **Operating System**.

For SLES 15 SP5 and earlier, SAP HANA table load performance can be slower because of a Linux kernel limitation that is optimized in SLES 15 SP6 and later. For more information, see the SUSE knowledge base article [High system CPU during HANA table load in SUSE Linux Enterprise 15 SP5 and earlier](https://support.scc.suse.com/s/kb/High-system-CPU-during-HANA-table-load-in-SUSE-Linux-Enterprise-15-SP5-and-earlier?language=en_US).

The following table doesn't include the following:

  * Certified operating system versions that are no longer in mainstream support.
  * Operating system versions that are not specific to SAP.

Operating system | Version | Supported SAP-certified machine types for use with SAP HANA | Minimum kernel version  
---|---|---|---  
**RHEL for SAP** | 10.0 |  All  | `6.12.0-55.73.1.el10_0.x86_64` for all SAP-certified machine types  
9.6 Note |  All except X5  | `5.14.0-570.16.1.el9_6`, for X4, C3-metal, and C4-metal  
9.4 Note |  All except X5  | `5.14.0-427.70.1.el9_4`, for X4, C3-metal, and C4-metal  
9.2 Note |  All except X4, X5, C3-metal, C4-metal  | N/A  
9.0 Note |  All except X4, X5, C3-metal, C4-metal  | N/A  
8.10 |  All except X5  | `4.18.0-553.58.1.el8_10`, for X4, C3-metal, and C4-metal  
8.8 |  All except X4, X5, C3-metal, C4-metal  | N/A  
8.6 |  All except X4, X5, C3-metal, C4-metal  | N/A  
8.4 |  All except X4, X5, C3-metal, M4, C4-metal  | N/A  
8.2 |  All except X4, X5, C3-metal, M4, C4-metal  | N/A  
8.1 |  All except X4, X5, C3, M3, M4, C4-metal  | N/A  
7.9 |  All except C4, X4, X5, C3-metal, M4  | N/A  
**SLES for SAP** | 16 | All | `6.12.0-16000.35.1`, for X4, X5, C3-metal, and C4-metal  
15 SP7 | All | `6.4.0-150700.53.3`, for X4, X5, C3-metal, and C4-metal  
15 SP6 | All except X5 | `6.4.0-150600.23.38.1`, for X4, C3-metal, and C4-metal  
15 SP5 | All except X5 | `5.14.21-150500.55.94.1`, for X4, C3-metal, and C4-metal  
15 SP4 | All except X5 | `5.14.21-150400.24.161.1`, for X4, C3-metal, and C4-metal  
15 SP3 |  All except X4, X5, C3-metal, C4-metal  | N/A  
15 SP2 |  All except X4, X5, C3-metal, M4, C4-metal  | N/A  
12 SP5 |  All except X4, X5, C3-metal, C4-metal  | N/A  
**Note:** Before you install any SAP software on RHEL for SAP 9.x, additional packages must be installed on your host machines, especially `chkconfig` and `compat-openssl11`. If you use an image provided by Compute Engine, then these packages are automatically installed for you. For more information from SAP, see the SAP note [3108316 - Red Hat Enterprise Linux 9.x: Installation and Configuration](https://me.sap.com/notes/3108316). 

## Persistent disk storage for SAP HANA

For persistent block storage, you can attach Persistent Disk or Hyperdisk volumes when you create your compute instances or add them to your compute instances later. 

### Supported disk types

Compute Engine offers different Persistent Disk and Hyperdisk types based on either [solid-state drive (SSD)](https://en.wikipedia.org/wiki/Solid-state_drive) technology or [standard hard disk drive (HDD)](https://en.wikipedia.org/wiki/Hard_disk_drive) technology. Each type has different performance characteristics. Google Cloud manages the underlying hardware of the disks to ensure data redundancy and to optimize performance.

For performance reasons, the SAP HANA `/hana/data` and `/hana/log` volumes require SSD-based persistent storage disks. SSD-based Hyperdisk and Persistent Disk types that are certified by SAP for use with SAP HANA include the following:

  * **Hyperdisk types** : Hyperdisk Extreme (`hyperdisk-extreme`) and Hyperdisk Balanced (`hyperdisk-balanced`)

    * Hyperdisk Extreme provides higher maximum IOPS and throughput options than SSD-based Persistent Disk types.
    * For a list of the machine types that support Hyperdisk Extreme and Hyperdisk Balanced, see [Machine type support](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#machine_type_support).
    * On Compute Engine bare metal instances such as X4, use Hyperdisk Balanced as the recommended disk for hosting the following volumes: 
      * The boot volume.
      * The `/usr/sap` volume.
      * The `/hana/shared` volume, if you're hosting it on its own disk.
      * The `/hanabackup` volume, if you're saving your backups on a disk.
    * For Hyperdisk Extreme, you select the performance you need by provisioning IOPS, which also determines your throughput. For more information, see [Size and performance limits for Hyperdisk Extreme](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-extreme#size_limits).
    * For Hyperdisk Balanced, you select the performance you need by provisioning IOPS and throughput. For more information, see [Size and performance limits for Hyperdisk Balanced](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced#size_limits).
    * You can use Hyperdisk Extreme for the `/hana/data` and `/hana/log` volumes when you require the highest performance.
    * To enable the best performance from Hyperdisk Extreme for SAP HANA, update your SAP HANA system properties as recommended in [Hyperdisk performance](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#hyperdisk_performance).
  * **Persistent Disk types** : Legacy machine types support Persistent Disk types. Google Cloud recommends that you use the latest machine types and Hyperdisk volumes for running performant SAP HANA workloads.

#### Click to expand and view information about supported Persistent Disk types

    * Supported Persistent Disk types include the following: Balanced (`pd-balanced`), Performance or SSD (`pd-ssd`), and Extreme (`pd-extreme`).
    * These disk types provide cost-effective and reliable block storage.
    * Performance (SSD) Persistent Disk (`pd-ssd`) provides higher performance than Balanced Persistent Disk (`pd-balanced`).
    * Use Balanced Persistent Disk as the recommended disk for hosting the following volumes: 
      * Boot volume of the compute instance.
      * The `/usr/sap` volume.
      * The `/hana/shared` volume, if you're hosting it on its own disk.
      * The `/hanabackup` volume, if you save your backups to a disk. If you want to reduce the backup costs, then you can use a Standard HDD Persistent Disk (`pd-standard`). Balanced Persistent Disk provides faster backups than Standard HDD Persistent Disk. While selecting the disk, make sure that your machine type supports the disk type.
    * Balanced and Performance (SSD) Persistent Disk support PD Async Replication. You can use this feature for cross-region active-passive disaster recovery. For more information, see [Disaster recovery using PD Async Replication](https://docs.cloud.google.com/sap/docs/sap-hana-dr-planning-guide#dr_using_pd_async_replication).
    * While Extreme Persistent Disk (`pd-extreme`) is certified for use with SAP HANA, we recommend that you instead use Hyperdisk Extreme (`hyperdisk-extreme`), which provides greater performance. If you want to use Extreme Persistent Disk, then make sure to provision the disks in accordance with the information in Minimum sizes for SSD-based Persistent Disk and Hyperdisk volumes.
    * For information about Persistent Disk performance, see [Persistent Disk performance overview](https://docs.cloud.google.com/compute/docs/disks/performance) and [Optimize Persistent Disk performance](https://docs.cloud.google.com/compute/docs/disks/optimizing-pd-performance#performance_factors)


For more information about persistent disk storage for SAP HANA on Google Cloud, see [Persistent disk storage](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#persistent_disk_storage). For more information about Hyperdisk types, their performance characteristics, and how to work with them, see the following documentation: 

  * [Storage options](https://docs.cloud.google.com/compute/docs/disks)
  * [About Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks)
  * [Hyperdisk performance](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-performance)
  * [Hyperdisk performance limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits)
  * [Attach a non-boot disk to a VM](https://docs.cloud.google.com/compute/docs/disks/attach-disks)
  * [Create and manage disk snapshots](https://docs.cloud.google.com/compute/docs/disks/create-snapshots)
  * [Migrate SAP HANA Persistent Disk volumes to Hyperdisk volumes](https://docs.cloud.google.com/sap/docs/migrate-hana-pd-to-hyperdisk)



### Minimum sizes and performance for Persistent Disk and Hyperdisk volumes

When you size certain Compute Engine SSD-based Persistent Disk or Hyperdisk volumes for SAP HANA, you need to account for not only the storage requirements of your SAP HANA instance, but also for the performance of the disk.

The performance of Hyperdisk is not affected by disk size. Its performance is determined by the IOPS or throughput that you provision. For information about the performance of Hyperdisk for SAP HANA workloads, see [Hyperdisk performance](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#hyperdisk_performance).

For information about Persistent Disk based storage configurations for SAP HANA, see Disk sizes for legacy machine and disk types.

Use the following widget to view Hyperdisk based storage configurations for SAP-certified machine types that support usage of Hyperdisk Balanced. Choose the configuration that best fits your needs. The following disk configurations are intended for scale-up systems. For scale-out systems, all disk calculations remain the same except for `/hana/shared`, which is subject to the number of worker nodes you deploy. For every four worker hosts, increase the disk size by 1 x memory, or 1 TB, whichever is smaller.

  * The widget presents the following configurations: **Simple** , **Advanced** , and **Performance**. All of these configurations are designed to help you meet the SAP HANA minimum storage and performance requirements.
  * These configurations differ in the following aspects: performance, deployment complexity, and cost.
  * **Simple** and **Advanced** cost nearly the same, with **Advanced** offering better performance because it uses striped disks to host the `/hana/data` volume. However, using striped disks adds to the complexity of your deployment and maintenance operations.
  * **Performance** is a disk configuration that helps you provision maximum performance without the complexity of maintaining striped disks. This is achieved by provisioning disks with high IOPS and throughput. Consequently, this configuration is the costliest in most cases.
  * The number of disks shown in the **Advanced** disk configuration is the minimum number of disks required to help you achieve a performant disk configuration. While you can add more disks to achieve the required performance, doing so increases the costs you incur.

**Note:** The following storage configurations are only initial recommendations. We strongly recommend that you size your workloads and perform validations to help ensure optimal performance.

#### Disk sizes for legacy machine and disk types

Within limits, the performance of an SSD or Balanced Persistent Disk volume increases as the size of the disk and the number of vCPUs increase. If an SSD or Balanced Persistent Disk volume is too small, then it might not provide the performance that SAP HANA requires.

A 550 GB SSD or a 943 GB Balanced Persistent Disk volume provides a sustained throughput of 400 MB per second for reads and writes, which is the minimum. For general information about Persistent Disk performance, see [Persistent Disk performance overview](https://docs.cloud.google.com/compute/docs/disks/performance).

The following table shows the minimum recommended sizes for SSD Persistent Disk (`pd-ssd`) and Balanced Persistent Disk (`pd-balanced`) to meet SAP HANA performance requirements in a production environment for each Compute Engine machine type that is certified for use with SAP HANA.

The sizes in the following table assume that you are using a separate disk for each of the following volumes: `/hana/data`, `/hana/log`, `/hana/shared`, and `/usr/sap` volumes. This table shows disk sizes for SAP-certified machine types that support using only Persistent Disk. For information about disk configuration for SAP-certified machine types that can use Hyperdisk, see Minimum sizes for SSD-based Persistent Disk and Hyperdisk volumes.

### Balanced Persistent Disk

If you want to use more than one Balanced Persistent Disk volume to host your `/hana/data` volume, then make sure to equally divide the size value given in the "`/hana/data` size (GB)" column among the disk volumes that you provision.

Compute Engine machine type |  `/hana/data` size (GB)  |  `/hana/log` size (GB) | `/hana/shared` size (GB) | `/usr/sap` size (GB) | Total size (GB) | `n1-highmem-32` |  599  | 104 | 208 | 32 |  943   
---|---|---|---|---|---  
`n1-highmem-64` | 499 | 208 | 416 | 32 | 1,155  
`n1-highmem-96` | 748 | 312 | 624 | 32 | 1,716  
`n2-highmem-32` |  527  | 128 | 256 | 32 |  943   
`n2-highmem-48` | 460 | 192 | 384 | 32 | 1,068  
`n2-highmem-64` | 614 | 256 | 512 | 32 | 1,414  
`n2-highmem-80` | 768 | 320 | 640 | 32 | 1,760  
`n2-highmem-96` | 921 | 384 | 768 | 32 | 2,105  
`n2-highmem-128` | 1,036 | 432 | 864 | 32 | 2,364  
  
### SSD Persistent Disk

If you want to use more than one SSD Persistent Disk volume to host your `/hana/data` volume, then make sure to equally divide the size value provided in the "`/hana/data` size (GB)" column among the disk volumes that you provision.

Compute Engine machine type |  `/hana/data` size (GB)  |  `/hana/log` size (GB) | `/hana/shared` size (GB) | `/usr/sap` size (GB) | Total size (GB) | `n1-highmem-32` |  249  | 104 | 208 | 32 |  593   
---|---|---|---|---|---  
`n1-highmem-64` | 499 | 208 | 416 | 32 | 1,155  
`n1-highmem-96` | 748 | 312 | 624 | 32 | 1,716  
`n2-highmem-32` |  307  | 128 | 256 | 32 |  723   
`n2-highmem-48` | 460 | 192 | 384 | 32 | 1,068  
`n2-highmem-64` | 614 | 256 | 512 | 32 | 1,414  
`n2-highmem-80` | 768 | 320 | 640 | 32 | 1,760  
`n2-highmem-96` | 921 | 384 | 768 | 32 | 2,105  
`n2-highmem-128` | 1,036 | 432 | 864 | 32 | 2,364  
  
## Certifications for Google Cloud NetApp Volumes

Google Cloud NetApp Volumes is a fully-managed, cloud-based data storage service that you can use to create an NFS file system for your SAP HANA workloads.

As indicated in the [Certified and supported SAP HANA hardware directory](https://www.sap.com/dmc/exp/2014-09-02-hana-hardware/enEN/#/solutions?filters=iaas;ve:29), SAP has certified Google Cloud NetApp Volumes for use with SAP HANA workloads that run on specific Compute Engine machine types. For information about the Compute Engine machines types that SAP has certified to run SAP HANA with NetApp Volumes, see [Certified machine types for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#certified-vms).

For information about how to size and configure NetApp Volumes for use with SAP HANA, see the [Google Cloud NetApp Volumes](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#netapp_cvs) section in the SAP HANA planning guide.

## Certified machine types for SAP HANA dynamic tiering

On Google Cloud, SAP HANA dynamic tiering must be installed on a dedicated Compute Engine instance. The following table shows the Compute Engine machine types that are certified by SAP for SAP HANA dynamic tiering on Google Cloud:

Warm store capacity | Production certified machine types  
---|---  
512 GB  
1,300 GB  
5,000 GB  
10,000 GB |  `n1-highmem-8`  
`n1-highmem-16`  
`n1-highmem-32`  
`n1-megamem-96`  
Custom configurations  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
