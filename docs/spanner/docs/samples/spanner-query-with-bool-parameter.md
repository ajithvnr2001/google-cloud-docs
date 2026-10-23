---
url: https://docs.cloud.google.com/spanner/docs/samples/spanner-query-with-bool-parameter/
title: Query with BOOL parameter \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:34.986545+00:00
---

# Query with BOOL parameter  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/samples/spanner-query-with-bool-parameter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Samples ](https://docs.cloud.google.com/spanner/docs/samples)



#  Query with BOOL parameter Stay organized with collections  Save and categorize content based on your preferences. 

Query data by using a BOOL parameter. 

## Code sample

### C++

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    void QueryWithBoolParameter(google::cloud::spanner::Client client) {
      namespace spanner = ::google::cloud::spanner;
      bool example_bool = true;
      spanner::SqlStatement select(
          "SELECT VenueId, VenueName, OutdoorVenue FROM Venues"
          " WHERE OutdoorVenue = @outdoor_venue",
          {{"outdoor_venue", spanner::Value(example_bool)}});
      using RowType =
          std::tuple<std::int64_t, std::optional<std::string>, std::optional<bool>>;
      auto rows = client.ExecuteQuery(std::move(select));
      for (auto& row : spanner::StreamOf<RowType>(rows)) {
        if (!row) throw std::move(row).status();
        std::cout << "VenueId: " << std::get<0>(*row) << "\t";
        std::cout << "VenueName: " << std::get<1>(*row).value() << "\t";
        std::cout << "OutdoorVenue: " << std::get<2>(*row).value() << "\n";
      }
      std::cout << "Query completed for [spanner_query_with_bool_parameter]\n";
    }

