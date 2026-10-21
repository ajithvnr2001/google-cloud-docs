---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-writes-simple/
title: Perform a simple write \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:23:57.916086+00:00
---

# Perform a simple write  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-writes-simple/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  Perform a simple write Stay organized with collections  Save and categorize content based on your preferences. 

Performing a simple write API call: MutateRow. Make sure samples use multiple SetCells (mutations).

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Write examples](https://docs.cloud.google.com/bigtable/docs/writing-data)



## Code sample

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace cbt = ::google::cloud::bigtable;
    [](cbt::Table table) {
      auto timestamp = std::chrono::duration_cast<std::chrono::milliseconds>(
          std::chrono::system_clock::now().time_since_epoch());
    
      std::string row_key = "phone#4c410523#20190501";
      cbt::SingleRowMutation mutation(row_key);
      std::string column_family = "stats_summary";
    
      mutation.emplace_back(cbt::SetCell(column_family, "connected_cell",
                                         timestamp, std::int64_t{1}));
      mutation.emplace_back(cbt::SetCell(column_family, "connected_wifi",
                                         timestamp, std::int64_t{1}));
      mutation.emplace_back(
          cbt::SetCell(column_family, "os_build", timestamp, "PQ2A.190405.003"));
      google::cloud::Status status = table.Apply(std::move(mutation));
      if (!status.ok()) throw std::runtime_error(status.message());
      std::cout << "Successfully wrote row" << row_key << "\n";
    }

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using [Google.Cloud.Bigtable.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.html);
    using [Google.Cloud.Bigtable.Common.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.html);
    
    namespace Writes
    {
        public class WriteSimpleSample
        {
            /// <summary>
            /// Mutate one row in an existing table and column family. Updates multiple cells within that row using one API call.
            ///</summary>
            /// <param name="projectId">Your Google Cloud Project ID.</param>
            /// <param name="instanceId">Your Google Cloud Bigtable Instance ID.</param>
            /// <param name="tableId">Your Google Cloud Bigtable table ID.</param>
            public string WriteSimple(
                string projectId = "YOUR-PROJECT-ID",
                string instanceId = "YOUR-INSTANCE-ID",
                string tableId = "YOUR-TABLE-ID")
            {
                [BigtableClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient.html) bigtableClient = [BigtableClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient.html#Google_Cloud_Bigtable_V2_BigtableClient_Create)();
    
                [TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html) tableName = new [TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)(projectId, instanceId, tableId);
                [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html) rowkey = new [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html)("phone#4c410523#20190501");
                [BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion.html) timestamp = new [BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion.html)(DateTime.UtcNow);
                string COLUMN_FAMILY = "stats_summary";
    
                [Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation.html)[] mutations = {
                        [Mutations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutations.html).[SetCell](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutations.html#Google_Cloud_Bigtable_V2_Mutations_SetCell_System_String_Google_Cloud_Bigtable_Common_V2_BigtableByteString_Google_Cloud_Bigtable_Common_V2_BigtableByteString_System_Nullable_Google_Cloud_Bigtable_V2_BigtableVersion__)(COLUMN_FAMILY, "connected_cell", 1, timestamp),
                        [Mutations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutations.html).[SetCell](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutations.html#Google_Cloud_Bigtable_V2_Mutations_SetCell_System_String_Google_Cloud_Bigtable_Common_V2_BigtableByteString_Google_Cloud_Bigtable_Common_V2_BigtableByteString_System_Nullable_Google_Cloud_Bigtable_V2_BigtableVersion__)(COLUMN_FAMILY, "connected_wifi", 1, timestamp),
                        [Mutations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutations.html).[SetCell](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutations.html#Google_Cloud_Bigtable_V2_Mutations_SetCell_System_String_Google_Cloud_Bigtable_Common_V2_BigtableByteString_Google_Cloud_Bigtable_Common_V2_BigtableByteString_System_Nullable_Google_Cloud_Bigtable_V2_BigtableVersion__)(COLUMN_FAMILY, "os_build", "PQ2A.190405.003", timestamp)
                    };
                [MutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowResponse.html) mutateRowResponse = bigtableClient.[MutateRow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient.html#Google_Cloud_Bigtable_V2_BigtableClient_MutateRow_Google_Cloud_Bigtable_Common_V2_TableName_Google_Cloud_Bigtable_Common_V2_BigtableByteString_Google_Cloud_Bigtable_V2_Mutation___)(tableName, rowkey, mutations);
                Console.WriteLine(mutateRowResponse);
                return $"Successfully wrote row {rowkey}";
            }
        }
    }

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"encoding/binary"
    	"fmt"
    	"io"
    
    	"bytes"
    
    	"cloud.google.com/go/bigtable"
    )
    
    func writeSimple(w io.Writer, projectID, instanceID string, tableName string) error {
    	// projectID := "my-project-id"
    	// instanceID := "my-instance-id"
    	// tableName := "mobile-time-series"
    
    	ctx := context.Background()
    	client, err := bigtable.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Client_NewClient)(ctx, projectID, instanceID)
    	if err != nil {
    		return fmt.Errorf("bigtable.NewClient: %w", err)
    	}
    	defer client.Close()
    	tbl := client.[Open](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Client_Open)(tableName)
    	columnFamilyName := "stats_summary"
    	timestamp := bigtable.[Now](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Timestamp_Now)()
    
    	mut := bigtable.[NewMutation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Mutation_NewMutation)()
    	buf := new(bytes.Buffer)
    	binary.Write(buf, binary.BigEndian, int64(1))
    
    	mut.[Set](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Mutation_Set)(columnFamilyName, "connected_cell", timestamp, buf.Bytes())
    	mut.[Set](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Mutation_Set)(columnFamilyName, "connected_wifi", timestamp, buf.Bytes())
    	mut.[Set](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Mutation_Set)(columnFamilyName, "os_build", timestamp, []byte("PQ2A.190405.003"))
    
    	rowKey := "phone#4c410523#20190501"
    	if err := tbl.Apply(ctx, rowKey, mut); err != nil {
    		return fmt.Errorf("Apply: %w", err)
    	}
    
    	fmt.Fprintf(w, "Successfully wrote row: %s\n", rowKey)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.bigtable.data.v2.[BigtableDataClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html);
    import com.google.cloud.bigtable.data.v2.models.[RowMutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.RowMutation.html);
    import com.google.cloud.bigtable.data.v2.models.[TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.TableId.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    
    public class WriteSimple {
      private static final String COLUMN_FAMILY_NAME = "stats_summary";
    
      public static void writeSimple(String projectId, String instanceId, String tableId) {
        // String projectId = "my-project-id";
        // String instanceId = "my-instance-id";
        // String tableId = "mobile-time-series";
    
        try ([BigtableDataClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html) dataClient = [BigtableDataClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html).create(projectId, instanceId)) {
          long timestamp = System.currentTimeMillis() * 1000;
    
          String rowkey = "phone#4c410523#20190501";
    
          [RowMutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.RowMutation.html) rowMutation =
              [RowMutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.RowMutation.html).create([TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.TableId.html).of(tableId), rowkey)
                  .setCell(
                      COLUMN_FAMILY_NAME,
                      [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)("connected_cell".getBytes()),
                      timestamp,
                      1)
                  .setCell(
                      COLUMN_FAMILY_NAME,
                      [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)("connected_wifi".getBytes()),
                      timestamp,
                      1)
                  .setCell(COLUMN_FAMILY_NAME, "os_build", timestamp, "PQ2A.190405.003");
    
          dataClient.[mutateRow](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html#com_google_cloud_bigtable_data_v2_BigtableDataClient_mutateRow_com_google_cloud_bigtable_data_v2_models_RowMutation_)(rowMutation);
          System.out.printf("Successfully wrote row %s", rowkey);
    
        } catch (Exception e) {
          System.out.println("Error during WriteSimple: \n" + e.toString());
        }
      }
    }
    

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Bigtable\BigtableClient;
    use Google\Cloud\Bigtable\DataUtil;
    use Google\Cloud\Bigtable\Mutations;
    
    /**
     * Write data in a table
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance
     * @param string $tableId The ID of the table where the data needs to be written
     */
    function write_simple(
        string $projectId,
        string $instanceId,
        string $tableId = 'mobile-time-series'
    ): void {
        // Connect to an existing table with an existing instance.
        $dataClient = new BigtableClient([
            'projectId' => $projectId,
        ]);
        $table = $dataClient->table($instanceId, $tableId);
    
        $timestampMicros = time() * 1000 * 1000;
        $columnFamilyId = 'stats_summary';
        $mutations = (new Mutations())
        ->upsert($columnFamilyId, 'connected_cell', '1', $timestampMicros)
        ->upsert($columnFamilyId, 'connected_wifi', DataUtil::intToByteString(1), $timestampMicros)
        ->upsert($columnFamilyId, 'os_build', 'PQ2A.190405.003', $timestampMicros);
    
        $table->mutateRow('phone#4c410523#20190501', $mutations);
    
        printf('Successfully wrote row.' . PHP_EOL);
    }

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from datetime import datetime, timezone
    
    from google.cloud import [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest)
    
    
    def write_simple(project_id, instance_id, table_id):
        client = [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html)(project=project_id, admin=True)
        instance = [client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.html).[instance](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html#google_cloud_bigtable_client_Client_instance)(instance_id)
        table = instance.table(table_id)
    
        timestamp = datetime.now(timezone.utc)
        column_family_id = "stats_summary"
    
        row_key = "phone#4c410523#20190501"
    
        row = table.[direct_row](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.table.Table.html#google_cloud_bigtable_table_Table_direct_row)(row_key)
        row.set_cell(column_family_id, "connected_cell", 1, timestamp)
        row.set_cell(column_family_id, "connected_wifi", 1, timestamp)
        row.set_cell(column_family_id, "os_build", "PQ2A.190405.003", timestamp)
    
        row.commit()
    
        print("Successfully wrote row {}.".format(row_key))
    
    

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # instance_id = "my-instance"
    # table_id    = "my-table"
    table = bigtable.table instance_id, table_id
    column_family = "stats_summary"
    timestamp = (Time.now.to_f * 1_000_000).round(-3)
    
    rowkey = "phone#4c410523#20190501"
    entry = table.new_mutation_entry(rowkey)
                 .set_cell(column_family, "connected_cell", 1, timestamp: timestamp)
                 .set_cell(column_family, "connected_wifi", 1, timestamp: timestamp)
                 .set_cell(column_family, "os_build", "PQ2A.190405.003", timestamp: timestamp)
    
    table.mutate_row entry
    puts "Successfully wrote row #{rowkey}"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
