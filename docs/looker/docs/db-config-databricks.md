---
url: https://docs.cloud.google.com/looker/docs/db-config-databricks/
title: Databricks \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:42:52.069992+00:00
---

# Databricks  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/db-config-databricks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Databricks Stay organized with collections  Save and categorize content based on your preferences. 

You can configure your Databricks instance to work with Looker to analyze and visualize your data for operational reporting. Looker connects to Databricks only when Unity Catalog is enabled. Setup requires encrypting network traffic, creating a dedicated Looker user, and configuring user permissions.

**Note:** Looker supports connections to Databricks with Unity Catalog enabled. See Looker functionality with Databricks Unity Catalog for more information.

## Encrypting network traffic

It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options that are described on the [Enabling secure database access](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access) documentation page.

## Create a Looker user

Looker authenticates to Databricks by [personal access tokens](https://docs.databricks.com/dev-tools/api/latest/authentication.html). Follow the Databricks documentation to create a personal access token for a Databricks user to use in Looker.

Add permissions to this user with [`GRANT`](https://docs.databricks.com/spark/latest/spark-sql/language-manual/security-grant.html).

At a minimum, the Looker user should have the `SELECT` and `READ_METADATA` permissions.
    
    
    GRANT SELECT ON DATABASE <YOUR_DATABASE> TO `<looker>@<your.databricks.com>`
    GRANT READ_METADATA ON DATABASE <YOUR_DATABASE> TO `<looker>@<your.databricks.com>`
    

## Server information

Follow the [Databricks documentation](https://docs.databricks.com/integrations/bi/jdbc-odbc-bi.html#get-server-hostname-port-http-path-and-jdbc-url) to find the **HTTP Path** for your Databricks cluster. This will be referred to as `<YOUR_HTTP_PATH>` on this page.

## Setting up persistent derived tables

To use [persistent derived tables](https://docs.cloud.google.com/looker/docs/derived-tables#persistent-derived-tables), create a separate database.
    
    
    CREATE DATABASE <YOUR_SCRATCH_DATABASE>
    

This will also require additional write-based user permissions to be granted.
    
    
    GRANT SELECT CREATE MODIFY ON DATABASE <YOUR_SCRATCH_DATABASE> TO `<looker>@<your.databricks.com>`
    GRANT READ_METADATA ON DATABASE <YOUR_SCRATCH_DATABASE> TO `<looker>@<your.databricks.com>`
    

## Creating the Looker connection to your database

In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.

Fill out the connection details. The majority of the settings are common to most database dialects. See the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db) documentation page for information. Some of the settings are described next:

  * **Name** : Specify the name of the connection. This is how you will refer to the connection in LookML projects.
  * **Dialect** : Specify the dialect **Databricks**.
  * **Host** : Specify the Databricks workspace URL. For example, `dbc-yyyyyyyy.cloud.databricks.com/`.
  * **Port** : Specify the database port. The default is 443.
  * **Database** : Specify the name of the database to use for Looker queries. The default value is `default`.
  * **Catalog** : For Databricks databases with [Unity Catalog](https://www.databricks.com/product/unity-catalog) enabled, specify the name of the catalog to use for Looker queries. If you don't specify a catalog, Looker will access schemas from the default catalog only. See Looker functionality with Databricks Unity Catalog for more information.
  * **Authentication** : Select **Database Account** or **OAuth** : 
    * Use **Database Account** to specify a Databricks personal access token that will be used to connect to Looker (see the Create a Looker user section for instructions). 
      * For **Username** , enter the value `token` (do not enter the Databricks user email in this field).
      * For **Password** , enter the Databricks personal access token.
    * Use **OAuth** to configure OAuth for the connection. See the Configuring OAuth for Databricks connections section for more information.
  * **Enable PDTs** : Use this toggle to enable [persistent derived tables](https://docs.cloud.google.com/looker/docs/derived-tables#persistent-derived-tables). When PDTs are enabled, the **Connection** window reveals additional PDT settings and the [**PDT Overrides**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#pdt-overrides) section. Note: PDTs are not supported for Databricks connections that use OAuth.
  * **Temp Database**: Enter the database you would like to use to store PDTs.
  * **Max number of PDT builder connections** : Specify the number of possible concurrent PDT builds on this connection. Setting this value too high could negatively impact query times. For more information, see the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#max_pdt_builder_connections) documentation page.
  * **Additional JDBC parameters** : Add any additional JDBC parameters. See the Supported JDBC parameters section on this page for the list of parameters that Looker supports.

**Note:** The following parameters are required: `transportMode=http;httpPath=<YOUR_HTTP_PATH>`

Where `YOUR_HTTP_PATH` is the **HTTP path** value that you can retrieve from the **Connection details** of your Databricks warehouse.

  * **Maintenance Schedule** : A [`cron`](https://en.wikipedia.org/wiki/Cron#CRON_expression) expression that indicates when Looker should check [datagroups](https://docs.cloud.google.com/looker/docs/caching-and-datagroups#specifying_caching_policies_with_datagroup_parameters) and persistent derived tables. Read more about this setting in the [Maintenance Schedule](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#pdt_maintenance_schedule) documentation.

**Warning:** The default interval for **Maintenance Schedule** is five minutes. If you keep the default value, Looker will call your Databricks database every five minutes. This frequency can prevent Databricks clusters from shutting down, which may cause unexpected costs. Consider changing the default to a less frequent interval to prevent these costs.
  * **SSL** : Check to use SSL connections.

  * **Verify SSL** : Check to enforce strict SSL certificate verification.

  * **Max connections per node** : You can leave this setting at the default value initially. Read more about this setting in the [Max connections per node](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#max_connections) section of the **Connecting Looker to your database** documentation page.

  * **Connection Pool Timeout** : You can leave this setting at the default value initially. Read more about this setting in the [Connection Pool Timeout](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#connection-pool-timeout) section of the **Connecting Looker to your database** documentation page.

  * **SQL Runner Precache** : To cause SQL Runner to not preload table information and to load table information only when a table is selected, clear this checkbox. Read more about this setting in the [SQL Runner Precache](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#sql_runner_precache) section of the **Connecting Looker to your database** documentation page.

  * **Fetch Information Schema For SQL Writing** : When this setting is enabled, Looker uses your database's information schema to optimize SQL writing. Read more about this setting in the [Fetch Information Schema For SQL Writing](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#fetch_information_schema_for_sql_writing) section of the **Connecting Looker to your database** documentation page.

**Note:** Don't enable this option when running an Explore query against a Databricks connection with multiple dimensions and the **Show Totals** (subtotals) option enabled. The query may fail with an `UNRESOLVED_COLUMN.WITH_SUGGESTION` error. This is a known issue.
  * **Database Time Zone** : Specify the time zone to be used in the database. Leave this field blank if you don't want time zone conversion. See the [Using time zone settings](https://docs.cloud.google.com/looker/docs/using-time-zone-settings) documentation page for more information.




To verify that the connection is successful, click the **Test Connection** button in the **Status details** section at the bottom of the **Connections Settings** page.

If Looker displays **Can Connect** , press **Connect** to create the connection. 

Your database connection is then added to the list on the Looker [**Connections**](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections) **Admin** page.

## Looker functionality with Databricks Unity Catalog

Looker supports connections to Databricks databases with [Unity Catalog](https://www.databricks.com/product/unity-catalog) enabled. You can specify the catalog name in the **Catalog** field of the Looker **Connection** window when you create a Looker connection to your database, or when you edit an existing Looker connection to a Databricks database.

If your Databricks database is enabled for Unity Catalog, you can specify a Databricks catalog in the **Catalog** field of the Looker connection. When you specify a Databricks catalog, Looker uses the catalog in the following scenarios:

  * When generating a new LookML project [from your database](https://docs.cloud.google.com/looker/docs/generating-a-model), Looker will create the project files based on the tables in your connection's configured catalog.
  * For existing projects, when using the Looker IDE to [create a view from a table](https://docs.cloud.google.com/looker/docs/creating-project-files#adding_a_new_view_from_an_existing_database_table), Looker will create view files only from the tables in your connection's configured catalog.
  * When using [SQL Runner](https://docs.cloud.google.com/looker/docs/sql-runner-basics), you can select only schemas from your connection's configured catalog.



If your Databricks database is enabled for Unity Catalog and the Looker connection doesn't have a value in the **Catalog** field, most Looker functionality will access schemas from the default catalog only, such as in the following scenarios:

  * When generating a new LookML project [from your database](https://docs.cloud.google.com/looker/docs/generating-a-model), Looker will create the project files based on the tables in the Unity Catalog default catalog.
  * For existing projects, when using the Looker IDE to [create a view from a table](https://docs.cloud.google.com/looker/docs/creating-project-files#adding_a_new_view_from_an_existing_database_table), Looker can create view files only from the tables in the Unity Catalog default catalog.
  * When using [SQL Runner](https://docs.cloud.google.com/looker/docs/sql-runner-basics), you can select only schemas from the Unity Catalog default catalog.



## Configuring OAuth for Databricks connections

Looker supports OAuth for Databricks connections, meaning that each Looker user authenticates in to the database and authorizes Looker to run queries on the database with the user's own OAuth user account.

OAuth lets database administrators perform the following tasks:

  * Audit which Looker users are running queries against the database
  * Enforce role-based access controls by using database-level permissions
  * Use OAuth tokens for all processes and actions that access the database, instead of embedding database IDs and passwords in multiple places
  * Revoke authorization for a given user through the database directly



With Databricks connections that use OAuth, users must sign in again periodically when their OAuth tokens expire.

Note the following for database-level OAuth connections:

  * If a user lets their OAuth token expire, any Looker schedules or alerts that the user owns will be affected. To guard against this, Looker will send a notification email to the owner of each schedule and each alert before the current active OAuth token expires. Looker sends these notification emails 14 days, 7 days, and 1 day before the token expires. The user can go to their Looker user page to reauthorize Looker to the database and avoid any interruption to their schedules and alerts. See the [Personalizing user account settings](https://docs.cloud.google.com/looker/docs/user-account#configuring_oauth_connection_credentials) documentation page for details.
  * Because database connections that use OAuth are "per user," caching policies are also per user and not just per query. This means that, instead of using cached results whenever the same query is run within the caching period, Looker will use cached results only if the _same user has run the same query_ within the caching period. For further information on caching, see the [Caching queries](https://docs.cloud.google.com/looker/docs/caching-and-datagroups) documentation page.
  * [Persistent derived tables (PDTs)](https://docs.cloud.google.com/looker/docs/derived-tables#persistent_derived_table) are not supported for Databricks connections with OAuth.
  * When a Looker administrator sudos as another user, the administrator uses that user's OAuth access token. If the user's access token is expired, the administrator can't create a new token on behalf of the sudoed user. See the [Users](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#impersonating_users) documentation page for information about using the `sudo` command.
  * When a user initiates an OAuth authorization flow for a Databricks connection in Looker, Looker displays an **Authorize OAuth Connection** dialog notifying the user that authorizing the connection lets the Looker instance access data on their behalf, and that privileged Looker users, such as administrators or developers, might have visibility into their data. The user must select **Authorize** before proceeding to sign in to Databricks. This consent information is stored in the user's browser local storage, and the dialog appears again if local storage is cleared. After the user selects **Authorize** , Databricks itself doesn't display an additional user consent dialog.
  * To use OAuth for a Databricks connection, you must have Databricks [users](https://docs.databricks.com/en/admin/users-groups/users.html) or [service principals](https://docs.databricks.com/en/admin/users-groups/service-principals.html) that can be used for Looker queries, and you must provide the users and service principals with the Databricks permissions that Looker will need to access the data sources and perform the required actions within Databricks.



To create a Databricks connection to Looker using OAuth, you must perform these general steps, which are detailed in the following sections:

  1. Enable a custom OAuth application in Databricks
  2. Configure the connection in Looker



### Enabling a custom OAuth application in Databricks

To use OAuth for a Looker connection to Databricks, you must enable Looker as a custom OAuth application for your Databricks database by following these steps:

**Note:** To enable OAuth applications, you need the Databricks Account Admin role. See the [Databricks documentation](https://docs.databricks.com/en/integrations/enable-disable-oauth.html) for more information.

  1. Sign in to the [Databricks account console](https://accounts.cloud.databricks.com).
  2. Click the **Settings** icon in the side panel.
  3. Click the **App Connections** tab in the **Settings** window.
  4. In the **App Connections** tab, click **Add connection**.
  5. Enter the following values in the Databricks **Add connection** dialog:

     * **Application Name** : Provide a descriptive name, such as "Looker Integration".
     * **Redirect URLs** : Enter the Looker URL where Databricks will redirect users after successful authorization, using this format (replace `example.looker.com` with the URL of your Looker instance):
           
           https://example.looker.com/external_oauth/redirect
           

     * **Access scopes** : Select **SQL** to allow Looker to query data through SQL.

     * **Generate a client secret** : Enable this option.

  6. Click **Add** in the Databricks **Add connection** dialog.

  7. Copy and securely store the **Client ID** and **Client Secret** that Databricks generates.




Registering an OAuth application may take up to 30 minutes to process on the Databricks database. For more information, see the official [Databricks documentation](https://docs.databricks.com/en/integrations/enable-disable-oauth.html#enable-custom-oauth-applications-using-the-databricks-ui).

### Configure the connection in Looker

After you have configured Looker as a custom OAuth application on your Databricks database, you can configure a Looker connection to Databricks that uses OAuth.

  1. In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.
  2. Fill out the connection details, as described in the Creating the Looker connection to your database section of this page.
  3. Select the [**OAuth**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#use_oauth) option in the **Authentication** field.
  4. When you select the **OAuth** option, Looker displays the **OAuth Client ID** and **OAuth Client Secret** fields. For these values, enter the **Client ID** and **Client Secret** that was generated by Databricks when you enabled Looker as a custom OAuth application in Databricks.
  5. Select the **Test** button at the bottom of the **Connections Settings** page to ensure that Looker can successfully establish the OAuth flow and connect to your Databricks instance.



## Supported JDBC parameters

For Databricks, Looker supports the following JDBC parameters in the [**Additional JDBC parameters**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#additional_jdbc_parameters) field for the connection. See the documentation for your database for information on these parameters.

  * `Auth_Flow`
  * `AuthMech`
  * `catalogSchemaSwitch`
  * `ConnSchema`
  * `httpPath`
  * `LogLevel`
  * `OAuth2ClientId`
  * `OAuth2Secret`
  * `PWD`
  * `SocketTimeout`
  * `ssl`
  * `transportMode`
  * `UID`
  * `UserAgentEntry`



## Feature support

For Looker to support some features, your database dialect must also support them.

**Note:** [Incremental PDTs](https://docs.cloud.google.com/looker/docs/incremental-pdts) are supported only on Databricks version 12.1 and higher.

Databricks supports the following features as of Looker 26.20:

Feature | Supported?  
---|---  
Looker (Google Cloud core)|   
Symmetric aggregates|   
Derived tables|   
Persistent SQL derived tables|   
Persistent native derived tables|   
Stable views|   
Query killing|   
SQL-based pivots|   
Time zones|   
SSL|   
Subtotals|   
JDBC additional params|   
Case-sensitive|   
Location type|   
List type|   
Percentile|   
Distinct percentile|   
SQL Runner Show Processes|   
SQL Runner Describe Table|   
SQL Runner Show Indexes|   
SQL Runner Select 10|   
SQL Runner Count|   
SQL Explain|   
OAuth 2.0 credentials|   
Context comments|   
Connection pooling|   
HLL sketches|   
Aggregate awareness|   
Incremental PDTs|   
Milliseconds|   
Microseconds|   
Materialized views|   
Period-over-period measures|   
Approximate count distinct|   
In-database analytic models|   
Custom calendars|   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
