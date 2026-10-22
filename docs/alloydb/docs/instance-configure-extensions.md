---
url: https://docs.cloud.google.com/alloydb/docs/instance-configure-extensions/
title: Configure database extensions \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:27:43.170316+00:00
---

# Configure database extensions  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/instance-configure-extensions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Configure database extensions Stay organized with collections  Save and categorize content based on your preferences. 

To add extra functionality to your AlloyDB for PostgreSQL databases—such as vector search, geospatial indexing, or query auditing—you can enable, update, and disable supported PostgreSQL extensions.

See [Supported database extensions](https://docs.cloud.google.com/alloydb/docs/reference/extensions) for the list of the extensions that AlloyDB supports.

## Enable an extension

In general, you enable an extension by connecting to a database in an AlloyDB cluster's primary instance and entering a `LOAD` or `CREATE EXTENSION` command.

However, some extensions require you to set one or more database flags **before** you can use the `LOAD` or `CREATE EXTENSION` command to enable the extension. You set these flags on the AlloyDB instance where you want to use the extension, whether that instance is the primary instance or read pool instance.

### Procedure

  1. If required, [ set the appropriate database flags](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags) on the instance where you want to use the extension, either the primary instance or a read pool instance.

The [list of supported extensions](https://docs.cloud.google.com/alloydb/docs/reference/extensions) shows which extensions require this step and states which database flags you must set.

  2. Connect a `psql` client to the cluster's primary instance, as described in [Connect a psql client to an instance](https://docs.cloud.google.com/alloydb/docs/connect-psql).

**Note:** You must connect to the primary instance even if you are enabling the extension on a read pool instance.
  3. At the `psql` command prompt, connect to the database and create the extension: 
         
         \c DB_NAME
         CREATE EXTENSION IF NOT EXISTS EXTENSION_NAME;

**Note:** To create the [`auto_explain`](https://www.postgresql.org/docs/17/auto-explain.html) extension, use the `LOAD` command.
  4. If you want, repeat the previous step to connect to other databases and create the extension in each of them.



## Update an extension

Although AlloyDB maintenance updates automatically install the latest extension binaries on your instance's underlying software, they don't automatically update the extension's database catalog. You are responsible for manually updating your extensions to make sure they use the latest supported versions.

To determine which extensions require an update, compare your installed version with the latest supported version listed in the [Supported extensions reference table](https://docs.cloud.google.com/alloydb/docs/reference/extensions).

Connect to your database and run the following command to see your installed versions:
    
    
    SELECT * FROM pg_extension;
    

To update an extension to the latest version available on your instance, use the `ALTER EXTENSION` command.

Connect to the cluster's primary instance using a client of your choice, such as AlloyDB Studio or a `psql` client, and run the following command for each extension that you want to update:
    
    
    ALTER EXTENSION EXTENSION_NAME UPDATE;
    

If you need to update to a specific version, use the following syntax:
    
    
    ALTER EXTENSION EXTENSION_NAME UPDATE TO 'VERSION_NUMBER';
    

## Disable an extension

You disable an extension by reversing the procedure used to enable it.

  1. Connect a `psql` client to the cluster's primary instance, as described in [Connect a psql client to an instance](https://docs.cloud.google.com/alloydb/docs/connect-psql).

**Note:** You must connect to the primary instance even if you are disabling an extension that is only being used on read pool instances.
  2. At the `psql` command prompt, connect to the database that has the extension enabled and drop the extension: 
         
         \c DB_NAME
         DROP EXTENSION EXTENSION_NAME;

  3. Repeat the previous step to connect to any other databases that have the extension enabled and drop the extension in each of them.
  4. If the extension required that database flags be set on the instances where it was used, remove the flags from each of the instances where it was used by following the instructions in [Configure an instance's database flags](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags).

The [list of supported extensions](https://docs.cloud.google.com/alloydb/docs/reference/extensions) shows which extensions require setting of database flags and identifies which flags.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
