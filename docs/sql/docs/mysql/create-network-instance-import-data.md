---
url: https://docs.cloud.google.com/sql/docs/mysql/create-network-instance-import-data/
title: Create an instance in a private network and then import a database \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:30:16.216851+00:00
---

# Create an instance in a private network and then import a database  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/create-network-instance-import-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Create an instance in a private network and then import a database Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/create-network-instance-import-data "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/create-network-instance-import-data "View this page for the SQL Server database engine")

Migrating a workload from another platform to Cloud SQL for MySQL often involves using the Google Cloud console to import data from a SQL dump file that you export from your previous environment.

This tutorial shows you how to create the Google Cloud resources that you need and then import a SQL database to a Cloud SQL for MySQL instance. The tutorial demonstrates best practices when migrating to Cloud SQL for MySQL, including the use of a Virtual Private Cloud (VPC) network with private services access and enabling private IP for your Cloud SQL instance.

As you work through the steps, retain the default values for settings unless otherwise specified.

## Objectives

  1. Download a sample SQL dump file.
  2. Create a new Virtual Private Cloud network with private services access.
  3. Create a Cloud Storage bucket and upload a SQL dump file to it.
  4. Create a Cloud SQL for MySQL instance configured for private IP. 
  5. Create a user. 
  6. Import from the dump file to a new database.
  7. Verify that the database was successfully imported by viewing the structure and running a query.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Cloud SQL for MySQL](https://cloud.google.com/sql/pricing#mysql-and-postgresql-pricing)
  * [Virtual Private Cloud](https://cloud.google.com/vpc/pricing)
  * [Cloud Storage](https://cloud.google.com/storage/pricing-examples#cloud-storage-pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

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

  5. Enable the Cloud SQL, Cloud SQL Admin, Compute Engine, Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=sql-component.googleapis.com,sqladmin.googleapis.com,compute.googleapis.com,storage.googleapis.com)

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. Enable the Cloud SQL, Cloud SQL Admin, Compute Engine, Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=sql-component.googleapis.com,sqladmin.googleapis.com,compute.googleapis.com,storage.googleapis.com)




### Required roles

To get the permissions that you need to complete this tutorial, ask your administrator to grant you the following IAM roles on your project: 

  * [Cloud SQL Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) (`roles/cloudsql.admin`)
  * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)
  * [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Obtain a sample database dump file

For this tutorial, you'll use a small sample database that contains country codes and world capitals.

Download the SQL file for the `countries` database to your local environment: [`countries-mysql.sql`](https://docs.cloud.google.com/static/sql/files/countries-mysql.sql).

## Create a network with private services access

Before you create the rest of your resources, create a VPC network to run your services on. _Private services access_ lets you restrict access to your Cloud SQL database by establishing a private connection between your external network and Cloud SQL for MySQL using internal IPv4 addresses.

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to the VPC networks page](https://console.cloud.google.com/networking/networks/list)

  2. Click **Create VPC network**.

  3. In the name field, enter `tutorial-network`.

  4. For **Subnet creation mode** , select **Custom**.

  5. In the name field, enter `tutorial-subnet`.

  6. Select a region near you.

  7. For **IPv4 range** , enter `10.0.0.0/24`.

  8. For **Private Google Access** , select **On**.

  9. Click **Done**.

  10. At the bottom of the page, click **Create**.




After the VPC network creation process finishes, you can configure private services access for the network.

  1. On the VPC networks screen, click **tutorial-network**.
  2. In the menu bar for **tutorial-network** , click **Private services access**.
  3. Click **Allocated IP ranges for services**.
  4. Click **Allocate IP range**.
  5. For Name, enter `tutorial-range`.
  6. For **IP address range** , select **Custom**.
  7. In the **Range** field, enter `192.168.0.0/20`.
  8. Click **Allocate**.
  9. In the submenu, click **Private connections to services**.
  10. Click **Create connection**.
  11. In the **Assigned allocation** drop-down, select **tutorial-range**.
  12. Click **Connect**. In a minute or two, the Google Cloud console displays a message letting you know that you have successfully created a private connection.



## Create a Cloud Storage bucket

Next, create a Cloud Storage bucket to store the SQL dump file that you downloaded earlier. The Cloud SQL import tool expects the dump file to be in a bucket. A Cloud Storage bucket must have a globally unique name.

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click **Create**.
  3. For the bucket name, create a globally unique name consisting of lowercase letters, numbers, and hyphens. You might want to use a random string generator, such as [random.org/strings](http://random.org/strings) to generate the name. Note the name that you choose.
  4. Click **Continue**.
  5. Under **Location type** , select **Region**. This is the lowest-cost option.
  6. Choose the same region you chose for your subnet. Locating your Google Cloud resources in the same region reduces latency, improves speed, lowers data transfer costs, and simplifies networking.
  7. Click **Continue**.
  8. Click **Create**.
  9. If prompted with a dialog, leave **Enforce public access prevention on this bucket** selected, and click **Confirm**.



The **Bucket details** page for the new bucket opens with the **Objects** pane selected.

## Upload your dump file to the bucket

Upload to your bucket the sample SQL dump file that you downloaded earlier.

  1. On the **Objects** tab, click **Upload** and then click **Upload files**.
  2. Navigate to and select the `countries-mysql.sql` file.
  3. Click **Open**. Cloud Storage uploads the dump file to the bucket.



## Create a Cloud SQL instance

Create a Cloud SQL instance in the Google Cloud console using the following settings. For all other settings, keep the default. Although you don't need to enable private IP for the import process, using private IP for a production workload is a best practice.

  1. Go to the Cloud SQL Instances page in the Google Cloud console.  
[Go to the Cloud SQL Instances page](https://console.cloud.google.com/sql/instances)
  2. Click **Create Instance**.
  3. Click **Choose MySQL**.
  4. For **Choose a Cloud SQL edition** , choose **Enterprise**.
  5. For **Edition preset** , select **Sandbox**.
  6. For **Instance ID** , enter `tutorial-instance`.
  7. Choose and enter a password for the default user account and save it for future use.
  8. Choose the same region that you chose for your subnet and bucket.
  9. For **Zonal availability** , select **Single zone**.
  10. Expand **Show configuration options**.
  11. Expand **Connections**.
  12. Clear **Public IP**.
  13. Select **Private IP**.
  14. From the **Network** drop-down, select **tutorial-network**. This places the new Cloud SQL instance in the private network that you created earlier.
  15. Click **Create instance** , and then wait until the instance initializes and starts. The initialization process can take more than five minutes.

**Tip:** You can monitor the status of Google Cloud console operations, including your instance-creation operation, in the _long-running operation drawer_ at the bottom of the Google Cloud console.

## Add a user

Before you can read or write to a database, you must create a database user that is different from the root user.

  1. In the SQL navigation menu, click **Users**.
  2. Click **Add user account**.
  3. In the pane that opens, select **Built-in authentication**.
  4. In the **User name** field, enter `tutorial-user`.
  5. Enter a password for the new user. Save this password for future use. 
  6. Select **Allow any host**. 
  7. Click **Add**.



## Import from the dump file

Now you're ready to import the `countries` database using the `countries-mysql.sql` dump file that you uploaded to your Cloud Storage bucket.

  1. In the SQL navigation menu, click **Overview**.
  2. On the overview page, click **Import**.
  3. Under **File format** , select **SQL**.
  4. Under **Select source file** , choose **Select file from Google Cloud Storage**.
  5. Click **Browse**.
  6. Expand the storage bucket that you created earlier.
  7. Click **countries-mysql.sql**.
  8. Click **Select**. 
  9. Confirm that for the **Database** field in the **Destination** section, **Specified in SQL file** is selected. 
  10. Click **Import**.



When the import process is complete and the `countries` database has been imported to Cloud SQL for MySQL, a success message is displayed.

## Validate the imported data in Cloud SQL for MySQL

After the import operation is complete, you can verify that the database was imported by connecting to it using Cloud SQL Studio, inspecting the list of tables, and running a test query against the data.

### Authenticate to Cloud SQL Studio

With the user account that you created earlier, connect to the new database using Cloud SQL Studio.

  1. In the SQL navigation menu, click **Cloud SQL Studio**. A login dialog is displayed.
  2. In the **Database** drop-down, choose **countries**.
  3. Select **Built-in database authentication**. 
  4. In the **User** drop-down, select **tutorial-user**.
  5. In the **Password** field, enter the password that you chose for the user in the Add a user section. 
  6. Click **Authenticate**. Cloud SQL Studio opens.



### View and query the tables

  1. In the **Explorer** pane, examine the `countries` database and confirm that the database has two tables: `capitals` and `country_codes`.
  2. Click **Untitled Query** to open the query editor.
  3. Paste the following code into the query editor:
         
         SELECT
           `capitals`.`country_capital`,
           `country_codes`.`country_name`
         FROM
           `capitals`
         JOIN
           `country_codes`
         ON
           `capitals`.`alpha_2_code` = `country_codes`.`alpha_2_code`
         ORDER BY
           `capitals`.`country_capital`;
         

  4. Click **Run**.




The results pane displays an alphabetical list of world capitals and their countries.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, do one of the following:

  * Delete the project that contains the resources
  * Keep the project and delete the individual resources.



### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




### Delete individual resources

If you want to keep the project but avoid incurring charges, delete the Cloud SQL instance, Cloud Storage bucket, and VPC network that you created during the tutorial.

#### Delete the Cloud SQL instance

First, disable deletion protection and then delete the tutorial Cloud SQL instance:

  1. In the SQL navigation menu, click **Overview**.
  2. Click **Edit**.
  3. Expand the **Data Protection** section.
  4. In **Instance deletion protection** , deselect all options.
  5. Click **Save**. When the operation is complete, **Delete** is selectable.
  6. Click **Delete**. A dialog appears.
  7. In the **Instance ID** field, enter `tutorial-instance`.
  8. Click **Delete**.



#### Delete the Cloud Storage bucket

Next, delete the storage bucket and its contents.

  1. In the main Google Cloud console navigation menu, go to **Cloud Storage** > **Buckets**.
  2. Select the box next to the name of the bucket you created earlier.
  3. Click delete **Delete**.
  4. In the dialog, confirm deletion by typing `DELETE`, and then click **Delete**.



#### Delete the VPC network

Now that you've deleted the resources in your VPC network, you are ready to delete the network. Before you can delete the VPC network, you must delete the peering connection that was created automatically when you created the VPC network.

  1. In the main navigation menu, go to **VPC networks** > **VPC network peering**.
  2. Select the box next to the peering connection with the VPC network **tutorial-network**.
  3. Click **Delete**.
  4. In the dialog, confirm by clicking **Delete**.



Now that the peering connection has been removed, you can delete the VPC network.

  1. In the **VPC Network** menu, click **VPC networks**.
  2. Click **tutorial-network** to open the details page.
  3. Click delete **Delete VPC network**.
  4. In the dialog, confirm deletion by typing `tutorial-network` and then clicking **Delete**.



## What's next

  * [Best practices for importing and exporting data](https://docs.cloud.google.com/sql/docs/mysql/import-export).
  * [Export and import using SQL dump files](https://docs.cloud.google.com/sql/docs/mysql/import-export/import-export-sql).
  * [VPC networks](https://docs.cloud.google.com/vpc/docs/vpc)
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
