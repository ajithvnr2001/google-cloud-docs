---
url: https://docs.cloud.google.com/knowledge-catalog/docs/postgresql-transfer/
title: Import metadata from PostgreSQL \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:27.281944+00:00
---

# Import metadata from PostgreSQL  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/postgresql-transfer/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Import metadata from PostgreSQL Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Knowledge Catalog (formerly Dataplex Universal Catalog) lets you import metadata from PostgreSQL databases by using a managed connector. You can then search, discover, and govern these database assets in a unified catalog and retrieve resource context for large language model (LLM) workloads.

This connector supports PostgreSQL instances hosted on-premises, in Cloud SQL, or in other cloud environments. For more information about how connectors work, see [About metadata connectors](https://docs.cloud.google.com/knowledge-catalog/docs/connectors).

## Before you begin

Before you can import metadata from PostgreSQL, complete the following tasks:

  1. Grant the required roles and permissions.
  2. Enable the Dataplex API and BigQuery Data Transfer Service API.
  3. Meet the PostgreSQL prerequisites.
  4. Meet the networking prerequisites.



### IAM roles and permissions

To create and manage a Knowledge Catalog connector job, you need Identity and Access Management (IAM) roles that grant permissions for Knowledge Catalog and BigQuery Data Transfer Service.

To get the permissions that you need to configure a PostgreSQL connector, ask your administrator to grant you the following IAM roles:

  * To create and manage entry groups: [**Dataplex Catalog Admin**](https://docs.cloud.google.com/knowledge-catalog/docs/iam-roles#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`), [**Dataplex Catalog Editor**](https://docs.cloud.google.com/knowledge-catalog/docs/iam-roles#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`), or [**Dataplex Entry Group Owner**](https://docs.cloud.google.com/knowledge-catalog/docs/iam-roles#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`) on the project.
  * To create and manage BigQuery Data Transfer Service transfer jobs: [**BigQuery Admin**](https://docs.cloud.google.com/iam/docs/understanding-roles#bigquery.admin) (`roles/bigquery.admin`) on the project.
  * To view logs in Cloud Logging: [**Logs Viewer**](https://docs.cloud.google.com/iam/docs/understanding-roles#logging.viewer) (`roles/logging.viewer`) on the project.



Additionally, you must grant the BigQuery Data Transfer Service service agent (`service-PROJECT_NUMBER@gcp-sa-bigquerydatatransfer.iam.gserviceaccount.com`) the `dataplex.entryGroups.import` permission or the [**Dataplex Entry Group Importer**](https://docs.cloud.google.com/knowledge-catalog/docs/iam-roles#dataplex.entryGroupImporter) (`roles/dataplex.entryGroupImporter`) role. You can grant this role at either the project level or the entry group level.

For more information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

### Enable APIs

Enable the Dataplex API and BigQuery Data Transfer Service API.

[Enable the APIs](https://console.cloud.google.com/flows/enableapi?apiid=dataplex.googleapis.com,bigquerydatatransfer.googleapis.com)

### PostgreSQL prerequisites

Ensure that you meet the prerequisites for PostgreSQL transfers. For details, see [PostgreSQL prerequisites](https://docs.cloud.google.com/bigquery/docs/postgresql-transfer#postgresql-prereqs) in the BigQuery Data Transfer Service documentation.

In addition to the BigQuery Data Transfer Service prerequisites, your PostgreSQL database must meet the following requirements for metadata extraction:

  * **Minimum version:** PostgreSQL version 15 or later.
  * **Minimum required permissions:** The extraction tool requires specific permissions to successfully gather metadata.



To grant these permissions, run the following SQL statements:

  1. Grant connection to the database:
         
         GRANT CONNECT ON DATABASE DATABASE_NAME TO USERNAME;
         

  2. Grant usage on the schema:
         
         GRANT USAGE ON SCHEMA SCHEMA_NAME TO USERNAME;
         

  3. Grant the required read roles to the user:
         
         GRANT pg_read_all_data TO USERNAME;
         GRANT pg_read_all_settings TO USERNAME;
         GRANT pg_read_all_stats TO USERNAME;
         




Replace the following:

  * `DATABASE_NAME`: the name of the PostgreSQL database that you want to access.
  * `USERNAME`: the database user that you want to configure.
  * `SCHEMA_NAME`: the name of the schema that you want to access.



### Networking prerequisites

A [network attachment](https://docs.cloud.google.com/vpc/docs/create-manage-network-attachments) for connection through Private Service Connect is required when securely connecting to external databases or third-party cloud data sources with a private IP address inside a private network, to allow BigQuery Data Transfer Service to access your database.

If you connect to an on-premises environment or a cloud-hosted instance using a public IP address, a network attachment is not required.

## Configure a PostgreSQL connector

Configure a PostgreSQL connector using the Google Cloud console or the API.

### Console

  1. In the Google Cloud console, go to the **Knowledge Catalog** page.

[Go to Knowledge Catalog](https://console.cloud.google.com/dataplex)




  1. In the navigation menu, in the **Manage** section, click **Connectors**.
  2. Click **Add connection**.
  3. In the **Connectors** list, select the **PostgreSQL** card.
  4. In the **Data source details** section, provide connection details for your PostgreSQL instance: 
     * For **Network attachment** , select an existing network attachment if required, or create one.
     * Enter the **Host** , **Port** , **Database name** , **Username** , and **Password**.
     * If using TLS, select a **TLS Mode** and provide a **Trusted PEM Certificate**.
     * For **PostgreSQL metadata objects to import** , click **Browse** to select objects.
  5. In the **Destination settings** section: 
     * Click **Browse** and select an existing **Knowledge Catalog entry group** to store the imported metadata, or click **Create new entry group**.
     * Choose whether to set permissions on the entry group now or later. We recommend setting permissions so that users can view the imported metadata. If you didn't grant the [**Dataplex Entry Group Importer**](https://docs.cloud.google.com/knowledge-catalog/docs/iam-roles#dataplex.entryGroupImporter) (`roles/dataplex.entryGroupImporter`) role or the `dataplex.entryGroups.import` permission to the BigQuery Data Transfer Service service agent (`service-PROJECT_NUMBER@gcp-sa-bigquerydatatransfer.iam.gserviceaccount.com`) at the project level, you must grant it at the entry group level.
  6. In the **Connector config name** section, for **Display name** , enter a name for the metadata import job.
  7. In the **Schedule options** section, configure the frequency for the metadata import job. If you select **On-demand** , the job runs only when you manually trigger it.
  8. Optional: In the **Notification options** section, configure email or Pub/Sub notifications for job failures.
  9. Optional: In the **Advanced options** section, configure encryption settings. If you select a customer-managed encryption key (CMEK), note that the key is used to encrypt any transient data staged before starting the Knowledge Catalog metadata import jobs. It is not used to encrypt the metadata in the destination Knowledge Catalog entry group.
  10. Click **Save**.



### REST

Use the [`projects.locations.transferConfigs.create`](https://docs.cloud.google.com/bigquery/docs/reference/datatransfer/rest/v1/projects.locations.transferConfigs/create) method. In the [`TransferConfig`](https://docs.cloud.google.com/bigquery/docs/reference/datatransfer/rest/v1/projects.locations.transferConfigs#TransferConfig) resource, configure the following fields:

  * Set the `dataSourceId` field to `"postgresql"`.
  * In the `metadataDestination` field, populate the `dataplexConfiguration` object with the resource path of the target Knowledge Catalog entry group: `projects/<var>PROJECT_ID</var>/locations/<var>LOCATION</var>/entryGroups/<var>ENTRY_GROUP_ID</var>`



After you create the job, Knowledge Catalog schedules the first run according to your configuration, or you can start it manually.

## Search and view PostgreSQL metadata

  1. In the Google Cloud console, go to the **Knowledge Catalog** **Search** page.

[Go to Search](https://console.cloud.google.com/dataplex/dp-search)

  2. In the **Filters** panel, you can filter for PostgreSQL assets by using the **Project** , **System** , and **Type aliases** sections. In the **System** section, select **Imported Context**. Selecting this filter opens a **Managed Connectors** sub-section. Select **PostgreSQL** to filter for all PostgreSQL metadata.

  3. You can use the search field to perform search queries. You can perform a keyword or natural language search. For example, to view all PostgreSQL tables through keyword search, enter `system=POSTGRESQL AND type=TABLE`.

To learn more about searching for resources, see [Search for resources in Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/search-assets). To learn more about the expressions that you can use in the search field, see [Search syntax for Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/search-syntax).

  4. You can also use the [LookupContext](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations/lookupContext) API to retrieve LLM context for specific PostgreSQL resources.




## What's next

  * Learn how to [Manage connector jobs](https://docs.cloud.google.com/knowledge-catalog/docs/manage-connector-jobs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
