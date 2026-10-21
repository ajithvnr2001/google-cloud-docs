---
url: https://docs.cloud.google.com/bigtable/docs/googlesql-overview/
title: GoogleSQL for Bigtable overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:29:16.666547+00:00
---

# GoogleSQL for Bigtable overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/googlesql-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# GoogleSQL for Bigtable overview

You can use GoogleSQL statements to query your Bigtable data. GoogleSQL is an ANSI-compliant structured query language (SQL) that is also implemented for other Google Cloud services such as BigQuery and Spanner.

This document provides an overview of GoogleSQL for Bigtable. It provides examples of SQL queries that you can use with Bigtable and describes how they relate to a Bigtable table schema. Before you read this document, you should be familiar with the [Bigtable storage model](https://docs.cloud.google.com/bigtable/docs/overview#storage-model) and [schema design concepts](https://docs.cloud.google.com/bigtable/docs/schema-design#general-concepts).

You can create and run queries in [Bigtable Studio](https://docs.cloud.google.com/bigtable/docs/manage-data-using-console) in the Google Cloud console, or you can run them programmatically using the [Bigtable client library for Java](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/overview), [Python](https://docs.cloud.google.com/python/docs/reference/bigtable/latest), or [Go](https://pkg.go.dev/cloud.google.com/go/bigtable). For more information, see Use SQL with a Bigtable client library.

SQL queries are handled by cluster nodes in the same way as NoSQL data requests. Therefore, the same best practices apply when creating SQL queries to run against your Bigtable data, such as avoiding full table scans or complex filters. For more information, see [Reads and performance](https://docs.cloud.google.com/bigtable/docs/reads#performance).

## Use cases

GoogleSQL for Bigtable is optimal for low-latency application development. Additionally, running SQL queries in the Google Cloud console can be useful for quickly getting a visual representation of a table's schema, verifying that certain data was written, or debugging possible data issues.

The current release of GoogleSQL for Bigtable doesn't support some common SQL constructs, including, but not limited to, the following:

  * Data Manipulation Language (DML) statements beyond `SELECT`, such as `INSERT`, `UPDATE`, or `DELETE`
  * Data Definition Language (DDL) statements such as `CREATE`, `ALTER`, or `DROP`
  * Data Access Control statements
  * Query syntax for subqueries, `JOIN`, `UNION`, and `CTEs`



For more information, including supported functions, operators, data types, and query syntax, see the [GoogleSQL for Bigtable reference documentation](https://docs.cloud.google.com/bigtable/docs/reference/sql/googlesql-reference-overview).

## Views

You can use GoogleSQL for Bigtable to create the following resources:

  * [Continuous materialized view](https://docs.cloud.google.com/bigtable/docs/continuous-materialized-views) \- a pre-computed result of a continuously running SQL query, including aggregated data, that synchronizes with its source table with incremental updates.
  * [Logical view](https://docs.cloud.google.com/bigtable/docs/create-manage-logical-views) \- a saved, named query that can be queried like a table.



To compare these types of views as well as authorized views, see [Tables and views](https://docs.cloud.google.com/bigtable/docs/tables-and-views).

## Key concepts

This section discusses key concepts to be aware of when you use GoogleSQL to query your Bigtable data.

### Column families in SQL responses

In Bigtable, a table contains one or more column families, which are used to group columns. When you query a Bigtable table with GoogleSQL, the schema for the table consists of the following:

  * A special column named `_key` that corresponds to row keys in the queried table
  * A single column for each Bigtable column family in the table, which contains the column family's data in that row



### Map data type

GoogleSQL for Bigtable includes the data type [`MAP<key, value>`](https://docs.cloud.google.com/bigtable/docs/reference/sql/data-types#map_type), which is designed specifically to accommodate column families.

By default, each row in a map column contains key-value pairs, where a key is the Bigtable column qualifier in the queried table, and the value is the most recent value for that column.

The following is an example of a SQL query returns a table with the row key value and the latest value of the qualifier from a map named `columnFamily`.
    
    
      SELECT _key, columnFamily['qualifier'] FROM myTable
    

If your Bigtable schema involves storing multiple cells – or versions of the data – in columns, you can add a temporal filter, such as `with_history`, to your SQL statement.

In this case, maps representing column families are nested and returned as an array. In the array, each value is itself a map consisting of a timestamp as the key and cell data as the value. The format is `MAP<key, ARRAY<STRUCT<timestamp, value>>>`.

The following example returns all cells in the 'info' column family for a single row.
    
    
      SELECT _key, info FROM users(with_history => TRUE) WHERE _key = 'user_123';
    

The returned map looks like the following. In the queried table, `info` is the column family, `user_123` is the row key and `city` and `state` are the column qualifiers. Each timestamp-value pair (`STRUCT`) in an array represents cells in those columns in that row, and they are sorted by timestamp descending.
    
    
    /*----------+------------------------------------------------------------------------------------------------------------------------------------*
     |   _key   |                                                                info                                                                |
     +----------+------------------------------------------------------------------------------------------------------------------------------------+
     | user_123 | {"city": [{<t5> timestamp, "Brooklyn" value}, {<t0> timestamp, "New York" value}], "state": [{<t0> timestamp, "NY" value}]}        |
     +----------+------------------------------------------------------------------------------------------------------------------------------------*/
    

### Sparse tables

A key feature of Bigtable is its flexible data model. In a Bigtable table, if a column is unused in a row, no data is stored for the column. A row might have one column and the next row might have 100 columns. In contrast, in a relational database table, all rows contain all columns, and a `NULL` value is typically stored in the column of a row that has no data for that column.

When you query a Bigtable table with GoogleSQL, however, an unused column is represented with an empty map and is returned as a `NULL` value. These `NULL` values can be used as query predicates. For example, a predicate like `WHERE family['column1'] IS NOT NULL` can be used to return a row only if `column1` is used in the row.

### Bytes

When you provide a string, GoogleSQL by default implicitly casts from `STRING` values to `BYTES` values. This means, for example, that you can provide the string `'qualifier'` rather than the bytes sequence `b'qualifier'`.

Because Bigtable by default treats all data as bytes, most Bigtable columns don't contain type information. However, with GoogleSQL you can define a schema at read time with the `CAST` function. For more information about casting, see [Conversion functions](https://docs.cloud.google.com/bigtable/docs/reference/sql/conversion_functions#conversion_functions).

### Temporal filters

The following table lists the arguments that you can use when accessing temporal elements of a table. Arguments are listed in the order in which they are filtered. For example, `with_history` is applied before `latest_n`. You must provide a valid timestamp.

**Argument** | **Description**  
---|---  
`as_of` | _Timestamp_. Returns the latest values with timestamps less than or equal to the provided timestamp.  
`with_history` | _Boolean_. Controls whether to return the latest value as a scalar or timestamped values(s) as `STRUCT`.  
`after` | _Timestamp_. Values with timestamps after the input, exclusive. Requires `with_history => TRUE`.  
`after_or_equal` | _Timestamp_. Values with timestamps after the input, inclusive. Requires `with_history => TRUE`.  
`before` | _Timestamp_. Values with timestamps before the input, exclusive. Requires `with_history => TRUE`.  
`latest_n` | _Integer_. The number of timestamped values to return per column qualifier (map key). Must be greater than or equal to 1. Requires `with_history => TRUE`.  
  
For more examples, see [Advanced query patterns](https://docs.cloud.google.com/bigtable/docs/googlesql-examples).

## Foundational queries

This section describes and shows examples of basic Bigtable SQL queries and how they work. For additional sample queries, see [GoogleSQL for Bigtable query pattern examples](https://docs.cloud.google.com/bigtable/docs/googlesql-examples).

### Retrieve the latest version

Although Bigtable lets you store multiple versions of data in each column, GoogleSQL for Bigtable by default returns the latest version – the most recent cell – of the data for each row.

Consider the following sample dataset, which shows that `user1` relocated twice in the state of NY and once within the city of Brooklyn. In this example, `address` is the column family, and the column qualifiers are `street`, `city`, and `state`. Cells in a column are separated by empty lines.

|  | **address** |   
---|---|---|---  
**_key** | **street** | **city** | **state**  
user1 | 2023/01/10-14:10:01.000:  
'113 Xyz Street'  
  
2021/12/20-09:44:31.010:  
'76 Xyz Street'  
  
2005/03/01-11:12:15.112:  
'123 Abc Street' | 2021/12/20-09:44:31.010:  
'Brooklyn'  
  
2005/03/01-11:12:15.112:  
'Queens' | 2005/03/01-11:12:15.112:  
'NY'  
  
To retrieve the **latest** version of each column for `user1`, you can use a `SELECT` statement like the following.
    
    
       SELECT address['street'], address['city'] FROM myTable WHERE _key = 'user1'
    

The response contains the current address, which is a combination of the most recent street, city and state values (written at different times) printed as JSON. Timestamps are not included in the response.

**_key** | **address**  
---|---  
user1 | {street:'113 Xyz Street', city:'Brooklyn', state: :'NY'}  
  
### Retrieve all versions

To retrieve earlier versions (cells) of the data, use the `with_history` flag. You can also alias columns and expressions, as illustrated in the following example.
    
    
      SELECT _key, columnFamily['qualifier'] AS col1
      FROM myTable(with_history => TRUE)
    

To better understand the events leading to the current state of a row, you can retrieve the timestamps for each value by retrieving the full history. For example, to understand when `user1` moved to their current address and where they moved from, you could run the following query:
    
    
      SELECT
        address['street'][0].value AS moved_to,
        address['street'][1].value AS moved_from,
        FORMAT_TIMESTAMP('%Y-%m-%d', address['street'][0].timestamp) AS moved_on,
      FROM myTable(with_history => TRUE)
      WHERE _key = 'user1'
    

When you use the `with_history` flag in your SQL query, the response is returned as `MAP<key, ARRAY<STRUCT<timestamp, value>>>`. Each item in the array is a timestamped value for the specified row, column family, and column. Timestamps are ordered in reverse chronological order, so the latest data is always the first item returned.

**Note:** Garbage collection policies control the expiration time or number of versions retained for a column family. For more information, see the [Garbage collection overview](https://docs.cloud.google.com/bigtable/docs/garbage-collection).

The query response is as follows.

**moved_to** | **moved_from** | **moved_on**  
---|---|---  
113 Xyz Street | 76 Xyz Street | 2023/01/10  
  
You can also retrieve the number of versions in each row using array functions as demonstrated in the following query:
    
    
      SELECT _key, ARRAY_LENGTH(MAP_ENTRIES(address)) AS version_count
      FROM myTable(with_history => TRUE)
    

### Retrieve data from a specified time

Using an `as_of` filter lets you retrieve the state of a row as it was at a certain point in time. For example, if you want to know the address of `user` as of January 10, 2022 1:14 PM, you can run the following query.
    
    
      SELECT address
      FROM myTable(as_of => TIMESTAMP('2022-01-10T13:14:00.234Z'))
      WHERE _key = 'user1'
    

The result shows what would have been the last known address on January 10, 2022 1:14 PM, which is the combination of street and city from the 2021/12/20-09:44:31.010 update and the state from 2005/03/01-11:12:15.112.

**address**  
---  
{street:'76 Xyz Street', city:'Brooklyn', state: :'NY'}  
  
The same result can also be achieved using Unix timestamps.
    
    
      SELECT address
      FROM myTable(as_of => TIMESTAMP_FROM_UNIX_MILLIS(1641820440000))
      WHERE _key = 'user1'
    

Consider the following dataset, which shows the on-or-off state of smoke and carbon monoxide alarms. The column family is `alarmType` and the column qualifiers are `smoke` and `carbonMonoxide`. Cells in each column are separated by empty lines.

|   
**alarmType**  
---|---  
**_key** | **smoke** | **carbonMonoxide**  
building1#section1 | 2023/04/01-09:10:15.000:  
'off'  
  
2023/04/01-08:41:40.000:  
'on'  
  
2020/07/03-06:25:31.000:  
'off'  
  
2020/07/03-06:02:04.000:  
'on' | 2023/04/01-09:22:08.000:  
'off'  
  
2023/04/01-08:53:12.000:  
'on'  
building1#section2 | 2021/03/11-07:15:04.000:  
'off'  
  
2021/03/11-07:00:25.000:  
'on' |   
  
You can find sections of `building1` where a smoke alarm was on at 9 AM on April 1, 2023 and the status of the carbon monoxide alarm at the time using the following query.
    
    
      SELECT _key AS location, alarmType['carbonMonoxide'] AS CO_sensor
      FROM alarms(as_of => TIMESTAMP('2023-04-01T09:00:00.000Z'))
      WHERE _key LIKE 'building1%' and alarmType['smoke'] = 'on'
    

The result is the following:

**location** | **CO_sensor**  
---|---  
building1#section1 | 'on'  
  
### Query time series data

A common use case for Bigtable is the storage of [time series data](https://docs.cloud.google.com/bigtable/docs/schema-design-time-series). Consider the following sample dataset, which shows temperature and humidity readings for weather sensors. The column family ID is `metrics` and the column qualifiers are `temperature` and `humidity`. Cells in a column are separated by empty lines, and each cell represents a timestamped sensor reading.

|   
**metrics**  
---|---  
**_key** | **temperature** | **humidity**  
sensorA#20230105 | 2023/01/05-02:00:00.000:  
54  
  
2023/01/05-01:00:00.000:  
56  
  
2023/01/05-00:00:00.000:  
55 | 2023/01/05-02:00:00.000:  
0.89  
  
2023/01/05-01:00:00.000:  
0.9  
  
2023/01/05-00:00:00.000:  
0.91  
sensorA#20230104 | 2023/01/04-23:00:00.000:  
56  
  
2023/01/04-22:00:00.000:  
57 | 2023/01/04-23:00:00.000:  
0.9  
  
2023/01/04-22:00:00.000:  
0.91  
  
You can retrieve a specific range of timestamp values using the temporal filters `after`, `before`, or `after_or_equal`. The following example uses `after`:
    
    
       SELECT metrics['temperature'] AS temp_versioned
       FROM
       sensorReadings(with_history => true, after => TIMESTAMP('2023-01-04T23:00:00.000Z'),
             before => TIMESTAMP('2023-01-05T01:00:00.000Z'))
       WHERE _key LIKE 'sensorA%'
    

The query returns the data in this format:

**temp_versioned**  
---  
[{timestamp: '2023/01/05-01:00:00.000', value:56}  
{timestamp: '2023/01/05-00:00:00.000', value: 55}]  
[{timestamp: '2023/01/04-23:00:00.000', value:56}]  
  
### `UNPACK` time series data

When you're analyzing time series data, it's often preferable to work with the data in a tabular format. The Bigtable `UNPACK` function can help.

`UNPACK` is a Bigtable table value function (TVF) that returns an entire output table instead of a single scalar value, and appears in the `FROM` clause like a table subquery. The `UNPACK` TVF expands each timestamped value into multiple rows – one per timestamp – and moves the timestamp into the `_timestamp` column.

The input to `UNPACK` is a subquery where `with_history => true`.

The output is an expanded table with a `_timestamp` column in each row.

An input column family `MAP<key, ARRAY<STRUCT<timestamp, value>>>`unpacks to `MAP<key, value>`, and a column qualifier `ARRAY<STRUCT<timestamp, value>>>` unpacks to `value`. Other input column types are unchanged. The columns must be selected in the subquery in order to be unpacked and selected. The new `_timestamp` column doesn't need to be selected in order for the timestamps to be unpacked.

Expanding on the time series example in [Query time series data](https://docs.cloud.google.com/bigtable/docs/googlesql-overview#time-series), and using the query in that section as the input, your `UNPACK` query is formatted like this:
    
    
      SELECT temp_versioned, _timestamp
      FROM
      UNPACK((
        SELECT metrics['temperature'] AS temperature_versioned
        FROM
        sensorReadings(with_history => true, after => TIMESTAMP('2023-01-04T23:00:00.000Z'),
              before => TIMESTAMP('2023-01-05T01:00:00.000Z'))
        WHERE _key LIKE 'sensorA%'
      ));
    

The query returns the data in this format:

temp_versioned | _timestamp  
---|---  
55 | 1672898400  
55 | 1672894800  
56 | 1672891200  
  
### Query JSON

JSON functions let you manipulate JSON stored as Bigtable values for operational workloads.

For example, you can retrieve the value for the JSON element `abc` from the latest cell in the `session` column family along with the row key by using the following query.
    
    
      SELECT _key, JSON_VALUE(session['payload'],'$.abc') AS abc FROM analytics
    

## Escape special characters and reserved words

Bigtable offers high flexibility in naming tables and columns. As a result, in your SQL queries, your table names might need to be escaped due to special characters or reserved words.

For example, the following query isn't valid SQL due to the period in the table name.
    
    
      -- ERROR: Table name format not supported
    
      SELECT * FROM my.table WHERE _key = 'r1'
    

However, you can resolve this issue by enclosing the items with backtick (`) characters.
    
    
      SELECT * FROM `my.table` WHERE _key = 'r1'
    

If a SQL reserved keyword is used as an identifier, it can similarly be escaped.
    
    
      SELECT * FROM `select` WHERE _key = 'r1'
    

## Use SQL with a Bigtable client library

The Bigtable client libraries for Java, Python, and Go support querying data with SQL using the `executeQuery` API. The following examples show how to issue a query and access the data:

### Go

To use this feature you must use `cloud.google.com/go/bigtable` version 1.36.0 or later. For more information on usage see [PrepareStatement](https://pkg.go.dev/cloud.google.com/go/bigtable#Client.PrepareStatement), [Bind](https://pkg.go.dev/cloud.google.com/go/bigtable#PreparedStatement.Bind), [Execute](https://pkg.go.dev/cloud.google.com/go/bigtable#BoundStatement.Execute), and [ResultRow](https://pkg.go.dev/cloud.google.com/go/bigtable#ResultRow) documentation.
    
    
      import (
        "cloud.google.com/go/bigtable"
      )
    
      func query(client *bigtable.[Client](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Client)) {
        // Prepare once for queries that will be run multiple times, and reuse
        // the PreparedStatement for each request. Use query parameters to
        // construct PreparedStatements that can be reused.
        ps, err := client.[PrepareStatement](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Client_PrepareStatement)(
          "SELECT cf1['bytesCol'] AS bytesCol, CAST(cf2['stringCol'] AS STRING) AS stringCol, cf3 FROM myTable WHERE _key=@keyParam",
          map[string][SQLType](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_SQLType){
            "keyParam": [BytesSQLType](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_BytesSQLType){},
          }
        )
        if err != nil {
          log.Fatalf("Failed to create PreparedStatement: %v", err)
        }
    
        // For each request, create a BoundStatement with your query parameters set.
        bs, err := ps.[Bind](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_PreparedStatement_Bind)(map[string]any{
          "keyParam": []byte("mykey")
        })
        if err != nil {
          log.Fatalf("Failed to bind parameters: %v", err)
        }
    
        err = bs.[Execute](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_BoundStatement_Execute)(ctx, func(rr [ResultRow](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_ResultRow)) bool {
          var byteValue []byte
          err := rr.GetByName("bytesCol", &byteValue)
          if err != nil {
            log.Fatalf("Failed to access bytesCol: %v", err)
          }
          var stringValue string
          err = rr.GetByName("stringCol", &stringValue)
          if err != nil {
            log.Fatalf("Failed to access stringCol: %v", err)
          }
          // Note that column family maps have byte valued keys. Go maps don't support
          // byte[] keys, so the map will have Base64 encoded string keys.
          var cf3 map[string][]byte
          err = rr.GetByName("cf3", &cf3)
          if err != nil {
            log.Fatalf("Failed to access cf3: %v", err)
          }
          // Do something with the data
          // ...
          return true
        })
      }
    

### Java

To use this feature you must use `java-bigtable` version 2.57.3 or later. For more information on usage, see [prepareStatement](https://javadoc.io/doc/com.google.cloud/google-cloud-bigtable/latest/com/google/cloud/bigtable/data/v2/BigtableDataClient.html#prepareStatement\(java.lang.String,java.util.Map\)), [executeQuery](https://javadoc.io/doc/com.google.cloud/google-cloud-bigtable/latest/com/google/cloud/bigtable/data/v2/BigtableDataClient.html#executeQuery\(com.google.cloud.bigtable.data.v2.models.sql.BoundStatement\)), [BoundStatement](https://javadoc.io/doc/com.google.cloud/google-cloud-bigtable/latest/com/google/cloud/bigtable/data/v2/models/sql/BoundStatement.html), and [ResultSet](https://javadoc.io/doc/com.google.cloud/google-cloud-bigtable/latest/com/google/cloud/bigtable/data/v2/models/sql/ResultSet.html) in the Javadoc.
    
    
      static void query(BigtableDataClient client) {
        // Prepare once for queries that will be run multiple times, and reuse
        // the PreparedStatement for each request. Use query parameters to
        // construct PreparedStatements that can be reused.
        PreparedStatement preparedStatement = client.prepareStatement(
          "SELECT cf1['bytesCol'] AS bytesCol, CAST(cf2['stringCol'] AS STRING) AS stringCol, cf3 FROM myTable WHERE _key=@keyParam",
          // For queries with parameters, set the parameter names and types here.
          Map.of("keyParam", SqlType.bytes())
        );
    
        // For each request, create a BoundStatement with your query parameters set.
        BoundStatement boundStatement = preparedStatement.bind()
          .setBytesParam("keyParam", ByteString.copyFromUtf8("mykey"))
          .build();
    
        try (ResultSet resultSet = client.executeQuery(boundStatement)) {
          while (resultSet.next()) {
            ByteString byteValue = resultSet.getBytes("bytesCol");
            String stringValue = resultSet.getString("stringCol");
            Map<ByteString, ByteString> cf3Value =
                resultSet.getMap("cf3", SqlType.mapOf(SqlType.bytes(), SqlType.bytes()));
            // Do something with the data.
          }
        }
      }
    

### Python asyncio

To use this feature, you must use `python-bigtable` version 2.30.1 or later.
    
    
      from google.cloud.bigtable.data import BigtableDataClientAsync
    
      async def execute_query(project_id, instance_id, table_id):
          async with BigtableDataClientAsync(project=project_id) as client:
              query = (
                "SELECT cf1['bytesCol'] AS bytesCol, CAST(cf2['stringCol'] AS STRING) AS stringCol,"
                " cf3 FROM {table_id} WHERE _key='mykey'"
              )
              async for row in await client.execute_query(query, instance_id):
                print(row["_key"], row["bytesCol"], row["stringCol"], row["cf3"])
    

## `SELECT *` usage

`SELECT *` queries can experience temporary errors when a column family is added or deleted from the queried table. For this reason, for production workloads, we recommend that you specify all column family IDs in your query, rather than using `SELECT *`. For example, use `SELECT cf1, cf2, cf3` instead of `SELECT *`.

In addition, the queries that define [logical views](https://docs.cloud.google.com/bigtable/docs/create-manage-logical-views) and [continuous materialized views](https://docs.cloud.google.com/bigtable/docs/continuous-materialized-views) can't use `SELECT *`.

## What's next

  * [Explore the GoogleSQL for Bigtable reference documentation.](https://docs.cloud.google.com/bigtable/docs/reference/sql/googlesql-reference-overview)
  * [Learn more about Bigtable Studio.](https://docs.cloud.google.com/bigtable/docs/manage-data-using-console)
  * [Learn how to develop applications with GoogleSQL for Bigtable.](https://docs.cloud.google.com/bigtable/docs/googlesql-develop-apps)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
