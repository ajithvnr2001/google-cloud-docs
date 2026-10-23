---
url: https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-cloud-dell-powerscale/
title: Connecting workload VMs to Dell PowerScale \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:15.253412+00:00
---

# Connecting workload VMs to Dell PowerScale  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-cloud-dell-powerscale/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Connecting workload VMs to Dell PowerScale

[Dell PowerScale](https://docs.cloud.google.com/architecture/partners/dell-powerscale) on Google Cloud speeds up the deployment of cloud-based applications through rapid provisioning of shared file services and storage management features. Connecting Dell PowerScale to VMware Engine lets you mount Dell PowerScale shares from within the guest OS of your workload virtual machines (VMs).

Here are some core benefits to using Dell PowerScale with VMware Engine:

  * Run the most demanding file-based workloads that require extreme performance and throughput, including AI and ML.
  * Create scale-out capacity up to 50 pebibytes (PiB) in a single namespace and scale-out performance up to 97 MBps/TiB.
  * Hand off complete lifecycle management of the environment to Dell experts.



Additionally, VMs in Compute Engine and Google Cloud VMware Engine can both mount the same Dell PowerScale volumes. Here's a diagram that shows Dell PowerScale being used with VMware Engine and Compute Engine:

![Architecture diagram of Dell PowerScale in relation to
          Google Cloud VMware Engine and Compute Engine](https://docs.cloud.google.com/static/vmware-engine/images/gcve-dell-powerscale.svg)

## Before you begin

The steps in this document assume that you have done the following:

  * [Created a fileshare](https://docs.cloud.google.com/architecture/partners/dell-powerscale/create-a-fileshare) with the selected parameters (like allocated capacity and protocol type) in a given region. You can use NFSv3 or SMB volumes for the connection described in this document.
  * [Created a private cloud](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-create-private-cloud) in the same region as your Cloud Volume.



## Get VPC network details

When creating a peering connection between VMware Engine and Dell PowerScale, you need some details about the VPC network used by Dell PowerScale:

  1. In the Google Cloud console, go to the **VPC Network peerings** page.

[Go to VPC Network peerings](https://console.cloud.google.com/vmwareengine/network-peerings)

  2. Click **Select a project** and then select the organization, folder, or project that contains the peering connection.

  3. Select the peering connection created for your Dell PowerScale that corresponds to your private cloud.

**Note:** You might see multiple peering connections with the same name if you have more than one peered VPC network for a service type. The person who set up the VPC Network Peering connections can help you determine which connection to use for VMware Engine.
  4. Copy the **Peered VPC network** and **Peered project ID** fields, which begin with `dellemc` and end with `-tp`, respectively.




### Create a peering connection for standard networks

To establish a connection between VMware Engine and Dell PowerScale create a [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering) between the tenant host project and the VMware Engine network using the details you copied previously.

  1. Create a new [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering)
  2. Select **Peered VPC type** : Dell PowerScale
  3. In the **Dell tenant project ID** field, enter the _peered project ID_.



Expect the VPC peering status of your new private connection to stay in the _Inactive_ state for up to 72 hours while VMware Engine services and validates the peering request.

### Create a peering connection for legacy networks

To establish a connection between VMware Engine and Dell PowerScale create a [VPC Private Connection](https://docs.cloud.google.com/vpc/docs/configure-private-services-access) between the tenant host project and the VMware Engine network using the details you copied previously.

  1. Create a new [VPC Private Connection](https://docs.cloud.google.com/vpc/docs/configure-private-services-access)
  2. Select **Private connection type** : Dell PowerScale
  3. In the **Peer Project ID** field, enter the _peered project ID_ of the Google Cloud project containing your Dell PowerScale.
  4. In the **Peer VPC ID** field, enter the name of the _peered VPC network_ your Dell PowerScale is in.



Repeat the preceding process for each region containing your Cloud Volumes and private clouds. Expect the VPC peering status of your new private connection to stay in the _Inactive_ state for up to 72 hours while VMware Engine services and validates the peering request.

## Mount a volume

Once the peering status of your private connection is listed as _Active_ , you can mount Dell PowerScale fileshare. Perform the mounting process from within the guest OS of your VMware VM.

To use the Google Cloud console to mount an NFS fileshare, follow these instructions:

  1. In the **Google Cloud console** , click **PowerScale > Clusters**. The **PowerScale Clusters** page opens.
  2. Click the name of the cluster you want to manage.
  3. From the fileshares list, click **More** _more_vert_ next to the fileshare you want to mount, and then click **Mount Instructions**.
  4. Follow the instructions in the **Mount Instructions for NFSv3** window for setting up your NFSv3 instance and mounting your NFSv3 fileshare to complete the process.



To use the Google Cloud console to mount an SMB fileshare, follow these instructions:

  1. In the **Google Cloud console** , click **PowerScale > Clusters**. The **PowerScale Clusters** page opens.
  2. Click the name of the cluster you want to manage.
  3. From the fileshares list, click **More** _more_vert_ next to the fileshare you want to mount, and then click **Mount Instructions**.
  4. Follow the instructions in the **Mount Instructions for SMB** window for setting up your SMB instance and mounting your SMB fileshare to complete the process.



After you mount your cloud volume, you can manage the volume using the standard interfaces described by [PowerScale Administration interface](https://docs.cloud.google.com/architecture/partners/dell-powerscale/webui-overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
