---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/db-configure-extensions/
title: Configure database extensions \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:18.329195+00:00
---

# Configure database extensions  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/db-configure-extensions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Configure database extensions Stay organized with collections  Save and categorize content based on your preferences. 

This section contains information about configuring the database extensions that Database Service supports.

## Install an extension

Extensions can only be installed on the primary DBCluster. Once installed, the extension is replicated to standby instances.

Most of the extensions can be installed directly by [connecting to the database cluster](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/db-connect-cluster) and running the [CREATE EXTENSION](https://www.postgresql.org/docs/current/sql-createextension.html) command.

However, there are a few extensions that require additional configuration, hence users must [set database flag](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/db-update-attributes#configure-database-flags), `"dbs.enable_<extension-name>": "on"` then connect to the database cluster and run the `CREATE EXTENSION` command.

Only database users who are members of the `alloydbsuperuser` role can run the `CREATE EXTENSION` command. By default, this includes the `dbsadmin` user.

**Note:** Not all the extensions listed with [pg_available_extensions](https://www.postgresql.org/docs/current/view-pg-available-extensions.html) are enabled for users. Refer to supported database extensions to get the list of supported extensions.

## Drop an extension

In order to drop an extension, the database user attempting to do so must be the owner of the extension. This implies that only the database user who initially created the extension has the authority to drop it. No other database user possesses the ability to drop the extension, ensuring controlled management of extensions.

## Supported database extensions

The following table lists all of the supported extensions.

Extension | Description  
---|---  
[alloydb_ai_nl](https://docs.cloud.google.com/alloydb/docs/ai/use-psvs) | Google Extension for AlloyDB AI & Natural Language  
[amcheck](https://www.postgresql.org/docs/15/amcheck.html) | Provides functions for verifying the logical consistency of the structure of relations, enabling the pg_amcheck application to check for corruption.  
[anon](https://postgresql-anonymizer.readthedocs.io/en/stable/) | Masks or replaces personally identifiable information (PII) or sensitive data from a PostgreSQL database. **Important:** To enable this extension, you must first set the database flag `dbs.enable_anon` to the value `on` in the DBCluster where you want to use the extension.   
`kubectl --kubeconfig MANAGEMENT_API_SERVER patch dbclusters.DB_ENGINE DBCLUSTER_NAME -n NAMESPACE --type=merge -p '{"spec":{"primarySpec":{"parameters":{"dbs.enable_anon": "on"}}}}'`  
[autonic](https://www.postgresql.org/docs/16/contrib-spi.html#CONTRIB-SPI-AUTOINC) | Provides functions for auto incrementing fields  
[bloom](https://www.postgresql.org/docs/15/bloom.html) | Provides a method to access indexes based on bloom filters. A bloom filter is a space-efficient data structure that you can use to test whether an element is a member of a set.  
[btree_gin](https://www.postgresql.org/docs/15/btree-gin.html) | Provides sample GIN operator classes that implement B-tree equivalent behavior.  
[btree_gist](https://www.postgresql.org/docs/15/btree-gist.html) | Provides GiST index operator classes that implement B-tree equivalent behavior.  
[citext](https://www.postgresql.org/docs/15/citext.html) | Provides a case-insensitive character string type citext.  
[cube](https://www.postgresql.org/docs/15/cube.html) | Implements a data type cube for representing multidimensional cubes.  
[dblink](https://www.postgresql.org/docs/15/dblink.html) | Provides functions to connect to PostgreSQL databases from within a database session  
[dict_int](https://www.postgresql.org/docs/15/dict-int.html) | An add-on dictionary template for full-text search that controls the indexing of integers.  
[dict_xsyn](https://www.postgresql.org/docs/current/dict-xsyn.html) | Text search dictionary template for extended synonym processing  
[earthdistance](https://www.postgresql.org/docs/15/earthdistance.html) | Provides two approaches to calculating great circle distances on the surface of the Earth.  
[fuzzystrmatch](https://www.postgresql.org/docs/15/fuzzystrmatch.html) | Provides several functions to determine similarities and distance between strings.  
[google_columnar_engine](https://docs.cloud.google.com/alloydb/docs/columnar-engine/about) | Provides the columnar engine feature of AlloyDB, which handles HTAP (hybrid transactional analytical processing) and OLAP (online analytical processing) workloads very efficiently.  
[google_db_advisor](https://docs.cloud.google.com/alloydb/docs/use-index-advisor) | Provides the index advisor feature of AlloyDB, which recommends indexes to speed up query processing.  
[google_ml_integration](https://docs.cloud.google.com/alloydb/docs/ai/invoke-predictions) | Provides functions you use to access Vertex AI endpoints to get predictions in SQL.  
[postgresql-hll](https://github.com/citusdata/postgresql-hll) | Provides a HyperLogLog (hll) data structure that estimates the cardinality of a set.  
[hstore](https://www.postgresql.org/docs/15/hstore.html) | Implements the hstore data type for storing sets of key/value pairs within a single PostgreSQL value.  
[hypopg](https://hypopg.readthedocs.io/en/rel1_stable/) | Provides support for hypothetical indexes.  
[insert_username](https://www.postgresql.org/docs/16/contrib-spi.html#CONTRIB-SPI-INSERT-USERNAME) | Provides functions for storing the current user's name into a text field. You can use this function to track which user last modified a row in a database table.  
[intagg](https://www.postgresql.org/docs/15/intagg.html) | Provides an integer aggregator and an enumerator.  
[intarray](https://www.postgresql.org/docs/15/intarray.html) | Provides a set of functions and operators for manipulating null-free arrays of integers and performing indexed searches on them.  
[ip4r](https://github.com/RhodiumToad/ip4r) | Provides data types for IPv4/v6 addresses, and address ranges, plus index support.  
[isn](https://www.postgresql.org/docs/15/isn.html) | Provides data types for some international product numbering standards.  
[lo](https://www.postgresql.org/docs/15/lo.html) | Support for managing Large Objects (also called LOs or BLOBs).  
[ltree](https://www.postgresql.org/docs/current/ltree.html) | Implements a data type ltree for representing labels of data stored in a hierarchical tree-like structure.  
[moddatetime](https://www.postgresql.org/docs/current/contrib-spi.html#CONTRIB-SPI-MODDATETIME) | Provides functions for storing the current time into a `timestamp` field. You can use this to track the last time that a row in a database table is modified.  
[pageinspect](https://www.postgresql.org/docs/11/pageinspect.html) | Inspects the contents of database pages at a low level.  
[pg_bigm](https://pgbigm.osdn.jp/index_en.html) | Enables full-text search, and allows a two-gram (bigram) index for faster full-text search. **Important:** To enable this extension, you must first set the database flag `dbs.enable_pg_bigm` to the value `on` in the DBCluster where you want to use the extension.   
`kubectl --kubeconfig MANAGEMENT_API_SERVER patch dbclusters.DB_ENGINE DBCLUSTER_NAME -n NAMESPACE --type=merge -p '{"spec":{"primarySpec":{"parameters":{"dbs.enable_pg_bigm": "on"}}}}'`  
[pg_buffercache](https://www.postgresql.org/docs/current/pgbuffercache.html) | Provides a means for examining what's happening in the shared buffer cache in real time.  
[pg_cron](https://github.com/citusdata/pg_cron) | Provides a cron-based job scheduler. This extension enables cron syntax to schedule PostgreSQL commands directly from the database. **Important:** To enable this extension, you must first set the database flag `dbs.enable_pg_cron` to the value `on` in the DBCluster where you want to use the extension.   
`kubectl --kubeconfig MANAGEMENT_API_SERVER patch dbclusters.DB_ENGINE DBCLUSTER_NAME -n NAMESPACE --type=merge -p '{"spec":{"primarySpec":{"parameters":{"dbs.enable_pg_cron": "on"}}}}'`  
[pg_freespacemap](https://www.postgresql.org/docs/11/pgfreespacemap.html) | Examines the free space map (FSM).  
[pg_hint_plan](https://pghintplan.osdn.jp/pg_hint_plan.html) | Lets you to improve PostgreSQL execution plans using hints, which are descriptions in SQL comments. **Important:** To enable this extension, you must first set the database flag `dbs.enable_pg_hint_plan` to the value `on` in the DBCluster where you want to use the extension.   
`kubectl --kubeconfig MANAGEMENT_API_SERVER patch dbclusters.DB_ENGINE DBCLUSTER_NAME -n NAMESPACE --type=merge -p '{"spec":{"primarySpec":{"parameters":{"dbs.enable_pg_hint_plan": "on"}}}}'`  
[pg_partman](https://github.com/pgpartman/pg_partman/) | Lets you to create and manage time-based and serial-based table partition sets.  
[pg_prewarm](https://www.postgresql.org/docs/current/pgprewarm.html) | Provides a convenient way to load relation data into either the operating system buffer cache or the PostgreSQL buffer cache.  
[pg_proctab](https://gitlab.com/pg_proctab/pg_proctab) | Lets you to use [pg_top](https://pg_top.gitlab.io/), and generate reports from the operating system process table.  
[pg_repack](https://reorg.github.io/pg_repack/) | Lets you remove bloat from tables and indexes. Optionally, lets you perform an online CLUSTER (order tables by cluster index).  
[pg_similarity](https://github.com/eulerto/pg_similarity) | Provides support for similarity queries on PostgreSQL.  
[pg_squeeze](https://github.com/cybertec-postgresql/pg_squeeze) | Removes unused space from a table and optionally uses an index to sort records or rows (tuples) of the table.  
[pg_stat_statements](https://www.postgresql.org/docs/current/pgstatstatements.html) | Provides a means for tracking execution statistics of all SQL statements executed.  
[pg_trgm](https://www.postgresql.org/docs/current/pgtrgm.html) | Provides functions and operators for determining the similarity of alphanumeric text based on trigram matching, as well as index operator classes that support fast searching for similar strings.  
[pg_visibility](https://www.postgresql.org/docs/11/pgvisibility.html) | Provides a way to examine the visibility map (VM) and the page-level visibility information of a table.  
[pg_wait_sampling](https://github.com/postgrespro/pg_wait_sampling) | Collects sampling statistics of wait events, providing wait event data for processes on servers. **Important:** To enable this extension, you must first set the database flag `dbs.enable_pg_wait_sampling` to the value `on` in the DBCluster where you want to use the extension.   
`kubectl --kubeconfig MANAGEMENT_API_SERVER patch dbclusters.DB_ENGINE DBCLUSTER_NAME -n NAMESPACE --type=merge -p '{"spec":{"primarySpec":{"parameters":{"dbs.enable_pg_wait_sampling": "on"}}}}'`  
[pgaudit](https://github.com/pgaudit/pgaudit) | Provides detailed session and object audit logging using the standard logging facility provided by PostgreSQL.  
[pgcrypto](https://www.postgresql.org/docs/current/pgcrypto.html) | Provides cryptographic functions for PostgreSQL.  
[pgfincore](https://github.com/klando/pgfincore) | A set of functions to manage pages in operating system disk cache memory from PostgreSQL.  
[pglogical](https://github.com/2ndQuadrant/pglogical) | Provides logical replication for PostgreSQL.  
[pgrowlocks](https://www.postgresql.org/docs/15/pgrowlocks.html) | Provides row locking information for the specified table.  
[pgstattuple](https://www.postgresql.org/docs/15/pgstattuple.html) | Provides various functions to obtain tuple-level statistics.  
[pgtap](https://pgtap.org/) | Provides a unit testing framework for PostgreSQL, written in PL/pgSQL and PL/SQL.  
[pgtt](https://github.com/darold/pgtt#readme) | Adds support for global temporary tables to your databases.  
[plpgsql](https://www.postgresql.org/docs/15/plpgsql.html) | A loadable procedural language for creating functions, procedures and triggers. You also can use this language for direct execution of code in DO blocks.  
[plproxy](https://plproxy.github.io/) | Procedural language handler that allows remote procedure calls among PostgreSQL databases, with optional sharding.  
[plv8](https://plv8.github.io/) | Provides a procedural language for enabling JavaScript.  
[postgres_ann](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/db-configure-extensions/) | PostgreSQL ANN Search  
[postgres_fdw](https://www.postgresql.org/docs/11/postgres-fdw.html) | Allows foreign data wrappers to be created within instances or across instances.  
[prefix](https://github.com/dimitri/prefix) | Provides prefix-matching, plus index support.  
[refint](https://www.postgresql.org/docs/current/contrib-spi.html) | Includes functions to check foreign key restraints, the referencing table, and the referenced table.  
[sslinfo](https://www.postgresql.org/docs/current/sslinfo.html) | Provides information about the SSL certificate that the current client provided when it connected to the instance.  
[tablefunc](https://www.postgresql.org/docs/current/tablefunc.html) | Includes various functions that return tables (multiple rows).  
[tcn](https://www.postgresql.org/docs/current/tcn.html) | Provides a trigger function that notifies listeners of changes to the content of database tables.  
[temporal_tables](https://pgxn.org/dist/temporal_tables/) | Provides support for temporal tables. A temporal table records the period of time when a row is valid from a database perspective.  
[tsm_system_rows](https://www.postgresql.org/docs/current/tsm-system-rows.html) | Provides the table sampling method `SYSTEM_ROWS`, which can be used in the `TABLESAMPLE` clause of a `SELECT` command.  
[tsm_system_time](https://www.postgresql.org/docs/current/tsm-system-time.html) | Provides the table sampling method `SYSTEM_TIME`, which can be used in the `TABLESAMPLE` clause of a `SELECT` command.  
[unaccent](https://www.postgresql.org/docs/current/unaccent.html) | A text search dictionary that removes accents (diacritic signs) from lexemes.  
[uuid-ossp](https://www.postgresql.org/docs/current/uuid-ossp.html) | Provides functions to generate universally unique identifiers (UUIDs) using one of several standard algorithms.  
[pgvector](https://github.com/pgvector/pgvector) | An open-source extension for storing and searching vector embeddings in PostgreSQL databases.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
