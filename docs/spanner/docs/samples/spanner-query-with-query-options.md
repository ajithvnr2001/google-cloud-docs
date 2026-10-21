---
url: https://docs.cloud.google.com/spanner/docs/samples/spanner-query-with-query-options/
title: Query with query options \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:30:09.101761+00:00
---

# Query with query options  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/samples/spanner-query-with-query-options/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Samples ](https://docs.cloud.google.com/spanner/docs/samples)



#  Query with query options Stay organized with collections  Save and categorize content based on your preferences. 

Specify query options.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Manage the query optimizer](https://docs.cloud.google.com/spanner/docs/query-optimizer/manage-query-optimizer)



## Code sample

### C++

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    void QueryWithQueryOptions(google::cloud::spanner::Client client) {
      namespace spanner = ::google::cloud::spanner;
      auto sql = spanner::SqlStatement("SELECT SingerId, FirstName FROM Singers");
      auto opts =
          google::cloud::Options{}
              .set<spanner::QueryOptimizerVersionOption>("1")
              .set<spanner::QueryOptimizerStatisticsPackageOption>("latest");
      auto rows = client.ExecuteQuery(std::move(sql), std::move(opts));
    
      using RowType = std::tuple<std::int64_t, std::string>;
      for (auto& row : spanner::StreamOf<RowType>(rows)) {
        if (!row) throw std::move(row).status();
        std::cout << "SingerId: " << std::get<0>(*row) << "\t";
        std::cout << "FirstName: " << std::get<1>(*row) << "\n";
      }
      std::cout << "Read completed for [spanner_query_with_query_options]\n";
    }

### C#

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Spanner.Data](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.html);
    using System.Collections.Generic;
    using System.Threading.Tasks;
    
    public class RunCommandWithQueryOptionsAsyncSample
    {
        public class Album
        {
            public int SingerId { get; set; }
            public int AlbumId { get; set; }
            public string AlbumTitle { get; set; }
        }
    
        public async Task<List<Album>> RunCommandWithQueryOptionsAsync(string projectId, string instanceId, string databaseId)
        {
            var connectionString = $"Data Source=projects/{projectId}/instances/{instanceId}/databases/{databaseId}";
            using var connection = new [SpannerConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html)(connectionString);
            using var cmd = connection.[CreateSelectCommand](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html#Google_Cloud_Spanner_Data_SpannerConnection_CreateSelectCommand_System_String_Google_Cloud_Spanner_Data_SpannerParameterCollection_)("SELECT SingerId, AlbumId, AlbumTitle FROM Albums");
    
            cmd.[QueryOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.QueryOptions.html) = [QueryOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.QueryOptions.html).[Empty](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.QueryOptions.html#Google_Cloud_Spanner_Data_QueryOptions_Empty)
                .[WithOptimizerVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.QueryOptions.html#Google_Cloud_Spanner_Data_QueryOptions_WithOptimizerVersion_System_String_)("1")
                // The list of available statistics packages for the database can
                // be found by querying the "INFORMATION_SCHEMA.SPANNER_STATISTICS"
                // table.
                .[WithOptimizerStatisticsPackage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.QueryOptions.html#Google_Cloud_Spanner_Data_QueryOptions_WithOptimizerStatisticsPackage_System_String_)("latest");
            var albums = new List<Album>();
            using var reader = await cmd.[ExecuteReaderAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerCommand.html#Google_Cloud_Spanner_Data_SpannerCommand_ExecuteReaderAsync)();
            while (await reader.[ReadAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDataReader.html#Google_Cloud_Spanner_Data_SpannerDataReader_ReadAsync_System_Threading_CancellationToken_)())
            {
                albums.Add(new Album()
                {
                    AlbumId = reader.GetFieldValue<int>("AlbumId"),
                    SingerId = reader.GetFieldValue<int>("SingerId"),
                    AlbumTitle = reader.GetFieldValue<string>("AlbumTitle")
                });
            }
            return albums;
        }
    }

### Go

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/spanner"
    	sppb "cloud.google.com/go/spanner/apiv1/spannerpb"
    	"google.golang.org/api/iterator"
    )
    
    func queryWithQueryOptions(w io.Writer, db string) error {
    	ctx := context.Background()
    	client, err := spanner.NewClient(ctx, db)
    	if err != nil {
    		return err
    	}
    	defer client.Close()
    
    	stmt := spanner.[Statement](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Statement){SQL: `SELECT VenueId, VenueName, LastUpdateTime FROM Venues`}
    	queryOptions := spanner.[QueryOptions](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_QueryOptions){
    		Options: &sppb.ExecuteSqlRequest_QueryOptions{
    			OptimizerVersion: "1",
    			// The list of available statistics packages can be found by
    			// querying the "INFORMATION_SCHEMA.SPANNER_STATISTICS" table.
    			OptimizerStatisticsPackage: "latest",
    		},
    	}
    	iter := client.[Single](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Client_Single)().QueryWithOptions(ctx, stmt, queryOptions)
    	defer iter.Stop()
    	for {
    		row, err := iter.Next()
    		if err == iterator.Done {
    			return nil
    		}
    		if err != nil {
    			return err
    		}
    		var venueID int64
    		var venueName string
    		var lastUpdateTime time.Time
    		if err := row.[Columns](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Row_Columns)(&venueID, &venueName, &lastUpdateTime); err != nil {
    			return err
    		}
    		fmt.Fprintf(w, "%d %s %s\n", venueID, venueName, lastUpdateTime)
    	}
    }
    

### Java

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    static void queryWithQueryOptions(DatabaseClient dbClient) {
      try (ResultSet resultSet =
          dbClient
              .singleUse()
              .executeQuery(
                  Statement
                      .newBuilder("SELECT SingerId, AlbumId, AlbumTitle FROM Albums")
                      .withQueryOptions(QueryOptions
                          .newBuilder()
                          .setOptimizerVersion("1")
                          // The list of available statistics packages can be found by querying the
                          // "INFORMATION_SCHEMA.SPANNER_STATISTICS" table.
                          .setOptimizerStatisticsPackage("latest")
                          .build())
                      .build())) {
        while (resultSet.next()) {
          System.out.printf(
              "%d %d %s\n", resultSet.getLong(0), resultSet.getLong(1), resultSet.getString(2));
        }
      }
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
    
      const query = {
        sql: `SELECT AlbumId, AlbumTitle, MarketingBudget
            FROM Albums
            ORDER BY AlbumTitle`,
        queryOptions: {
          optimizerVersion: 'latest',
          // The list of available statistics packages can be found by querying the
          // "INFORMATION_SCHEMA.SPANNER_STATISTICS" table.
          optimizerStatisticsPackage: 'latest',
        },
      };
    
      // Queries rows from the Albums table
      const [rows] = await database.run(query);
    
      rows.forEach(row => {
        const json = row.toJSON();
        const marketingBudget = json.MarketingBudget
          ? json.MarketingBudget
          : null; // This value is nullable
        console.log(
          `AlbumId: ${json.AlbumId}, AlbumTitle: ${json.AlbumTitle}, MarketingBudget: ${marketingBudget}`
        );
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
    use Google\Cloud\Spanner\Database;
    
    /**
     * Queries sample data using SQL with query options.
     * Example:
     * ```
     * query_data_with_query_options($instanceId, $databaseId);
     * ```
     *
     * @param string $instanceId The Spanner instance ID.
     * @param string $databaseId The Spanner database ID.
     */
    function query_data_with_query_options(string $instanceId, string $databaseId): void
    {
        $spanner = new SpannerClient();
        $instance = $spanner->instance($instanceId);
        $database = $instance->database($databaseId);
    
        $results = $database->execute(
            'SELECT VenueId, VenueName, LastUpdateTime FROM Venues',
            [
                'queryOptions' => [
                    'optimizerVersion' => '1',
                    // Pin the statistics package to the latest version just for
                    // this query.
                    'optimizerStatisticsPackage' => 'latest'
                ]
            ]
        );
    
        foreach ($results as $row) {
            printf('VenueId: %s, VenueName: %s, LastUpdateTime: %s' . PHP_EOL,
                $row['VenueId'], $row['VenueName'], $row['LastUpdateTime']);
        }
    }

### Python

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)
    
    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            "SELECT VenueId, VenueName, LastUpdateTime FROM Venues",
            query_options={
                "optimizer_version": "1",
                "optimizer_statistics_package": "latest",
            },
        )
    
        for row in results:
            print("VenueId: {}, VenueName: {}, LastUpdateTime: {}".format(*row))

### Ruby

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project_id  = "Your Google Cloud project ID"
    # instance_id = "Your Spanner instance ID"
    # database_id = "Your Spanner database ID"
    
    require "google/cloud/spanner"
    
    spanner = Google::Cloud::[Spanner](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-instance-v1/latest/Google-Cloud-Spanner.html).new project: project_id
    client  = spanner.[client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-Project.html) instance_id, database_id
    
    sql_query = "SELECT VenueId, VenueName, LastUpdateTime FROM Venues"
    query_options = {
      optimizer_version: "1",
      # The list of available statistics packagebs can be
      # found by querying the "INFORMATION_SCHEMA.SPANNER_STATISTICS"
      # table.
      optimizer_statistics_package: "latest"
    }
    
    client.execute(sql_query, query_options: query_options).rows.[each](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-BatchWriteResults.html) do |row|
      puts "#{row[:VenueId]} #{row[:VenueName]} #{row[:LastUpdateTime]}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudspanner). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
