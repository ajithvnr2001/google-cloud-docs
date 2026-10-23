---
url: https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-cloud-volumes-service/
title: Connecting workload VMs to Cloud Volumes Service \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:17.817846+00:00
---

# Connecting workload VMs to Cloud Volumes Service  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-cloud-volumes-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Connecting workload VMs to Cloud Volumes Service

**Important:** This document has been replaced by [Connecting workload VMs to Google Cloud NetApp Volumes](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-connect-workload-vm-to-netapp-volumes). Refer to that page for information on connecting NetApp Volumes to VMware Engine.

[NetApp Cloud Volumes Service for Google Cloud](https://docs.cloud.google.com/solutions/partners/netapp-cloud-volumes) (CVS) speeds up the deployment of cloud-based applications through rapid provisioning of shared file services and storage management features. Connecting Cloud Volumes Service to VMware Engine lets you mount CVS cloud volumes from within the guest OS of your workload virtual machines (VMs).

Here are some common use cases for using cloud volumes with VMware Engine:

  * Virtual desktop infrastructure (VDI)
  * Creating VM home directories
  * Setting up file services
  * Shared file storage for applications and databases



Additionally, VMs in Compute Engine and Google Cloud VMware Engine can both mount the same cloud volumes. Here's a diagram that shows NetApp Cloud Volumes Service for Google Cloud being used with VMware Engine and Compute Engine:

![Architecture diagram of Cloud Volumes Service in relation to
          Google Cloud VMware Engine and Compute Engine](https://docs.cloud.google.com/static/vmware-engine/images/gcve-netapp-cvs.png)

## Before you begin

The steps in this document assume that you have done the following:

  * [Created a Cloud Volume](https://docs.cloud.google.com/solutions/partners/netapp-cloud-volumes/quickstart) with the selected parameters (like allocated capacity and protocol type) in a given region. You can use NFSv3, NFSv4, or SMB volumes for the connection described in this document.
  * [Created a private cloud](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-create-private-cloud) in the same region as your Cloud Volume.



## Get VPC network details

When creating a peering connection between VMware Engine and Cloud Volumes Service, you need some details about the VPC network used by Cloud Volumes Service:

  1. In the Google Cloud console, go to the **VPC Network peerings** page.

[Go to VPC Network peerings](https://console.cloud.google.com/vmwareengine/network-peerings)

  2. Click **Select a project** and then select the organization, folder, or project that contains the peering connection.

  3. Select the peering connection created for your Cloud Volume that corresponds to your private cloud. The CVS-Performance [service type](https://docs.cloud.google.com/architecture/partners/netapp-cloud-volumes/service-types) uses connections named "netapp-cv-nw-customer-peer", and the CVS service type uses connections named "netapp-sds-nw-customer-peer".

**Note:** You might see multiple peering connections with the same name if you have more than one peered VPC network for a service type. The person who set up the VPC Network Peering connections can help you determine which connection to use for VMware Engine.
  4. Copy the **Peered project ID** field, which ends with _-tp_.




### Create a peering connection for standard networks

To establish a connection between VMware Engine and Cloud Volumes Service create a [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering) between the tenant host project and the VMware Engine network using the details you copied previously.

  1. Create a new [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering).
  2. Select **Peered VPC type** : NetApp Cloud Volumes.
  3. In the **NetApp tenant project ID** field, enter the _peered project ID_.



Expect the VPC peering status of your new private connection to stay in the _Inactive_ state for up to 72 hours while VMware Engine services and validates the peering request.

## Mount a volume

Once the peering status of your private connection is listed as _Active_ , you can mount your cloud volume. Perform the mounting process from within the guest OS of your VMware VM.

To mount an NFS volume, do the following:

  1. In the Google Cloud console, go to **Cloud Volumes > Volumes**.

[Go to the Volumes page](https://console.cloud.google.com/netapp/cloud-volumes/volumes)

  2. Click **Select a project** and then select the organization, folder, or project that contains the volume.

  3. Click the NFS volume for which you want to mount NFS exports.

  4. Click **More** _more_vert_ , and then click **Mount Instructions**.

  5. Follow the instructions in the **Mount Instructions for NFS** window that appears. The mounting instructions might be slightly different depending on which NFS protocol you have configured for the volume.




To mount an SMB volume, do the following:

  1. In the Google Cloud console, go to **Cloud Volumes > Volumes**.

[Go to the Volumes page](https://console.cloud.google.com/netapp/cloud-volumes/volumes)

  2. Click **Select a project** and then select the organization, folder, or project that contains the volume.

  3. Click the SMB volume for which you want to map an SMB share.

  4. Click **More** _more_vert_ , and then click **Mount Instructions**.

  5. Follow the instructions in the **Mount Instructions for SMB** window that appears.




After you mount your cloud volume, you can manage the volume using the standard interfaces described by [Workflow for managing cloud volumes](https://docs.cloud.google.com/solutions/partners/netapp-cloud-volumes/workflow).

## What's next

  * Learn about [Using NFS volumes hosted by CVS as vSphere datastores](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-cloud-volumes-service-datastores).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
