---
url: https://docs.cloud.google.com/sql/docs/postgres/extensions/
title: Configure PostgreSQL extensions \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:33.399394+00:00
---

# Configure PostgreSQL extensions  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/extensions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Configure PostgreSQL extensions Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

You can extend PostgreSQL by bundling SQL objects into a package and using them as a unit. This page contains information about configuring the PostgreSQL extensions that Cloud SQL supports.

## Use PostgreSQL extensions

You can install only the extensions that Cloud SQL supports. For more information, see PostgreSQL extensions supported by Cloud SQL.

**Note:** You can only install extensions on the primary instance, not the read replica. Once installed, the extension replicates to the read replica.

### Install an extension

Before using an extension, install it:

  * In the psql tool, run the [CREATE EXTENSION](https://www.postgresql.org/docs/current/static/sql-createextension.html) command.

**Note:** You must set flags before creating some extensions, such as `pglogical`. For more information, see [Configure external replicas](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-external-replica).

### Update an extension

Although Cloud SQL for PostgreSQL maintenance updates automatically install the latest extension binaries on your instance's underlying software, they don't automatically update the extension's database catalog. You are responsible for manually updating your extensions to make sure they use the latest supported versions.

To determine which extensions require an update, compare your installed version with the latest supported version listed in the PostgreSQL extensions supported by Cloud SQL tables.

Connect to your database and run the following command to see your installed versions:
    
    
    SELECT * FROM pg_extension;
    

To update an extension to the latest version available on your instance, use the `ALTER EXTENSION` command.

Connect to the primary instance using a client of your choice, such as [Cloud SQL Studio](https://docs.cloud.google.com/sql/docs/postgres/manage-data-using-studio) or the `psql` client, and run the following command for each extension that you want to update:
    
    
    ALTER EXTENSION EXTENSION_NAME UPDATE;
    

If you need to update to a specific version, then use the following syntax:
    
    
    ALTER EXTENSION EXTENSION_NAME
    UPDATE TO 'VERSION_NUMBER';
    

### Requirement for superuser privileges

In Cloud SQL, extensions can only be created by users that are part of the `cloudsqlsuperuser` role. When you create a new PostgreSQL instance, the default `postgres` user is created for you (although you must set the user's password). The default `postgres` user is part of the `cloudsqlsuperuser` role. For more information, see [About PostgreSQL users](https://docs.cloud.google.com/sql/docs/postgres/users).

**Note:** If you import a database containing an extension that was created by a custom user, you can't delete that user without deleting the entire imported database.

### Inter-database connections

The target instances for connections must be in the same VPC network as the connecting instance.

For cluster instances, you can't choose the **Require trusted client certificates** option in the Google Cloud console. Additionally, to connect to databases within the same instance, you cannot set host to localhost or to `127.0.0.1`. Instead, you must use the IP address shown for your instance in the Google Cloud console.

### Request support for a new extension

You cannot create your own extensions in Cloud SQL.

To request support for an extension, click **+1** on the open issue or create a new issue. For a list of open Cloud SQL issues and information about creating new issues, see [Search for or create issues and feature requests, by product](https://docs.cloud.google.com/support/docs/issue-trackers#trackers-list).

## PostgreSQL extensions supported by Cloud SQL

For information about using a specific extension, see the documentation link in one of the tables below.

Cloud SQL support for PostgreSQL extensions can be divided into these categories:

  * PostGIS extensions
  * Data type extensions
  * Language extensions
  * Miscellaneous extensions



### PostGIS

The [PostGIS extension](https://postgis.net) is supported for Cloud SQL for PostgreSQL for all major versions.

The following table contains the PostGIS extension versions for each Cloud SQL for PostgreSQL version: 

**Cloud SQL for PostgreSQL version** | **PostGIS extension**  
---|---  
PostgreSQL 9.6 | 3.2.5  
PostgreSQL 10 | 3.2.5  
PostgreSQL 11 | 3.2.5  
PostgreSQL 12 | 3.4.4  
PostgreSQL 13 | 3.5.2  
PostgreSQL 14 | 3.5.2  
PostgreSQL 15 | 3.5.2  
PostgreSQL 16 | 3.5.2  
PostgreSQL 17 | 3.5.2  
PostgreSQL 18 | 3.6.0  
  
For a specific PostgreSQL major version, in the [CREATE EXTENSION](https://www.postgresql.org/docs/current/static/sql-createextension.html) command, you can specify a PostGIS extension version by using the `VERSION` clause.

The PostGIS extension includes the following:

  * [`postgis`](http://www.postgis.net/)
  * [`postgis_raster`](https://postgis.net/docs/RT_reference.html)
  * [`postgis_sfcgal`](http://www.sfcgal.org/)
  * [`postgis_tiger_geocoder`](http://postgis.net/docs/Geocode.html)
  * [`postgis_topology`](http://postgis.net/docs/manual-dev/Topology.html)
  * [`address_standardizer`](https://postgis.net/docs/manual-dev/Extras.html)
  * [`address_standardizer_data_us`](https://postgis.net/docs/manual-dev/Extras.html)



For more information, see [PostGIS Installation](http://postgis.net/docs/manual-2.3/postgis_installation.html).

Additionally, Cloud SQL for PostgreSQL includes version 3.6.2 of the [`pgRouting`](https://github.com/pgRouting) extension, which extends PostGIS. The `pgRouting` extension enhances geospatial processing through network routing and analysis.

You can upgrade PostGIS and its related extensions to their latest version manually. To learn more about upgrading your PostGIS extensions, see [Upgrading PostGIS](https://postgis.net/workshops/postgis-intro/upgrades.html#upgrading-postgis).

### Data type extensions

**Extension** | **Description**  
---|---  
[btree_gin](https://www.postgresql.org/docs/current/static/btree-gin.html) | Provides sample GIN operator classes that implement B-tree equivalent behavior.  
PostgreSQL 9.6 uses version 1.0. PostgreSQL 10 uses version 1.2. PostgreSQL 11 and later use version 1.3.   
[btree_gist](https://www.postgresql.org/docs/current/static/btree-gist.html) | Provides GiST index operator classes that implement B-tree equivalent behavior.  
PostgreSQL 9.6 uses version 1.2. PostgreSQL 10, 11, 12, and 13 use version 1.5. PostgreSQL 14 uses version 1.6. PostgreSQL 15, 16, and 17 use version 1.7. PostgreSQL 18 uses version 1.8.   
[chkpass](https://www.postgresql.org/docs/10/static/chkpass.html) | Implements a data type `chkpass` that is designed for storing encrypted passwords.   
PostgreSQL 9.6 and 10 use version 1.0. Not supported for other versions.   
[citext](https://www.postgresql.org/docs/current/static/citext.html) | Provides a case-insensitive character string type `citext`.  
PostgreSQL 9.6 uses version 1.3. PostgreSQL 10 uses version 1.4. PostgreSQL 11 uses version 1.5. PostgreSQL 12, 13, 14, 15, 16, and 17 use version 1.6. PostgreSQL 18 uses version 1.8.   
[cube](https://www.postgresql.org/docs/current/static/cube.html) | Implements a data type `cube` for representing multidimensional cubes.  
PostgreSQL 9.6 and 10 use version 1.2. PostgreSQL 11 uses version 1.3. PostgreSQL 12 and 13 use version 1.4. PostgreSQL 14 and later use version 1.5.   
[hstore](https://www.postgresql.org/docs/current/static/hstore.html) | Implements the `hstore` data type for storing sets of key/value pairs within a single PostgreSQL value.  
PostgreSQL 9.6 and 10 use version 1.4. PostgreSQL 11 uses version 1.5. PostgreSQL 12 uses version 1.6. PostgreSQL 13 uses version 1.7. PostgreSQL 14 and later use version 1.8.   
[ip4r](https://github.com/RhodiumToad/ip4r) | Provides data types for IPv4/v6 addresses, and address ranges, plus index support.  
Cloud SQL for PostgreSQL uses version 2.4.2.   
[isn](https://www.postgresql.org/docs/current/static/isn.html) | Provides data types for some international product numbering standards.   
PostgreSQL 9.6 and 10 use version 1.1. PostgreSQL 11, 12, 13, 14, 15, 16, and 17 use version 1.2. PostgreSQL 18 uses version 1.3.   
[lo](https://www.postgresql.org/docs/current/static/lo.html) | Support for managing Large Objects (also called LOs or BLOBs).  
Cloud SQL for PostgreSQL uses version 1.1.   
[ltree](https://www.postgresql.org/docs/current/static/ltree.html) | Implements a data type `ltree` for representing labels of data stored in a hierarchical tree-like structure.   
PostgreSQL 9.6, 10, 11, and 12 use version 1.1. PostgreSQL 13, 14, 15, and 16 use version 1.2. PostgreSQL 17 uses version 1.3.   
[postgresql-hll](https://github.com/citusdata/postgresql-hll) | Introduces a new data type, `hll`, which is a HyperLogLog data structure. Also see postgresql-hll in this document.  
Cloud SQL for PostgreSQL uses version 2.18.  
[prefix](https://github.com/dimitri/prefix) | Provides prefix-matching, plus index support.  
Cloud SQL for PostgreSQL uses version 1.2.0.   
  
### Language extensions

**Extension** | **Description**  
---|---  
[plpgsql](https://www.postgresql.org/docs/current/static/plpgsql.html) | A loadable procedural language for creating functions, procedures and triggers. You also can use this language for direct execution of code in DO blocks.  
Cloud SQL for PostgreSQL uses version 1.0.   
[plv8](https://plv8.github.io/) | Provides a procedural language for enabling JavaScript.  
Cloud SQL for PostgreSQL uses version 3.2.2, which in turn uses V8 JavaScript engine version 11.5.   
  
### Miscellaneous extensions

**Extension** | **Description**  
---|---  
[ amcheck](https://www.postgresql.org/docs/current/amcheck.html) | Provides functions for verifying the logical consistency of the structure of relations, enabling the pg_amcheck application to check for corruption.   
[ auto_explain](https://www.postgresql.org/docs/current/auto-explain.html) | Enables automatic logging of execution plans of slow statements, for troubleshooting and more. Provides an automated way to perform the functionality of the [ EXPLAIN](https://www.postgresql.org/docs/9.1/sql-explain.html) command. Also see auto_explain in this document.  
[ autoinc](https://www.postgresql.org/docs/current/static/contrib-spi.html#CONTRIB-SPI-AUTOINC) | Provides functions for incrementing fields automatically. This trigger stores the next value of a sequence into an integer field.  
Cloud SQL for PostgreSQL uses version 1.0.   
[ bloom](https://www.postgresql.org/docs/current/static/bloom.html) | Provides a method to access indexes based on bloom filters. A bloom filter is a space-efficient data structure that you can use to test whether an element is a member of a set.  
Cloud SQL for PostgreSQL uses version 1.0.   
[ dblink](https://www.postgresql.org/docs/current/dblink.html) | Provides functions to connect to PostgreSQL databases from within a database session. Also see  dblink in this document.  
Cloud SQL for PostgreSQL uses version 1.2. **Note:** If you're [using Private Service Connect to connect to a Cloud SQL instance](https://docs.cloud.google.com/sql/docs/postgres/configure-private-service-connect), then you need to [enable PSC outbound connectivity](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect#psc-outbound) to use this extension.   
[ decoderbufs](https://github.com/debezium/postgres-decoderbufs) | A PostgreSQL logical decoder that delivers output data as Protocol Buffers, adapted for Debezium.   
[dict_int](https://www.postgresql.org/docs/current/static/dict-int.html) | An add-on dictionary template for full-text search that controls the indexing of integers.  
Cloud SQL for PostgreSQL uses version 1.0.   
[earthdistance](https://www.postgresql.org/docs/current/static/earthdistance.html) | Provides two approaches to calculating great circle distances on the surface of the Earth.  
PostgreSQL 9.6, 10, 11, 12, 13, 14, 15, and 16 use version 1.1. PostgreSQL 17 and 18 use version 1.2.   
[fuzzystrmatch](https://www.postgresql.org/docs/current/static/fuzzystrmatch.html) | Provides several functions to determine similarities and distance between strings.  
PostgreSQL 9.6, 10, 11, 12, 13, 14 and 15 use version 1.1. PostgreSQL 16 and later use version 1.2   
[google_ml_integration](https://docs.cloud.google.com/sql/docs/postgres/work-with-vectors#required-database-extensions) | [Generates vector embeddings](https://docs.cloud.google.com/sql/docs/postgres/work-with-vectors) to translate text prompts into numerical vectors using a large language model (LLM).  
PostgreSQL 12 and later use version 1.4.3. Not supported for other versions.   
[google_read_only_session](https://docs.cloud.google.com/sql/docs/postgres/read-only-sessions#allowlist) | When write access is temporarily or permanently restricted during a session by the [`cloudsql_session_read_only` flag](https://docs.cloud.google.com/sql/docs/postgres/read-only-sessions), the `google_read_only_session` extension allowlists the following: 

  * All built-in volatile C functions that are considered safe for read-only mode.
  * All safe functions from extensions that are loaded in the database, including the handler functions for `pl/pgsql` and `pl/v8` languages.

  
[ insert_username](https://www.postgresql.org/docs/current/static/contrib-spi.html#CONTRIB-SPI-INSERT-USERNAME) | Provides functions for storing the current user's name into a text field. You can use this to track who last modified a row in a database table.  
Cloud SQL for PostgreSQL uses version 1.0.   
[intagg](https://www.postgresql.org/docs/current/static/intagg.html) | Provides an integer aggregator and an enumerator.  
Cloud SQL for PostgreSQL uses version 1.1.   
[intarray](https://www.postgresql.org/docs/current/static/intarray.html) | Provides a set of functions and operators for manipulating null-free arrays of integers and performing indexed searches on them.  
PostgreSQL 9.6, 10, 11, and 12 use version 1.2. PostgreSQL 13 uses version 1.3. PostgreSQL 14 and later use version 1.5.   
[ moddatetime](https://www.postgresql.org/docs/current/static/contrib-spi.html#CONTRIB-SPI-MODDATETIME) | Provides functions for storing the current time into a `timestamp` field. You can use this to track the last time that a row in a database table is modified.  
Cloud SQL for PostgreSQL uses version 1.0.   
[ oracle_fdw](https://github.com/laurenz/oracle_fdw) | Provides a foreign data wrapper (fdw) for accessing Oracle databases easily and efficiently.  
Cloud SQL for PostgreSQL uses version 1.2.  
  
If you're using Private Service Connect to connect to your Cloud SQL instance, then you need to [enable Private Service Connect outbound connectivity](https://docs.cloud.google.com/sql/docs/postgres/configure-private-service-connect#configure-psc-outbound) to use this extension.   
[ orafce](https://github.com/orafce/orafce) | Provides functions and operators that emulate a subset of functions and packages from an Oracle database. Use these functions to port Oracle applications to PostgreSQL.  
PostgreSQL 9.6 and 10 use version 3.25. PostgreSQL 11 and later use version 4.13.   
[ pageinspect](https://www.postgresql.org/docs/11/pageinspect.html) | Inspects the contents of database pages at a low level. Also see pageinspect in this document.  
PostgreSQL 9.6 uses version 1.5. PostgreSQL 10 uses version 1.6. PostgreSQL 11 and 12 use version 1.7. PostgreSQL 13 and 14 use version 1.8. PostgreSQL 15 uses version 1.11. PostgreSQL 16 and 17 use version 1.12. PostgreSQL 18 uses version 1.13.   
[pgAudit](https://github.com/pgaudit/pgaudit) | Collects audit data.  


  * PostgreSQL 9.6 uses [pgAudit, version 1.1.4](https://github.com/pgaudit/pgaudit/tree/1.1.4#pgauditlog).
  * PostgreSQL 10 uses [pgAudit, version 1.2.3](https://github.com/pgaudit/pgaudit/tree/1.2.3#pgauditlog).
  * PostgreSQL 11 uses [pgAudit, version 1.3.3](https://github.com/pgaudit/pgaudit/tree/1.3.3#pgauditlog).
  * PostgreSQL 12 uses [pgAudit, version 1.4.2](https://github.com/pgaudit/pgaudit/tree/1.4.2#pgauditlog).
  * PostgreSQL 13 uses [pgAudit, version 1.5.1](https://github.com/pgaudit/pgaudit/tree/1.5.1#pgauditlog).
  * PostgreSQL 14 uses [pgAudit, version 1.6.1](https://github.com/pgaudit/pgaudit/tree/1.6.1#pgauditlog).
  * PostgreSQL 15 uses [pgAudit, version 1.7.0](https://github.com/pgaudit/pgaudit/tree/1.7.0#pgauditlog).
  * PostgreSQL 16 uses [pgAudit, version 16.0](https://github.com/pgaudit/pgaudit/tree/16.0#pgauditlog).
  * PostgreSQL 17 uses [pgAudit, version 17.0](https://github.com/pgaudit/pgaudit/tree/17.0#pgauditlog).
  * PostgreSQL 18 uses [pgAudit, version 18.0](https://github.com/pgaudit/pgaudit/tree/18.0#pgauditlog).

Possible values to set for the audit log files for all versions of pgAudit are `READ`, `WRITE`, `FUNCTION`, `ROLE`, `DDL`, `MISC`, and `ALL`. For versions 1.4.2 and above, you can also set the value of `MISC_SET`. For more information about using this extension with Cloud SQL, see [ Audit for PostgreSQL using pgAudit](https://docs.cloud.google.com/sql/docs/postgres/pg-audit).  
[ pg_background](https://github.com/vibhorkum/pg_background#postgres-background-worker) | Lets you run arbitrary commands in a background worker.  
PostgreSQL 17 and earlier use version 1.3. PostgreSQL 18 uses version 1.4.   
[pg_bigm](https://pgbigm.osdn.jp/index_en.html) | Enables full-text search, and allows a two-gram (bigram) index for faster full-text search. Also see pg_bigm in this document.   
[pg_buffercache](https://www.postgresql.org/docs/current/static/pgbuffercache.html) | Provides a means for examining what's happening in the shared buffer cache in real time.   
PostgreSQL 9.6 uses version 1.2. PostgreSQL 10, 11, 12, 13, 14 and 15 use version 1.3. PostgreSQL 16 uses version 1.4. PostgreSQL 17 and later use version 1.5.   
[pg_cron](https://github.com/citusdata/pg_cron) | Provides a cron-based job scheduler. This extension enables cron syntax to schedule PostgreSQL commands directly from the database. For more information about the extension, see pg_cron in this document.   
PostgreSQL versions 10 and later use version 1.6.4.  
[pgcrypto](https://www.postgresql.org/docs/current/static/pgcrypto.html) | Provides cryptographic functions for PostgreSQL.  
Cloud SQL for PostgreSQL uses version 1.3.   
[ pglogical](https://github.com/2ndQuadrant/pglogical) | Provides logical replication for PostgreSQL. See [ Setting up logical replication and decoding](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-logical-replication).  
PostgreSQL 17 and earlier use version 2.4.5. PostgreSQL 18 uses version 2.4.6. **Note:** If you're [using Private Service Connect to connect to a Cloud SQL instance](https://docs.cloud.google.com/sql/docs/postgres/configure-private-service-connect), then you need to [enable PSC outbound connectivity](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect#psc-outbound) to use this extension.   
[pgfincore](https://github.com/klando/pgfincore) | A set of functions to manage pages in operating system disk cache memory from PostgreSQL. Also see pgfincore in this document.  
Cloud SQL for PostgreSQL uses version 1.4.   
[ pg_freespacemap](https://www.postgresql.org/docs/11/pgfreespacemap.html) | Examines the free space map (FSM). Also see pg_freespacemap in this document.  
PostgreSQL 17 and earlier uses version 1.2. PostgreSQL 18 uses version 1.3.   
[pg_hint_plan](https://pghintplan.osdn.jp/pg_hint_plan.html) | Enables you to improve PostgreSQL execution plans using hints, which are simple descriptions in SQL comments. Also see pg_hint_plan in this document.   
[pgoutput](https://www.postgresql.org/docs/current/logical-replication-architecture.html) | This plugin is used by logical replication for change data capture. `pgoutput` is a default plugin and is therefore supported on all versions of Cloud SQL for PostgreSQL.   
[pg_ivm](https://github.com/sraoss/pg_ivm/) | Enables you to make materialized views up-to-date in which only incremental changes are computed and applied on views rather than recomputing the contents from scratch.  
PostgreSQL versions 13 and later support version 1.9. **Warning:** Due to inherent limitations, this extension is incompatible with certain Cloud SQL for PostgreSQL operations: 

  * [In-place major version upgrade](https://docs.cloud.google.com/sql/docs/postgres/upgrade-major-db-version-inplace)
  * [Exporting data](https://docs.cloud.google.com/sql/docs/postgres/import-export/import-export-dmp)
  * [Data Migration Service](https://docs.cloud.google.com/database-migration)

If users want to use any of these operations, they must first remove the extension, complete the operation, and then reapply the extension.   
[pg_partman](https://github.com/pgpartman/pg_partman/) | Helps you create and manage time-based and serial-based table partition sets. Also see pg_partman in this document.  
PostgreSQL versions 14 and later support version 5.4.3 while PostgreSQL versions that are earlier than 14 support only up to version 4.7.4.   
[pg_prewarm](https://www.postgresql.org/docs/current/static/pgprewarm.html) | Provides a convenient way to load relation data into either the operating system buffer cache or the PostgreSQL buffer cache.   
PostgreSQL 9.6 and 10 use version 1.1. PostgreSQL 11 and later use version 1.2.   
[pg_qualstats](https://github.com/powa-team/pg_qualstats) | Collects statistics about predicates, which can help you find which indexes are missing.  
Cloud SQL for PostgreSQL uses version 2.1.2.  
  
[plpgsql_check](https://github.com/okbob/plpgsql_check) | A static analysis linter tool for PL/pgSQL, the native stored procedure language in PostgreSQL.  
Cloud SQL for PostgreSQL uses version 2.8.  
This extension is supported for PostgreSQL versions 14 and later.  
**Note:** [Tracer](https://github.com/okbob/plpgsql_check/blob/master/README.md#tracer) functionality is not supported in Cloud SQL for PostgreSQL.   
[pg_proctab](https://gitlab.com/pg_proctab/pg_proctab) | Enables you to use [pg_top](https://pg_top.gitlab.io/) with Cloud SQL for PostgreSQL, and generate reports from the operating system process table. Also see pg_proctab in this document.   
[pg_repack](http://reorg.github.io/pg_repack/) | Lets you remove bloat from tables and indexes. Optionally, lets you perform an online CLUSTER (order tables by cluster index). Also see pg_repack in this document.  
Cloud SQL for PostgreSQL uses version 1.5.2.   
[pg_roaringbitmap](https://github.com/ChenHuajun/pg_roaringbitmap) | The `pg_roaringbitmap` extension introduces a roaring bitmap data type that enables highly efficient storage and fast set operations on large collections of integers. It dynamically stores integers in compressed forms (arrays, bitmaps, or run containers) based on their density, significantly reducing storage footprint and accelerating common operations like union, intersection, and cardinality calculations.  
Available in PostgreSQL 12 onwards. Cloud SQL for PostgreSQL uses version 0.5 of pg_roaringbitmap.   
[pgrowlocks](https://www.postgresql.org/docs/current/static/pgrowlocks.html) | Provides row locking information for the specified table.  
Cloud SQL for PostgreSQL uses version 1.2.   
[pgstattuple](https://www.postgresql.org/docs/current/static/pgstattuple.html) | Provides various functions to obtain tuple-level statistics.   
PostgreSQL 9.6 uses version 1.4. All other versions use version 1.5.   
[pg_similarity](https://github.com/eulerto/pg_similarity) | Provides support for similarity queries on PostgreSQL.  
Cloud SQL for PostgreSQL uses version 1.0.   
[ pg_squeeze](https://github.com/cybertec-postgresql/pg_squeeze) | Removes unused space from a table and optionally uses an index to sort records or rows (tuples) of the table. For more information about this extension, see pg_squeeze in this document.  
PostgreSQL 11 uses version 1.5 of the extension.  
PostgreSQL 12, 13, 14, 15, 16, and 17 use version 1.8 of the extension.  
PostgreSQL 18 uses version 1.9 of the extension.   
[ pg_textsearch](https://github.com/timescale/pg_textsearch) | provides full-text search using the industry-standard BM25 (Best Matching 25) scoring algorithm to deliver highly accurate relevance scoring. For more information about this extension, see [Full-text search using `pg_textsearch`](https://docs.cloud.google.com/sql/docs/postgres/pg-textsearch).  
Requires PostgreSQL 17 or later.   
[pg_stat_statements](https://www.postgresql.org/docs/current/static/pgstatstatements.html) | Provides a means for tracking execution statistics of all SQL statements executed.   
PostgreSQL 9.6 uses version 1.4. PostgreSQL 10 and 11 use version 1.6. PostgreSQL 12 uses 1.7. PostgreSQL 13 uses 1.8. PostgreSQL 14 uses 1.9. PostgreSQL 15 and 16 use 1.10. PostgreSQL 17 uses 1.11. PostgreSQL 18 uses 1.12.   
[pgTAP](https://pgtap.org/) | Provides a unit testing framework for PostgreSQL, written in PL/pgSQL and PL/SQL.  
Cloud SQL for PostgreSQL uses version 1.3.0.   
[pg_trgm](https://www.postgresql.org/docs/current/static/pgtrgm.html) | Provides functions and operators for determining the similarity of alphanumeric text based on trigram matching, as well as index operator classes that support fast searching for similar strings.   
PostgreSQL 9.6 and 10 use version 1.3. PostgreSQL 11 and 12 use version 1.4. PostgreSQL 13 uses 1.5. PostgreSQL 14 and later use version 1.6.   
[pgtt](https://github.com/darold/pgtt) | Creates and manages DB2 or Oracle-style global temporary tables in a PostgreSQL database.  
PostgreSQL 9.6, 10 and 11 use version 3.0. PostgreSQL 12 and later use version 4.0.  
[pgvector](https://github.com/pgvector/pgvector) |  An open-source extension for storing and searching vector embeddings in PostgreSQL databases.  
PostgreSQL versions 13 and later support version 0.8.5, PostgreSQL version 12 supports up to version 0.7.4, and PostgreSQL version 11 supports up to version 0.5.1. **Note:** The recommended TOAST storage mode for pgvector 0.6.0 with PostgreSQL version 12 is `extended`. For versions 13 and later, the storage mode is `external` for optimal performance. If you're using pgvector 0.6.0 with version 12, and then upgrade to a major version, we recommend that you modify the storage mode to `external` as follows:   
`ALTER TYPE vector SET (STORAGE = external);`.   
[pg_visibility](https://www.postgresql.org/docs/11/pgvisibility.html) | Provides a way to examine the visibility map (VM) and the page-level visibility information of a table. Also see pg_visibility in this document.  
Cloud SQL for PostgreSQL uses version 1.2.   
[ pg_wait_sampling](https://github.com/postgrespro/pg_wait_sampling) | Collects sampling statistics of wait events, providing wait event data for processes on servers. Cloud SQL for PostgreSQL uses version 1.1.5.   
[PL/Proxy](https://plproxy.github.io/) | Procedural language handler that allows remote procedure calls among PostgreSQL databases, with optional sharding. Also see PL/Proxy in this document.  
Cloud SQL for PostgreSQL uses version 2.11.0. **Note:** If you're [using Private Service Connect to connect to a Cloud SQL instance](https://docs.cloud.google.com/sql/docs/postgres/configure-private-service-connect), then you need to [enable PSC outbound connectivity](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect#psc-outbound) to use this extension.  
[postgres_fdw](https://www.postgresql.org/docs/11/postgres-fdw.html) | Allows foreign data wrappers to be created within instances or across instances. Also see postgres_fdw in this document.  
PostgreSQL 9.6, 10, 11, 12, and 13 use version 1.0. PostgreSQL 14 and later use version 1.1.  
**Note:** If you're [using Private Service Connect to connect to a Cloud SQL instance](https://docs.cloud.google.com/sql/docs/postgres/configure-private-service-connect), then you need to [enable PSC outbound connectivity](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect#psc-outbound) to use this extension.   
[ postgresql_anonymizer](https://postgresql-anonymizer.readthedocs.io/en/stable/) | Masks or replaces personally identifiable information (PII) or sensitive data from a PostgreSQL database. For more information, see the postgresql_anonymizer section. Cloud SQL for PostgreSQL uses version 1.0.0.  
[ postgresql_hll](https://github.com/citusdata/postgresql-hll) | Provides a HyperLogLog (`hll`) data structure that estimates the cardinality of a set. Cloud SQL for PostgreSQL uses version 2.18.  
[rdkit](https://github.com/rdkit/rdkit) | A collection of cheminformatics and machine-learning software. You can use this extension for comparing, manipulating, and identifying molecular structures.   
Cloud SQL for PostgreSQL uses version 4.6.1. **Note** : RDKit extension can't be upgraded to version 4.6.1 from older versions on PostgreSQL 9.6, 10, 11, 12 and 13. It must be dropped and re-created for the upgrade.   
[refint](https://www.postgresql.org/docs/current/static/contrib-spi.html) | Includes functions to check foreign key restraints, the referencing table, and the referenced table. This extension also demonstrates the [ Server Programming Interface (SPI)](https://www.postgresql.org/docs/current/static/spi.html). Cloud SQL for PostgreSQL uses version 1.0.   
[sslinfo](https://www.postgresql.org/docs/current/static/sslinfo.html) | Provides information about the SSL certificate that the current client provided when it connected to the instance.   
Cloud SQL for PostgreSQL uses version 1.2.   
[tablefunc](https://www.postgresql.org/docs/current/static/tablefunc.html) | Includes various functions that return tables (multiple rows).  
Cloud SQL for PostgreSQL uses version 1.0.   
[ tcn](https://www.postgresql.org/docs/current/static/tcn.html) | Provides a trigger function that notifies listeners of changes to the content of database tables.  
Cloud SQL for PostgreSQL uses version 1.0.   
[tds_fdw](https://github.com/tds-fdw/tds_fdw/) | Provides a foreign data wrapper (fdw) for accessing databases, such as Microsoft SQL Server and Sybase, that use the Tabular Data Stream (TDS) protocol. Cloud SQL for PostgreSQL uses version 2.0.4. The Postgres client can connect to a SQL server source using SSL encryption. However, server certificate validation is not enforced.   
[temporal_tables](https://pgxn.org/dist/temporal_tables/) | Provides support for temporal tables. A temporal table records the period of time when a row is valid from a database perspective.  
Cloud SQL for PostgreSQL uses version 1.2.2.   
[tsm_system_rows](https://www.postgresql.org/docs/current/static/tsm-system-rows.html) | Provides the table sampling method SYSTEM_ROWS, which can be used in the TABLESAMPLE clause of a SELECT command.  
Cloud SQL for PostgreSQL uses version 1.0.   
[tsm_system_time](https://www.postgresql.org/docs/current/static/tsm-system-time.html) | Provides the table sampling method SYSTEM_TIME, which can be used in the TABLESAMPLE clause of a SELECT command.   
Cloud SQL for PostgreSQL uses version 1.0.   
[unaccent](https://www.postgresql.org/docs/current/static/unaccent.html) | A text search dictionary that removes accents (diacritic signs) from lexemes.   
Cloud SQL for PostgreSQL uses version 1.1.   
[uuid-ossp](https://www.postgresql.org/docs/current/static/uuid-ossp.html) | Provides functions to generate universally unique identifiers (UUIDs) using one of several standard algorithms.   
Cloud SQL for PostgreSQL uses version 1.1.   
  
## More about some PostgreSQL extensions

This section describes more information about some of the supported PostgreSQL extensions in the tables above.

### auto_explain

To begin using this extension on an instance, set the `cloudsql.enable_auto_explain` flag to `on`. For information about setting flags, and to review the flags supported for this extension, see [Configure database flags](https://docs.cloud.google.com/sql/docs/postgres/flags).

To view logging data and events that are associated with the logs of the execution plans that this extension enables, see the [Cloud Logging](https://docs.cloud.google.com/logging/docs) documentation.

Alternatively, for a user that has the `cloudsqlsuperuser` role (only), you can use the `load` command to load this extension for one session.

### dblink

From within a database session, you can use this extension to connect to PostgreSQL databases and execute queries.

Currently, this extension works for two Cloud SQL private IP instances within the same VPC network, or for cross databases within the same instance.

**Note:** In Cloud SQL, the use of client certificates with dblink isn't supported.

For additional information, see [dblink](https://www.postgresql.org/docs/current/dblink.html) in the PostgreSQL documentation.

#### Use dblink to connect with a password

To connect to databases, or to connect to the same instance as another user, you must specify a password. For example purposes (but not for production purposes), here is a code snippet:
    
    
      SELECT * FROM dblink (
        'dbname=name port=1234 host=host user=user password=password',
        'select id, name from table' \
      ) AS t(id int, name text);
    

Alternatively, to only set up a connection, here is a code snippet for example purposes (not for production purposes):
    
    
      SELECT dblink_connect('dbname=dblinktest user=postgres host=name_or_ip password=xxx');
    

#### Use dblink to connect without a password

To connect to the same instance as the same user, you can connect without a password. For example:

  1. Set the following database flag to enable local connections without a password  
`cloudsql.allow_passwordless_local_connections`

  2. Connect without specifying a host, which implies connecting to the same instance. Here is an example:
         
         SELECT *
           FROM dblink('dbname=finance user=alice',
                       'select income from revenue')
             AS revenue(income integer);
         

The result could be similar to the following:
         
         income
               --------
               1000
               (1 row)
         




To connect to databases within the same instance, you cannot set host to localhost or to `127.0.0.1`. Instead, you must use the IP address shown for your instance in the Google Cloud console.

Also see postgres_fdw and PL/Proxy in this document.

### pageinspect

This extension inspects the contents of database pages at a low level. For more information, see [pageinspect](https://www.postgresql.org/docs/11/pageinspect.html) in the PostgreSQL documentation.

### pg_bigm

This extension enables full-text search, and allows a two-gram (bigram) index for faster full-text search.

To begin using this extension on an instance, set the `cloudsql.enable_pg_bigm` flag to `on`. The following flags also are supported:

  * `pg_bigm.enable_recheck`
  * `pg_bigm.gin_key_limit`
  * `pg_bigm.similarity_limit`



For information about setting flags, and to review the flags supported for this extension, see [Configure database flags](https://docs.cloud.google.com/sql/docs/postgres/flags).

### pg_cron

To begin using [pg_cron](https://github.com/citusdata/pg_cron) on an instance, set the `cloudsql.enable_pg_cron` flag to `on`. For information about setting flags, and to review the flags supported for this extension, see [Configure database flags](https://docs.cloud.google.com/sql/docs/postgres/flags).

The jobs are configured as background workers, so you might need to use standard PostgreSQL techniques (such as the `max_worker_processes` flag) to adjust the number of those background workers.

For this extension, Cloud SQL supports the background worker mode, but not the libpq interface. Therefore, trust authentication directly involving this extension is not required.

### pgfincore

This extension contains functions for managing pages in operating system disk cache memory from PostgreSQL. For more information, see the [pgfincore documentation](https://github.com/klando/pgfincore).

### pg_freespacemap

This extension examines the free space map (FSM). For more information, see [pg_freespacemap](https://www.postgresql.org/docs/11/pgfreespacemap.html) in the PostgreSQL documentation.

### pg_hint_plan

To begin using this extension on an instance, set the `cloudsql.enable_pg_hint_plan` flag to `on`. For information about setting flags, and to review the flags supported for this extension, see [Configure database flags](https://docs.cloud.google.com/sql/docs/postgres/flags).

Alternatively, for only a user with the `cloudsqlsuperuser` role, you can use the `load` command to load this extension for one session.

### pg_partman

This extension helps you create and manage time-based and serial-based table partition sets.

In Cloud SQL, this extension doesn't include the background worker (`pg_partman_bgw`) for automatic partition maintenance. Instead, you can use `pg_cron`, or [Cloud Scheduler](https://docs.cloud.google.com/scheduler/docs) with [Cloud Run functions](https://docs.cloud.google.com/functions/docs), to drive maintenance by calling [`pg_partman` maintenance functions or procedures](https://github.com/pgpartman/pg_partman/blob/master/doc/pg_partman.md#maintenance-objects) at a regular interval.

For example, to schedule partition maintenance using `pg_cron`:

  1. Enable `pg_cron` on your instance by setting the `cloudsql.enable_pg_cron` flag to `on`. By default, `pg_cron` runs in the `postgres` database; to use a different database, set the `cron.database_name` flag to that database's name. For more information, see [Configure database flags](https://docs.cloud.google.com/sql/docs/postgres/flags).
  2. Connect to the database and create the `pg_partman` and `pg_cron` extensions:
         
         CREATE SCHEMA IF NOT EXISTS partman;
         CREATE EXTENSION pg_partman SCHEMA partman;
         CREATE EXTENSION pg_cron;
         

  3. After you configure your partitioned tables with `pg_partman`, schedule a `pg_cron` job to run partition maintenance at a regular interval (for example, every hour):
         
         SELECT cron.schedule('@hourly', $$CALL partman.run_maintenance_proc()$$);
         




### pg_proctab

Here are the steps to use the [pg_proctab](https://gitlab.com/pg_proctab/pg_proctab) extension to enable the [pg_top](https://pg_top.gitlab.io/) utility:

  1. In the psql tool, run the [CREATE EXTENSION](https://www.postgresql.org/docs/current/static/sql-createextension.html) command for pg_proctab.
  2. Download and run [pg_top](https://pg_top.gitlab.io/).
  3. When connecting to a Cloud SQL for PostgreSQL instance, add the `-r` option for connecting to a remote database, for getting metrics.



The following instance-wide metrics, which are included in the output, include usage by other supporting agents and services in the instance:

  * Load average
  * CPU states (% user, nice, system, idle, and iowait)
  * Memory (used, free, and cached)



### pg_repack

This extension enables you to remove bloat from tables and indexes. Optionally, you can use this extension to perform an online CLUSTER (order tables by cluster index). For more information, see the [pg_repack documentation](http://reorg.github.io/pg_repack/). Additionally, for use of this extension in Cloud SQL, a special procedure is needed for adding privileges to a user.

If a user outside of the `cloudsqlsuperuser` role wants to use an extension, you must grant the user `cloudsqlsuperuser` privileges. For more information, in this document, see Requirement for superuser privileges. The following example uses the `GRANT` command to add the necessary privileges.

#### Example of adding privileges

For example purposes below, `csuper1` is a `cloudsqlsuperuser` and `testdb` is a database owned by `testuser`. To create the pg_repack extension in `testdb`, initially run the following commands:

  1. Connect to `testdb` as the `cloudsqlsuperuser`:
         
         psql -U csuper1 -d testdb;
         

  2. Grant the database owner, which is `testuser,` to `csuper1`:
         
         GRANT testuser TO csuper1;
         

  3. Create the extension:
         
         CREATE EXTENSION pg_repack;
         

  4. Run the `pg_repack` command on a table, such as `t1` in `testdb`, as `csuper1`:
         
         pg_repack -h <hostname> -d testdb -U csuper1 -k -t t1
         

  5. After the pg_repack job is completed, revoke the grant that you performed in step 2:
         
         REVOKE testuser FROM csuper1;
         




The `pg_repack` command might fail with the following error:  
`"ERROR: query failed: SSL SYSCALL error: EOF detected"`

If that error occurs, try setting TCP keepalives to a smaller value and then run the `pg_repack` command. For more information, see [Connections timeout (from Compute Engine)](https://docs.cloud.google.com/sql/docs/postgres/debugging-connectivity#compute-engine).

### pg_squeeze

This extension removes unused space from a table and optionally uses an index to sort tuples of the table. To begin using the extension on an instance, set the `cloudsql.enable_pg_squeeze` flag to `on`.

This extension also supports logical decoding by writing additional information to the write-ahead log (WAL). To enable this functionality for the extension, set the `wal_level` configuration parameter to `logical` or higher by setting the `cloudsql.logical_decoding` flag to `on`.

The extension requires a value to be set for the `max_replication_slots` flag. If you haven't specified a value for this flag, then set the value to `1`. Otherwise, add 1 to the value that's set for the flag.

For information about setting flags, and to review the flags supported for this extension, see [Configure database flags](https://docs.cloud.google.com/sql/docs/postgres/flags).

### `pg_textsearch`

The [`pg_textsearch`](https://www.tigerdata.com/blog/pg-textsearch-bm25-full-text-search-postgres) extension provides full-text search using the industry-standard [BM25 (Best Matching 25)](https://en.wikipedia.org/wiki/Okapi_BM25) scoring algorithm to deliver highly accurate relevance scoring. The extension is an [open-source project](https://github.com/timescale/pg_textsearch) available on GitHub.

The `pg_textsearch` extension requires PostgreSQL 17 or later.

Because the `pg_textsearch` extension supports inverse document frequency ([td-idf](https://en.wikipedia.org/wiki/Tf%E2%80%93idf)), term frequency saturation, and document length normalization, it can produce more relevant results than PostgreSQL's built-in `ts_rank` function. Also, because it operates directly on standard PostgreSQL storage pages, you don't have to install a third party engine like Elasticsearch, or worry about dual-cluster maintenance and data synchronization. Using `pg_textsearch`, you can build robust, scalable, and highly relevant search experiences without leaving the PostgreSQL ecosystem.

For more information, see [Full-text search using `pg_textsearch`](https://docs.cloud.google.com/sql/docs/postgres/pg-textsearch).

### pgtt

To begin using this extension on an instance, set the `pgtt.enabled` flag to `on`. For information about setting flags, and to review the flags supported for this extension, see [Configuring database flags](https://docs.cloud.google.com/sql/docs/postgres/flags).

### pg_visibility

This extension provides a way to examine the visibility map (VM) and the page-level visibility information of a table. For more information, see [pg_visibility](https://www.postgresql.org/docs/11/pgvisibility.html) in the PostgreSQL documentation.

### PL/Proxy

This extension is a procedural language handler that allows remote procedure calls among PostgreSQL databases, with optional sharding.

For more information, see the [PL/Proxy documentation](https://plproxy.github.io/).

The target instances for connections must be in the same VPC network as the connecting instance. Additionally, you cannot choose, in the Google Cloud console, the **Allow only SSL connections** button for cluster instances.

To connect to databases within the same instance, you cannot set host to localhost or to `127.0.0.1`. Instead, you must use the IP address shown for your instance in the Google Cloud console.

Also see postgres_fdw and dblink in this document.

### postgresql_anonymizer

To begin using this extension on an instance, set the `cloudsql.enable_anon` flag to `on`. For information about setting flags, and to review the flags supported for this extension, see [Configuring database flags](https://docs.cloud.google.com/sql/docs/postgres/flags).

### postgres_fdw

This extension allows tables from other ("foreign") PostgreSQL databases to be exposed as "foreign" tables in the current database. Those tables then are available for use, almost as if they were local tables. For more information, see [postgres_fdw](https://www.postgresql.org/docs/11/postgres-fdw.html) in the PostgreSQL documentation.

This extension works for two Cloud SQL private IP instances within the same VPC network, or for cross databases within the same instance.

To connect to databases within the same instance, you cannot set host to localhost or to `127.0.0.1`. Instead, you must use the IP address shown for your instance in the Google Cloud console.

Additionally, for an instance where foreign data is stored, you can choose the **Allow only SSL connections** option in the Google Cloud console. You can't choose the **Require trusted client certificates** option. Only the `cloudsqlsuperuser` can be the owner of a `postgres_fdw` foreign data wrapper.

Also see PL/Proxy and dblink in this document.

### postgresql-hll

This extension introduces a new data type, `hll`, which is a HyperLogLog data structure. For more information, see the [postgresql-hll documentation](https://github.com/citusdata/postgresql-hll).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
