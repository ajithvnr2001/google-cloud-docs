---
url: https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-cloud-volumes-service-datastores/
title: Using NFS volume as vSphere datastore hosted by Cloud Volumes Service \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:44.088755+00:00
---

# Using NFS volume as vSphere datastore hosted by Cloud Volumes Service  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-cloud-volumes-service-datastores/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Using NFS volume as vSphere datastore hosted by Cloud Volumes Service

You can use [NetApp Cloud Volumes Service for Google Cloud](https://docs.cloud.google.com/solutions/partners/netapp-cloud-volumes) (CVS) as an external datastore for ESXi hosts in Google Cloud VMware Engine. To do so, you must create CVS-Performance volumes in select regions and then mount them as external datastores to their existing ESXi hosts in Google Cloud VMware Engine.

This solution supports CVS-Performance only and has the following functionality for datastores:

  * NFSv3 protocol
  * CVS-Performance with crash-resistant snapshots and cross-region replication



## Before you begin

The steps in this document assume that you have done the following:

  * Earmarked a `/26` CIDR for the Google Cloud VMware Engine service network to be used for external NFS storage.



## Configuring Service Subnets

**Note:** NSX-T gateway and distributed firewall rules don't apply to any service subnet.

Service subnets don't have a CIDR allocation on initial creation. You must specify a non-overlapping CIDR range and prefix. The first usable address becomes the gateway address. To allocate a CIDR range and prefix, edit one of the service subnets. Service subnets can be updated if CIDR requirements change. Modification of an existing service subnet CIDR can cause network availability disruption for VMs attached to that service subnet.

## Peering CVS Service with Google Cloud VMware Engine

**Note:** You don't need to repeat this process if you have already completed network peering to use CVS volumes as in-guest file shares. 

You must peer your CVS tenant project with your Google Cloud VMware Engine tenant project to enable ESXi hosts to communicate with the CVS file servers. To achieve this, follow the instructions provided under the **Get VPC network details** and **Create a peering connection** in [Using NFS shares hosted by CVS in workload VM Guests](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-cloud-volumes-service).

## Creating CVS volumes

You can create and manage CVS volumes using the CVS UI, VMware Engine API, and gcloud CLI by following the steps at [Workflow for managing cloud volumes](https://docs.cloud.google.com/solutions/partners/netapp-cloud-volumes/workflow).

**Note:** When using a CVS volume as a VMware Engine data store, don't select **Secondary** under the **Volume Replication** field. Selecting **Secondary** marks the volume read-only and prevents ESXi hosts from mounting the volume. For more details on the volume replication field, refer to [Use volume replication to protect your data](https://docs.cloud.google.com/architecture/partners/netapp-cloud-volumes/volume-replication).

## Marking CVS volumes as non-deletable

Before you can mount CVS volume as an external NFS datastore to ESXi hosts in Google Cloud VMware Engine, you must block users from accidentally deleting the volumes to avoid disruption. Follow the instructions found under [Creating an NFS volume](https://docs.cloud.google.com/architecture/partners/netapp-cloud-volumes/creating-nfs-volumes#creating_an_nfs_volume) to select this option in the CVS UI.

After creating the initial volume, you can perform CVS volume management (for example, grow or monitor), using the CVS Google Cloud console, VMware Engine API, or gcloud CLI. Refer to [Workflow for managing cloud volumes](https://docs.cloud.google.com/solutions/partners/netapp-cloud-volumes/workflow) for more information on completing management tasks.

After the datastores are mounted and available, users can use the vCenter UI to provision VMs against the external datastores, view metrics and view logs related to I/O operations performed against external datastores.

For more information on CVS, see [NetApp Cloud Volumes Service for Google Cloud documentation](https://docs.cloud.google.com/solutions/partners/netapp-cloud-volumes). You can also find general background information at [VMware vSphere for ONTAP](https://docs.netapp.com/us-en/netapp-solutions/virtualization/vsphere_ontap_ontap_for_vsphere.html).

Contact your account team if you need help completing onboarding.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
