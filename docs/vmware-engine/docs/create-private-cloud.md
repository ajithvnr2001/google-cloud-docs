---
url: https://docs.cloud.google.com/vmware-engine/docs/create-private-cloud/
title: Quickstart: Create a private cloud by using VMware Engine \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:15.852248+00:00
---

# Quickstart: Create a private cloud by using VMware Engine  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/create-private-cloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a private cloud by using VMware Engine

This quickstart explains how to set up Google Cloud VMware Engine and create a standard [private cloud](https://docs.cloud.google.com/vmware-engine/docs/concepts-private-cloud).

## Before you begin

To perform the steps in this quickstart, you need access to Google Cloud VMware Engine, available VMware Engine node quota, and an appropriate IAM role. Prepare the following requirements before you proceed:

  1. [Request API access and node quota](https://docs.cloud.google.com/vmware-engine/docs/quickstart-prerequisites).
  2. Verify that you're familiar with the address ranges you want to use for VMware management appliances and the HCX deployment network. For details, see [Networking requirements](https://docs.cloud.google.com/vmware-engine/docs/quickstart-networking-requirements).
  3. Have the `VMware Engine Service Admin` IAM role.

**Note:** The **Owner** and **Editor** basic roles include the **VMware Engine Service Admin** role. The **Viewer** basic role includes the **VMware Engine Service Viewer** role.

For more information, see [VMware Engine IAM roles and permissions](https://docs.cloud.google.com/vmware-engine/docs/iam).

## Create a standard private cloud

  1. In the Google Cloud console, go to the **Private clouds** page.

[Go to Private clouds](https://console.cloud.google.com/vmwareengine/privateclouds)

  2. Click **Select a project** and then select the organization, folder, or project where you want to create the private cloud.

  3. Click **Create**.

  4. Enter a name for the private cloud.

  5. Select **Standard private cloud** for the private cloud type.

  6. Select the location where you want the private cloud deployed.

  7. Enter a name for the primary cluster.

  8. Select the node type for your primary cluster.

  9. Select the number of nodes for the private cloud. For production workloads, create your private cloud with at least 3 nodes. VMware Engine deletes private clouds that contain only 1 node after 60 days.

  10. Optional: Click the **Customize Node Cores** toggle if you want to reduce the number of available cores for each node in the management cluster. For details, see [Custom core counts](https://docs.cloud.google.com/vmware-engine/docs/concepts-private-cloud#custom-core-count).

  11. Enter a CIDR range for the VMware management network. Make sure that the CIDR range doesn't overlap with any of your on-premises or cloud subnets.

  12. Select **Create new network** to create a new VMware Engine network or select from an existing network, if applicable.

  13. Click **Create** to begin creating the private cloud.




As VMware Engine creates your new private cloud, it deploys a number of [VMware components](https://docs.cloud.google.com/vmware-engine/docs/concepts-vmware-components) and divides the provided IP address range into subnets. Private cloud creation can take 30 minutes to 2 hours. After the provisioning is complete, you receive an email.

## Connect to your private cloud

To connect to your private cloud vCenter server, establish a secure connection from your network to the private cloud. You can use any of the following options to create a secure connection:

  * [Connect an on-premises network to VMware Engine private cloud](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-connect-to-onpremises).
  * [Connect using a point-to-site VPN connection](https://docs.cloud.google.com/vmware-engine/docs/concepts-vpn-gateways).



## What's next

  * [Get management appliance sign-in credentials](https://docs.cloud.google.com/vmware-engine/docs/vmware-platform/howto-access-vsphere-client) for your private cloud.
  * [Configure internet access for workload VMs](https://docs.cloud.google.com/vmware-engine/docs/networking/workload-internet-access) for your private cloud.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
