---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/
title: Google.Cloud.Spanner.Data \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:49:35.973327+00:00
---

# Google.Cloud.Spanner.Data  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google.Cloud.Spanner.Data Stay organized with collections  Save and categorize content based on your preferences. 

5.13.0-beta11  5.13.0-beta10  5.12.0 (latest)  5.11.0  5.10.0  5.9.0  5.8.0  5.7.0  5.6.0  5.5.0  5.4.0  5.3.0  5.2.0  5.1.0  5.0.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.15.1  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0 

`Google.Cloud.Spanner.Data` is the ADO.NET provider for Cloud Spanner. It is the recommended package for regular Cloud Spanner database access from .NET.

Note: This documentation is for version `5.13.0-beta11` of the library. Some samples may not work with other versions.

The [Google.Cloud.Spanner.Admin.Instance.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest) package should be used for Cloud Spanner instance administration, such as creating or deleting instances.

## Installation

Install the `Google.Cloud.Spanner.Data` package from NuGet. Add it to your project in the normal way (for example by right-clicking on the project in Visual Studio and choosing "Manage NuGet Packages..."). Please ensure you enable pre-release packages (for example, in the Visual Studio NuGet user interface, check the "Include prerelease" box). Some of the following samples might only work with the latest pre-release version (`5.13.0-beta11`) of `Google.Cloud.Spanner.Data`.

## Authentication

When running on Google Cloud, no action needs to be taken to authenticate.

