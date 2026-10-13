---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/
title: Google.Cloud.BigQuery.V2 \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:57:38.205077+00:00
---

# Google.Cloud.BigQuery.V2  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google.Cloud.BigQuery.V2 Stay organized with collections  Save and categorize content based on your preferences. 

3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.4.0  2.3.0  2.2.0 

`Google.Cloud.BigQuery.V2` is a.NET client library for the [Google BigQuery API](https://cloud.google.com/bigquery/). It wraps the `Google.Apis.Bigquery.v2` generated library, providing a higher-level API to make it easier to use.

Note: This documentation is for version `3.12.0` of the library. Some samples may not work with other versions.

## Installation

Install the `Google.Cloud.BigQuery.V2` package from NuGet. Add it to your project in the normal way (for example by right-clicking on the project in Visual Studio and choosing "Manage NuGet Packages...").

## Authentication

When running on Google Cloud, no action needs to be taken to authenticate.

Otherwise, the simplest way of authenticating your API calls is to set up Application Default Credentials. The credentials will automatically be used to authenticate. See [Set up Application Default Credentials](https://cloud.google.com/docs/authentication/provide-credentials-adc) for more details.

## Getting started

Common operations are exposed via the [BigQueryClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient) class, and additional wrapper classes are present to make operations with datasets, tables and query results simpler.

## Client life-cycle management

In many cases you don't need to worry about disposing of `BigQueryClient` objects, and can create them reasonably freely - but be aware that this _can_ causes issues with memory and network connection usage. We advise you to reuse a single client object if possible; if your architecture requires you to frequently create new client objects, please dispose of them to help with timely resource clean-up. See [the resource clean-up guide](https://cloud.google.com/dotnet/docs/reference/help/cleanup#rest-based-apis) for more details.

## Sample code

## Querying
    
    
    BigQueryClient client = BigQueryClient.Create(projectId);
    BigQueryTable table = client.GetTable("bigquery-public-data", "samples", "shakespeare");
    
    string sql = $"SELECT corpus AS title, COUNT(word) AS unique_words FROM {table} GROUP BY title ORDER BY unique_words DESC LIMIT 10";
    BigQueryParameter[] parameters = null;
    BigQueryResults results = client.ExecuteQuery(sql, parameters);
    
    foreach (BigQueryRow row in results)
    {
        Console.WriteLine($"{row["title"]}: {row["unique_words"]}");
    }
    

## Parameterized queries

Queries can be provided with parameters, either using names (the default):
    
    
    BigQueryClient client = BigQueryClient.Create(projectId);
    BigQueryTable table = client.GetTable(datasetId, tableId);
    string sql = $"SELECT player, score, level FROM {table} WHERE score >= @score AND level >= @level";
    BigQueryParameter[] parameters = new[]
    {
        new BigQueryParameter("level", BigQueryDbType.Int64, 2),
        new BigQueryParameter("score", BigQueryDbType.Int64, 1500)
    };
    BigQueryResults results = client.ExecuteQuery(sql, parameters);
    foreach (BigQueryRow row in results)
    {
        Console.WriteLine($"Name: {row["player"]}; Score: {row["score"]}; Level: {row["level"]}");
    }
    

Or using positional parameters:
    
    
    BigQueryClient client = BigQueryClient.Create(projectId);
    BigQueryTable table = client.GetTable(datasetId, tableId);
    string sql = $"SELECT player, score, level FROM {table} WHERE score >= ? AND level >= ?";
    BigQueryParameter[] parameters = new[]
    {
        new BigQueryParameter(BigQueryDbType.Int64, 1500), // For score
        new BigQueryParameter(BigQueryDbType.Int64, 2), // For level
    };
    QueryOptions queryOptions = new QueryOptions { ParameterMode = BigQueryParameterMode.Positional };
    BigQueryResults results = client.ExecuteQuery(sql, parameters, queryOptions);
    foreach (BigQueryRow row in results)
    {
        Console.WriteLine($"Name: {row["player"]}; Score: {row["score"]}; Level: {row["level"]}");
    }
    

## Using legacy SQL

By default, [BigQueryClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient) uses [Standard SQL](https://cloud.google.com/bigquery/sql-reference/). To use [Legacy SQL](https://cloud.google.com/bigquery/query-reference), simply set `UseLegacySql` to true in the query options, and make sure that you use the legacy format for the table name, as shown below.
    
    
    BigQueryClient client = BigQueryClient.Create(projectId);
    BigQueryTable table = client.GetTable("bigquery-public-data", "samples", "shakespeare");
    
    string sql = $"SELECT TOP(corpus, 10) AS title, COUNT(*) AS unique_words FROM {table:legacy}";
    BigQueryParameter[] parameters = null;
    BigQueryResults results = client.ExecuteQuery(sql, parameters, new QueryOptions { UseLegacySql = true });
    
    foreach (BigQueryRow row in results)
    {
        Console.WriteLine($"{row["title"]}: {row["unique_words"]}");
    }
    

## Wildcard queries

[Wildcard queries](https://cloud.google.com/bigquery/docs/querying-wildcard-tables) can be used to query multiple tables at the same time. Wildcard table names only work in queries written using Standard SQL, so make sure to use the standard format for the table name as shown below.
    
    
    BigQueryClient client = BigQueryClient.Create(projectId);
    
    string sql = $"SELECT year, mo, da, temp, min, max FROM `bigquery-public-data.noaa_gsod.gsod*` where `max` > 120 and `max` < 121 LIMIT 10";
    BigQueryParameter[] parameters = null;
    BigQueryResults results = client.ExecuteQuery(sql, parameters);
    
    foreach (BigQueryRow row in results)
    {
        Console.WriteLine($"On {row["year"]}-{row["mo"]}-{row["da"]} the mean temperature was {row["temp"]} with min temperature at {row["min"]} and max temperature at {row["max"]}.");
    }
    

## Data insertion
    
    
    BigQueryClient client = BigQueryClient.Create(projectId);
    
    // Create the dataset if it doesn't exist.
    BigQueryDataset dataset = client.GetOrCreateDataset("mydata");
    
    // Create the table if it doesn't exist.
    BigQueryTable table = dataset.GetOrCreateTable("scores", new TableSchemaBuilder
    {
        { "player", BigQueryDbType.String },
        { "gameStarted", BigQueryDbType.Timestamp },
        { "score", BigQueryDbType.Int64 }
    }.Build());
    
    // Insert a single row. There are many other ways of inserting
    // data into a table.
    table.InsertRow(new BigQueryInsertRow
    {
        { "player", "Bob" },
        { "score", 85 },
        { "gameStarted", new DateTime(2000, 1, 14, 10, 30, 0, DateTimeKind.Utc) }
    });
    

## DML

BigQuery supports [DML](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-manipulation-language).

Suppose we have a high score table, and we realize that on one day we accidentally recorded incorrect scores: each player was only awarded half the score they actually earned. We can update the data afterwards using DML:
    
    
    BigQueryClient client = BigQueryClient.Create(projectId);
    BigQueryTable table = client.GetTable(datasetId, tableId);
    BigQueryResults result = client.ExecuteQuery(
        $"UPDATE {table} SET score = score * 2 WHERE DATE(game_started) = @date",
        new[] { new BigQueryParameter("date", BigQueryDbType.Date, new DateTime(2013, 6, 1)) })
        .ThrowOnAnyError();
    Console.WriteLine($"Modified {result.NumDmlAffectedRows} row(s)");
    

### Important note on the result returned by DML operations (in version 1.3.0)

In version 1.3.0, iterating over the results of a `BigQueryResults` object returned from a DML operation will iterate over the entire table modified by that operation. This is a side-effect of the way the underlying API is called, but it's rarely useful to iterate over the results. The `NumDmlAffectedRows` property of the results object is useful, however, in determining how many rows were modified.

From version 1.4.0-beta01 onwards, the `BigQueryResults` object returned from a DML operation returns no rows, but `NumDmlAffectedRows` still returns the number of affected rows.

## Creating a table partitioned by time
    
    
    BigQueryClient client = BigQueryClient.Create(projectId);
    TableSchema schema = new TableSchemaBuilder
    {
        { "message", BigQueryDbType.String }
    }.Build();
    Table tableToCreate = new Table
    {
        TimePartitioning = TimePartition.CreateDailyPartitioning(expiration: null),
        Schema = schema
    };
    BigQueryTable table = client.CreateTable(datasetId, tableId, tableToCreate);
    // Upload a single row to the table, using JSON rather than the streaming buffer, as
    // the _PARTITIONTIME column will be null while it's being served from the streaming buffer.
    // This code assumes the upload succeeds; normally, you should check the job results.
    table.UploadJson(new[] { "{ \"message\": \"Sample message\" }" }).PollUntilCompleted();
    
    BigQueryResults results = client.ExecuteQuery(
        $"SELECT message, _PARTITIONTIME AS pt FROM {table}",
        parameters: null);
    List<BigQueryRow> rows = results.ToList();
    foreach (BigQueryRow row in rows)
    {
        string message = (string) row["message"];
        DateTime partition = (DateTime) row["pt"];
        Console.WriteLine($"Message: {message}; partition: {partition:yyyy-MM-dd}");
    }
    

## Querying an external data source

As [described in the documentation](https://cloud.google.com/bigquery/external-data-sources), BigQuery can query some external data sources. The sample code below demonstrates querying a CSV file stored in Google Cloud Storage.
    
    
    BigQueryClient client = BigQueryClient.Create(projectId);
    TableSchema schema = new TableSchemaBuilder
    {
        { "name", BigQueryDbType.String },
        { "score", BigQueryDbType.Int64 }
    }.Build();
    Table tableToCreate = new Table
    {
        ExternalDataConfiguration = new ExternalDataConfiguration
        {
            SourceFormat = "CSV",
            SourceUris = new[] { $"gs://{bucket}/{objectName}" }
        },
        Schema = schema
    };
    BigQueryTable table = client.CreateTable(datasetId, tableId, tableToCreate);
    BigQueryParameter[] parameters = null;
    List<BigQueryRow> rows = client.ExecuteQuery($"SELECT name, score FROM {table} ORDER BY score", parameters).ToList();
    foreach (BigQueryRow row in rows)
    {
        Console.WriteLine($"{row["name"]} - {row["score"]}");
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
