---
url: https://docs.cloud.google.com/spanner/docs/samples/spanner-update-data-with-numeric-column/
title: Mutations update data with NUMERIC \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:30:25.549215+00:00
---

# Mutations update data with NUMERIC  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/samples/spanner-update-data-with-numeric-column/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Samples ](https://docs.cloud.google.com/spanner/docs/samples)



#  Mutations update data with NUMERIC Stay organized with collections  Save and categorize content based on your preferences. 

Update data in NUMERIC column by using mutations.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Work with NUMERIC data](https://docs.cloud.google.com/spanner/docs/working-with-numerics)



## Code sample

### C++

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    void UpdateDataWithNumeric(google::cloud::spanner::Client client) {
      namespace spanner = ::google::cloud::spanner;
      auto insert_venues =
          spanner::InsertMutationBuilder(
              "Venues", {"VenueId", "VenueName", "Revenue", "LastUpdateTime"})
              .EmplaceRow(1, "Venue 1", spanner::MakeNumeric(35000).value(),
                          spanner::CommitTimestamp())
              .EmplaceRow(6, "Venue 6", spanner::MakeNumeric(104500).value(),
                          spanner::CommitTimestamp())
              .EmplaceRow(
                  14, "Venue 14",
                  spanner::MakeNumeric("99999999999999999999999999999.99").value(),
                  spanner::CommitTimestamp())
              .Build();
    
      auto commit_result = client.Commit(spanner::Mutations{insert_venues});
      if (!commit_result) throw std::move(commit_result).status();
      std::cout
          << "Insert was successful [spanner_update_data_with_numeric_column]\n";
    }

### C#

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Spanner.Data](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.html);
    using [Google.Cloud.Spanner.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.html);
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Threading.Tasks;
    
    public class UpdateDataWithNumericAsyncSample
    {
        public class Venue
        {
            public int VenueId { get; set; }
            public [SpannerNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.SpannerNumeric.html) Revenue { get; set; }
        }
    
        public async Task<int> UpdateDataWithNumericAsync(string projectId, string instanceId, string databaseId)
        {
            string connectionString = $"Data Source=projects/{projectId}/instances/{instanceId}/databases/{databaseId}";
            List<Venue> venues = new List<Venue>
            {
                new Venue { VenueId = 4, Revenue = [SpannerNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.SpannerNumeric.html).[Parse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.SpannerNumeric.html#Google_Cloud_Spanner_V1_SpannerNumeric_Parse_System_String_)("35000") },
                new Venue { VenueId = 19, Revenue = [SpannerNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.SpannerNumeric.html).[Parse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.SpannerNumeric.html#Google_Cloud_Spanner_V1_SpannerNumeric_Parse_System_String_)("104500") },
                new Venue { VenueId = 42, Revenue = [SpannerNumeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.SpannerNumeric.html).[Parse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.SpannerNumeric.html#Google_Cloud_Spanner_V1_SpannerNumeric_Parse_System_String_)("99999999999999999999999999999.99") },
            };
            // Create connection to Cloud Spanner.
            using var connection = new [SpannerConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html)(connectionString);
            await connection.[OpenAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html#Google_Cloud_Spanner_Data_SpannerConnection_OpenAsync_Google_Cloud_Spanner_Data_SpannerTransactionCreationOptions_Google_Cloud_Spanner_Data_SpannerTransactionOptions_System_Threading_CancellationToken_)();
    
            var affectedRows = await Task.WhenAll(venues.[Select](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerCommandType.html#Google_Cloud_Spanner_Data_SpannerCommandType_Select)(venue =>
            {
                // Update rows in the Venues table.
                using var cmd = connection.[CreateUpdateCommand](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html#Google_Cloud_Spanner_Data_SpannerConnection_CreateUpdateCommand_System_String_Google_Cloud_Spanner_Data_SpannerParameterCollection_)("Venues", new [SpannerParameterCollection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerParameterCollection.html)
                {
                    { "VenueId", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[Int64](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_Int64), venue.VenueId },
                    { "Revenue", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[Numeric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_Numeric), venue.Revenue }
                });
                return cmd.ExecuteNonQueryAsync();
            }));
    
            Console.WriteLine("Data updated.");
            return affectedRows.Sum();
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
    
    func updateDataWithNumericColumn(w io.Writer, db string) error {
    	ctx := context.Background()
    
    	client, err := spanner.NewClient(ctx, db)
    	if err != nil {
    		return err
    	}
    	defer client.Close()
    
    	cols := []string{"VenueId", "Revenue"}
    	_, err = client.[Apply](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Client_Apply)(ctx, []*spanner.Mutation{
    		spanner.Update("Venues", cols, []interface{}{4, "35000"}),
    		spanner.Update("Venues", cols, []interface{}{19, "104500"}),
    		spanner.Update("Venues", cols, []interface{}{42, "99999999999999999999999999999.99"}),
    	})
    	return err
    }
    

### Java

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.spanner.[DatabaseClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.DatabaseClient.html);
    import com.google.cloud.spanner.[DatabaseId](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.DatabaseId.html);
    import com.google.cloud.spanner.[Mutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Mutation.html);
    import com.google.cloud.spanner.[Spanner](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html);
    import com.google.cloud.spanner.[SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html);
    import com.google.common.collect.ImmutableList;
    import java.math.BigDecimal;
    
    class UpdateNumericDataSample {
    
      static void updateNumericData() {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project";
        String instanceId = "my-instance";
        String databaseId = "my-database";
    
        try ([Spanner](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html) spanner =
            [SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html).newBuilder().setProjectId(projectId).build().getService()) {
          [DatabaseClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.DatabaseClient.html) client =
              spanner.getDatabaseClient([DatabaseId](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.DatabaseId.html).of(projectId, instanceId, databaseId));
          updateNumericData(client);
        }
      }
    
      static void updateNumericData([DatabaseClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.DatabaseClient.html) client) {
        client.[write](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.DatabaseClient.html#com_google_cloud_spanner_DatabaseClient_write_java_lang_Iterable_com_google_cloud_spanner_Mutation__)(
            ImmutableList.of(
                Mutation.newInsertOrUpdateBuilder("Venues")
                    .set("VenueId")
                    .to(4L)
                    .set("Revenue")
                    .to(new BigDecimal("35000"))
                    .build(),
                Mutation.newInsertOrUpdateBuilder("Venues")
                    .set("VenueId")
                    .to(19L)
                    .set("Revenue")
                    .to(new BigDecimal("104500"))
                    .build(),
                Mutation.newInsertOrUpdateBuilder("Venues")
                    .set("VenueId")
                    .to(42L)
                    .set("Revenue")
                    .to(new BigDecimal("99999999999999999999999999999.99"))
                    .build()));
        System.out.println("Venues successfully updated");
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
    
    // Creates a client.
    const spanner = new [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)({
      projectId: projectId,
    });
    let database;
    try {
      // Gets a reference to a Cloud Spanner instance and database.
      const instance = spanner.instance(instanceId);
      database = instance.database(databaseId);
    
      // Instantiate Spanner table objects.
      const venuesTable = database.table('Venues');
    
      const data = [
        {
          VenueId: '4',
          Revenue: [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html).[numeric](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)('35000'),
          LastUpdateTime: 'spanner.commit_timestamp()',
        },
        {
          VenueId: '19',
          Revenue: [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html).[numeric](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)('104500'),
          LastUpdateTime: 'spanner.commit_timestamp()',
        },
        {
          VenueId: '42',
          Revenue: [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html).[numeric](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)('99999999999999999999999999999.99'),
          LastUpdateTime: 'spanner.commit_timestamp()',
        },
      ];
    
      // Updates rows in the Venues table.
      await venuesTable.update(data);
      console.log('Updated data.');
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
     * Updates sample data in a table with a NUMERIC column.
     *
     * Before executing this method, a new column Revenue has to be added to the Venues
     * table by applying the DDL statement "ALTER TABLE Venues ADD COLUMN Revenue NUMERIC".
     *
     * Example:
     * ```
     * update_data_with_numeric_column($instanceId, $databaseId);
     * ```
     *
     * @param string $instanceId The Spanner instance ID.
     * @param string $databaseId The Spanner database ID.
     */
    function update_data_with_numeric_column(string $instanceId, string $databaseId): void
    {
        $spanner = new SpannerClient();
        $instance = $spanner->instance($instanceId);
        $database = $instance->database($databaseId);
    
        $database->transaction(['singleUse' => true])
            ->updateBatch('Venues', [
                ['VenueId' => 4, 'Revenue' => $spanner->numeric('35000')],
                ['VenueId' => 19, 'Revenue' => $spanner->numeric('104500')],
                ['VenueId' => 42, 'Revenue' => $spanner->numeric('99999999999999999999999999999.99')],
            ])
            ->commit();
    
        print('Updated data.' . PHP_EOL);
    }

### Python

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def update_data_with_numeric(instance_id, database_id):
        """Updates Venues tables in the database with the NUMERIC
        column.
    
        This updates the `Revenue` column which must be created before
        running this sample. You can add the column by running the
        `add_numeric_column` sample or by running this DDL statement
         against your database:
    
            ALTER TABLE Venues ADD COLUMN Revenue NUMERIC
        """
        spanner_client = spanner.Client()
        instance = spanner_client.instance(instance_id)
    
        database = instance.database(database_id)
    
        with database.batch() as batch:
            batch.update(
                table="Venues",
                columns=("VenueId", "Revenue"),
                values=[
                    (4, decimal.Decimal("35000")),
                    (19, decimal.Decimal("104500")),
                    (42, decimal.Decimal("99999999999999999999999999999.99")),
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
    
    client.commit do |c|
      c.update "Venues", [
        { VenueId: 4, Revenue: "35000" },
        { VenueId: 19, Revenue: "104500" },
        { VenueId: 42, Revenue: "99999999999999999999999999999.99" }
      ]
    end
    
    puts "Updated data"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudspanner). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
