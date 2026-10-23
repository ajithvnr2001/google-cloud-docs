---
url: https://docs.cloud.google.com/spanner/docs/samples/spanner-create-client-with-query-options/
title: Create client with query options \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:31:21.214005+00:00
---

# Create client with query options  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/samples/spanner-create-client-with-query-options/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Samples ](https://docs.cloud.google.com/spanner/docs/samples)



#  Create client with query options Stay organized with collections  Save and categorize content based on your preferences. 

Create a client with query options. The client can then be used to read, write, and run transactions.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Manage the query optimizer](https://docs.cloud.google.com/spanner/docs/query-optimizer/manage-query-optimizer)



## Code sample

### C++

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace spanner = ::google::cloud::spanner;
    spanner::Client client(
        spanner::MakeConnection(db),
        google::cloud::Options{}
            .set<spanner::QueryOptimizerVersionOption>("1")
            .set<spanner::QueryOptimizerStatisticsPackageOption>(
                "auto_20191128_14_47_22UTC"));

### C#

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Spanner.Data](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.html);
    using System.Collections.Generic;
    using System.Threading.Tasks;
    
    public class CreateConnectionWithQueryOptionsAsyncSample
    {
        public class Album
        {
            public int AlbumId { get; set; }
            public int SingerId { get; set; }
            public string AlbumTitle { get; set; }
        }
    
        public async Task<List<Album>> CreateConnectionWithQueryOptionsAsync(string projectId, string instanceId, string databaseId)
        {
            string connectionString = $"Data Source=projects/{projectId}/instances/{instanceId}/databases/{databaseId}";
    
            using var connection = new [SpannerConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html)(connectionString)
            {
                // Set query options on the connection.
                QueryOptions = [QueryOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.QueryOptions.html).[Empty](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.QueryOptions.html#Google_Cloud_Spanner_Data_QueryOptions_Empty)
                    .[WithOptimizerVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.QueryOptions.html#Google_Cloud_Spanner_Data_QueryOptions_WithOptimizerVersion_System_String_)("1")
                    // The list of available statistics packages for the database can
                    // be found by querying the "INFORMATION_SCHEMA.SPANNER_STATISTICS"
                    // table.
                    .[WithOptimizerStatisticsPackage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.QueryOptions.html#Google_Cloud_Spanner_Data_QueryOptions_WithOptimizerStatisticsPackage_System_String_)("latest")
            };
    
            var albums = new List<Album>();
            var cmd = connection.[CreateSelectCommand](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html#Google_Cloud_Spanner_Data_SpannerConnection_CreateSelectCommand_System_String_Google_Cloud_Spanner_Data_SpannerParameterCollection_)("SELECT SingerId, AlbumId, AlbumTitle FROM Albums");
            using var reader = await cmd.[ExecuteReaderAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerCommand.html#Google_Cloud_Spanner_Data_SpannerCommand_ExecuteReaderAsync)();
            while (await reader.[ReadAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDataReader.html#Google_Cloud_Spanner_Data_SpannerDataReader_ReadAsync_System_Threading_CancellationToken_)())
            {
                albums.Add(new Album
                {
                    SingerId = reader.GetFieldValue<int>("SingerId"),
                    AlbumId = reader.GetFieldValue<int>("AlbumId"),
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
    
    func createClientWithQueryOptions(w io.Writer, database string) error {
    	ctx := context.Background()
    	queryOptions := spanner.[QueryOptions](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_QueryOptions){
    		Options: &sppb.ExecuteSqlRequest_QueryOptions{
    			OptimizerVersion: "1",
    			// The list of available statistics packages can be found by
    			// querying the "INFORMATION_SCHEMA.SPANNER_STATISTICS" table.
    			OptimizerStatisticsPackage: "latest",
    		},
    	}
    	client, err := spanner.[NewClientWithConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Client_NewClientWithConfig)(
    		ctx, database, spanner.[ClientConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_ClientConfig){QueryOptions: queryOptions},
    	)
    	if err != nil {
    		return err
    	}
    	defer client.Close()
    
    	stmt := spanner.[Statement](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Statement){SQL: `SELECT VenueId, VenueName, LastUpdateTime FROM Venues`}
    	iter := client.[Single](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Client_Single)().Query(ctx, stmt)
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
    
    
    static void clientWithQueryOptions(DatabaseId db) {
      SpannerOptions options =
          SpannerOptions.newBuilder()
              .setDefaultQueryOptions(
                  db, QueryOptions
                      .newBuilder()
                      .setOptimizerVersion("1")
                      // The list of available statistics packages can be found by querying the
                      // "INFORMATION_SCHEMA.SPANNER_STATISTICS" table.
                      .setOptimizerStatisticsPackage("latest")
                      .build())
              .build();
      Spanner spanner = options.getService();
      DatabaseClient dbClient = spanner.getDatabaseClient(db);
      try (ResultSet resultSet =
          dbClient
              .singleUse()
              .executeQuery(Statement.of("SELECT SingerId, AlbumId, AlbumTitle FROM Albums"))) {
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
      database = instance.database(
        databaseId,
        {},
        {
          optimizerVersion: '1',
          // The list of available statistics packages can be found by querying the
          // "INFORMATION_SCHEMA.SPANNER_STATISTICS" table.
          optimizerStatisticsPackage: 'latest',
        }
      );
    
      const query = {
        sql: `SELECT AlbumId, AlbumTitle, MarketingBudget
            FROM Albums
            ORDER BY AlbumTitle`,
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
     * Create a client with query options.
     * Example:
     * ```
     * create_client_with_query_options($instanceId, $databaseId);
     * ```
     *
     * @param string $instanceId The Spanner instance ID.
     * @param string $databaseId The Spanner database ID.
     */
    function create_client_with_query_options(string $instanceId, string $databaseId): void
    {
        $spanner = new SpannerClient([
            'queryOptions' => [
                'optimizerVersion' => '1',
                // Pin the statistics package used for this client instance to the
                // latest version. The list of available statistics packages can be
                // found by querying the "INFORMATION_SCHEMA.SPANNER_STATISTICS"
                // table.
                'optimizerStatisticsPackage' => 'latest'
            ]
        ]);
        $instance = $spanner->instance($instanceId);
        $database = $instance->database($databaseId);
    
        $results = $database->execute(
            'SELECT VenueId, VenueName, LastUpdateTime FROM Venues'
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
    spanner_client = spanner.Client(
        query_options={
            "optimizer_version": "1",
            "optimizer_statistics_package": "latest",
        }
    )
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)
    
    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            "SELECT VenueId, VenueName, LastUpdateTime FROM Venues"
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
    
    query_options = {
      optimizer_version: "1",
      # The list of available statistics packages can be
      # found by querying the "INFORMATION_SCHEMA.SPANNER_STATISTICS"
      # table.
      optimizer_statistics_package: "latest"
    }
    
    spanner = Google::Cloud::[Spanner](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-instance-v1/latest/Google-Cloud-Spanner.html).new project: project_id
    client  = spanner.[client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-Project.html) instance_id, database_id, query_options: query_options
    
    sql_query = "SELECT VenueId, VenueName, LastUpdateTime FROM Venues"
    
    client.execute(sql_query).rows.[each](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-BatchWriteResults.html) do |row|
      puts "#{row[:VenueId]} #{row[:VenueName]} #{row[:LastUpdateTime]}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudspanner). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
