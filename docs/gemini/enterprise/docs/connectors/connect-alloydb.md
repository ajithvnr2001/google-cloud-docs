---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-alloydb/
title: Connect to AlloyDB for PostgreSQL \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:50:12.283214+00:00
---

# Connect to AlloyDB for PostgreSQL  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-alloydb/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Connect to AlloyDB for PostgreSQL Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to create a [data store](https://docs.cloud.google.com/gemini/enterprise/docs/concepts) that connects to AlloyDB for PostgreSQL data. You can link this data store to a Gemini Enterprise app to allow the agents to analyze your data.

To connect to AlloyDB for PostgreSQL data using a Gemini Enterprise data store, you can use one of the following modes:

  * **Federated query (recommended)** [[Preview](https://cloud.google.com/products#product-launch-stages)]: Connect to AlloyDB for PostgreSQL data in place without incurring egress costs for copying and moving the data. Federated query sends your query directly to AlloyDB for PostgreSQL across all clusters, databases, and tables that your identity has Identity and Access Management (IAM) permission to access, which is more efficient for analytical queries. When you use federated query mode, [Knowledge Catalog](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-knowledge-catalog) is automatically enabled on the **Assistant** tab of your Gemini Enterprise app to give the agent tools to search for data that the user has access to and look up context.

**Caution:** **High-accuracy database queries:** Federated query mode provides broad access across all clusters and databases accessible by the user, but query accuracy can vary on complex transactional schemas. For workloads requiring high accuracy, deterministic table scoping, and verified queries (golden SQL), create a scoped data agent in [AlloyDB for PostgreSQL](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics/alloydb/create-data-agents#publish-agent-gemini-enterprise) and publish it to Gemini Enterprise.
  * **Data ingestion** : Copy data from a specific AlloyDB for PostgreSQL table to the Gemini Enterprise data store. Data must be manually refreshed to reflect changes in the AlloyDB for PostgreSQL table. This mode incurs egress costs for moving data to a new location, and existing IAM permissions aren't replicated into the data store.




## Before you begin

To create an AlloyDB for PostgreSQL data store in Gemini Enterprise, you must have the [Gemini Enterprise Admin](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) (`roles/discoveryengine.agentspaceAdmin`) or [Discovery Engine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.admin) (`roles/discoveryengine.admin`) role. For more information, see [Grant permissions to admins](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#grant-permissions-to-admins).

If your project is protected by a VPC Service Controls perimeter or has organization policy enforcement enabled, ensure that your organization policy allows the connector:

  * Add `alloydb` to the `allowedDataSources` parameter in the `discoveryengine.managed.allowedDataSources` managed constraint (**Restrict allowed data sources for data connectors**). For more information, see [Overview of managed policy constraints](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/managed-policy-constraints-overview) and [Configure allowed data sources](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/configure-allowed-data-sources).



In addition, configure the required AlloyDB for PostgreSQL IAM permissions for the connector mode that you plan to use:

### Federated query

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To connect to AlloyDB for PostgreSQL using federated query mode, grant the following IAM roles in the Google Cloud project that contains your AlloyDB for PostgreSQL cluster to users who query or perform actions through the connector:

  * **Cluster and database access** : 
    * [Cloud AlloyDB Viewer (`roles/alloydb.viewer`)](https://docs.cloud.google.com/alloydb/docs/reference/iam-roles-permissions#roles) and [Cloud AlloyDB Client (`roles/alloydb.client`)](https://docs.cloud.google.com/alloydb/docs/reference/iam-roles-permissions#roles) (or [Cloud AlloyDB Database User (`roles/alloydb.databaseUser`)](https://docs.cloud.google.com/alloydb/docs/reference/iam-roles-permissions#roles) with IAM database authentication) for read-only queries and tools.
    * [Cloud AlloyDB Admin (`roles/alloydb.admin`)](https://docs.cloud.google.com/alloydb/docs/reference/iam-roles-permissions#roles) if write or cluster management actions (such as creating clusters, instances, or backups, or executing SQL writes) are enabled.
  * **MCP tool access** : 
    * [MCP Tool User (`roles/mcp.toolUser`)](https://docs.cloud.google.com/iam/docs/roles-permissions/mcp#mcp.toolUser) permission in the Google Cloud project where the AlloyDB for PostgreSQL cluster lives to invoke MCP tools.



### Data ingestion

To ingest data from a source Google Cloud project that's different from the Google Cloud project that contains the Gemini Enterprise data store that you're creating, grant the [Cloud AlloyDB Admin (`roles/alloydb.admin`)](https://docs.cloud.google.com/alloydb/docs/reference/iam-roles-permissions#roles) role on the source AlloyDB for PostgreSQL project to the `service-PROJECT_NUMBER@gcp-sa-discoveryengine.iam.gserviceaccount.com` service account (where `PROJECT_NUMBER` is the project number of the Google Cloud project that contains the Gemini Enterprise data store).

**Caution:** If you choose to ingest data from AlloyDB for PostgreSQL into a Gemini Enterprise data store, AlloyDB for PostgreSQL permissions aren't imported with the data. After import, any user with [sufficient Gemini Enterprise permissions](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#roles) can view the data, even if they don't have permission to view the data in AlloyDB for PostgreSQL.

## Create a AlloyDB for PostgreSQL data store

To create a data store that connects data from AlloyDB for PostgreSQL to Gemini Enterprise, follow these steps:

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Go to the **Data stores** page.

  3. Click **Create data store**.

  4. On the **Source** page, choose a data source for your data store. Search for "AlloyDB for PostgreSQL" in the **Select a data source** search field, or find AlloyDB for PostgreSQL in the list of **First-party data sources**. Select **Add data source**.

  5. On the **Data** page, select the connector mode for how to connect to your data. Select from the following tabs for further instructions based on the mode that you have chosen.

### Federated query

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

     1. Select **Federated query (recommended)**. Click **Continue**.
     2. On the **Actions** page, select the AlloyDB for PostgreSQL actions that you want to enable for your data store. You can edit these settings later. Click **Continue**.

### Data ingestion

     1. Select **Data ingestion**.
     2. Specify details about the data that you want to import. Under **Import data from your AlloyDB for PostgreSQL table** , specify the following information: 
        * **Project ID** : The Google Cloud project that contains the AlloyDB for PostgreSQL table. This is a required field.
        * **Location ID** : The AlloyDB for PostgreSQL location ID that contains the data you want to import. This is a required field.
        * **Cluster ID** : The AlloyDB for PostgreSQL cluster ID that contains the data you want to import. This is a required field.
        * **Database ID** : The AlloyDB for PostgreSQL database ID that contains the data you want to import. This is a required field.
        * **Table ID** : The AlloyDB for PostgreSQL table ID that contains the data you want to import. This is a required field.
     3. Click **Continue**.

  6. On the **Configuration** page, configure your data store settings.

     * **Location of your data connector** : Choose a region for where to store the metadata of your data store. You cannot change the location after the data store is created. For important information about multi-regions, see [Gemini Enterprise locations](https://docs.cloud.google.com/gemini/enterprise/docs/locations).
     * **Your data connector name** : In the **Data connector name** field, enter a name for your data connector. You cannot change the name after the data connector is created. Entering a name generates a unique ID for your data connector. Optionally, in the **Tag (optional)** field, enter a tag for your data connector, which serves as a stable identifier for the connector across all versions.
     * **Sensitive data protection policy** : Select a [sensitive data protection policy](https://docs.cloud.google.com/gemini/enterprise/docs/protect-sensitive-data) for your data store. The format should follow: `projects/{project}/locations/{location}/contentPolicies/{policy}`. You can edit this setting later.
  7. Click **Create**.




Now you're ready to attach your data store to a Gemini Enterprise app. In federated query mode, queries incur AlloyDB for PostgreSQL usage costs when users run queries through the attached app; in data ingestion mode, importing data incurs AlloyDB for PostgreSQL and Gemini Enterprise indexing costs even before the data store is attached to an app. To learn more about these charges, see [Gemini Enterprise pricing](https://cloud.google.com/generative-ai-app-builder/pricing).

## Next steps

  * To attach your data store to an app, create an app and select your data store following the steps on [Create a Gemini Enterprise app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app).

  * Learn how [Knowledge Catalog works with Data Cloud connectors](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-knowledge-catalog) (automatically enabled when you use federated query mode) to help the agent search for data that the user has access to and look up organizational context.

  * To build a high-accuracy, scoped agent with verified queries, see [Publish an AlloyDB for PostgreSQL data agent](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics/alloydb/create-data-agents#publish-agent-gemini-enterprise) to Gemini Enterprise.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
