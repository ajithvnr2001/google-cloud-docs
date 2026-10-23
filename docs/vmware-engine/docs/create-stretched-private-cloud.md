---
url: https://docs.cloud.google.com/vmware-engine/docs/create-stretched-private-cloud/
title: Create a stretched private cloud with VMware Engine \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:04.105550+00:00
---

# Create a stretched private cloud with VMware Engine  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/create-stretched-private-cloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a stretched private cloud with VMware Engine

This quickstart explains how to set up Google Cloud VMware Engine and create a [stretched private cloud](https://docs.cloud.google.com/vmware-engine/docs/concepts-stretched-private-cloud).

## Before you begin

To perform the steps in this quickstart, you need access to Google Cloud VMware Engine, available VMware Engine node quota, and an appropriate IAM role.

Prepare the following requirements before you proceed:

  1. [Request API access and node quota](https://docs.cloud.google.com/vmware-engine/docs/quickstart-prerequisites).

  2. Verify that you're familiar with the address ranges you want to use for VMware management appliances and the HCX deployment network. For details, see [Networking requirements](https://docs.cloud.google.com/vmware-engine/docs/quickstart-networking-requirements).

  3. Have the `VMware Engine Service Admin` IAM role.


**Note:** The **Owner** and **Editor** basic roles include the **VMware Engine Service Admin** role. The **Viewer** basic role includes the **VMware Engine Service Viewer** role. For more information, see [VMware Engine IAM roles and permissions](https://docs.cloud.google.com/vmware-engine/docs/iam).

Lastly, the steps in this document assume that you first do the following:

  * Allocate a unique IP address range for vSphere or vSAN subnets of the private cloud you want to create. 
    * **Minimum CIDR range prefix:** _/24_
    * **Maximum CIDR range prefix:** _/20_
  * If you want [global address resolution using Cloud DNS](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-dns-on-premises#global-address-resolution-cloud-dns), then [enable the Cloud DNS API](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name#before-you-begin) and complete Cloud DNS setup before you create your private cloud.



The vSphere or vSAN subnet address space must not overlap with any network that will communicate with the private cloud, such as on-premises networks and Google Cloud Virtual Private Cloud (VPC) networks. For more information about vSphere or vSAN subnets, see [VLANs and subnets on VMware Engine](https://docs.cloud.google.com/vmware-engine/docs/concepts-vlans-subnets).

## Create a stretched private cloud

  1. In the Google Cloud console, go to the **Private clouds** page.

[Go to Private clouds](https://console.cloud.google.com/vmwareengine/privateclouds)

  2. Click **Select a project** and then select the organization, folder, or project where you want to create the stretched private cloud.

  3. Click **Create**.

  4. Click **Stretched private cloud**.

  5. Enter your primary hosting location and select your secondary zone.

  6. Select the node type for your primary cluster.

  7. Select the number of nodes per zone for the stretched private cloud. Create your stretched private cloud with a minimum of 3 nodes per zone.

  8. Optional: Click the **Customize Cores** toggle if you want to reduce the number of available cores for each node in the management cluster. For details, see [Custom core counts](https://docs.cloud.google.com/vmware-engine/docs/concepts-private-cloud#custom-core-count).

  9. Enter a CIDR range for the VMware management network. Make sure that the CIDR range doesn't overlap with any of your on-premises or cloud subnets.

  10. Select **Create new network** to create a new VMware Engine network or select from an existing network, if applicable.

  11. Click **Create** to begin creating the private cloud.




As VMware Engine creates your new stretched private cloud, it deploys a number of [VMware components](https://docs.cloud.google.com/vmware-engine/docs/concepts-vmware-components) and divides the provided IP address range into subnets. Stretched private cloud creation can take 30 minutes to 2 hours. After the provisioning is complete, you receive an email.

**Note:** If the stretched cluster creation fails and you see the message `error Stretched private cloud creation is not allowed in projects without the gcp.requiresPhysicalZoneSeparation organizational policy constraint`, reach out to your account or support team before creating the stretched cluster for a new organization.

## Connect to your private cloud

To connect to your standard or stretched private cloud vCenter server, establish a secure connection from your network to the private cloud. You can use any of the following options to create a secure connection:

  * [Connect an on-premises network to VMware Engine private cloud](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-connect-to-onpremises)
  * [Connect using a point-to-site VPN connection](https://docs.cloud.google.com/vmware-engine/docs/concepts-vpn-gateways)



## What's next

  * [Get management appliance sign-in credentials](https://docs.cloud.google.com/vmware-engine/docs/vmware-platform/howto-access-vsphere-client) for your private cloud.
  * [Configure internet access for workload VMs](https://docs.cloud.google.com/vmware-engine/docs/networking/workload-internet-access) for your private cloud.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
