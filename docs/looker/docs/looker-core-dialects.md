---
url: https://docs.cloud.google.com/looker/docs/looker-core-dialects/
title: Connecting Looker (Google Cloud core) to your database \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:14.886934+00:00
---

# Connecting Looker (Google Cloud core) to your database  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-core-dialects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Connecting Looker (Google Cloud core) to your database Stay organized with collections  Save and categorize content based on your preferences. 

To query your data, connect your Looker (Google Cloud core) instance to a database. This guide describes how to use supported dialects and configure specific connection options.

For instances that use [private connections](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#private_ip_connections), you may need to complete [additional configuration](https://docs.cloud.google.com/looker/docs/looker-core#connect_to_external_services) to access databases. The specific configuration depends on the networking setup for the Looker (Google Cloud core) instance that you are working with.

## Set up a database connection

Looker (Google Cloud core) must be connected to a database to enable data exploration. See the list of supported dialects to learn which dialects are supported by Looker (Google Cloud core).

You can create a database connection within a Looker (Google Cloud core) instance if you have one of the following permissions:

  * the Looker [Admin role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_permission_sets)
  * the [`manage_project_connections` Looker permission](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_project_connections)

**Note:** Looker (Google Cloud core) instances can use [BigQuery Quickstart Connection](https://docs.cloud.google.com/looker/docs/looker-core-bigquery-default-connection) to streamline the connection process to an existing BigQuery project.

You can follow the **Set up Looker** guide that appears dynamically within the Looker (Google Cloud core) instance to connect your database, or you can follow the steps that are listed on the dialect-specific documentation pages. The majority of the settings are common to most database dialects. See the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db) documentation page for information about common fields in the Looker connection setup window.

There are additional steps if you want to set up your Looker (Google Cloud core) connection with any of the following options:

  * **Private connections** : If your Looker (Google Cloud core) instance uses a [private connections](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#private_ip_connections), you must configure [Private Service Connect](https://docs.cloud.google.com/looker/docs/looker-core-psc-southbound) or [private services access](https://docs.cloud.google.com/looker/docs/looker-core-private-ip-config) (depending on which connection type the instance uses) to connect it to any of the following types of databases:

    * A database in a different network within Google Cloud
    * A database that is hosted by another cloud service provider
    * An on-premises database

To set up a private connection to databases that are hosted by other cloud service providers, ensure that your Google Cloud project is configured to route traffic to those cloud service providers to allow for data exchange. Learn more about connecting cloud environments on the [Patterns for connecting other cloud service providers with Google Cloud](https://docs.cloud.google.com/architecture/patterns-for-connecting-other-csps-with-gcp) documentation page.

  * **Authenticate with Application Default Credentials for BigQuery and Cloud SQL databases** : Looker (Google Cloud core) instances can use [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/application-default-credentials) to authenticate in to your database, as described in the following sections:

    * Using Application Default Credentials to connect to a BigQuery database
    * Using Application Default Credentials with a BigQuery database in a different Google Cloud project
    * Using Application Default Credentials to connect to a Cloud SQL database
  * **Authenticate to a BigQuery database using OAuth** : For BigQuery connections, Looker (Google Cloud core) can use the [OAuth application credentials that your Looker admin used](https://docs.cloud.google.com/looker/docs/looker-core-create-oauth) when they created the Looker (Google Cloud core) instance. See the Configuring OAuth authentication with BigQuery section of this page for more information.




## Using Application Default Credentials to connect to a BigQuery database

Looker (Google Cloud core) instances can use [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/application-default-credentials) to authenticate when you're [setting up a connection](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery) to a BigQuery Standard SQL database. When you use ADC, the connection will authenticate to the database by using the credentials of the [Looker (Google Cloud core) project's service account](https://docs.cloud.google.com/looker/docs/looker-core-service-account).

To use ADC with a BigQuery database, select **Application Default Credentials** in the **Authentication** field of the **Connection Settings** page of the Looker instance. For the full procedure, see the documentation for [connecting Looker to a BigQuery database](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery).

If your Looker (Google Cloud core) instance uses [persistent derived tables](https://docs.cloud.google.com/looker/docs/derived-tables#temporary_and_persistent_derived_tables) with a BigQuery dataset, you must also grant the [Looker service account](https://docs.cloud.google.com/looker/docs/looker-core-instance-create#service_account) the [BigQuery Data Editor Identity and Access Management (IAM) role](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.dataEditor).

If you're connecting to a BigQuery database that is in a different project from your Looker (Google Cloud core) instance, some additional setup is required. See the Using Application Default Credentials with a BigQuery database in a different Google Cloud project section.

### Service account impersonation

If you want to authenticate to the BigQuery database by using a service account other than the Looker (Google Cloud core) project's service account, you can create a [delegated request flow](https://docs.cloud.google.com/iam/docs/create-short-lived-credentials-delegated#sa-credentials-delegated) by entering another service account, or a comma-separated chain of service accounts, into the **Impersonated Service Account** field. The Looker (Google Cloud core) service account is automatically used as the first service account in the chain and does not need to be added to the field. The last service account in the chain (also known as the _impersonated service account_) is the one that authenticates with the database.

**Note:** Looker doesn't support [Liquid templating](https://docs.cloud.google.com/looker/docs/liquid-variable-reference) or [user attributes](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes) for authentication credentials, such as the **Impersonated Service Account** field or service account key files; these values must remain static. User attributes are supported only for fields such as **Project ID** and **Dataset**. To separate database access or quota usage by user group, use OAuth or create separate database connections.

When using service account impersonation, do the following:

  * Enable the Service Consumer Management API. 

[ Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=serviceconsumermanagement.googleapis.com)

  * Make sure that all service accounts in the chain, including the Looker (Google Cloud core) project's service account, [have the appropriate IAM permissions](https://docs.cloud.google.com/iam/docs/create-short-lived-credentials-delegated#sa-credentials-permissions).
  * Make sure that the impersonated service account has the [BigQuery Job User role](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.jobUser) and the [BigQuery Data Viewer role](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.dataViewer). If you need to inspect service states and operations, or use quota and billing from a consumer project, the [Service Usage Consumer role](https://docs.cloud.google.com/service-usage/docs/access-control#predefined_roles) is also required.
  * If you have enabled [persistent derived tables (PDTs)](https://docs.cloud.google.com/looker/docs/derived-tables#temporary_and_persistent_derived_tables) for your connection, you must also enter the impersonated service account's email address in the **Service Account Email Address** field within the **PDT Overrides** section. This ensures that the PDT processes use the impersonated service account. See the [Enable PDT Overrides section](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#enable_pdt_overrides) on the **Connecting Looker to your database** documentation page for more information.



### Using Application Default Credentials with a BigQuery database in a different Google Cloud project

The steps for using ADC for a BigQuery Standard SQL database that is outside the project that houses your Looker (Google Cloud core) instance are the same as those for setting up a connection inside the same project. However, before you can set up the connection in your Looker (Google Cloud core) instance, your Looker (Google Cloud core) project's service account must have the following IAM roles:

  * [BigQuery Data Viewer role](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.dataViewer) for the project that contains the BigQuery dataset.
  * [BigQuery Job User role](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.jobUser) and the [Service Usage Consumer role](https://docs.cloud.google.com/service-usage/docs/access-control#predefined_roles) on the billing project that's listed on the [**Connection Settings** page](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery#connecting-to).
  * If your Looker (Google Cloud core) instance uses [persistent derived tables](https://docs.cloud.google.com/looker/docs/derived-tables#temporary_and_persistent_derived_tables) with a BigQuery dataset, the service account must also have the [BigQuery Data Editor role](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.dataEditor) for the project that contains the BigQuery dataset.



If the Looker (Google Cloud core) service account doesn't already have IAM roles in the project that contains the BigQuery dataset, use the service account's email address when you grant roles in that project. To [find the service account's email address](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents), go to the **IAM** page in the Google Cloud console and select the **Include Google-provided role grants** checkbox. The email will have the format `service-<project number>@gcp-sa-looker.iam.gserviceaccount.com`. Use that email to [grant the proper roles to the service account](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role).

Once the proper roles are granted, follow the steps to use ADC.

You can now use ADC with this BigQuery Standard SQL database. The project attached to the service account that is specified in the [**Connection Settings** page](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery#connecting-to) will be used for billing and also act as the default project.

## Using Application Default Credentials to connect to a Cloud SQL database

Looker (Google Cloud core) instances can use [ADC](https://docs.cloud.google.com/docs/authentication/application-default-credentials) to authenticate a connection to a Cloud SQL database (either [Cloud SQL for PostgreSQL](https://docs.cloud.google.com/looker/docs/db-config-postgresql) or [Cloud SQL for MySQL](https://docs.cloud.google.com/looker/docs/db-config-google-cloud-sql)). When you use ADC to authenticate in to your Cloud SQL database, the Google Cloud project where the Cloud SQL database is running is the project that is billed for Looker queries.

For Looker connections to Cloud SQL that use ADC, ADC [impersonates](https://docs.cloud.google.com/iam/docs/service-account-impersonation) a service account or a chain of service accounts to access your database. When you create the Looker connection to your database, you use the **IAM database username(s)** field to specify the service account, or the chain of service accounts, that ADC will impersonate. The [Looker service account](https://docs.cloud.google.com/looker/docs/looker-core-instance-create#service_account) that was created automatically when you created the Looker (Google Cloud core) instance is automatically used as the first service account in the chain and does not need to be added to the field.

If you want to authenticate to your Cloud SQL database by using a service account other than the Looker service account, you can create a [delegated request flow](https://docs.cloud.google.com/iam/docs/create-short-lived-credentials-delegated#sa-credentials-delegated) by entering another [service account](https://docs.cloud.google.com/iam/docs/service-account-types), or a comma-separated chain of service accounts, into the **IAM database username(s)** field.

The last service account in the chain (also known as the _impersonated service account_) is the one that authenticates with the database, and this account must be added as a user on your Cloud SQL database. If you are using the Looker service account as the last service account in the chain (by leaving the **IAM database username(s)** field blank), you must add the Looker service account as a user on your Cloud SQL database.

The following are the general steps for connecting a Cloud SQL for PostgreSQL or Cloud SQL for MySQL database to Looker using ADC:

  1. Add the impersonated service account to your Cloud SQL database.
  2. Set up service account impersonation on your Cloud SQL database.
  3. Connect to your database to run additional configuration commands for Cloud SQL for PostgreSQL or Cloud SQL for MySQL.
  4. Create the Looker connection to your database.



### Add the impersonated service account to your Cloud SQL database

When you create the Looker connection to your database, you use the **IAM database username(s)** field to specify the service account, or the chain of service accounts, that ADC will [impersonate](https://docs.cloud.google.com/iam/docs/service-account-impersonation) to perform actions on your database. The last service account in the impersonation chain is considered the _impersonated service account_.

To use ADC with Cloud SQL, you must add the impersonated service account to your Cloud SQL database:

  * In the default case, if you leave the **IAM database username(s)** field blank, ADC will impersonate the Looker service account. In this case, the Looker service account is the impersonated service account, so you need to add the Looker service account to your Cloud SQL database. See the [Create a Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-instance-create#service_account) documentation page for information about the Looker service account and for the procedure for viewing the Looker service account email address.
  * If you specify a service account other than the Looker service account, or if you specify a chain of service accounts in the **IAM database username(s)** field, you must add the last service account in the impersonation chain to your Cloud SQL database.



To add a service account to your Cloud SQL database, you must have the [Cloud SQL Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) IAM role.

Follow the "Add an IAM user or service account to your database instance" procedure for your database dialect to add the impersonated service account to your Cloud SQL database:

  * [Cloud SQL for PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/add-manage-iam-users#creating-a-database-user)
  * [Cloud SQL for MySQL](https://docs.cloud.google.com/sql/docs/mysql/add-manage-iam-users#creating-a-database-user)



### Set up service account impersonation on your Cloud SQL database

Once you have created the Cloud SQL user on your database, you must set up your Cloud SQL database for service impersonation by performing the following steps:

  1. Follow the procedure to [enable the Cloud SQL Admin API](https://docs.cloud.google.com/sql/docs/mysql/admin-api#enable_the_api).
  2. Make sure that all service accounts in the chain, including the Looker service account, [have the appropriate IAM permissions](https://docs.cloud.google.com/iam/docs/create-short-lived-credentials-delegated#sa-credentials-permissions).
  3. Follow the procedure for [granting a single role in the Google Cloud console](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role). Grant the following [Cloud SQL roles](https://docs.cloud.google.com/sql/docs/mysql/iam-roles) to the impersonated service account that you added to your Cloud SQL database:

     * [Cloud SQL Instance User](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.instanceUser)
     * [Cloud SQL Client](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.client)
     * [Service Usage Consumer](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer)

If you specify a service account other than the Looker service account, or if you specify a chain of service accounts in the **IAM database username(s)** field, grant every service account in the chain the following permission:

     * [Service Account Token Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountTokenCreator)



### Additional configuration commands for Cloud SQL for MySQL

For Cloud SQL for MySQL, you must [connect to your database instance](https://docs.cloud.google.com/sql/docs/mysql/connect-instance-cloud-shell#connect) and run the following command on the Cloud SQL for MySQL database:
    
    
    GRANT ALL on DATABASE_NAME.* to 'DATABASE_USER'@'%'
    

Replace the following:

  * DATABASE_NAME: The name of your database.
  * DATABASE_USER: The truncated service account username for the impersonated service account that you added to your Cloud SQL database. The service account will have the format `service-<project number>@gcp-sa-looker.iam.gserviceaccount.com`. Truncate the username by removing the `@` and everything that follows. After truncating, the username would look like `service-<project number>`.



For example, if the service account username is `service-12345678901@gcp-sa-looker.iam.gserviceaccount.com` and the database name is `looker-test`, the command would be as follows:
    
    
    GRANT ALL on looker-test.* to 'service-12345678901'@'%'
    

### Additional configuration commands for Cloud SQL for PostgreSQL

For Cloud SQL for PostgreSQL, you must [connect to your database instance](https://docs.cloud.google.com/sql/docs/postgres/connect-instance-cloud-shell#connect) and run some configuration commands on the Cloud SQL for PostgreSQL database:

  * Grant the user permissions on your database as described in the [Users and security](https://docs.cloud.google.com/looker/docs/db-config-postgresql#users_and_security) section of the PostgreSQL documentation page.
  * Set the search path for the Looker SQL Runner to use to retrieve metadata from your database, as described in the [Setting the `search_path`](https://docs.cloud.google.com/looker/docs/db-config-postgresql#setting-the-search_path) section of the Looker documentation PostgreSQL page.



### Create the connection from Looker (Google Cloud core) to your Cloud SQL database

To create the connection from Looker to your database, follow these steps:

  1. In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.
  2. From the **Dialect** drop-down menu, select **Google Cloud PostgreSQL** or, for Cloud SQL for MySQL, select **Google Cloud SQL**.
  3. In the **Authentication** section, click the **Application Default Credentials** option.
  4. In the **IAM database username(s)** field, specify the service account, or the chain of service accounts, that you want ADC to [impersonate](https://docs.cloud.google.com/iam/docs/service-account-impersonation) to perform actions on your database:

     * If you want Looker to authenticate to the Cloud SQL database by using the [Looker (Google Cloud core) project's service account](https://docs.cloud.google.com/looker/docs/looker-core-instance-create#service_account), leave this field blank.
     * If you want Looker to authenticate to the Cloud SQL database by using a service account other than the Looker (Google Cloud core) project's service account, you can create a [delegated request flow](https://docs.cloud.google.com/iam/docs/create-short-lived-credentials-delegated#sa-credentials-delegated) by entering another [service account](https://docs.cloud.google.com/iam/docs/service-account-types), or a comma-separated chain of service accounts.
  5. Fill out the rest of the connection details. The majority of the settings are common to most database dialects. See the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db) documentation page for information.

  6. To verify that the connection is successful, click the **Test Connection** button in the **Status details** section at the bottom of the **Connections Settings** page.

  7. If Looker displays **Can Connect** , press **Connect** to create the connection.




Your database connection is then added to the list on the Looker [**Connections**](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections) **Admin** page.

**Note:** It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options that's described on the [Enabling secure database access](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access) documentation page. For Cloud SQL for PostgreSQL, if you're interested in using SSL encryption, see the [PostgreSQL documentation](https://www.postgresql.org/docs/).

Once a database connection is set up, you are ready to [set up a LookML project](https://docs.cloud.google.com/looker/docs/looker-core-instance-setup#setup_lookml).

## Configuring OAuth authentication with BigQuery

To configure OAuth authentication for connections to a BigQuery database on a Looker (Google Cloud core) instance, follow these steps:

  1. Under **Authentication** , select **OAuth**. Looker (Google Cloud core) defaults to using the OAuth application credentials that your Looker admin used when they [created the Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-create-oauth). You don't need to manually create or enter a client ID and secret.
  2. Add an additional redirect URI to the **Authorized redirect URIs** field in the instance's OAuth client (or create a new OAuth client with the credentials and add a redirect URI). The redirect URI must use the Looker instance's URL followed by `/external_oauth/redirect`. For background information, see the [generating OAuth credentials for BigQuery](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery#generating_google_oauth_credentials) documentation.



If you want to manually enter different OAuth credentials for this connection, enable the **Manually configure OAuth credentials** toggle, and then fill out the **OAuth Client ID** and **OAuth Client Secret** fields. If you manually enter OAuth credentials, that won't change or update the credentials that were used when the Looker (Google Cloud core) instance was created. Follow the steps in the [Configuring a BigQuery database project for OAuth](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery#configuring-a-database-project-for-oauth) documentation to create and use different credentials.

## Supported dialects for Looker (Google Cloud core)

The following table shows the Looker (Google Cloud core) support for database dialects:

Dialect | Supported?  
---|---  
Actian Avalanche|   
Amazon Athena|   
Amazon Aurora MySQL|   
Amazon Redshift|   
Amazon Redshift 2.1+|   
Amazon Redshift Serverless 2.1+|   
Apache Druid|   
Apache Druid 0.13.x - 0.17.x|   
Apache Druid 0.18+|   
Apache Hive 2.3+|   
Apache Hive 3.1.2+|   
Apache Spark 3+|   
ClickHouse|   
ClickHouse 26+|   
Cloudera Impala 3.1+|   
Cloudera Impala 3.1+ with Native Driver|   
Cloudera Impala with Native Driver|   
DataVirtuality|   
Databricks|   
Denodo 7|   
Denodo 8 & 9|   
Dremio|   
Dremio 11+|   
Dremio 26+ with Arrow Flight SQL|   
Exasol|   
Google BigQuery Legacy SQL|   
Google BigQuery Standard SQL|   
Google Cloud AlloyDB for PostgreSQL|   
Google Cloud PostgreSQL|   
Google Cloud SQL|   
Google Spanner|   
Greenplum|   
HyperSQL|   
IBM Netezza|   
MariaDB|   
Microsoft Azure PostgreSQL|   
Microsoft Azure SQL Database|   
Microsoft Azure Synapse Analytics|   
Microsoft SQL Server 2008+|   
Microsoft SQL Server 2012+|   
Microsoft SQL Server 2016|   
Microsoft SQL Server 2017+|   
MongoBI|   
MongoSQL|   
MySQL|   
MySQL 8.0.12+|   
Oracle|   
Oracle ADWC|   
PostgreSQL 9.5+|   
PostgreSQL pre-9.5|   
PrestoDB|   
PrestoSQL|   
SAP HANA|   
SAP HANA 2+|   
SingleStore|   
SingleStore 7+|   
Snowflake|   
Teradata|   
Trino|   
Vector|   
Vertica|   
  
## Database configuration instructions

Instructions are available for these SQL dialects:

**Note:** The following links navigate to the instructions for Looker (original) database connections, but they apply to Looker (Google Cloud core) as well.

  * [Amazon Athena](https://docs.cloud.google.com/looker/docs/db-config-amazon-athena)
  * [Amazon Aurora MySQL](https://docs.cloud.google.com/looker/docs/db-config-amazon-aurora-mysql)
  * [Amazon Redshift](https://docs.cloud.google.com/looker/docs/db-config-amazon-redshift)
  * [Apache Druid 0.18+](https://docs.cloud.google.com/looker/docs/db-config-apache-druid)
  * [Apache Hive 3.1.2+](https://docs.cloud.google.com/looker/docs/db-config-apache-hive)
  * [Apache Spark 3+](https://docs.cloud.google.com/looker/docs/db-config-apache-spark)
  * [ClickHouse](https://docs.cloud.google.com/looker/docs/db-config-clickhouse)
  * [Cloudera Impala 3.1+](https://docs.cloud.google.com/looker/docs/db-config-cloudera-impala)
  * [Databricks](https://docs.cloud.google.com/looker/docs/db-config-databricks)
  * [Denodo 8](https://docs.cloud.google.com/looker/docs/db-config-denodo)

| 

  * [Dremio 11+](https://docs.cloud.google.com/looker/docs/db-config-dremio)
  * [Google BigQuery Standard SQL](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery)
  * [Google Cloud SQL for MySQL](https://docs.cloud.google.com/looker/docs/db-config-google-cloud-sql)
  * [Google Cloud SQL for PostgreSQL](https://docs.cloud.google.com/looker/docs/db-config-postgresql)
  * [Google Spanner](https://docs.cloud.google.com/looker/docs/db-config-cloud-spanner)
  * [MariaDB](https://docs.cloud.google.com/looker/docs/db-config-mysql-mariadb-singlestore)
  * [Microsoft Azure PostgreSQL](https://docs.cloud.google.com/looker/docs/db-config-postgresql)
  * [Microsoft Azure SQL Database](https://docs.cloud.google.com/looker/docs/db-config-microsoft-azure-sql-database)
  * [Microsoft Azure Synapse Analytics](https://docs.cloud.google.com/looker/docs/db-config-microsoft-azure-synapse-analytics)
  * [Microsoft SQL Server 2017+](https://docs.cloud.google.com/looker/docs/db-config-microsoft-sql-server)

| 

  * [MySQL 8.0.12+](https://docs.cloud.google.com/looker/docs/db-config-mysql-mariadb-singlestore)
  * [Oracle](https://docs.cloud.google.com/looker/docs/db-config-oracle)
  * [PostgreSQL 9.5+](https://docs.cloud.google.com/looker/docs/db-config-postgresql)
  * [Presto (formerly PrestoDB)](https://docs.cloud.google.com/looker/docs/db-config-prestodb-and-trino)
  * [SAP HANA](https://docs.cloud.google.com/looker/docs/db-config-sap-hana)
  * [SingleStore 7+](https://docs.cloud.google.com/looker/docs/db-config-mysql-mariadb-singlestore)
  * [Snowflake](https://docs.cloud.google.com/looker/docs/db-config-snowflake)
  * [Teradata](https://docs.cloud.google.com/looker/docs/db-config-teradata)
  * [Trino (formerly PrestoSQL)](https://docs.cloud.google.com/looker/docs/db-config-prestodb-and-trino)
  * [Vertica](https://docs.cloud.google.com/looker/docs/db-config-vertica)

  
---|---|---  
  
## What's next

  * [Configure a Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-instance-setup)
  * [Manage users within Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-user-management)
  * [Administer a Looker (Google Cloud core) instance from the Google Cloud console](https://docs.cloud.google.com/looker/docs/looker-core-admin-console)
  * [Looker (Google Cloud core) admin settings](https://docs.cloud.google.com/looker/docs/looker-core-admin-looker)
  * [Use the sample LookML project on a Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-sample-project)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
