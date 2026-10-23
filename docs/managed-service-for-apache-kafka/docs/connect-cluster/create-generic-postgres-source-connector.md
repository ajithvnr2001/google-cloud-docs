---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-generic-postgres-source-connector/
title: Create a Generic PostgreSQL Source connector \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:29.003362+00:00
---

# Create a Generic PostgreSQL Source connector  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-generic-postgres-source-connector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Create a Generic PostgreSQL Source connector Stay organized with collections  Save and categorize content based on your preferences. 

A Generic PostgreSQL Source connector lets you capture row-level changes from a PostgreSQL database and stream them to topics in a Managed Service for Apache Kafka cluster.

Typical use cases for this connector include:

  * Monitor row-level database changes in real time.
  * Integrate database change events into an event-driven architecture.
  * Respond to database events such as row insertions or deletions.
  * Copy database changes to other systems.
  * Replicate or restore PostgreSQL tables.



To read changes from a Cloud SQL for PostgreSQL database, use the [Cloud SQL for PostgreSQL Source connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-cloud-sql-postgres-source-connector).

## Before you begin

Before creating a Generic PostgreSQL Source connector, ensure you have the following:

  * A PostgreSQL database.

  * A [Connect cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-connect-cluster) associated with the Kafka cluster.

  * Create a Secret Manager secret that stores the database password. If your configuration uses database SSL, also create a secret for the database SSL password. Configure your Connect cluster with the secrets. For more information, see [Secret Manager resources](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-connect-cluster#secrets).

**Note:** Plaintext passwords are not supported. Only secret paths are supported in the `database.password` and `database.sslpassword` configurations. The backend expects these configurations to use the following format: `${directory:/var/secrets:PROJECT_ID-SECRET_NAME-SECRET_VERSION}`.



## Required roles and permissions

To get the permissions that you need to create a connector, ask your administrator to grant you the [Managed Kafka Connector Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create a connector. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create a connector:

  * Create a connector: `managedkafka.connectors.create`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Grant permissions to access Secret Manager secrets

The Managed Kafka service account needs permission to view and access the secrets stored in Secret Manager. Grant the following IAM roles to the service account:

  * **Secret Manager Viewer** (`roles/secretmanager.viewer`)
  * **Secret Manager Secret Accessor** (`roles/secretmanager.secretAccessor`)



The Managed Kafka service account has the following format: `service-PROJECT_NUMBER@gcp-sa-managedkafka.iam.gserviceaccount.com`, where PROJECT_NUMBER is the project number of the Connect cluster.

If your Connect cluster is in a different project from your Managed Service for Apache Kafka cluster, see [ Create a Connect cluster in a different project](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-connect-cluster#create-a-connect-cluster-in-a-different-project).

## Configure your PostgreSQL database

To enable the connector to read data-change events from your database, configure the following settings.

  1. Set the server's [`wal_level`](https://www.postgresql.org/docs/current/runtime-config-wal.html) to `logical`.
         
         ALTER SYSTEM SET wal_level = logical;
         

Restart the server to apply the setting.

  2. Create a database user for the connector to authenticate to PostgreSQL. The database user must be a replication role, allowing it to connect to the server in replication mode.
         
         CREATE ROLE ROLE_NAME WITH REPLICATION LOGIN PASSWORD 'ROLE_PASSWORD';
         

Replace the following:

     * `ROLE_NAME`: The name of the user, for example `debezium_user`.
     * `ROLE_PASSWORD`: The user's password.
  3. Create a [publication](https://www.postgresql.org/docs/current/logical-replication-publication.html) for the tables that you want to capture. The connector subscribes to the publication to receive data-change events.
         
         CREATE PUBLICATION dbz_publication FOR TABLE "SCHEMA_NAME"."TABLE_NAME";
         

Replace the following:

     * `SCHEMA_NAME`: The table's schema.

     * `TABLE_NAME`: The name of the table.

We recommend enclosing the schema and table names in double quotes, as shown, to avoid syntax errors if the names contain special characters or uppercase letters.

Alternatively, you can create a publication that replicates changes for all tables in the database:
    
    CREATE PUBLICATION dbz_publication FOR ALL TABLES;
    

Depending on the connector's `publication.autocreate.mode` setting, you can create the publication manually or let the connector create it automatically. For more information, see Publication mode.

  4. For each table, grant `SELECT` privileges on the table to the database user.
         
         GRANT SELECT ON TABLE "SCHEMA_NAME"."TABLE_NAME" TO ROLE_NAME;
         

Alternatively, you can grant select on all tables in a schema:
         
         GRANT SELECT ON ALL TABLES IN SCHEMA "SCHEMA_NAME" TO ROLE_NAME;
         

  5. For each table, grant `USAGE` privileges on the table schema to the database user. You can skip this step if the table is in the default `public` schema.
         
         GRANT USAGE ON SCHEMA "SCHEMA_NAME" TO ROLE_NAME;
         




## Create a Generic PostgreSQL Source connector

To create a Generic PostgreSQL Source connector, perform the following steps.

When the connector is initialized, it performs the following actions:

  1. Creates an initial snapshot of the database.
  2. Creates a Kafka topic for every table that has rows.
  3. For each database row, sends a change event to the corresponding topic.



While the connector is running, it continues to send change events to the topics. For more information about the initial snapshot, see [Snapshots](https://debezium.io/documentation/reference/stable/connectors/postgresql.html#postgresql-snapshots) in the Debezium documentation.

###  Console 

  1. In the Google Cloud console, go to the **Connect Clusters** page.

[Go to Connect Clusters](https://console.cloud.google.com/managedkafka/connectClusters)

  2. Click the Connect cluster where you want to create the connector.

  3. Click **Create connector**.

  4. For the connector name, enter a string.

For guidelines on how to name a connector, see [Guidelines to name a Managed Service for Apache Kafka resource](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/guidelines-resource).

  5. For **Connector plugin** , select **Generic PostgreSQL Source**.

  6. In the **Database hostname** field, enter the hostname or IP address of the PostgreSQL server.

  7. In the **Database name** field, enter the name of the database.

  8. In the **Database user** field, enter the name of replica role. The connector authenticates to the PostgreSQL server using this role.

  9. In the **Topic prefix** field, enter a prefix to use for the Kafka topic names.

  10. In the **Secret** list, select the secret that contains the database password.

  11. Optional: In the **Configurations** box, add configuration properties or edit the default properties. For more information, see Configure the connector.

  12. Optional: Select the **Task restart policy**. For more information, see [Task restart policy](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/connectors-overview#task-restart-policy).

  13. Click **Create**.




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Run the [`gcloud managed-kafka connectors create`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/connectors/create) command:
         
         gcloud managed-kafka connectors create CONNECTOR_ID \
             --location=LOCATION \
             --connect-cluster=CONNECT_CLUSTER_ID \
             --config-file=CONFIG_FILE
         

Replace the following:

     * `CONNECTOR_ID`: The ID or name of the connector. For guidelines on how to name a connector, see [Guidelines to name a Managed Service for Apache Kafka resource](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/guidelines-resource). The name of a connector is immutable.

     * `LOCATION`: The location where you create the connector. This must be the same location where you created the [Connect cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-connect-cluster).

     * `CONNECT_CLUSTER_ID`: The ID of the Connect cluster where the connector is created.

     * `CONFIG_FILE`: The path to the YAML configuration file for the connector.

Here is an example of a configuration file for the Generic PostgreSQL Source connector:
    
    connector.class: io.debezium.connector.postgresql.PostgresConnector
    database.dbname: DATABASE_NAME
    database.hostname: HOSTNAME
    database.password: CREDENTIALS
    database.user: DATABASE_USER
    key.converter: org.apache.kafka.connect.json.JsonConverter
    key.converter.schemas.enable: "false"
    plugin.name: pgoutput
    topic.prefix: TOPIC_PREFIX
    value.converter: org.apache.kafka.connect.json.JsonConverter
    value.converter.schemas.enable: "true"
    

Replace the following:

     * `HOSTNAME`: The hostname of the PostgreSQL database to read from.

     * `DATABASE_NAME`: The name of the PostgreSQL database to read from.

     * `DATABASE_USER`: The PostgreSQL database user to use when authenticating to the database.

     * CREDENTIALS: A path to the Secret Manager secret that contains the database password. Specify the secret using the following format:
           
           ${directory:/var/secrets:PROJECT_ID-SECRET_NAME-SECRET_VERSION}
           

     * `TOPIC_PREFIX`: A prefix to use for the Kafka topic names.




## Configure the connector

This section describes some configuration properties that you can set on the connector. For a complete list, see [Debezium connector for PostgreSQL](https://debezium.io/documentation/reference/stable/connectors/postgresql.html) in the Debezium documentation.

### Password and SSL password configurations

Only secret paths are supported in the `database.password` and `database.sslpassword` configurations. The backend expects these configurations to use the following format: `${directory:/var/secrets:PROJECT_ID-SECRET_NAME-SECRET_VERSION}`.

### IP address types

The `driver.ipTypes` property specifies the type of IP address that the connector uses to connect to the database:

  * `PRIVATE`: Private IP
  * `PSC`: Private Service Connect
  * `PUBLIC`: Public IP



The `driver.ipTypes` property contains a comma-separated list of IP types in preferred order; for example, `driver.ipTypes=PRIVATE,PUBLIC`.

### Publication mode

A Generic PostgreSQL Source connector streams change events from a [publication](https://www.postgresql.org/docs/current/logical-replication-publication.html) in the database. You can create the publication manually, or let the connector create it automatically.

The [`publication.autocreate.mode`](https://debezium.io/documentation/reference/stable/connectors/postgresql.html#postgresql-publication-autocreate-mode) setting specifies how and whether the connector should create a publication.

  * `filtered`. If the publication doesn't exist, the connector creates a new publication that includes only the captured tables. The database user must have `CREATE` permissions on the database and be the owner of the included tables.

If the publication already exists, the connector alters it to include the captured tables. To alter an existing publication, the database user must be the owner of the publication and the owner of the included tables.

  * `all_tables`. If the publication doesn't exist, the connector creates a new publication using the `FOR ALL TABLES` parameter. The database user must be a superuser.

Superuser roles bypass all permission checks in a database, so it's not recommended to grant `SUPERUSER` to the database user. Instead, either create the publication manually or set `publication.autocreate.mode=filtered`.

  * `disabled`. If the publication doesn't exist, an error occurs. The connector doesn't create a new publication.




The default value is `all_tables`.

### Publication name

By default, the connector tries to stream from a publication named `dbz_publication`. To specify a different publication, add `publication.name=PUBLICATION_NAME` to the configuration, where `PUBLICATION_NAME` is the publication name. Example: `publication.name=my_publication`.

### Replication slots

PostgreSQL uses _replication slots_ to stream database table changes. By default, the connector creates a replication slot named `debezium`. To use a different slot name, set the `slot.name` property.

If you create two instances of the connector for the same database, you must specify a unique slot name for each connector.

**Warning:** If a connector is paused, fails, or is deleted, its replication slot is not dropped automatically. The database continues to retain Write-Ahead Log (WAL) files indefinitely, which can quickly fill up your database server disk and cause a database outage. 

By default, the connector sets the [ `slot.drop.on.stop`](https://debezium.io/documentation/reference/stable/connectors/postgresql.html#postgresql-property-slot-drop-on-stop) property to `false` to prevent data loss. When you permanently delete a connector, you must manually drop the replication slot that the connector was using. The replication slot name defaults to `debezium`, unless configured differently using the [`slot.name`](https://debezium.io/documentation/reference/stable/connectors/postgresql.html#postgresql-property-slot-name) property.

We recommend that you set up alerts to monitor WAL disk usage on your source PostgreSQL database server, and drop any unused replication slots.

### Table filter

By default, the connector captures change data from every non-system table in the database. To filter which tables are captured, specify one or more of the following settings:

  * `schema.include.list`. A list of schemas to include.
  * `schema.exclude.list`. A list of schemas to exclude. Cannot be used with `schema.include.list`.
  * `table.include.list`. A list of tables to include.
  * `table.exclude.list`. A list of tables to exclude. Cannot be used with `table.include.list`.



### Topic names

By default, the connector creates Kafka topics with the following naming convention: `topic_prefix.schema.table_name`, where `topic.prefix` is the value of the `topic.prefix` configuration.

For more information, see [ Topic names](https://debezium.io/documentation/reference/stable/connectors/postgresql.html#postgresql-topic-names) in the Debezium documentation.

## What's next

  * [Troubleshoot a PostgreSQL Source connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/troubleshoot-postgres-source-connector)
  * [Troubleshoot Connect clusters and connectors](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/troubleshoot-kafka-connect)
  * [Create a Cloud SQL for PostgreSQL Source connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-cloud-sql-postgres-source-connector)



_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
