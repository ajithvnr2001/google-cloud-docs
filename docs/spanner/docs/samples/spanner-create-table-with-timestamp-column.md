---
url: https://docs.cloud.google.com/spanner/docs/samples/spanner-create-table-with-timestamp-column/
title: Create table with TIMESTAMP column \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:26.697658+00:00
---

# Create table with TIMESTAMP column  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/samples/spanner-create-table-with-timestamp-column/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Samples ](https://docs.cloud.google.com/spanner/docs/samples)



#  Create table with TIMESTAMP column Stay organized with collections  Save and categorize content based on your preferences. 

Create a table with a TIMESTAMP column.

## Code sample

### C++

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    void CreateTableWithTimestamp(
        google::cloud::spanner_admin::DatabaseAdminClient client,
        std::string const& project_id, std::string const& instance_id,
        std::string const& database_id) {
      google::cloud::spanner::Database database(project_id, instance_id,
                                                database_id);
      auto metadata = client
                          .UpdateDatabaseDdl(database.FullName(), {R"""(
                            CREATE TABLE Performances (
                                SingerId        INT64 NOT NULL,
                                VenueId         INT64 NOT NULL,
                                EventDate       Date,
                                Revenue         INT64,
                                LastUpdateTime  TIMESTAMP NOT NULL OPTIONS
                                    (allow_commit_timestamp=true)
                            ) PRIMARY KEY (SingerId, VenueId, EventDate),
                                INTERLEAVE IN PARENT Singers ON DELETE CASCADE)"""})
                          .get();
      google::cloud::spanner_testing::LogUpdateDatabaseDdl(  //! TODO(#4758)
          client, database, metadata.status());              //! TODO(#4758)
      if (!metadata) throw std::move(metadata).status();
      std::cout << "`Performances` table created, new DDL:\n"
                << metadata->DebugString();
    }

### C#

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Spanner.Data](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.html);
    using System.Threading.Tasks;
    
    public class CreateTableWithTimestampColumnAsyncSample
    {
        public async Task CreateTableWithTimestampColumnAsync(string projectId, string instanceId, string databaseId)
        {
            string connectionString = $"Data Source=projects/{projectId}/instances/{instanceId}/databases/{databaseId}";
            using var connection = new [SpannerConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html)(connectionString);
            // Define create table statement for table with commit timestamp column.
            string createTableStatement =
            @"CREATE TABLE Performances (
                        SingerId       INT64 NOT NULL,
                        VenueId        INT64 NOT NULL,
                        EventDate      Date,
                        Revenue        INT64,
                        LastUpdateTime TIMESTAMP NOT NULL OPTIONS (allow_commit_timestamp=true)
                    ) PRIMARY KEY (SingerId, VenueId, EventDate),
                        INTERLEAVE IN PARENT Singers ON DELETE CASCADE";
            var cmd = connection.[CreateDdlCommand](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html#Google_Cloud_Spanner_Data_SpannerConnection_CreateDdlCommand_System_String_Google_Protobuf_Reflection_FileDescriptorSet_System_String___)(createTableStatement);
            await cmd.ExecuteNonQueryAsync();
        }
    }

