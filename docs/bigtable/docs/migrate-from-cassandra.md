---
url: https://docs.cloud.google.com/bigtable/docs/migrate-from-cassandra/
title: Migrate from Apache Cassandra to Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:33:48.889305+00:00
---

# Migrate from Apache Cassandra to Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/migrate-from-cassandra/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Migrate from Apache Cassandra to Bigtable

This document guides you through the process of migrating data from Apache Cassandra to Bigtable with minimal disruption. It describes how to use open-source tools, such as the Cassandra to Bigtable proxy adapter or the Cassandra to Bigtable client for Java, to perform the migration. Before you begin, make sure you're familiar with [Bigtable for Cassandra users](https://docs.cloud.google.com/bigtable/docs/cloud-bigtable-for-cassandra-users).

## Choose a migration approach

You can migrate from Apache Cassandra to Bigtable using one of the following approaches:

  * Cassandra to Bigtable proxy adapter lets you connect Cassandra-based applications to Bigtable without changing Cassandra drivers. This approach is ideal for applications that require minimal code changes.
  * Cassandra to Bigtable client for Java lets you integrate directly with Bigtable and replace your Cassandra drivers. This approach is ideal for applications that require high performance and flexibility.



## Cassandra to Bigtable proxy adapter

The Cassandra to Bigtable proxy adapter lets you connect Cassandra-based applications to Bigtable. The proxy adapter functions as a wire-compatible Cassandra interface, and it lets your application interact with Bigtable using CQL. Using the proxy adapter doesn't require you to change Cassandra drivers, and configuration adjustments are minimal.

