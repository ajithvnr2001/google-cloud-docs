---
url: https://docs.cloud.google.com/spanner/docs/migrate-spanner-pg-to-pg-database/
title: Migrate Spanner to a PostgreSQL-dialect database \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:32:40.094061+00:00
---

# Migrate Spanner to a PostgreSQL-dialect database  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/migrate-spanner-pg-to-pg-database/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Migrate Spanner to a PostgreSQL-dialect database Stay organized with collections  Save and categorize content based on your preferences. 

This page describes key considerations and steps to follow when migrating from Spanner to another PostgreSQL-dialect database if you want to move an application out of Spanner or Google Cloud. You can also use information on this page if you need to understand or demonstrate thefeasibility of moving your database, for example, for _stressed exit_ disaster planning.

Spanner's PostgreSQL interface is the best choice for applications that need the option to deploy to another PostgreSQL-compatible environment, either within Google Cloud or elsewhere. Using familiar syntax and standard clients from the PostgreSQL ecosystem, the PostgreSQL interface lets developers and operators use their existing PostgreSQL knowledge and skills.

It uses the same query processing, transaction coordination, distributed storage, and network infrastructure as the GoogleSQL dialect. If you need a database that supports portability, you're not compromising on Spanner's core scalability, consistency, or price-performance benefits when you select the PostgreSQL interface.

