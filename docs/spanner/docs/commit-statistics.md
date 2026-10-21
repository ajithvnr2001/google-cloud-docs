---
url: https://docs.cloud.google.com/spanner/docs/commit-statistics/
title: Retrieve commit statistics for a transaction \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:17.206872+00:00
---

# Retrieve commit statistics for a transaction  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/commit-statistics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Retrieve commit statistics for a transaction Stay organized with collections  Save and categorize content based on your preferences. 

To help you better understand, optimize, and diagnose transaction issues, Spanner gives you access to transaction commit statistics. Currently, you can retrieve the total number of mutations for a transaction.

## When to use commit statistics

Knowing the mutation count for a transaction can be useful in the following scenarios.

### Optimize for round trips

To help improve the performance of your application you can reduce the number of round trips to the database by doing as much work as possible in each transaction. In this scenario you want to maximize the number of mutations per transaction, while at the same time staying within system [limits](https://docs.cloud.google.com/spanner/quotas#limits_for_creating_reading_updating_and_deleting_data).

To determine how many rows you can commit per transaction while staying under the limit, first commit one row in a transaction. This gives you a baseline of the mutation count per row. Then divide the system limit by your baseline to get a rows-per-transaction number. For more information on how mutations are counted, refer to this [note](https://docs.cloud.google.com/spanner/quotas#note2).

When using DML, the 80,000 limit (including indexes) applies per statement, not per transaction. You can execute multiple DML statements in a single transaction to commit more than 80,000 mutations, subject to the transaction size limit of 100 MiB. In this case, the returned `mutation_count` in commit statistics reflects the total cumulative mutations (including indexes) across all statements, and can exceed 80,000.

Note that optimizing for round trips is not always beneficial, particularly if it results in more lock contentions. You can troubleshoot lock conflicts in your database using [lock statistics](https://docs.cloud.google.com/spanner/docs/introspection/lock-statistics).

### Monitor your transactions to avoid hitting system limits

As application usage increases, it's possible that the number of mutations in your transaction also grows. To avoid hitting the system limit and having your transaction eventually fail, you can proactively monitor the mutation count commit statistic over time. If you observe this value increasing for the same transaction, it might be time to re-optimize your transaction as described in the preceding section.

## How to access commit statistics

Commit statistics are not returned by default. Instead, you need to set the `return_commit_stats` flag to true on each [CommitRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.v1#commitrequest). If you use the Mutation API and your commit attempt exceeds the maximum allowable number of mutations (including indexes), the commit fails and an [INVALID_ARGUMENT](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Code#ENUM_VALUES.INVALID_ARGUMENT) error is returned. For DML, exceeding the mutation limit (including indexes) causes the individual DML statement to fail during execution with a `BadUsage` error, rather than failing at commit time.

Here's an example of how to return commit statistics using the Spanner client libraries.

### Retrieve commit statistics

The following sample shows how to get commit statistics using the Spanner client libraries.

### C++

The following code calls `set_return_stats()` on `CommitOptions` and returns a mutation count of 6, because we are inserting or updating 2 rows and 3 columns in each row.
    
    
    void GetCommitStatistics(google::cloud::spanner::Client client) {
      namespace spanner = ::google::cloud::spanner;
    
      auto commit = client.Commit(
          spanner::Mutations{
              spanner::UpdateMutationBuilder(
                  "Albums", {"SingerId", "AlbumId", "MarketingBudget"})
                  .EmplaceRow(1, 1, 200000)
                  .EmplaceRow(2, 2, 400000)
                  .Build()},
          google::cloud::Options{}.set<spanner::CommitReturnStatsOption>(true));
    
      if (!commit) throw std::move(commit).status();
      if (commit->commit_stats) {
        std::cout << "Updated data with " << commit->commit_stats->mutation_count
                  << " mutations.\n";
      }
      std::cout << "Update was successful [spanner_get_commit_stats]\n";
    }

### C#

In C#, commit statistics are not returned directly through the API. Instead, they are logged at the **Information** log level by the default logger.

The following code enables commit statistics logging for all transactions by setting the `LogCommitStats` property on `SpannerConnectionStringBuilder` to true. The code also implements a sample logger that keeps a reference to the last seen commit response. The `MutationCount` is then retrieved from this response and displayed.
    
    
    using [Google.Cloud.Spanner.Data](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.html);
    using [Google.Cloud.Spanner.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.html);
    using [Google.Cloud.Spanner.V1.Internal.Logging](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.Internal.Logging.html);
    using System;
    using System.Collections.Generic;
    using System.Diagnostics;
    using System.Threading.Tasks;
    
    public class LogCommitStatsAsyncSample
    {
        public async Task<long> LogCommitStatsAsync(string projectId, string instanceId, string databaseId)
        {
            // Commit statistics are logged at level Info by the default logger.
            // This sample uses a custom logger to access the commit statistics.
            // See https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Spanner.Data/logging.html
            // for more information on how to use loggers.
            var logger = new CommitStatsSampleLogger();
            var options = new [SessionPoolOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.SessionPoolOptions.html)();
            var poolManager = [SessionPoolManager](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SessionPoolManager.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SessionPoolManager.html#Google_Cloud_Spanner_Data_SessionPoolManager_Create_Google_Cloud_Spanner_V1_SessionPoolOptions_Google_Cloud_Spanner_V1_Internal_Logging_Logger_)(options, logger);
            var connectionStringBuilder = new [SpannerConnectionStringBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnectionStringBuilder.html)
            {
                ConnectionString = $"Data Source=projects/{projectId}/instances/{instanceId}/databases/{databaseId}",
                // Set LogCommitStats to true to enable logging commit statistics for all transactions on the connection.
                // LogCommitStats can also be enabled/disabled for individual Spanner transactions.
                LogCommitStats = true,
                SessionPoolManager = poolManager,
            };
    
            using var connection = new [SpannerConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html)(connectionStringBuilder);
            await connection.[OpenAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html#Google_Cloud_Spanner_Data_SpannerConnection_OpenAsync_Google_Cloud_Spanner_Data_SpannerTransactionCreationOptions_Google_Cloud_Spanner_Data_SpannerTransactionOptions_System_Threading_CancellationToken_)();
    
            using var cmd = connection.[CreateDmlCommand](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html#Google_Cloud_Spanner_Data_SpannerConnection_CreateDmlCommand_System_String_Google_Cloud_Spanner_Data_SpannerParameterCollection_)("INSERT Singers (SingerId, FirstName, LastName) VALUES (110, 'Virginia', 'Watson')");
            var rowCount = await cmd.ExecuteNonQueryAsync();
            var mutationCount = logger._lastCommitResponse.CommitStats.[MutationCount](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.CommitResponse.Types.CommitStats.html#Google_Cloud_Spanner_V1_CommitResponse_Types_CommitStats_MutationCount);
    
            Console.WriteLine($"{rowCount} row(s) inserted...");
            Console.WriteLine($"{mutationCount} mutation(s) in transaction...");
    
            return mutationCount;
        }
    
        /// <summary>
        /// Sample logger that keeps a reference to the last seen commit response.
        /// Use the default logger if you only want to log the commit stats.
        /// </summary>
        public class CommitStatsSampleLogger : Logger
        {
            internal [CommitResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.CommitResponse.html) _lastCommitResponse;
    
            /// <summary>
            /// This method is called when a transaction that requested commit stats is committed.
            /// </summary>
            public override void LogCommitStats([CommitRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.CommitRequest.html) request, [CommitResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.CommitResponse.html) response)
            {
                _lastCommitResponse = response;
                base.LogCommitStats(request, response);
            }
    
            protected override void LogImpl(LogLevel level, string message, Exception exception) =>
                WriteLine(exception == null ? $"{level}: {message}" : $"{level}: {message}, Exception: {exception}");
    
            protected override void LogPerformanceEntries(IEnumerable<string> entries)
            {
                string separator = Environment.NewLine + "  ";
                WriteLine($"Performance:{separator}{string.Join(separator, entries)}");
            }
    
            private void WriteLine(string line) => Trace.TraceInformation(line);
        }
    }

### Go

The following code sets the `ReturnCommitStats` flag and prints out the mutation count when the transaction is successfully committed.
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/spanner"
    )
    
    func commitStats(w io.Writer, db string) error {
    	ctx := context.Background()
    	client, err := spanner.NewClient(ctx, db)
    	if err != nil {
    		return fmt.Errorf("commitStats.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	resp, err := client.[ReadWriteTransactionWithOptions](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Client_ReadWriteTransactionWithOptions)(ctx, func(ctx context.Context, txn *spanner.ReadWriteTransaction) error {
    		stmt := spanner.[Statement](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Statement){
    			SQL: `INSERT Singers (SingerId, FirstName, LastName)
    					VALUES (110, 'Virginia', 'Watson')`,
    		}
    		rowCount, err := txn.Update(ctx, stmt)
    		if err != nil {
    			return err
    		}
    		fmt.Fprintf(w, "%d record(s) inserted.\n", rowCount)
    		return nil
    	}, spanner.TransactionOptions{CommitOptions: spanner.[CommitOptions](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_CommitOptions){ReturnCommitStats: true}})
    	if err != nil {
    		return fmt.Errorf("commitStats.ReadWriteTransactionWithOptions: %w", err)
    	}
    	fmt.Fprintf(w, "%d mutations in transaction\n", resp.CommitStats.MutationCount)
    	return nil
    }
    

### Java
    
    
    import com.google.cloud.spanner.[CommitResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.CommitResponse.html);
    import com.google.cloud.spanner.[DatabaseClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.DatabaseClient.html);
    import com.google.cloud.spanner.[DatabaseId](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.DatabaseId.html);
    import com.google.cloud.spanner.[Mutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Mutation.html);
    import com.google.cloud.spanner.[Options](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Options.html);
    import com.google.cloud.spanner.[Spanner](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html);
    import com.google.cloud.spanner.[SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html);
    import java.util.Arrays;
    
    public class GetCommitStatsSample {
    
      static void getCommitStats() {
        // TODO(developer): Replace these variables before running the sample.
        final String projectId = "my-project";
        final String instanceId = "my-instance";
        final String databaseId = "my-database";
    
        try ([Spanner](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html) spanner =
            [SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html).newBuilder().setProjectId(projectId).build().getService()) {
          final [DatabaseClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.DatabaseClient.html) databaseClient = spanner
              .getDatabaseClient([DatabaseId](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.DatabaseId.html).of(projectId, instanceId, databaseId));
          getCommitStats(databaseClient);
        }
      }
    
      static void getCommitStats([DatabaseClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.DatabaseClient.html) databaseClient) {
        final [CommitResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.CommitResponse.html) commitResponse = databaseClient.[writeWithOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.DatabaseClient.html#com_google_cloud_spanner_DatabaseClient_writeWithOptions_java_lang_Iterable_com_google_cloud_spanner_Mutation__com_google_cloud_spanner_Options_TransactionOption____)(Arrays.asList(
            [Mutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Mutation.html).[newInsertOrUpdateBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Mutation.html#com_google_cloud_spanner_Mutation_newInsertOrUpdateBuilder_java_lang_String_)("Albums")
                .set("SingerId")
                .[to](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.ValueBinder.html#com_google_cloud_spanner_ValueBinder_to_boolean_)("1")
                .set("AlbumId")
                .[to](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.ValueBinder.html#com_google_cloud_spanner_ValueBinder_to_boolean_)("1")
                .set("MarketingBudget")
                .[to](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.ValueBinder.html#com_google_cloud_spanner_ValueBinder_to_boolean_)("200000")
                .build(),
            [Mutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Mutation.html).[newInsertOrUpdateBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Mutation.html#com_google_cloud_spanner_Mutation_newInsertOrUpdateBuilder_java_lang_String_)("Albums")
                .set("SingerId")
                .[to](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.ValueBinder.html#com_google_cloud_spanner_ValueBinder_to_boolean_)("2")
                .set("AlbumId")
                .[to](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.ValueBinder.html#com_google_cloud_spanner_ValueBinder_to_boolean_)("2")
                .set("MarketingBudget")
                .[to](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.ValueBinder.html#com_google_cloud_spanner_ValueBinder_to_boolean_)("400000")
                .build()
        ), [Options](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Options.html).[commitStats](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Options.html#com_google_cloud_spanner_Options_commitStats__)());
    
        System.out.println(
            "Updated data with " + commitResponse.[getCommitStats](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.CommitResponse.html#com_google_cloud_spanner_CommitResponse_getCommitStats__)().[getMutationCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.CommitStats.html#com_google_cloud_spanner_CommitStats_getMutationCount__)() + " mutations.");
      }
    }

### Node.js

The following code sets the `returnCommitStats` flag and returns a mutation count of 6, because we are inserting or updating 2 rows and 3 columns in each row.
    
    
    // Imports the Google Cloud client library.
    const {Spanner} = require('[@google-cloud/spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/overview.html)');
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // const projectId = 'my-project-id';
    // const instanceId = 'my-instance';
    // const databaseId = 'my-database';
    
    // Creates a client.
    const spanner = new [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)({
      projectId: projectId,
    });
    
    // Gets a reference to a Cloud Spanner instance and database.
    const instance = spanner.instance(instanceId);
    const database = instance.database(databaseId);
    
    // Instantiate Spanner table objects.
    const albumsTable = database.table('Albums');
    
    // Updates rows in the Venues table.
    try {
      const [response] = await albumsTable.upsert(
        [
          {SingerId: '1', AlbumId: '1', MarketingBudget: '200000'},
          {SingerId: '2', AlbumId: '2', MarketingBudget: '400000'},
        ],
        {returnCommitStats: true},
      );
      console.log(
        `Updated data with ${response.commitStats.mutationCount} mutations.`,
      );
    } catch (err) {
      console.error('ERROR:', err);
    } finally {
      // Close the database when finished.
      database.close();
    }

### PHP
    
    
    use Google\Cloud\Spanner\SpannerClient;
    use Google\Cloud\Spanner\Transaction;
    
    /**
     * Creates a database and tables for sample data.
     * Example:
     * ```
     * create_database($instanceId, $databaseId);
     * ```
     *
     * @param string $instanceId The Spanner instance ID.
     * @param string $databaseId The Spanner database ID.
     */
    function get_commit_stats(string $instanceId, string $databaseId): void
    {
        $spanner = new SpannerClient();
        $instance = $spanner->instance($instanceId);
        $database = $instance->database($databaseId);
    
        $commitStats = $database->runTransaction(function (Transaction $t) {
            $t->updateBatch('Albums', [
                [
                    'SingerId' => 1,
                    'AlbumId' => 1,
                    'MarketingBudget' => 200000,
                ],
                [
                    'SingerId' => 2,
                    'AlbumId' => 2,
                    'MarketingBudget' => 400000,
                ]
            ]);
            $t->commit(['returnCommitStats' => true]);
            return $t->getCommitStats();
        });
    
        print('Updated data with ' . $commitStats['mutationCount'] . ' mutations.' . PHP_EOL);
    }

### Python

Instead of returning commit statistics directly through the API, the Python client library logs them using `stdout` at level `Info`.

The following code enables commit statistics logging for all transactions by setting `database.log_commit_stats = True`. The code also implements a sample logger that keeps a reference to the last seen commit response. The `mutation_count` is then retrieved from this response and displayed.
    
    
    def log_commit_stats(instance_id, database_id):
        """Inserts sample data using DML and displays the commit statistics."""
    
        # By default, commit statistics are logged via stdout at level Info.
        # This sample uses a custom logger to access the commit statistics.
        class CommitStatsSampleLogger(logging.Logger):
            def __init__(self):
                self.last_commit_stats = None
                super().__init__("commit_stats_sample")
    
            def info(self, msg, *args, **kwargs):
                if (
                    "extra" in kwargs
                    and kwargs["extra"]
                    and "commit_stats" in kwargs["extra"]
                ):
                    self.last_commit_stats = kwargs["extra"]["commit_stats"]
                super().info(msg, *args, **kwargs)
    
        spanner_client = spanner.Client()
        instance = spanner_client.instance(instance_id)
        database = instance.database(database_id, logger=CommitStatsSampleLogger())
        database.log_commit_stats = True
    
        def insert_singers(transaction):
            row_ct = transaction.execute_update(
                "INSERT Singers (SingerId, FirstName, LastName) "
                " VALUES (110, 'Virginia', 'Watson')"
            )
    
            print("{} record(s) inserted.".format(row_ct))
    
        database.run_in_transaction(insert_singers)
        commit_stats = database.logger.last_commit_stats
        print("{} mutation(s) in transaction.".format(commit_stats.mutation_count))
    
    

### Ruby

The following code sets the `return_commit_stats` flag and returns a mutation count of 6, because we are inserting or updating 2 rows and 3 columns in each row.
    
    
    # project_id  = "Your Google Cloud project ID"
    # instance_id = "Your Spanner instance ID"
    # database_id = "Your Spanner database ID"
    
    require "google/cloud/spanner"
    
    spanner = Google::Cloud::Spanner.new project: project_id
    client  = spanner.client instance_id, database_id
    
    records = [
      { SingerId: 1, AlbumId: 1, MarketingBudget: 200_000 },
      { SingerId: 2, AlbumId: 2, MarketingBudget: 400_000 }
    ]
    commit_options = { return_commit_stats: true }
    resp = client.upsert "Albums", records, commit_options: commit_options
    puts "Updated data with #{resp.stats.mutation_count} mutations."
    

## What's next

  * [CommitStats REST reference](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/commit#commitstats).
  * [CommitStats gRPC reference](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.v1#commitstats).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
