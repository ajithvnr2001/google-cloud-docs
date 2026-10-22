---
url: https://docs.cloud.google.com/firewall/docs/quickstarts/configure-nwfwpolicy-allow-egress/
title: Quickstart: Allow egress traffic using a global network firewall policy \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:01.942964+00:00
---

# Quickstart: Allow egress traffic using a global network firewall policy  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/quickstarts/configure-nwfwpolicy-allow-egress/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Allow egress traffic using a global network firewall policy

Learn how to secure your network by limiting egress traffic from a virtual machine (VM) instance. This quickstart shows you how to configure a [global network firewall policy](https://docs.cloud.google.com/firewall/docs/network-firewall-policies) to allow egress traffic from a VM instance to a specific IP address, while blocking all other egress traffic from VM instances in the same Virtual Private Cloud (VPC) network.

In this quickstart, you will complete the following tasks:

  * Create a custom mode VPC network with a subnet.
  * Create client and server VMs.
  * Create a global network firewall policy.
  * Add firewall rules.
  * Test the firewall policy.
  * Clean up and delete the resources.



## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Enable the [Compute Engine API](https://console.cloud.google.com/marketplace/product/google/compute.googleapis.com) for your project. 



### Required roles

To create custom mode VPC networks, VM instances, and global network firewall policies, or to view the logs, ask your administrator to grant you the required Identity and Access Management (IAM) roles on your project:

  * [Compute Network Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)
  * [Compute Instance Admin (v1) role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * [Compute Security Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.securityAdmin) (`roles/compute.securityAdmin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined).

## Create a custom mode VPC network with a subnet

In this section, you create a custom mode VPC network and an IPv4 subnet to host your VMs.

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click **Create VPC network**.

  3. For **Name** , enter `vpc-fw-rules`.

  4. For **Description** , enter `VPC network for the firewall rules quickstart`.

  5. For **Subnet creation mode** , select **Custom**.

  6. In the **New subnet** section, specify the following:

     * **Name** : `subnet-fw-rules`
     * **Region** : `us-central1`
     * **IPv4 range** : `10.0.0.0/24`
     * **Private Google Access** : **On**

Setting **Private Google Access** to **On** lets the VMs in this subnet access Google Cloud services without using an external IP address.

  7. Click **Done** , then click **Create**.




By default, the VPC network includes following implied IPv4 rules:

  * An allow egress rule with destination `0.0.0.0/0` and lowest possible priority (65535) that allows any instance to send traffic to any destination, except for traffic blocked by Google Cloud.
  * A deny ingress with source `0.0.0.0/0` and lowest possible priority (65535) that protects all instances by blocking incoming connections to them.



For more information about the implied rule or action for an ingress or egress traffic, see [Firewall rule evaluation process](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-eval-order#default-rule-evaluation).

## Create client and server VMs

In this section, you create two Linux VMs without external IP addresses in the subnet of the VPC network you created earlier.

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. For **Name** , enter `vm-fw-rules-server`.

  3. For **Region** , select `us-central1 (Iowa)`.

  4. In the **Networking** menu, under **Network interfaces** , select:

     * **Network** : `vpc-fw-rules`
     * **Subnetwork** : `subnet-fw-rules IPv4 (10.0.0.0/24)`
     * **External IPv4 address** : **Ephemeral**
  5. Click **Done** , then click **Create**.

  6. Make a note of the internal IP address of the VM after it is created.

  7. Repeat these steps to create a second VM named `vm-fw-rules-client` using the same network settings, but set **External IPv4 address** to **None**.




To install and run an `nginx` web server on `vm-fw-rules-server`, follow these steps:

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click **SSH** for `vm-fw-rules-server`.

  3. In the **SSH-in-browser** dialog, click **Authorize** and wait for the connection to establish.

  4. To install and run the `nginx` web server, run the `sudo apt update && sudo apt install nginx` command.




## Create a global network firewall policy

In this section, you create a global network firewall policy and associate it with the VPC network you created earlier.

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. Click **Create firewall policy**.

  3. For **Policy name** , enter `fw-policy`.

  4. For **Deployment scope** , select **Global**.

  5. Click **Continue** to skip through the rules section. You will add firewall rules in the next sections of this quickstart.

  6. In the **Associate policy with networks** section, click **Associate**.

  7. Select the `vpc-fw-rules` checkbox and click **Associate** to associate the VPC network with the policy.

  8. Click **Continue** , then click **Create**.




## Add firewall rules

In this section, you add firewall rules to the global network firewall policy that you created earlier.

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. Click the name of your firewall policy. On the **Firewall rules** tab of your policy, click **Create firewall rule**.

  3. Add an ingress rule to allow TCP traffic to port `22`. This rule enables Identity-Aware Proxy (IAP) access to the VM instances in the VPC network. The IAP service uses a central authorization layer to help you access the client and server VMs. For more information, see [Identity-Aware Proxy overview](https://docs.cloud.google.com/iap/docs/concepts-overview).

     * For **Priority** , enter `100`.
     * For **Target type** , select **Instances**.
     * For **Target** , select **Apply to all**.
     * For **Direction of traffic** , select **Ingress**.
     * For **Action on match** , select **Allow**.
     * For **Logs** , select **Enabled**.

**Note:** Enabling logs can generate a large number of logs, which can result in higher costs.

     * For **Source network context** , select **All network contexts**.

     * In the **Source** section, for **IP type** , select **IPv4**. In **IP ranges** , enter `35.235.240.0/20`.

     * For **Protocols and ports** , select **Specified protocols and ports** , and then select **TCP**. For **Ports** , enter `22`.

     * For **Enforcement** , select **Enabled**.

  4. Click **Create**.

  5. Add an ingress rule to allow ingress traffic on the server VM from the client VM:

     * For **Priority** , enter `200`.
     * For **Target type** , select **Instances**.
     * For **Target** , select **Apply to all**.
     * For **Direction of traffic** , select **Ingress**.
     * For **Action on match** , select **Allow**.
     * For **Logs** , select **Enabled**.

**Note:** Enabling logs can generate a large number of logs, which can result in higher costs.

     * For **Source network context** , select **Specific network context** , and then select **Intra VPC**.

     * In the **Source** section, for **IP type** , select **IPv4**. In **IP ranges** , specify the internal IP address of the client VM. For example, `10.0.0.2/32`.

     * In the **Destination** section, for **IP type** , select **IPv4**. In **IP ranges** , specify the internal IP address of the server VM. For example, `10.0.0.1/32`.

     * For **Protocols and ports** , select **Specified protocols and ports** , and then select **TCP**. For **Ports** , enter `80`.

     * For **Enforcement** , select **Enabled**.

  6. Click **Create**.

  7. For improved security, you can limit all outbound traffic and create a narrowly defined egress rule to allow only the identified traffic.

     1. Add an egress rule to delegate the egress traffic from the client VM (towards the server VM) to the next rule in the [firewall rule evaluation order](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-eval-order#determine-rule-evaluation), which is the implied IPv4 action that allows all egress traffic. 
        * For **Priority** , enter `300`.
        * For **Target type** , select **Instances**.
        * For **Target** , select **Apply to all**.
        * For **Direction of traffic** , select **Egress**.
        * For **Action on match** , select **Go to next**.
        * For **Destination network context** , select **Specific network context** , and then select **Non-internet**.
        * In the **Destination** section, for **IP type** , select **IPv4**. In **IP ranges** , specify the internal IP address of the server VM. For example, `10.0.0.1/32`.
        * In the **Source** section, for **IP type** , select **IPv4**. In **IP ranges** , specify the internal IP address of the client VM. For example, `10.0.0.2/32`.
        * For **Protocols and ports** , select **Specified protocols and ports** , and then select **TCP**. For **Ports** , enter `80`.
        * For **Enforcement** , select **Enabled**.
     2. Click **Create**.
     3. Add an egress rule to deny egress traffic from all VMs:

        * For **Priority** , enter `400`.
        * For **Target type** , select **Instances**.
        * For **Target** , select **Apply to all**.
        * For **Direction of traffic** , select **Egress**.
        * For **Action on match** , select **Deny**.
        * For **Logs** , select **Enabled**.

**Note:** Enabling logs can generate a large number of logs, which can result in higher costs.

        * For **Destination network context** , select **All network contexts**.

        * In the **Destination** section, for **IP type** , select **IPv4**. In **IP ranges** , enter `0.0.0.0/0`.

        * For **Protocols and ports** , select **Allow all**.

        * For **Enforcement** , select **Enabled**.

     4. Click **Create**.




## Test the firewall policy

In this section, you test the global network firewall policy.

To verify that `vm-fw-rules-client` can send traffic to `vm-fw-rules-server`, follow these steps:

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click **SSH** for `vm-fw-rules-client`.

  3. In the **SSH-in-browser** dialog, click **Authorize** and wait for the connection to establish.

  4. To verify that the connection succeeds, run the following command:

`curl <IP_vm-fw-rules-server> -m 2`

Replace `IP_vm-fw-rules-server` with the internal IP address of the `vm-fw-rules-server` VM.




To verify that the egress traffic from any VM in the VPC network is blocked, follow these steps:

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click **SSH** for `vm-fw-rules-server`.

  3. In the **SSH-in-browser** dialog, click **Authorize** and wait for the connection to establish.

  4. To verify that the connection times out, run the following command:

`curl <IP_vm-fw-rules-client> -m 2`

Replace `IP_vm-fw-rules-client` with the internal IP address of the `vm-fw-rules-client` VM.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this quickstart, either delete the project that contains the resources, or keep the project and delete the individual resources.

In this section, you delete the resources created in this quickstart.

### Delete the firewall policy

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the **Network firewall policies** section, select the `fw-policy` name.

  3. Click the **Associations** tab, and remove the association with `vpc-fw-rules`.

  4. Next to the `fw-policy` title, click **Delete** to delete the firewall policy.




### Delete the VMs

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select the checkboxes for `vm-fw-rules-client` and `vm-fw-rules-server` VMs.

  3. Click **Delete**.




### Delete the VPC network and its subnets

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. In the **Name** column, click `vpc-fw-rules`.

  3. Click **Delete VPC network**. Deleting a VPC also deletes its subnets.




## What's next

  * [Create a custom mode VPC network with IPv4-only subnets](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#create-custom-network)
  * [Create and start a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance)
  * [Firewall policies and rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview)
  * [Firewall policy rule components](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details)
  * [Evaluation order for firewall policies and rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-eval-order)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
