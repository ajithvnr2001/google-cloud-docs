---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-cloud-sql-postgres-source-connector/
title: Create a Cloud SQL for PostgreSQL Source connector \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:28:18.140245+00:00
---

# Create a Cloud SQL for PostgreSQL Source connector  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-cloud-sql-postgres-source-connector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Create a Cloud SQL for PostgreSQL Source connector Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to create a Cloud SQL for PostgreSQL Source connector for Kafka Connect.

A Cloud SQL for PostgreSQL Source connector is an instance of a [Debezium PostgreSQL connector](https://debezium.io/documentation/reference/stable/connectors/postgresql.html). It reads row-level changes from a [Cloud SQL for PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/introduction) database and writes them to topics in a Managed Service for Apache Kafka cluster.

Use cases for this connector include:

  * Monitor row-level database changes in real time.
  * Integrate database change events into an event-driven architecture.
  * Respond to database events such as row insertions or deletions.
  * Copy database changes to other systems.



## Before you begin

Before creating a Cloud SQL for PostgreSQL Source connector, ensure you have the following:

  * A Cloud SQL for PostgreSQL instance with a database. To learn how to create these resources, see [Create and query a Cloud SQL for PostgreSQL database using the Google Cloud console](https://docs.cloud.google.com/sql/docs/postgres/create-query-database).

  * A [Managed Service for Apache Kafka cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-cluster).

  * A [Connect cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-connect-cluster).




## Required roles and permissions

To get the permissions that you need to create a connector, ask your administrator to grant you the [Managed Kafka Connector Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.connectorEditor) (`roles/managedkafka.connectorEditor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create a connector. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create a connector:

  * Create a connector: `managedkafka.connectors.create`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Grant permissions to read from Cloud SQL

The Managed Kafka service account must have permission to access Cloud SQL for PostgreSQL. Grant the following IAM roles to the service account:

  * **Cloud SQL Client** (`roles/cloudsql.client`)
  * **Cloud SQL Instance User** (`roles/cloudsql.instanceUser`)



The Managed Kafka service account has the following format: `service-PROJECT_NUMBER@gcp-sa-managedkafka.iam.gserviceaccount.com`, where PROJECT_NUMBER is the project number of the Connect cluster.

If your Connect cluster is in a different project from your Managed Service for Apache Kafka cluster, see [ Create a Connect cluster in a different project](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-connect-cluster#create-a-connect-cluster-in-a-different-project).

## Configure the database

Before you create the connector, you must configure database replication and enable the connector to authenticate with the database. The following sections describe these steps.

### Enable logical decoding

A Cloud SQL for PostgreSQL Source connector relies on the [logical decoding](https://www.postgresql.org/docs/current/logicaldecoding-explanation.html) feature of PostgreSQL. To enable logical decoding in your Cloud SQL for PostgreSQL instance, perform the following steps.

###  Console 

  1. Go to **Cloud SQL** > **Instances**.

[Go to Instances](https://console.cloud.google.com/sql/instances)

  2. Click the name of the instance.

  3. Click mode_edit **Edit**.

  4. Expand **Flags and parameters**.

  5. Click **Add a database flag**.

  6. In the **Choose a flag** list, select `cloudsql.logical_decoding`.

  7. For **Value** , select `On`.

  8. Click **Done**.

  9. Click **Save**.


**Note:** Enabling logical replication causes the database to restart.

For more information, see [Set up logical replication and decoding](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-logical-replication).

### Configure change data capture (CDC)

After you enable logical decoding in your instance, enable change data capture (CDC) for the tables that you want to replicate.

To enable CDC for a table, run the `CREATE PUBLICATION` SQL statement. This statement creates a _publication_ , which defines a group of tables to replicate.

  * **Option 1**. Create a publication that replicates changes for all tables in the database.
        
        CREATE PUBLICATION dbz_publication FOR ALL TABLES;
        

  * **Option 2**. Create a publication for a specific set of tables.
        
        CREATE PUBLICATION dbz_publication FOR TABLE TABLE_LIST;
        

Replace `TABLE_LIST` with a comma-separated list of tables, in the format `"schema_name"."table_name"`. Enclosing the schema and table names in double quotes, as shown, prevents syntax errors if the names contain special characters or uppercase letters.




By default, the connector uses `dbz_publication` for the publication name. To use a publication with a different name, see Publication name.

### Create a user account for the Managed Kafka service account

The Cloud SQL for PostgreSQL Source connector uses [IAM database authentication](https://docs.cloud.google.com/sql/docs/postgres/iam-authentication) to connect to the database. To enable IAM database authentication, add the Managed Kafka service account to the Cloud SQL instance, as follows:

###  Console 

  1. Go to **Cloud SQL** > **Instances**

[Go to Instances](https://console.cloud.google.com/sql/instances)

  2. Click the name of the instance.

  3. In the navigation pane, click **Users**.

  4. Click **Add user account**.

  5. In the **Add a user account** pane, select **Cloud IAM**.

  6. In the **IAM principal** field, enter the following:
         
         service-PROJECT_NUMBER@gcp-sa-managedkafka.iam.gserviceaccount.com
         

Replace `PROJECT_NUMBER` with the project number of the Connect cluster.

  7. Click **Add**.




###  gcloud 

Run the [`gcloud sql users create`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/users/create) command:
    
    
    gcloud sql users create service-PROJECT_NUMBER@gcp-sa-managedkafka.iam \
      --instance=INSTANCE_NAME \
      --type=cloud_iam_service_account
    

Replace the following:

  * `PROJECT_NUMBER`: The project number of the Connect cluster.

  * `INSTANCE_NAME`: The name of the Cloud SQL for PostgreSQL instance.




Due to the length limit on a database username, the `.gserviceaccount.com` suffix is dropped from the username, so the username is `service-PROJECT_NUMBER@gcp-sa-managedkafka.iam`. When you run SQL queries that reference the IAM user account, specify the truncated name.

### Configure the user account

After you create the IAM user account, connect to the database as a user with the `cloudsqlsuperuser` role (such as the default `postgres` user), and run the following SQL queries.

###  Console 

  1. Enable the user to read the write-ahead log.
         
         ALTER USER "service-PROJECT_NUMBER@gcp-sa-managedkafka.iam" WITH REPLICATION;
         

  2. Grant the user `SELECT` permission on the tables.
         
         GRANT SELECT ON ALL TABLES IN SCHEMA "SCHEMA_NAME"
         TO "service-PROJECT_NUMBER@gcp-sa-managedkafka.iam";
         

Alternatively, you can grant `SELECT` permission on individual tables. If you choose this option, you must also set the connector's `table.include.list` configuration property to the list of allowed tables. The following SQL query grants `SELECT` permission on a single table:
         
         GRANT SELECT ON TABLE SCHEMA_NAME.TABLE_NAME
         TO "service-PROJECT_NUMBER@gcp-sa-managedkafka.iam";
         

  3. For each table, give the user access the table's schema. You can skip this step if the table is in the default `public` schema.
         
         GRANT USAGE ON SCHEMA SCHEMA_NAME
         TO "service-PROJECT_NUMBER@gcp-sa-managedkafka.iam";
         




### Configure networking

A Cloud SQL for PostgreSQL Source connector can connect to the Cloud SQL instance in the following ways:

  * Private IP
  * Private Service Connect
  * Public IP



For more information about these options, see [Choose how to connect to Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/connection-options). As a security best practice, it's recommended to use either private IP or Private Service Connect, because these options don't require connecting to an external IP address.

The following table shows the network requirements for each option:

IP address type | Requirements  
---|---  
Private IP |  Configure private IP for your instance. For more information, see [Configure private IP](https://docs.cloud.google.com/sql/docs/postgres/configure-private-ip).   
Private Service Connect | 

  1. Configure Private Service Connect for your instance and get the DNS name of the Private Service Connect endpoint. For more information, see [Connect to an instance using Private Service Connect](https://docs.cloud.google.com/sql/docs/postgres/configure-private-service-connect).
  2. Add the endpoint's DNS name to the Connect cluster's [ Resolvable DNS domains](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-connect-cluster#dns-peering). For more information, see [ Update a Connect cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/update-connect-cluster).

  
Public IP | 

  1. Configure public IP for your instance. For more information, see [Configure public IP](https://docs.cloud.google.com/sql/docs/postgres/configure-ip). 
  2. Set up Public NAT to enable the Connect cluster workers to communicate with the internet. For more information, see [Set up Public NAT](https://docs.cloud.google.com/nat/docs/set-up-manage-network-address-translation). When you create the Cloud NAT gateway, specify the VPC network that contains the Connect cluster's [ primary subnet](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-connect-cluster#worker-subnet).

  
  
## Create a Cloud SQL for PostgreSQL Source connector

To create a Cloud SQL for PostgreSQL Source connector, perform the following steps.

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

  5. For **Connector plugin** , select **Cloud SQL for PostgreSQL Source**.

  6. In the **Instance** list, select the Cloud SQL instance.

  7. In the **Database** list, select the Cloud SQL database.

  8. In the **Topic prefix** field, enter a prefix to use for the Kafka topic names. Choose a unique prefix for each Cloud SQL for PostgreSQL Source connector.

  9. Optional: In the **Table names** field, enter a comma-separated list of tables to read change data from, in the format `"schema_name"."table_name"`. If you leave this field empty, the connector reads change data from all non-system tables in the database.

  10. Optional: In the **Configurations** box, add configuration properties or edit the default properties. For more information, see Configure the connector.

You might need to override the defaults for the following properties:

     * `driver.ipTypes`: This property must match the network configuration of your Cloud SQL instance. See IP address types.

     * `slot.name`: If you create multiple instances of the connector for the same database, specify a unique value for each connector. See Replication slots.

  11. Optional: Select the **Task restart policy**. For more information, see [Task restart policy](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/connectors-overview#task-restart-policy).

  12. Click **Create**.




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

Here is an example of a configuration file for the Cloud SQL for PostgreSQL Source connector:
    
    connector.class: io.debezium.connector.postgresql.PostgresConnector
    database.dbname: DATABASE_NAME
    driver.cloudSqlInstance: INSTANCE_ID
    driver.enableIamAuth: "true"
    driver.ipTypes: IP_TYPES
    driver.sslmode: disable
    key.converter: org.apache.kafka.connect.json.JsonConverter
    key.converter.schemas.enable: "false"
    plugin.name: pgoutput
    slot.name: SLOT_NAME
    table.include.list: TABLE_LIST
    topic.prefix: TOPIC_PREFIX
    value.converter: org.apache.kafka.connect.json.JsonConverter
    value.converter.schemas.enable: "true"
    

Replace the following:

     * `INSTANCE_ID`: The ID of the Cloud SQL instance that contains the database, formatted as follows:
           
           PROJECT_ID:REGION:INSTANCE_NAME
           

     * `DATABASE_NAME`: The name of the Cloud SQL database to read from.

     * `IP_TYPES`: A comma-separated list of IP address types

     * `SLOT_NAME`: The name of the replication slot to create.

     * `TABLE_LIST`: A comma-separated list of tables to read change data from, in the format `"schema_name"."table_name"`.

     * `TOPIC_PREFIX`: A prefix to use for the Kafka topic names.




## Configure the connector

This section describes some configuration properties that you can set on the connector. For a complete list, see [Debezium connector for PostgreSQL](https://debezium.io/documentation/reference/stable/connectors/postgresql.html) in the Debezium documentation.

### IP address types

The `driver.ipTypes` property specifies the type of IP address that the connector uses to connect to the database:

  * `PRIVATE`: Private IP
  * `PSC`: Private Service Connect
  * `PUBLIC`: Public IP



The `driver.ipTypes` property contains a comma-separated list of IP types in preferred order; for example, `driver.ipTypes=PRIVATE,PUBLIC`.

For more information, see Configure networking.

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
  * [Create a Generic PostgreSQL Source connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-generic-postgres-source-connector)



_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
