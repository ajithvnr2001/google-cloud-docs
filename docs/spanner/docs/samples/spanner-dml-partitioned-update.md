---
url: https://docs.cloud.google.com/spanner/docs/samples/spanner-dml-partitioned-update/
title: Bulk update with partitioned DML \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:22.158178+00:00
---

# Bulk update with partitioned DML  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/samples/spanner-dml-partitioned-update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Samples ](https://docs.cloud.google.com/spanner/docs/samples)



#  Bulk update with partitioned DML Stay organized with collections  Save and categorize content based on your preferences. 

Bulk update data by using a partitioned DML statement.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Insert, update, and delete data using data manipulation language (DML)](https://docs.cloud.google.com/spanner/docs/dml-tasks)
  * [Partitioned Data Manipulation Language](https://docs.cloud.google.com/spanner/docs/dml-partitioned)
  * [Transactions overview](https://docs.cloud.google.com/spanner/docs/transactions)



## Code sample

### C++

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    void DmlPartitionedUpdate(google::cloud::spanner::Client client) {
      namespace spanner = ::google::cloud::spanner;
      auto result = client.ExecutePartitionedDml(
          spanner::SqlStatement("UPDATE Albums SET MarketingBudget = 100000"
                                "  WHERE SingerId > 1"));
      if (!result) throw std::move(result).status();
      std::cout << "Updated at least " << result->row_count_lower_bound
                << " row(s) [spanner_dml_partitioned_update]\n";
    }

### C#

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Spanner.Data](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.html);
    using System;
    using System.Threading.Tasks;
    
    public class UpdateUsingPartitionedDmlCoreAsyncSample
    {
        public async Task<long> UpdateUsingPartitionedDmlCoreAsync(string projectId, string instanceId, string databaseId)
        {
            string connectionString = $"Data Source=projects/{projectId}/instances/{instanceId}/databases/{databaseId}";
    
            using var connection = new [SpannerConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html)(connectionString);
            await connection.[OpenAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html#Google_Cloud_Spanner_Data_SpannerConnection_OpenAsync_Google_Cloud_Spanner_Data_SpannerTransactionCreationOptions_Google_Cloud_Spanner_Data_SpannerTransactionOptions_System_Threading_CancellationToken_)();
    
            using var cmd = connection.[CreateDmlCommand](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html#Google_Cloud_Spanner_Data_SpannerConnection_CreateDmlCommand_System_String_Google_Cloud_Spanner_Data_SpannerParameterCollection_)("UPDATE Albums SET MarketingBudget = 100000 WHERE SingerId > 1");
            long rowCount = await cmd.[ExecutePartitionedUpdateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerCommand.html#Google_Cloud_Spanner_Data_SpannerCommand_ExecutePartitionedUpdateAsync_System_Threading_CancellationToken_)();
    
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
    
    func updateUsingPartitionedDML(w io.Writer, db string) error {
    	ctx := context.Background()
    	client, err := spanner.NewClient(ctx, db)
    	if err != nil {
    		return err
    	}
    	defer client.Close()
    
    	stmt := spanner.[Statement](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Statement){SQL: "UPDATE Albums SET MarketingBudget = 100000 WHERE SingerId > 1"}
    	rowCount, err := client.PartitionedUpdate(ctx, stmt)
    	if err != nil {
    		return err
    	}
    	fmt.Fprintf(w, "%d record(s) updated.\n", rowCount)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    static void updateUsingPartitionedDml(DatabaseClient dbClient) {
      String sql = "UPDATE Albums SET MarketingBudget = 100000 WHERE SingerId > 1";
      long rowCount = dbClient.executePartitionedUpdate(Statement.of(sql));
      System.out.printf("%d records updated.\n", rowCount);
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
      const [rowCount] = await database.[runPartitionedUpdate](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/database.html)({
        sql: 'UPDATE Albums SET MarketingBudget = 100000 WHERE SingerId > 1',
      });
      console.log(`Successfully updated ${rowCount} records.`);
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
    
    /**
     * Updates sample data in the database by partition with a DML statement.
     *
     * This updates the `MarketingBudget` column which must be created before
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
    function update_data_with_partitioned_dml(string $instanceId, string $databaseId): void
    {
        $spanner = new SpannerClient();
        $instance = $spanner->instance($instanceId);
        $database = $instance->database($databaseId);
    
        $rowCount = $database->executePartitionedUpdate(
            'UPDATE Albums SET MarketingBudget = 100000 WHERE SingerId > 1'
        );
    
        printf('Updated %d row(s).' . PHP_EOL, $rowCount);
    }

### Python

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"
    
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)
    
    row_ct = database.execute_partitioned_dml(
        "UPDATE Albums SET MarketingBudget = 100000 WHERE SingerId > 1"
    )
    
    print("{} records updated.".format(row_ct))

### Ruby

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project_id  = "Your Google Cloud project ID"
    # instance_id = "Your Spanner instance ID"
    # database_id = "Your Spanner database ID"
    
    require "google/cloud/spanner"
    
    spanner = Google::Cloud::[Spanner](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-instance-v1/latest/Google-Cloud-Spanner.html).new project: project_id
    client  = spanner.[client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-Project.html) instance_id, database_id
    
    row_count = client.[execute_partition_update](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-Client.html)(
      "UPDATE Albums SET MarketingBudget = 100000 WHERE SingerId > 1"
    )
    
    puts "#{row_count} records updated."

### Rust
    
    
    use google_cloud_spanner::client::DatabaseClient;
    use google_cloud_spanner::statement::Statement;
    
    pub async fn sample(client: &DatabaseClient) -> anyhow::Result<()> {
        let transaction = client.partitioned_dml_transaction().build();
        let statement =
            Statement::builder("UPDATE Albums SET MarketingBudget = 100000 WHERE SingerId > 1").build();
    
        let row_count = transaction.execute_update(statement).await?;
        println!("{row_count} records updated.");
        Ok(())
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudspanner). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
