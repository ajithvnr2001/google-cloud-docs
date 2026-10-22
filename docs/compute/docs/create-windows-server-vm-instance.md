---
url: https://docs.cloud.google.com/compute/docs/create-windows-server-vm-instance/
title: Create a Windows Server VM instance in Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:19:03.239429+00:00
---

# Create a Windows Server VM instance in Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/create-windows-server-vm-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a Windows Server VM instance in Compute Engine

Learn how to create a Windows Server virtual machine (VM) instance by using the Google Cloud console. 

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/compute?walkthrough_id=compute_windows_quickstart)

* * *

## Pricing

  * Windows Server images are premium images, and using them results in [additional charges](https://docs.cloud.google.com/compute/disks-image-pricing#windows_server_pricing).

  * Windows Server VMs are not included with the [Free Trial](https://docs.cloud.google.com/free/docs/gcp-free-tier#free-trial).




## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Make sure that you have the following role or roles on the project: Compute Instance Admin (v1), Compute Security Admin, Service Account User, Service Usage Admin 

#### Check for the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

     4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

     5. Click **Select a role** , then search for the role. 
     6. To grant additional roles, click add **Add another role** and add each additional role. 
     7. Click **Save**. 

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Make sure that you have the following role or roles on the project: Compute Instance Admin (v1), Compute Security Admin, Service Account User, Service Usage Admin 

#### Check for the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

     4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

     5. Click **Select a role** , then search for the role. 
     6. To grant additional roles, click add **Add another role** and add each additional role. 
     7. Click **Save**. 

  8. Enable the Compute Engine API.

[ Enable Compute Engine API](https://console.cloud.google.com/apis/api/compute.googleapis.com/overview)

  9. If you aren't using Windows on your local machine, install an RDP client such as [Chrome Remote Desktop](https://chrome.google.com/webstore/detail/inomeogfingihgjfjlpeplalcfajhgai).



## Create a Windows Server VM instance

  1. In the Google Cloud console, go to the **Create an instance** page. 

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. In the **OS and Storage** section, click **Change** to begin configuring your boot disk. 
  3. On the **Public images** tab, choose **Windows Server** from the **Operating system** list. 
  4. Choose **Windows Server 2019 Datacenter** from the **Version** list.
  5. Click **Select**. 
  6. In the **Firewall** section, select **Allow HTTP traffic**. 
  7. To create the VM, click **Create**. 



Allow a short time for the VM instance to start. After the VM instance is ready, it is listed on the **VM instances** page with a green status icon.

## Connect to the VM instance

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Under the **Name** column, click the name of your VM instance.

  3. Under the **Remote access** section, click **Set Windows password**.

  4. Specify a username, then click **Set** to generate a new password for this Windows Server VM. Save the username and password so you can log into the VM.

  5. [Install the Chrome Remote Desktop service](https://docs.cloud.google.com/architecture/chrome-desktop-remote-windows-compute-engine#install_the_chrome_remote_desktop_service) on your VM.

  6. Connect to your VM instance using your choice of [graphical](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows#iap-desktop) or [command line](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows#remote-desktop-connection-app) tools.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the name of the VM instance you created.

  3. At the top of the VM instance's details page, click **Delete**.




## What's next

  * Learn about [Windows Server images provided by Compute Engine](https://docs.cloud.google.com/compute/docs/images/os-details#windows_server).

  * Learn about [Microsoft software on Compute Engine](https://docs.cloud.google.com/compute/docs/instances/windows).

  * [Set up a basic IIS web server](https://docs.cloud.google.com/compute/docs/tutorials/basic-webserver-iis).

  * [Deploy an ASP.NET app on Compute Engine](https://docs.cloud.google.com/compute/docs/tutorials/deploy-aspnet-app).

  * Learn how to [create and manage Windows Server instances](https://docs.cloud.google.com/compute/docs/instances/windows/creating-managing-windows-instances).

  * [Deploy a fault-tolerant Microsoft Active Directory environment](https://docs.cloud.google.com/compute/docs/tutorials/setup-active-directory).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