Learn more about the [differences between the PostgreSQL and GoogleSQL dialects](https://docs.cloud.google.com/spanner/docs/choose-googlesql-or-postgres) in Spanner.

At a high level, the steps are the following:

  1. Remove Spanner-specific extensions from queries and DDL statements
  2. Migrate the schema
  3. Migrate the data
  4. Migrate the application



## Spanner-specific considerations

Spanner's PostgreSQL interface supports PostgreSQL queries out of the box, so most SQL queries that run on a Spanner PostgreSQL-dialect database have the same behavior as other PostgreSQL-compatible databases. Using this approach, the number of SQL and data access changes required to move an application from one platform to another is likely low. This makes the porting process quicker, easier, and less prone to error than a similar GoogleSQL-dialect database.

In addition to broad PostgreSQL compatibility, the PostgreSQL interface offers a number of Spanner-specific extensions. If you use these extensions in your applications, you'll have to remove them or map them to PostgreSQL features manually. Some notable examples are given in Query syntax extensions and Schema Management (DDL) extensions.

### Query syntax extensions

Spanner's PostgreSQL interface provides a number of Spanner-specific extensions. Most use the prefix `spanner.` for identification. In the following table, we list these extensions and the actions that you might need to take before the same application can run on a PostgreSQL database.

**Extension kind** | **Specific extensions** | **Actions to take before migration**  
---|---|---  
Spanner-specific functions | 

  * Vector functions listed in the [Mathematical functions list](https://docs.cloud.google.com/spanner/docs/reference/postgresql/functions-and-operators#mathematical) with the `spanner.` prefix
  * [Machine learning functions](https://docs.cloud.google.com/spanner/docs/reference/postgresql/functions-and-operators#ml)
  * [Hash functions](https://docs.cloud.google.com/spanner/docs/reference/postgresql/functions-and-operators#hash-functions)
  * [Date and time functions](https://docs.cloud.google.com/spanner/docs/reference/postgresql/functions-and-operators#spanner-date-time-functions)
  * [Commit timestamp functions](https://docs.cloud.google.com/spanner/docs/commit-timestamp-postgresql).
  * [JSONB functions](https://docs.cloud.google.com/spanner/docs/reference/postgresql/functions-and-operators#spanner-jsonb-functions)
  * [Sequence functions](https://docs.cloud.google.com/spanner/docs/reference/postgresql/functions-and-operators#sequence) with the `spanner.` prefix
  * [Utility functions](https://docs.cloud.google.com/spanner/docs/reference/postgresql/functions-and-operators#utility)

| Find functions prefixed with `spanner.` and remove these calls.   
Type extensions | 

  * [Array data type](https://docs.cloud.google.com/spanner/docs/reference/postgresql/data-types#array-extensions) with the `VECTOR LENGTH` parameter

| Remove the `VECTOR LENGTH` syntax or consider using [pgvector](https://github.com/pgvector/pgvector).   
Query syntax | 

  * [Spanner query hints](https://docs.cloud.google.com/spanner/docs/reference/postgresql/query-syntax#pg_extensions)

| No action required as hints are represented inside comments.   
For details on performance considerations, see Query migration.   
Stored system procedures | 

  * [Query cancellation](https://docs.cloud.google.com/spanner/docs/reference/postgresql/stored-procedures-pg#query-cancellation)

| Remove calls to `spanner.cancel_query()`.   
Optionally, you can replace the calls with a [PostgreSQL equivalent](https://www.postgresql.org/docs/current/libpq-cancel.html).   
SET/SHOW operations |  | Can be ignored as PostgreSQL doesn't have any built-in parameters that begin with `spanner.`, so setting any variables with that prefix doesn't have any impact on expected behavior.  
  
### Schema Management (DDL) extensions

Spanner offers a range of extensions related to data management, as described in the [data definition language (DDL)](https://docs.cloud.google.com/spanner/docs/reference/postgresql/data-definition-language) page.

**Extension** | **Actions to take before migration**  
---|---  
[Interleaved tables](https://docs.cloud.google.com/spanner/docs/schema-and-data-model#create-interleaved-tables)   
Co-locates many-to-one related data in physical storage, making joins across them significantly more efficient.  | Remove the `INTERLEAVE IN` clause.  
[Commit timestamps](https://docs.cloud.google.com/spanner/docs/commit-timestamp-postgresql)   
Enables atomically storing the commit timestamp of a transaction into a column.  | Either replace `SPANNER.COMMIT_TIMESTAMP` with a PostgreSQL timestamp type and manage setting the timestamp in your application or remove that column.   
[Point-in-time recovery](https://docs.cloud.google.com/spanner/docs/reference/postgresql/data-definition-language#alter-database)   
Provides protection against accidental deletion or writes.  | Remove any DDL statements that set `spanner.version_retention_period`.   
[Time to live](https://docs.cloud.google.com/spanner/docs/ttl) (TTL)   
Prompts the automatic deletion of records based on age.  | Remove the `TTL INTERVAL` clause. Consider leveraging a `cron` or scheduled task to periodically delete outdated. rows.   
[Optimizer options](https://docs.cloud.google.com/spanner/docs/query-optimizer/manage-query-optimizer)   
Sets options to minimize any potential for performance regression when the query optimizer or statistics change.  | Remove DDL statements that set optimizer options.   
[Change streams](https://docs.cloud.google.com/spanner/docs/change-streams/manage)   
Watches and streams out a Spanner database's data changes—inserts, updates, and deletes—in near real-time.  | Remove any DDL statements related to change streams.   
[Default leader](https://docs.cloud.google.com/spanner/docs/reference/postgresql/data-definition-language#alter-database)   
Lets you specify the leader for your database in dual- and multi-region configurations. | Remove any DDL statements that set `spanner.default_leader`.   
[Geo-partitioning](https://docs.cloud.google.com/spanner/docs/create-manage-data-placements)   
Lets you further segment and store rows in your database table across different instance configurations.  | Remove any DDL statements related to geo-partitioning.  
[Sequences](https://docs.cloud.google.com/spanner/docs/reference/postgresql/data-definition-language#sequence_statements)   
Spanner only supports the `bit_reversed_positive` sequence. | Replace `bit_reversed_positive` with a sequence available in PostgreSQL. Remove any DDL statements that set `spanner.default_sequence_kind`.  
[Locality groups](https://docs.cloud.google.com/spanner/docs/reference/postgresql/data-definition-language#locality-group-statements)   
Lets you define column group strategy to store columns separately or to use [tiered storage](https://docs.cloud.google.com/spanner/docs/tiered-storage). | Remove any DDL statements related to locality groups.  
[Search indexes](https://docs.cloud.google.com/spanner/docs/reference/postgresql/data-definition-language#search-index-statements)   
Lets you define indexes to perform [full text search](https://docs.cloud.google.com/spanner/docs/full-text-search). | Remove any DDL statements related to search indexes.  
  
## Schema migration

You can export a PostgreSQL-dialect database schema in PostgreSQL syntax. For databases configured to use the PostgreSQL interface, you can achieve this with `psql` using [PGAdapter](https://docs.cloud.google.com/spanner/docs/pgadapter), the sidecar proxy that lets you use standard PostgreSQL drivers or client libraries to connect to Spanner:
    
    
    psql -v ON_ERROR_STOP=1 \
      --host "$PGADAPTER_HOST" \
      --port "$PGADAPTER_PORT" \
      --dbname "$SPANNER_DATABASE" \
      -qAtX \
      -c "show database ddl"
    

You can also use the following `gcloud`command to output the schema as a PostgreSQL-compatible SQL script:
    
    
    gcloud spanner databases ddl describe databasename
    

If the database uses Spanner-specific schema extensions, like those discussed in Schema management extensions, they are listed when you run this command. You need to remove them before migrating the schema to PostgreSQL.

## Data migration

Spanner's PostgreSQL interface supports PostgreSQL's `COPY TO STDIN` and `STDOUT` extensions using [PGAdapter](https://docs.cloud.google.com/spanner/docs/pgadapter). This is one way to load data into and out of Spanner. Read more about the `COPY` command in the [psql command-line tool for Spanner documentation](https://docs.cloud.google.com/spanner/docs/psql-commands#copy-command).

This script exports smaller quantities of data (recommended for less than 100GB of data) from Spanner's PostgreSQL interface into the new PostgreSQL database:
    
    
    psql -h pgadapter-host -c "COPY $TABLE TO STDOUT BINARY" | \
    psql -h postgresql-host -c "COPY $TABLE FROM STDIN BINARY"
    

For larger tables (greater than or equal to100GB of data), you can launch a [Dataflow export to a CSV template](https://docs.cloud.google.com/spanner/docs/import-export-csv#export-to-csv).

You can perform live data migrations using the Debezium Kafka connector to [stream Spanner updates](https://cloud.google.com/blog/products/databases/stream-data-changes-from-spanner-at-scale-with-apache-kafka) into PostgreSQL. You can customize it further if you use the [Spanner Change Streams API](https://docs.cloud.google.com/spanner/docs/change-streams/details#query) to access the Change Data Capture (CDC) streams directly.

## Query migration

The PostgreSQL interface for Spanner implements much of the most common PostgreSQL query syntax, functions, and operators.

If you are using hints in your queries, you don't need to re-write your queries because query hints on Spanner are defined in PostgreSQL-compatible comments:
    
    
    SELECT s.FirstName, s.LastName,
     s.SingerInfo, a.AlbumTitle, a.Charts
    FROM Singers AS s
    LEFT OUTER JOIN/*@JOIN_METHOD=APPLY_JOIN*/ Albums AS a
     ON s.SingerId = a.SingerId;
    

These comments are processed by Spanner's query planner, but a PostgreSQL database ignores these, so you can either include them or remove them.

To achieve optimal performance in the new environment, queries and database schema (such as indexes) might need optimization for the new environment. We recommend that you run benchmark checks to confirm this empirically.

## Application migration

When it comes to connectivity from your applications, your migration strategy depends on the initial choices made when configuring your application to use Spanner, such as whether you use PostgreSQL drivers, Spanner drivers, or Spanner client libraries. This section describes considerations for each option.

### PostgreSQL drivers

Spanner supports common PostgreSQL clients using PGAdaper, a lightweight proxy that translates the PostgreSQL wire protocol into Spanner's low-level gRPC query APIs. If you are using one of these, the change to a different PostgreSQL target involves updating your connection string to point directly to the new PostgreSQL database instead of the PGAdapter proxy. This approach provides good performance and strong compatibility, so it's a good fit for when portability is a top concern. Most queries that run on Spanner's PostgreSQL interface works the same in other PostgreSQL environments. However, the opposite isn't necessarily true; PostgreSQL supports syntax and features that Spanner doesn't support.

### Spanner drivers

These drivers are Spanner-specific implementations for [common languages and application frameworks](https://docs.cloud.google.com/spanner/docs/drivers-overview). For example, the Spanner JDBC (Java) driver implements the same API that the PostgreSQL JDBC driver implements, so applications that use the Spanner JDBC driver can update their build process to link in the equivalent built-in PostgreSQL driver when they want to run the application with PostgreSQL. This option is best if you are already using Spanner or if you are seeking a performant solution that leverages Spanner features like the [Mutations API](https://docs.cloud.google.com/spanner/docs/modify-mutation-api#java), which wouldn't be exposed using a built-in PostgreSQL driver. If you need full compatibility with built-in drivers and value portability, you should instead consider using PostgreSQL's built-in drivers with PGAdapter to ensure some level of application portability.

For more information, see [PostgreSQL drivers and ORMs](https://docs.cloud.google.com/spanner/docs/drivers-overview#postgresql_drivers_and_orms).

### Spanner client libraries

Spanner also offers various [idiomatic client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries) that provide direct access to Spanner without implementing or going through a PostgreSQL-standardized interface. These clients provide maximum access to Spanner-specific features, but are not API-compatible with PostgreSQL drivers. These options offer the highest level of feature performance, but are less portable than the aforementioned options.

## What's next

  * Learn how to [choose between PostgreSQL and GoogleSQL](https://docs.cloud.google.com/spanner/docs/choose-googlesql-or-postgres).
  * Follow the [quickstart](https://docs.cloud.google.com/spanner/docs/create-query-database-console) to create and interact with a PostgreSQL database.
  * Learn more about [Spanner's PostgreSQL language support](https://docs.cloud.google.com/spanner/docs/reference/postgresql/overview).
  * Learn about [PGAdapter](https://docs.cloud.google.com/spanner/docs/pgadapter).
  * Learn about the [PGAdapter GitHub repository](https://github.com/GoogleCloudPlatform/pgadapter).
  * Review [known issues](https://docs.cloud.google.com/spanner/docs/known-issues-postgresql-interface) in the PostgreSQL interface.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
