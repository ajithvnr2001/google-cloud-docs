---
url: https://docs.cloud.google.com/spanner/docs/samples/spanner-write-data-for-struct-queries/
title: Mutations write data for STRUCT queries \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:21.928573+00:00
---

# Mutations write data for STRUCT queries  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/samples/spanner-write-data-for-struct-queries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Samples ](https://docs.cloud.google.com/spanner/docs/samples)



#  Mutations write data for STRUCT queries Stay organized with collections  Save and categorize content based on your preferences. 

Insert data used for STRUCT queries. 

## Code sample

### C++

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    void WriteDataForStructQueries(google::cloud::spanner::Client client) {
      namespace spanner = ::google::cloud::spanner;
      auto commit_result = client.Commit(
          spanner::Mutations{spanner::InsertMutationBuilder(
                                 "Singers", {"SingerId", "FirstName", "LastName"})
                                 .EmplaceRow(6, "Elena", "Campbell")
                                 .EmplaceRow(7, "Gabriel", "Wright")
                                 .EmplaceRow(8, "Benjamin", "Martinez")
                                 .EmplaceRow(9, "Hannah", "Harris")
                                 .Build()});
      if (!commit_result) throw std::move(commit_result).status();
      std::cout << "Insert was successful "
                << "[spanner_write_data_for_struct_queries]\n";
    }

