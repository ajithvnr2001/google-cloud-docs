---
url: https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-conversion-workspace/
title: Create a conversion workspace and convert schema \u00a0|\u00a0 Database Migration Service for heterogeneous Oracle to Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:40.679460+00:00
---

# Create a conversion workspace and convert schema  |  Database Migration Service for heterogeneous Oracle to Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-conversion-workspace/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Oracle to PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/scenario-overview)



Send feedback 

#  Create a conversion workspace and convert schema Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to create a conversion workspace and use it to immediately perform deterministic code and schema conversion from Oracle to PostgreSQL. Before you create the workspace, make sure that you [ create a connection profile for your source database](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-source-connection-profile).

## Required roles

To get the permissions that you need to create a conversion workspace, ask your administrator to grant you the [ Database Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datamigration#datamigration.admin) (`roles/datamigration.admin`) IAM role on your project.

For more information about granting roles, see [ Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) in the Identity and Access Management documentation.

This predefined role contains the permissions required to create a conversion workspace in Database Migration Service. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create a conversion workspace in Database Migration Service: 

  * `cloudaicompanion.entitlements.get`

This permission is included in the `roles/datamigration.admin` role. It is required for the [ Gemini-enhanced conversion features](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/code-conversion-with-gemini). 

  * `datamigration.conversionworkspaces.apply`
  * `datamigration.conversionworkspaces.commit`
  * `datamigration.conversionworkspaces.convert`
  * `datamigration.conversionworkspaces.create`
  * `datamigration.conversionworkspaces.delete`
  * `datamigration.conversionworkspaces.get`
  * `datamigration.conversionworkspaces.getIamPolicy`
  * `datamigration.conversionworkspaces.list`
  * `datamigration.conversionworkspaces.rollback`
  * `datamigration.conversionworkspaces.seed`
  * `datamigration.conversionworkspaces.setIamPolicy`
  * `datamigration.conversionworkspaces.update`



You might also be able to get these permissions with [ custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [ predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions). 

## Workspaces with the built-in editor

To create an interactive conversion workspace and perform the schema conversion, do the following:

  1. In the Google Cloud console, go to **Conversion workspaces**. 

[ Go to Conversion workspaces](https://console.cloud.google.com/dbmigration/conversion-workspaces)

  2. Click **Set up workspace**.
  3. On the **Create a conversion workspace** page, do the following: 
     1. Enter the name, identifier, and region for your conversion workspace.
     2. From the **Source database engine** drop-down menu, select **Oracle**. 
     3. From the **Destination database engine** select **Cloud SQL for PostgreSQL**. 
     4. In the **Enable Gemini settings for your workspace** section, use the checkboxes to enable Gemini-powered conversion features. You can also enable these features later when you want to [ Convert code and schema with Gemini assistance](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/code-conversion-with-gemini). 

Gemini-powered conversion features require the Gemini for Google Cloud API. Fore more information, see [ Gemini-powered conversion features](https://docs.cloud.google.com/database-migration/docs/convert-sql-with-dms#gemini-conversion). 

     5. Click **Create workspace and continue**.
  4. On the **Define source and pull schema snapshot** page, do the following: 
     1. From the **Source connection profile** drop-down menu, select the connection profile for your source database. 
     2. Click **Pull schema snapshot and continue**.

Database Migration Service is now connecting to the source database and retrieving your schema. This process can take several minutes. 

  5. On the **Select and convert objects** page, use the checkboxes to select which objects you want to convert to PostgreSQL syntax. 

You don't have to convert all your objects in one go. Instead, you can select just a few objects now and [ add more objects to the conversion](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/work-with-conversion-workspaces#add-source-objects) later. 

  6. Click **Convert and continue**. 

The conversion workspace opens.

  7. When you open a new workspace for the first time, you can upgrade it to access the Gemini-powered auto-conversion feature. Do the following: 
     * In the **Introducing Gemini auto-conversion** dialog, select the **Upgrade workspace to explore the new experience** checkbox, and click **Continue**. 
     * In the **Convert source objects with Gemini?** dialog, click **Convert**. 

Database Migration Service now performs the conversion process again to apply Gemini-powered conversion enhancements on top of the deterministic conversion results. For more information on Gemini auto-conversion feature, see [ Gemini auto-conversion](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/code-conversion-with-gemini#auto-conversion). 




## Legacy conversion workspaces

Legacy conversion workspaces are an older, more limited type of conversion workspaces. We don't recommend using the legacy type of conversion workspaces for your migrations. If you need to use a legacy conversion workspace, expand the **Create a legacy conversion workspace and convert schema** section for more information.

#### Create a legacy conversion workspace and convert schema

Legacy conversion workspaces use Ora2Pg configuration files. Before you create a legacy conversion workspace, make sure you first create your Ora2Pg configuration outside Database Migration Service. For more information, see [ Work with legacy conversion workspaces](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/legacy-conversion-workspaces). 

  1. In the Google Cloud console, go to **Conversion workspaces**. 

[ Go to Conversion workspaces](https://console.cloud.google.com/dbmigration/conversion-workspaces)

  2. Click **Set up workspace**.
  3. On the **Create a conversion workspace** page, do the following: 
     1. Enter the name, identifier, and region for your conversion workspace.
     2. From the **Source database engine** drop-down menu, select **Oracle**. 
     3. From the **Destination database engine** select **Cloud SQL for PostgreSQL**. 
     4. Expand the **Customize workspace configurations** section, and select the **Enable legacy conversion workspace** checkbox. 
     5. Click **Create workspace and continue**.
  4. On the **Connect to source and convert objects** page, do the following: 
     1. From the **Source connection profile** drop-down menu, select the connection profile for your source database. 
     2. In the **Configuration file** box, click **Browse** and use the system file picker to select your conversion mapping file. 

You can upload multiple conversion mapping files by clicking **Add file**. 

     3. In the **Convert the configuration** section, click **Pull schema and convert**. 

Database Migration Service is now connecting to the source database, retrieving your schema and converting it to the destination SQL schema according to the rules defined in your conversion mapping file. This process can take several minutes. 

  5. Click **Save and close**. 

The conversion workspace details page opens.




You can now apply the converted schema to your destination database. If your source database includes tables that don't have primary keys, you also need to manually create primary key constraints in the converted tables in the destination database after you apply the converted schema. For more information, see [ Work with legacy conversion workspaces](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/legacy-conversion-workspaces). 

## What's next

You can now work with your conversion workspace to fix conversion issues, modify your objects with the interactive editor, and apply converted schema to your destination database. See [ Convert Oracle code and schema to PostgreSQL syntax](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/convert-sql).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
