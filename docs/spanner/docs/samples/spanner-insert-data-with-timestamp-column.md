---
url: https://docs.cloud.google.com/spanner/docs/samples/spanner-insert-data-with-timestamp-column/
title: Mutations write data with TIMESTAMP column \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:24.617585+00:00
---

# Mutations write data with TIMESTAMP column  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/samples/spanner-insert-data-with-timestamp-column/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Samples ](https://docs.cloud.google.com/spanner/docs/samples)



#  Mutations write data with TIMESTAMP column Stay organized with collections  Save and categorize content based on your preferences. 

Write data into a table containing a TIMESTAMP column by using mutations.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Commit timestamps in PostgreSQL-dialect databases](https://docs.cloud.google.com/spanner/docs/commit-timestamp-postgresql)



## Code sample

### C++

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    void InsertDataWithTimestamp(google::cloud::spanner::Client client) {
      namespace spanner = ::google::cloud::spanner;
      auto commit_result = client.Commit(spanner::Mutations{
          spanner::InsertOrUpdateMutationBuilder(
              "Performances",
              {"SingerId", "VenueId", "EventDate", "Revenue", "LastUpdateTime"})
              .EmplaceRow(1, 4, absl::CivilDay(2017, 10, 5), 11000,
                          spanner::CommitTimestamp{})
              .EmplaceRow(1, 19, absl::CivilDay(2017, 11, 2), 15000,
                          spanner::CommitTimestamp{})
              .EmplaceRow(2, 42, absl::CivilDay(2017, 12, 23), 7000,
                          spanner::CommitTimestamp{})
              .Build()});
      if (!commit_result) throw std::move(commit_result).status();
      std::cout
          << "Update was successful [spanner_insert_data_with_timestamp_column]\n";
    }

### C#

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Spanner.Data](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.html);
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Threading.Tasks;
    
    public class WriteDataWithTimestampAsyncSample
    {
        public class Performance
        {
            public int SingerId { get; set; }
            public int VenueId { get; set; }
            public DateTime EventDate { get; set; }
            public long Revenue { get; set; }
        }
    
        public async Task<int> WriteDataWithTimestampAsync(string projectId, string instanceId, string databaseId)
        {
            string connectionString = $"Data Source=projects/{projectId}/instances/{instanceId}/databases/{databaseId}";
    
            List<Performance> performances = new List<Performance>
            {
                new Performance { SingerId = 1, VenueId = 4, EventDate = DateTime.Parse("2017-10-05"), Revenue = 11000 },
                new Performance { SingerId = 1, VenueId = 19, EventDate = DateTime.Parse("2017-11-02"), Revenue = 15000 },
                new Performance { SingerId = 2, VenueId = 42, EventDate = DateTime.Parse("2017-12-23"), Revenue = 7000 },
            };
            // Create connection to Cloud Spanner.
            using var connection = new [SpannerConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html)(connectionString);
            await connection.[OpenAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html#Google_Cloud_Spanner_Data_SpannerConnection_OpenAsync_Google_Cloud_Spanner_Data_SpannerTransactionCreationOptions_Google_Cloud_Spanner_Data_SpannerTransactionOptions_System_Threading_CancellationToken_)();
    
            // Insert rows into the Performances table.
            var rowCountAarray = await Task.WhenAll(performances.[Select](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerCommandType.html#Google_Cloud_Spanner_Data_SpannerCommandType_Select)(performance =>
            {
                var cmd = connection.[CreateInsertCommand](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html#Google_Cloud_Spanner_Data_SpannerConnection_CreateInsertCommand_System_String_Google_Cloud_Spanner_Data_SpannerParameterCollection_)("Performances", new [SpannerParameterCollection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerParameterCollection.html)
                {
                    { "SingerId", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[Int64](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_Int64), performance.SingerId },
                    { "VenueId", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[Int64](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_Int64), performance.VenueId },
                    { "EventDate", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[Date](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_Date), performance.EventDate },
                    { "Revenue", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[Int64](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_Int64), performance.Revenue },
                    { "LastUpdateTime", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[Timestamp](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_Timestamp), [SpannerParameter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerParameter.html).[CommitTimestamp](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerParameter.html#Google_Cloud_Spanner_Data_SpannerParameter_CommitTimestamp) },
                });
                return cmd.ExecuteNonQueryAsync();
            }));
            return rowCountAarray.Sum();
        }
    }

### Go

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    
    	"cloud.google.com/go/spanner"
    )
    
    func writeWithTimestamp(db string) error {
    	ctx := context.Background()
    
    	client, err := spanner.NewClient(ctx, db)
    	if err != nil {
    		return err
    	}
    	defer client.Close()
    
    	performanceColumns := []string{"SingerId", "VenueId", "EventDate", "Revenue", "LastUpdateTime"}
    	m := []*spanner.Mutation{
    		spanner.[InsertOrUpdate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Mutation_InsertOrUpdate)("Performances", performanceColumns, []interface{}{1, 4, "2017-10-05", 11000, spanner.[CommitTimestamp](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_CommitTimestamp)}),
    		spanner.[InsertOrUpdate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Mutation_InsertOrUpdate)("Performances", performanceColumns, []interface{}{1, 19, "2017-11-02", 15000, spanner.[CommitTimestamp](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_CommitTimestamp)}),
    		spanner.[InsertOrUpdate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Mutation_InsertOrUpdate)("Performances", performanceColumns, []interface{}{2, 42, "2017-12-23", 7000, spanner.[CommitTimestamp](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_CommitTimestamp)}),
    	}
    	_, err = client.[Apply](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Client_Apply)(ctx, m)
    	return err
    }
    

### Java

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    static final List<Performance> PERFORMANCES =
        Arrays.asList(
            new Performance(1, 4, "2017-10-05", 11000),
            new Performance(1, 19, "2017-11-02", 15000),
            new Performance(2, 42, "2017-12-23", 7000));
    static void writeExampleDataWithTimestamp(DatabaseClient dbClient) {
      List<Mutation> mutations = new ArrayList<>();
      for (Performance performance : PERFORMANCES) {
        mutations.add(
            Mutation.newInsertBuilder("Performances")
                .set("SingerId")
                .to(performance.singerId)
                .set("VenueId")
                .to(performance.venueId)
                .set("EventDate")
                .to(performance.eventDate)
                .set("Revenue")
                .to(performance.revenue)
                .set("LastUpdateTime")
                .to(Value.COMMIT_TIMESTAMP)
                .build());
      }
      dbClient.write(mutations);
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
    let database;
    try {
      // Gets a reference to a Cloud Spanner instance and database
      const instance = spanner.instance(instanceId);
      database = instance.database(databaseId);
    
      // Instantiate Spanner table objects
      const performancesTable = database.table('Performances');
    
      const data = [
        {
          SingerId: '1',
          VenueId: '4',
          EventDate: '2017-10-05',
          Revenue: '11000',
          LastUpdateTime: 'spanner.commit_timestamp()',
        },
        {
          SingerId: '1',
          VenueId: '19',
          EventDate: '2017-11-02',
          Revenue: '15000',
          LastUpdateTime: 'spanner.commit_timestamp()',
        },
        {
          SingerId: '2',
          VenueId: '42',
          EventDate: '2017-12-23',
          Revenue: '7000',
          LastUpdateTime: 'spanner.commit_timestamp()',
        },
      ];
    
      // Inserts rows into the Singers table
      // Note: Cloud Spanner interprets Node.js numbers as FLOAT64s, so
      // they must be converted to strings before being inserted as INT64s
      await performancesTable.insert(data);
      console.log('Inserted data.');
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
     * Inserts sample data into a table with a commit timestamp column.
     *
     * The database and table must already exist and can be created using
     * `create_table_with_timestamp_column`.
     * Example:
     * ```
     * insert_data_with_timestamp_column($instanceId, $databaseId);
     * ```
     *
     * @param string $instanceId The Spanner instance ID.
     * @param string $databaseId The Spanner database ID.
     */
    function insert_data_with_timestamp_column(string $instanceId, string $databaseId): void
    {
        $spanner = new SpannerClient();
        $instance = $spanner->instance($instanceId);
        $database = $instance->database($databaseId);
    
        $operation = $database->transaction(['singleUse' => true])
            ->insertBatch('Performances', [
                ['SingerId' => 1, 'VenueId' => 4, 'EventDate' => '2017-10-05', 'Revenue' => 11000, 'LastUpdateTime' => $spanner->commitTimestamp()],
                ['SingerId' => 1, 'VenueId' => 19, 'EventDate' => '2017-11-02', 'Revenue' => 15000, 'LastUpdateTime' => $spanner->commitTimestamp()],
                ['SingerId' => 2, 'VenueId' => 42, 'EventDate' => '2017-12-23', 'Revenue' => 7000, 'LastUpdateTime' => $spanner->commitTimestamp()],
            ])
            ->commit();
    
        print('Inserted data.' . PHP_EOL);
    }

### Python

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def insert_data_with_timestamp(instance_id, database_id):
        """Inserts data with a COMMIT_TIMESTAMP field into a table."""
    
        spanner_client = spanner.Client()
        instance = spanner_client.instance(instance_id)
    
        database = instance.database(database_id)
    
        with database.batch() as batch:
            batch.insert(
                table="Performances",
                columns=("SingerId", "VenueId", "EventDate", "Revenue", "LastUpdateTime"),
                values=[
                    (1, 4, "2017-10-05", 11000, spanner.COMMIT_TIMESTAMP),
                    (1, 19, "2017-11-02", 15000, spanner.COMMIT_TIMESTAMP),
                    (2, 42, "2017-12-23", 7000, spanner.COMMIT_TIMESTAMP),
                ],
            )
    
        print("Inserted data.")
    
    

### Ruby

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project_id  = "Your Google Cloud project ID"
    # instance_id = "Your Spanner instance ID"
    # database_id = "Your Spanner database ID"
    
    require "google/cloud/spanner"
    
    spanner = Google::Cloud::[Spanner](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-instance-v1/latest/Google-Cloud-Spanner.html).new project: project_id
    client  = spanner.[client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-Project.html) instance_id, database_id
    
    # Get commit_timestamp
    commit_timestamp = client.commit_timestamp
    
    client.commit do |c|
      c.insert "Performances", [
        { SingerId: 1, VenueId: 4, EventDate: "2017-10-05", Revenue: 11_000, LastUpdateTime: commit_timestamp },
        { SingerId: 1, VenueId: 19, EventDate: "2017-11-02", Revenue: 15_000, LastUpdateTime: commit_timestamp },
        { SingerId: 2, VenueId: 42, EventDate: "2017-12-23", Revenue: 7000, LastUpdateTime: commit_timestamp }
      ]
    end
    
    puts "Inserted data"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudspanner). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