To set up and configure the proxy adapter, see [Cassandra to Bigtable proxy adapter](https://github.com/GoogleCloudPlatform/cloud-bigtable-ecosystem/blob/main/cassandra-bigtable-migration-tools/cassandra-bigtable-proxy/README.md).

To learn which Cassandra versions support the proxy adapter, see [Supported Cassandra versions](https://github.com/GoogleCloudPlatform/cloud-bigtable-ecosystem/tree/main/cassandra-bigtable-migration-tools/cassandra-bigtable-proxy#supported-cassandra-versions).

### Limitations

The Cassandra to Bigtable proxy adapter provides limited support for certain data types, functions, queries, and clauses.

For more information, see [Cassandra to Bigtable Proxy - Limitations](https://github.com/GoogleCloudPlatform/cloud-bigtable-ecosystem/blob/main/cassandra-bigtable-migration-tools/cassandra-bigtable-proxy/docs/limitations.md).

### Cassandra keyspace

A Cassandra _keyspace_ stores your tables and manages resources in a similar way to a Bigtable instance. The Cassandra to Bigtable proxy adapter handles keyspace naming transparently, so that you can query using the same keyspaces. However, you must create a new [Bigtable instance](https://docs.cloud.google.com/bigtable/docs/creating-instance) to achieve logical grouping of your tables. You must also configure Bigtable replication separately.

### DDL support

The Cassandra to Bigtable proxy adapter supports Data Definition Language (DDL) operations. DDL operations let you create and manage tables directly through CQL commands. We recommend this approach for setting up your schema because it's similar to SQL but you don't need to define your schema in configuration files and then execute scripts to create tables.

The following examples show how the Cassandra to Bigtable proxy adapter supports DDL operations:

  * To create a Cassandra table using CQL, run the `CREATE TABLE` command:
        
        CREATE TABLE keyspace.table (
            id bigint,
            name text,
            age int,
            PRIMARY KEY ((id), name)
        );
        

  * To add a new column to the table, run the `ALTER TABLE` command:
        
        ALTER TABLE keyspace.table ADD email text;
        

  * To delete a table, run the `DROP TABLE` command:
        
        DROP TABLE keyspace.table;
        




For more information, see [DDL Support for Schema Creation (Recommended Method)](https://github.com/GoogleCloudPlatform/cloud-bigtable-ecosystem/tree/main/cassandra-bigtable-migration-tools/cassandra-bigtable-proxy#ddl-support-for-schema-creation-recommended-method).

### DML support

The Cassandra to Bigtable proxy adapter supports Data Manipulation Language (DML) operations such as `INSERT`, `DELETE`, `UPDATE`, and `SELECT`.

To run the raw DML queries, all values except numerics must have single quotes, as shown in the following examples:

  * SELECT * FROM keyspace.table WHERE name='john doe';
        

  * INSERT INTO keyspace.table (id, name) VALUES (1, 'john doe');
        




### Achieve zero downtime migration

You can use the Cassandra to Bigtable proxy adapter with the open-source [Zero Downtime Migration (ZDM) proxy tool](https://github.com/datastax/zdm-proxy) and the [Cassandra data migrator](https://github.com/datastax/cassandra-data-migrator) tool to migrate data with minimal downtime.

The following diagram shows the steps for migrating from Cassandra to Bigtable using the proxy adapter:

![The process of migrating Cassandra to Bigtable.](https://docs.cloud.google.com/static/bigtable/img/migrate-cassandra-to-bt-diagram.png) **Figure 1.** The process of migrating Cassandra to Bigtable (click to enlarge).![](https://docs.cloud.google.com/static/bigtable/img/migrate-cassandra-to-bt-diagram.png)

To migrate Cassandra to Bigtable, follow these steps:

  1. Connect your Cassandra application to the ZDM proxy tool.
  2. Enable dual writes to Cassandra and Bigtable.
  3. Move data in bulk using the [Cassandra data migrator](https://github.com/datastax/cassandra-data-migrator) tool.
  4. Validate your migration. Once validated, you can terminate the connection to Cassandra and connect directly to Bigtable.



When using the proxy adapter with the ZDM proxy tool, the following migration capabilities are supported:

  * **Dual writes** : maintain data availability during migration
  * **Asynchronous reads** : scale and stress-test your Bigtable instance
  * **Automated data verification and reporting** : ensure data integrity throughout the process
  * **Data mapping** : map field and data types to meet your production standards



To practice migrating Cassandra to Bigtable, see the [Migration from Cassandra to Bigtable with a Dual-Write Proxy](https://codelabs.developers.google.com/codelabs/cbt-for-cassandra) codelab.

## Cassandra to Bigtable client for Java

You can integrate directly with Bigtable and replace your Cassandra drivers, the Cassandra to Bigtable client for Java library lets you integrate Cassandra-based Java applications with Bigtable using CQL.

For instructions on building the library and including the dependency in application code, see [Cassandra to Bigtable Client for Java](https://github.com/GoogleCloudPlatform/cloud-bigtable-ecosystem/blob/main/cassandra-bigtable-migration-tools/cassandra-bigtable-java-client/cassandra-bigtable-java-client-lib/README.md).

The following example shows how to configure your application with the Cassandra to Bigtable client for Java:
    
    
    import com.datastax.oss.driver.api.core.CqlSession;
    import com.datastax.oss.driver.api.core.cql.BoundStatement;
    import com.datastax.oss.driver.api.core.cql.PreparedStatement;
    import com.datastax.oss.driver.api.core.cql.ResultSet;
    import com.datastax.oss.driver.api.core.cql.Row;
    import com.google.bigtable.cassandra.BigtableCqlConfiguration;
    import com.google.bigtable.cassandra.BigtableCqlSessionFactory;
    
    /**
     * Example using Bigtable CQLSession
     */
    public class ExampleWithBigtableCqlSession {
    
      public static void main(String[] args) {
    
        // Construct BigtableCqlConfiguration
        BigtableCqlConfiguration bigtableCqlConfiguration = BigtableCqlConfiguration.builder()
            .setProjectId("example-project-id")
            .setInstanceId("example-instance-id")
            .setDefaultColumnFamily("example-column-family")
            .setBigtableChannelPoolSize(4)
            .build();
    
        // Create CqlSession with BigtableCqlConfiguration
        BigtableCqlSessionFactory bigtableCqlSessionFactory = new BigtableCqlSessionFactory(bigtableCqlConfiguration);
    
        // Create CqlSession
        try (CqlSession session = bigtableCqlSessionFactory.newSession()) {
    
          // Create a table
          String createTableQuery = "CREATE TABLE <KEYSPACE>.<TABLE_NAME> (<COLUMN> <TYPE> PRIMARY KEY);";
          session.execute(createTableQuery);
    
          // Prepare an insert statement
          PreparedStatement preparedInsert = session.prepare(
              "INSERT INTO <KEYSPACE>.<TABLE_NAME> (<COLUMN>) VALUES (?)" // replace with your keyspace, table and columns
          );
    
          // Insert
          BoundStatement boundInsert = preparedInsert
              .bind()
              .setString("<COLUMN>", "<VALUE>");
          session.execute(boundInsert);
    
          // Query for all entries
          ResultSet resultSet = session.execute("SELECT <COLUMN> FROM <KEYSPACE>.<TABLE_NAME>;");
          // Print results
          for (Row row : resultSet) {
            System.out.println(row);
          }
    
        }
    
      }
    
    }
    
    [ExampleWithBigtableCqlSession.java](https://github.com/GoogleCloudPlatform/cloud-bigtable-ecosystem/blob/0982eb87525e0bae9bc7ff74a611e69eb99500d8/cassandra-bigtable-migration-tools/cassandra-bigtable-java-client/example/src/main/java/ExampleWithBigtableCqlSession.java#L16-L71)

## Understand performance

Bigtable is designed for high throughput, low latency, and massive scalability. It can handle millions of requests per second on petabytes of data. When you migrate from Cassandra using either the Cassandra to Bigtable client for Java or the Cassandra to Bigtable proxy adapter, understand the following performance implications:

### Client and proxy overhead

Both migration approaches introduce minimal performance overhead. They act as a translation layer between the Cassandra Query Language (CQL) and the Bigtable Data API, which is optimized for efficiency.

### Performance with Cassandra collection types

If your Cassandra data model uses collection types such as maps, sets, or lists to implement dynamic schemas, then Bigtable can handle these patterns effectively. Both the proxy adapter and the client for Java map these collection operations to Bigtable's underlying data model, which is well-suited for sparse and wide datasets.

Element-level operations within these collections are highly efficient. This includes the following actions:

  * To read or write a single value in a map.
  * To add or remove an element from a set.
  * To append or prepend an element to a list.



Bigtable optimizes these types of point operations on individual collection elements, and their performance is identical to operations on standard scalar columns.

### Benchmark your workload

Bigtable performance can vary depending on your workload, schema design, data access patterns, and cluster configuration. To get accurate performance metrics for your use case and ensure that Bigtable meets your specific requirements, we recommend that you benchmark your Cassandra workloads against Bigtable using one of the migration approaches.

For more information about Bigtable performance best practices, see [Understand performance](https://docs.cloud.google.com/bigtable/docs/performance).

## Additional Cassandra open-source tools

Because of the wire compatibility of the Cassandra to Bigtable proxy adapter with CQL lets you use additional tools in the Cassandra open-source ecosystem. These tools include the following:

  * [**Cqlsh**](https://cassandra.apache.org/doc/latest/cassandra/managing/tools/cqlsh.html): The CQL shell lets you connect directly to Bigtable through the proxy adapter. You can use it for debugging and quick data lookups using CQL.
  * [**Cassandra Data Migrator (CDM)**](https://github.com/datastax/cassandra-data-migrator): This Spark-based tool is suitable for migrating large volumes (up to billions of rows) of historical data. The tool provides validation, diff reporting, and replay capabilities, and it's fully compatible with the proxy adapter.



## What's next

  * [Schema design best practices](https://docs.cloud.google.com/bigtable/docs/schema-design)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
