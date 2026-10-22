---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-bigquery/
title: Connect to BigQuery \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:50:10.733127+00:00
---

# Connect to BigQuery  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-bigquery/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Connect to BigQuery Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to create a [data store](https://docs.cloud.google.com/gemini/enterprise/docs/concepts) that connects to BigQuery data. You can link this data store to a Gemini Enterprise app to allow the agents to analyze your data.

To connect to BigQuery data using a Gemini Enterprise data store, you can use one of the following modes:

  * **Federated query (recommended)** [[Preview](https://cloud.google.com/products#product-launch-stages)]: Connect to BigQuery data in place without incurring egress costs for copying and moving the data. Federated query sends your query directly to BigQuery across all datasets and tables that your identity has Identity and Access Management (IAM) permission to access, which is more efficient for analytical queries. Because queries run using your credentials, BigQuery IAM permissions, including [row-level security](https://docs.cloud.google.com/bigquery/docs/row-level-security-intro), remain intact. When you use federated query mode, [Knowledge Catalog](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-knowledge-catalog) is automatically enabled on the **Assistant** tab of your Gemini Enterprise app to give the agent tools to search for data that the user has access to and look up context.
  * **Data ingestion** : Copy data from a specific BigQuery table to the Gemini Enterprise data store. Data must be refreshed to reflect changes in the BigQuery table. This mode incurs egress costs for moving data to a new location, and existing IAM permissions aren't replicated into the data store.



## Before you begin

To create a BigQuery data store in Gemini Enterprise, you must have the [Gemini Enterprise Admin](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) (`roles/discoveryengine.agentspaceAdmin`) or [Discovery Engine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.admin) (`roles/discoveryengine.admin`) role. For more information, see [Grant permissions to admins](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#grant-permissions-to-admins).

If your project is protected by a VPC Service Controls perimeter or has organization policy enforcement enabled, ensure that your organization policy allows the connector:

  * Add `bigquery_mcp` to the `allowedDataSources` parameter in the `discoveryengine.managed.allowedDataSources` managed constraint (**Restrict allowed data sources for data connectors**). For more information, see [Overview of managed policy constraints](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/managed-policy-constraints-overview) and [Configure allowed data sources](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/configure-allowed-data-sources).



In addition, configure the required BigQuery IAM permissions for the connector mode that you plan to use:

### Federated query

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Federated query mode uses the [BigQuery MCP server](https://docs.cloud.google.com/bigquery/docs/use-bigquery-mcp). Because different [MCP tools](https://docs.cloud.google.com/bigquery/docs/reference/mcp) (actions) require different permissions, the required IAM permissions depend on which tools you use. For more information, see [Required roles](https://docs.cloud.google.com/bigquery/docs/use-bigquery-mcp#required-roles) in the BigQuery MCP documentation.

**Note:** Users aren't required to have the [MCP Tool User (`roles/mcp.toolUser`)](https://docs.cloud.google.com/iam/docs/roles-permissions/mcp#mcp.toolUser) role, even if the connector is configured to use actions that require that role.

The following are the most commonly applied IAM roles for users who query or perform actions through the connector:

  * [BigQuery Job User (`roles/bigquery.jobUser`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.jobUser) on the BigQuery Google Cloud project where the query executes (compute or billing project), to give users the ability to run query jobs.
  * [BigQuery Data Viewer (`roles/bigquery.dataViewer`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.dataViewer) on the BigQuery Google Cloud project where the data is stored (storage project), to give users the ability to access data in a query or through BigQuery metadata tools such as [`get_table_info`](https://docs.cloud.google.com/bigquery/docs/reference/mcp/tools_list/get_table_info). If write actions are enabled, grant [BigQuery Data Editor (`roles/bigquery.dataEditor`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.dataEditor) instead.



### Data ingestion

To ingest data from a source Google Cloud project that's different from the Google Cloud project that contains the Gemini Enterprise data store that you're creating, grant the following IAM roles on the source BigQuery project to the `service-PROJECT_NUMBER@gcp-sa-discoveryengine.iam.gserviceaccount.com` service account (where `PROJECT_NUMBER` is the project number of the Google Cloud project that contains the Gemini Enterprise data store):

  * [BigQuery Job User (`roles/bigquery.jobUser`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.jobUser)
  * [BigQuery Data Editor (`roles/bigquery.dataEditor`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.dataEditor)

**Caution:** If you choose to ingest data from BigQuery into a Gemini Enterprise data store, BigQuery permissions aren't imported with the data. After import, any user with [sufficient Gemini Enterprise permissions](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#roles) can view the data, even if they don't have permission to view the data in BigQuery.

## Create a BigQuery data store

To create a data store that connects data from BigQuery to Gemini Enterprise, follow these steps:

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Go to the **Data stores** page.

  3. Click **Create data store**.

  4. On the **Source** page, choose a data source for your data store. Search for "BigQuery" in the **Select a data source** search field, or find BigQuery in the list of **First-party data sources**. Select **Add data source**.

  5. On the **Data** page, select the connector mode for how to connect to your data. Select from the following tabs for further instructions based on the mode that you have chosen.

### Federated query

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

     1. Select **Federated query (recommended)**.
     2. Optionally, under **Advanced options** , specify the Google Cloud billing project for your data store's query execution by typing the project ID into the **Billing Project ID** field. If you leave this field empty, queries will prompt the user for a billing project or rely on custom instructions.
     3. Click **Continue**.
     4. On the **Actions** page, select the BigQuery actions that you want to enable for your data store. You can edit these settings later. Click **Continue**.

### Data ingestion

     1. Select **Data ingestion**.
     2. Determine what kind of data you are importing. Before importing your data, review [Prepare data for ingesting](https://docs.cloud.google.com/gemini/enterprise/docs/prepare-data). 
        * If you are importing structured data, select from **BigQuery table with your own schema** or **BigQuery table with metadata**. If using your own schema, your schema will be auto-detected during import. If using metadata, you must define a Google-specified schema during import.
        * If you are importing data that requires specialized processing, select from the options under **Specialized Data Import**.
     3. Under **Synchronization frequency** , select how often you want to import data from your BigQuery table. This option cannot be changed after the data store is created.

        * Select **One time** for a single import.
        * Select **Periodic** to set a recurring import schedule.
     4. Select the data table that you want to import. In the **BigQuery path** field, click **Browse** , select a table that you have [prepared for ingesting](https://docs.cloud.google.com/gemini/enterprise/docs/prepare-data), and then click **Select**. Alternatively, enter the table location directly in the **BigQuery path** field.

     5. Click **Continue**.

After you've created your data store, you can check the status of your ingestion by going to the **Data stores** page and clicking your data store name to see details about it on its **Data** page. When the status column on the **Activity** tab changes from **In progress** to **Import completed** , the ingestion is complete.

Depending on the size of your data, ingestion can take several minutes to several hours.

  6. On the **Configuration** page, configure your data store settings.

     * **Location of your data connector** : Choose a region for where to store the metadata of your data store. You cannot change the location after the data store is created. For important information about multi-regions, see [Gemini Enterprise locations](https://docs.cloud.google.com/gemini/enterprise/docs/locations).
     * **Your data connector name** : In the **Data connector name** field, enter a name for your data connector. You cannot change the name after the data connector is created. Entering a name generates a unique ID for your data connector. Optionally, in the **Tag (optional)** field, enter a tag for your data connector, which serves as a stable identifier for the connector across all versions.
     * **Sensitive data protection policy** : Select a [sensitive data protection policy](https://docs.cloud.google.com/gemini/enterprise/docs/protect-sensitive-data) for your data store. The format should follow: `projects/{project}/locations/{location}/contentPolicies/{policy}`. You can edit this setting later.
  7. Click **Create**.




Now you're ready to attach your data store to a Gemini Enterprise app. In federated query mode, queries incur BigQuery compute costs when users run queries through the attached app; in data ingestion mode, importing data incurs BigQuery and Gemini Enterprise indexing costs even before the data store is attached to an app. To learn more about these charges, see [Gemini Enterprise pricing](https://cloud.google.com/generative-ai-app-builder/pricing).

## Next steps

  * To attach your data store to an app, create an app and select your data store following the steps on [Create a Gemini Enterprise app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app).

  * Learn how [Knowledge Catalog works with Data Cloud connectors](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-knowledge-catalog) (automatically enabled when you use federated query mode) to help the agent search for data that the user has access to and look up organizational context.

  * To build a scoped agent with verified queries in BigQuery, see [Publish a BigQuery data agent to Gemini Enterprise](https://docs.cloud.google.com/bigquery/docs/create-data-agents#publish-agent-gemini-enterprise).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
