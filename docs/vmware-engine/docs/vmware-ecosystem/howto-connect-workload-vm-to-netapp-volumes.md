---
url: https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-connect-workload-vm-to-netapp-volumes/
title: Connecting workload VMs to Google Cloud NetApp Volumes \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:27:08.997162+00:00
---

# Connecting workload VMs to Google Cloud NetApp Volumes  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-connect-workload-vm-to-netapp-volumes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Connecting workload VMs to Google Cloud NetApp Volumes

[Google Cloud NetApp Volumes](https://docs.cloud.google.com/architecture/partners/netapp-cloud-volumes) speeds up the deployment of cloud-based applications through rapid provisioning of shared file services and storage management features. Connecting NetApp Volumes to VMware Engine lets you mount NetApp Volumes volumes from within the guest OS of your workload virtual machines (VMs).

Here are some common use cases for using NetApp Volumes with VMware Engine:

  * Virtual desktop infrastructure (VDI)
  * Creating VM home directories
  * Setting up file services
  * Shared file storage for applications and databases



Additionally, VMs in Compute Engine and Google Cloud VMware Engine can both mount the same volumes. Here's a diagram that shows Google Cloud NetApp Volumes being used with VMware Engine and Compute Engine:

![Architecture diagram of NetApp Volumes in relation to
          Google Cloud VMware Engine and Compute Engine](https://docs.cloud.google.com/static/vmware-engine/images/gcve-cloud-netapp-volumes.png)

## Before you begin

The steps in this document assume that you have done the following:

  * [Created a Storage Pool](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/storage-pools/create-storage-pool) with the chosen location, service level, capacity, data encryption, and AD policy.
  * [Created a Volume](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/create-volume) in a pre-existing storage pool with the selected parameters (like allocated capacity and protocol type) in a given region. You can use NFSv3, NFSv4, or SMB volumes for the connection described in this document.
  * [Created a private cloud](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-create-private-cloud) in the same region as your volume.
  * If your organization enforces [organization restrictions](https://docs.cloud.google.com/resource-manager/docs/organization-restrictions/overview) using the `X-Goog-Allowed-Resources` header or restricts VPC network peering using the [`constraints/compute.restrictVpcPeering`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) organization policy constraint, added the NetApp Volumes service producer organization (`organizations/326276363991`) to your allowed organizations list. NetApp Volumes tenant projects reside in `organizations/326276363991`, and peering requests fail with a `Request is prohibited by organization's policy` error if this organization ID is not allowed.



## Get VPC network details

When creating a peering connection between VMware Engine and NetApp Volumes, you need some details about the VPC network used by NetApp Volumes. To get these details, do the following:

  1. In the Google Cloud console, go to the **VPC Network peerings** page.

[Go to VPC Network peerings](https://console.cloud.google.com/vmwareengine/network-peerings)

  2. Click **Select a project** and then select the organization, folder, or project that contains the peering connection.

  3. Select the peering connection created in NetApp Volumes for your project. The connection is named `sn-netapp-prod`.

You might see multiple peering connections with the same name if you have more than one peered VPC network. The person who set up the VPC Network Peering connections can help you determine which connection to use for VMware Engine.

  4. Copy the **Peered VPC network** and **Peered project ID** fields, which begin with _netapp_ and end with _-tp_ , respectively.




## Create a peering connection

If your VMware Engine project and private clouds were created after Nov 12, 2023, do the following. For more information on how to create VPC peerings for such environments, see [Peer a VPC network](https://docs.cloud.google.com/vmware-engine/docs/networking/peer-vpc-network).

  1. In the Google Cloud console, go to the **VPC Network peerings** page.

[Go to VPC Network peerings](https://console.cloud.google.com/vmwareengine/network-peerings)

  2. Click **Select a project** and then select the organization, folder, or project where you want to create the peering connection.

  3. Click **Create**.

  4. In the **Name** field, provide a name for your networking peering. For example, `peering-2-netapp-volumes`.

  5. In the **VMware Engine network** section, keep the default **"In current project"** selected. Specify the VMware Engine network you want to peer, for example `ven1`.

  6. For **Peering** , select **Google Cloud NetApp Volumes**.

  7. In the **Service tenant project ID** field, enter the _peered project ID_ of the Google Cloud project containing your volume.

  8. In the **Service tenant VPC name** field, enter the name of the _peered VPC network_ your volume is in.

  9. In the **Route exchange** section, keep the default settings.

  10. Click **Create**.




## Create a peering connection for legacy networks

To establish a connection between VMware Engine and NetApp Volumes, make a one-time peering between tenant host projects. If you created your VMware Engine project and private clouds before November 12, 2023, you are using an earlier version of the VMware Engine network. For environments using an earlier version of the VMware Engine network, do the following:

  1. In the Google Cloud console, go to the **Private connections** page.

[Go to Private connections](https://console.cloud.google.com/vmwareengine/private-connections)

  2. Click **Select a project** and then select the organization, folder, or project where you want to create the peering connection.

  3. Click **Create**.

  4. In **Private connection name** , provide a name for your peering, for example, `peering-2-netapp-volumes`.

  5. In **VMware Engine network** , specify the VMware Engine network you want to peer, for example, `us-central1-default`.

  6. For **Private connection type** , select **Third party service**.

  7. In **Peered project ID** , enter the peered project ID of the NetApp Volumes that contains your volume.

  8. In **Peered VPC network** , enter the name of the peered VPC network that the volume is in.

  9. Click **Create**.




Expect the VPC peering status of your new private connection to stay in the _Inactive_ state for up to 72 hours while VMware Engine services and validates the peering request.

## Mount a volume

Once the peering status is listed as _Active_ , you can mount your NetApp Volumes volume. Perform the mounting process from within the guest OS of your VMware VM.

To mount an NFS volume, do the following:

  1. In the Google Cloud console, go to **NetApp Volumes > Volumes**.

[Go to the Volumes page](https://console.cloud.google.com/netapp/cloud-volumes/volumes)

  2. Click **Select a project** and then select the organization, folder, or project that contains the volume.

  3. Click the NFS volume for which you want to mount NFS exports.

  4. Go to the right, click **More** _more_vert_ , and then click **Mount Instructions**.

  5. Follow the instructions in the **Mount Instructions for NFS** window that appears. The mounting instructions might be slightly different depending on which NFS protocol you have configured for the volume.




To mount an SMB volume, do the following:

  1. In the Google Cloud console, go to **NetApp Volumes > Volumes**.

[Go to the Volumes page](https://console.cloud.google.com/netapp/cloud-volumes/volumes)

  2. Click **Select a project** and then select the organization, folder, or project that contains the volume.

  3. Click the SMB volume for which you want to map an SMB share.

  4. Go to the right, click **More** _more_vert_ , and then click **Mount Instructions**.

  5. Follow the instructions in the **Mount Instructions for SMB** window that appears.




After you mount your volume, you can manage the volume using the standard interfaces described by [Edit a volume](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/edit-volume).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
