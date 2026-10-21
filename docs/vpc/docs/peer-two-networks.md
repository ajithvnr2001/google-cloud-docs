---
url: https://docs.cloud.google.com/vpc/docs/peer-two-networks/
title: Quickstart: Peer two VPC networks \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:15:59.604194+00:00
---

# Quickstart: Peer two VPC networks  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/peer-two-networks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Peer two VPC networks

In this quickstart, learn how to peer two Virtual Private Cloud (VPC) networks by using the Google Cloud console.

Consider an organization `organization-a` that needs VPC Network Peering to be established between `network-a` in `project-a` and `network-b` in `project-b`. In order for VPC Network Peering to be established successfully, administrators of `network-a` and `network-b` must separately configure the peering association.

By completing the steps on this page, you create the following configuration:

[ ![Peering active.](https://docs.cloud.google.com/static/vpc/images/peering/network-peering-quickstart.svg)](https://docs.cloud.google.com/static/vpc/images/peering/network-peering-quickstart.svg) Two networks with an active peering connection (click to enlarge).

The peering connection is in [independent mode](https://docs.cloud.google.com/vpc/docs/about-peering-connections#connection-mode) (default).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. Enable the Compute Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com)

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. Enable the Compute Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com)

  10. Repeat these steps for a second project. This quickstart describes how to peer VPC networks that are in separate projects.



### Required roles

To get the permissions that you need to peer two VPC networks, ask your administrator to grant you the following IAM roles on the project: 

  * [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)
  * [Compute Security Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.securityAdmin) (`roles/compute.securityAdmin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create two VPC networks

In this section, you create two VPC networks, each in different projects.

### Create `network-a` and `subnet-a` in your first project

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click **Create VPC network**.

  3. In the **Name** field, enter `network-a`.

  4. In the **New subnet** section, specify the following:

     1. In the **Name** field, enter `subnet-a`.
     2. Select any **Region**.
     3. In the **IPv4 range** field, enter `10.0.1.0/24`.
     4. Click **Done**.
  5. In the **IPv4 firewall rules** tab, on the right side of the row that contains the predefined ingress firewall rule named **`NETWORK -allow-custom`**, click **Edit**.

     1. Deselect **Use subnets' IPv4 ranges**.
     2. In **Other IPv4 ranges** , enter `10.0.0.0/20`. Entering this range ensures that the resources in your peered networks can communicate with each other and lets you add more subnets in the future without having to update firewall rules.
     3. Click **Confirm**.
  6. Click **Create**.




### Create `network-b` and `subnet-b` in your second project

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click **Create VPC network**.

  3. In the **Name** field, enter `network-b`.

  4. In the **New subnet** section, specify the following:

     1. In the **Name** field, enter `subnet-b`.
     2. Select any **Region**.
     3. In the **IPv4 range** field, enter `10.0.8.0/24`.
     4. Click **Done**.
  5. In the **IPv4 firewall rules** tab, on the right side of the row that contains the predefined ingress firewall rule named **`NETWORK -allow-custom`**, click **Edit**.

     1. Deselect **Use subnets' IPv4 ranges**.
     2. In **Other IPv4 ranges** , enter `10.0.0.0/20`. Entering this range ensures that the resources in your peered networks can communicate with each other and lets you add more subnets in the future without having to update firewall rules.
     3. Click **Confirm**.
  6. Click **Create**.




## Peer `network-a` with `network-b`

In this section, you configure `network-a` to peer with `network-b`.

###  Console 

  1. In the Google Cloud console, go to the **VPC Network Peering** page.

[Go to VPC Network Peering](https://console.cloud.google.com/networking/vpc-connectivity/peering)

  2. Click **Create connection**.

  3. Click **Continue**.

  4. Enter a **Name** of `peer-ab` for this side of the connection.

  5. Under **Your VPC network** , select `network-a`.

  6. Set the **Peering VPC network** radio buttons to `In another project`.

  7. Specify the **Project ID** of the other project.

  8. Specify the **VPC network name** of the other network, `network-b`.

  9. Select **Import custom routes** and **Export custom routes**.

  10. Click **Create**.




At this point, the peering state remains `INACTIVE` because of the absence of a matching configuration in `network-b` in `project-b`.

When the peering state becomes `ACTIVE`, VPC Network Peering automatically exchanges subnet routes. Google Cloud also exchanges custom routes (static routes and dynamic routes) by importing or exporting them over the peering connection. Both networks must be configured to exchange custom routes before they are shared. For more information, see [Importing and exporting custom routes](https://docs.cloud.google.com/vpc/docs/vpc-peering#importing-exporting-routes).

To see the current peering state, view the peering connection:

###  Console 

  1. In the Google Cloud console, go to the **VPC Network Peering** page.

[Go to VPC Network Peering](https://console.cloud.google.com/networking/vpc-connectivity/peering)

  2. Select `peer-ab`. On the **Peering connection details** page, the status says `Inactive. Waiting for the connection to be created by network-b`.




## Peer `network-b` with `network-a`

In this section, you create a matching peering configuration from `network-b` to `network-a` so that the peering becomes `ACTIVE` on both ends.

###  Console 

  1. In the Google Cloud console, go to the **VPC Network Peering** page.

[Go to VPC Network Peering](https://console.cloud.google.com/networking/vpc-connectivity/peering)

  2. Click **Create connection**.

  3. Click **Continue**.

  4. Enter a **Name** of `peer-ba` for this side of the connection.

  5. Under **Your VPC network** , select `network-b`.

  6. Set the **Peering VPC network** radio buttons to `In another project`.

  7. Specify the **Project ID** of the other project.

  8. Specify the **VPC network name** of the other network, `network-a`.

  9. Select **Import custom routes** and **Export custom routes**.

  10. Click **Create**.




## VPC Network Peering becomes `ACTIVE`

As soon as the peering moves to an `ACTIVE` state, subnet routes and custom routes are exchanged, which allows traffic to flow between resources in the networks.

###  Console 

  1. In the Google Cloud console, go to the **VPC Network Peering** page.

[Go to VPC Network Peering](https://console.cloud.google.com/networking/vpc-connectivity/peering)

  2. On the VPC Network Peering page, the status for the connection that you created says `ACTIVE`.

  3. Go to the VPC Network Peering page in the other project to see that it also says `ACTIVE`.




The routes to peered network CIDR prefixes are now visible across the VPC network peers. These routes are implicit routes that are generated for active peering connections. They don't have corresponding route resources. The following procedure shows routes for all VPC networks for `project-a`.

###  Console 

  1. In the Google Cloud console, go to the **Routes** page.

[Go to Routes](https://console.cloud.google.com/networking/routes/list)

  2. For **Network** and **Region** , select `network-a` and the region in which you created `subnet-a`, then click **View**.

  3. In the list of routes, there is a `Peering subnet` route for `subnet-b`.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

### Delete the projects

To delete the projects that you created:

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete individual resources

If you don't want to delete the entire project, delete the VPC Network Peering connections and the VPC networks that you created.

Before you can delete a network, you must delete its VPC Network Peering connection.

#### Delete VPC Network Peering connections

To delete a VPC Network Peering connection:

###  Console 

  1. In the Google Cloud console, go to the **VPC Network Peering** page.

[Go to VPC Network Peering](https://console.cloud.google.com/networking/vpc-connectivity/peering)

  2. Select the checkbox next to the peering you want to remove.

  3. Click **Delete**.




#### Delete VPC networks

To delete a VPC network:

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click the name of a VPC network to show its **VPC network details** page.

  3. Click **Delete VPC network**.

  4. In the message that appears, click **Delete** to confirm.




## What's next

  * [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering) overview
  * [About peering connections](https://docs.cloud.google.com/vpc/docs/about-peering-connections)
  * [Set up and manage VPC Network Peering](https://docs.cloud.google.com/vpc/docs/using-vpc-peering)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
