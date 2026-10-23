---
url: https://docs.cloud.google.com/spanner/docs/fgac-queues/
title: Fine-grained access control for queues \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:30.815615+00:00
---

# Fine-grained access control for queues  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/fgac-queues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Fine-grained access control for queues Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how [fine-grained access control](https://docs.cloud.google.com/spanner/docs/fgac-about) works with Spanner queues for GoogleSQL-dialect databases and PostgreSQL-dialect databases.

In Spanner, a queue is defined as a schema object. Access to send messages, receive messages, extend message leases, acknowledge and delete messages, or query queues directly complies with standard Spanner database roles and privileges.

## Grants for sending messages (producers)

To send messages to a queue using DML (`INSERT INTO`) or the Mutation API (see [Insert statement](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/dml-syntax#insert-statement)), grant the `INSERT` privilege on the queue to the database role:

###  GoogleSQL 
    
    
    GRANT INSERT ON QUEUE QUEUE_NAME TO ROLE ROLE_NAME;

###  PostgreSQL 
    
    
    GRANT INSERT ON QUEUE QUEUE_NAME TO ROLE_NAME;

To revoke the privilege:

###  GoogleSQL 
    
    
    REVOKE INSERT ON QUEUE QUEUE_NAME FROM ROLE ROLE_NAME;

###  PostgreSQL 
    
    
    REVOKE INSERT ON QUEUE QUEUE_NAME FROM ROLE_NAME;

## Grants for receiving messages (consumers)

To stream messages from a queue, consumer workers execute the `RECEIVE_QUEUE_NAME()` table-valued function (TVF) with `ExecuteStreamingSQL`.

To allow a database role to stream messages from the queue, grant `EXECUTE` on the automatically created `RECEIVE_QUEUE_NAME` function:

###  GoogleSQL 
    
    
    GRANT EXECUTE ON TABLE FUNCTION RECEIVE_QUEUE_NAME TO ROLE ROLE_NAME;

###  PostgreSQL 
    
    
    GRANT EXECUTE ON FUNCTION spanner.receive_QUEUE_NAME TO ROLE_NAME;

To revoke the privilege:

###  GoogleSQL 
    
    
    REVOKE EXECUTE ON TABLE FUNCTION RECEIVE_QUEUE_NAME FROM ROLE ROLE_NAME;

###  PostgreSQL 
    
    
    REVOKE EXECUTE ON FUNCTION spanner.receive_QUEUE_NAME FROM ROLE_NAME;

Calling `RECEIVE_QUEUE_NAME()` requires only `EXECUTE` on the TVF; it does not require `SELECT` on the queue.

### Extend message leases

When a consumer receives a message, Spanner assigns an initial 10-second lease. If message processing takes longer than the initial lease, the consumer must extend the lease using the `RENEWLEASE_QUEUE_NAME()` TVF.

To extend leases, the role must have `EXECUTE` on the `RENEWLEASE_QUEUE_NAME` function:

###  GoogleSQL 
    
    
    GRANT EXECUTE ON TABLE FUNCTION RENEWLEASE_QUEUE_NAME TO ROLE ROLE_NAME;

###  PostgreSQL 
    
    
    GRANT EXECUTE ON FUNCTION spanner.renewlease_QUEUE_NAME TO ROLE_NAME;

To revoke the privilege:

###  GoogleSQL 
    
    
    REVOKE EXECUTE ON TABLE FUNCTION RENEWLEASE_QUEUE_NAME FROM ROLE ROLE_NAME;

###  PostgreSQL 
    
    
    REVOKE EXECUTE ON FUNCTION spanner.renewlease_QUEUE_NAME FROM ROLE_NAME;

Calling `RENEWLEASE_QUEUE_NAME()` requires only `EXECUTE` on the TVF; it does not require `SELECT` on the queue.

For more information about receiving messages and extending leases, see [Use queues](https://docs.cloud.google.com/spanner/docs/queues/queues-using).

## Grants for querying queues directly

To read or inspect messages directly from a queue using standard SQL (`SELECT * FROM QUEUE_NAME`) or the Read API, grant the `SELECT` privilege on the queue:

###  GoogleSQL 
    
    
    GRANT SELECT ON QUEUE QUEUE_NAME TO ROLE ROLE_NAME;

###  PostgreSQL 
    
    
    GRANT SELECT ON QUEUE QUEUE_NAME TO ROLE_NAME;

To revoke the privilege:

###  GoogleSQL 
    
    
    REVOKE SELECT ON QUEUE QUEUE_NAME FROM ROLE ROLE_NAME;

###  PostgreSQL 
    
    
    REVOKE SELECT ON QUEUE QUEUE_NAME FROM ROLE_NAME;

Granting `SELECT` on the queue allows querying the queue as a table, but does not grant `EXECUTE` on `RECEIVE_QUEUE_NAME()` or `RENEWLEASE_QUEUE_NAME()`.

## Grants for acknowledging and deleting messages

To acknowledge or delete messages from a queue using DML (`DELETE FROM`) or the Mutation API (`Ack` or `Delete`), grant the `DELETE` privilege on the queue:

###  GoogleSQL 
    
    
    GRANT DELETE ON QUEUE QUEUE_NAME TO ROLE ROLE_NAME;

###  PostgreSQL 
    
    
    GRANT DELETE ON QUEUE QUEUE_NAME TO ROLE_NAME;

To revoke the privilege:

###  GoogleSQL 
    
    
    REVOKE DELETE ON QUEUE QUEUE_NAME FROM ROLE ROLE_NAME;

###  PostgreSQL 
    
    
    REVOKE DELETE ON QUEUE QUEUE_NAME FROM ROLE_NAME;

## Required privileges for queue operations

The following table summarizes the privileges required for common queue operations:

Operation | Required privileges  
---|---  
Send messages (DML `INSERT` or Mutation API `Send`) | `INSERT` on the queue  
Receive messages (`RECEIVE_QUEUE_NAME()` TVF) | `EXECUTE` on the `RECEIVE_QUEUE_NAME` function  
Extend message lease (`RENEWLEASE_QUEUE_NAME()` TVF) | `EXECUTE` on the `RENEWLEASE_QUEUE_NAME` function  
Acknowledge or delete messages (DML `DELETE` or Mutation API `Ack` or `Delete`) | `DELETE` on the queue  
Read queue data directly (SQL `SELECT` or Read API) | `SELECT` on the queue  
  
## Example: Configure producer and consumer roles

The following example configures separate database roles for a producer, a consumer, and an auditor on a queue named `OrdersQueue`:

###  GoogleSQL 
    
    
    -- Create producer role and grant send permissions
    CREATE ROLE queue_producer;
    GRANT INSERT ON QUEUE OrdersQueue TO ROLE queue_producer;
    
    -- Create consumer role and grant receive, renew, and delete permissions
    CREATE ROLE queue_consumer;
    GRANT EXECUTE ON TABLE FUNCTION RECEIVE_OrdersQueue TO ROLE queue_consumer;
    GRANT EXECUTE ON TABLE FUNCTION RENEWLEASE_OrdersQueue TO ROLE queue_consumer;
    GRANT DELETE ON QUEUE OrdersQueue TO ROLE queue_consumer;
    
    -- Create reader role for inspection without consumer streaming permissions
    CREATE ROLE queue_reader;
    GRANT SELECT ON QUEUE OrdersQueue TO ROLE queue_reader;
    

###  PostgreSQL 
    
    
    -- Create producer role and grant send permissions
    CREATE ROLE queue_producer;
    GRANT INSERT ON QUEUE OrdersQueue TO queue_producer;
    
    -- Create consumer role and grant receive, renew, and delete permissions
    CREATE ROLE queue_consumer;
    GRANT EXECUTE ON FUNCTION spanner.receive_OrdersQueue TO queue_consumer;
    GRANT EXECUTE ON FUNCTION spanner.renewlease_OrdersQueue TO queue_consumer;
    GRANT DELETE ON QUEUE OrdersQueue TO queue_consumer;
    
    -- Create reader role for inspection without consumer streaming permissions
    CREATE ROLE queue_reader;
    GRANT SELECT ON QUEUE OrdersQueue TO queue_reader;
    

## `INFORMATION_SCHEMA` views for queues

The following views show database roles and privileges information for queues:

  * GoogleSQL-dialect databases: [`INFORMATION_SCHEMA.TABLE_PRIVILEGES`](https://docs.cloud.google.com/spanner/docs/information-schema#table-privileges)
  * PostgreSQL-dialect databases: [`information_schema.table_privileges`](https://docs.cloud.google.com/spanner/docs/information-schema-pg#table-privileges)



Because Spanner models queues as table-level schema objects, privileges granted on queues appear in `TABLE_PRIVILEGES`. Privileges granted on queue table-valued functions appear in `ROUTINE_PRIVILEGES`.

The rows in these views are filtered based on the current database role's privileges. This ensures that principals can view only the roles, privileges, and queues that they have access to.

Row filtering also applies to the following queue metadata views:

###  GoogleSQL 

  * `INFORMATION_SCHEMA.TABLES`
  * `INFORMATION_SCHEMA.COLUMNS`



###  PostgreSQL 

  * `information_schema.tables`
  * `information_schema.columns`



Row filtering also applies to the metadata views for queue table-valued functions (`RECEIVE_QUEUE_NAME` and `RENEWLEASE_QUEUE_NAME`):

###  GoogleSQL 

  * [`INFORMATION_SCHEMA.ROUTINES`](https://docs.cloud.google.com/spanner/docs/information-schema#routines)
  * [`INFORMATION_SCHEMA.ROUTINE_OPTIONS`](https://docs.cloud.google.com/spanner/docs/information-schema#routine_options)
  * [`INFORMATION_SCHEMA.ROUTINE_PRIVILEGES`](https://docs.cloud.google.com/spanner/docs/information-schema#routine_privileges)
  * [`INFORMATION_SCHEMA.PARAMETERS`](https://docs.cloud.google.com/spanner/docs/information-schema#parameters)



###  PostgreSQL 

  * [`information_schema.routines`](https://docs.cloud.google.com/spanner/docs/information-schema-pg#routines)
  * [`information_schema.routine_options`](https://docs.cloud.google.com/spanner/docs/information-schema-pg#routine_options)
  * [`information_schema.routine_privileges`](https://docs.cloud.google.com/spanner/docs/information-schema-pg#routine_privileges)
  * [`information_schema.parameters`](https://docs.cloud.google.com/spanner/docs/information-schema-pg#parameters)



The system role `spanner_info_reader` and its members always see an unfiltered `INFORMATION_SCHEMA`.

## Caveats and considerations

  * **Distinct privileges for TVF execution and direct queue queries** : Granting `SELECT` on the queue does not grant `EXECUTE` on the associated table-valued functions (`RECEIVE_QUEUE_NAME` or `RENEWLEASE_QUEUE_NAME`). Similarly, granting `EXECUTE` on the TVF does not grant `SELECT` on the queue.

    * If a role with only `SELECT` on the queue attempts to execute `RECEIVE_QUEUE_NAME()`, Spanner returns an error stating that the role does not have required privileges on table function `RECEIVE_QUEUE_NAME`.
    * If a role with only `EXECUTE` on the TVF attempts to run `SELECT * FROM QUEUE_NAME`, Spanner returns an error stating that the role does not have required privileges on queue `QUEUE_NAME`.
  * **Difference from change streams** : Unlike change streams (which require both `SELECT` on the stream and `EXECUTE` on the read function), queue message consumers require only `EXECUTE` on the `RECEIVE` TVF. They don't require `SELECT` on the queue itself.

  * **Column-level privileges not supported** : Unlike tables, Spanner does not support column-level privileges on queues (such as `GRANT SELECT (COLUMN_NAME) ON QUEUE`). Privileges must be granted on the queue object as a whole because queues include internal system metadata columns.

  * **Separation of producer and consumer roles** : We recommend defining separate database roles for message producers and message consumers. For example:

    * A producer role with only `INSERT` on the queue.
    * A consumer role with `EXECUTE` on the `RECEIVE_QUEUE_NAME` and `RENEWLEASE_QUEUE_NAME` functions, plus `DELETE` on the queue if acknowledging messages with `DELETE` or the `Ack` mutation.
  * **Direct DML vs. Queue TVF delivery** : Direct `DELETE` or `UPDATE` statements bypass the queue leasing and delivery state machine. We recommend restricting these privileges to administrative or maintenance roles.




## What's next

  * [Queues overview](https://docs.cloud.google.com/spanner/docs/queues/queues-overview)
  * [Use queues](https://docs.cloud.google.com/spanner/docs/queues/queues-using)
  * [Queues scenarios and examples](https://docs.cloud.google.com/spanner/docs/queues/queues-examples)
  * [Fine-grained access control overview](https://docs.cloud.google.com/spanner/docs/fgac-about)
  * [Fine-grained access control privileges](https://docs.cloud.google.com/spanner/docs/fgac-privileges)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