### C#

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Spanner.Data](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.html);
    using System.Collections.Generic;
    using System.Threading.Tasks;
    
    public class QueryWithBoolAsyncSample
    {
        public class Venue
        {
            public int VenueId { get; set; }
            public string VenueName { get; set; }
            public bool OutdoorVenue { get; set; }
        }
    
        public async Task<List<Venue>> QueryWithBoolAsync(string projectId, string instanceId, string databaseId)
        {
            string connectionString = $"Data Source=projects/{projectId}/instances/{instanceId}/databases/{databaseId}";
            bool exampleBool = true;
    
            using var connection = new [SpannerConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html)(connectionString);
            var cmd = connection.[CreateSelectCommand](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html#Google_Cloud_Spanner_Data_SpannerConnection_CreateSelectCommand_System_String_Google_Cloud_Spanner_Data_SpannerParameterCollection_)(
                "SELECT VenueId, VenueName, OutdoorVenue FROM Venues "
                + "WHERE OutdoorVenue = @ExampleBool");
            cmd.[Parameters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerCommand.html#Google_Cloud_Spanner_Data_SpannerCommand_Parameters).Add("ExampleBool", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[Bool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_Bool), exampleBool);
    
            var venues = new List<Venue>();
            using var reader = await cmd.[ExecuteReaderAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerCommand.html#Google_Cloud_Spanner_Data_SpannerCommand_ExecuteReaderAsync)();
            while (await reader.[ReadAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDataReader.html#Google_Cloud_Spanner_Data_SpannerDataReader_ReadAsync_System_Threading_CancellationToken_)())
            {
                venues.Add(new Venue
                {
                    VenueId = reader.GetFieldValue<int>("VenueId"),
                    VenueName = reader.GetFieldValue<string>("VenueName"),
                    OutdoorVenue = reader.GetFieldValue<bool>("OutdoorVenue")
                });
            }
            return venues;
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
    	"google.golang.org/api/iterator"
    )
    
    func queryWithBool(w io.Writer, db string) error {
    	ctx := context.Background()
    	client, err := spanner.NewClient(ctx, db)
    	if err != nil {
    		return err
    	}
    	defer client.Close()
    
    	var exampleBool = true
    	stmt := spanner.[Statement](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Statement){
    		SQL: `SELECT VenueId, VenueName, OutdoorVenue FROM Venues
                	WHERE OutdoorVenue = @outdoorVenue`,
    		Params: map[string]interface{}{
    			"outdoorVenue": exampleBool,
    		},
    	}
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
    		var outdoorVenue bool
    		if err := row.[Columns](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Row_Columns)(&venueID, &venueName, &outdoorVenue); err != nil {
    			return err
    		}
    		fmt.Fprintf(w, "%d %s %t\n", venueID, venueName, outdoorVenue)
    	}
    }
    

### Java

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    static void queryWithBool(DatabaseClient dbClient) {
      boolean exampleBool = true;
      Statement statement =
          Statement.newBuilder(
                  "SELECT VenueId, VenueName, OutdoorVenue FROM Venues "
                      + "WHERE OutdoorVenue = @outdoorVenue")
              .bind("outdoorVenue")
              .to(exampleBool)
              .build();
      try (ResultSet resultSet = dbClient.singleUse().executeQuery(statement)) {
        while (resultSet.next()) {
          System.out.printf(
              "%d %s %b\n",
              resultSet.getLong("VenueId"),
              resultSet.getString("VenueName"),
              resultSet.getBoolean("OutdoorVenue"));
        }
      }
    }

### Node.js

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library.
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
    
    // Gets a reference to a Cloud Spanner instance and database.
    const instance = spanner.instance(instanceId);
    const database = instance.database(databaseId);
    
    const fieldType = {
      type: 'bool',
    };
    
    const exampleBool = true;
    
    const query = {
      sql: `SELECT VenueId, VenueName, OutdoorVenue FROM Venues
              WHERE OutdoorVenue = @outdoorVenue`,
      params: {
        outdoorVenue: exampleBool,
      },
      types: {
        outdoorVenue: fieldType,
      },
    };
    
    // Queries rows from the Venues table.
    try {
      const [rows] = await database.run(query);
    
      rows.forEach(row => {
        const json = row.toJSON();
        console.log(
          `VenueId: ${json.VenueId}, VenueName: ${json.VenueName},` +
            ` OutdoorVenue: ${json.OutdoorVenue}`
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
     * Queries sample data from the database using SQL with a BOOL parameter.
     * Example:
     * ```
     * query_data_with_bool_parameter($instanceId, $databaseId);
     * ```
     *
     * @param string $instanceId The Spanner instance ID.
     * @param string $databaseId The Spanner database ID.
     */
    function query_data_with_bool_parameter(string $instanceId, string $databaseId): void
    {
        $spanner = new SpannerClient();
        $instance = $spanner->instance($instanceId);
        $database = $instance->database($databaseId);
    
        $exampleBool = true;
    
        $results = $database->execute(
            'SELECT VenueId, VenueName, OutdoorVenue FROM Venues ' .
            'WHERE OutdoorVenue = @outdoorVenue',
            [
                'parameters' => [
                    'outdoorVenue' => $exampleBool
                ]
            ]
        );
    
        foreach ($results as $row) {
            printf('VenueId: %s, VenueName: %s, OutdoorVenue: %s' . PHP_EOL,
                $row['VenueId'], $row['VenueName'],
                $row['OutdoorVenue'] ? 'True' : 'False');
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
    
    exampleBool = True
    param = {"outdoor_venue": exampleBool}
    param_type = {"outdoor_venue": param_types.BOOL}
    
    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            "SELECT VenueId, VenueName, OutdoorVenue FROM Venues "
            "WHERE OutdoorVenue = @outdoor_venue",
            params=param,
            param_types=param_type,
        )
    
        for row in results:
            print("VenueId: {}, VenueName: {}, OutdoorVenue: {}".format(*row))

### Ruby

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project_id  = "Your Google Cloud project ID"
    # instance_id = "Your Spanner instance ID"
    # database_id = "Your Spanner database ID"
    
    require "google/cloud/spanner"
    
    spanner = Google::Cloud::[Spanner](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-instance-v1/latest/Google-Cloud-Spanner.html).new project: project_id
    client  = spanner.[client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-Project.html) instance_id, database_id
    
    sql_query = "SELECT VenueId, VenueName, OutdoorVenue FROM Venues
                 WHERE OutdoorVenue = @outdoor_venue"
    
    params      = { outdoor_venue: true }
    param_types = { outdoor_venue: :BOOL }
    
    client.execute(sql_query, params: params, types: param_types).rows.[each](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-BatchWriteResults.html) do |row|
      puts "#{row[:VenueId]} #{row[:VenueName]} #{row[:OutdoorVenue]}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudspanner). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
