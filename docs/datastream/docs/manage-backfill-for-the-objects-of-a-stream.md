---
url: https://docs.cloud.google.com/datastream/docs/manage-backfill-for-the-objects-of-a-stream/
title: Manage backfill for the objects of a stream \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:31.521772+00:00
---

# Manage backfill for the objects of a stream  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/manage-backfill-for-the-objects-of-a-stream/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Manage backfill for the objects of a stream Stay organized with collections  Save and categorize content based on your preferences. 

A stream in Datastream can backfill historical data, as well as stream ongoing changes into a destination. As part of creating a stream, you [configured information about the source database for the stream](https://docs.cloud.google.com/datastream/docs/create-a-stream#configuresourcedbinfo).

If you selected the **Backfill historical data** checkbox, then Datastream streams all existing data, in addition to changes to the data, from the source into the destination.

If you didn't select this checkbox, then Datastream streams only changes to the data. To have Datastream stream a snapshot of all existing data from the source to the destination, you must initiate backfill for the objects that contain this data. The objects are in the form of database schemas, tables, and columns.

Another reason for initiating backfill for an object is if data is out of sync between the source and the destination. For example, a user can delete data in the destination inadvertently, and the data is now lost. In this case, initiating backfill for the object serves as a reset mechanism because all data is streamed into the destination in one shot. As a result, the data is synced between the source and the destination.

After initiating backfill for an object, you can stop backfill for it. In the preceding example, the user modifies the database schema, and the schema or data is corrupted. You don't want this schema or data to be streamed into the destination, and so you stop backfill for the object.

You can also stop backfill for objects for load balancing purposes. Datastream can run multiple backfills in parallel. This may put an additional load on the source. If the load is significant, stop backfill for the objects, and then initiate backfill for them, one by one.

## Object statuses

The various statuses in the lifecycle of initiating and stopping backfill for an object include:

  * No status (represented in the UI as `-`): Reasons for an object receiving this status include:

    * The stream hasn't been started.
    * The **Backfill historical data** checkbox wasn't selected (so the backfill is defined as manual).
    * The object is excluded explicitly from being backfilled automatically.
    * The stream is configured to include future tables. If this happens, then when new tables are added to the source, there's no automatic backfill task created for them (because new tables typically don't have any historical data to backfill).
