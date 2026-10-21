---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-writes-batch/
title: Perform batch writes \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:23:58.763780+00:00
---

# Perform batch writes  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-writes-batch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  Perform batch writes Stay organized with collections  Save and categorize content based on your preferences. 

Write multiple rows at once. This type of write makes a MutateRows API request.

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
      std::string column_family = "stats_summary";
    
      cbt::BulkMutation bulk;
      bulk.emplace_back(cbt::SingleRowMutation(
          "tablet#a0b81f74#20190501",
          cbt::SetCell(column_family, "connected_cell", timestamp,
                       std::int64_t{1}),
          cbt::SetCell(column_family, "os_build", timestamp, "12155.0.0-rc1")));
      bulk.emplace_back(cbt::SingleRowMutation(
          "tablet#a0b81f74#20190502",
          cbt::SetCell(column_family, "connected_cell", timestamp,
                       std::int64_t{1}),
          cbt::SetCell(column_family, "os_build", timestamp, "12145.0.0-rc6")));
    
      std::vector<cbt::FailedMutation> failures =
          table.BulkApply(std::move(bulk));
      if (failures.empty()) {
        std::cout << "Successfully wrote 2 rows.\n";
        return;
      }
      std::cerr << "The following mutations failed:\n";
      for (auto const& f : failures) {
        std::cerr << "rowkey[" << f.original_index() << "]=" << f.status()
                  << "\n";
      }
    }

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using [Google.Cloud.Bigtable.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.html);
    using [Google.Cloud.Bigtable.Common.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.html);
    
    namespace Writes
    {
        public class WriteBatchSample
        {
            /// <summary>
            /// Mutate multiple rows in an existing table and column family. Updates multiple cells within each row.
            ///</summary>
            /// <param name="projectId">Your Google Cloud Project ID.</param>
            /// <param name="instanceId">Your Google Cloud Bigtable Instance ID.</param>
            /// <param name="tableId">Your Google Cloud Bigtable table ID.</param>
            public string WriteBatch(
                string projectId = "YOUR-PROJECT-ID",
                string instanceId = "YOUR-INSTANCE-ID",
                string tableId = "YOUR-TABLE-ID")
            {
                [BigtableClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient.html) bigtableClient = [BigtableClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient.html#Google_Cloud_Bigtable_V2_BigtableClient_Create)();
    
                [TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html) tableName = new [TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)(projectId, instanceId, tableId);
                [BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion.html) timestamp = new [BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion.html)(DateTime.UtcNow);
                string COLUMN_FAMILY = "stats_summary";
    
                MutateRowsRequest.Types.Entry mutations1 = [Mutations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutations.html).[CreateEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutations.html#Google_Cloud_Bigtable_V2_Mutations_CreateEntry_Google_Cloud_Bigtable_Common_V2_BigtableByteString_Google_Cloud_Bigtable_V2_Mutation___)(new [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html)("tablet#a0b81f74#20190501"),
                    [Mutations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutations.html).[SetCell](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutations.html#Google_Cloud_Bigtable_V2_Mutations_SetCell_System_String_Google_Cloud_Bigtable_Common_V2_BigtableByteString_Google_Cloud_Bigtable_Common_V2_BigtableByteString_System_Nullable_Google_Cloud_Bigtable_V2_BigtableVersion__)(COLUMN_FAMILY, "connected_cell", 1, timestamp),
                    [Mutations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutations.html).[SetCell](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutations.html#Google_Cloud_Bigtable_V2_Mutations_SetCell_System_String_Google_Cloud_Bigtable_Common_V2_BigtableByteString_Google_Cloud_Bigtable_Common_V2_BigtableByteString_System_Nullable_Google_Cloud_Bigtable_V2_BigtableVersion__)(COLUMN_FAMILY, "os_build", "12155.0.0-rc1", timestamp)
                );
                MutateRowsRequest.Types.Entry mutations2 = [Mutations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutations.html).[CreateEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutations.html#Google_Cloud_Bigtable_V2_Mutations_CreateEntry_Google_Cloud_Bigtable_Common_V2_BigtableByteString_Google_Cloud_Bigtable_V2_Mutation___)(new [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html)("tablet#a0b81f74#20190502"),
                    [Mutations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutations.html).[SetCell](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutations.html#Google_Cloud_Bigtable_V2_Mutations_SetCell_System_String_Google_Cloud_Bigtable_Common_V2_BigtableByteString_Google_Cloud_Bigtable_Common_V2_BigtableByteString_System_Nullable_Google_Cloud_Bigtable_V2_BigtableVersion__)(COLUMN_FAMILY, "connected_cell", 1, timestamp),
                    [Mutations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutations.html).[SetCell](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutations.html#Google_Cloud_Bigtable_V2_Mutations_SetCell_System_String_Google_Cloud_Bigtable_Common_V2_BigtableByteString_Google_Cloud_Bigtable_Common_V2_BigtableByteString_System_Nullable_Google_Cloud_Bigtable_V2_BigtableVersion__)(COLUMN_FAMILY, "os_build", "12145.0.0-rc6", timestamp)
                );
                MutateRowsRequest.Types.Entry[] entries = {
                        mutations1,
                        mutations2
                    };
                [MutateRowsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsResponse.html) mutateRowResponse = bigtableClient.[MutateRows](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient.html#Google_Cloud_Bigtable_V2_BigtableClient_MutateRows_Google_Cloud_Bigtable_Common_V2_TableName_Google_Cloud_Bigtable_V2_MutateRowsRequest_Types_Entry___)(tableName, entries);
                foreach (MutateRowsResponse.Types.Entry entry in mutateRowResponse.[Entries](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsResponse.html#Google_Cloud_Bigtable_V2_MutateRowsResponse_Entries))
                {
                    if (entry.Status.Code == 0)
                    {
                        Console.WriteLine($"Row {entry.Index} written successfully");
                    }
                    else
                    {
                        Console.WriteLine($"\tFailed to write row {entry.Index}");
                        Console.WriteLine(entry.Status.Message);
                        return entry.Status.Message;
                    }
                }
                return "Successfully wrote 2 rows";
            }
        }
    }

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"bytes"
    	"context"
    	"encoding/binary"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/bigtable"
    )
    
    func writeBatch(w io.Writer, projectID, instanceID string, tableName string) error {
    	// projectID := "my-project-id"
    	// instanceID := "my-instance-id"
    	// tableName := "mobile-time-series"
    
    	ctx := context.Background()
    	client, err := bigtable.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Client_NewClient)(ctx, projectID, instanceID)
    	if err != nil {
    		return fmt.Errorf("bigtable.NewAdminClient: %w", err)
    	}
    	defer client.Close()
    	tbl := client.[Open](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Client_Open)(tableName)
    	columnFamilyName := "stats_summary"
    	timestamp := bigtable.[Now](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Timestamp_Now)()
    
    	var muts []*bigtable.Mutation
    
    	binary1 := new(bytes.Buffer)
    	binary.Write(binary1, binary.BigEndian, int64(1))
    
    	mut := bigtable.[NewMutation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Mutation_NewMutation)()
    	mut.[Set](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Mutation_Set)(columnFamilyName, "connected_wifi", timestamp, binary1.Bytes())
    	mut.[Set](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Mutation_Set)(columnFamilyName, "os_build", timestamp, []byte("12155.0.0-rc1"))
    	muts = append(muts, mut)
    
    	mut = bigtable.[NewMutation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Mutation_NewMutation)()
    	mut.[Set](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Mutation_Set)(columnFamilyName, "connected_wifi", timestamp, binary1.Bytes())
    	mut.[Set](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Mutation_Set)(columnFamilyName, "os_build", timestamp, []byte("12145.0.0-rc6"))
    	muts = append(muts, mut)
    
    	rowKeys := []string{"tablet#a0b81f74#20190501", "tablet#a0b81f74#20190502"}
    	if _, err := tbl.ApplyBulk(ctx, rowKeys, muts); err != nil {
    		return fmt.Errorf("ApplyBulk: %w", err)
    	}
    
    	fmt.Fprintf(w, "Successfully wrote 2 rows: %s\n", rowKeys)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.api.gax.batching.[Batcher](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.batching.Batcher.html);
    import com.google.api.gax.batching.[BatchingException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.batching.BatchingException.html);
    import com.google.cloud.bigtable.data.v2.[BigtableDataClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html);
    import com.google.cloud.bigtable.data.v2.models.[RowMutationEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.RowMutationEntry.html);
    import com.google.cloud.bigtable.data.v2.models.[TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.TableId.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.util.ArrayList;
    import java.util.List;
    import java.util.concurrent.ExecutionException;
    
    public class WriteBatch {
      private static final String COLUMN_FAMILY_NAME = "stats_summary";
    
      public static void writeBatch(String projectId, String instanceId, String tableId) {
        // String projectId = "my-project-id";
        // String instanceId = "my-instance-id";
        // String tableId = "mobile-time-series";
    
        try ([BigtableDataClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html) dataClient = [BigtableDataClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html).create(projectId, instanceId)) {
          List<ApiFuture<Void>> batchFutures = new ArrayList<>();
          try (Batcher<RowMutationEntry, Void> batcher =
              dataClient.[newBulkMutationBatcher](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html#com_google_cloud_bigtable_data_v2_BigtableDataClient_newBulkMutationBatcher_com_google_cloud_bigtable_data_v2_models_TargetId_)([TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.TableId.html).of(tableId))) {
            long timestamp = System.currentTimeMillis() * 1000;
            batchFutures.add(
                batcher.add(
                    [RowMutationEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.RowMutationEntry.html).create("tablet#a0b81f74#20190501")
                        .setCell(
                            COLUMN_FAMILY_NAME, [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFromUtf8](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFromUtf8_java_lang_String_)("connected_wifi"), timestamp, 1)
                        .setCell(COLUMN_FAMILY_NAME, "os_build", timestamp, "12155.0.0-rc1")));
            batchFutures.add(
                batcher.add(
                    [RowMutationEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.RowMutationEntry.html).create("tablet#a0b81f74#20190502")
                        .setCell(
                            COLUMN_FAMILY_NAME, [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFromUtf8](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFromUtf8_java_lang_String_)("connected_wifi"), timestamp, 1)
                        .setCell(COLUMN_FAMILY_NAME, "os_build", timestamp, "12155.0.0-rc6")));
    
            // Blocks until mutations are applied on all submitted row entries.
            // flush will be called automatically when a batch is full.
            batcher.flush();
            // Before batcher is closed, all remaining (if any) mutations are applied.
          } catch ([BatchingException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.batching.BatchingException.html) batchingException) {
            System.out.println(
                "At least one entry failed to apply. Summary of the errors: \n" + batchingException);
            // get individual entry error details
            for (ApiFuture<Void> future : batchFutures) {
              try {
                future.get();
              } catch (ExecutionException entryException) {
                System.out.println("Entry failure: " + entryException.getCause());
              } catch (InterruptedException e) {
                // handle interrupted exception
              }
            }
          }
          System.out.println("Successfully wrote 2 rows");
        } catch (Exception e) {
          System.out.println("Error during WriteBatch: \n" + e);
        }
      }
    }
    

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Bigtable\BigtableClient;
    use Google\Cloud\Bigtable\Mutations;
    
    /**
     * Write data in batches in a table
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance
     * @param string $tableId The ID of the table where the batch data needs to be written
     */
    function write_batch(
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
        $mutations = [
            (new Mutations())
                ->upsert($columnFamilyId, 'connected_wifi', '1', $timestampMicros)
                ->upsert($columnFamilyId, 'os_build', '12155.0.0-rc1', $timestampMicros),
            (new Mutations())
                ->upsert($columnFamilyId, 'connected_wifi', '1', $timestampMicros)
                ->upsert($columnFamilyId, 'os_build', '12145.0.0-rc6', $timestampMicros)];
    
        $table->mutateRows([
            'tablet#a0b81f74#20190501' => $mutations[0],
            'tablet#a0b81f74#20190502' => $mutations[1]
        ]);
    
        printf('Successfully wrote 2 rows.' . PHP_EOL);
    }

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from datetime import datetime, timezone
    
    from google.cloud import [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest)
    from google.cloud.bigtable.batcher import MutationsBatcher
    
    
    def write_batch(project_id, instance_id, table_id):
        client = [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html)(project=project_id, admin=True)
        instance = [client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.html).[instance](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html#google_cloud_bigtable_client_Client_instance)(instance_id)
        table = instance.table(table_id)
    
        with MutationsBatcher(table=table) as batcher:
            timestamp = datetime.now(timezone.utc)
            column_family_id = "stats_summary"
    
            rows = [
                table.[direct_row](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.table.Table.html#google_cloud_bigtable_table_Table_direct_row)("tablet#a0b81f74#20190501"),
                table.[direct_row](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.table.Table.html#google_cloud_bigtable_table_Table_direct_row)("tablet#a0b81f74#20190502"),
            ]
    
            rows[0].set_cell(column_family_id, "connected_wifi", 1, timestamp)
            rows[0].set_cell(column_family_id, "os_build", "12155.0.0-rc1", timestamp)
            rows[1].set_cell(column_family_id, "connected_wifi", 1, timestamp)
            rows[1].set_cell(column_family_id, "os_build", "12145.0.0-rc6", timestamp)
    
            [batcher](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.batcher.html).mutate_rows(rows)
    
        print("Successfully wrote 2 rows.")
    
    

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # instance_id = "my-instance"
    # table_id    = "my-table"
    table = bigtable.table instance_id, table_id
    column_family = "stats_summary"
    timestamp = (Time.now.to_f * 1_000_000).round(-3)
    
    entries = []
    entries << table.new_mutation_entry("tablet#a0b81f74#20190501")
                    .set_cell(column_family, "connected_cell", 1, timestamp: timestamp)
                    .set_cell(column_family, "os_build", "12155.0.0-rc1", timestamp: timestamp)
    entries << table.new_mutation_entry("tablet#a0b81f74#20190502")
                    .set_cell(column_family, "connected_cell", 1, timestamp: timestamp)
                    .set_cell(column_family, "os_build", "12155.0.0-rc6", timestamp: timestamp)
    
    results = table.mutate_rows entries
    puts "Successfully wrote #{results.length} rows"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
