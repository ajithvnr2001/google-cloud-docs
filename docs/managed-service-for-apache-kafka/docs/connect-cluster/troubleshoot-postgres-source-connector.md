---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/troubleshoot-postgres-source-connector/
title: Troubleshoot a PostgreSQL Source connector \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:28:19.450887+00:00
---

# Troubleshoot a PostgreSQL Source connector  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/troubleshoot-postgres-source-connector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Troubleshoot a PostgreSQL Source connector Stay organized with collections  Save and categorize content based on your preferences. 

This section provides troubleshooting guidance for common issues encountered when using a Debezium PostgreSQL Source connector, including the following connector types:

  * [Cloud SQL for PostgreSQL Source connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-cloud-sql-postgres-source-connector)
  * [Generic PostgreSQL Source connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-generic-postgres-source-connector)



## Snapshotting failed

If the user doesn't have `USAGE` privilege on the table's schema, the connector can't create the initial snapshot, and the following error occurs:
    
    
    Snapshotting of table SCHEMA.TABLE failed
    

To resolve this issue, use the `GRANT` SQL command to grant `USAGE` privilege on the schema:
    
    
    GRANT USAGE ON SCHEMA SCHEMA_NAME TO ROLE_NAME;
    

## Creation of replication slot failed

If you create multiple connectors for the same PostgreSQL database server, the connectors must use different replication slots. Otherwise, the following error occurs:
    
    
    io.debezium.DebeziumException: Creation of replication slot failed; when setting up multiple connectors
    for the same database host, please make sure to use a distinct replication slot name for each.
        at io.debezium.connector.postgresql.PostgresConnectorTask.tryToCreateSlot(PostgresConnectorTask.java:282)
    

You might also see an error like the following:
    
    
    io.debezium.DebeziumException: Failed to start replication stream at LSN{0/80002808}; when setting
    up multiple connectors for the same database host, please make sure to use a distinct replication
    slot name for each.
    

To resolve this issue, set `slot.name` to a unique value. For more information, see [Setting up multiple connectors for same database server](https://debezium.io/documentation/reference/stable/connectors/postgresql.html#postgresql-deploying-multiple-connectors) in the Debezium documentation.

## Error creating or updating the publication

A Debezium PostgreSQL connector reads change events from a [publication](https://www.postgresql.org/docs/current/logical-replication-publication.html) in the database. If the connector can't access or create the publication, the errors listed in the following sections might appear in the connector logs.

### The publication doesn't exist

If `publication.autocreate.mode=disabled` and the publication doesn't exist, the following error occurs:
    
    
    org.apache.kafka.connect.errors.ConnectException: Publication PUBLICATION autocreation is disabled, please
    create one and restart the connector.
        at io.debezium.connector.postgresql.connection.PostgresReplicationConnection.initPublication(PostgresReplicationConnection.java:163)
    
    

To resolve this error, create the publication manually or set `publication.autocreate.mode` to `all_tables` or `filtered`.

### Unable to update filtered publication

If `publication.autocreate.mode=filtered` and the connector can't update an existing publication, the following error occurs:
    
    
    org.apache.kafka.connect.errors.ConnectException: Unable to update filtered publication PUBLICATION for
    "SCHEMA"."TABLE"
        at io.debezium.connector.postgresql.connection.PostgresReplicationConnection.createOrUpdatePublicationModeFilterted(PostgresReplicationConnection.java:227)
        at io.debezium.connector.postgresql.connection.PostgresReplicationConnection.initPublication(PostgresReplicationConnection.java:191)
    

To resolve this issue, make sure the database user is the owner of the publication.

### Unable to create filtered publication

If `publication.autocreate.mode=filtered` and the connector can't create a new publication, the following error occurs:
    
    
    org.apache.kafka.connect.errors.ConnectException: Unable to create filtered publication PUBLICATION for
    "SCHEMA"."TABLE"
        at io.debezium.connector.postgresql.connection.PostgresReplicationConnection.createOrUpdatePublicationModeFilterted(PostgresReplicationConnection.java:227)
        at io.debezium.connector.postgresql.connection.PostgresReplicationConnection.initPublication(PostgresReplicationConnection.java:171)
    

To resolve this issue, make sure the database user has `CREATE` permission on the database and is the owner of the included tables.

### A publication for all tables is already active

If `publication.autocreate.mode=filtered` and the publication was already created with `FOR ALL TABLES`, the following error occurs:
    
    
    io.debezium.DebeziumException: A logical publication for all tables named 'PUBLICATION' for plugin
    'PGOUTPUT' and database 'DATABASE' is already active on the server and can not be altered. If you need to
    exclude some tables or include only specific subset, please recreate the publication with necessary
    configuration or let plugin recreate it by dropping existing publication. Otherwise please change the
    'publication.autocreate.mode' property to 'all_tables'.
        at io.debezium.connector.postgresql.connection.PostgresReplicationConnection.initPublication(PostgresReplicationConnection.java:181)
    

This error occurs because the connector attempts to alter the tables in a publication for all tables. To resolve this issue, drop the existing publication and restart the connector. Alternatively, update 'publication.autocreate.mode' to `all_tables`.

### Must be superuser to create FOR ALL TABLES publication

If `publication.autocreate.mode=all_tables` and the connector tries to create a new publication, the following error might occur:
    
    
    io.debezium.jdbc.JdbcConnectionException: ERROR: must be superuser to create FOR ALL TABLES publication
        at io.debezium.connector.postgresql.connection.PostgresReplicationConnection.initPublication(PostgresReplicationConnection.java:207)
    

This error occurs when the database user isn't a superuser (or doesn't have the `cloudsqlsuperuser` role in Cloud SQL), which is required to create a publication with `FOR ALL TABLES`. To resolve this error, do one of the following:

  * Create the publication manually.
  * Update `publication.autocreate.mode` to a different value.
  * Grant `SUPERUSER` (or `cloudsqlsuperuser` in Cloud SQL) to the database user. However, generally this option isn't recommended, because these roles bypass permission checks in the database.



## What's next

  * [Troubleshoot Connect clusters and connectors](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/troubleshoot-kafka-connect)
  * [Create a Cloud SQL for PostgreSQL Source connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-cloud-sql-postgres-source-connector)
  * [Create a Generic PostgreSQL Source connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-generic-postgres-source-connector)



_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
