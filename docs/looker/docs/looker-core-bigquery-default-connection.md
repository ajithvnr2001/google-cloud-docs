---
url: https://docs.cloud.google.com/looker/docs/looker-core-bigquery-default-connection/
title: BigQuery default connection for Looker (Google Cloud core) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:01.869372+00:00
---

# BigQuery default connection for Looker (Google Cloud core)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-core-bigquery-default-connection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  BigQuery default connection for Looker (Google Cloud core) Stay organized with collections  Save and categorize content based on your preferences. 

To explore data, connect Looker (Google Cloud core) to a database. You can use the BigQuery QuickStart Connection to create a default connection to a BigQuery Standard SQL database.

![The BigQuery QuickStart tile on a home page.](https://docs.cloud.google.com/static/looker/docs/images/bq-quickstart-2418.png)

## Before you begin

Configuring a BigQuery QuickStart Connection requires the following permissions.

### Looker permissions

You can view and edit the **BigQuery QuickStart Connection** page on your Looker (Google Cloud core) instance **Home** page if you have one of the following [Looker permissions](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles):

  * The Looker [Admin role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_permission_sets)
  * The [`manage_project_connections` Looker permission](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_project_connections)



### IAM permissions

Looker (Google Cloud core) instances can use [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/application-default-credentials) to authenticate when you're [setting up a connection](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery) to BigQuery. When you use ADC, the connection will authenticate to the database by using the credentials of the [Looker (Google Cloud core) service account](https://docs.cloud.google.com/looker/docs/looker-core-service-account). The service account must have the following IAM permissions to access the BigQuery dataset:

  * For the project that contains the BigQuery dataset, the Looker service account must have the following IAM roles:

    * [Service Usage Consumer](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`)
    * [BigQuery Job User](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.jobUser) (`roles/bigquery.jobUser`)
    * [BigQuery Data Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`), or the following IAM permissions:

      * `bigquery.config.get`
      * `bigquery.datasets.create`
      * `bigquery.datasets.get`
      * `bigquery.tables.create`
      * `bigquery.tables.get`
**Note:** If your Looker (Google Cloud core) instance uses [persistent derived tables](https://docs.cloud.google.com/looker/docs/derived-tables#temporary_and_persistent_derived_tables) with a BigQuery dataset, the service account must have the [BigQuery Data Editor role](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) rather than the individual permissions listed here.
  * For the billing project, the Looker service account must have the following IAM roles:

    * [Service Usage Consumer](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`)
    * [BigQuery Job User](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.jobUser) (`roles/bigquery.jobUser`)



If the Looker (Google Cloud core) service account doesn't already have the necessary IAM roles, use the service account's email address when granting roles in that project. To [find the service account's email address](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents), go to the **IAM** page in the Google Cloud console and select the **Include Google-provided role grants** checkbox. The email will have the format `service-<project number>@gcp-sa-looker.iam.gserviceaccount.com`. Use that email to [grant the proper roles to the service account](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role).

## Configure a BigQuery QuickStart Connection

The BigQuery QuickStart Connection can be viewed and edited by users who have the correct permissions either from the **Home** page or from the **Connections** page in the **Admin** panel. On the **Connections** page, the BigQuery QuickStart Connection appears under the name **Default BigQuery Connection**. On a new instance, the **Storage project ID** and **Billing project ID** fields will default to **None**.

From the **Home** page, click the **Review connection** button to manage the connection. You can dismiss the **Home** page tile by clicking the **x** or by toggling the **BigQuery Quick Start** option in the **Discover** sidebar.

The BigQuery QuickStart Connection contains the following sections:

  * Billing Project ID
  * Primary Dataset
  * Optional Settings
  * Review



## Billing Project ID

The [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) serves as a unique identifier for the Google Cloud billing project. The billing project is the Google Cloud [project that gets billed for BigQuery usage](https://docs.cloud.google.com/billing/docs/how-to/modify-project), but you can still query datasets in a different Google Cloud project if your LookML developers specify fully scoped table names in the `sql_table_name` parameter of your LookML [views](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-table-name), [Explores](https://docs.cloud.google.com/looker/docs/reference/param-explore-sql-table-name), or [joins](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-sql-table-name). This is a required field.

**To authenticate to a BigQuery database using OAuth** : For BigQuery connections, Looker (Google Cloud core) can automatically use the OAuth application credentials that your Looker (Google Cloud core) admin used when they created the instance. See the [Create an OAuth client and credentials for a Looker (Google Cloud core) instance page](https://docs.cloud.google.com/looker/docs/looker-core-create-oauth) for more information.

Expand the **Status Details** section to test the settings for your connection.

## Primary Dataset

The **Primary Dataset** page contains the following settings.

### Storage Project ID

In the **Storage Project ID** field, enter the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) for the project that contains the BigQuery dataset to which you want to connect, even if it's the same project that contains the Looker (Google Cloud core) instance. This is a required field.

### Primary Dataset

The primary dataset is where BigQuery will look for tables if their location is not specified in the SQL query text. Note that Looker (Google Cloud core) queries can reference tables in any project or dataset, as long as the queries use fully scoped table names with the format `project_id.dataset_name.table_name`. The Looker (Google Cloud core) service account will also need the appropriate IAM permissions to access the tables in that location. This is a required field.

To learn more about datasets, see the [Connecting Looker to BigQuery](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery#connecting-to) documentation page.

Expand the **Status Details** section to test the settings for your connection.

## Configure optional settings for your BigQuery connection

The **Optional Settings** section contains the following options:

  * **Maximum Connections per Node** : The maximum number of connections to the database that are allowed at one time. **Note** : This setting is per each node in the Looker (Google Cloud core) deployment. The value must be between 5 and 100 and can be left at the default value initially. Read more about this setting in the [Max connections per node](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#max_connections) section of the **Connecting Looker to your database** documentation page.

  * **Connection Pool Timeout** : The number of seconds that a query will wait before timing out when the connection pool is full. Can be left at the default value initially. Read more about this setting in the [Connection Pool Timeout](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#connection-pool-timeout) section of the **Connecting Looker to your database** documentation page.

  * **Additional JDBC Parameters** : Add any additional JDBC parameters, such as BigQuery labels (see the [Job labels and context comments for BigQuery connections](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery#context_comments) section on this page for more information).

  * **Maintenance Schedule** : Cron expression that indicates the maximum frequency of datagroup trigger checks and PDT maintenance. Read more about this setting in the [Maintenance Schedule](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#datagroup_and_pdt_maintenance_schedule) documentation.

  * **SSL** : Choose whether you want to use SSL encryption to protect data as it passes between Looker (Google Cloud core) and your database. SSL is only one option that can be used to protect your data; other secure options are described on the [Enabling secure database access](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access) documentation page.

  * **Verify SSL** : Choose whether you want to require verification of the SSL certificate used by the connection. Read more about this setting in the [Verify SSL](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#verify_ssl) section of the **Connecting Looker to your database** documentation page.

  * **Precache tables and columns** : In SQL Runner, all table information is pre-loaded as soon as you select a connection and schema. This enables SQL Runner to quickly display table columns as soon as you click a table name. However, for connections and schema with many tables or with very large tables, you may not want SQL Runner to pre-load all the information.

  * **Fetch and cache schema** : For some SQL-writing features such as aggregate awareness, Looker (Google Cloud core) uses your database's information schema to optimize SQL writing. Read more about this setting in the [Fetch Information Schema For SQL Writing](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#fetch_information_schema_for_sql_writing) section of the **Connecting Looker to your database** documentation page.

  * **Enable PDTs** : Turn on the **Enable PDTs** toggle to enable [persistent derived tables](https://docs.cloud.google.com/looker/docs/derived-tables#persistent-derived-tables). When PDTs are enabled, the **Optional Settings** window reveals additional PDT fields and the **PDT Overrides** section.

  * **Temp database** : Enter the dataset in BigQuery where Looker (Google Cloud core) will create [persistent derived tables](https://docs.cloud.google.com/looker/docs/derived-tables#persistent-derived-tables). You should configure this dataset ahead of time, with the appropriate write permissions. This field is required to use PDTs.

  * **Max Number of PDT Builder Connections** : The **Max number of PDT builder connections** setting defaults to **1** but may be set as high as **100**. However, the value cannot be higher than the value set in the **Max connections per node**. Read more about this setting in the [Max Number of PDT Builder Connections section](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#max_number_of_pdt_builder_connections) of the **Connecting Looker to your database** documentation page. Set this value carefully. If the value is too high, you may overwhelm your database. If the value is low, then long-running PDTs or aggregate tables can delay the creation of other persistent tables or slow down other queries on the connection.

  * **Retry failed PDT builds** : The **Retry failed PDT builds** toggle configures how the [Looker (Google Cloud core) regenerator](https://docs.cloud.google.com/looker/docs/derived-tables#the_looker_regenerator) attempts to rebuild trigger-persisted tables that failed in the previous regenerator cycle. Read more about this setting in the [Retry failed PDT builds](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#retry_failed_pdt_builds) section of the **Connecting Looker to your database** documentation page.

  * **PDT API Control** : The **PDT API Control** toggle determines whether the [`start_pdt_build`](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/DerivedTable/start_pdt_build), [`check_pdt_build`](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/DerivedTable/check_pdt_build), and [`stop_pdt_build`](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/DerivedTable/stop_pdt_build) API calls can be used for this connection. When the **PDT API Control** toggle is disabled, these API calls will fail when they reference PDTs on this connection.

  * **PDT Overrides** : If your database supports persistent derived tables, and you have turned on the **Enable PDTs** toggle in the connection settings, Looker (Google Cloud core) displays the **PDT Overrides** section. In the **PDT Overrides** section, you can enter separate JDBC parameters (host, port, database, username, password, schema, additional parameters, and after connect statements) that are specific to PDT processes. Read more about this setting in the [PDT Overrides](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#pdt_overrides) section of the **Connecting Looker to your database** documentation page.

  * **Database Time Zone** : The time zone in which your database stores time-based information. Looker (Google Cloud core) needs to know this so that it can convert time values for users, making it easier to understand and use time-based data. See the [Using time zone settings](https://docs.cloud.google.com/looker/docs/using-time-zone-settings) documentation page for more information.

  * **Query Time Zone** : The **Query Time Zone** option is visible only if you have disabled [**User Specific Time Zones**](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings#user_specific_time_zones). See the [Using time zone settings](https://docs.cloud.google.com/looker/docs/using-time-zone-settings) documentation page for more information.




Expand the **Status Details** section to test the settings for your connection.

## Review

Review and modify the connection details that you entered in the previous sections in the **Review** section.

Expand the **Status Details** section to test the settings for your connection. Click the edit icon next to each section to be taken back to that section to change your settings.

## Save and test the connection

To save any changes made to the BigQuery QuickStart Connection, click **Save**.

You can test your connection settings from a couple of places in the Looker (Google Cloud core) UI:

  * Expand the **Status Details** section at the bottom of any of the QuickStart Connection pages, and click **Test Connection**.
  * From the **Home** page, expand the **Status Details** section at the bottom of the QuickStart Connection tile, and click **Test Connection**.
  * On the **Connections** Admin page, select the **Test Connection** button next to the connection's listing, as described on the [Connections](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections#testing_connections) documentation page.



If your connection does not pass one or more tests, here are some troubleshooting options:

  * Access the [logs of your Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-logging) for more detailed error messaging.
  * [Reach out to support](https://docs.cloud.google.com/looker/docs/looker-core-support) for additional troubleshooting assistance.



## What's next

  * [Manage users within Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-user-management)
  * [Administer a Looker (Google Cloud core) instance from the Google Cloud console](https://docs.cloud.google.com/looker/docs/looker-core-admin-console)
  * [Looker (Google Cloud core) admin settings](https://docs.cloud.google.com/looker/docs/looker-core-admin-looker)
  * [Use the sample LookML project on a Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-sample-project)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
