---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/configure-database-batch-source/
title: Database batch source \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:19.155719+00:00
---

# Database batch source  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/configure-database-batch-source/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Database batch source Stay organized with collections  Save and categorize content based on your preferences. 

This page provides guidance about configuring the Database batch source plugin in Cloud Data Fusion. 

You can use this generic source whenever you need to read from a database. For example, you might use it to create daily snapshots of a generic database table and write the output to BigQuery.

## Configure the plugin

  1. [Go to the Cloud Data Fusion web interface](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline#navigate-web-interface) and click **Studio**.
  2. Check that **Data Pipeline - Batch** is selected (not **Realtime**).
  3. In the **Source** menu, click **Database**.
  4. To configure the plugin, hold the pointer over the plugin node and click **Properties**.
  5. Enter the following properties. For more information about each property, see Properties.

     1. Enter a **Label** for the database node—for example, `database tables`.
     2. Enter the connection details. You can set up a new, one-time connection, or an existing, reusable connection.

### New connection

To add a one-time connection to the database, follow these steps:

        1. Keep **Use connection** turned off.
        2. Enter the following connection properties: 
           1. In the JDBC driver name field, enter the name of the driver, if there is one. Otherwise, keep **No JDBC plugins** selected.
           2. In the **Connection string** field, enter the JDBC connection string, including the database name.
           3. Optional: if your database requires authentication, enter database username and password credentials.
           4. Optional: if your JDBC driver needs additional configurations, in the **Connection arguments** field, enter key-value arguments for the connection.

### Reusable connection

To reuse an existing connection, follow these steps:

        1. Turn on **Use connection**.
        2. Click **Browse connections**.
        3. Select the connection.

**Note:** For more information about adding, importing, and editing the connections that appear when you browse connections, see [Create and manage connections](https://docs.cloud.google.com/data-fusion/docs/how-to/managing-connections).
        4. Optional: if a connection doesn't exist and you want to create a new, reusable connection, click **Add connection** and refer to the steps in the **New connection** tab on this page.

     3. Optional: to test connectivity, click **Get schema**. This schema is used in place of whatever schema comes back from the query. It must match the schema that comes back from the query, except that you can mark fields as nullable and it can contain a subset of the fields.

     4. In the **Import query** field, enter a `SELECT` query for importing data from the specified table—for example, `select id, name, email, phone from users;`.

     5. Optional: in the **Bounding query** field, enter the minimum and maximum values to read—for example, `SELECT * FROM table WHERE $CONDITIONS`.

     6. Optional: in the **Split-by field name** field, enter the name of the field that generates the splits.

     7. Optional: in the **Number of splits to generate** field, enter a number—for example, `2`.

     8. Optional: in the **Fetch size** field, enter a number—for example, `1000`.

     9. Optional: enter **Advanced properties** , such as changing the case of the column names.

  6. Optional: click **Validate** and address any errors found.

  7. Click **Close**. Properties are saved and you can continue to build your data pipeline in the Cloud Data Fusion Studio.




### Properties

Property | Macro enabled | Required | Description  
---|---|---|---  
**Label** | No | Yes | The name of the node in your data pipeline.  
**Use connection** | No | No | Browse for a connection to the source. If **Use connection** is selected, you don't need to provide credentials.  
**Connection** | Yes | Yes | Name of the connection to use. If **Use connection** is selected, this field appears. Database and table information is provided by the connection.  
**JDBC driver name** | Yes |  Yes | The JDBC driver to use.  
Default is **No JDBC plugins**.  
**Connection string** | Yes |  Yes | JDBC connection string, including database name.  
**Username** | Yes |  No | User identity for connecting to the database. Required for databases that need authentication. Optional for databases that don't require authentication.  
**Password** | Yes |  No | Password to use to connect to the specified database. Required for databases that need authentication. Optional for databases that don't require authentication.  
**Connection arguments** | Yes |  No | A list of arbitrary string tag/value pairs as connection arguments. For JDBC drivers that need additional configuration, these arguments are passed to the JDBC driver as connection arguments in the following format: `key1=value1;key2=value`.  
**Reference name** | No |  Yes | A name that uniquely identifies this source for lineage and annotating metadata. It's usually the name of the table or the view.  
**Get schema** | No | No | The schema of records output by the source. It's used in place of the schema that's returned by the query. It must match the schema that comes back from the query, except that it lets you mark fields as nullable and it can contain a subset of the fields.  
**Import query** | Yes | Yes | The `SELECT` query for importing data from the specified table. You can specify an arbitrary number of columns to import, or import all columns using `*`. The query should contain the `$CONDITIONS` string. For example, `SELECT * FROM table WHERE $CONDITIONS`. The `$CONDITIONS` string is replaced by `splitBy` field limit specified in the **Bounding query** field. The `$CONDITIONS` string isn't required if the **Number of splits** field is set to 1.  
**Bounding query** | Yes |  No | The bounding query that returns the minimum and maximum of the values from the split column. For example, `SELECT MIN(id),MAX(id) FROM table`. Not required if the number of splits is set to 1.  
**Split-by field name** | Yes |  No | The field name used to generate splits. Not required if the number of splits to generate is set to 1.  
**Number of splits to generate** | Yes |  No | Number of splits to generate.  
Default is **1**.  
**Fetch size** | Yes |  No | The number of rows to fetch at a time per split. A greater fetch size can cause faster import, with the trade-off of higher memory usage.  
Default is **1000**.  
**Enable auto-commit** | No |  No | Whether to enable auto-commit for queries run by this source. Keep this set to **False** unless you use a JDBC driver that causes an error when the commit operation is run.  
Default is **False**.  
**Column name case** | Yes |  No | Sets the letter case of the column names returned from the query. You can choose uppercase or lowercase. By default, or for any other input, the column names aren't modified and letter case returned from the database is used. Setting this property provides predictability of column name capitalization across different databases, but it might cause column name conflicts if multiple column names are the same when the case is ignored.  
Default is **No change**.  
**Transaction isolation level** | Yes |  No | The transaction isolation level for queries run by this sink. For more information, see the [`setTransactionIsolation()`](https://docs.oracle.com/javadb/10.8.3.0/ref/rrefjavcsti.html). The Phoenix JDBC driver throws an exception if the Phoenix database doesn't have transactions enabled and this field is set to `true`. For drivers like that, set this field to `TRANSACTION_NONE`.  
Default is **TRANSACTION_SERIALIZABLE**.  
**Pattern to replace** | No |  No | The pattern to replace in the field name in the table (typically used with the **Replace with** property). If the **Replace with** property isn't set, the pattern is removed from the field name.  
**Replace with** | No |  No | The string that's replaced in the field name in the table. You must also configure the **Pattern to replace** field.  
**Output schema** | No | No | Specifies the schema that's output. Only columns defined in the schema are included in the output record.  
  
## Best practices

Check if a more specific plugin is available for your database. For example, if you have an Oracle database source, instead use the Oracle database batch source plugin because it's designed to work with the Oracle schema.

## Release notes

  * [June 14, 2023](https://docs.cloud.google.com/data-fusion/docs/release-notes#June_14_2023)
  * [February 28, 2023](https://docs.cloud.google.com/data-fusion/docs/release-notes#February_28_2023)
  * [January 12, 2023](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1280901131/CDAP+Hub+Release+Log#January-12%2C-2023)



## What's next

  * Learn more about [plugins in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/plugins).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
