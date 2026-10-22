---
url: https://docs.cloud.google.com/cluster-director/docs/create/quickstart/
title: Quickstart: Create a Slurm cluster \u00a0|\u00a0 Cluster Director \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:42:01.335195+00:00
---

# Quickstart: Create a Slurm cluster  |  Cluster Director  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-director/docs/create/quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Director ](https://docs.cloud.google.com/cluster-director/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-director/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a Slurm cluster

This quickstart shows you how to create and connect to a Slurm cluster in Cluster Director.

To test cluster management without reserving capacity, the cluster that you create in this quickstart uses three N2 virtual machine (VM) instances. One VM is for the login node, and two VMs are for compute nodes. After Cluster Director creates the login node, you connect to the node and run sample jobs by using Slurm commands.

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/?walkthrough_id=cluster-director--quickstart)

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
     * To get the permissions that you need to complete this quickstart, ask your administrator to grant you the following IAM roles on your project: 

       * To create and manage a cluster: [Cluster Director Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.editor) (`roles/hypercomputecluster.editor`) 
       * To create and manage VMs in a cluster: [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) 
       * To connect to the login node in a cluster: 
         * [Compute OS Login ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.osLogin) (`roles/compute.osLogin`)
         * [IAP-Secured Tunnel User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.tunnelResourceAccessor) (`roles/iap.tunnelResourceAccessor`)

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

  * **Compute Engine** : three VMs that use the `n2-standard-2` machine type, which has 2 vCPUs and 8 GB of memory.

  * **Filestore** : a Filestore instance with a capacity of 1 TiB, which is the default storage resource for the `/home` directory in Cluster Director.




To generate a cost estimate based on your projected usage, use the [pricing calculator](https://cloud.google.com/products/calculator).

## Create a Slurm cluster

To create a Slurm cluster, complete the following steps:

  1. In the Google Cloud console, go to the **Cluster Director** page.

[Go to Cluster Director](https://console.cloud.google.com/cluster-director/overview)

  2. Click add **Create a cluster**.

  3. In the dialog that appears, click **Step-by-step configuration**. The **Create cluster** page appears.

  4. In the **Cluster name** field, enter `cluster000`.

  5. In the **Compute** section, click **Configure resources**. In the **Add resource configuration** pane that appears, complete the following steps:

     1. In the **Machine configuration** section, click **General purpose**.

     2. In the **Number of instances** field, enter `2`.

     3. In the **Location** section, specify the following options:

        * For **Region** , select **us-central1**.

        * For **Zone** , select **us-central1-a**.

     4. Click **Done**.

  6. Click **Create**. The **Clusters** page appears.

Creating the cluster can take some time to complete. The completion time depends on the number of VMs that you request and resource availability in the VMs' zone. If your requested resources are unavailable, then Cluster Director maintains the creation request until resources become available.




## View the cluster creation request

To review the cluster creation request, complete the following steps:

  1. In the **Clusters** table, in the **Name** column, click **cluster000**. A page that gives the details of the cluster appears, and the **Details** tab is selected.

  2. In the **Compute** section, locate the **Status** row. When Cluster Director sets its value to **Ready** , you can proceed to the next section.




## Connect to your cluster by using SSH

To connect to your cluster by using SSH, complete the following steps:

  1. Click the **Nodes** tab.

  2. In the **Login nodes** table, find the row that contains the **cluster000-login-001** node. In that row, in the **Connect** column, click the **SSH** button. The **SSH-in-browser** window appears.

  3. If prompted, then click **Authorize**. Connecting to your cluster can take some time to complete. When the terminal is ready, proceed to the next section.

**Note:** If you encounter errors when connecting to your cluster, then see [Troubleshooting SSH errors](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-ssh-errors).



## Run sample jobs

In the **SSH-in-browser** window, complete the following steps:

  1. To verify that Slurm is running, run the following command:
         
         sinfo
         

  2. To submit a test job that returns the hostname of the node, run the following command:
         
         srun hostname
         

  3. To submit a batch job that sleeps for 10 seconds, run the following command:
         
         sbatch --wrap="sleep 10"
         

  4. To check the status of jobs in the queue, run the following command:
         
         squeue
         

  5. To view accounting data for jobs, run the following command:
         
         sacct
         




You've successfully created a Slurm cluster, connected to the login node, and run sample jobs!

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

To delete your Slurm cluster and its associated resources, complete the following steps:

  1. On the page that contains the details of your cluster, click delete **Delete**.

  2. In the dialog that appears, enter `cluster000`, and then click **Delete** to confirm.




## What's next

  * [Choose a consumption option](https://docs.cloud.google.com/cluster-director/docs/choose-consumption-option)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
