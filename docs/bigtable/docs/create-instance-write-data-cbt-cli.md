---
url: https://docs.cloud.google.com/bigtable/docs/create-instance-write-data-cbt-cli/
title: Quickstart: Create an instance and write data with the cbt CLI \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:22.233017+00:00
---

# Quickstart: Create an instance and write data with the cbt CLI  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/create-instance-write-data-cbt-cli/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create an instance and write data with the cbt CLI

If you're learning about Bigtable, you can work through a quickstart to get a taste of the fundamentals that you would use at scale in a production environment.

In this quickstart, you perform the following actions:

  * Connect to a Bigtable instance.
  * Perform basic administrative tasks.
  * Write data to a table.
  * Read data from a table.



## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Cloud Bigtable and Cloud Bigtable Admin APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable bigtable.googleapis.com bigtableadmin.googleapis.com

  8. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/bigtable.admin`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  13. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  14. Enable the Cloud Bigtable and Cloud Bigtable Admin APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable bigtable.googleapis.com bigtableadmin.googleapis.com

  15. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/bigtable.admin`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.

  16. Run the following command to install the `cbt` CLI : 
         
         gcloud components install cbt




## Create a Bigtable instance

  1. Open the **Create instance** page in the Google Cloud console.

[Create an instance](https://console.cloud.google.com/bigtable/create-instance)

  2. For **Instance name** , enter `Quickstart instance`.

  3. For **Instance ID** , enter `quickstart-instance`.

  4. Click **Continue**.

  5. For **Storage type** , select **SSD**.

  6. Click **Continue**.

  7. For **Cluster ID** , enter `quickstart-instance-c1`.

  8. For **Region** , select a region near you.

  9. For **Zone** , select **Any**.

  10. For **Node scaling mode** , choose **Manual allocation**.

  11. For **Quantity** , select **1**.

  12. Click **Create** to create the instance.




## Connect to your instance

  1. Configure the `cbt` CLI to use your project and instance by creating a `.cbtrc` file, replacing `PROJECT_ID` with the ID for the project where you created your Bigtable instance:
         
         echo project = PROJECT_ID >> ~/.cbtrc && echo instance = quickstart-instance >> ~/.cbtrc
         

  2. Verify that you set up the `.cbtrc` file correctly:
         
         cat ~/.cbtrc

The terminal displays the contents of the `.cbtrc` file, which looks similar to the following:
         
         project = PROJECT_ID
         instance = quickstart-instance

Now you can use the `cbt` CLI with your instance.




## Read and write data

Bigtable stores data in _tables_ , which contain _rows_. Each row is identified by a _row key_.

Data in a row is organized into _column families_ , which are groups of columns. A _column qualifier_ identifies a single column within a column family.

There can be multiple time-stamped cells at the intersection of a row and column.

  1. Create a table named `my-table`.
         
         cbt createtable my-table

  2. List your tables:
         
         cbt ls

The command displays output similar to the following:
         
         my-table

  3. Add one column family named `cf1`:
         
         cbt createfamily my-table cf1

  4. List your column families:
         
         cbt ls my-table

The command displays output similar to the following:
         
         Family Name     GC Policy
             -----------     ---------
             cf1             <never>

  5. Write the values `test-value1` and `test-value2` to the row `r1`, using the column family `cf1` and the column qualifier `c1`:
         
         cbt set my-table r1 cf1:c1=test-value1
           cbt set my-table r1 cf1:c1=test-value2
         

  6. Use the `cbt read` command to read the data you added to the table:
         
         cbt read my-table

The shell displays output similar to the following:
         
         ----------------------------------------
             r1
               cf1:c1                                   @ 2023/03/22-06:56:11.323000
                 "test-value1"
               cf1:c1                                   @ 2023/03/22-06:56:04.361000
                 "test-value2"

Two timestamped values are stored for the same column in row `r1`.

**Note:** In this quickstart you set only two cells, but Bigtable lets you set up to 10,000 cells in a single write request.



## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this quickstart, delete the instance. Deleting the `.cbtrc` file leaves you ready to work on a different project.

  1. Delete the table `my-table`:
         
         cbt deletetable my-table

  2. Delete the instance:
         
         cbt deleteinstance quickstart-instance

  3. Delete the `.cbtrc` file: 
         
         rm ~/.cbtrc

  4. Optional: Revoke credentials from the gcloud CLI:
         
         gcloud auth revoke




## What's next

  * Work through a [Bigtable codelab](https://codelabs.developers.google.com/codelabs/cloud-bigtable-intro-java/index.html).
  * View the [ `cbt` CLI reference documentation](https://docs.cloud.google.com/bigtable/docs/cbt-reference).
  * See sample source code for a [fraud detection use case](https://github.com/GoogleCloudPlatform/java-docs-samples/tree/main/bigtable/use-cases/fraudDetection).
  * Write a Hello World application in [C#](https://docs.cloud.google.com/bigtable/docs/samples-c-sharp-hello), [C++](https://docs.cloud.google.com/bigtable/docs/samples-cpp-hello), [Go](https://docs.cloud.google.com/bigtable/docs/samples-go-hello), [Java](https://docs.cloud.google.com/bigtable/docs/samples-java-hello-world), [Node.js](https://docs.cloud.google.com/bigtable/docs/samples-nodejs-hello), [PHP](https://docs.cloud.google.com/bigtable/docs/samples-php-hello), [Python](https://docs.cloud.google.com/bigtable/docs/samples-python-hello), [Ruby](https://docs.cloud.google.com/bigtable/docs/samples-ruby-hello), or using the [HBase client for Java](https://docs.cloud.google.com/bigtable/docs/samples-hbase-java-hello).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
