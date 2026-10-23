---
url: https://docs.cloud.google.com/spanner/docs/samples/spanner-dml-write-then-read/
title: DML write then read \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:19.794165+00:00
---

# DML write then read  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/samples/spanner-dml-write-then-read/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Samples ](https://docs.cloud.google.com/spanner/docs/samples)



#  DML write then read Stay organized with collections  Save and categorize content based on your preferences. 

Insert data and then read the inserted data.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Insert, update, and delete data using data manipulation language (DML)](https://docs.cloud.google.com/spanner/docs/dml-tasks)



## Code sample

### C++

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    void DmlWriteThenRead(google::cloud::spanner::Client client) {
      namespace spanner = ::google::cloud::spanner;
      using ::google::cloud::StatusOr;
    
      auto commit_result = client.Commit(
          [&client](spanner::Transaction txn) -> StatusOr<spanner::Mutations> {
            auto insert = client.ExecuteDml(
                txn, spanner::SqlStatement(
                         "INSERT INTO Singers (SingerId, FirstName, LastName)"
                         "  VALUES (11, 'Timothy', 'Campbell')"));
            if (!insert) return std::move(insert).status();
            // Read newly inserted record.
            spanner::SqlStatement select(
                "SELECT FirstName, LastName FROM Singers where SingerId = 11");
            using RowType = std::tuple<std::string, std::string>;
            auto rows = client.ExecuteQuery(std::move(txn), std::move(select));
            // Note: This mutator might be re-run, or its effects discarded, so
            // changing non-transactional state (e.g., by producing output) is,
            // in general, not something to be imitated.
            for (auto const& row : spanner::StreamOf<RowType>(rows)) {
              if (!row) return std::move(row).status();
              std::cout << "FirstName: " << std::get<0>(*row) << "\t";
              std::cout << "LastName: " << std::get<1>(*row) << "\n";
            }
            return spanner::Mutations{};
          });
      if (!commit_result) throw std::move(commit_result).status();
      std::cout << "Write then read succeeded [spanner_dml_write_then_read]\n";
    }

### C#

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Spanner.Data](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.html);
    using System;
    using System.Threading.Tasks;
    
    public class WriteAndReadUsingDmlCoreAsyncSample
    {
        public async Task<int> WriteAndReadUsingDmlCoreAsync(string projectId, string instanceId, string databaseId)
        {
            string connectionString = $"Data Source=projects/{projectId}/instances/{instanceId}/databases/{databaseId}";
    
            using var connection = new [SpannerConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html)(connectionString);
            await connection.[OpenAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html#Google_Cloud_Spanner_Data_SpannerConnection_OpenAsync_Google_Cloud_Spanner_Data_SpannerTransactionCreationOptions_Google_Cloud_Spanner_Data_SpannerTransactionOptions_System_Threading_CancellationToken_)();
    
            using var createDmlCmd = connection.[CreateDmlCommand](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html#Google_Cloud_Spanner_Data_SpannerConnection_CreateDmlCommand_System_String_Google_Cloud_Spanner_Data_SpannerParameterCollection_)(@"INSERT Singers (SingerId, FirstName, LastName) VALUES (11, 'Timothy', 'Campbell')");
            int rowCount = await createDmlCmd.ExecuteNonQueryAsync();
            Console.WriteLine($"{rowCount} row(s) inserted...");
    
            // Read newly inserted record.
            using var createSelectCmd = connection.[CreateSelectCommand](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerConnection.html#Google_Cloud_Spanner_Data_SpannerConnection_CreateSelectCommand_System_String_Google_Cloud_Spanner_Data_SpannerParameterCollection_)(@"SELECT FirstName, LastName FROM Singers WHERE SingerId = 11");
            using var reader = await createSelectCmd.[ExecuteReaderAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerCommand.html#Google_Cloud_Spanner_Data_SpannerCommand_ExecuteReaderAsync)();
            while (await reader.[ReadAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Data/latest/Google.Cloud.Spanner.Data.SpannerDataReader.html#Google_Cloud_Spanner_Data_SpannerDataReader_ReadAsync_System_Threading_CancellationToken_)())
            {
                Console.WriteLine($"{reader.GetFieldValue<string>("FirstName")}  {reader.GetFieldValue<string>("LastName")}");
            }
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
    	"google.golang.org/api/iterator"
    )
    
    func writeAndReadUsingDML(w io.Writer, db string) error {
    	ctx := context.Background()
    	client, err := spanner.NewClient(ctx, db)
    	if err != nil {
    		return err
    	}
    	defer client.Close()
    
    	_, err = client.ReadWriteTransaction(ctx, func(ctx context.Context, txn *spanner.ReadWriteTransaction) error {
    		// Insert Record
    		stmt := spanner.[Statement](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Statement){
    			SQL: `INSERT Singers (SingerId, FirstName, LastName)
    				VALUES (11, 'Timothy', 'Campbell')`,
    		}
    		rowCount, err := txn.Update(ctx, stmt)
    		if err != nil {
    			return err
    		}
    		fmt.Fprintf(w, "%d record(s) inserted.\n", rowCount)
    
    		// Read newly inserted record
    		stmt = spanner.[Statement](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Statement){SQL: `SELECT FirstName, LastName FROM Singers WHERE SingerId = 11`}
    		iter := txn.Query(ctx, stmt)
    		defer iter.Stop()
    
    		for {
    			row, err := iter.Next()
    			if err == iterator.Done || err != nil {
    				break
    			}
    			var firstName, lastName string
    			if err := row.[ColumnByName](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Row_ColumnByName)("FirstName", &firstName); err != nil {
    				return err
    			}
    			if err := row.[ColumnByName](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Row_ColumnByName)("LastName", &lastName); err != nil {
    				return err
    			}
    			fmt.Fprintf(w, "Found record name with %s, %s", firstName, lastName)
    		}
    		return err
    	})
    	return err
    }
    

### Java

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    static void writeAndReadUsingDml(DatabaseClient dbClient) {
      dbClient
          .readWriteTransaction()
          .run(transaction -> {
            // Insert record.
            String sql =
                "INSERT INTO Singers (SingerId, FirstName, LastName) "
                    + " VALUES (11, 'Timothy', 'Campbell')";
            long rowCount = transaction.executeUpdate(Statement.of(sql));
            System.out.printf("%d record inserted.\n", rowCount);
            // Read newly inserted record.
            sql = "SELECT FirstName, LastName FROM Singers WHERE SingerId = 11";
            // We use a try-with-resource block to automatically release resources held by
            // ResultSet.
            try (ResultSet resultSet = transaction.executeQuery(Statement.of(sql))) {
              while (resultSet.next()) {
                System.out.printf(
                    "%s %s\n",
                    resultSet.getString("FirstName"), resultSet.getString("LastName"));
              }
            }
            return null;
          });
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
    
    // Gets a reference to a Cloud Spanner instance and database
    const instance = spanner.instance(instanceId);
    const database = instance.database(databaseId);
    
    try {
      await database.[runTransactionAsync](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/database.html)(async transaction => {
        await transaction.[runUpdate](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/partitioneddml.html)({
          sql: `INSERT Singers (SingerId, FirstName, LastName)
            VALUES (11, 'Timothy', 'Campbell')`,
        });
    
        const [rows] = await transaction.run({
          sql: 'SELECT FirstName, LastName FROM Singers',
        });
        rows.forEach(row => {
          const json = row.toJSON();
          console.log(`${json.FirstName} ${json.LastName}`);
        });
    
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
    use Google\Cloud\Spanner\Transaction;
    
    /**
     * Writes then reads data inside a Transaction with a DML statement.
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
    function write_read_with_dml(string $instanceId, string $databaseId): void
    {
        $spanner = new SpannerClient();
        $instance = $spanner->instance($instanceId);
        $database = $instance->database($databaseId);
    
        $database->runTransaction(function (Transaction $t) {
            $rowCount = $t->executeUpdate(
                'INSERT Singers (SingerId, FirstName, LastName) '
                . " VALUES (11, 'Timothy', 'Campbell')");
    
            printf('Inserted %d row(s).' . PHP_EOL, $rowCount);
    
            $results = $t->execute('SELECT FirstName, LastName FROM Singers WHERE SingerId = 11');
    
            foreach ($results as $row) {
                printf('%s %s' . PHP_EOL, $row['FirstName'], $row['LastName']);
            }
    
            $t->commit();
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
    
    def write_then_read(transaction):
        # Insert record.
        row_ct = transaction.execute_update(
            "INSERT INTO Singers (SingerId, FirstName, LastName) "
            " VALUES (11, 'Timothy', 'Campbell')"
        )
        print("{} record(s) inserted.".format(row_ct))
    
        # Read newly inserted record.
        results = transaction.execute_sql(
            "SELECT FirstName, LastName FROM Singers WHERE SingerId = 11"
        )
        for result in results:
            print("FirstName: {}, LastName: {}".format(*result))
    
    database.run_in_transaction(write_then_read)

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
    
    client.transaction do |transaction|
      row_count = transaction.[execute_update](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-Transaction.html)(
        "INSERT INTO Singers (SingerId, FirstName, LastName) VALUES (11, 'Timothy', 'Campbell')"
      )
      puts "#{row_count} record updated."
      transaction.execute("SELECT FirstName, LastName FROM Singers WHERE SingerId = 11").rows.[each](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-BatchWriteResults.html) do |row|
        puts "#{row[:FirstName]} #{row[:LastName]}"
      end
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudspanner). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
