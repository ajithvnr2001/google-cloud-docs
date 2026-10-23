---
url: https://docs.cloud.google.com/spanner/docs/samples/spanner-update-data-with-timestamp-column/
title: Mutations update data with TIMESTAMP \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:11.114820+00:00
---

# Mutations update data with TIMESTAMP  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/samples/spanner-update-data-with-timestamp-column/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Samples ](https://docs.cloud.google.com/spanner/docs/samples)



#  Mutations update data with TIMESTAMP Stay organized with collections  Save and categorize content based on your preferences. 

Update data in a table containing a TIMESTAMP column by using mutations.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Commit timestamps in GoogleSQL-dialect databases](https://docs.cloud.google.com/spanner/docs/commit-timestamp)
  * [Commit timestamps in PostgreSQL-dialect databases](https://docs.cloud.google.com/spanner/docs/commit-timestamp-postgresql)



## Code sample

### C++

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    void UpdateDataWithTimestamp(google::cloud::spanner::Client client) {
      namespace spanner = ::google::cloud::spanner;
      auto commit_result = client.Commit(spanner::Mutations{
          spanner::UpdateMutationBuilder(
              "Albums",
              {"SingerId", "AlbumId", "MarketingBudget", "LastUpdateTime"})
              .EmplaceRow(1, 1, 1000000, spanner::CommitTimestamp{})
              .EmplaceRow(2, 2, 750000, spanner::CommitTimestamp{})
              .Build()});
      if (!commit_result) throw std::move(commit_result).status();
      std::cout
          << "Update was successful [spanner_update_data_with_timestamp_column]\n";
    }

### C#

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Spanner.Data](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.html);
    using System;
    using System.Threading.Tasks;
    
    public class UpdateDataWithTimestampColumnAsyncSample
    {
        public async Task<int> UpdateDataWithTimestampColumnAsync(string projectId, string instanceId, string databaseId)
        {
            string connectionString = $"Data Source=projects/{projectId}/instances/{instanceId}/databases/{databaseId}";
            using var connection = new [SpannerConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html)(connectionString);
    
            var rowCount = 0;
            using var updateCmd1 = connection.[CreateUpdateCommand](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html#Google_Cloud_Spanner_Data_SpannerConnection_CreateUpdateCommand_System_String_Google_Cloud_Spanner_Data_SpannerParameterCollection_)("Albums", new [SpannerParameterCollection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerParameterCollection.html)
            {
                { "SingerId", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[Int64](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_Int64), 1 },
                { "AlbumId", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[Int64](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_Int64), 1 },
                { "MarketingBudget", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[Int64](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_Int64), 1000000 },
                { "LastUpdateTime", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[Timestamp](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_Timestamp), [SpannerParameter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerParameter.html).[CommitTimestamp](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerParameter.html#Google_Cloud_Spanner_Data_SpannerParameter_CommitTimestamp) },
            });
            rowCount += await updateCmd1.ExecuteNonQueryAsync();
    
            using var updateCmd2 = connection.[CreateUpdateCommand](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html#Google_Cloud_Spanner_Data_SpannerConnection_CreateUpdateCommand_System_String_Google_Cloud_Spanner_Data_SpannerParameterCollection_)("Albums", new [SpannerParameterCollection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerParameterCollection.html)
            {
                { "SingerId", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[Int64](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_Int64), 2 },
                { "AlbumId", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[Int64](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_Int64), 2 },
                { "MarketingBudget", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[Int64](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_Int64), 750000 },
                { "LastUpdateTime", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[Timestamp](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_Timestamp), [SpannerParameter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerParameter.html).[CommitTimestamp](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerParameter.html#Google_Cloud_Spanner_Data_SpannerParameter_CommitTimestamp) },
            });
            rowCount += await updateCmd2.ExecuteNonQueryAsync();
    
            Console.WriteLine("Updated data.");
            return rowCount;
        }
    }

### Go

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"io"
    
    	"cloud.google.com/go/spanner"
    )
    
    func updateWithTimestamp(w io.Writer, db string) error {
    	ctx := context.Background()
    	client, err := spanner.NewClient(ctx, db)
    	if err != nil {
    		return err
    	}
    	defer client.Close()
    
    	cols := []string{"SingerId", "AlbumId", "MarketingBudget", "LastUpdateTime"}
    	_, err = client.[Apply](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Client_Apply)(ctx, []*spanner.Mutation{
    		spanner.Update("Albums", cols, []interface{}{1, 1, 1000000, spanner.[CommitTimestamp](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_CommitTimestamp)}),
    		spanner.Update("Albums", cols, []interface{}{2, 2, 750000, spanner.[CommitTimestamp](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_CommitTimestamp)}),
    	})
    	return err
    }
    

### Java

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    static void updateWithTimestamp(DatabaseClient dbClient) {
      // Mutation can be used to update/insert/delete a single row in a table. Here we use
      // newUpdateBuilder to create update mutations.
      List<Mutation> mutations =
          Arrays.asList(
              Mutation.newUpdateBuilder("Albums")
                  .set("SingerId")
                  .to(1)
                  .set("AlbumId")
                  .to(1)
                  .set("MarketingBudget")
                  .to(1000000)
                  .set("LastUpdateTime")
                  .to(Value.COMMIT_TIMESTAMP)
                  .build(),
              Mutation.newUpdateBuilder("Albums")
                  .set("SingerId")
                  .to(2)
                  .set("AlbumId")
                  .to(2)
                  .set("MarketingBudget")
                  .to(750000)
                  .set("LastUpdateTime")
                  .to(Value.COMMIT_TIMESTAMP)
                  .build());
      // This writes all the mutations to Cloud Spanner atomically.
      dbClient.write(mutations);
    }

### Node.js

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // ...
    
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
    let database;
    try {
      // Gets a reference to a Cloud Spanner instance and database
      const instance = spanner.instance(instanceId);
      database = instance.database(databaseId);
    
      // Update a row in the Albums table
      // Note: Cloud Spanner interprets Node.js numbers as FLOAT64s, so they
      // must be converted to strings before being inserted as INT64s
      const albumsTable = database.table('Albums');
    
      const data = [
        {
          SingerId: '1',
          AlbumId: '1',
          MarketingBudget: '1000000',
          LastUpdateTime: 'spanner.commit_timestamp()',
        },
        {
          SingerId: '2',
          AlbumId: '2',
          MarketingBudget: '750000',
          LastUpdateTime: 'spanner.commit_timestamp()',
        },
      ];
    
      await albumsTable.update(data);
      console.log('Updated data.');
    } catch (err) {
      console.error('ERROR:', err);
    } finally {
      // Close the database when finished
      await database.close();
    }

### PHP

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Spanner\SpannerClient;
    
    /**
     * Updates sample data in a table with a commit timestamp column.
     *
     * Before executing this method, a new column MarketingBudget has to be added to the Albums
     * table by applying the DDL statement "ALTER TABLE Albums ADD COLUMN MarketingBudget INT64".
     *
     * In addition this update expects the LastUpdateTime column added by applying the DDL statement
     * "ALTER TABLE Albums ADD COLUMN LastUpdateTime TIMESTAMP OPTIONS (allow_commit_timestamp=true)"
     *
     * Example:
     * ```
     * update_data_with_timestamp_column($instanceId, $databaseId);
     * ```
     *
     * @param string $instanceId The Spanner instance ID.
     * @param string $databaseId The Spanner database ID.
     */
    function update_data_with_timestamp_column(string $instanceId, string $databaseId): void
    {
        $spanner = new SpannerClient();
        $instance = $spanner->instance($instanceId);
        $database = $instance->database($databaseId);
    
        $operation = $database->transaction(['singleUse' => true])
            ->updateBatch('Albums', [
                ['SingerId' => 1, 'AlbumId' => 1, 'MarketingBudget' => 1000000, 'LastUpdateTime' => $spanner->commitTimestamp()],
                ['SingerId' => 2, 'AlbumId' => 2, 'MarketingBudget' => 750000, 'LastUpdateTime' => $spanner->commitTimestamp()],
            ])
            ->commit();
    
        print('Updated data.' . PHP_EOL);
    }

### Python

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def update_data_with_timestamp(instance_id, database_id):
        """Updates Performances tables in the database with the COMMIT_TIMESTAMP
        column.
    
        This updates the `MarketingBudget` column which must be created before
        running this sample. You can add the column by running the `add_column`
        sample or by running this DDL statement against your database:
    
            ALTER TABLE Albums ADD COLUMN MarketingBudget INT64
    
        In addition this update expects the LastUpdateTime column added by
        applying this DDL statement against your database:
    
            ALTER TABLE Albums ADD COLUMN LastUpdateTime TIMESTAMP
            OPTIONS(allow_commit_timestamp=true)
        """
        spanner_client = spanner.Client()
        instance = spanner_client.instance(instance_id)
    
        database = instance.database(database_id)
    
        with database.batch() as batch:
            batch.update(
                table="Albums",
                columns=("SingerId", "AlbumId", "MarketingBudget", "LastUpdateTime"),
                values=[
                    (1, 1, 1000000, spanner.COMMIT_TIMESTAMP),
                    (2, 2, 750000, spanner.COMMIT_TIMESTAMP),
                ],
            )
    
        print("Updated data.")
    
    

### Ruby

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project_id  = "Your Google Cloud project ID"
    # instance_id = "Your Spanner instance ID"
    # database_id = "Your Spanner database ID"
    
    require "google/cloud/spanner"
    
    spanner = Google::Cloud::[Spanner](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-instance-v1/latest/Google-Cloud-Spanner.html).new project: project_id
    client  = spanner.[client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-Project.html) instance_id, database_id
    
    commit_timestamp = client.commit_timestamp
    
    client.commit do |c|
      c.update "Albums", [
        { SingerId: 1, AlbumId: 1, MarketingBudget: 100_000, LastUpdateTime: commit_timestamp },
        { SingerId: 2, AlbumId: 2, MarketingBudget: 750_000, LastUpdateTime: commit_timestamp }
      ]
    end
    
    puts "Updated data"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudspanner). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
