---
url: https://docs.cloud.google.com/alloydb/docs/create-free-trial-cluster/
title: Create a free trial cluster \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:43:44.851001+00:00
---

# Create a free trial cluster  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/create-free-trial-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Create a free trial cluster Stay organized with collections  Save and categorize content based on your preferences. 

This page guides you through the process of creating and managing an AlloyDB free trial cluster.

For more information about AlloyDB free trial clusters, see [AlloyDB free trial clusters overview](https://docs.cloud.google.com/alloydb/docs/free-trial-cluster).

## Before your begin

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




You are not charged for free trial clusters and instance resources, but you are charged for data transfer costs for connections outside the region, through the public internet, and for taking and storing your final backup. For more information, see [Trial inclusions and conditions](https://docs.cloud.google.com/alloydb/docs/free-trial-cluster#trial-inclusion").

## Create a free trial cluster

### Console

When you create a free trial cluster, a primary instance is automatically created.

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click **Create Free Cluster**.

  3. In the **Cluster ID** field of the **Basic info** section, enter a name for the cluster—for example, `my-trial-cluster`.

  4. In the **Password** field, enter a password you'd like. This password is used to connect to the default database.

  5. In the **Region** field of the **Location** section, select a region—for example, `us-central1 (Iowa)`.

  6. In the **Database version** field, keep the default value.

  7. Under **Networking** , select `default`.

If you have not set up private services access yet, a dialog labeled **Private service access connection required** appears.

In the **Private service access connection required** dialog, to create private services access connection, complete the following:

     1. Click **Set up connection**.

A new pane labeled **Enable Service Networking API** appears.

     2. In the pane, select **Use an automatically allocated IP range**.

     3. Click **Continue**.

     4. Click **Create connection** , and wait for the connection configuration to finish.

The **Enable Service Networking API** pane is removed.

  8. Click **Create Free Cluster**.




After you create the free trial cluster, you are redirected to the **Overview** page. You can view your primary instance in the **Instances in your cluster** section, and other information about your cluster, such as days left on trial.

**Note:** If a primary instance doesn't get created when you create a free trial cluster, then don't delete the cluster, and try [creating a primary instance](https://docs.cloud.google.com/alloydb/docs/instance-primary-create#procedure) manually.

### gcloud

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

To create an AlloyDB cluster using private services access, you must [enable private services access](https://docs.cloud.google.com/alloydb/docs/configure-connectivity).

Use the [`gcloud alloydb clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/clusters/create) and [`gcloud alloydb instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/create) command to create a cluster and primary instance respectively.
    
    
    gcloud alloydb clusters create CLUSTER_ID \
        --password=PASSWORD \
        --region=REGION_ID \
        --subscription-type=TRIAL
    gcloud alloydb instances create INSTANCE_ID \
        --instance-type=PRIMARY \ 
        --cpu-count=8 \
        --region=REGION_ID \
        --cluster=CLUSTER_ID \

Replace the following:

  * `CLUSTER_ID`: the ID of the cluster that you are creating. It must begin with a lowercase letter and can contain lowercase letters, numbers, and hyphens.

  * `PASSWORD`: the password to use for the default `postgres` user.

  * `REGION_ID`: the region where you want the cluster placed.

  * `CLUSTER_ID`: The ID of the free trial cluster where you want the instance placed.




## Add a read pool instance

You can add a single read pool instance of 8 vCPU compute capacity in a free trial cluster.

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click the free trial cluster in the **Resource Name** column.

  3. Go to the **Instances in your cluster** section, and click **Add read pool**.

  4. Configure your read pool instance:

     1. In the **Read pool instance ID** field, enter an ID for the read pool instance.

     2. In the **Node count** field, the node count value is auto-set to `1` for a pool instance in a free trial cluster. This value cannot be changed.

     3. Click **Create read pool**.




## Optional: Import your SQL file

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can import your SQL file that contains a logical backup of a PostgreSQL database to the free trial cluster.

Before you begin, do the following:

  * Upload your SQL file to a Cloud Storage bucket. For more information, see [Import a SQL file](https://docs.cloud.google.com/alloydb/docs/import-sql-file).

    * Grant the [AlloyDB service account permissions to the Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions#bucket-add) for the import operation.

The format of the service account is as follows:
          
          service-PROJECT_NUMBER@gcp-sa-alloydb.iam.gserviceaccount.com
          

Replace `PROJECT_NUMBER` with your project number—for example, `212340152241`.

    * Ensure that the service account is granted the Storage Object Viewer (`roles/storage.objectViewer`) role.

  * Ensure that you are granted the AlloyDB Admin (`roles/alloydb.admin`) role. For custom roles, add the `alloydb.clusters.import` permission to the role.

  * (Optional). If you don't want to use the default database, [connect to your instance and create a database](https://docs.cloud.google.com/alloydb/docs/database-create).




To import your SQL file into an AlloyDB database, complete the following steps:

  1. Go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click the free trial cluster in the **Resource Name** column.

  3. In the **Overview** page, expand the **Get the most out of your free cluster** menu.

  4. Click the **Import data into AlloyDB** step, and then click **Import Data**.

  5. In the **Choose the file you'd like to import data from** section, enter the path to the bucket and SQL file to use for the import, or browse to an existing file.

The SQL file is a file with a sequence of SQL commands, like the output of the `pg_dump` utility.

  6. In the **Destination** section, select the database you want the data to be imported into.

  7. Select a database user in the **User** list.

  8. In the **Password** field, enter the password set for your database.

**Note:** If you want to use the default database, then select the `postgres` user and enter the password you set when the free trial cluster was created.
  9. Click **Import** to start the import.




## Upgrade a free trial cluster

You can upgrade your free trial cluster anytime during your 30-day free trial period.

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

     1. Click the free trial cluster you created earlier in the **Resource Name** column.

     2. In the **Overview** page, click **Upgrade now** in the **Days left on trial** field.

     3. In the **Machine type** field of the **Machine** section, select the machine type you want to upgrade to.

     4. To start the upgrade, click **Upgrade now**.

![Screenshot of the AlloyDB Overview page in the Google Cloud console, highlighting the Upgrade now button.](https://docs.cloud.google.com/static/alloydb/images/upgrade-free-trial-cluster.png)




After the upgrade completes, the **Overview** page no longer shows the days left on trial information, and any [limitations](https://docs.cloud.google.com/alloydb/docs/free-trial-cluster#trial-inclusion) that apply to the free trial cluster are removed.

## What's next

  * Learn about [creating and connecting to a database](https://docs.cloud.google.com/alloydb/docs/quickstart/create-and-connect).
  * Use [columnar engine to accelerate your analytical queries](https://docs.cloud.google.com/alloydb/docs/columnar-engine/about).
  * [Import your DMP file into an AlloyDB database](https://docs.cloud.google.com/alloydb/docs/import-dmp-file).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
