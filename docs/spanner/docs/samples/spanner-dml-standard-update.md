---
url: https://docs.cloud.google.com/spanner/docs/samples/spanner-dml-standard-update/
title: DML update data \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:20.294302+00:00
---

# DML update data  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/samples/spanner-dml-standard-update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Samples ](https://docs.cloud.google.com/spanner/docs/samples)



#  DML update data Stay organized with collections  Save and categorize content based on your preferences. 

Update data using DML.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Insert, update, and delete data using data manipulation language (DML)](https://docs.cloud.google.com/spanner/docs/dml-tasks)



## Code sample

### C++

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    void DmlStandardUpdate(google::cloud::spanner::Client client) {
      //! [commit-with-mutator]
      using ::google::cloud::StatusOr;
      namespace spanner = ::google::cloud::spanner;
      auto commit_result = client.Commit(
          [&client](spanner::Transaction txn) -> StatusOr<spanner::Mutations> {
            auto update = client.ExecuteDml(
                std::move(txn),
                spanner::SqlStatement(
                    "UPDATE Albums SET MarketingBudget = MarketingBudget * 2"
                    "  WHERE SingerId = 1 AND AlbumId = 1"));
            if (!update) return std::move(update).status();
            return spanner::Mutations{};
          });
      if (!commit_result) throw std::move(commit_result).status();
      //! [commit-with-mutator]
      std::cout << "Update was successful [spanner_dml_standard_update]\n";
    }

### C#

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Spanner.Data](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.html);
    using System;
    using System.Threading.Tasks;
    
    public class UpdateUsingDmlCoreAsyncSample
    {
        public async Task<int> UpdateUsingDmlCoreAsync(string projectId, string instanceId, string databaseId)
        {
            string connectionString = $"Data Source=projects/{projectId}/instances/{instanceId}/databases/{databaseId}";
    
            using var connection = new [SpannerConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html)(connectionString);
            await connection.[OpenAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html#Google_Cloud_Spanner_Data_SpannerConnection_OpenAsync_Google_Cloud_Spanner_Data_SpannerTransactionCreationOptions_Google_Cloud_Spanner_Data_SpannerTransactionOptions_System_Threading_CancellationToken_)();
    
            using var cmd = connection.[CreateDmlCommand](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html#Google_Cloud_Spanner_Data_SpannerConnection_CreateDmlCommand_System_String_Google_Cloud_Spanner_Data_SpannerParameterCollection_)("UPDATE Albums SET MarketingBudget = MarketingBudget * 2 WHERE SingerId = 1 and AlbumId = 1");
            int rowCount = await cmd.ExecuteNonQueryAsync();
    
            Console.WriteLine($"{rowCount} row(s) updated...");
            return rowCount;
        }
    }

### Go

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/spanner"
    )
    
    func updateUsingDML(w io.Writer, db string) error {
    	ctx := context.Background()
    	client, err := spanner.NewClient(ctx, db)
    	if err != nil {
    		return err
    	}
    	defer client.Close()
    
    	_, err = client.ReadWriteTransaction(ctx, func(ctx context.Context, txn *spanner.ReadWriteTransaction) error {
    		stmt := spanner.[Statement](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Statement){
    			SQL: `UPDATE Albums
    				SET MarketingBudget = MarketingBudget * 2
    				WHERE SingerId = 1 and AlbumId = 1`,
    		}
    		rowCount, err := txn.Update(ctx, stmt)
    		if err != nil {
    			return err
    		}
    		fmt.Fprintf(w, "%d record(s) updated.\n", rowCount)
    		return nil
    	})
    	return err
    }
    

### Java

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    static void updateUsingDml(DatabaseClient dbClient) {
      dbClient
          .readWriteTransaction()
          .run(transaction -> {
            String sql =
                "UPDATE Albums "
                    + "SET MarketingBudget = MarketingBudget * 2 "
                    + "WHERE SingerId = 1 and AlbumId = 1";
            long rowCount = transaction.executeUpdate(Statement.of(sql));
            System.out.printf("%d record updated.\n", rowCount);
            return null;
          });
    }

### Node.js

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const {Spanner} = require('[@google-cloud/spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/overview.html)');
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // const projectId = 'my-project-id';
    // const instanceId = 'my-instance';
    // const databaseId = 'my-database';
    
    // Creates a client
    const spanner = new [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)({
      projectId: projectId,
    });
    
    // Gets a reference to a Cloud Spanner instance and database
    const instance = spanner.instance(instanceId);
    const database = instance.database(databaseId);
    
    try {
      await database.[runTransactionAsync](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/database.html)(async transaction => {
        const [rowCount] = await transaction.runUpdate({
          sql: `UPDATE Albums SET MarketingBudget = MarketingBudget * 2
            WHERE SingerId = 1 and AlbumId = 1`,
        });
    
        console.log(`Successfully updated ${rowCount} record.`);
        await transaction.commit();
      });
    } catch (err) {
      console.error('ERROR:', err);
    } finally {
      // Close the database when finished.
      await database.close();
    }

### PHP

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Spanner\SpannerClient;
    use Google\Cloud\Spanner\Transaction;
    
    /**
     * Updates sample data in the database with a DML statement.
     *
     * This requires the `MarketingBudget` column which must be created before
     * running this sample. You can add the column by running the `add_column`
     * sample or by running this DDL statement against your database:
     *
     *     ALTER TABLE Albums ADD COLUMN MarketingBudget INT64
     *
     * Example:
     * ```
     * update_data($instanceId, $databaseId);
     * ```
     *
     * @param string $instanceId The Spanner instance ID.
     * @param string $databaseId The Spanner database ID.
     */
    function update_data_with_dml(string $instanceId, string $databaseId): void
    {
        $spanner = new SpannerClient();
        $instance = $spanner->instance($instanceId);
        $database = $instance->database($databaseId);
    
        $database->runTransaction(function (Transaction $t) {
            $rowCount = $t->executeUpdate(
                'UPDATE Albums '
                . 'SET MarketingBudget = MarketingBudget * 2 '
                . 'WHERE SingerId = 1 and AlbumId = 1');
            $t->commit();
            printf('Updated %d row(s).' . PHP_EOL, $rowCount);
        });
    }

### Python

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"
    
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)
    
    def update_albums(transaction):
        row_ct = transaction.execute_update(
            "UPDATE Albums "
            "SET MarketingBudget = MarketingBudget * 2 "
            "WHERE SingerId = 1 and AlbumId = 1"
        )
    
        print("{} record(s) updated.".format(row_ct))
    
    database.run_in_transaction(update_albums)

### Ruby

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project_id  = "Your Google Cloud project ID"
    # instance_id = "Your Spanner instance ID"
    # database_id = "Your Spanner database ID"
    
    require "google/cloud/spanner"
    
    spanner = Google::Cloud::[Spanner](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-instance-v1/latest/Google-Cloud-Spanner.html).new project: project_id
    client  = spanner.[client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-Project.html) instance_id, database_id
    row_count = 0
    
    client.transaction do |transaction|
      row_count = transaction.[execute_update](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-Transaction.html)(
        "UPDATE Albums
         SET MarketingBudget = MarketingBudget * 2
         WHERE SingerId = 1 and AlbumId = 1"
      )
    end
    
    puts "#{row_count} record updated."

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudspanner). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
