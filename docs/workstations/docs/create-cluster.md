---
url: https://docs.cloud.google.com/workstations/docs/create-cluster/
title: Create a workstation cluster \u00a0|\u00a0 Cloud Workstations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:06.686359+00:00
---

# Create a workstation cluster  |  Cloud Workstations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workstations/docs/create-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Workstations ](https://docs.cloud.google.com/workstations/docs)
  * [ Guides ](https://docs.cloud.google.com/workstations/docs/overview)



Send feedback 

#  Create a workstation cluster Stay organized with collections  Save and categorize content based on your preferences. 

Learn how to get started creating a workstation cluster with Cloud Workstations. 

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/freetrial?redirectPath=/?walkthrough_id=workstations--create-cluster)

* * *

## Before you begin

Before you begin using Cloud Workstations, be sure that you have the [required permissions](https://docs.cloud.google.com/workstations/docs/access-control#enable_required_roles) and that you complete these required setup steps. You can skip this section if you've already completed this setup.

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

  6. Enable the Cloud Workstations API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=workstations.googleapis.com)

  7. Make sure that you have a Cloud Workstations Admin IAM role on the project so that you can create workstation configurations. To check your IAM roles in the Google Cloud console, go to the **IAM** page:

[ Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  8. Cloud Workstations are hosted on VMs booted from Compute Engine's preconfigured public [Container-Optimized OS (COS)](https://docs.cloud.google.com/compute/docs/images/os-details#container-optimized_os_cos) images. If the `constraints/compute.trustedimageProjects` organization policy constraint is enforced, you must [set image access constraints](https://docs.cloud.google.com/compute/docs/images/restricting-image-access#trusted_images) to allow users to create boot disks from `projects/cos-cloud` or all public images. 
  9. Cloud Workstations uses Private Service Connect to connect to Google-managed services. If the `constraints/compute.restrictPrivateServiceConnectProducer` organization policy constraint is enforced in your organization, you must [add Google as an allowed producer](https://docs.cloud.google.com/vpc/docs/manage-security-private-service-connect-consumers#add-org-policy) (`under:organizations/433637338589`). 
  10. If the `constraints/compute.disablePrivateServiceConnectCreationForConsumers` organization policy constraint is enforced in your organization, you must ensure that Private Service Connect endpoints connecting to Google APIs (`GOOGLE_APIS`) are [allowed](https://docs.cloud.google.com/vpc/docs/manage-security-private-service-connect-consumers#connection-type). If you configure private clusters, endpoints connecting to published services (`SERVICE_PRODUCERS`) must also be allowed. 
  11. **Optional:** Enable the Container File System API to allow faster workstation startup. 

[Enable the Container File System API](https://console.cloud.google.com/apis/library/containerfilesystem.googleapis.com?q=container%20file%20system)

For more information, see [Reduce workstation startup time with Image streaming](https://docs.cloud.google.com/workstations/docs/architecture#image-streaming). 




## Create your workstation cluster

Workstation clusters define a group of workstations in a particular region, manage workstations during their lifecycle, and provide configurable network connectivity.

Workstation clusters aren't related to Google Kubernetes Engine (GKE) clusters.

To create a workstation cluster, follow these steps:

  1. In the console, navigate to the **Cloud Workstations** > **Cluster management** page. 

[Go to Cluster management](https://console.cloud.google.com/workstations/clusters)

  2. From the workstations **Cluster management** page, click add_box**Create**.

  3. In the **Name** field, enter a name for your workstation cluster.

  4. Select the **Region** that is closest to you.

  5. Optional: Enter a different **Workstation authorization URL** to use a custom authentication flow. Cloud Workstations redirects unauthenticated users to this URL to sign in.

  6. Optional: To create your workstations inside a [VPC](https://docs.cloud.google.com/vpc/docs/vpc), expand the **Network settings** section and select your custom network.

     1. In the **Network** field, enter the name for your network—for example, `test-network`.

     2. In the **Subnetwork** field, enter the name for your subnetwork—for example, `test-subnetwork`.

     3. In the **Gateway type** section, select **Public gateway** or **Private gateway**.

        * To make your workstations accessible from public networks, select **Public gateway**. 

        * If you require [data residency](https://docs.cloud.google.com/assured-workloads/docs/data-residency) for data in transit, select **Private gateway**.

        * To allow ingress and egress to the workstations service from inside the selected network, select **Private gateway**. For more information about creating a private clusters, see [Configure VPC Service Controls and private clusters](https://docs.cloud.google.com/workstations/docs/configure-vpc-service-controls-private-clusters)

  7. Optional: The **Workstation launcher URL** is populated with the default Google Cloud console launcher, which [automatically starts stopped workstations](https://docs.cloud.google.com/workstations/docs/automatically-restart-stopped-workstations). If you want to use a custom launcher, replace this URL with your custom page.

To reset a custom URL back to the default, click **Use Cloud Console launcher**.

  8. Click **Create** , which begins the cluster creation process.




Workstation cluster creation is generally only needed once. 

## Clean up

To delete a workstation cluster from the Google Cloud console:

  1. In the Google Cloud console, go to **Cloud Workstations > Clusters**.
  2. Select the checkbox beside the cluster that you want to delete.
  3. Click themore_vert**More** options menu and select **Delete** to delete the selected workstation cluster. 

For more about deleting workstations, workstation configurations, and Google Cloud projects, see [Delete resources](https://docs.cloud.google.com/workstations/docs/delete-resources). 

## What's next

  * Learn more about configuring options in your [workstation configuration](https://docs.cloud.google.com/workstations/docs/create-configuration).

  * Use the [Cloud Workstations base editor](https://docs.cloud.google.com/workstations/docs/base-editor-overview).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
