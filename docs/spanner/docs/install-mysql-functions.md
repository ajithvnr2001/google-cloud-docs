---
url: https://docs.cloud.google.com/spanner/docs/install-mysql-functions/
title: Install MySQL user-defined functions \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:54.079247+00:00
---

# Install MySQL user-defined functions  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/install-mysql-functions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Install MySQL user-defined functions Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to install a predefined library of MySQL functions in a Spanner database. You can add these functions to your database using the Google Cloud console or the Google Cloud CLI.

Installing these MySQL functions extends Spanner's capabilities, allowing you to perform operations that are common in MySQL environments directly within Spanner.

For more information about the MySQL functions that Spanner supports, see [MySQL functions](https://docs.cloud.google.com/spanner/docs/reference/mysql/user_defined_functions_all).

## Required roles

To get the permissions that you need to install the MySQL functions, ask your administrator to grant you the [Cloud Spanner Database Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.databaseAdmin) (`roles/spanner.databaseAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Install the MySQL user-defined functions

You can install the MySQL user-defined functions in a Spanner database in the following ways:

###  Google Cloud console 

  1. In the Google Cloud console, go to the Spanner **Instances** page.

[Go to the Instances page](https://console.cloud.google.com/spanner/instances)

  2. Click the instance containing the database.

  3. Click the database.

  4. Click the **Write DDL** button to open Spanner Studio.

  5. Copy the entire content of the DDL file in the [`mysql_udfs.sql`](https://github.com/googleapis/spanner-sql-udf/blob/main/mysql/mysql_udfs.sql) file.

  6. In a SQL editor tab, paste the copied content from the DDL file,

  7. Click **Run**.




###  gcloud 

You can use the [`gcloud spanner database ddl update`](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/databases/ddl/update) command to install the MySQL UDFs.

Before using any of the command data below, make the following replacements: 

  * DATABASE_ID: the ID of the database to add the MySQL UDFs.
  * INSTANCE_ID: the ID of the instance where the database is located.
  * DDL_FILE_PATH: path to a file containing all the `CREATE OR REPLACE FUNCTION` statements in the [mysql_udfs.sql](https://github.com/googleapis/spanner-sql-udf/blob/main/mysql/mysql_udfs.sql) file. 



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud spanner databases ddl update DATABASE_ID \
    --instance=INSTANCE_ID \
    --ddl-file=DDL_FILE_PATH

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud spanner databases ddl update DATABASE_ID `
    --instance=INSTANCE_ID `
    --ddl-file=DDL_FILE_PATH

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud spanner databases ddl update DATABASE_ID ^
    --instance=INSTANCE_ID ^
    --ddl-file=DDL_FILE_PATH

## What's next

  * Learn about all the Spanner supported [MySQL user-defined functions](https://docs.cloud.google.com/spanner/docs/reference/mysql/user_defined_functions_all).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
