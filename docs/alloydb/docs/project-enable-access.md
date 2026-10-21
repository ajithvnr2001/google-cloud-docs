---
url: https://docs.cloud.google.com/alloydb/docs/project-enable-access/
title: Create and query an AlloyDB database using the Google Cloud console \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T02:22:05.282794+00:00
---

# Create and query an AlloyDB database using the Google Cloud console  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/project-enable-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create and query an AlloyDB database using the Google Cloud console

In AlloyDB for PostgreSQL, your databases are stored in _clusters_ that contain _instances_. In this quickstart, you set up a cluster, connect to its instance, and insert and query sample data. For more information about AlloyDB architecture, clusters, and instances, see [AlloyDB overview](https://docs.cloud.google.com/alloydb/docs/overview).

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

  5. Enable the Compute Engine, AlloyDB, Cloud Resource Manager, and Service Networking APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,alloydb.googleapis.com,cloudresourcemanager.googleapis.com,servicenetworking.googleapis.com)

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. Enable the Compute Engine, AlloyDB, Cloud Resource Manager, and Service Networking APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,alloydb.googleapis.com,cloudresourcemanager.googleapis.com,servicenetworking.googleapis.com)

The Service Networking API is required if you plan to configure network connectivity to AlloyDB using a VPC network that resides in the same Google Cloud project as AlloyDB. 

The Compute Engine API and Cloud Resource Manager API are required if you plan to configure network connectivity to AlloyDB using a VPC network that resides in a different Google Cloud project.

  10. [Choose how to connect to AlloyDB](https://docs.cloud.google.com/alloydb/docs/choose-alloydb-connectivity).



### Required roles

To get the permissions that you need to create and connect to an AlloyDB database, ask your administrator to grant you the following IAM roles on your project: 

  * [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)
  * [AlloyDB Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.admin) (`roles/alloydb.admin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to create and connect to an AlloyDB database. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create and connect to an AlloyDB database:

  * `compute.networks.list`
  * `compute.networks.addPeering`
  * `compute.addresses.create`
  * `servicenetworking.services.addPeering`
  * `alloydb.clusters.create`
  * `alloydb.instances.create`
  * `alloydb.instances.login`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a cluster and its primary AlloyDB instance

**Note:** To quickly set up a cluster, instance, and network for your development environment using a web interface, follow the steps in this [codelab](https://codelabs.developers.google.com/easy-alloydb-setup).

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click **Create cluster**.

  3. In **Configure your cluster** , follow these steps:

     1. In the **Cluster ID** field, enter `my-cluster`.

     2. Enter a password. Take note of this password because you use it in this quickstart.

     3. Retain the default database version.

     4. In the **Region** drop-down of **Location** , select the `us-central1 (Iowa)` region.

  4. In **Configure your primary instance** , follow these steps:

     1. In the **Instance ID** field, enter `my-cluster-primary`.

     2. In **Zonal availability** , click **Single zone**.

**Note:** While we don't recommend a single zone instance for production, you can use a single zone in this quickstart to minimize costs. For more information, see [Reduce costs using basic instances](https://docs.cloud.google.com/alloydb/docs/basic-instance).
     3. In the **Machine type** drop-down, select the `2 vCPU, 16 GB` machine type.

     4. In the **Network** drop-down of **Connectivity** , select the `default` network.

If you have a private access connection, continue to the creating a cluster step. Otherwise, click **Set up connection** and follow these steps:

        1. In **Allocate an IP range** , click **Use automatically assigned IP range**.

        2. Click **Continue** and then click **Create connection**.

     5. Retain the default settings under **Network security**.

  5. Click **Create cluster**. It might take several minutes for AlloyDB to create the cluster and display it on the primary cluster **Overview** page.




## Connect to your instance and create a database in AlloyDB Studio

**Note:** To connect a psql client to an instance, follow the steps in [Connect a psql client to an instance](https://docs.cloud.google.com/alloydb/docs/connect-psql).

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click the name of your cluster, `my-cluster`, in the **Resource name** column.

  3. In the navigation pane, click **AlloyDB Studio**.

  4. In the **Sign in to AlloyDB Studio** page, follow these steps:

     1. Choose a [database authentication method](https://docs.cloud.google.com/alloydb/docs/manage-data-using-studio#authentication).

     2. Select the `postgres` database.

     3. Click **Authenticate**. The **Explorer** pane displays a list of the objects in the `postgres` database.

  5. To create a database, enter the following statement in the **Editor 1** tab and then click **Run** :
         
         CREATE DATABASE guestbook;
         

You know your database is created when the `Statement executed successfully` message displays in the **Results** pane.




## Connect to the `guestbook` database

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click the name of your cluster, `my-cluster`, in the **Resource name** column.

  3. In the navigation pane, click **AlloyDB Studio**.

  4. In the **Sign in to AlloyDB Studio** page, follow these steps:

     1. Select the `guestbook` database.

     2. Select the `postgres` user.

     3. Enter the password you created in Create a cluster and its primary instance.

     4. Click **Authenticate**. The **Explorer** pane displays a list of the objects in the `guestbook` database.




## Verify your database connection

  1. Follow the steps in Connect to the `guestbook` database.

  2. To insert sample data into the `guestbook` database, enter the following in the **Editor 1** tab:
         
         CREATE TABLE entries (guestName VARCHAR(255),
                               content VARCHAR(255),
                               entryID SERIAL PRIMARY KEY);
         INSERT INTO entries (guestName, content) values ('Alex', 'I got here!');
         INSERT INTO entries (guestName, content) values ('Kai', 'Me too!');
         

  3. Click **Run**. The `Statement executed successfully` message in the **Results** pane indicates that data is inserted into your database.

  4. To remove text from the **Editor 1** tab so that you can run another command, click **Clear**.

  5. To select all entries in the database, enter the following query in the **Editor 1** tab:
         
         SELECT * FROM entries;
         

  6. Click **Run**. Output that is similar to following appears in the **Results** pane:
         
         guestname     | content     | entryid
             --------------+-------------+---------
             Alex          | I got here! | 1
             Kai           | Me too!     | 2
         




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click the name of your cluster, `my-cluster`, in the **Resource name** column.

  3. Click _delete_ **Delete cluster**.

  4. In **Delete cluster my-cluster** , enter `my-cluster` to confirm you want to delete your cluster.

  5. Click **Delete**.

  6. If you created a private connection when you created a cluster, go to the Google Cloud console [Networking page](https://console.cloud.google.com/networking/networks/details/default) and click **Delete VPC network**.




## What's next

  * Learn about other [ways to connect to AlloyDB](https://docs.cloud.google.com/alloydb/docs/choose-alloydb-connectivity).

  * [Enable project access to AlloyDB](https://docs.cloud.google.com/alloydb/docs/project-enable-access).

  * [Grant access to other users](https://docs.cloud.google.com/alloydb/docs/user-grant-access).

  * [Enable private services access](https://docs.cloud.google.com/alloydb/docs/configure-connectivity).

  * [Choose an AlloyDB machine type](https://docs.cloud.google.com/alloydb/docs/choose-machine-type).

  * [Create an AlloyDB cluster and its primary instance](https://docs.cloud.google.com/alloydb/docs/cluster-create).

  * [Learn about sizing recommendations](https://docs.cloud.google.com/alloydb/docs/use-sizing-recommendations).

  * [Connect a psql client to an instance](https://docs.cloud.google.com/alloydb/docs/connect-psql).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
