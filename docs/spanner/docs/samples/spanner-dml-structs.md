---
url: https://docs.cloud.google.com/spanner/docs/samples/spanner-dml-structs/
title: DML update data with STRUCT \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:09:28.728216+00:00
---

# DML update data with STRUCT  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/samples/spanner-dml-structs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Samples ](https://docs.cloud.google.com/spanner/docs/samples)



#  DML update data with STRUCT Stay organized with collections  Save and categorize content based on your preferences. 

Update data by using DML with a STRUCT object.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [GoogleSQL data manipulation language](https://docs.cloud.google.com/spanner/docs/reference/standard-sql/dml-syntax)
  * [Insert, update, and delete data using data manipulation language (DML)](https://docs.cloud.google.com/spanner/docs/dml-tasks)
  * [Working with STRUCT objects](https://docs.cloud.google.com/spanner/docs/structs)



## Code sample

### C++

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    void DmlStructs(google::cloud::spanner::Client client) {
      namespace spanner = ::google::cloud::spanner;
      std::int64_t rows_modified = 0;
      auto commit_result =
          client.Commit([&client, &rows_modified](spanner::Transaction const& txn)
                            -> google::cloud::StatusOr<spanner::Mutations> {
            auto singer_info = std::make_tuple("Marc", "Richards");
            auto sql = spanner::SqlStatement(
                "UPDATE Singers SET FirstName = 'Keith' WHERE "
                "STRUCT<FirstName String, LastName String>(FirstName, LastName) "
                "= @name",
                {{"name", spanner::Value(std::move(singer_info))}});
            auto dml_result = client.ExecuteDml(txn, std::move(sql));
            if (!dml_result) return std::move(dml_result).status();
            rows_modified = dml_result->RowsModified();
            return spanner::Mutations{};
          });
      if (!commit_result) throw std::move(commit_result).status();
      std::cout << rows_modified
                << " update was successful [spanner_dml_structs]\n";
    }

### C#

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Spanner.Data](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.html);
    using System;
    using System.Threading.Tasks;
    
    public class UpdateUsingDmlWithStructCoreAsyncSample
    {
        public async Task<int> UpdateUsingDmlWithStructCoreAsync(string projectId, string instanceId, string databaseId)
        {
            var nameStruct = new [SpannerStruct](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerStruct.html)
            {
                { "FirstName", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[String](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_String), "Timothy" },
                { "LastName", [SpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html).[String](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDbType.html#Google_Cloud_Spanner_Data_SpannerDbType_String), "Campbell" }
            };
            string connectionString = $"Data Source=projects/{projectId}/instances/{instanceId}/databases/{databaseId}";
    
            using var connection = new [SpannerConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html)(connectionString);
            await connection.[OpenAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html#Google_Cloud_Spanner_Data_SpannerConnection_OpenAsync_Google_Cloud_Spanner_Data_SpannerTransactionCreationOptions_Google_Cloud_Spanner_Data_SpannerTransactionOptions_System_Threading_CancellationToken_)();
    
            using var cmd = connection.[CreateDmlCommand](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html#Google_Cloud_Spanner_Data_SpannerConnection_CreateDmlCommand_System_String_Google_Cloud_Spanner_Data_SpannerParameterCollection_)("UPDATE Singers SET LastName = 'Grant' WHERE STRUCT<FirstName STRING, LastName STRING>(FirstName, LastName) = @name");
            cmd.[Parameters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerCommand.html#Google_Cloud_Spanner_Data_SpannerCommand_Parameters).Add("name", nameStruct.[GetSpannerDbType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerStruct.html#Google_Cloud_Spanner_Data_SpannerStruct_GetSpannerDbType)(), nameStruct);
            int rowCount = await cmd.ExecuteNonQueryAsync();
    
            Console.WriteLine($"{rowCount} row(s) updated...");
            return rowCount;
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
    )
    
    func updateUsingDMLStruct(w io.Writer, db string) error {
    	ctx := context.Background()
    	client, err := spanner.NewClient(ctx, db)
    	if err != nil {
    		return err
    	}
    	defer client.Close()
    
    	_, err = client.ReadWriteTransaction(ctx, func(ctx context.Context, txn *spanner.ReadWriteTransaction) error {
    		type name struct {
    			FirstName string
    			LastName  string
    		}
    		var singerInfo = name{"Timothy", "Campbell"}
    
    		stmt := spanner.[Statement](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Statement){
    			SQL: `Update Singers Set LastName = 'Grant'
    				WHERE STRUCT<FirstName String, LastName String>(Firstname, LastName) = @name`,
    			Params: map[string]interface{}{"name": singerInfo},
    		}
    		rowCount, err := txn.Update(ctx, stmt)
    		if err != nil {
    			return err
    		}
    		fmt.Fprintf(w, "%d record(s) inserted.\n", rowCount)
    		return nil
    	})
    	return err
    }
    

### Java

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    static void updateUsingDmlWithStruct(DatabaseClient dbClient) {
      Struct name =
          Struct.newBuilder().set("FirstName").to("Timothy").set("LastName").to("Campbell").build();
      Statement s =
          Statement.newBuilder(
                  "UPDATE Singers SET LastName = 'Grant' "
                      + "WHERE STRUCT<FirstName STRING, LastName STRING>(FirstName, LastName) "
                      + "= @name")
              .bind("name")
              .to(name)
              .build();
      dbClient
          .readWriteTransaction()
          .run(transaction -> {
            long rowCount = transaction.executeUpdate(s);
            System.out.printf("%d record updated.\n", rowCount);
            return null;
          });
    }

### Node.js

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const {Spanner} = require('[@google-cloud/spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/overview.html)');
    
    const nameStruct = [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html).[struct](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)({
      FirstName: 'Timothy',
      LastName: 'Campbell',
    });
    
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
    
    // Gets a reference to a Cloud Spanner instance and database
    const instance = spanner.instance(instanceId);
    const database = instance.database(databaseId);
    
    try {
      await database.[runTransactionAsync](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/database.html)(async transaction => {
        const [rowCount] = await transaction.runUpdate({
          sql: `UPDATE Singers SET LastName = 'Grant'
          WHERE STRUCT<FirstName STRING, LastName STRING>(FirstName, LastName) = @name`,
          params: {
            name: nameStruct,
          },
        });
    
        console.log(`Successfully updated ${rowCount} record.`);
        await transaction.commit();
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
    use Google\Cloud\Spanner\Transaction;
    use Google\Cloud\Spanner\StructType;
    use Google\Cloud\Spanner\StructValue;
    
    /**
     * Update data with a DML statement using Structs.
     *
     * The database and table must already exist and can be created using
     * `create_database`.
     * Example:
     * ```
     * insert_data($instanceId, $databaseId);
     * ```
     *
     * @param string $instanceId The Spanner instance ID.
     * @param string $databaseId The Spanner database ID.
     */
    function update_data_with_dml_structs(string $instanceId, string $databaseId): void
    {
        $spanner = new SpannerClient();
        $instance = $spanner->instance($instanceId);
        $database = $instance->database($databaseId);
    
        $database->runTransaction(function (Transaction $t) {
            $nameValue = (new StructValue)
                ->add('FirstName', 'Timothy')
                ->add('LastName', 'Campbell');
            $nameType = (new StructType)
                ->add('FirstName', Database::TYPE_STRING)
                ->add('LastName', Database::TYPE_STRING);
    
            $rowCount = $t->executeUpdate(
                "UPDATE Singers SET LastName = 'Grant' "
                 . 'WHERE STRUCT<FirstName STRING, LastName STRING>(FirstName, LastName) '
                 . '= @name',
                [
                    'parameters' => [
                        'name' => $nameValue
                    ],
                    'types' => [
                        'name' => $nameType
                    ]
                ]);
            $t->commit();
            printf('Updated %d row(s).' . PHP_EOL, $rowCount);
        });
    }

### Python

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"
    
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)
    
    record_type = param_types.Struct(
        [
            param_types.StructField("FirstName", param_types.STRING),
            param_types.StructField("LastName", param_types.STRING),
        ]
    )
    record_value = ("Timothy", "Campbell")
    
    def write_with_struct(transaction):
        row_ct = transaction.execute_update(
            "UPDATE Singers SET LastName = 'Grant' "
            "WHERE STRUCT<FirstName STRING, LastName STRING>"
            "(FirstName, LastName) = @name",
            params={"name": record_value},
            param_types={"name": record_type},
        )
        print("{} record(s) updated.".format(row_ct))
    
    database.run_in_transaction(write_with_struct)

### Ruby

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project_id  = "Your Google Cloud project ID"
    # instance_id = "Your Spanner instance ID"
    # database_id = "Your Spanner database ID"
    
    require "google/cloud/spanner"
    
    spanner = Google::Cloud::[Spanner](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-instance-v1/latest/Google-Cloud-Spanner.html).new project: project_id
    client  = spanner.[client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-Project.html) instance_id, database_id
    row_count = 0
    name_struct = { FirstName: "Timothy", LastName: "Campbell" }
    
    client.transaction do |transaction|
      row_count = transaction.[execute_update](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-Transaction.html)(
        "UPDATE Singers SET LastName = 'Grant'
         WHERE STRUCT<FirstName STRING, LastName STRING>(FirstName, LastName) = @name",
        params: { name: name_struct }
      )
    end
    
    puts "#{row_count} record updated."

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudspanner). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
