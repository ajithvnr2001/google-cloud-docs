---
url: https://docs.cloud.google.com/solutions/migrating-oracle-database-to-cloud-sql-for-postgresql/
title: Migrating Oracle\u00ae Database users and schemas to Cloud SQL for PostgreSQL \u00a0|\u00a0 Solutions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:55:31.382118+00:00
---

# Migrating Oracle® Database users and schemas to Cloud SQL for PostgreSQL  |  Solutions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/solutions/migrating-oracle-database-to-cloud-sql-for-postgresql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Solutions ](https://docs.cloud.google.com/solutions)



Send feedback 

#  Migrating Oracle® Database users and schemas to Cloud SQL for PostgreSQL Stay organized with collections  Save and categorize content based on your preferences. 

This document is part of a series that provides key information and guidance related to planning and performing Oracle® 11g/12c database migrations to [Cloud SQL for PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres) version 12. This document discusses the basic differences between Oracle® Database and Cloud SQL for PostgreSQL as they relate to creating users, schemas, tables, indexes, and views.

In addition to the [introductory setup part](https://docs.cloud.google.com/solutions/setting-up-cloud-sql-for-postgresql-for-production), the series includes the following parts:

  * [Migrating Oracle users to Cloud SQL for PostgreSQL: Terminology and functionality](https://docs.cloud.google.com/solutions/migrating-oracle-users-to-cloud-sql-for-postgresql-terminology)
  * [Migrating Oracle users to Cloud SQL for PostgreSQL: Data types, users, and tables](https://docs.cloud.google.com/solutions/migrating-oracle-users-to-cloud-sql-for-postgresql-data-types)
  * [Migrating Oracle users to Cloud SQL for PostgreSQL: Queries, stored procedures, functions, and triggers](https://docs.cloud.google.com/solutions/migrating-oracle-users-to-cloud-sql-for-postgresql-queries)
  * [Migrating Oracle users to Cloud SQL for PostgreSQL: Security, operations, monitoring, and logging](https://docs.cloud.google.com/solutions/migrating-oracle-users-to-cloud-sql-for-postgresql-security)
  * Migrating Oracle Database users and schemas to Cloud SQL for PostgreSQL (this document)



## Terminology differences between Oracle and Cloud SQL for PostgreSQL

Oracle and Cloud SQL for PostgreSQL have different architectures and terminology for instances, databases, users, and schemas. For a summary of these differences, see the [terminology](https://docs.cloud.google.com/solutions/migrating-oracle-users-to-cloud-sql-for-postgresql-terminology#terminology) part of this series.

## Exporting Oracle configurations

One of the first steps when planning a migration to Cloud SQL for PostgreSQL is to review the existing parameters settings on the source Oracle database. The settings around memory allocation, character-set, and storage parameters are particularly useful because they can inform the initial configuration and sizing of the Cloud SQL for PostgreSQL target environment. There are several methods for extracting Oracle parameters settings. Here are a few common ones:

  * Automatic Workload Repository (AWR) reports hold resource allocation data (CPU, RAM), instance parameters configuration, and maximum active sessions.
  * `DBA_HIST`, `V$OSSTAT` and `V$LICENSE`for CPU usage details.
  * `V$PARAMETER` view for database configuration parameters.
  * `V$NLS_PARAMETERS` view for database language parameters.
  * `DBA_DATA_FILES` view for calculating the database storage size.
  * The Oracle [`SPFILE`](https://docs.oracle.com/cd/B28359_01/server.111/b28286/statements_6016.htm#SQLRF01315) for database instance configurations.
  * Job scheduler tools (for example, `crontab`) to identify routine backups or maintenance windows that should be taken under consideration.



## Importing and configuring users in Cloud SQL for PostgreSQL

At a high-level, each Oracle schema should be created as its own schema in PostgreSQL. In an Oracle database, _user_ is synonymous with _schema_. That means a schema is created when you create a user. There is always a 1:1 relationship between users and schemas. In PostgreSQL, users and schemas are created separately. A user could be created without creating a corresponding schema. To maintain the same Oracle user or schema structure in PostgreSQL, you can create a schema for each user.

The following table illustrates conversion examples:

Action type | Database type | Command comparison  
---|---|---  
Create user and schema | `Oracle` | `CREATE USER username IDENTIFIED BY password;`  
| `PostgreSQL` | User and schema are distinct concepts in PostgreSQL, therefore require two separate `CREATE` statements  
  
`CREATE USER username WITH PASSWORD 'password';  
CREATE SCHEMA schema_name;`  
Assigning roles | `Oracle` | `GRANT CONNECT TO username;`  
| `PostgreSQL` | `GRANT pg_monitor TO username;`  
Granting privileges | `Oracle` | `GRANT SELECT, INSERT, UPDATE ON HR.EMPLOYEES TO username;`  
| `PostgreSQL` | `GRANT SELECT, INSERT, UPDATE ON HR.EMPLOYEES TO username;`  
Revoking privileges | `Oracle` | `REVOKE UPDATE ON HR.EMPLOYEES FROM username;`  
| `PostgreSQL` | `REVOKE UPDATE ON HR.EMPLOYEES FROM username;`  
Grant DBA/superuser | `Oracle` | `GRANT DBA TO username;`  
| `PostgreSQL` | `GRANT cloudsqlsuperuser TO username;`  
Drop user | `Oracle` | `DROP USER username CASCADE;`  
| `PostgreSQL` | User and schema are distinct concepts in PostgreSQL, therefore require two separate `DROP` statements  
  
`DROP USER username;  
DROP SCHEMA schema_name CASCADE;`  
Users metadata | `Oracle` | `DBA_USERS`  
| `PostgreSQL` | `pg_catalog.pg_user`  
Permissions metadata | `Oracle` | `DBA_SYS_PRIVS  
DBA_ROLE_PRIVS  
SESSION_PRIVS`  
| `PostgreSQL` | `pg_catalog.pg_roles`  
CLI connection string | `Oracle` | `sqlplus username/password@host/tns_alias  
Sqlplus username/password@host:IP/sid`  
| `PostgreSQL` | Without password prompt:  
  
`PGPASSWORD=password psql -h hostname -U username -d database_name`  
  
With password prompt:  
  
`psql -h hostname -U username -W -d database_name`  
  
**Oracle 12c databases users:**

There are two types of users in Oracle 12c, common users and local users. Common users are created in the root CDB including PDBs. They are identified by the `C##` prefix in their username. Local users are created only in a specific PDB. Different database users with identical usernames can be created in multiple PDBs. When migrating from Oracle 12c to PostgreSQL, modify users and permissions to suit PostgreSQL's architecture. Here are two common examples to illustrate these differences:
    
    
    # Oracle local user
    SQL> ALTER SESSION SET CONTAINER=pdb;
    SQL> CREATE USER username IDENTIFIED BY password QUOTA 50M ON USERS;
    
    # PostgreSQL user for a single database and schema
    postgres=> CREATE USER username WITH PASSWORD 'password';
    postgres=> GRANT CONNECT TO DATABASE database_name TO username;
    postgres=> GRANT USAGE ON SCHEMA schema_name TO username;
    postgres=> -- Optionally, grant object privileges in the schema
    postgres=> GRANT ALL ON ALL TABLES IN SCHEMA schema_name TO username;
    postgres=> GRANT ALL ON ALL SEQUENCES IN SCHEMA schema_name TO username;
    postgres=> GRANT ALL ON ALL FUNCTIONS IN SCHEMA schema_name TO username;
    postgres=> GRANT ALL ON ALL PROCEDURES IN SCHEMA schema_name TO username;
    postgres=> GRANT ALL ON ALL ROUTINES IN SCHEMA schema_name TO username;
    
    # Oracle common user
    SQL> CREATE USER c##username IDENTIFIED BY password CONTAINER=ALL;
    
    # PostgreSQL user with permissions for all database (use the local user script above and repeat it for each database and schema)
    

**Managing users through the Google Cloud console**

To view Cloud SQL for PostgreSQL current configured users, go to the following page in the Google Cloud console:

**Google Cloud > Storage > SQL > Instance > Users**

![Screenshot of Users page.](https://docs.cloud.google.com/static/architecture/images/oracle-to-postgresql-users.png)

## Importing table and view definitions

Oracle and PostgreSQL differ in terms of case sensitivity. Oracle names are not case sensitive. PostgreSQL names are not case sensitive except when surrounded by double quotation marks. Many schema export and SQL generating tools for Oracle such as `DBMS_METADATA.GET_DDL` automatically add double quotation marks to object names. These quotation marks can lead to all sorts of problems after migration. We recommend removing all quotation marks surrounding object names from data definition language (DDL) statements before you create the objects in PostgreSQL.

### Create table syntax

When converting tables from Oracle to [PostgreSQL data types](https://www.postgresql.org/docs/12/datatype.html), the first step is to extract the Oracle create table statements from the source database. The following sample query extracts the DDL for the locations table from the HR schema:
    
    
    SQL> SELECT DBMS_METADATA.GET_DDL('TABLE', 'LOCATIONS') FROM DUAL;
    
    CREATE TABLE "HR"."LOCATIONS"
       (  "LOCATION_ID" NUMBER(4,0),
      "STREET_ADDRESS" VARCHAR2(40),
      "POSTAL_CODE" VARCHAR2(12),
      "CITY" VARCHAR2(30) CONSTRAINT "LOC_CITY_NN" NOT NULL ENABLE,
      "STATE_PROVINCE" VARCHAR2(25),
      "COUNTRY_ID" CHAR(2),
      CONSTRAINT "LOC_ID_PK" PRIMARY KEY ("LOCATION_ID")
    ...
          CONSTRAINT "LOC_C_ID_FK" FOREIGN KEY ("COUNTRY_ID")
              REFERENCES "HR"."COUNTRIES" ("COUNTRY_ID") ENABLE
    

The full output includes storage elements, indexes, and tablespace information, which were omitted because these additional elements are not supported by the PostgreSQL `CREATE TABLE` statement.

After the DDL has been extracted, remove quotation marks surrounding names and perform the table conversion according to the Oracle-to-PostgreSQL data types [conversion table](https://docs.cloud.google.com/solutions/migrating-oracle-users-to-cloud-sql-for-postgresql-data-types#data_types). Check each column data type to see if it can be converted as is, or if not supported, choose a different data type according to the conversion table. For example, the following is the converted DDL for the locations table.
    
    
    CREATE TABLE HR.LOCATIONS (
      LOCATION_ID NUMERIC(4,0),
      STREET_ADDRESS VARCHAR(40),
      POSTAL_CODE VARCHAR(12),
      CITY VARCHAR(30) CONSTRAINT LOC_CITY_NN NOT NULL,
      STATE_PROVINCE VARCHAR(25),
      COUNTRY_ID CHAR(2),
      CONSTRAINT LOC_ID_PK PRIMARY KEY (LOCATION_ID),
      CONSTRAINT LOC_C_ID_FK FOREIGN KEY (COUNTRY_ID)
    REFERENCES HR.COUNTRIES (COUNTRY_ID)
    )
    

### Create Table As Select (CTAS)

The `CREATE TABLE AS SELECT` (CTAS) statement is used to create a new table based on an existing table. Note that only column names and column data types are copied, while constraints and indexes are not. PostgreSQL supports the ANSI SQL standard for CTAS functionality, and is compatible with the Oracle CTAS statement.

### Oracle 12c invisible columns

PostgreSQL does not support invisible columns. For a workaround, create a view that holds only the visible columns.

### Table constraints

Oracle provides six types of table constraints that can be defined on table creation or after table creation using the `ALTER TABLE` command. The Oracle constraints types are `PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, `CHECK`, `NOT NULL`, and `REF`. In addition, Oracle lets the user control the state of a constraint through the following options:

  * **`INITIALLY IMMEDIATE`** : Checks the constraint at the end of each subsequent SQL statement (the default state).
  * **`DEFERRABLE/NOT DEFERRABLE`** : Enables the use of the `SET CONSTRAINT` clause in subsequent transactions until a `COMMIT` statement is submitted
  * **`INITIALLY DEFERRED`** : Checks the constraint at the end of subsequent transactions.
  * **`VALIDATE/NO VALIDATE`** : Checks (or deliberately does _not_ check) new or modified rows for errors. These parameters depend on whether the constraint is `ENABLED` or `DISABLED`.
  * **`ENABLED/DISABLED`** : Specifies whether the constraint should be enforced after creation (`ENABLED` by default)



PostgreSQL also supports six types of table constraints: `PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, `CHECK`, `NOT NULL`, and `EXCLUDE`. However, there are a few notable differences between Oracle and PostgreSQL constraint types, including the following:

  * PostgreSQL does not support Oracle's `REF` constraint.
  * PostgreSQL does not automatically create an index on the referencing columns for a foreign key constraint. A separate `CREATE INDEX` statement on the referencing columns is needed if an index is required.
  * PostgreSQL does not support Oracle's `ON DELETE SET NULL` clause. This clause instructs Oracle to set any dependent values in child tables to `NULL` when the record in the parent table is deleted.
  * Constraints on `VIEWS` are not supported, with the exception of [`CHECK OPTION`](https://www.postgresql.org/docs/12/sql-createview.html).
  * PostgreSQL does not support disabling constraints. PostgreSQL supports the `NOT VALID` option when a new foreign key or check constraint is added using an `ALTER TABLE` statement. This option tells PostgreSQL to skip the referential integrity checks on existing records in the child table.



The following table summarizes the key differences between Oracle and PostgreSQL's constraint types:

Oracle constraint type | Cloud SQL for PostgreSQL support | Cloud SQL for PostgreSQL equivalent  
---|---|---  
`PRIMARY KEY` | Yes | `PRIMARY KEY`  
`FOREIGN KEY` | Yes | Uses the same ANSI SQL syntax as Oracle.   
  
Uses the `ON DELETE` clause to handle cases of `FOREIGN KEY` parent record deletions. PostgreSQL provides three options to handle cases where data is deleted from the parent table and a child table is referenced by a `FOREIGN KEY` constraint:  
  


  * `ON DELETE CASCADE`
  * `ON DELETE RESTRICT`
  * `ON DELETE NO ACTION`

  
PostgreSQL does not support Oracle's `ON DELETE SET NULL` clause.   
  
Uses the `ON UPDATE` clause to handle cases of `FOREIGN KEY` parent records updates.  
PostgreSQL provides three options to handle `FOREIGN KEY` constraint update events:  
  


  * `ON UPDATE CASCADE`
  * `ON UPDATE RESTRICT`
  * `ON UPDATE NO ACTION`

  
PostgreSQL does not automatically create an index on the referencing columns for a foreign key constraint.  
`UNIQUE` | Yes | Creates a `UNIQUE` index by default.   
`CHECK` | Yes | `CHECK`  
`NOT NULL` | Yes | `NOT NULL`  
`REF` | No | Not supported.  
`DEFERRABLE/NOT DEFERRABLE` | Yes | `DEFERRABLE/NOT DEFERRABLE`  
`INITIALLY IMMEDIATE` | Yes | `INITIALLY IMMEDIATE`  
`INITIALLY DEFERRED` | Yes | `INITIALLY DEFERRED`  
`VALIDATE/NO VALIDATE` | No | Not supported.  
`ENABLE/DISABLE` | No | Enabled by default. Use the `NOT VALID` option when a new foreign key or check constraint is added to the table using an `ALTER TABLE` statement to skip referential integrity checks on existing records.  
**Constraint on VIEWs** | No | Not supported except the `VIEW WITH CHECK OPTION`.  
**Constraints metadata** | Oracle | `DBA_CONSTRAINTS`  
| PostgreSQL | [`INFORMATION_SCHEMA.TABLE_CONSTRAINTS`](https://dev.mysql.com/doc/refman/5.7/en/information-schema-table-constraints-table.html)  
  
### Virtual and generated columns

Oracle's virtual columns are based on other columns' calculation results. They appear as regular columns, but their values are derived from a calculation on the fly by the Oracle database engine and not stored in the database. Virtual columns can be used with constraints, indexes, table partitioning, and foreign keys, but cannot be manipulated through data manipulation language (DML) operations.

PostgreSQL's [generated columns](https://www.postgresql.org/docs/12/ddl-generated-columns.html) are comparable to Oracle's virtual columns in terms of functionality. However, unlike Oracle, generated columns in PostgreSQL are stored and you must specify a data type for each generated column, meaning that they occupy storage as if they are normal columns.

**Example of a virtual column in Oracle** :
    
    
    SQL> CREATE TABLE PRODUCTS (
            PRODUCT_ID     INT PRIMARY KEY,
            PRODUCT_TYPE   VARCHAR2(100) NOT NULL,
            PRODUCT_PRICE  NUMBER(6,2) NOT NULL,
            PRICE_WITH_TAX AS (ROUND(PRODUCT_PRICE * 1.01, 2))
    );
    
    SQL> INSERT INTO PRODUCTS(PRODUCT_ID, PRODUCT_TYPE, PRODUCT_PRICE)
         VALUES(1, 'A', 99.99);
    
    SQL> SELECT * FROM PRODUCTS;
    
    
    
    PRODUCT_ID PRODUCT_TYPE         PRODUCT_PRICE PRICE_WITH_TAX
    ---------- -------------------- ------------- --------------
             1 A                            99.99         100.99
    

**Equivalent example in PostgreSQL:**
    
    
    postgres=> CREATE TABLE PRODUCTS (
    postgres(>         PRODUCT_ID     INT PRIMARY KEY,
    postgres(>         PRODUCT_TYPE   VARCHAR(100) NOT NULL,
    postgres(>         PRODUCT_PRICE  NUMERIC(6,2) NOT NULL,
    postgres(>         PRICE_WITH_TAX NUMERIC GENERATED ALWAYS AS (ROUND(PRODUCT_PRICE * 1.01, 2)) STORED
    postgres(> );
    
    postgres=> INSERT INTO PRODUCTS(PRODUCT_ID, PRODUCT_TYPE, PRODUCT_PRICE) VALUES(1, 'A', 99.99);
    
    postgres=> SELECT * FROM PRODUCTS;
    
    
    
     product_id | product_type | product_price | price_with_tax
    ------------+--------------+---------------+----------------
              1 | A            |         99.99 |         100.99
    (1 row)
    

### Table indexes

Oracle and PostgreSQL provide a variety of indexing algorithms and types of indexes that can be used for a variety of applications. The following is a list of available indexing algorithms in PostgreSQL:

Index algorithm | Description  
---|---  
**B-tree** | 

  * Default index type for PostgreSQL, used for speeding up equality and range queries 
  * Supports all primitive data types and can be used to retrieve `NULL` values
  * Index values are sorted in ascending order by default but can be configured in a descending order as well 

  
**Hash** | 

  * Used to speed up equality searches
  * More efficient than B-tree index but limited to only handling equality searches

  
**GIN** | 

  * Inverted tree indexes
  * More efficient than B-tree index when dealing with columns that contain multiple component values, such as array and text

  
**GiST** | 

  * Not a single kind of index, but an infrastructure for defining indexes that could support more comparison operators than a normal B-tree index would support
  * Useful for geometric data when optimizing "nearest-neighbor" searches is needed

  
**SP-GiST** | 

  * Similar to GiST, SP-GiST is an infrastructure for user-defined indexing strategies
  * Allows a wide range of different non-balanced data structures such as quadtrees
  * Not available in Cloud SQL for PostgreSQL

  
**BRIN** | 

  * Block Range INdexes
  * Stores summaries of physical block ranges of a table
  * For columns with a linear sort order
  * Useful for range lookup on huge tables

  
  
The following table compares the index types between Oracle and PostgreSQL:

Oracle index | Description | Supported by PostgreSQL | PostgreSQL equivalent   
---|---|---|---  
**Bitmap index** | Stores a bitmap for each index key, best suited for providing fast data retrieval for OLAP workloads | No | N/A  
**B-tree index** | Most common index type, well suited for a variety of workloads and can be configured in `ASC|DESC` sorting. | Yes | B-tree index  
**Composite index** | Created over two or more columns to improve the performance of data retrieval. Column ordering inside the index determines the access path.  | Yes | [Multiple-column indexes](https://www.postgresql.org/docs/12/indexes-multicolumn.html)  
Up to 32 columns can be specified when creating a multiple-column index.  
**Function-based index** | Stores the output of a function applied on the values of a table column. | Yes | [Indexes on expressions](https://www.postgresql.org/docs/12/indexes-expressional.html)  
**Unique index** | A B-tree index which enforces a `UNIQUE` constraint on the indexed values on a per column basis.  | Yes | [Unique index](https://dev.mysql.com/doc/refman/5.7/en/glossary.html#glos_unique_index)  
**Application domain index** | Suited for indexing non-relational data such as audio/video data, LOB data and other non-textual types.  | No | N/A   
**Invisible index** | Oracle feature that lets you manage, maintain, and test indexes without affecting the optimizer decision making. | No | For an alternative solution, you can create an additional index on a read-replica for test purposes without affecting on-going activity.  
**Index-organized table** | A type of index that controls how data is stored at the table and index level. | No | PostgreSQL does not support index-organized tables. The [`CLUSTER`](https://www.postgresql.org/docs/12/sql-cluster.html) statement instructs PostgreSQL to organize table storage according to a specified index. It serves a similar purpose to Oracle's index-organized table. However, clustering is a one-time operation, and PostgreSQL does not maintain the structure of the table on subsequent updates. Manual, periodic clustering is needed.  
**Local and global index** | Used for indexing partitioned tables in an Oracle database. Each index is defined as either `LOCAL` or `GLOBAL`. | No | PostgreSQL partitions work indexes have the same functionality as Oracle local indexes (i.e., the index is defined at the partition level, global level is not supported).   
**Partial indexes for partitioned tables (Oracle 12c)** | Creates an index on a subset of a table's partitions. Supports `LOCAL` and `GLOBAL`. | Yes  | Partitioning in PostgreSQL works by attaching child tables into a parent table. It's possible to create indexes only on a subset of child tables.  
`CREATE/DROP INDEX` | Command used for index creation and dropping. | Yes | PostgreSQL supports the `CREATE INDEX` command. It also supports `ALTER TABLE tableName ADD INDEX indexName columnName`  
`ALTER INDEX ... REBUILD` | Rebuilds the index, which can cause an exclusive lock on the indexed table.  | Requires different syntax | PostgreSQL supports index rebuilds using the [`REINDEX`](https://www.postgresql.org/docs/12/sql-reindex.html) statement. The table is locked for writes during this operation and only reads are allowed.  
`ALTER INDEX ... REBUILD ONLINE` | Rebuilds an index without creating an exclusive lock on the table. | Requires different syntax | PostgreSQL supports concurrent index rebuilds using the `REINDEX TABLE CONCURRENTLY` statement. In this mode, PostgreSQL tries to rebuild indexes using minimum locking with the trade-off of potentially taking more time and resources to complete the rebuild.  
**Index compression** | A feature to reduce index physical size. | No | N/A  
**Allocate**  
**index to a tablespace** | Creates an index tablespace that can be stored on a separate disk from table data to reduce disk I/O bottlenecks. | No | Although PostgreSQL allows an index to be created in user-defined tablespace, you cannot create tablespaces in Cloud SQL for PostgreSQL, and the index has to be built in default tablespace.  
**Indexes metadata (tables/views)** | **Oracle** | `DBA_INDEXES  
DBA_PART_INDEXES  
DBA_IND_COLUMNS` |   
| **PostgreSQL** | `pg_catalog.pg_index  
pg_catalog.pg_attribute  
pg_catalog.pg_class` |   
  
**Index conversion considerations**

In most cases, Oracle indexes can simply be converted to PostgreSQL's B-tree indexes, because this type of index is the most commonly used index type. As in an Oracle database, an index is automatically created on the `PRIMARY KEY` fields of a table. Similarly, a `UNIQUE` index is automatically created on fields which have a `UNIQUE` constraint. In addition, secondary indexes are created using the standard `CREATE INDEX` statement.

The following example illustrates how an Oracle table with multiple indexed fields can be converted to PostgreSQL:
    
    
    SQL> CREATE TABLE ORA_IDX_TO_PG (
            col1 INT PRIMARY KEY,
            col2 VARCHAR2(60),
            col3 DATE,
            col4 CLOB,
            col5 VARCHAR2(20)
          );
    
    -- Single-field index
    SQL> CREATE INDEX idx_col2 ON ora_idx_to_pg(col2);
    
    -- Composite index
    SQL> CREATE INDEX idx_cols3_2 ON ora_idx_to_pg(col3 DESC, col2);
    
    -- Unique index
    SQL> CREATE UNIQUE INDEX idx_col3_uni ON ora_idx_to_pg(col3);
    
    -- Function-based index
    SQL> CREATE INDEX idx_func_col3 ON
            ora_idx_to_pg(EXTRACT(MONTH FROM col3));
    
    -- CLOB index
    SQL> CREATE INDEX idx_col4 ON
           ora_idx_to_pg(col4) INDEXTYPE IS CTXSYS.CONTEXT;
    
    -- Invisible index
    SQL> CREATE INDEX idx_col5_inv ON
            ora_idx_to_pg(col5) INVISIBLE;
    
    -- Drop index
    SQL> DROP INDEX idx_col5_inv;
    
    postgres=> CREATE TABLE ORA_IDX_TO_PG (
    postgres(> col1 INT PRIMARY KEY,
    postgres(> col2 VARCHAR(60),
    postgres(> col3 DATE,
    postgres(> col4 TEXT,
    postgres(> col5 VARCHAR(20)
    postgres(> );
    
    -- Single index (supported)
    postgres=> CREATE INDEX idx_col2 ON ora_idx_to_pg(col2);
    
    -- Composite index (supported)
    postgres=> CREATE INDEX idx_cols3_2 ON ora_idx_to_pg(col3 DESC, col2);
    
    -- Unique index (supported)
    postgres=> CREATE UNIQUE INDEX idx_col3_uni ON ora_idx_to_pg(COL3);
    
    -- Function-based index (supported)
    postgres=> CREATE INDEX idx_func_col3 ON
    postgres->         ora_idx_to_pg(EXTRACT(MONTH FROM col3));
    
    -- CLOB (Supported, but requires different syntax. See Full Text Search for details)
    postgres=> CREATE INDEX idx_col4 ON ora_idx_to_pg
    postgres->         USING GIN (to_tsvector('english', col4));
    
    -- Invisible index (not supported)
    -- Optional - create the index as a B-tree index
    postgres=> CREATE INDEX idx_col5 ON ora_idx_to_pg(col5);
    
    -- Drop index
    postgres=> DROP INDEX idx_col2;
    
    SQL> SELECT ui.table_name,
                ui.index_name,
                ui.index_type,
                ic.column_name
         FROM user_indexes ui JOIN user_ind_columns ic
         ON ui.index_name = ic.index_name
         WHERE ui.table_name = 'ORA_IDX_TO_PG'
         ORDER BY 4;
    
    postgres=> select distinct
    postgres->     t.relname as table_name,
    postgres->     i.relname as index_name,
    postgres-> pg_get_indexdef(ix.indexrelid) index_definition
    postgres-> from
    postgres->     pg_class t,
    postgres->     pg_class i,
    postgres->     pg_index ix
    postgres-> where
    postgres->     t.oid = ix.indrelid
    postgres->     and i.oid = ix.indexrelid
    postgres->     and t.relname = 'ora_idx_to_pg'
    postgres-> order by
    postgres->     t.relname,
    postgres->     i.relname;
    
    -- OR Use psql \d command:
    postgres=> \d ora_idx_to_pg
                      Table "public.ora_idx_to_pg"
     Column |         Type          | Collation | Nullable | Default
    --------+-----------------------+-----------+----------+---------
     col1   | integer               |           | not null |
     col2   | character varying(60) |           |          |
     col3   | date                  |           |          |
     col4   | text                  |           |          |
     col5   | character varying(20) |           |          |
    Indexes:
        "ora_idx_to_pg_pkey" PRIMARY KEY, btree (col1)
        "idx_col2" btree (col2)
        "idx_col4" gin (to_tsvector('english'::regconfig, col4))
        "idx_col5" btree (col5)
        "idx_cols3_2" btree (col3 DESC, col2)
        "idx_func_col3" btree (date_part('month'::text, col3))
    
    postgres=>
    

## Table partitioning

Both Oracle and PostgreSQL offer partitioning capabilities for splitting up large tables. This is accomplished by physically segmenting a table into smaller parts, where each part contains a horizontal subset of the rows. The partitioned table is referred to as the parent table and its rows are physically stored in its partitions. Though not all of Oracle's partition types are supported in PostgreSQL, PostgreSQL does support the most common ones.

The following sections describe the PostgreSQL supported partition types, illustrating each one with an example on how to create the partitions that correspond to that type.

### RANGE partitioning

This type of partition assigns rows to partitions based on column values falling within a given range. Each partition contains rows for which the partitioning expression value lies within a given range. It's important to note that ranges do not overlap across partitions.

**Example**
    
    
    CREATE TABLE employees (
     empid     INT,
     fname     VARCHAR(30),
     lname     VARCHAR(30),
     hired     DATE,
     separated DATE,
     job_code  INT,
     store_id  INT)
     PARTITION BY RANGE (store_id);
    
    CREATE TABLE employees_p0 PARTITION OF employees
     FOR VALUES FROM (MINVALUE) TO (6);
    CREATE TABLE employees_p1 PARTITION OF employees
     FOR VALUES FROM (6) TO (11);
    CREATE TABLE employees_p2 PARTITION OF employees
     FOR VALUES FROM (11) TO (16);
    CREATE TABLE employees_p3 PARTITION OF employees
     FOR VALUES FROM (16) TO (21);
    

### LIST partitioning

Similar to `RANGE` partitioning, `LIST` partitioning assigns rows to partitions based on column values falling within a predefined set of values. Key values that appear in each partition are explicitly listed for `LIST` partitions.

**Example**
    
    
    CREATE TABLE employees (
     empid     INT,
     fname     VARCHAR(30),
     lname     VARCHAR(30),
     hired     DATE,
     separated DATE,
     job_code  INT,
     store_id  INT)
     PARTITION BY LIST (store_id);
    
    CREATE TABLE employees_pNorth PARTITION OF employees
     FOR VALUES IN (3,5,6);
    CREATE TABLE employees_pEast PARTITION OF employees
     FOR VALUES IN (1,2,10);
    CREATE TABLE employees_pWest PARTITION OF employees
     FOR VALUES IN (4,12,13);
    CREATE TABLE employees_pCnrl PARTITION OF employees
     FOR VALUES IN (7,8,15);
    

### HASH partitioning

`HASH` partitioning is best suited for when the goal is to achieve an even distribution of data between all partitions. A column value (or expression based on a column value to be hashed) and the row value are assigned to the partition that corresponds to that hash value. Hash values must be uniquely assigned to partitions, and all inserted values must be mapped to exactly one partition.

**Example**
    
    
    CREATE TABLE employees (
     empid     INT,
     fname     VARCHAR(30),
     lname     VARCHAR(30),
     hired     DATE,
     separated DATE,
     job_code  INT,
     store_id  INT)
     PARTITION BY HASH (date_part('year', hired));
    
    CREATE TABLE employees_p0 PARTITION OF employees
     FOR VALUES WITH (MODULUS 4, REMAINDER 0);
    CREATE TABLE employees_p1 PARTITION OF employees
     FOR VALUES WITH (MODULUS 4, REMAINDER 1);
    CREATE TABLE employees_p2 PARTITION OF employees
     FOR VALUES WITH (MODULUS 4, REMAINDER 2);
    CREATE TABLE employees_p3 PARTITION OF employees
     FOR VALUES WITH (MODULUS 4, REMAINDER 3);
    

### Multi-level partitioning

Multi-level partitioning is a method of creating a hierarchy of partitions for a single table. Each partition is further divided into a number of different partitions. The number of sub-partitions can vary from one partition to another.

**Example**
    
    
    CREATE TABLE sales (
     Saleid    INT,
     sale_date DATE,
     cust_code VARCHAR(15),
     income    DECIMAL(8,2))
    PARTITION BY RANGE(date_part('year', sale_date));
    
    CREATE TABLE sales_2019 PARTITION OF sales
     FOR VALUES FROM (2019) TO (2020)
     PARTITION BY RANGE(date_part('month', sale_date));
    
    CREATE TABLE sales_2019_q1 PARTITION OF sales_2019
     FOR VALUES FROM (1) TO (4);
    CREATE TABLE sales_2019_q2 PARTITION OF sales_2019
     FOR VALUES FROM (4) TO (7);
    CREATE TABLE sales_2019_q3 PARTITION OF sales_2019
     FOR VALUES FROM (7) TO (10);
    CREATE TABLE sales_2019_q4 PARTITION OF sales_2019
     FOR VALUES FROM (10) TO (13);
    
    CREATE TABLE sales_2020 PARTITION OF sales
     FOR VALUES FROM (2020) TO (2021)
     PARTITION BY RANGE(date_part('month', sale_date));
    
    CREATE TABLE sales_2020_q1 PARTITION OF sales_2020
     FOR VALUES FROM (1) TO (4);
    CREATE TABLE sales_2020_q2 PARTITION OF sales_2020
     FOR VALUES FROM (4) TO (7);
    CREATE TABLE sales_2020_h2 PARTITION OF sales_2020
     FOR VALUES FROM (7) TO (13);
    

### Attaching or detaching partitions

In PostgreSQL, partitions can be added or removed from the parent table. A partition that is detached can later be reattached to the same table. Moreover, new partitioning conditions can be specified when reattaching the partition, which allows partition boundaries to be adjusted.

**Example**
    
    
    CREATE TABLE employees (
     empid     INT,
     fname     VARCHAR(30),
     lname     VARCHAR(30),
     hired     DATE,
     separated DATE,
     job_code  INT,
     store_id  INT)
     PARTITION BY RANGE (date_part('year', hired));
    
    CREATE TABLE employees_p0 PARTITION OF employees
     FOR VALUES FROM (2010) TO (2015);
    CREATE TABLE employees_p1 PARTITION OF employees
     FOR VALUES FROM (2015) TO (2020);
    
    -- changing partition boundaries
    BEGIN TRANSACTION;
    ALTER TABLE employees DETACH PARTITION employees_p1;
    ALTER TABLE employees ATTACH PARTITION employees_p1 FOR VALUES FROM (2015) TO (2022);
    COMMIT TRANSACTION;
    

The following table describes where Oracle and Cloud SQL for PostgreSQL partition types are equivalent and where a conversion is recommended:

Oracle partition type | Supported by PostgreSQL | PostgreSQL implementation  
---|---|---  
`RANGE` partitions | Yes | `PARTITION BY RANGE`  
`LIST` partitions | Yes | `PARTITION BY LIST`  
`HASH` partitions | Yes | `PARTITION BY HASH`  
`SUB-PARTITIONING` | Yes | Multi-level partitioning  
**Interval partitions** | No | Not supported  
**Partition advisor** | No | Not supported  
**Preference partitioning** | No | Not supported  
**Virtual column-based partitioning** | No | As a workaround, consider partitioning with the virtual column expression directly:  
  
`CREATE TABLE users (  
id INT,  
username VARCHAR(20),  
first_letter VARCHAR(1)  
GENERATED ALWAYS AS  
(  
UPPER(SUBSTR(TRIM(username), 1, 1))  
) STORED  
)  
PARTITION BY LIST (UPPER(SUBSTR(TRIM(username), 1, 1)));`  
**Automatic list partitioning** | No | Not supported  
**Split**  
**partitions** | No | For a workaround, consider detaching or attaching table partitions to adjust partition boundaries  
**Exchange partitions** | Yes | `DETACH / ATTACH PARTITION`  
**Multi-type partitioning (composite partitioning)** | Yes | Multi-level partitioning  
**Partitions metadata** | Oracle | `DBA_TAB_PARTITIONS  
DBA_TAB_SUBPARTITIONS`  
| PostgreSQL | `pg_catalog.pg_class  
pg_catalog.pg_partitioned_table`  
  
The following example is a side-by-side comparison of creating table partitions on both platforms. Note that PostgreSQL does not support referencing a tablespace in the `PARTITIONS` clause of the `CREATE TABLE` command.

**Oracle implementation**

`CREATE TABLE employees (  
empid NUMBER,  
fname VARCHAR2(30),  
lname VARCHAR2(30),  
hired DATE,  
separated DATE,  
job_code NUMBER,  
store_id NUMBER)  
PARTITION BY LIST (store_id) (  
PARTITION employees_pNorth VALUES (3,5,6) TABLESPACE users,  
PARTITION employees_pEast VALUES (1,2,10) TABLESPACE users,  
PARTITION employees_pWest VALUES (4,12,13) TABLESPACE users,  
PARTITION employees_pCnrl VALUES (7,8,15) TABLESPACE users  
);`

**PostgreSQL implementation**

`CREATE TABLE employees (  
empid INT,  
fname VARCHAR(30),  
lname VARCHAR(30),  
hired DATE,  
separated DATE,  
job_code INT,  
store_id INT)  
PARTITION BY LIST (store_id);  
  
CREATE TABLE employees_pNorth PARTITION OF employees  
FOR VALUES IN (3,5,6);  
CREATE TABLE employees_pEast PARTITION OF employees  
FOR VALUES IN (1,2,10);  
CREATE TABLE employees_pWest PARTITION OF employees  
FOR VALUES IN (4,12,13);  
CREATE TABLE employees_pCnrl PARTITION OF employees  
FOR VALUES IN (7,8,15);`

## Temporary tables

In an Oracle database, temporary tables are called `GLOBAL TEMPORARY TABLES`, while in PostgreSQL, they are known simply as temporary tables. The basic functionality of a temporary table is identical on both platforms. There are, however, a few notable differences:

  * Oracle stores the temporary table structure for repeated use even after a database restart, while PostgreSQL stores the temporary table only for the duration of a session.
  * A temporary table in an Oracle database can be accessed by different users with the appropriate permissions. By contrast, a temporary table in PostgreSQL can only be accessed during the session in which it was created unless the temporary table is referenced with schema-qualified names.
  * In an Oracle database, there is a distinction between `GLOBAL` and `LOCAL` temporary tables that specify whether the content of the table is global or session specific. In PostgreSQL, the `GLOBAL` and `LOCAL` keywords are supported for compatibility reasons, but they have no effect on the visibility of the data.
  * If the `ON COMMIT` clause is omitted when creating a temporary table, the default behavior in Oracle Database is `ON COMMIT DELETE ROWS`, which means that Oracle truncates the temporary table after each commit. By contrast, in PostgreSQL the default behavior is to preserve rows in the temporary table after each commit.



The following table highlights the differences in temporary tables between Oracle and Cloud SQL for PostgreSQL.

Temporary table feature | Oracle implementation | PostgreSQL implementation  
---|---|---  
**Syntax** | `CREATE GLOBAL TEMPORARY TABLE` | `CREATE TEMPORARY TABLE`  
**Accessibility** | Accessible from multiple sessions | Accessible from the creator's session only unless referenced with schema-qualified names  
**Index support** | Yes | Yes  
**Foreign key support** | Yes | Yes  
**Preserve DDL** | Yes | No  
**`ON COMMIT` default action** | Records are deleted | Records are preserved  
`ON COMMIT PRESERVE ROWS` | Yes | Yes  
`ON COMMIT DELETE ROWS` | Yes | Yes  
`ON COMMIT DROP` | No | Yes  
**`ALTER TABLE`support** | Yes | Yes  
**Gathering statistics** | `DBMS_STATS.GATHER_TABLE_STATS` | `ANALYZE`  
**Oracle 12c`GLOBAL_TEMP_`**  
  
`TABLE_STATS` | `DBMS_STATS.SET_TABLE_PREFS` | `ANALYZE`  
  
### Unused columns

Oracle's feature of marking specific columns as `UNUSED` is often used to remove columns from tables without physically removing the column data. This is to prevent the potential high loads that occur when dropping columns from large tables.

In PostgreSQL, dropping a large column does not remove the column data from the physical storage and is therefore a fast operation even on large tables. There is no need to mark a column as `UNUSED` as in an Oracle database. The space occupied by the dropped column is reclaimed either by new DML statements or during a subsequent [`VACUUM`](https://www.postgresql.org/docs/12/sql-vacuum.html) operation.

### Read-only tables

Read-only tables is an Oracle feature which marks tables as read-only using the `ALTER TABLE` command. In Oracle 12c R2, this feature is also available for tables with partitions and subpartitions. PostgreSQL does not offer an equivalent feature, but there are two possible workarounds:

  * Grant `SELECT` permission on tables for specific users. Note that this does not preclude the table owner from performing DML operations on their tables.
  * Create a Cloud SQL for PostgreSQL [read replica](https://docs.cloud.google.com/sql/docs/postgres/replication/create-replica) and direct users to the replica tables that are read-only tables. This solution requires adding a read-replica instance to an existing Cloud SQL for PostgreSQL instance.
  * Create a database trigger that raises exceptions on DML statements—for example:
        
        -- Define trigger function
        CREATE OR REPLACE FUNCTION raise_readonly_exception() RETURNS TRIGGER AS $$
        BEGIN
          RAISE EXCEPTION 'Table is readonly!';
          RETURN NULL;
        END;
        $$ LANGUAGE 'plpgsql';
        
        -- Fire trigger when DML statements is executed on read only table
        CREATE TRIGGER myTable_readonly_trigger
        BEFORE INSERT OR UPDATE OR DELETE OR TRUNCATE ON myTable FOR EACH STATEMENT
        EXECUTE PROCEDURE raise_readonly_exception();
        
        -- Testing the trigger
        postgres=> INSERT INTO myTable (id) VALUES (1);
        ERROR:  Table is readonly!
        CONTEXT:  PL/pgSQL function raise_readonly_exception() line 3 at RAISE
        postgres=>
        




## Character sets

Both Oracle and PostgreSQL support a wide variety of character sets, collations, and unicode, including support for both single-byte and multi-byte languages. In addition, PostgreSQL databases that reside on the same instance can be configured with distinct character sets. See the [list of supported character sets in PostgreSQL](https://www.postgresql.org/docs/12/multibyte.html#MULTIBYTE-CHARSET-SUPPORTED).

In Oracle Database, character sets are specified at the database level (Oracle 12g R1 or earlier) or at pluggable database level (Oracle 12g R2 or later). In PostgreSQL, a default character set is specified when a new Cloud SQL for PostgreSQL instance is [created](https://docs.cloud.google.com/sql/docs/postgres/create-manage-databases#create). Each database created within that instance can be created with a different character set. [Sort order and character classification](https://www.postgresql.org/docs/12/collation.html#COLLATION-MANAGING) can be specified per table column.

**Example**
    
    
    -- Create a database using UTF-8 character set and ja_JP.UTF collation
    postgres=> CREATE DATABASE jpdb WITH ENCODING 'UTF8' LC_COLLATE='ja_JP.UTF8' LC_CTYPE='ja_JP.UTF8' TEMPLATE=template0;
    
    -- Query the character set and collation settings of all databases
    postgres=> SELECT datname AS DATABASE_NAME, datcollate AS LC_COLLATE, datctype AS LC_CTYPE from pg_database;
     database_name | lc_collate |  lc_ctype
    ---------------+------------+------------
     cloudsqladmin | en_US.UTF8 | en_US.UTF8
     template0     | en_US.UTF8 | en_US.UTF8
     template1     | en_US.UTF8 | en_US.UTF8
     postgres      | en_US.UTF8 | en_US.UTF8
     jpdb          | ja_JP.UTF8 | ja_JP.UTF8
    (5 rows)
    
    -- Alternatively, use psql \l command to query the database settings
    postgres=> \l
                                                    List of databases
         Name      |       Owner       | Encoding |  Collate   |   Ctype    |            Access privileges
    ---------------+-------------------+----------+------------+------------+-----------------------------------------
     cloudsqladmin | cloudsqladmin     | UTF8     | en_US.UTF8 | en_US.UTF8 |
     postgres      | cloudsqlsuperuser | UTF8     | en_US.UTF8 | en_US.UTF8 | =Tc/cloudsqlsuperuser                  +
                   |                   |          |            |            | cloudsqlsuperuser=CTc/cloudsqlsuperuser+
                   |                   |          |            |            | testuser=CTc/cloudsqlsuperuser
     template0     | cloudsqladmin     | UTF8     | en_US.UTF8 | en_US.UTF8 | =c/cloudsqladmin                       +
                   |                   |          |            |            | cloudsqladmin=CTc/cloudsqladmin
     template1     | cloudsqlsuperuser | UTF8     | en_US.UTF8 | en_US.UTF8 | =c/cloudsqlsuperuser                   +
                   |                   |          |            |            | cloudsqlsuperuser=CTc/cloudsqlsuperuser
    -- Specifying column level collation
    postgres=> CREATE TABLE test1 (
    postgres(>     a text COLLATE "de_DE",
    postgres(>     b text COLLATE "es_ES"
    postgres(> );
    

## Views

PostgreSQL supports both simple and complex views. For view-creation options, there are a few differences between Oracle and PostgreSQL. The following table highlights these differences.

Oracle view feature | Description | Cloud SQL for PostgreSQL support | Conversion considerations  
---|---|---|---  
`FORCE` | Create a view without verifying if the source tables/views exist. | No | No equivalent option available.  
`CREATE OR REPLACE` | Create a non-existing view or overwrite an existing view. | Yes | PostgreSQL supports the `CREATE OR REPLACE` command for views.  
`WITH CHECK OPTION` | Specifies the level of enforcement when performing DML operations against the view. | Yes | Default is `CASCADED`, which causes referenced views to be evaluated as well.  
  
The `LOCAL` keyword causes only the current view to be evaluated.  
`WITH READ-ONLY` | Permits only read operations on the view. DML operations are forbidden. | No | A workaround is to grant SELECT privileges on the view to all users.  
`VISIBLE | INVISIBLE` (Oracle 12c) | Specify whether a column based on the view is visible or invisible to the user. | No | Create the `VIEW` with the required columns only.  
  
The following conversion example demonstrates converting from Oracle to Cloud SQL PostgreSQL for views.
    
    
    -- Create view to retrieve employees from department 100 using the WITH CHECK -- OPTION option
    SQL> CREATE OR REPLACE FORCE VIEW vw_emp_dept100
    AS
    SELECT EMPLOYEE_ID,
           FIRST_NAME,
           LAST_NAME,
           SALARY,
           DEPARTMENT_ID
    FROM EMPLOYEES
    WHERE DEPARTMENT_ID=100
    WITH CHECK OPTION;
    
    -- Perform an UPDATE operation on the VIEW
    SQL> UPDATE vw_emp_dept100
         SET salary=salary+1000;
    
    postgres=> CREATE OR REPLACE VIEW vw_emp_dept100
    postgres-> AS
    postgres-> SELECT EMPLOYEE_ID,
    postgres->        FIRST_NAME,
    postgres->        LAST_NAME,
    postgres->        SALARY,
    postgres->        DEPARTMENT_ID
    postgres-> FROM EMPLOYEES
    postgres-> WHERE DEPARTMENT_ID=100
    postgres-> WITH CHECK OPTION;
    
    -- Perform an UPDATE operation on the VIEW
    postgres=> UPDATE vw_emp_dept100
    postgres-> SET salary=salary+1000;
    
    -- Update one employee department id to 60
    postgres=> UPDATE vw_emp_dept100
    postgres-> SET DEPARTMENT_ID=60
    postgres-> WHERE EMPLOYEE_ID=110;
    
    ERROR:  new row violates check option for view "vw_emp_dept100"
    DETAIL:  Failing row contains (110, John, Chen, JCHEN, 515.124.4269, 1997-09-28, FI_ACCOUNT, 9200.00, null, 108, 60).
    

### View access management:

The owners of a view must have privileges on the base tables to create the view. The user of a view needs the appropriate `SELECT` permissions on the view. They also need the appropriate `INSERT`, `UPDATE`, `DELETE` permissions on the view when performing DML operations through the view. In either case, users don't need permissions on the underlying tables.

## What's next

  * Explore more about [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/users) user accounts.
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
