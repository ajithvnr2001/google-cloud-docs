---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-quickstart/
title: Bigtable quickstart \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:43:43.658530+00:00
---

# Bigtable quickstart  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  Bigtable quickstart Stay organized with collections  Save and categorize content based on your preferences. 

Quickstart for Cloud Bigtable which shows connecting to an instance and reading a row from a table.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries)



## Code sample

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    #include "google/cloud/bigtable/table.h"
    
    int main(int argc, char* argv[]) try {
      if (argc != 4 && argc != 5) {
        std::string const cmd = argv[0];
        auto last_slash = std::string(cmd).find_last_of('/');
        std::cerr << "Usage: " << cmd.substr(last_slash + 1)
                  << " <project_id> <instance_id> <table_id> [app_profile_id]\n";
        return 1;
      }
    
      std::string const project_id = argv[1];
      std::string const instance_id = argv[2];
      std::string const table_id = argv[3];
      std::string const app_profile_id = (argc == 5 ? argv[4] : "default");
    
      // Create a namespace alias to make the code easier to read.
      namespace cbt = ::google::cloud::bigtable;
    
      cbt::Table table(
          cbt::MakeDataConnection(),
          cbt::TableResource(project_id, instance_id, table_id),
          google::cloud::Options{}.set<cbt::AppProfileIdOption>(app_profile_id));
    
      std::string row_key = "r1";
      std::string column_family = "cf1";
    
      std::cout << "Getting a single row by row key:" << std::flush;
      google::cloud::StatusOr<std::pair<bool, cbt::Row>> result =
          table.ReadRow(row_key, cbt::Filter::FamilyRegex(column_family));
      if (!result) throw std::move(result).status();
      if (!result->first) {
        std::cout << "Cannot find row " << row_key << " in the table: " << table_id
                  << "\n";
        return 0;
      }
    
      cbt::Cell const& cell = result->second.cells().front();
      std::cout << cell.family_name() << ":" << cell.column_qualifier() << "    @ "
                << cell.timestamp().count() << "us\n"
                << '"' << cell.value() << '"' << "\n";
    
      return 0;
    } catch (google::cloud::Status const& status) {
      std::cerr << "google::cloud::Status thrown: " << status << "\n";
      return 1;
    }

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using [Google.Cloud.Bigtable.Common.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.html);
    // Imports the Google Cloud client library
    using [Google.Cloud.Bigtable.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.html);
    
    namespace GoogleCloudSamples.Bigtable
    {
        public class QuickStart
        {
            public static int Main(string[] args)
            {
                // Your Google Cloud Platform project ID
                const string projectId = "YOUR-PROJECT-ID";
                // The name of the Cloud Bigtable instance
                const string instanceId = "YOUR-INSTANCE-ID";
                // The name of the Cloud Bigtable table
                const string tableId = "my-table";
    
                try
                {
                    // Creates a Bigtable client
                    [BigtableClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient.html) bigtableClient = [BigtableClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient.html#Google_Cloud_Bigtable_V2_BigtableClient_Create)();
    
                    // Read a row from my-table using a row key
                    [Row](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Row.html) row = bigtableClient.[ReadRow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient.html#Google_Cloud_Bigtable_V2_BigtableClient_ReadRow_Google_Cloud_Bigtable_Common_V2_TableName_Google_Cloud_Bigtable_Common_V2_BigtableByteString_Google_Cloud_Bigtable_V2_RowFilter_Google_Api_Gax_Grpc_CallSettings_)(
                        new [TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)(projectId, instanceId, tableId), "r1", [RowFilters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilters.html).[CellsPerRowLimit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilters.html#Google_Cloud_Bigtable_V2_RowFilters_CellsPerRowLimit_System_Int32_)(1));
                    // Print the row key and data (column value, labels, timestamp)
                    Console.WriteLine($"{"Row key:",-30}{row.[Key](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Row.html#Google_Cloud_Bigtable_V2_Row_Key).ToStringUtf8()}\n" +
                                      $"{"  Column Family:",-30}{row.[Families](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Row.html#Google_Cloud_Bigtable_V2_Row_Families)[0].Name}\n" +
                                      $"{"    Column Qualifyer:",-30}{row.[Families](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Row.html#Google_Cloud_Bigtable_V2_Row_Families)[0].Columns[0].Qualifier.ToStringUtf8()}\n" +
                                      $"{"      Value:",-30}{row.[Families](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Row.html#Google_Cloud_Bigtable_V2_Row_Families)[0].Columns[0].[Cells](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Column.html#Google_Cloud_Bigtable_V2_Column_Cells)[0].[Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Value.html).ToStringUtf8()}\n" +
                                      $"{"      Labels:",-30}{row.[Families](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Row.html#Google_Cloud_Bigtable_V2_Row_Families)[0].Columns[0].[Cells](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Column.html#Google_Cloud_Bigtable_V2_Column_Cells)[0].Labels}\n" +
                                      $"{"      Timestamp:",-30}{row.[Families](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Row.html#Google_Cloud_Bigtable_V2_Row_Families)[0].Columns[0].[Cells](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Column.html#Google_Cloud_Bigtable_V2_Column_Cells)[0].TimestampMicros}\n");
                }
                catch (Exception ex)
                {
                    // Handle error performing the read operation
                    Console.WriteLine($"Error reading row r1: {ex.Message}");
                }
                return 0;
            }
        }
    }

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Quickstart is a sample program demonstrating use of the Cloud Bigtable client
    // library to read a row from an existing table.
    package main
    
    import (
    	"context"
    	"flag"
    	"log"
    
    	"cloud.google.com/go/bigtable"
    )
    
    func main() {
    	projectID := "my-project-id"   // The Google Cloud Platform project ID
    	instanceID := "my-instance-id" // The Google Cloud Bigtable instance ID
    	tableID := "my-table"          // The Google Cloud Bigtable table
    
    	ctx := context.Background()
    
    	// Set up Bigtable data operations client.
    	client, err := bigtable.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Client_NewClient)(ctx, projectID, instanceID)
    	if err != nil {
    		log.Fatalf("Could not create data operations client: %v", err)
    	}
    
    	tbl := client.[Open](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Client_Open)(tableID)
    
    	// Read data in a row using a row key
    	rowKey := "r1"
    	columnFamilyName := "cf1"
    
    	log.Printf("Getting a single row by row key:")
    	row, err := tbl.ReadRow(ctx, rowKey)
    	if err != nil {
    		log.Fatalf("Could not read row with key %s: %v", rowKey, err)
    	}
    	log.Printf("Row key: %s\n", rowKey)
    	log.Printf("Data: %s\n", string(row[columnFamilyName][0].[Value](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/apiv2/bigtablepb.html#cloud_google_com_go_bigtable_apiv2_bigtablepb_Value)))
    
    	if err = client.Close(); err != nil {
    		log.Fatalf("Could not close data operations client: %v", err)
    	}
    }
    

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.rpc.[NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html);
    import com.google.cloud.bigtable.data.v2.[BigtableDataClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html);
    import com.google.cloud.bigtable.data.v2.[BigtableDataSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataSettings.html);
    import com.google.cloud.bigtable.data.v2.models.[Row](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Row.html);
    import com.google.cloud.bigtable.data.v2.models.[RowCell](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.RowCell.html);
    import com.google.cloud.bigtable.data.v2.models.[TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.TableId.html);
    
    public class Quickstart {
    
      public static void main(String... args) {
        String projectId = args[0]; // my-gcp-project-id
        String instanceId = args[1]; // my-bigtable-instance-id
        String tableId = args[2]; // my-bigtable-table-id
    
        quickstart(projectId, instanceId, tableId);
      }
    
      public static void quickstart(String projectId, String instanceId, String tableId) {
        [BigtableDataSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataSettings.html) settings =
            [BigtableDataSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataSettings.html).newBuilder().[setProjectId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataSettings.Builder.html#com_google_cloud_bigtable_data_v2_BigtableDataSettings_Builder_setProjectId_java_lang_String_)(projectId).[setInstanceId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataSettings.Builder.html#com_google_cloud_bigtable_data_v2_BigtableDataSettings_Builder_setInstanceId_java_lang_String_)(instanceId).build();
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([BigtableDataClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html) dataClient = [BigtableDataClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html).create(settings)) {
          System.out.println("\nReading a single row by row key");
          [Row](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Row.html) row = dataClient.[readRow](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html#com_google_cloud_bigtable_data_v2_BigtableDataClient_readRow_com_google_cloud_bigtable_data_v2_models_TargetId_com_google_protobuf_ByteString_)([TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.TableId.html).of(tableId), "r1");
          System.out.println("Row: " + row.[getKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Row.html#com_google_cloud_bigtable_data_v2_models_Row_getKey__)().toStringUtf8());
          for ([RowCell](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.RowCell.html) cell : row.[getCells](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Row.html#com_google_cloud_bigtable_data_v2_models_Row_getCells__)()) {
            System.out.printf(
                "Family: %s    Qualifier: %s    Value: %s%n",
                cell.getFamily(), cell.getQualifier().toStringUtf8(), cell.getValue().toStringUtf8());
          }
        } catch ([NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html) e) {
          System.err.println("Failed to read from a non-existent table: " + e.getMessage());
        } catch (Exception e) {
          System.out.println("Error during quickstart: \n" + e.toString());
        }
      }
    }

### Node.js

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const Bigtable = require('[@google-cloud/bigtable](https://docs.cloud.google.com/nodejs/docs/reference/bigtable/latest/overview.html)');
    
    async function quickstart(
      INSTANCE_ID = 'my-instance', // ID of the Cloud Bigtable instance
      TABLE_ID = 'my-table' // ID of the Cloud Bigtable table
    ) {
      const bigtable = Bigtable();
    
      // Connect to an existing instance:my-bigtable-instance
      const instance = bigtable.instance(INSTANCE_ID);
    
      // Connect to an existing table:my-table
      const table = instance.table(TABLE_ID);
    
      // Read a row from my-table using a row key
      const [singleRow] = await table.row('r1').get();
    
      // Print the row key and data (column value, labels, timestamp)
      const rowData = JSON.stringify(singleRow.data, null, 4);
      console.log(`Row key: ${singleRow.id}\nData: ${rowData}`);
    }

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Bigtable\BigtableClient;
    
    /** Uncomment and populate these variables in your code */
    // $projectId = 'The Google project ID';
    // $instanceId = 'The Bigtable instance ID';
    // $tableId = 'The Bigtable table ID';
    
    // Connect to an existing table with an existing instance.
    $dataClient = new BigtableClient([
        'projectId' => $projectId,
    ]);
    $table = $dataClient->table($instanceId, $tableId);
    $key = 'r1';
    // Read a row from my-table using a row key
    $row = $table->readRow($key);
    
    $columnFamilyId = 'cf1';
    $columnId = 'c1';
    // Get the Value from the Row, using the column_family_id and column_id
    $value = $row[$columnFamilyId][$columnId][0]['value'];
    
    printf("Row key: %s\nData: %s\n", $key, $value);

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    
    from google.cloud import [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest)
    
    
    def main(project_id="project-id", instance_id="instance-id", table_id="my-table"):
        # Create a Cloud Bigtable client.
        client = [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html)(project=project_id)
    
        # Connect to an existing Cloud Bigtable instance.
        instance = [client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.html).[instance](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html#google_cloud_bigtable_client_Client_instance)(instance_id)
    
        # Open an existing table.
        table = instance.table(table_id)
    
        row_key = "r1"
        row = table.read_row(row_key.encode("utf-8"))
    
        column_family_id = "cf1"
        column_id = "c1".encode("utf-8")
        value = row.[cells](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.row.PartialRowData.html#google_cloud_bigtable_row_PartialRowData_cells)[column_family_id][column_id][0].value.decode("utf-8")
    
        print("Row key: {}\nData: {}".format(row_key, value))
    
    
    if __name__ == "__main__":
        parser = argparse.ArgumentParser(
            description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter
        )
        parser.add_argument("project_id", help="Your Cloud Platform project ID.")
        parser.add_argument(
            "instance_id", help="ID of the Cloud Bigtable instance to connect to."
        )
        parser.add_argument(
            "--table", help="Existing table used in the quickstart.", default="my-table"
        )
    
        args = parser.parse_args()
        main(args.project_id, args.instance_id, args.table)

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Import google bigtable client lib
    require "google/cloud/bigtable"
    
    # Instantiates a client
    bigtable = Google::Cloud::[Bigtable](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable.html)
    
    # Your Cloud Bigtable instance ID
    # instance_id = "my-instance"
    
    # Your Cloud Bigtable table ID
    # table_id = "my-table"
    
    # Get table client
    table = bigtable.table instance_id, table_id
    
    # Read and print row
    p table.read_row "user0000001"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
