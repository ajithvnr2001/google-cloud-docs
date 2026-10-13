---
url: https://docs.cloud.google.com/spanner/docs/samples/spanner-add-numeric-column/
title: Add NUMERIC column \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:47:18.158552+00:00
---

# Add NUMERIC column  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/samples/spanner-add-numeric-column/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Samples ](https://docs.cloud.google.com/spanner/docs/samples)



#  Add NUMERIC column Stay organized with collections  Save and categorize content based on your preferences. 

Update a schema by adding a NUMERIC column.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Work with NUMERIC data](https://docs.cloud.google.com/spanner/docs/working-with-numerics)



## Code sample

### C++

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    void AddNumericColumn(google::cloud::spanner_admin::DatabaseAdminClient client,
                          std::string const& project_id,
                          std::string const& instance_id,
                          std::string const& database_id) {
      google::cloud::spanner::Database database(project_id, instance_id,
                                                database_id);
      auto metadata = client
                          .UpdateDatabaseDdl(database.FullName(), {R"""(
                            ALTER TABLE Venues ADD COLUMN Revenue NUMERIC)"""})
                          .get();
      google::cloud::spanner_testing::LogUpdateDatabaseDdl(  //! TODO(#4758)
          client, database, metadata.status());              //! TODO(#4758)
      if (!metadata) throw std::move(metadata).status();
      std::cout << "`Venues` table altered, new DDL:\n" << metadata->DebugString();
    }

### C#

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Spanner.Data](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.html);
    using System;
    using System.Threading.Tasks;
    
    public class AddNumericColumnAsyncSample
    {
        public async Task AddNumericColumnAsync(string projectId, string instanceId, string databaseId)
        {
            string connectionString = $"Data Source=projects/{projectId}/instances/{instanceId}/databases/{databaseId}";
            string alterStatement = "ALTER TABLE Venues ADD COLUMN Revenue NUMERIC";
    
            using var connection = new [SpannerConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html)(connectionString);
            using var updateCmd = connection.[CreateDdlCommand](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html#Google_Cloud_Spanner_Data_SpannerConnection_CreateDdlCommand_System_String_Google_Protobuf_Reflection_FileDescriptorSet_System_String___)(alterStatement);
            await updateCmd.ExecuteNonQueryAsync();
            Console.WriteLine("Added the Revenue column.");
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
    
    func addNumericColumn(ctx context.Context, w io.Writer, db string) error {
    	adminClient, err := database.NewDatabaseAdminClient(ctx)
    	if err != nil {
    		return err
    	}
    	defer adminClient.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/admin/database/apiv1.html#cloud_google_com_go_spanner_admin_database_apiv1_DatabaseAdminClient_Close)()
    
    	op, err := adminClient.UpdateDatabaseDdl(ctx, &adminpb.UpdateDatabaseDdlRequest{
    		Database: db,
    		Statements: []string{
    			"ALTER TABLE Venues ADD COLUMN Revenue NUMERIC",
    		},
    	})
    	if err != nil {
    		return err
    	}
    	if err := op.Wait(ctx); err != nil {
    		return err
    	}
    	fmt.Fprintf(w, "Added Revenue column\n")
    	return nil
    }
    

### Java

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.spanner.[Spanner](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html);
    import com.google.cloud.spanner.[SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html);
    import com.google.cloud.spanner.admin.database.v1.[DatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html);
    import com.google.common.collect.ImmutableList;
    import com.google.spanner.admin.database.v1.[DatabaseName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.DatabaseName.html);
    import java.util.concurrent.ExecutionException;
    
    class AddNumericColumnSample {
    
      static void addNumericColumn() throws InterruptedException, ExecutionException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project";
        String instanceId = "my-instance";
        String databaseId = "my-database";
    
        addNumericColumn(projectId, instanceId, databaseId);
      }
    
      static void addNumericColumn(String projectId, String instanceId, String databaseId)
          throws InterruptedException, ExecutionException {
        try ([Spanner](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html) spanner =
            [SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html).newBuilder()
                .setProjectId(projectId)
                .build()
                .getService();
            [DatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html) databaseAdminClient = spanner.[createDatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html#com_google_cloud_spanner_Spanner_createDatabaseAdminClient__)()) {
          // Wait for the operation to finish.
          // This will throw an ExecutionException if the operation fails.
          databaseAdminClient.updateDatabaseDdlAsync(
              [DatabaseName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.DatabaseName.html).of(projectId, instanceId, databaseId),
              ImmutableList.of("ALTER TABLE Venues ADD COLUMN Revenue NUMERIC")).get();
          System.out.printf("Successfully added column `Revenue`%n");
        }
      }
    }

### Node.js

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // const projectId = 'my-project-id';
    // const instanceId = 'my-instance';
    // const databaseId = 'my-database';
    
    // Imports the Google Cloud client library
    const {Spanner} = require('[@google-cloud/spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/overview.html)');
    
    // creates a client
    const spanner = new [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)({
      projectId: projectId,
    });
    
    const databaseAdminClient = spanner.[getDatabaseAdminClient](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)();
    
    const request = ['ALTER TABLE Venues ADD COLUMN Revenue NUMERIC'];
    try {
      // Alter existing table to add a column.
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
    
      console.log(
        `Added Revenue column to Venues table in database ${databaseId}.`
      );
    } catch (err) {
      console.error('ERROR:', err);
    }

### PHP

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Spanner\Admin\Database\V1\Client\DatabaseAdminClient;
    use Google\Cloud\Spanner\Admin\Database\V1\UpdateDatabaseDdlRequest;
    
    /**
     * Adds a NUMERIC column to a table.
     * Example:
     * ```
     * add_numeric_column($projectId, $instanceId, $databaseId);
     * ```
     *
     * @param string $projectId The Google Cloud project ID.
     * @param string $instanceId The Spanner instance ID.
     * @param string $databaseId The Spanner database ID.
     */
    function add_numeric_column(string $projectId, string $instanceId, string $databaseId): void
    {
        $databaseAdminClient = new DatabaseAdminClient();
        $databaseName = DatabaseAdminClient::databaseName($projectId, $instanceId, $databaseId);
    
        $request = new UpdateDatabaseDdlRequest([
            'database' => $databaseName,
            'statements' => ['ALTER TABLE Venues ADD COLUMN Revenue NUMERIC']
        ]);
    
        $operation = $databaseAdminClient->updateDatabaseDdl($request);
    
        print('Waiting for operation to complete...' . PHP_EOL);
        $operation->pollUntilComplete();
    
        printf('Added Revenue as a NUMERIC column in Venues table' . PHP_EOL);
    }

### Python

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def add_numeric_column(instance_id, database_id):
        """Adds a new NUMERIC column to the Venues table in the example database."""
        spanner_client = spanner.Client()
        instance = spanner_client.instance(instance_id)
    
        database = instance.database(database_id)
    
        operation = database.update_ddl(["ALTER TABLE Venues ADD COLUMN Revenue NUMERIC"])
    
        print("Waiting for operation to complete...")
        operation.result(OPERATION_TIMEOUT_SECONDS)
    
        print(
            'Altered table "Venues" on database {} on instance {}.'.format(
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
                                                      "ALTER TABLE Venues ADD COLUMN Revenue NUMERIC"
                                                    ]
    
    puts "Waiting for database update to complete"
    
    job.wait_until_done!
    
    puts "Added the Revenue as a numeric column in Venues table"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudspanner). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
