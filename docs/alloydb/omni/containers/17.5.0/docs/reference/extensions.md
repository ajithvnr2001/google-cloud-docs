---
url: https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/reference/extensions/
title: Supported database extensions \u00a0|\u00a0 AlloyDB Omni for containers: 17.5.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:48:02.236171+00:00
---

# Supported database extensions  |  AlloyDB Omni for containers: 17.5.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/reference/extensions/

This page documents AlloyDB Omni version **17.5.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/overview)
  * [ Reference ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/reference/database-flags)



Send feedback 

#  Supported database extensions Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 17.5.0keyboard_arrow_down

  * [ Current (18.3.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/reference/extensions)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/reference/extensions)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/reference/extensions)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/reference/extensions)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/reference/extensions)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/reference/extensions)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/reference/extensions)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/reference/extensions)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/reference/extensions)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/reference/extensions)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/reference/extensions)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/reference/extensions)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/reference/extensions)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/reference/extensions)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/reference/extensions)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/reference/extensions)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/reference/extensions)

The following table lists all of the extensions supported by AlloyDB Omni 16.8.0. 

All of these extensions are available on every AlloyDB Omni instance. To enable any of them, see Enable an extension.

**Note:** Some extensions require additional steps before you can enable them—typically, by [setting one or more database flags](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/configure-database-flags) on your instances.Extension | Description  
---|---  
`[alloydb_ai_nl](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/reference/alloydb-flags#alloydb_ai_nl)` |  Provides functions to securely query data using natural language from your application.   
`[alloydb_password_validation](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/reference/extensions/)` |  Provides functions to [set and manage password policies](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/manage-password-policy) for AlloyDB Omni.   
`[alloydb_scann](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/reference/alloydb-flags#alloydb_scann)` |  Provides features for [improving vector query performance](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/reference/extensions/) with the ScaNN index.   
`[amcheck](https://www.postgresql.org/docs/16/amcheck.html)` | Provides functions for verifying the logical consistency of the structure of relations, enabling the `pg_amcheck` application to check for corruption.  
`[anon](https://postgresql-anonymizer.readthedocs.io/en/stable/)` | Helps you hide or replace personally identifiable information (PII) or commercially sensitive data. **Important:** Before you can use the `CREATE EXTENSION` command to enable this extension, you must add the `anon` extension into [the `shared_preload_libraries` parameter](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/reference/extensions#preload-shared-libraries), and you must ensure that the `anon` extension is loaded by restarting the database. In addition, install the `pgcrypto` extension before installing the `anon` extension.   
`[auto_explain](https://www.postgresql.org/docs/16/auto-explain.html)` | Enables automatic logging of execution plans of slow statements, for troubleshooting and more. It provides an automated way to perform the functionality of the `EXPLAIN` command. **Important:** Before you can use the `LOAD` command to enable this extension, you must first add the `auto_explain` extension into [the `shared_preload_libraries` parameter](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/reference/extensions#preload-shared-libraries), and you must ensure that the `auto_explain` extension is loaded by restarting the database.   
`[autoinc](https://www.postgresql.org/docs/16/contrib-spi.html#CONTRIB-SPI-AUTOINC)` | Provides functions for incrementing fields automatically. This trigger stores the next value of a sequence into an integer field.   
`[bloom](https://www.postgresql.org/docs/16/bloom.html)` | Provides an index access method based on Bloom filters.  
`[btree_gin](https://www.postgresql.org/docs/16/btree-gin.html)` | Provides sample GIN operator classes that implement B-tree equivalent behavior.   
`[btree_gist](https://www.postgresql.org/docs/16/btree-gist.html)` | Provides GiST index operator classes that implement B-tree equivalent behavior.   
`[citext](https://www.postgresql.org/docs/16/citext.html)` | Provides a case-insensitive character string type `citext`.  
`[credcheck](https://github.com/HexaCluster/credcheck)` | The `credcheck` PostgreSQL extension provides credential checks, which are evaluated when you create a user, change a password, or rename a user. **Important:** To use the `Password Reuse Policy` and `Authentication Failure Ban` features, you must add the `credcheck` extension to the [`shared_preload_libraries`](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/reference/extensions#preload-shared-libraries) parameter, and then restart the database to make sure that the `credcheck` extension is loaded.   
`[cube](https://www.postgresql.org/docs/16/cube.html)` | Implements a data type `cube` for representing multidimensional cubes.   
`[dblink](https://www.postgresql.org/docs/16/dblink.html)` | Provides functions to connect to PostgreSQL databases from within a database session.   
`[dict_int](https://www.postgresql.org/docs/16/dict-int.html)` | An add-on dictionary template for full-text search that controls the indexing of integers.   
`[dict_xsyn](https://www.postgresql.org/docs/16/dict-xsyn.html)` | An add-on dictionary template that controls string indexing for full-text search.   
`[earthdistance](https://www.postgresql.org/docs/16/earthdistance.html)` | Provides two approaches to calculating great circle distances on the surface of the Earth.   
`[fuzzystrmatch](https://www.postgresql.org/docs/16/fuzzystrmatch.html)` | Provides several functions to determine similarities and distance between strings.   
`[google_columnar_engine](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/columnar-engine/about)` | Provides the columnar engine feature of AlloyDB Omni, which handles HTAP (hybrid transactional analytical processing) and OLAP (online analytical processing) workloads very efficiently. **Important:** Before you can use `CREATE EXTENSION` to enable this extension, you must first [set the database flag](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/reference/database-flags) `google_columnar_engine.enabled` to the value `on` in the AlloyDB Omni instance where you want to use the extension.   
`[google_db_advisor](https://docs.cloud.google.com/alloydb/docs/use-index-advisor)` | Provides the index advisor feature of AlloyDB Omni, which recommends indexes to speed up query processing.   
`[google_ml_integration](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/vertex-ai/invoke-predictions)` | Provides functions you use to access Vertex AI prediction endpoints to get predictions in SQL.   
`[hstore](https://www.postgresql.org/docs/16/hstore.html)` | Implements the `hstore` data type for storing sets of key/value pairs within a single PostgreSQL value.   
`[hypopg](https://hypopg.readthedocs.io/)` | Provides support for hypothetical indexes.  
`[insert_username](https://www.postgresql.org/docs/16/contrib-spi.html#CONTRIB-SPI-INSERT-USERNAME)` | Provides functions for storing the current user's name into a text field. You can use this function to track which user last modified a row in a database table.  
`[intagg](https://www.postgresql.org/docs/16/intagg.html)` | Provides an integer aggregator and an enumerator.  
`[intarray](https://www.postgresql.org/docs/16/intarray.html)` | Provides a set of functions and operators for manipulating null-free arrays of integers and performing indexed searches on them.   
`[ip4r](https://github.com/RhodiumToad/ip4r)` | Provides data types for IPv4/v6 addresses, and address ranges, plus index support.   
`[isn](https://www.postgresql.org/docs/16/isn.html)` | Provides data types for some international product numbering standards.  
`[lo](https://www.postgresql.org/docs/16/lo.html)` | Support for managing Large Objects (also called LOs or BLOBs).  
`[ltree](https://www.postgresql.org/docs/16/ltree.html)` | Implements a data type `ltree` for representing labels of data stored in a hierarchical tree-like structure.   
`[moddatetime](https://www.postgresql.org/docs/16/contrib-spi.html#CONTRIB-SPI-MODDATETIME)` | Provides functions for storing the current time into a `timestamp` field. You can use this function to track the last time that a row in a database table was modified.   
`[pageinspect](https://www.postgresql.org/docs/16/pageinspect.html)` | Inspects the contents of database pages at a low level.  
`[pg_bigm](https://github.com/pgbigm/pg_bigm/blob/REL1_2_STABLE/docs/pg_bigm_en.md)` | Provides full text search capability in PostgreSQL using 2-gram (bigram) indexes for faster full text searches. **Important:** Before you can use the `CREATE EXTENSION` command to enable this extension, you must first add the `pg_bigm` extension into [the `shared_preload_libraries` parameter>](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/reference/extensions#preload-shared-libraries), and you must ensure that the `pg_bigm` extension is loaded by restarting the database.   
`[parameterized_views](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/reference/alloydb-flags#parameterized_views)` | Provides functions that add a security layer when natural language queries are translated to SQL queries. This extension works together with the `alloydb_ai_nl` extension.   
`[pg_buffercache](https://www.postgresql.org/docs/16/pgbuffercache.html)` | Provides a means for examining what's happening in the shared buffer cache in real time.   
`[pg_cron](https://github.com/citusdata/pg_cron/#readme)` | Provides a cron-based job scheduler for PostgreSQL that runs inside the database as an extension. It uses the same syntax as regular `cron`, but it lets you schedule PostgreSQL commands directly from the database. **Important:** Before you can use the `CREATE EXTENSION` command to enable this extension, you must first add the `pg_cron` extension into [the `shared_preload_libraries` parameter](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/reference/extensions#preload-shared-libraries), and you must ensure that the `pg_cron` extension is loaded by restarting the database.   
`[pg_freespacemap](https://www.postgresql.org/docs/16/pgfreespacemap.html)` | Examines the free space map (FSM).  
`[pg_hint_plan](https://github.com/ossc-db/pg_hint_plan#readme)` | Helps you improve PostgreSQL execution plans using hints, which are descriptions in SQL comments. **Important:** Before you can use the `CREATE EXTENSION` command to enable this extension, you must first add the `pg_hint_plan` extension into [the `shared_preload_libraries` parameter>](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/reference/extensions#preload-shared-libraries), and you must ensure that the `pg_hint_plan` extension is loaded by restarting the database.   
`[pg_ivm](https://github.com/sraoss/pg_ivm?tab=readme-ov-file#pg_ivm)` | Provides Incremental View Maintenance (IVM) feature for PostgreSQL.   
`[pg_partman](https://github.com/pgpartman/pg_partman/)` | Lets you create and manage time-based and serial-based table partition sets.   
`[pg_prewarm](https://www.postgresql.org/docs/16/pgprewarm.html)` | Provides a convenient way to load relation data into either the operating system buffer cache or the PostgreSQL buffer cache.   
`[pg_proctab](https://gitlab.com/pg_proctab/pg_proctab)` | Lets you use [pg_top](https://pg_top.gitlab.io/) with AlloyDB Omni, and generate reports from the operating system process table.   
`[pg_repack](http://reorg.github.io/pg_repack/)` | Lets you remove bloat from tables and indexes. Optionally, lets you perform an online CLUSTER (order tables by cluster index).   
`[pg_similarity](https://github.com/eulerto/pg_similarity)` | Provides support for similarity queries on PostgreSQL.  
`[pg_squeeze](https://github.com/cybertec-postgresql/pg_squeeze)` | Removes unused space from a table and optionally uses an index to sort records or rows (tuples) of the table. **Important:** Before you can use `CREATE EXTENSION` to enable this extension, you must first add `pg_squeeze` into [`shared_preload_libraries`](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/reference/extensions#preload-shared-libraries), and you must ensure that it's loaded by restarting the database.   
`[g_stats](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/reference/extensions/)` |  Enables one to [optimize database performance](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/optimize-database-performance-compare-snapshots) by comparing performance snapshots.   
`[pg_stat_statements](https://www.postgresql.org/docs/16/pgstatstatements.html)` | Provides a means for tracking execution statistics of all SQL statements executed.   
`[pg_surgery](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/reference/extensions/)` | Provides functions to perform low-level surgery on relation data. Use this low-level tool with extreme care and as a last resort only.   
`[pg_trgm](https://www.postgresql.org/docs/16/pgtrgm.html)` | Provides functions and operators for determining the similarity of alphanumeric text based on trigram matching, as well as index operator classes that support fast searching for similar strings.   
`[pg_visibility](https://www.postgresql.org/docs/16/pgvisibility.html)` | Provides a way to examine the visibility map (VM) and the page-level visibility information of a table.   
`[pg_wait_sampling](https://github.com/postgrespro/pg_wait_sampling)` | Provides the ability to collect sampling statistics of wait events. **Important:** Before you can use `CREATE EXTENSION` to enable this extension, you must first add the `pg_wait_sampling` extension into [the `shared_preload_libraries` parameter](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/reference/extensions#preload-shared-libraries), and you must ensure that the `pg_wait_sampling` extension is loaded by restarting the database. You must also [set the database flag](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/reference/database-flags) `alloydb.enable_pgaudit` to the value `on` in the AlloyDB Omni instance where you want to use the extension.   
`[pgaudit](https://github.com/pgaudit/pgaudit)` | Provides detailed session and object audit logging using the standard logging facility provided by PostgreSQL. **Important:** Before you can use `CREATE EXTENSION` to enable this extension, you must first add `pgaudit` into [`shared_preload_libraries`](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/reference/extensions#preload-shared-libraries), and you must ensure that it's loaded by restarting the database.   
`[pgcrypto](https://www.postgresql.org/docs/16/pgcrypto.html)` | Provides cryptographic functions for PostgreSQL.  
`[pgfincore](https://github.com/klando/pgfincore)` | A set of functions to manage pages in operating system disk cache memory from PostgreSQL.   
`[pglogical](https://github.com/2ndQuadrant/pglogical)` | Provides logical streaming replication for PostgreSQL using a publish/subscribe model. AlloyDB Omni includes a number of plugins used by the `pglogical` extension. **Important:** Before you can use `CREATE EXTENSION` to enable this extension, you must first add `pglogical` into [`shared_preload_libraries`](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/reference/extensions#preload-shared-libraries), and you must ensure that it's loaded by restarting the database. You must also [set the database flags](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/reference/database-flags) `alloydb.logical_decoding` to the value `on` in the AlloyDB Omni instance where you want to use the extension.  
`[pgrowlocks](https://www.postgresql.org/docs/16/pgrowlocks.html)` | Provides row locking information for the specified table.  
`[pgstattuple](https://www.postgresql.org/docs/16/pgstattuple.html)` | Provides various functions to obtain tuple-level statistics.  
`[pgtap](https://pgtap.org/)` | Provides a unit testing framework for PostgreSQL, written in PL/pgSQL and PL/SQL.   
`[pgtt](https://github.com/darold/pgtt#readme)` | Adds support for global temporary tables to your databases.   
`[vector](https://github.com/pgvector/pgvector#readme)` | The stock `pgvector` PostgreSQL extension extension is customized for AlloyDB Omni, and referred to as `vector`. It supports store generated embeddings in a vector column, generate vector-optimized indexes, and search vector embeddings.   
`[plpgsql](https://www.postgresql.org/docs/16/plpgsql.html)` | A loadable procedural language for creating functions, procedures and triggers. You also can use this language for direct execution of code in `DO` blocks.   
`[plproxy](https://plproxy.github.io/)` | Procedural language handler that allows remote procedure calls among PostgreSQL databases, with optional sharding.  
`[plv8](https://plv8.github.io/)` | Provides a procedural language for enabling JavaScript.  
`[postgres_fdw](https://www.postgresql.org/docs/16/postgres-fdw.html)` | Provides a foreign-data wrapper that you can use to access data stored in external PostgreSQL servers.   
`[postgresql-hll](https://github.com/citusdata/postgresql-hll)` | Introduces a new data type, `hll`, which is a HyperLogLog data structure.   
`[prefix](https://github.com/dimitri/prefix)` | Provides prefix-matching, plus index support.  
`[refint](https://www.postgresql.org/docs/16/static/contrib-spi.html)` | Includes functions to check foreign key restraints, the referencing table, and the referenced table.  
`[sslinfo](https://www.postgresql.org/docs/16/sslinfo.html)` | Provides information about the SSL certificate that the current client provided when it connected to the instance.   
`[tablefunc](https://www.postgresql.org/docs/16/tablefunc.html)` | Provides various functions that return tables (multiple rows).  
`[tcn](https://www.postgresql.org/docs/16/tcn.html)` | Provides a trigger function that notifies listeners of changes to the content of database tables.  
`[temporal_tables](https://pgxn.org/dist/temporal_tables/)` | Provides support for temporal tables. In databases, a temporal table records the period of time for which a row is valid.  
`[tsm_system_rows](https://www.postgresql.org/docs/16/tsm-system-rows.html)` | Provides the table sampling method SYSTEM_ROWS, which can be used in the TABLESAMPLE clause of a SELECT command.   
`[tsm_system_time](https://www.postgresql.org/docs/16/tsm-system-time.html)` | Provides the table sampling method SYSTEM_TIME, which can be used in the TABLESAMPLE clause of a SELECT command.   
`[unaccent](https://www.postgresql.org/docs/16/unaccent.html)` | A text search dictionary that removes accents and other diacritical signs from lexemes.  
`[uuid-ossp](https://www.postgresql.org/docs/16/uuid-ossp.html)` | Provides functions to generate universally unique identifiers (UUIDs) using one of several standard algorithms.   
  
## Logical decoding plugins

In addition to the extensions listed earlier on this page, AlloyDB Omni supports the following plugins used by the `pglogical` extension for formatting that extension's streamed output.

Plugin | Description  
---|---  
`pgoutput` | PostgreSQL's built-in logical decoding plugin.  
`test_decoding` | Formats streamed data into a text format.  
  
## PostGIS extensions

The following [PostGIS extensions](https://www.postgis.net/) are supported, but are not included in AlloyDB Omni:

  * [`postgis`](http://www.postgis.net/)
  * [`postgis_raster`](https://postgis.net/docs/RT_reference.html)
  * [`postgis_sfcgal`](http://www.sfcgal.org/)
  * [`postgis_tiger_geocoder`](http://postgis.net/docs/Geocode.html)
  * [`postgis_topology`](http://postgis.net/docs/manual-dev/Topology.html)
  * [`address_standardizer`](https://postgis.net/docs/manual-dev/Extras.html)
  * [`address_standardizer_data_us`](https://postgis.net/docs/manual-dev/Extras.html)



For more information, see [Install PostGIS for AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/install-postgis).

## Orafce extensions

AlloyDB Omni does not include the [Orafce extension](https://github.com/orafce/orafce), but you can manually add it to an existing AlloyDB Omni installation by following the instructions in [Install Orafce for AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/install-orafce) to provide additional functions and operators from the Oracle database.

## Enable an extension

To enable an extension, follow these steps: 

  1. [Connect to a database](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/run-connect) in AlloyDB Omni cluster's primary instance.

  2. Run the [`CREATE EXTENSION`](https://www.postgresql.org/docs/16/sql-createextension.html) command. For example, after connecting to your primary instance, you can enable the `citext` extension using `psql`:
         
         CREATE EXTENSION IF NOT EXISTS citext;
         




## Add extension's shared library to PostgreSQL

To add an extension's shared library to PostgreSQL, you must update the `shared_preload_libraries` database flag in your `DBCluster` manifest.

For detailed instructions on how to do this, see [Update a parameter in AlloyDB Omni on a Kubernetes cluster](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/configure-database-flags#update-parameter-kubernetes-cluster).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