Otherwise, the simplest way of authenticating your API calls is to set up Application Default Credentials. The credentials will automatically be used to authenticate. See [Set up Application Default Credentials](https://cloud.google.com/docs/authentication/provide-credentials-adc) for more details.

## Getting started

Operations generally follow ADO.NET conventions. There may be some incompatibilities between the ADO.NET surface and Spanner capabilities, in which case you should use the relevant SpannerConnection methods.

## Credentials

Without any other configuration, `Google.Cloud.Spanner.Data` uses [Application Default Credentials](https://cloud.google.com/docs/authentication#adc). If you need to provide other credentials, there are three alternatives:

  * Specify `CredentialFile` in the [connection string](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/connection_string)
  * Pass a `GoogleCredential` into the constructor of `SpannerConnection` or `SpannerConnectionStringBuilder`. Scopes will be applied automatically, and self-signed JWTs will be used where possible.
  * Pass a `ChannelCredentials` into the constructor of `SpannerConnection` or `SpannerConnectionStringBuilder`.



## SpannerConnection and Dependency Injection

A `SpannerConnection` can be provided via dependency injection based on the ConnectionStrings section of the application configuration, via the `AddSpannerConnection` extension method. For example, consider an application configured with `appsettings.json` file like this:
    
    
    {
      "ConnectionStrings": {
        "SpannerDb": "Data Source=projects/my-project/instances/my-instance"
      }
    }
    

The `SpannerConnection` can be configured on the service collection as shown below:
    
    
    services.AddSpannerConnection("SpannerDb");
    

The dependency is registered as a transient dependency (as a new `SpannerConnection` should be created for each request), and is automatically disposed by the dependency injection infrastructure.

If the dependency injection container has been configured with `ChannelCredentials` or `GoogleCredential` values, those are used automatically by `AddSpannerConnection`. (If both are specified, `ChannelCredentials` takes priority.) Note that this means any `CredentialsFile` specified in the connection string is ignored when the connection is obtained via dependency injection and a `ChannelCredentials` or `GoogleCredential` is available from the same container.

## Sample code

Once you have created your Google Cloud Project and Spanner Instance using the web console, you can start using the ADO.NET provider to create and modify a Cloud Spanner database.

## Creating a Database and Table

> **Note**  
>  For convenience `Google.Cloud.Spanner.Data` allows you to use standard `SpannerCommand`s for DDL operations. But do take into account that Spanner transactions do not support DDL operations, so even if you set `SpannerCommand.Transaction` on a DDL command, the command will execute outside the transaction.
    
    
    using (SpannerConnection connection = new SpannerConnection(connectionString))
    {
        SpannerCommand createDbCmd = connection.CreateDdlCommand($"CREATE DATABASE {databaseName}");
        await createDbCmd.ExecuteNonQueryAsync();
    
        SpannerCommand createTableCmd = connection.CreateDdlCommand(
            @"CREATE TABLE TestTable (
                                    Key                STRING(MAX) NOT NULL,
                                    StringValue        STRING(MAX),
                                    Int64Value         INT64,
                                  ) PRIMARY KEY (Key)");
        await createTableCmd.ExecuteNonQueryAsync();
    }
    

## DataAdapter support (.NET 4.5+ only)

Cloud Spanner supports a limited DataAdapter that provides basic CRUD operations on any table. Create a SpannerDataAdapter with the target table and its primary keys. You may replace any commands provided by SpannerDataAdapter with your own custom commands.
    
    
    using (SpannerConnection connection = new SpannerConnection(connectionString))
    {
        DataSet untypedDataSet = new DataSet();
    
        // Provide the name of the Cloud Spanner table and primary key column names.
        SpannerDataAdapter adapter = new SpannerDataAdapter(connection, "TestTable", "Key");
        adapter.Fill(untypedDataSet);
    
        // Insert a row
        DataRow row = untypedDataSet.Tables[0].NewRow();
        row["Key"] = Guid.NewGuid().ToString("N");
        row["StringValue"] = "New String Value";
        row["Int64Value"] = 0L;
        untypedDataSet.Tables[0].Rows.Add(row);
    
        adapter.Update(untypedDataSet.Tables[0]);
    }
    

## Modifying data

Cloud Spanner supports two approaches to modifying data: DML, and direct row modifications.

### DML

DML is capable of affecting multiple rows with a single command. For example, you could delete all rows matching a query, or update rows to set the value of one column equal to another one.

DML can be executed in standard mode using `ExecuteNonQuery` or `ExecuteNonQueryAsync`:
    
    
    using (SpannerConnection connection = new SpannerConnection(connectionString))
    {
        await connection.OpenAsync();
    
        // If the transaction is aborted, RunWithRetriableTransactionAsync will
        // retry the whole unit of work with a fresh transaction each time.
        // Please be aware that the whole unit of work needs to be prepared
        // to be called more than once.
        await connection.RunWithRetriableTransactionAsync(async transaction =>
        {
            SpannerCommand cmd = connection.CreateDmlCommand(
                "UPDATE TestTable SET StringValue='Updated' WHERE Int64Value=@value");
            cmd.Parameters.Add("value", SpannerDbType.Int64, 10);
            cmd.Transaction = transaction;
            int rowsAffected = await cmd.ExecuteNonQueryAsync();
            Console.WriteLine($"{rowsAffected} rows updated...");
        });
    }
    

It is recommended that you execute DML statements within a retriable transaction. Queries within the same transaction are able to observe the changes already made by DML statements, and later DML statements can use the values created or updated by earlier ones. Also, if the transaction is aborted at any point, the whole unit of work will be retried automatically. Note that the code executing within a retriable transaction needs to be prepared to be called more than once. Please read the [Cloud Spanner user documentation](https://cloud.google.com/spanner/docs/reference/rest/v1/TransactionOptions) for details on when and why transactions can be aborted.

Some DML statements can be executed in a _partitioned_ manner, enabling an efficient update of large data sets. `ExecutePartitionedUpdate` or `ExecutePartitionedUpdateAsync`:
    
    
    using (SpannerConnection connection = new SpannerConnection(connectionString))
    {
        await connection.OpenAsync();
    
        SpannerCommand cmd = connection.CreateDmlCommand(
            "UPDATE TestTable SET TestTable.StringValue='Updated in partitions' WHERE TestTable.Int64Value=@value");
        cmd.Parameters.Add("value", SpannerDbType.Int64, 9);
        long rowsAffected = await cmd.ExecutePartitionedUpdateAsync();
        Console.WriteLine($"{rowsAffected} rows updated...");
    }
    

Partitioned DML updates cannot be performed within another transaction, and have "at least once" semantics: the update can be applied more than once to a row in some cases, and so is best used with idempotent updates.

Not all DML statements can be partitioned. Please read the Cloud Spanner user documentation for details on the restrictions.

### Batch DML

Batch DML allows you to execute multiple DML commands in one batched operation.
    
    
    using (SpannerConnection connection = new SpannerConnection(connectionString))
    {
        await connection.OpenAsync();
    
        // If the transaction is aborted, RunWithRetriableTransactionAsync will
        // retry the whole unit of work with a fresh transaction each time.
        // Please be aware that the whole unit of work needs to be prepared
        // to be called more than once.
        await connection.RunWithRetriableTransactionAsync(async (transaction) =>
        {
            SpannerBatchCommand cmd = transaction.CreateBatchDmlCommand();
    
            cmd.Add(
                "UPDATE TestTable SET StringValue='Updated' WHERE Int64Value=@value",
                new SpannerParameterCollection { { "value", SpannerDbType.Int64, 5 } });
    
            cmd.Add(
                "DELETE FROM TestTable WHERE Int64Value=@value",
                new SpannerParameterCollection { { "value", SpannerDbType.Int64, 250 } });
    
            IEnumerable<long> rowsAffected = await cmd.ExecuteNonQueryAsync();
            Console.WriteLine($"{rowsAffected.ElementAt(0)} rows updated...");
            Console.WriteLine($"{rowsAffected.ElementAt(1)} rows deleted...");
        });
    }
    

Statements are executed sequentally in the same order they are provided. Changes made by one statement are visible to all subsequent statements in the batch.

When one of the statemens in the batch fails, execution is halted and all subsequent statements are not executed. A `SpannerBatchNonQueryException` will be thrown that contains both information about the error and the number of rows affected by each of the statements that executed before the failed one. If you are executing the batch DML command inside a non-retriable transaction you can simply commit the transaction when `SpannerBatchNonQueryException` is thrown if partial success is acceptable in your application. It is recommended to run Batch DML within a retriable transaction. If the transaction aborts the whole unit of work will be retried automatically. Note that the code executing within a retriable transaction needs to be prepared to be called more than once. Please read the [Cloud Spanner user documentation](https://cloud.google.com/spanner/docs/reference/rest/v1/TransactionOptions) for details on when and why transactions can be aborted.

### Direct row modifications

The following operations are supported for direct row modification:

  * Insert
  * Update
  * Delete
  * Insert or update (also known as "upsert")



Create a command from the `SpannerConnection`, providing the table name to the appropriate method (`CreateInsertCommand` and the like), then use the command parameters to specify values for columns. The command can be reused to perform the same kind of operation for multiple rows.

This sample inserts two rows, then reads them again:
    
    
    using (SpannerConnection connection = new SpannerConnection(connectionString))
    {
        await connection.OpenAsync();
    
        // If the transaction is aborted, RunWithRetriableTransactionAsync will
        // retry the whole unit of work with a fresh transaction each time.
        await connection.RunWithRetriableTransactionAsync(async transaction =>
        {
            SpannerCommand cmd = connection.CreateInsertCommand("TestTable");
            SpannerParameter keyParameter = cmd.Parameters.Add("Key", SpannerDbType.String);
            SpannerParameter stringValueParameter = cmd.Parameters.Add("StringValue", SpannerDbType.String);
            SpannerParameter int64ValueParameter = cmd.Parameters.Add("Int64Value", SpannerDbType.Int64);
            cmd.Transaction = transaction;
    
            // This executes 5 distinct insert commands using the retriable transaction.
            // The mutations will be effective once the transaction has committed successfully.
            for (int i = 0; i < 5; i++)
            {
                keyParameter.Value = Guid.NewGuid().ToString("N");
                stringValueParameter.Value = $"StringValue{i}";
                int64ValueParameter.Value = i;
                int rowsAffected = await cmd.ExecuteNonQueryAsync();
                Console.WriteLine($"{rowsAffected} rows written...");
            }
        });
    }
    

This sample reads three keys using a `SELECT` command, updates a row using an `UPDATE` command, then deletes a row using a `DELETE` command:
    
    
    using (SpannerConnection connection = new SpannerConnection(connectionString))
    {
        await connection.OpenAsync();
    
        // If the transaction is aborted, RunWithRetriableTransactionAsync will
        // retry the whole unit of work with a fresh transaction each time.
        // Please be aware that the whole unit of work needs to be prepared
        // to be called more than once.
        await connection.RunWithRetriableTransactionAsync(async transaction =>
        {
            // Read the first 3 keys in the database.
            List<string> keys = new List<string>();
            SpannerCommand selectCmd = connection.CreateSelectCommand("SELECT * FROM TestTable");
            selectCmd.Transaction = transaction;
            using (SpannerDataReader reader = await selectCmd.ExecuteReaderAsync())
            {
                while (keys.Count < 4 && await reader.ReadAsync())
                {
                    keys.Add(reader.GetFieldValue<string>("Key"));
                }
            }
    
            // Update the Int64Value of keys[0]
            // Include the primary key and update columns.
            SpannerCommand updateCmd = connection.CreateUpdateCommand("TestTable");
            updateCmd.Parameters.Add("Key", SpannerDbType.String, keys[0]);
            updateCmd.Parameters.Add("Int64Value", SpannerDbType.Int64, 0L);
            updateCmd.Transaction = transaction;
            await updateCmd.ExecuteNonQueryAsync();
    
            // Delete row for keys[1] and keys[2]
            SpannerCommand deleteCmd = connection.CreateDeleteCommandForKeySet(
                "TestTable",
                KeySet.FromKeys(new Key(keys[1]), new Key(keys[2])));
            deleteCmd.Transaction = transaction;
            await deleteCmd.ExecuteNonQueryAsync();
        });
    

When direct row modifications are performed in a transaction, they are only applied when the transaction is committed. Queries within the transaction will not observe any changes. It is recommended to run direct row modifications within a retriable transaction. If the transaction aborts the whole unit of work will be retried automatically. Note that the code executing within a retriable transaction needs to be prepared to be called more than once. Please read the [Cloud Spanner user documentation](https://cloud.google.com/spanner/docs/reference/rest/v1/TransactionOptions) for details on when and why transactions can be aborted.

### Automatic retry of single commands

When executing a single write command without specifying a transaction, an exclusive ephemeral transaction will be used internally. If the transaction is aborted the command will be retried automatically. This means that, for executing single commands that don't need to share a transaction, you don't need to use a retriable transaction.
    
    
    using (SpannerConnection connection = new SpannerConnection(connectionString))
    {
        await connection.OpenAsync();
    
        // The following commands will be executed within an exclusive ephemeral transaction.
        // If the transaction is aborted, execution of the command will be automatically retried.
        SpannerCommand cmd = connection.CreateInsertCommand("TestTable");
        cmd.Parameters.Add("Key", SpannerDbType.String, Guid.NewGuid().ToString("N"));
        cmd.Parameters.Add("StringValue", SpannerDbType.String, "hello");
        cmd.Parameters.Add("Int64Value", SpannerDbType.Int64, 8);
    
        int rowsAffected = await cmd.ExecuteNonQueryAsync();
        Console.WriteLine($"{rowsAffected} rows written...");
    }
    

This applies to DML, Batch DML and direct row modifications. It does not apply to partioned DML commands as it is the Cloud Spanner service the one that handles the transaction lifecycle for partioned DML commands, which are already automatically retried on aborted.

### Using a commit timestamp

Spanner allows you to write a commit timestamp for insert and update operations.

When using direct row modifications, the commit timestamp can be set using `SpannerParameter.CommitTimestamp` as the value for a parameter, as shown below.
    
    
    using (SpannerConnection connection = new SpannerConnection(connectionString))
    {
        await connection.OpenAsync();
    
        string createTableStatement =
            @"CREATE TABLE UsersHistory (
            Id INT64 NOT NULL,
            CommitTs TIMESTAMP NOT NULL OPTIONS
                (allow_commit_timestamp=true),
            Name STRING(MAX) NOT NULL,
            Email STRING(MAX),
            Deleted BOOL NOT NULL,
            ) PRIMARY KEY(Id, CommitTs DESC)";
    
        await connection.CreateDdlCommand(createTableStatement).ExecuteNonQueryAsync();
    
        // Create a command for inserting rows.
        SpannerCommand cmd = connection.CreateInsertCommand("UsersHistory",
            new SpannerParameterCollection
            {
                { "Id", SpannerDbType.Int64 },
                { "CommitTs", SpannerDbType.Timestamp, SpannerParameter.CommitTimestamp },
                { "Name", SpannerDbType.String },
                { "Deleted", SpannerDbType.Bool , false}
            });
    
        int rowsAffected = 0;
    
        // If the transaction is aborted, RunWithRetriableTransactionAsync will
        // retry the whole unit of work with a fresh transaction each time.
        // Please be aware that the whole unit of work needs to be prepared
        // to be called more than once.
        await connection.RunWithRetriableTransactionAsync(async transaction =>
        {
            // Insert a first row
            cmd.Parameters["Id"].Value = 10L;
            cmd.Parameters["Name"].Value = "Demo 1";
            cmd.Transaction = transaction;
            rowsAffected += await cmd.ExecuteNonQueryAsync();
        });
    
        await connection.RunWithRetriableTransactionAsync(async transaction =>
        {
            // Insert a second row
            cmd.Parameters["Id"].Value = 11L;
            cmd.Parameters["Name"].Value = "Demo 2";
            cmd.Transaction = transaction;
            rowsAffected += await cmd.ExecuteNonQueryAsync();
        });
    
        Console.WriteLine($"{rowsAffected} rows written...");
    
        // Display the inserted values
        SpannerCommand selectCmd = connection.CreateSelectCommand("SELECT * FROM UsersHistory");
        using (SpannerDataReader reader = await selectCmd.ExecuteReaderAsync())
        {
            while (await reader.ReadAsync())
            {
                long id = reader.GetFieldValue<long>("Id");
                string name = reader.GetFieldValue<string>("Name");
                DateTime timestamp = reader.GetFieldValue<DateTime>("CommitTs");
                Console.WriteLine($"{id}: {name} - {timestamp:HH:mm:ss.ffffff}");
            }
        }
    }
    

This parameter value cannot be used in DML. Instead, use the `PENDING_COMMIT_TIMESTAMP()` function in your DML statement.

See the [Cloud Spanner documentation](https://cloud.google.com/spanner/docs/commit-timestamp) for more information about commit timestamps.

## Transactions and Fault Handling

Cloud Spanner is fully ACID compliant.

Retries should be implemented at the transaction level (as opposed to individual call level) because there is a chance in high stress situations that a Cloud Spanner session (transaction) can be aborted due to causing a deadlock. In this case, the entire transaction should be retried. The methods `SpannerConnection.RunWithRetriableTransactionAsync(...)` will take care of automatically retrying the entire callback passed as a paremeter using a fresh transaction if previous attempts aborted.

  * The callback doesn't need to handle the transaction lifecycle.
  * The callback needs to set the transaction received on all the commands it creates.
  * The callback might be called more than once, so the code should be written bearing this in mind.



Please read the [Cloud Spanner user documentation](https://cloud.google.com/spanner/docs/reference/rest/v1/TransactionOptions) for details on when and why transactions can be aborted.
    
    
    using (SpannerConnection connection = new SpannerConnection(connectionString))
    {
        await connection.OpenAsync();
    
        // If the transaction is aborted, RunWithRetriableTransactionAsync will
        // retry the whole unit of work with a fresh transaction each time.
        await connection.RunWithRetriableTransactionAsync(async transaction =>
        {
            SpannerCommand cmd = connection.CreateInsertCommand("TestTable");
            SpannerParameter keyParameter = cmd.Parameters.Add("Key", SpannerDbType.String);
            SpannerParameter stringValueParameter = cmd.Parameters.Add("StringValue", SpannerDbType.String);
            SpannerParameter int64ValueParameter = cmd.Parameters.Add("Int64Value", SpannerDbType.Int64);
            cmd.Transaction = transaction;
    
            // This executes 5 distinct insert commands using the retriable transaction.
            // The mutations will be effective once the transaction has committed successfully.
            for (int i = 0; i < 5; i++)
            {
                keyParameter.Value = Guid.NewGuid().ToString("N");
                stringValueParameter.Value = $"StringValue{i}";
                int64ValueParameter.Value = i;
                int rowsAffected = await cmd.ExecuteNonQueryAsync();
                Console.WriteLine($"{rowsAffected} rows written...");
            }
        });
    }
    

## Session pool management

`Google.Cloud.Spanner.Data` manages Spanner sessions for you via a session pool. The pool has various [configuration options](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/configuration), but additionally you may wish to take advantage of additional `SpannerConnection` methods at the start and end of your application.

To ensure that the session pool is populated with the configured minimum number of sessions before serving requests from your application, you may wish to wait for the task returned by `SpannerConnection.WhenSessionPoolReady()` to complete before marking your application as "ready to serve".
    
    
    // This would usually be executed during application start-up, before any Spanner
    // operations are performed. It can be used at any time, however. It is purely passive:
    // it doesn't modify the session pool or trigger any other actions.
    using (SpannerConnection connection = new SpannerConnection(connectionString))
    {
        await connection.WhenSessionPoolReady();
    }
    

When your application is shutting down, you may wish to delete the sessions it has been using from the server. Most applications will not need to do this: sessions automatically expire after an idle time of an hour anyway, and the server-enforced session limit is high. Applications using a large number of sessions may wish to clean up sessions more actively, however. Again, `SpannerConnection` provides a simple method to accomplish this:
    
    
    // When your application is shutting down. Note that any pending or future requests
    // for sessions will fail.
    using (SpannerConnection connection = new SpannerConnection(connectionString))
    {
        await connection.ShutdownSessionPoolAsync();
    }
    

## Retrieving an RpcException from a SpannerException

The `RpcException` property of `SpannerException` returns the underlying `RpcException` which caused the `SpannerException`. The returned value may be null if the `SpannerException` was not caused by an `RpcException`.

This can in turn be used to [obtain an ErrorInfo](https://docs.cloud.google.com/dotnet/docs/docs/devsite-help/troubleshooting.md#how-can-i-get-errorinfo-from-rpcexception) which can provide actionable error details. 

Sample code:
    
    
    using Google.Api.Gax.Grpc;
    try
    {
        // Code using Spanner. 
    }
    catch (SpannerException ex)
    {
        if (ex.RpcException is RpcException rpcException)
        {
            if (rpcException.GetErrorInfo() is ErrorInfo errorInfo)
            {
                var domain = errorInfo.Domain;
                var reason = errorInfo.Reason;
                var metadata = errorInfo.Metadata;
                // Use the domain, reason and metadata of ErrorInfo, e.g. for logging or taking remedial action.
            }
            else
            {
                // Use RpcException's other properties (e.g. Status and Message) to handle the exception appropriately.
            }
        }
        else
        {
            // Use SpannerException's other properties (e.g. ErrorCode and Message) to handle the exception appropriately.
        }
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
