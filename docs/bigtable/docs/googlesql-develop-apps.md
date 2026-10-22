---
url: https://docs.cloud.google.com/bigtable/docs/googlesql-develop-apps/
title: Develop applications with GoogleSQL for Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:33:48.431174+00:00
---

# Develop applications with GoogleSQL for Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/googlesql-develop-apps/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Develop applications with GoogleSQL for Bigtable

You can use GoogleSQL for Bigtable to run queries from your applications to offload compute functions to Bigtable. This reduces the need for client-side processing. GoogleSQL is an ANSI-compliant structured query language implemented for Bigtable and other Google Cloud services. For more information about other uses of GoogleSQL for Bigtable, see [ GoogleSQL for Bigtable overview](https://docs.cloud.google.com/bigtable/docs/googlesql-overview).

## Before you begin

Ensure that you have the following:

  * A Bigtable instance and table.
  * The Bigtable client library for your language. For more information about how to install and use client libraries for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries).
  * Authentication set up through Application Default Credentials (ADC). For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).



## Example scenario

The examples in this guide use a sample `weather-data` table that you can access from your [free trial](https://docs.cloud.google.com/bigtable/docs/free-trial-instance) instance in the Google Cloud console. Suppose your table stores information from different weather stations that are identified by a `station_id`. Each station records the temperature in the Fahrenheit scale in a column named `temp_f`. Instead of calculating the temperature in your application, you can use a SQL query to convert these temperatures to the Celsius scale directly in Bigtable before sending the results back to your application. For more information about querying the weather data table, see [Query sample data](https://docs.cloud.google.com/bigtable/docs/create-free-trial-instance#query).

## Best practices

To optimize performance and resource usage, consider the following best practices when you develop applications:

  * **Reuse the client:** create a single `BigtableDataClient` for your application. The client handles gRPC channel management and is designed for high concurrency. We recommend that you create this client once after your application starts, and then reuse it for every query.
  * **Use parameterized queries:** use `PreparedStatement` to separate query logic from data values. This lets Bigtable cache the execution plan and prevents SQL injection.
  * **Reuse prepared statements:** only call `PreparedStatement` once per SQL string. Store and reuse the statement across multiple requests.



## Create the Bigtable client

To handle the connection between your application and Bigtable, create a `BigtableDataClient`. The following sample shows how to share a single client instance across your application to manage connections efficiently:
    
    
    BigtableDataSettings settings = BigtableDataSettings.newBuilder()
        .setProject(PROJECT_ID)
        .setInstance(INSTANCE_ID)
        .build();
    
    // The client is thread-safe and should be reused.
    try (BigtableDataClient dataClient = BigtableDataClient.create(settings)) {
        System.out.println("Connected to: " + INSTANCE_ID);
    }
    

## Prepare the query

Instead of putting your data directly into a SQL string, we recommend that you use _parameterized queries_. In GoogleSQL for Bigtable, parameterized queries are the equivalent of a [prepared statement](https://en.wikipedia.org/wiki/Prepared_statement). This lets you separate the query logic from the data values.

The following sample shows how to define your GoogleSQL query using parameter placeholders, such as `@sid`. Then create a `PreparedStatement` by specifying the SQL string and the types for each parameter so that the query can run faster next time:
    
    
    Map<String, SqlType<?>> paramTypes = new HashMap<>();
    paramTypes.put("sid", SqlType.string());
    
    String sql = "SELECT " +
                 "ROUND((CAST(CAST(weather['temp_f'] AS STRING) AS INT64) - 32) * 5 / 9, 2) AS temp_celsius " +
                 "FROM " + TABLE_NAME + " WHERE station_id = @sid LIMIT 1";
    
    // Create and reuse the PreparedStatement.
    PreparedStatement preparedStatement = dataClient.prepareStatement(sql, paramTypes);
    

## Run the query

Provide parameter values and run the query. The following sample shows how to use the `PreparedStatement` to bind values to your parameters to create a `BoundStatement`. Then it runs the query and loops through the results to print the `ResultSet`, which is the temperature in degrees Celsius:
    
    
    BoundStatement boundStatement = preparedStatement.bind()
        .setStringParam("sid", stationId)
        .build();
    
    try (ResultSet resultSet = dataClient.executeQuery(boundStatement)) {
        while (resultSet.next()) {
            System.out.println("Temp: " + resultSet.getDouble("temp_celsius"));
        }
    }
    

## Check the data structure

When you develop or explore SQL, we recommend that you explore the metadata associated with the table to understand the data structure. Because Bigtable has a flexible schema, if you use `SELECT *` queries, your query results can change based on the data. Therefore we recommend that you don't use `SELECT *` queries in production applications.

The following sample looks at the metadata of the result set (such as the column names and types) and then sends them back to the client independently of the data. This lets you obtain the column information first and then create the data structure that you need to process the data in the application.
    
    
    ResultSetMetadata metadata = resultSet.getMetadata();
    System.out.print("Columns: ");
    metadata.getColumnsList().forEach(col -> System.out.print(col.getName() + " "));
    System.out.println();
    

## Work with column families

Bigtable stores data in column families. GoogleSQL returns these families as lists of names and values that are known as [maps](https://docs.cloud.google.com/bigtable/docs/reference/sql/data-types#map_type) of column qualifiers and values. When reading a column family, Bigtable returns the `SqlType.Map` type. When reading a column family from a table with history, such as `SELECT column FROM my_table(with_history=>true)`, Bigtable returns a [`SqlType.historicalMap()`](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.sql.SqlType#com_google_cloud_bigtable_data_v2_models_sql_SqlType_historicalMap__) type, which is a map of column qualifiers and an array of cell timestamps and values. For more examples of `SqlType` types, see [`SqlType`](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.sql.SqlType).

The following sample shows how, instead of getting one column at a time, you can get an entire group of columns at once. The code stores the column family in a map so that you can loop through all the names and values:
    
    
    Map<String, SqlType<?>> paramTypes = new HashMap<>();
    paramTypes.put("keyPrefix", SqlType.bytes());
    String sql = String.format("SELECT weather FROM %s WHERE STARTS_WITH(_key, @keyPrefix)", TABLE_NAME);
    PreparedStatement preparedStatement = dataClient.prepareStatement(sql, paramTypes);
    BoundStatement boundStatement = preparedStatement.bind()
       .setBytesParam("keyPrefix", ByteString.copyFromUtf8(key))
       .build();
    
    
    try (ResultSet resultSet = dataClient.executeQuery(boundStatement)) {
       while (resultSet.next()) {
         SqlType.Map<ByteString, ByteString> mapType = SqlType.mapOf(SqlType.bytes(), SqlType.bytes());
         Map<ByteString, ByteString> weatherValues = resultSet.getMap("weather", mapType);
         for (Map.Entry<ByteString, ByteString> entry : weatherValues.entrySet()) {
           System.out.printf("%s = %s\n",
             entry.getKey().toStringUtf8(),
             entry.getValue().toStringUtf8());
       }
     }
    }
    

## What's next

  * Explore the [GoogleSQL for Bigtable reference documentation](https://docs.cloud.google.com/bigtable/docs/reference/sql/googlesql-reference-overview).
  * Learn how to [write SQL with Gemini assistance](https://docs.cloud.google.com/bigtable/docs/write-sql-gemini).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
