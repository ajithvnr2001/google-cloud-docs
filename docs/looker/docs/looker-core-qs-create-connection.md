---
url: https://docs.cloud.google.com/looker/docs/looker-core-qs-create-connection/
title: Quickstart: Create a database connection for a public secure connections instance \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:19.955811+00:00
---

# Quickstart: Create a database connection for a public secure connections instance  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-core-qs-create-connection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a database connection for a public secure connections instance

Looker (Google Cloud core) must be connected to a database to let users explore data and create content. Learn how to create a database connection for a Looker (Google Cloud core) public secure connections instance to use as the basis for any LookML project, or for a specific LookML project.

See the [Connecting Looker (Google Cloud core) to your database](https://docs.cloud.google.com/looker/docs/looker-core-dialects) documentation page for instructions on creating a database connection to an instance configured for private connections. See the [BigQuery default connection for Looker (Google Cloud core) quickstart](https://docs.cloud.google.com/looker/docs/looker-core-bigquery-default-connection) to use the BigQuery Quickstart Connection to create a default BigQuery connection that can use [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials).

**Note:** This quickstart is for creating a connection to a Looker (Google Cloud core) public secure connections instance using a database dialect that is [supported by Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-dialects#supported_dialects_for). You can also use this quickstart to create a database connection for a Looker (original) instance 

## Before you begin

To follow along with this quickstart, you'll need a database dialect that is compatible with Looker (Google Cloud core). For a list of compatible dialects, see [Supported dialects for Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-dialects#supported_dialects_for).

### Required roles

To complete this quickstart, you need the appropriate Identity and Access Management (IAM) role and Looker role.

#### Identity and Access Management roles

Your Looker (Google Cloud core) administrator grants you access to the Looker (Google Cloud core) application through Google Cloud's Identity and Access Management system.

To get the permission that you need to access the Looker (Google Cloud core) application, ask your administrator to grant you the [Looker Instance User ](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.instanceUser) (`roles/looker.instanceUser`) IAM role on the Google Cloud project that contains the Looker (Google Cloud core) instance. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `looker.instances.login` permission, which is required to access the Looker (Google Cloud core) application. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

#### Looker permissions

You must have the [**Looker Admin**](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles) role or have the [`manage_project_connections` Looker permission](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_project_connections).

## Navigate to the Connect your database to Looker page

  1. On the Looker (Google Cloud core) homepage, click the **Create** button in the main navigation menu to open the drop-down menu.
  2. From the drop-down menu, select **Connection** to open the **Connect your database to Looker** page.



## Create your database connection

On the **Connect your database to Looker** page, complete the following steps:

  1. In the **Name** section, enter a name for your connection. This name will appear in the **Connection** field of the **Create a Model** page, as well as the **Connections** page.

**Tip:** Don't use the name of any [folders](https://docs.cloud.google.com/looker/docs/organizing-spaces) for this setting. This value doesn't need to match anything in your database; `Name` is a label that identifies this connection within the Looker UI.
  2. In the **Connection Scope** section, select **All Projects** to create a connection that will be used for all LookML projects in your Looker (Google Cloud core) instance, or select **Selected Project** to create a connection that will be used only for the LookML project that you specify.

  3. If you chose **Selected Project** in the **Connection Scope** section, select the project that you want to use this connection for.

  4. In the **Dialect** section, choose the appropriate dialect for your database. You can also begin typing the dialect name and Looker will display suggestions for the dialect names that match what you've typed.

  5. Once you select a dialect for the connection, Looker displays the connection settings fields that apply to your database dialect. Fill in the subsequent settings that Looker displays:

     * The majority of the connection settings are common to most database dialects. For descriptions of common database settings, see the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db) documentation page.
     * For instructions for your specific dialect, see the [Connecting Looker (Google Cloud core) to your database](https://docs.cloud.google.com/looker/docs/looker-core-dialects#database_configuration_instructions) documentation page.
  6. In the **Optional Settings** section, expand or collapse the sections to see and configure the available options for your database connection. You can also click **Expand all** to expand all the sections.

  7. To test your connection configuration settings, click **Test**. If your connection is configured correctly, you'll see a green check mark.

  8. To create your connection, click **Create**.




You can view and manage the connection on the [**Connections** admin page](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections).

## What's next

  * [Generate a model from sample data quickstart](https://docs.cloud.google.com/looker/docs/looker-core-qs-model-generation)
  * [Looker IDE overview](https://docs.cloud.google.com/looker/docs/looker-ide)
  * [Managing LookML files and folders](https://docs.cloud.google.com/looker/docs/creating-project-files)
  * [Common LookML patterns](https://docs.cloud.google.com/looker/docs/additional-lookml-basics)
  * [Using version control and deploying](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