**Note:** For more information, see [Configure information about the source database for the stream](https://docs.cloud.google.com/datastream/docs/create-a-stream#configuresourcedbinfo).
  * `Pending`: backfill hasn't yet started for the object.

  * `Active`: backfill is in progress for the object.

  * `Completed`: backfill is completed for the object.

  * `Stopped`: backfill is stopped for the object. If backfill is initiated again for the object, then Datastream will stream all existing data associated with the object from the source into the destination.

  * `Failed`: backfill failed for the object and the backfill must be initiated again.




## Initiate backfill

  1. Go to the **Streams** page in the Google Cloud Console.

[Go to the Streams page](https://console.cloud.google.com/datastream/streams)

  2. Click the stream that contains objects for which you want to initiate backfill.

  3. Click the **Objects** tab.

  4. Select the checkbox for each object for which you want to initiate backfill.

  5. Click **Initiate backfill**.

If an object has a status of `Pending` or `Active`, then you can't initiate backfill for the object.

  6. If you selected only one object, then in the dialog, click **INITIATE OBJECT BACKFILL**. Otherwise, if you selected multiple objects, then click **INITIATE OBJECT BACKFILLS**.

Datastream will start backfill for the objects that you selected, and the status of each object will change from `Pending` to `Active` to `Completed`. When an object has a status of `Completed`, this means that Datastream has read all the data for the object, but the data might still be loading to the destination.

If an object has a status of `Failed`, then backfill failed for the object, and you must initiate the backfill again.



## Initiate partial backfill

In addition to full backfills, you can perform a partial backfill to load a specific subset of data from the source into the destination. To do this, you provide a SQL `WHERE` clause as a custom filter.

Datastream supports partial backfill for the following sources:

  * SQL Server
  * Spanner
  * Oracle
  * PostgreSQL
  * MySQL

Partial backfill for Oracle, PostgreSQL, and MySQL sources is made available gradually. In the Google Cloud console, partial backfill option only appears if your stream supports this feature. If you use Google Cloud CLI or Datastream API to configure partial backfill for a stream that doesn't support the feature yet, the request fails.

To initiate a partial backfill:

  1. Go to the **Streams** page in the Google Cloud Console.

[Go to the Streams page](https://console.cloud.google.com/datastream/streams)

  2. Click the stream that contains objects for which you want to initiate backfill.

  3. Click the **Objects** tab.

  4. Select the object for which you want to initiate backfill.

  5. Click **Initiate backfill**.

  6. In the panel that appears, select the **Enable custom filter** checkbox.

  7. Enter your SQL `WHERE` clause. For example, `product_id > 12 AND timestamp = '2025-01-06T22:00:00.00'`.

  8. Click **Initiate backfill**.




Datastream validates the filter. If the validation fails, an error message appears above the editor. If the validation succeeds, Datastream starts the backfill job.

### Supported custom filter syntax

When you provide a custom filter, Datastream supports a fundamental subset of SQL `WHERE` clause syntax. The supported elements include:

  * **Logical operators** : `AND`, `OR`
  * **Comparison operators** : `=`, `<`, `>`, `<=`, `>=`, `!=`
  * **Conditions** : `IN`, `NOT IN`, `IS NULL`, `IS NOT NULL`
  * **Grouping** : parentheses `()` for defining condition groups
  * **Values** :

    * Strings: text enclosed in single quotes, for example, `'value'`,
    * Numbers: integers (`123`), decimals (`123.45`), negative numbers (`-10`), and numbers with exponents (`1.2e3`).
    * Boolean values: `TRUE` or `FALSE` case-sensitive keywords.
**Note:** `DATE`, `TIME`, and `BYTE` and other complex type literals aren't directly supported. To filter based on a boolean column, you must compare it with the boolean literals using an operator (for example, `is_active = TRUE`).
  * **Identifiers** :

    * Qualification: column names can be fully qualified using dots to specify the schema or table, for example, `myColumn`, `myTable.myColumn`, or `mySchema.myTable.myColumn`.
    * Unquoted identifiers: they can contain letters, numbers, and underscores, and must start with a letter or underscore. Case sensitivity for column or table names depends on the target database.
    * Double-quoted identifiers: must be enclosed in double quotes (`"`).



### Partial backfill limitations

Certain statements, operators, and keywords are explicitly forbidden and using them results in an error. These include:

  * Comments, such as `--` or `/* */`.
  * Functions, for example, `UPPER(column)` and `NOW()`.
  * Arithmetic expressions, for example, `column + 1 > 10`.
  * The `LIKE` operator. Wildcards such as `%` or `_` aren't supported with `LIKE`.
  * The `BETWEEN` operator. Use `>=` and `<=` instead.
  * Subqueries, for example, `(SELECT ...)` within the `WHERE` clause.
  * `CASE` statements, for example, `CASE WHEN ... END`.
  * Column comparisons, such as `column1 = column2`. Comparisons must be against literals.
  * `DATE` and `TIME` specific types or functions.
  * Array or JSON specific operators.
  * Explicit casting: for example, `CAST(column AS INT)`.



## Stop backfill

  1. Go to the **Streams** page in the Google Cloud Console.

[Go to the Streams page](https://console.cloud.google.com/datastream/streams)

  2. Click the stream that contains objects for which you want to stop backfill.

  3. Click the **Objects** tab.

  4. Select the checkbox for each object for which you want to stop backfill.

  5. Click **Stop backfill**.

If an object has a status of `Completed`, `Stopped`, or `Failed`, then you can't stop backfill for the object.

  6. If you selected only one object, then in the dialog, click **Stop object backfill**. Otherwise, if you selected multiple objects, then click **Stop object backfills**.

Datastream will stop backfill for the objects that you selected, and the status of each object will change to `Stopped`.

When an object has this status, backfill is stopped for the object. If backfill is initiated again for the object, then Datastream will stream all existing data associated with the object from the source into the destination.




You can also use the **OBJECTS** tab to view additional information about the objects of a stream. This information includes: 

  * The status of the objects.
  * How many events Datastream processed and loaded into the destination for an object in the last 7 days.
  * The total size (in GB) of all events that Datastream processed and loaded into the destination for an object in the last 30 days.
  * Details about the table columns of the database schemas that are streamed from the source into the destination.



## What's next

  * To learn more about streams, see [Stream lifecycle](https://docs.cloud.google.com/datastream/docs/stream-states-and-actions).
  * To learn how to view information about your stream, see [View a stream](https://docs.cloud.google.com/datastream/docs/view-a-stream).
  * To learn how to modify a stream, see [Modify a stream](https://docs.cloud.google.com/datastream/docs/modify-a-stream).
  * To learn how to monitor a stream, see [Monitor a stream](https://docs.cloud.google.com/datastream/docs/monitor-a-stream).
  * To learn how to recover a failed stream, see [Recover a stream](https://docs.cloud.google.com/datastream/docs/recover-a-stream).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