### Go

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	database "cloud.google.com/go/spanner/admin/database/apiv1"
    	adminpb "cloud.google.com/go/spanner/admin/database/apiv1/databasepb"
    )
    
    func createTableWithTimestamp(w io.Writer, db string) error {
    	ctx := context.Background()
    	adminClient, err := database.NewDatabaseAdminClient(ctx)
    	if err != nil {
    		return err
    	}
    	defer adminClient.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/admin/database/apiv1.html#cloud_google_com_go_spanner_admin_database_apiv1_DatabaseAdminClient_Close)()
    
    	op, err := adminClient.UpdateDatabaseDdl(ctx, &adminpb.UpdateDatabaseDdlRequest{
    		Database: db,
    		Statements: []string{
    			`CREATE TABLE Performances (
    				SingerId        INT64 NOT NULL,
    				VenueId         INT64 NOT NULL,
    				EventDate       Date,
    				Revenue         INT64,
    				LastUpdateTime  TIMESTAMP NOT NULL OPTIONS (allow_commit_timestamp=true)
    			) PRIMARY KEY (SingerId, VenueId, EventDate),
    			INTERLEAVE IN PARENT Singers ON DELETE CASCADE`,
    		},
    	})
    	if err != nil {
    		return err
    	}
    	if err := op.Wait(ctx); err != nil {
    		return err
    	}
    	fmt.Fprintf(w, "Created Performances table in database [%s]\n", db)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    static void createTableWithTimestamp(DatabaseAdminClient dbAdminClient,
        DatabaseName databaseName) {
      try {
        // Initiate the request which returns an OperationFuture.
        dbAdminClient.updateDatabaseDdlAsync(
            databaseName,
            Arrays.asList(
                "CREATE TABLE Performances ("
                    + "  SingerId     INT64 NOT NULL,"
                    + "  VenueId      INT64 NOT NULL,"
                    + "  EventDate    Date,"
                    + "  Revenue      INT64, "
                    + "  LastUpdateTime TIMESTAMP NOT NULL OPTIONS (allow_commit_timestamp=true)"
                    + ") PRIMARY KEY (SingerId, VenueId, EventDate),"
                    + "  INTERLEAVE IN PARENT Singers ON DELETE CASCADE")).get();
        System.out.println(
            "Created Performances table in database: [" + databaseName.toString() + "]");
      } catch (ExecutionException e) {
        // If the operation failed during execution, expose the cause.
        throw (SpannerException) e.getCause();
      } catch (InterruptedException e) {
        // Throw when a thread is waiting, sleeping, or otherwise occupied,
        // and the thread is interrupted, either before or during the activity.
        throw SpannerExceptionFactory.propagateInterrupt(e);
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
    
    // Gets a reference to a Cloud Spanner Database Admin Client object
    const databaseAdminClient = spanner.[getDatabaseAdminClient](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)();
    
    // Note: Cloud Spanner interprets Node.js numbers as FLOAT64s, so they
    // must be converted to strings before being inserted as INT64s
    const request = [
      `CREATE TABLE Performances (
          SingerId    INT64 NOT NULL,
          VenueId     INT64 NOT NULL,
          EventDate   DATE,
          Revenue     INT64,
          LastUpdateTime TIMESTAMP NOT NULL OPTIONS (allow_commit_timestamp=true)
        ) PRIMARY KEY (SingerId, VenueId, EventDate),
        INTERLEAVE IN PARENT Singers ON DELETE CASCADE`,
    ];
    try {
      // Creates a table in an existing database
      const [operation] = await databaseAdminClient.updateDatabaseDdl({
        database: databaseAdminClient.databasePath(
          projectId,
          instanceId,
          databaseId
        ),
        statements: request,
      });
    
      console.log(`Waiting for operation on ${databaseId} to complete...`);
    
      await operation.promise();
    
      console.log(`Created table Performances in database ${databaseId}.`);
    } catch (err) {
      console.error('ERROR:', err);
    }

### PHP

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Spanner\SpannerClient;
    
    /**
     * Creates a table with a commit timestamp column.
     * Example:
     * ```
     * create_table_with_timestamp_column($instanceId, $databaseId);
     * ```
     *
     * @param string $instanceId The Spanner instance ID.
     * @param string $databaseId The Spanner database ID.
     */
    function create_table_with_timestamp_column(string $instanceId, string $databaseId): void
    {
        $spanner = new SpannerClient();
        $instance = $spanner->instance($instanceId);
        $database = $instance->database($databaseId);
    
        $operation = $database->updateDdl(
            'CREATE TABLE Performances (
        		SingerId	INT64 NOT NULL,
        		VenueId		INT64 NOT NULL,
        		EventDate	DATE,
        		Revenue		INT64,
        		LastUpdateTime	TIMESTAMP NOT NULL OPTIONS (allow_commit_timestamp=true)
        	) PRIMARY KEY (SingerId, VenueId, EventDate),
        	INTERLEAVE IN PARENT Singers on DELETE CASCADE'
        );
    
        print('Waiting for operation to complete...' . PHP_EOL);
        $operation->pollUntilComplete();
    
        printf('Created Performances table in database %s on instance %s' . PHP_EOL,
            $databaseId, $instanceId);
    }

### Python

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def create_table_with_timestamp(instance_id, database_id):
        """Creates a table with a COMMIT_TIMESTAMP column."""
    
        spanner_client = spanner.Client()
        instance = spanner_client.instance(instance_id)
        database = instance.database(database_id)
    
        operation = database.update_ddl(
            [
                """CREATE TABLE Performances (
                SingerId     INT64 NOT NULL,
                VenueId      INT64 NOT NULL,
                EventDate    Date,
                Revenue      INT64,
                LastUpdateTime TIMESTAMP NOT NULL
                OPTIONS(allow_commit_timestamp=true)
            ) PRIMARY KEY (SingerId, VenueId, EventDate),
              INTERLEAVE IN PARENT Singers ON DELETE CASCADE"""
            ]
        )
    
        print("Waiting for operation to complete...")
        operation.result(OPERATION_TIMEOUT_SECONDS)
    
        print(
            "Created Performances table on database {} on instance {}".format(
                database_id, instance_id
            )
        )
    
    

### Ruby

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project_id  = "Your Google Cloud project ID"
    # instance_id = "Your Spanner instance ID"
    # database_id = "Your Spanner database ID"
    
    require "google/cloud/spanner"
    require "google/cloud/spanner/admin/database"
    
    database_admin_client = Google::Cloud::Spanner::Admin::Database.database_admin
    
    db_path = database_admin_client.database_path project: project_id,
                                                  instance: instance_id,
                                                  database: database_id
    
    job = database_admin_client.update_database_ddl database: db_path,
                                                    statements: [
                                                      "CREATE TABLE Performances (
        SingerId     INT64 NOT NULL,
        VenueId      INT64 NOT NULL,
        EventDate    Date,
        Revenue      INT64,
        LastUpdateTime TIMESTAMP NOT NULL OPTIONS (allow_commit_timestamp=true)
       ) PRIMARY KEY (SingerId, VenueId, EventDate),
       INTERLEAVE IN PARENT Singers ON DELETE CASCADE"
                                                    ]
    
    puts "Waiting for update database operation to complete"
    
    job.wait_until_done!
    
    puts "Created table Performances in #{database_id}"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudspanner). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
