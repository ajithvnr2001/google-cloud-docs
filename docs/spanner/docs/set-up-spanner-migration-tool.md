---
url: https://docs.cloud.google.com/spanner/docs/set-up-spanner-migration-tool/
title: Set up Spanner migration tool \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:32:37.690222+00:00
---

# Set up Spanner migration tool  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/set-up-spanner-migration-tool/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Set up Spanner migration tool Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to install and run the Spanner migration tool (SMT) on Cloud Shell. For more information about SMT, see [Spanner migration tool](https://googlecloudplatform.github.io/spanner-migration-tool/).

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

  6. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 
  7. To initialize the Google Cloud CLI, run the `gcloud init` command. 



## Install Spanner migration tool

You can install SMT using a Linux shell command or Google Cloud CLI:

### Linux shell

To install SMT, run the following command:
    
    
      sudo apt-get install google-cloud-sdk-spanner-migration-tool
    

###  gcloud 

You can install SMT by using the [`gcloud components install`](https://docs.cloud.google.com/sdk/gcloud/reference/components/install) command:
    
    
      gcloud components install spanner-migration-tool
    

For more information on installing SMT, see [Installing Spanner migration tool](https://googlecloudplatform.github.io/spanner-migration-tool/install.html#installing-spanner-migration-tool).

## Access Spanner migration tool

You can use the [`gcloud alpha spanner migrate`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/spanner/migrate) command to access and use SMT.

To launch the SMT web UI, you can run the following command:
    
    
      gcloud alpha spanner migrate web
    

You need to provide your Google Cloud credentials to allow SMT to access resources. Click `http://localhost:8080` on the response to the previous command to open the web UI.

**Note:** Keep the Google Cloud CLI tab open while you view the SMT web UI.

## Connect to Spanner

To connect to Spanner using the SMT web UI, do the following:

  1. Click the edit button to configure the connection to Spanner.

  2. Specify the following information to connect to Spanner:

     * **Project ID** : the project ID where your Spanner instance is.
     * **Instance ID** : the Spanner instance ID.
  3. Click **Save**.




## Connect to your source database

You need to connect to the source database using the SMT web UI by providing the following information:

  * **Database Engine** : specify whether your source database is MySQL, SQL Server, Oracle, or PostgreSQL.
  * **Hostname** : the IP address of your source database.
  * **Port** : the port where your source database is accessible.
  * **User name** : the username of the source database.
  * **Password** : the password of the source database.
  * **Spanner Dialect** : specify whether you want to use [GoogleSQL](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/overview) or [PostgreSQL](https://docs.cloud.google.com/spanner/docs/reference/postgresql/overview).



After entering the information you can connect to the source database by clicking **Test Connection** , and then clicking **Connect**.

## What's next?

  * [Migrate schema from MySQL](https://docs.cloud.google.com/spanner/docs/migrate-mysql-schema).
  * [Use Spanner migration tool for MySQL schema migration](https://docs.cloud.google.com/spanner/docs/migrate-mysql-schema).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
