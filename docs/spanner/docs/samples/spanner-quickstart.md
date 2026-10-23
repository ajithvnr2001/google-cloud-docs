---
url: https://docs.cloud.google.com/spanner/docs/samples/spanner-quickstart/
title: Quickstart \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:09.574088+00:00
---

# Quickstart  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/samples/spanner-quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Samples ](https://docs.cloud.google.com/spanner/docs/samples)



#  Quickstart Stay organized with collections  Save and categorize content based on your preferences. 

Use a basic SELECT query.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Getting started with Spanner in C#](https://docs.cloud.google.com/spanner/docs/getting-started/csharp)
  * [Getting started with Spanner in Node.js](https://docs.cloud.google.com/spanner/docs/getting-started/nodejs)
  * [Getting started with Spanner in PHP](https://docs.cloud.google.com/spanner/docs/getting-started/php)
  * [Getting started with Spanner in Python](https://docs.cloud.google.com/spanner/docs/getting-started/python)
  * [Getting started with Spanner in Ruby](https://docs.cloud.google.com/spanner/docs/getting-started/ruby)
  * [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries)



## Code sample

### C++

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    #include "google/cloud/spanner/client.h"
    void Quickstart(std::string const& project_id, std::string const& instance_id,
                    std::string const& database_id) {
      namespace spanner = ::google::cloud::spanner;
    
      auto database = spanner::Database(project_id, instance_id, database_id);
      auto connection = spanner::MakeConnection(database);
      auto client = spanner::Client(connection);
    
      auto rows =
          client.ExecuteQuery(spanner::SqlStatement("SELECT 'Hello World'"));
      using RowType = std::tuple<std::string>;
      for (auto& row : spanner::StreamOf<RowType>(rows)) {
        if (!row) throw std::move(row).status();
        std::cout << std::get<0>(*row) << "\n";
      }
    }

### C#

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Spanner.Data](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.html);
    using System;
    using System.Threading.Tasks;
    
    namespace GoogleCloudSamples.Spanner
    {
        public class QuickStart
        {
            static async Task MainAsync()
            {
                string projectId = "YOUR-PROJECT-ID";
                string instanceId = "my-instance";
                string databaseId = "my-database";
                string connectionString =
                    $"Data Source=projects/{projectId}/instances/{instanceId}/"
                    + $"databases/{databaseId}";
                // Create connection to Cloud Spanner.
                using (var connection = new [SpannerConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html)(connectionString))
                {
                    // Execute a simple SQL statement.
                    var cmd = connection.[CreateSelectCommand](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html#Google_Cloud_Spanner_Data_SpannerConnection_CreateSelectCommand_System_String_Google_Cloud_Spanner_Data_SpannerParameterCollection_)(
                        @"SELECT ""Hello World"" as test");
                    using (var reader = await cmd.[ExecuteReaderAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerCommand.html#Google_Cloud_Spanner_Data_SpannerCommand_ExecuteReaderAsync)())
                    {
                        while (await reader.[ReadAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDataReader.html#Google_Cloud_Spanner_Data_SpannerDataReader_ReadAsync_System_Threading_CancellationToken_)())
                        {
                            Console.WriteLine(
                                reader.GetFieldValue<string>("test"));
                        }
                    }
                }
            }
            public static void Main(string[] args)
            {
                MainAsync().Wait();
            }
        }
    }
    

### Go

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Sample spanner_quickstart is a basic program that uses Cloud Spanner.
    package main
    
    import (
    	"context"
    	"fmt"
    	"log"
    
    	"cloud.google.com/go/spanner"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    
    	// This database must exist.
    	databaseName := "projects/your-project-id/instances/your-instance-id/databases/your-database-id"
    
    	client, err := spanner.NewClient(ctx, databaseName)
    	if err != nil {
    		log.Fatalf("Failed to create client %v", err)
    	}
    	defer client.Close()
    
    	stmt := spanner.[Statement](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Statement){SQL: "SELECT 1"}
    	iter := client.[Single](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Client_Single)().Query(ctx, stmt)
    	defer iter.Stop()
    
    	for {
    		row, err := iter.Next()
    		if err == iterator.Done {
    			fmt.Println("Done")
    			return
    		}
    		if err != nil {
    			log.Fatalf("Query failed with %v", err)
    		}
    
    		var i int64
    		if row.[Columns](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Row_Columns)(&i) != nil {
    			log.Fatalf("Failed to parse row %v", err)
    		}
    		fmt.Printf("Got value %v\n", i)
    	}
    }
    

### Java

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    import com.google.cloud.spanner.[DatabaseClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.DatabaseClient.html);
    import com.google.cloud.spanner.[DatabaseId](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.DatabaseId.html);
    import com.google.cloud.spanner.[ResultSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.ResultSet.html);
    import com.google.cloud.spanner.[Spanner](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html);
    import com.google.cloud.spanner.[SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html);
    import com.google.cloud.spanner.[Statement](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Statement.html);
    
    /**
     * A quick start code for Cloud Spanner. It demonstrates how to setup the Cloud Spanner client and
     * execute a simple query using it against an existing database.
     */
    public class QuickstartSample {
      public static void main(String... args) throws Exception {
    
        if (args.length != 2) {
          System.err.println("Usage: QuickStartSample <instance_id> <database_id>");
          return;
        }
        // Instantiates a client
        [SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html) options = [SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html).newBuilder().build();
        [Spanner](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html) spanner = [options](https://docs.cloud.google.com/java/docs/reference/pgadapter/latest/com.google.cloud.spanner.pgadapter.statements.IntermediateStatement.html#com_google_cloud_spanner_pgadapter_statements_IntermediateStatement_options).getService();
    
        // Name of your instance & database.
        String instanceId = args[0];
        String databaseId = args[1];
        try {
          // Creates a database client
          [DatabaseClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.DatabaseClient.html) dbClient =
              spanner.[getDatabaseClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html#com_google_cloud_spanner_Spanner_getDatabaseClient_com_google_cloud_spanner_DatabaseId_)(DatabaseId.of(options.getProjectId(), instanceId, databaseId));
          // Queries the database
          [ResultSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.ResultSet.html) resultSet = dbClient.[singleUse](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.DatabaseClient.html#com_google_cloud_spanner_DatabaseClient_singleUse__)().executeQuery([Statement](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Statement.html).of("SELECT 1"));
    
          System.out.println("\n\nResults:");
          // Prints the results
          while (resultSet.[next](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.ResultSet.html#com_google_cloud_spanner_ResultSet_next__)()) {
            System.out.printf("%d\n\n", resultSet.getLong(0));
          }
        } finally {
          // Closes the client which will free up the resources used
          spanner.[close](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html#com_google_cloud_spanner_Spanner_close__)();
        }
      }
    }

### Node.js

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const {Spanner} = require('[@google-cloud/spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/overview.html)');
    const {status} = require('@grpc/grpc-js');
    
    // Creates a client using the ambient project ID or environment configuration
    const spanner = new [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)();
    
    /**
     * Executes a query against a Cloud Spanner database.
     *
     * @param {string} projectId The project ID containing the Spanner instance (for example, 'example-project-id').
     * @param {string} instanceId The ID of the Spanner instance (for example, 'example-instance').
     * @param {string} databaseId The ID of the Spanner database (for example 'example-database').
     */
    async function quickstart(projectId, instanceId, databaseId) {
      try {
        // Gets a reference to a Cloud Spanner instance and database
        const instance = spanner.instance(instanceId);
        const database = instance.database(databaseId);
    
        const query = {
          sql: 'SELECT 1',
        };
    
        const [rows] = await database.run(query);
    
        console.log(`Query successfully executed. ${rows.length} row(s) found.`);
        rows.forEach(row => {
          console.log(`  Row details: ${JSON.stringify(row)}`);
        });
      } catch (err) {
        if (err.code === status.NOT_FOUND) {
          console.error(
            `Resource not found. Please verify that instance '${instanceId}' and database '${databaseId}' exist under project '${projectId}'.`
          );
        } else {
          console.error('An unexpected error occurred during execution:', err);
        }
      }
    }

### PHP

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Includes the autoloader for libraries installed with composer
    require __DIR__ . '/vendor/autoload.php';
    
    # Imports the Google Cloud client library
    use Google\Cloud\Spanner\SpannerClient;
    
    # Your Google Cloud Platform project ID
    $projectId = 'YOUR_PROJECT_ID';
    
    # Instantiates a client
    $spanner = new SpannerClient([
        'projectId' => $projectId
    ]);
    
    # Your Cloud Spanner instance ID.
    $instanceId = 'your-instance-id';
    
    # Get a Cloud Spanner instance by ID.
    $instance = $spanner->instance($instanceId);
    
    # Your Cloud Spanner database ID.
    $databaseId = 'your-database-id';
    
    # Get a Cloud Spanner database by ID.
    $database = $instance->database($databaseId);
    
    # Execute a simple SQL statement.
    $results = $database->execute('SELECT "Hello World" as test');
    
    foreach ($results as $row) {
        print($row['test'] . PHP_EOL);
    }

### Python

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Imports the Google Cloud Client Library.
    from google.cloud import [spanner](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.html)
    
    # Your Cloud Spanner instance ID.
    # instance_id = "my-instance-id"
    #
    # Your Cloud Spanner database ID.
    # database_id = "my-database-id"
    # Instantiate a client.
    spanner_client = [spanner](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.html).[Client](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client.html)()
    
    # Get a Cloud Spanner instance by ID.
    instance = spanner_client.[instance](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client.html#google_cloud_spanner_v1_client_Client_instance)(instance_id)
    
    # Get a Cloud Spanner database by ID.
    database = instance.database(database_id)
    
    # Execute a simple SQL statement.
    with database.snapshot() as snapshot:
        results = snapshot.execute_sql("SELECT 1")
    
        for row in results:
            print(row)

### Ruby

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Imports the Google Cloud client library
    require "google/cloud/spanner"
    
    # Your Google Cloud Platform project ID
    project_id = "YOUR_PROJECT_ID"
    
    # Instantiates a client
    spanner = Google::Cloud::[Spanner](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-instance-v1/latest/Google-Cloud-Spanner.html).new project: project_id
    
    # Your Cloud Spanner instance ID
    instance_id = "my-instance"
    
    # Your Cloud Spanner database ID
    database_id = "my-database"
    
    # Gets a reference to a Cloud Spanner instance database
    database_client = spanner.[client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-Project.html) instance_id, database_id
    
    # Execute a simple SQL statement
    results = database_client.execute_query "SELECT 1"
    results.rows.[each](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-BatchWriteResults.html) do |row|
      puts row
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudspanner). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