### C#

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Spanner.Data](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.html);
    using System.Collections.Generic;
    using System.Linq;
    using System.Threading.Tasks;
    
    public class InsertStructSampleDataAsyncSample
    {
        public class Singer
        {
            public int SingerId { get; set; }
            public string FirstName { get; set; }
            public string LastName { get; set; }
        }
    
        public async Task<int> InsertStructSampleDataAsync(string projectId, string instanceId, string databaseId)
        {
            string connectionString = $"Data Source=projects/{projectId}/instances/{instanceId}/databases/{databaseId}";
            List<Singer> singers = new List<Singer> {
                new Singer { SingerId = 6, FirstName = "Elena", LastName = "Campbell" },
                new Singer { SingerId = 7, FirstName = "Gabriel", LastName = "Wright" },
                new Singer { SingerId = 8, FirstName = "Benjamin", LastName = "Martinez" },
                new Singer { SingerId = 9, FirstName = "Hannah", LastName = "Harris" }
            };
    
            using var connection = new [SpannerConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html)(connectionString);
            await connection.[OpenAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html#Google_Cloud_Spanner_Data_SpannerConnection_OpenAsync_Google_Cloud_Spanner_Data_SpannerTransactionCreationOptions_Google_Cloud_Spanner_Data_SpannerTransactionOptions_System_Threading_CancellationToken_)();
    
            var rows = await Task.WhenAll(singers.[Select](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerCommandType.html#Google_Cloud_Spanner_Data_SpannerCommandType_Select)(singer =>
            {
                var cmd = connection.[CreateInsertCommand](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html#Google_Cloud_Spanner_Data_SpannerConnection_CreateInsertCommand_System_String_Google_Cloud_Spanner_Data_SpannerParameterCollection_)("Singers",
                    new [SpannerParameterCollection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerParameterCollection.html) {
                        { "SingerId", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[Int64](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_Int64), singer.SingerId },
                        { "FirstName", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[String](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_String), singer.FirstName },
                        { "LastName", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[String](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_String), singer.LastName }
                    });
                return cmd.ExecuteNonQueryAsync();
            }));
            return rows.Sum();
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
    
    func writeStructData(w io.Writer, db string) error {
    	ctx := context.Background()
    	client, err := spanner.NewClient(ctx, db)
    	if err != nil {
    		return err
    	}
    	defer client.Close()
    
    	singerColumns := []string{"SingerId", "FirstName", "LastName"}
    	m := []*spanner.Mutation{
    		spanner.[InsertOrUpdate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Mutation_InsertOrUpdate)("Singers", singerColumns, []interface{}{6, "Elena", "Campbell"}),
    		spanner.[InsertOrUpdate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Mutation_InsertOrUpdate)("Singers", singerColumns, []interface{}{7, "Gabriel", "Wright"}),
    		spanner.[InsertOrUpdate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Mutation_InsertOrUpdate)("Singers", singerColumns, []interface{}{8, "Benjamin", "Martinez"}),
    		spanner.[InsertOrUpdate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Mutation_InsertOrUpdate)("Singers", singerColumns, []interface{}{9, "Hannah", "Harris"}),
    	}
    	_, err = client.[Apply](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Client_Apply)(ctx, m)
    	return err
    }
    

### Java

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    static void writeStructExampleData(DatabaseClient dbClient) {
      final List<Singer> singers =
          Arrays.asList(
              new Singer(6, "Elena", "Campbell"),
              new Singer(7, "Gabriel", "Wright"),
              new Singer(8, "Benjamin", "Martinez"),
              new Singer(9, "Hannah", "Harris"));
    
      List<Mutation> mutations = new ArrayList<>();
      for (Singer singer : singers) {
        mutations.add(
            Mutation.newInsertBuilder("Singers")
                .set("SingerId")
                .to(singer.singerId)
                .set("FirstName")
                .to(singer.firstName)
                .set("LastName")
                .to(singer.lastName)
                .build());
      }
      dbClient.write(mutations);
      System.out.println("Inserted example data for struct parameter queries.");
    }

### Node.js

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const {Spanner} = require('[@google-cloud/spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/overview.html)');
    
    /**
     * TODO(developer): Uncomment and update the following lines before running the sample.
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
    
      // Instantiates Spanner table objects
      const singersTable = database.table('Singers');
    
      // Inserts rows into the Singers table
      // Note: Cloud Spanner interprets Javascript numbers as FLOAT64s.
      // Use strings as shown in this example if you need INT64s.
      const data = [
        {
          SingerId: '6',
          FirstName: 'Elena',
          LastName: 'Campbell',
        },
        {
          SingerId: '7',
          FirstName: 'Gabriel',
          LastName: 'Wright',
        },
        {
          SingerId: '8',
          FirstName: 'Benjamin',
          LastName: 'Martinez',
        },
        {
          SingerId: '9',
          FirstName: 'Hannah',
          LastName: 'Harris',
        },
      ];
    
      await singersTable.insert(data);
      console.log('Inserted data.');
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
     * Inserts sample data that can be used to test STRUCT parameters in queries.
     *
     * The database and table must already exist and can be created using
     * `create_database`.
     * Example:
     * ```
     * insert_struct_data($instanceId, $databaseId);
     * ```
     *
     * @param string $instanceId The Spanner instance ID.
     * @param string $databaseId The Spanner database ID.
     */
    function insert_struct_data(string $instanceId, string $databaseId): void
    {
        $spanner = new SpannerClient();
        $instance = $spanner->instance($instanceId);
        $database = $instance->database($databaseId);
    
        $operation = $database->transaction(['singleUse' => true])
            ->insertBatch('Singers', [
                ['SingerId' => 6, 'FirstName' => 'Elena', 'LastName' => 'Campbell'],
                ['SingerId' => 7, 'FirstName' => 'Gabriel', 'LastName' => 'Wright'],
                ['SingerId' => 8, 'FirstName' => 'Benjamin', 'LastName' => 'Martinez'],
                ['SingerId' => 9, 'FirstName' => 'Hannah', 'LastName' => 'Harris'],
            ])
            ->commit();
    
        print('Inserted data.' . PHP_EOL);
    }

### Python

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def write_struct_data(instance_id, database_id):
        """Inserts sample data that can be used to test STRUCT parameters
        in queries.
        """
        spanner_client = spanner.Client()
        instance = spanner_client.instance(instance_id)
        database = instance.database(database_id)
    
        with database.batch() as batch:
            batch.insert(
                table="Singers",
                columns=("SingerId", "FirstName", "LastName"),
                values=[
                    (6, "Elena", "Campbell"),
                    (7, "Gabriel", "Wright"),
                    (8, "Benjamin", "Martinez"),
                    (9, "Hannah", "Harris"),
                ],
            )
    
        print("Inserted sample data for STRUCT queries")
    
    

### Ruby

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project_id  = "Your Google Cloud project ID"
    # instance_id = "Your Spanner instance ID"
    # database_id = "Your Spanner database ID"
    
    require "google/cloud/spanner"
    
    spanner = Google::Cloud::[Spanner](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-instance-v1/latest/Google-Cloud-Spanner.html).new project: project_id
    client  = spanner.[client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-Project.html) instance_id, database_id
    
    client.commit do |c|
      c.insert "Singers", [
        { SingerId: 6, FirstName: "Elena",    LastName: "Campbell" },
        { SingerId: 7, FirstName: "Gabriel",  LastName: "Wright"    },
        { SingerId: 8, FirstName: "Benjamin", LastName: "Martinez"  },
        { SingerId: 9, FirstName: "Hannah",   LastName: "Harris" }
      ]
    end
    puts "Inserted Data for Struct queries"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudspanner). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
