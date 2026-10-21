---
url: https://docs.cloud.google.com/alloydb/docs/migration-overview/
title: Migration overview \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:46:06.228690+00:00
---

# Migration overview  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/migration-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Migration overview Stay organized with collections  Save and categorize content based on your preferences. 

To move databases into or out of AlloyDB for PostgreSQL, you can migrate active PostgreSQL instances with minimal downtime using Database Migration Service or import and export CSV, DMP, and SQL files stored in Cloud Storage.

## Importing data

You can migrate data into AlloyDB through two methods:

  * Manually importing files containing your data.

  * Using Database Migration Service to migrate the contents of a whole, active PostgreSQL instance into a new AlloyDB cluster. For more information, see [Migrate to AlloyDB for PostgreSQL using Database Migration Service](https://docs.cloud.google.com/alloydb/docs/migrate-with-dms).


**Caution:** If your source database uses a default collation based on a locale provided by `libc`, you might need to add ICU-based collations to your tables after importing their data into AlloyDB. For more information, see Supported locales for imported data.

### Import archived data from files

AlloyDB lets you import data from files located in a Cloud Storage bucket. AlloyDB supports a variety of file formats for data import, including the following:

  * [CSV](https://docs.cloud.google.com/alloydb/docs/import-csv-file), with the contents of one table per file, loaded using `psql`.

  * [DMP](https://docs.cloud.google.com/alloydb/docs/import-dmp-file), a binary archive of a whole PostgreSQL database, imported using `pg_restore`.

  * [SQL](https://docs.cloud.google.com/alloydb/docs/import-sql-file), a plain-text reconstruction of a PostgreSQL database, processed with `psql`.




### Migrate an active instance with Database Migration Service

As an alternative to manually importing data-dump files, you can use [Database Migration Service for AlloyDB](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest). This service lets you migrate the entire contents of an active PostgreSQL instance—including all of its databases and metadata—into a new AlloyDB cluster. Database Migration Service can help you transition your existing applications to using AlloyDB as their new datastore with minimal downtime.

### Supported locales for imported data

AlloyDB supports the following [locales](https://www.postgresql.org/docs/17//locale.html):

  * The full set of ICU-provided locales.
  * A limited set of locales provided by `libc`: 
    * `C.UTF-8`
    * `en_US.utf8`



If the database you want to import into AlloyDB defaults to a `libc` locale other than the two listed here, you can still import your data, but that default won't carry over. To ensure that SQL queries using `ORDER BY` sort their results properly, you might need to take additional steps after importing your data.

Google recommends allowing your new database to use the default locale for AlloyDB: `C.UTF-8`, provided by `libc`. Then, associate [collations](https://www.postgresql.org/docs/17//collation.html) with any columns that your application's queries might involve in `ORDER BY` clauses, naming an appropriate ICU-based collation for each one. You can do this through [`ALTER TABLE` DDL queries](https://www.postgresql.org/docs/17//sql-altertable.html), such as the following:
    
    
    ALTER TABLE TABLE_NAME
        ALTER COLUMN COLUMN_NAME
        SET DATA TYPE COLUMN_DATA_TYPE
        COLLATE "COLLATION_NAME";
    

Replace the following:

  * `TABLE_NAME`: the name of the table containing the column.
  * `COLUMN_NAME`: the name of the column to update.
  * `COLUMN_DATA_TYPE`: the data type of the column.
  * `COLLATION_NAME`: the name of the ICU-based collation to apply.



A new AlloyDB cluster defines hundreds of collations based on ICU-provided locales, and you can add more using [the PostgreSQL `CREATE COLLATION` facility](https://www.postgresql.org/docs/17//sql-createcollation.html). To see the full list of ICU-based collation names defined on an AlloyDB cluster, run the following query on any of its instances:
    
    
    SELECT collname FROM pg_collation WHERE collprovider = 'i';
    

In addition to ICU-based collations, AlloyDB supports the PostgreSQL built-in collation named `ucs_basic`. This collation uses the standard order of Unicode code points to enable especially efficient sorting. Google recommends its use with columns whose appropriate sort order matches that of the Unicode code-point list.

## Exporting data

You can use command-line utilities to export your AlloyDB data into files stored on a Cloud Storage bucket, in a variety of formats:

  * [CSV](https://docs.cloud.google.com/alloydb/docs/export-csv-file), exporting one table per file, using `psql`.

  * [DMP](https://docs.cloud.google.com/alloydb/docs/export-dmp-file), using `pg_dump` to create a portable, binary archive of your whole database.

  * [SQL](https://docs.cloud.google.com/alloydb/docs/export-sql-file), using `pg_dump` to create a list of DDL and SQL statements to reconstruct your database.




## What's next

  * [Migrate data from a vector database to AlloyDB using LangChain](https://docs.cloud.google.com/alloydb/docs/ai/migrate-data-from-langchain-vector-stores-to-alloydb).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
