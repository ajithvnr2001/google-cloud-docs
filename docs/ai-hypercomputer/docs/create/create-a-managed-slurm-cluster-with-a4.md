---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-a-managed-slurm-cluster-with-a4/
title: Quickstart: Create a Slurm cluster \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:27:14.428773+00:00
---

# Quickstart: Create a Slurm cluster  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-a-managed-slurm-cluster-with-a4/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a fully managed Slurm cluster with two A4 VMs

This quickstart explains how to create and connect to a Slurm cluster by using Cluster Director. The cluster that you create uses two [A4 virtual machine (VM) instances](https://docs.cloud.google.com/compute/docs/gpus#b200-gpus), which are engineered to help your Slurm cluster efficiently handle large-scale model training and inference workloads.

**Important:** To complete this quickstart, you must have enough resources for creating two A4 VMs. To obtain these resources, you must either reserve resources for a future date and time, or create your A4 VMs as Flex-start VMs or Spot VMs. For more information, see [Choose a consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models).

[Cluster Director](https://docs.cloud.google.com/cluster-director/docs/overview) is a managed service that simplifies and automates cluster deployment, reducing operational overhead and letting you focus on running your workload. If you want more control over the deployment and management of your cluster, then [create a Slurm cluster by using Cluster Toolkit](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-a-slurm-cluster-with-a4).

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/?walkthrough_id=ai-hypercomputer--quickstart)

* * *

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

  6. Enable the Hypercompute Cluster API, Compute Engine API, Filestore API, Google Cloud Managed Lustre API, Cloud Logging API, and Cloud Monitoring API: 

[ Enable the APIs](https://console.cloud.google.com/apis/api/compute.googleapis.com/overview)
  7. Verify that your project and the Compute Engine default service account have the following Identity and Access Management (IAM) roles: 
     * To get the permissions that you need to complete this quickstart, ask your administrator to grant you the following IAM roles: 

       * To create and manage a cluster: [Cluster Director Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.editor) (`roles/hypercomputecluster.editor`) on your project 
       * To create and manage VMs in a cluster: [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) on your project 
       * To consume a single-project reservation: [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) on your project 
       * To consume a shared reservation: [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) on both the owner project and any consumer project where you want to consume the reservation 
       * To connect to the login node in a cluster: 
         * [Compute OS Login ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.osLogin) (`roles/compute.osLogin`) on your project
         * [IAP-Secured Tunnel User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.tunnelResourceAccessor) (`roles/iap.tunnelResourceAccessor`) on your project

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

     * To get the permissions that you need to complete this quickstart, ask your administrator to grant you the following IAM roles on the Compute Engine default service account: 

       * To create a cluster: [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) 
       * To manage resources in a cluster: 
         * [Logs Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter) (`roles/logging.logWriter`)
         * [Monitoring Metric Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.metricWriter) (`roles/monitoring.metricWriter`)
         * [Storage Object Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`)

  8. If the organization in which your project exists has a trusted image policy (`constraints/compute.trustedImageProjects`), then verify that the `clusterdirector-public-images` project is included in the list of allowed projects. To view the trusted image policies for your organization, see [Set image access constraints](https://docs.cloud.google.com/compute/docs/images/restricting-image-access#trusted_images).



## Costs

This quickstart uses the following billable Google Cloud resources:

  * **Compute Engine** :

    * Two VMs with A4 machine types

    * One Persistent Disk volume for the Slurm login node with 100 GB

    * One Google Cloud Hyperdisk Balanced volume with 100 GB for the A4 VMs

  * **Filestore** : a Filestore instance with 10 TiB (10,240 GiB)




To generate a cost estimate based on your projected usage, use the [pricing calculator](https://cloud.google.com/products/calculator).

## Create a Slurm cluster

To create a Slurm cluster, complete the following steps:

  1. In the Google Cloud console, go to the **Cluster Director** page.

[Go to Cluster Director](https://console.cloud.google.com/cluster-director/overview)

  2. Click add **Create a cluster**.

  3. In the dialog that appears, click **Step-by-step configuration**. The **Create cluster** page appears.

  4. In the **Cluster name** field, enter `cluster001`.

  5. In the **Compute** section, click **Configure resources**. In the **Add resource configuration** pane that appears, complete the following steps:

     1. In the **GPU type** list, select **NVIDIA B200 180GB**.

     2. In the **Number of instances** field, enter `2`.

     3. In the **Consumption options** section, select the consumption option that you want to use to obtain resources.

     4. In the **Location** section, specify the **Region** and **Zone** where you want to create your A4 VMs, or where the reservation that you want to use to create your VMs exists.

     5. Click **Done**.

  6. In the navigation menu, click **Storage**.

  7. In the **Storage** section, click edit **Edit storage configuration**. In the **Add storage configuration** pane that appears, complete the following steps:

     1. In the **Capacity** section, select **10-100 TiB, with increments of 2.5 TiB**.

     2. Click **Done**.

  8. Click **Create**. The **Clusters** page appears.

Creating the cluster can take some time to complete. The completion time depends on the number of VMs that you request and resource availability in the VMs' zone. If your requested resources are unavailable, then Cluster Director maintains the creation request until resources become available.




## View the cluster creation request

To review the cluster creation request, complete the following steps:

  1. In the **Clusters** table, in the **Name** column, click **cluster001**. A page that gives the details of the cluster appears, and the **Details** tab is selected.

  2. In the **Compute** section, locate the **Status** row. When AI Hypercomputer sets its value to **Ready** , you can proceed to the next section.




## Connect to your cluster through SSH

To connect to your cluster through SSH, complete the following steps:

  1. Click the **Nodes** tab.

  2. In the **Login nodes** table, find the row that contains the **cluster001-login-001** node. In that row, in the **Connect** column, click the **SSH** button. The **SSH-in-browser** window appears.

  3. If prompted, then click **Authorize**. Connecting to your cluster can take some time to complete. When the terminal is ready, proceed to the next section.

**Note:** If you encounter errors when connecting to your cluster, then see [Troubleshooting SSH errors](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-ssh-errors).



## Run sample jobs

In the **SSH-in-browser** window, complete the following steps:

  1. To verify that Slurm is running, run the following command:
         
         sinfo
         

  2. To submit a test job that returns the hostname of the node, run the following command:
         
         srun hostname
         

  3. To submit a batch job that sleeps for 30 seconds, run the following command:
         
         sbatch --wrap="sleep 30"
         

  4. To check the status of jobs in the queue, run the following command:
         
         squeue
         

  5. To view accounting data for jobs, run the following command:
         
         sacct
         




You've successfully created a Slurm cluster, connected to it, and run sample jobs. If AI Hypercomputer still hasn't created the A4 VMs, then you can wait for the cluster to create the VMs, modify the cluster to add or remove VMs, or delete the cluster to avoid incurring any unnecessary charges.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

### Delete your project

The easiest way to eliminate billing is to delete the project that you created for the tutorial. 

To delete the project: 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete your cluster

To delete the cluster, and its associated resources, that you created as part of this quickstart, complete the following steps:

  1. On the page that contains the details of your cluster, click delete **Delete**.

  2. In the dialog that appears, enter `cluster001`, and then click **Delete** to confirm.




## What's next

  * [Verify reservation consumption](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#verify-consumption)

  * [View cluster topology](https://docs.cloud.google.com/cluster-director/docs/monitor/view-topology)

  * [Modify a cluster](https://docs.cloud.google.com/cluster-director/docs/manage/modify-cluster)

  * [Manage cluster health](https://docs.cloud.google.com/cluster-director/docs/monitor/cluster-health)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
