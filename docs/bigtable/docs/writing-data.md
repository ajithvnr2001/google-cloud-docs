---
url: https://docs.cloud.google.com/bigtable/docs/writing-data/
title: Write examples \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:55.707365+00:00
---

# Write examples  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/writing-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Write examples

This document shows code samples that illustrate the various types of write requests that you can send to Bigtable when you use the Cloud Bigtable client libraries.

Examples on this page use `SetCell` mutations to send _write requests_ to non-aggregate cells. For examples of how to send _add requests_ to aggregate cells, see [Aggregate your data at write time](https://docs.cloud.google.com/bigtable/docs/aggregates).

Before you try these samples, make sure you understand when and when not to use each type of [write request](https://docs.cloud.google.com/bigtable/docs/writes).

**Note:** When you access Bigtable tables with sample code, your queries per second (QPS) is low. As a result, latency for the requests is higher than latency is a standard production environment. For more information, see [Cold starts and low QPS](https://docs.cloud.google.com/bigtable/docs/performance#cold-starts).

The Python client library for Bigtable offers two APIs, `asyncio` and a synchronous API. If your application is asynchronous, use `asyncio`. 

Code samples on this page refer to the sample table at [Data for examples](https://docs.cloud.google.com/bigtable/docs/using-filters#data).

## Perform a simple write

The following code samples demonstrate how to make [simple write requests](https://docs.cloud.google.com/bigtable/docs/writes#simple) to Bigtable. This type of write makes a `MutateRow` API request.

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
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
    	client, err := bigtable.NewClient(ctx, projectID, instanceID)
    	if err != nil {
    		return fmt.Errorf("bigtable.NewClient: %w", err)
    	}
    	defer client.Close()
    	tbl := client.Open(tableName)
    	columnFamilyName := "stats_summary"
    	timestamp := bigtable.Now()
    
    	mut := bigtable.NewMutation()
    	buf := new(bytes.Buffer)
    	binary.Write(buf, binary.BigEndian, int64(1))
    
    	mut.Set(columnFamilyName, "connected_cell", timestamp, buf.Bytes())
    	mut.Set(columnFamilyName, "connected_wifi", timestamp, buf.Bytes())
    	mut.Set(columnFamilyName, "os_build", timestamp, []byte("PQ2A.190405.003"))
    
    	rowKey := "phone#4c410523#20190501"
    	if err := tbl.Apply(ctx, rowKey, mut); err != nil {
    		return fmt.Errorf("Apply: %w", err)
    	}
    
    	fmt.Fprintf(w, "Successfully wrote row: %s\n", rowKey)
    	return nil
    }
    

### HBase

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    import com.google.cloud.bigtable.hbase.BigtableConfiguration;
    import org.apache.hadoop.hbase.TableName;
    import org.apache.hadoop.hbase.client.Connection;
    import org.apache.hadoop.hbase.client.Put;
    import org.apache.hadoop.hbase.client.Table;
    import org.apache.hadoop.hbase.util.Bytes;
    
    public class WriteSimple {
    
      private static final byte[] COLUMN_FAMILY_NAME = Bytes.toBytes("stats_summary");
    
      public static void writeSimple(String projectId, String instanceId, String tableId) {
        // String projectId = "my-project-id";
        // String instanceId = "my-instance-id";
        // String tableId = "mobile-time-series";
    
        try (Connection connection = BigtableConfiguration.connect(projectId, instanceId)) {
          final Table table = connection.getTable(TableName.valueOf(Bytes.toBytes(tableId)));
          long timestamp = System.currentTimeMillis();
          byte[] one = new byte[]{0, 0, 0, 0, 0, 0, 0, 1};
    
          String rowKey = "phone#4c410523#20190501";
          Put put = new Put(Bytes.toBytes(rowKey));
    
          put.addColumn(COLUMN_FAMILY_NAME, Bytes.toBytes("connected_cell"), timestamp, one);
          put.addColumn(COLUMN_FAMILY_NAME, Bytes.toBytes("connected_wifi"), timestamp, one);
          put.addColumn(
              COLUMN_FAMILY_NAME,
              Bytes.toBytes("os_build"),
              timestamp,
              Bytes.toBytes("PQ2A.190405.003"));
          table.put(put);
    
          System.out.printf("Successfully wrote row %s", rowKey);
    
        } catch (Exception e) {
          System.out.println("Error during WriteSimple: \n" + e.toString());
        }
      }
    }
    

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
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
    

### Python asyncio

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    from google.cloud.bigtable.data import BigtableDataClientAsync
    from google.cloud.bigtable.data import [SetCell](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.mutations.SetCell.html)
    
    async def write_simple(project_id, instance_id, table_id):
        async with BigtableDataClientAsync(project=project_id) as client:
            async with client.get_table(instance_id, table_id) as table:
                family_id = "stats_summary"
                row_key = b"phone#4c410523#20190501"
    
                cell_mutation = SetCell(family_id, "connected_cell", 1)
                wifi_mutation = SetCell(family_id, "connected_wifi", 1)
                os_mutation = SetCell(family_id, "os_build", "PQ2A.190405.003")
    
                await table.mutate_row(row_key, cell_mutation)
                await table.mutate_row(row_key, wifi_mutation)
                await table.mutate_row(row_key, os_mutation)
    

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    from datetime import datetime, timezone
    
    from google.cloud import bigtable
    
    
    def write_simple(project_id, instance_id, table_id):
        client = bigtable.Client(project=project_id, admin=True)
        instance = client.instance(instance_id)
        table = instance.table(table_id)
    
        timestamp = datetime.now(timezone.utc)
        column_family_id = "stats_summary"
    
        row_key = "phone#4c410523#20190501"
    
        row = table.direct_row(row_key)
        row.set_cell(column_family_id, "connected_cell", 1, timestamp)
        row.set_cell(column_family_id, "connected_wifi", 1, timestamp)
        row.set_cell(column_family_id, "os_build", "PQ2A.190405.003", timestamp)
    
        row.commit()
    
        print("Successfully wrote row {}.".format(row_key))
    
    

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    using System;
    using Google.Cloud.Bigtable.V2;
    using Google.Cloud.Bigtable.Common.V2;
    
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
                BigtableClient bigtableClient = BigtableClient.Create();
    
                TableName tableName = new TableName(projectId, instanceId, tableId);
                BigtableByteString rowkey = new BigtableByteString("phone#4c410523#20190501");
                BigtableVersion timestamp = new BigtableVersion(DateTime.UtcNow);
                string COLUMN_FAMILY = "stats_summary";
    
                Mutation[] mutations = {
                        Mutations.SetCell(COLUMN_FAMILY, "connected_cell", 1, timestamp),
                        Mutations.SetCell(COLUMN_FAMILY, "connected_wifi", 1, timestamp),
                        Mutations.SetCell(COLUMN_FAMILY, "os_build", "PQ2A.190405.003", timestamp)
                    };
                MutateRowResponse mutateRowResponse = bigtableClient.MutateRow(tableName, rowkey, mutations);
                Console.WriteLine(mutateRowResponse);
                return $"Successfully wrote row {rowkey}";
            }
        }
    }

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
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

### Node.js

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    const {Bigtable} = require('@google-cloud/bigtable');
    const bigtable = new Bigtable();
    
    async function writeSimple() {
      /**
       * TODO(developer): Uncomment these variables before running the sample.
       */
      // const instanceId = 'YOUR_INSTANCE_ID';
      // const tableId = 'YOUR_TABLE_ID';
      const instance = bigtable.instance(instanceId);
      const table = instance.table(tableId);
    
      const timestamp = new Date();
      const rowToInsert = {
        key: 'phone#4c410523#20190501',
        data: {
          stats_summary: {
            connected_cell: {
              value: 1,
              timestamp,
            },
            connected_wifi: {
              value: 1,
              timestamp,
            },
            os_build: {
              value: 'PQ2A.190405.003',
              timestamp,
            },
          },
        },
      };
    
      await table.insert(rowToInsert);
    
      console.log(`Successfully wrote row ${rowToInsert.key}`);
    }
    
    writeSimple();

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
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

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
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

## Increment a value

The following code samples demonstrate how to send a [write request that increments or decrements](https://docs.cloud.google.com/bigtable/docs/writes#increments) an existing numeric value in an aggregate cell. This type of write makes `MutateRow` request with an `AddToCell` mutation type. The examples add to a sum in a column family that expects input type `Int64`.

### cbt
    
    
    cbt addtocell TABLE_ID ROW_KEY
    FAMILY_NAME:COLUMN_QUALIFER=VALUE@TIMESTAMP
    

Replace the following:

  * `TABLE_ID`: the permanent identifier for the table
  * `ROW_KEY`: the row key
  * `FAMILY_NAME`: the name of the aggregate column family
  * `COLUMN_QUALIFIER`: an identifier for the column
  * `VALUE`: the value to add to the cell
  * `TIMESTAMP`: a Unix timestamp in microseconds, such as `1710868850000000`



This example decrements by 100 the value stored in the `week12` column in the `device-1` row:
    
    
    cbt addtocell mobile-data device-1 updates:week12=-100@1710868850000000
    

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/bigtable"
    )
    
    func writeAggregate(w io.Writer, projectID, instanceID string, tableName string) error {
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
    	columnFamilyName := "view_count"
    	viewTimestamp, err := time.Parse(time.RFC3339, "2024-03-13T12:41:34Z")
    	if err != nil {
    		return err
    	}
    	hourlyBucket := viewTimestamp.Truncate(time.Hour)
    
    	mut := bigtable.[NewMutation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Mutation_NewMutation)()
    	mut.[AddIntToCell](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Mutation_AddIntToCell)(columnFamilyName, "views", bigtable.[Time](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Timestamp_Time)(hourlyBucket), 1)
    
    	rowKey := "page#index.html"
    	if err := tbl.Apply(ctx, rowKey, mut); err != nil {
    		return fmt.Errorf("Apply: %w", err)
    	}
    
    	fmt.Fprintf(w, "Successfully wrote row: %s\n", rowKey)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    import com.google.cloud.bigtable.data.v2.[BigtableDataClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html);
    import com.google.cloud.bigtable.data.v2.models.[RowMutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.RowMutation.html);
    import com.google.common.primitives.Longs;
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.time.Instant;
    import java.time.temporal.ChronoUnit;
    
    public class WriteAggregate {
      private static final String COUNT_COLUMN_FAMILY_NAME = "view_count";
      private static final long MICROS_PER_MILLI = 1000;
    
      public static void writeAggregate(String projectId, String instanceId, String tableId) {
        // String projectId = "my-project-id";
        // String instanceId = "my-instance-id";
        // String tableId = "page-view-counter";
    
        try ([BigtableDataClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html) dataClient = [BigtableDataClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html).create(projectId, instanceId)) {
    
          String rowKey = "page#index.html";
          Instant viewTimestamp = Instant.parse("2024-03-13T12:41:34.123Z");
    
          // Bucket the views for an hour into a single count, giving us an hourly view count for a
          // given page.
          Instant hourlyBucket = viewTimestamp.truncatedTo(ChronoUnit.HOURS);
          long hourlyBucketMicros = hourlyBucket.toEpochMilli() * MICROS_PER_MILLI;
    
          [RowMutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.RowMutation.html) rowMutation =
              [RowMutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.RowMutation.html).create(tableId, rowKey)
                  .addToCell(COUNT_COLUMN_FAMILY_NAME, "views", hourlyBucketMicros, 1);
    
          dataClient.[mutateRow](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html#com_google_cloud_bigtable_data_v2_BigtableDataClient_mutateRow_com_google_cloud_bigtable_data_v2_models_RowMutation_)(rowMutation);
          System.out.printf("Successfully wrote row %s", rowKey);
    
        } catch (Exception e) {
          System.out.println("Error during WriteAggregate: \n" + e.toString());
        }
      }
    
      public static void mergeAggregate(String projectId, String instanceId, String tableId) {
        // String projectId = "my-project-id";
        // String instanceId = "my-instance-id";
        // String tableId = "page-view-counter";
    
        try ([BigtableDataClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html) dataClient = [BigtableDataClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html).create(projectId, instanceId)) {
    
          String rowKey = "page#index.html";
          Instant viewTimestamp = Instant.parse("2024-03-13T12:41:34.123Z");
    
          // Bucket the views for an hour into a single count, giving us an hourly view count for a
          // given page.
          Instant hourlyBucket = viewTimestamp.truncatedTo(ChronoUnit.HOURS);
          long hourlyBucketMicros = hourlyBucket.toEpochMilli() * MICROS_PER_MILLI;
    
          [RowMutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.RowMutation.html) rowMutation =
              [RowMutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.RowMutation.html).create(tableId, rowKey)
                  .mergeToCell(
                      COUNT_COLUMN_FAMILY_NAME,
                      "views",
                      hourlyBucketMicros,
                      [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(Longs.toByteArray(1L)));
    
          dataClient.[mutateRow](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html#com_google_cloud_bigtable_data_v2_BigtableDataClient_mutateRow_com_google_cloud_bigtable_data_v2_models_RowMutation_)(rowMutation);
          System.out.printf("Successfully wrote row %s", rowKey);
    
        } catch (Exception e) {
          System.out.println("Error during mergeAggregate: \n" + e.toString());
        }
      }
    }
    

### Python asyncio

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    import time
    from google.cloud.bigtable.data import BigtableDataClientAsync
    from google.cloud.bigtable.data.mutations import [AddToCell](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.mutations.AddToCell.html), [RowMutationEntry](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.mutations.RowMutationEntry.html)
    from google.cloud.bigtable.data.exceptions import [MutationsExceptionGroup](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.exceptions.MutationsExceptionGroup.html)
    
    async def write_aggregate(project_id, instance_id, table_id):
        """Increments a value in a Bigtable table using AddToCell mutation."""
        async with BigtableDataClientAsync(project=project_id) as client:
            table = client.get_table(instance_id, table_id)
            row_key = "unique_device_ids_1"
            try:
                async with table.mutations_batcher() as batcher:
                    # The AddToCell mutation increments the value of a cell.
                    # The `counters` family must be set up to be an aggregate
                    # family with an int64 input type.
                    reading = AddToCell(
                        family="counters",
                        qualifier="odometer",
                        value=32304,
                        # Convert nanoseconds to microseconds
                        timestamp_micros=time.time_ns() // 1000,
                    )
                    await batcher.append(
                        RowMutationEntry(row_key.encode("utf-8"), [reading])
                    )
            except MutationsExceptionGroup as e:
                # MutationsExceptionGroup contains a FailedMutationEntryError for
                # each mutation that failed.
                for sub_exception in e.[exceptions](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.exceptions.html):
                    failed_entry: RowMutationEntry = sub_exception.entry
                    cause: Exception = sub_exception.__cause__
                    print(
                        f"Failed mutation for row {failed_entry.row_key!r} with error: {cause!r}"
                    )
    

## Conditionally write a value

The following code samples demonstrate how to send a [conditional write request](https://docs.cloud.google.com/bigtable/docs/writes#conditional), which checks a row for a condition and then, depending on the result, writes data to that row. This type of write makes a `CheckAndMutateRow` API request.

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/bigtable"
    )
    
    func writeConditionally(w io.Writer, projectID, instanceID string, tableName string) error {
    	// projectID := "my-project-id"
    	// instanceID := "my-instance-id"
    	// tableName := "mobile-time-series"
    
    	ctx := context.Background()
    	client, err := bigtable.NewClient(ctx, projectID, instanceID)
    	if err != nil {
    		return fmt.Errorf("bigtable.NewAdminClient: %w", err)
    	}
    	defer client.Close()
    	tbl := client.Open(tableName)
    	columnFamilyName := "stats_summary"
    	timestamp := bigtable.Now()
    
    	mut := bigtable.NewMutation()
    	mut.Set(columnFamilyName, "os_name", timestamp, []byte("android"))
    
    	filter := bigtable.ChainFilters(
    		bigtable.FamilyFilter(columnFamilyName),
    		bigtable.ColumnFilter("os_build"),
    		bigtable.ValueFilter("PQ2A\\..*"))
    	conditionalMutation := bigtable.NewCondMutation(filter, mut, nil)
    
    	rowKey := "phone#4c410523#20190501"
    	if err := tbl.Apply(ctx, rowKey, conditionalMutation); err != nil {
    		return fmt.Errorf("Apply: %w", err)
    	}
    
    	fmt.Fprintln(w, "Successfully updated row's os_name")
    	return nil
    }
    

### HBase

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    import com.google.cloud.bigtable.hbase.BigtableConfiguration;
    import org.apache.hadoop.hbase.TableName;
    import org.apache.hadoop.hbase.client.Connection;
    import org.apache.hadoop.hbase.client.Put;
    import org.apache.hadoop.hbase.client.RowMutations;
    import org.apache.hadoop.hbase.client.Table;
    import org.apache.hadoop.hbase.filter.CompareFilter.CompareOp;
    import org.apache.hadoop.hbase.util.Bytes;
    
    public class WriteConditionally {
    
      private static final byte[] COLUMN_FAMILY_NAME = Bytes.toBytes("stats_summary");
    
      public static void writeConditionally(String projectId, String instanceId, String tableId) {
        // String projectId = "my-project-id";
        // String instanceId = "my-instance-id";
        // String tableId = "mobile-time-series";
    
        try (Connection connection = BigtableConfiguration.connect(projectId, instanceId)) {
          Table table = connection.getTable(TableName.valueOf(Bytes.toBytes(tableId)));
          long timestamp = System.currentTimeMillis();
    
          String rowKey = "phone#4c410523#20190501";
          RowMutations mutations = new RowMutations(Bytes.toBytes(rowKey));
    
          Put put = new Put(Bytes.toBytes(rowKey));
          put.addColumn(
              COLUMN_FAMILY_NAME, Bytes.toBytes("os_name"), timestamp, Bytes.toBytes("android"));
          mutations.add(put);
    
          table.checkAndMutate(
              Bytes.toBytes(rowKey),
              COLUMN_FAMILY_NAME,
              Bytes.toBytes("os_build"),
              CompareOp.GREATER_OR_EQUAL,
              Bytes.toBytes("PQ2A.190405"),
              mutations);
    
          System.out.print("Successfully updated row's os_name");
    
        } catch (Exception e) {
          System.out.println("Error during WriteConditionally: \n" + e.toString());
          e.printStackTrace();
        }
      }
    }
    

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    import static com.google.cloud.bigtable.data.v2.models.[Filters](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Filters.html).FILTERS;
    
    import com.google.cloud.bigtable.data.v2.[BigtableDataClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html);
    import com.google.cloud.bigtable.data.v2.models.[ConditionalRowMutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.ConditionalRowMutation.html);
    import com.google.cloud.bigtable.data.v2.models.[Filters](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Filters.html).Filter;
    import com.google.cloud.bigtable.data.v2.models.[Mutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Mutation.html);
    import com.google.cloud.bigtable.data.v2.models.[TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.TableId.html);
    
    public class WriteConditionally {
      private static final String COLUMN_FAMILY_NAME = "stats_summary";
    
      public static void writeConditionally(String projectId, String instanceId, String tableId) {
        // String projectId = "my-project-id";
        // String instanceId = "my-instance-id";
        // String tableId = "mobile-time-series";
    
        try ([BigtableDataClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html) dataClient = [BigtableDataClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html).create(projectId, instanceId)) {
          long timestamp = System.currentTimeMillis() * 1000;
    
          String rowkey = "phone#4c410523#20190501";
    
          [Mutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Mutation.html) mutation =
              [Mutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Mutation.html).create().setCell(COLUMN_FAMILY_NAME, "os_name", timestamp, "android");
    
          Filter filter =
              FILTERS
                  .chain()
                  .filter(FILTERS.family().exactMatch(COLUMN_FAMILY_NAME))
                  .filter(FILTERS.qualifier().exactMatch("os_build"))
                  .filter(FILTERS.value().regex("PQ2A\\..*"));
    
          [ConditionalRowMutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.ConditionalRowMutation.html) conditionalRowMutation =
              [ConditionalRowMutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.ConditionalRowMutation.html).create([TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.TableId.html).of(tableId), rowkey)
                  .condition(filter)
                  .then(mutation);
    
          boolean success = dataClient.[checkAndMutateRow](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html#com_google_cloud_bigtable_data_v2_BigtableDataClient_checkAndMutateRow_com_google_cloud_bigtable_data_v2_models_ConditionalRowMutation_)(conditionalRowMutation);
    
          System.out.printf("Successfully updated row's os_name: %b", success);
    
        } catch (Exception e) {
          System.out.println("Error during WriteConditionally: \n" + e.toString());
          e.printStackTrace();
        }
      }
    }
    

### Python asyncio

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    from google.cloud.bigtable.data import BigtableDataClientAsync
    from google.cloud.bigtable.data import [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html)
    from google.cloud.bigtable.data import [SetCell](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.mutations.SetCell.html)
    
    async def write_conditional(project_id, instance_id, table_id):
        async with BigtableDataClientAsync(project=project_id) as client:
            async with client.get_table(instance_id, table_id) as table:
                family_id = "stats_summary"
                row_key = "phone#4c410523#20190501"
    
                row_filter = [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[RowFilterChain](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.RowFilterChain.html)(
                    filters=[
                        [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[FamilyNameRegexFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.FamilyNameRegexFilter.html)(family_id),
                        [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[ColumnQualifierRegexFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.ColumnQualifierRegexFilter.html)("os_build"),
                        [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[ValueRegexFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.ValueRegexFilter.html)("PQ2A\\..*"),
                    ]
                )
    
                if_true = SetCell(family_id, "os_name", "android")
                result = await table.check_and_mutate_row(
                    row_key,
                    row_filter,
                    true_case_mutations=if_true,
                    false_case_mutations=None,
                )
                if result is True:
                    print("The row os_name was set to android")
    

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    from datetime import datetime, timezone
    
    from google.cloud import bigtable
    from google.cloud.bigtable import row_filters
    
    
    def write_conditional(project_id, instance_id, table_id):
        client = bigtable.Client(project=project_id, admin=True)
        instance = client.instance(instance_id)
        table = instance.table(table_id)
    
        timestamp = datetime.now(timezone.utc)
        column_family_id = "stats_summary"
    
        row_key = "phone#4c410523#20190501"
    
        row_filter = row_filters.RowFilterChain(
            filters=[
                row_filters.FamilyNameRegexFilter(column_family_id),
                row_filters.ColumnQualifierRegexFilter("os_build"),
                row_filters.ValueRegexFilter("PQ2A\\..*"),
            ]
        )
        row = table.conditional_row(row_key, filter_=row_filter)
        row.set_cell(column_family_id, "os_name", "android", timestamp)
        row.commit()
    
        print("Successfully updated row's os_name.")
    
    

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    using System;
    using Google.Cloud.Bigtable.V2;
    using Google.Cloud.Bigtable.Common.V2;
    
    namespace Writes
    {
        public class WriteConditionalSample
        {
            /// <summary>
            /// Check if a row has a certain value then mutate the row if it does.
            ///</summary>
            /// <param name="projectId">Your Google Cloud Project ID.</param>
            /// <param name="instanceId">Your Google Cloud Bigtable Instance ID.</param>
            /// <param name="tableId">Your Google Cloud Bigtable table ID.</param>
            public string WriteConditional(
                string projectId = "YOUR-PROJECT-ID",
                string instanceId = "YOUR-INSTANCE-ID",
                string tableId = "YOUR-TABLE-ID")
            {
                BigtableClient bigtableClient = BigtableClient.Create();
    
                TableName tableName = new TableName(projectId, instanceId, tableId);
                BigtableByteString rowkey = new BigtableByteString("phone#4c410523#20190501");
                BigtableVersion timestamp = new BigtableVersion(DateTime.UtcNow);
                string COLUMN_FAMILY = "stats_summary";
    
                CheckAndMutateRowResponse checkAndMutateRowResponse = bigtableClient.CheckAndMutateRow(
                    tableName,
                    rowkey,
                    RowFilters.Chain(
                        RowFilters.FamilyNameExact(COLUMN_FAMILY),
                        RowFilters.ColumnQualifierExact("os_build"),
                        RowFilters.ValueRegex("PQ2A\\..*")),
                    Mutations.SetCell(COLUMN_FAMILY, "os_name", "android", timestamp));
    
                return $"Successfully updated row's os_name: {checkAndMutateRowResponse.PredicateMatched}";
            }
        }
    }

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    namespace cbt = ::google::cloud::bigtable;
    [](cbt::Table table) {
      auto timestamp = std::chrono::duration_cast<std::chrono::milliseconds>(
          std::chrono::system_clock::now().time_since_epoch());
    
      std::string row_key = "phone#4c410523#20190501";
      cbt::SingleRowMutation mutation(row_key);
      std::string column_family = "stats_summary";
      cbt::Filter predicate = cbt::Filter::Chain(
          cbt::Filter::ColumnName(column_family, "os_build"),
          cbt::Filter::Latest(1), cbt::Filter::ValueRegex("PQ2A\\..*"));
    
      google::cloud::StatusOr<cbt::MutationBranch> branch =
          table.CheckAndMutateRow(
              row_key, std::move(predicate),
              {cbt::SetCell(column_family, "os_name", timestamp, "android")}, {});
    
      if (!branch) throw std::move(branch).status();
      if (*branch == cbt::MutationBranch::kPredicateMatched) {
        std::cout << "Successfully updated row\n";
      } else {
        std::cout << "The predicate was not matched\n";
      }
    }

### Node.js

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const instanceId = 'YOUR_INSTANCE_ID';
    // const tableId = 'YOUR_TABLE_ID';
    
    const {Bigtable} = require('@google-cloud/bigtable');
    
    const bigtable = new Bigtable();
    
    async function writeConditionally() {
      const instance = bigtable.instance(instanceId);
      const table = instance.table(tableId);
    
      const timestamp = new Date();
      const row = table.row('phone#4c410523#20190501');
      const filter = [
        {
          column: 'os_build',
          value: {
            start: 'PQ2A',
            end: 'PQ2A',
          },
        },
      ];
    
      const config = {
        onMatch: [
          {
            method: 'insert',
            data: {
              stats_summary: {
                os_name: 'android',
                timestamp,
              },
            },
          },
        ],
      };
    
      await row.filter(filter, config);
    
      console.log("Successfully updated row's os_name");
    }
    
    writeConditionally();

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Bigtable\BigtableClient;
    use Google\Cloud\Bigtable\Filter;
    use Google\Cloud\Bigtable\Mutations;
    
    /**
     * Write data conditionally in a table
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance
     * @param string $tableId The ID of the table where the data needs to be written
     */
    function write_conditionally(
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
    
        $mutations = (new Mutations())->upsert($columnFamilyId, 'os_name', 'android', $timestampMicros);
        $predicateFilter = Filter::chain()
        ->addFilter(Filter::family()->exactMatch($columnFamilyId))
        ->addFilter(Filter::qualifier()->exactMatch('os_build'))
        ->addFilter(Filter::value()->regex('PQ2A.*'));
        $options = ['predicateFilter' => $predicateFilter, 'trueMutations' => $mutations];
    
        $table->checkAndMutateRow('phone#4c410523#20190501', $options);
    
        printf('Successfully updated row\'s os_name' . PHP_EOL);
    }

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    # instance_id = "my-instance"
    # table_id    = "my-table"
    table = bigtable.table instance_id, table_id
    column_family = "stats_summary"
    timestamp = (Time.now.to_f * 1_000_000).round(-3)
    
    rowkey = "phone#4c410523#20190501"
    predicate_filter = Google::Cloud::Bigtable::RowFilter.chain
                                                         .family(column_family)
                                                         .qualifier("os_build")
                                                         .value("PQ2A\\..*")
    
    on_match_mutations = Google::Cloud::Bigtable::MutationEntry.new
    on_match_mutations.set_cell(
      column_family,
      "os_name",
      "android",
      timestamp: timestamp
    )
    
    response = table.check_and_mutate_row(
      rowkey,
      predicate_filter,
      on_match: on_match_mutations
    )
    
    puts "Successfully updated row's os_name: #{response}"

## Perform batch writes

The following code samples demonstrate how to make [batch write requests](https://docs.cloud.google.com/bigtable/docs/writes#batch) to Bigtable. This type of write makes a `MutateRows` API request.

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
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
    	client, err := bigtable.NewClient(ctx, projectID, instanceID)
    	if err != nil {
    		return fmt.Errorf("bigtable.NewAdminClient: %w", err)
    	}
    	defer client.Close()
    	tbl := client.Open(tableName)
    	columnFamilyName := "stats_summary"
    	timestamp := bigtable.Now()
    
    	var muts []*bigtable.Mutation
    
    	binary1 := new(bytes.Buffer)
    	binary.Write(binary1, binary.BigEndian, int64(1))
    
    	mut := bigtable.NewMutation()
    	mut.Set(columnFamilyName, "connected_wifi", timestamp, binary1.Bytes())
    	mut.Set(columnFamilyName, "os_build", timestamp, []byte("12155.0.0-rc1"))
    	muts = append(muts, mut)
    
    	mut = bigtable.NewMutation()
    	mut.Set(columnFamilyName, "connected_wifi", timestamp, binary1.Bytes())
    	mut.Set(columnFamilyName, "os_build", timestamp, []byte("12145.0.0-rc6"))
    	muts = append(muts, mut)
    
    	rowKeys := []string{"tablet#a0b81f74#20190501", "tablet#a0b81f74#20190502"}
    	if _, err := tbl.ApplyBulk(ctx, rowKeys, muts); err != nil {
    		return fmt.Errorf("ApplyBulk: %w", err)
    	}
    
    	fmt.Fprintf(w, "Successfully wrote 2 rows: %s\n", rowKeys)
    	return nil
    }
    

### HBase

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    import com.google.cloud.bigtable.hbase.BigtableConfiguration;
    import java.util.ArrayList;
    import java.util.List;
    import org.apache.hadoop.hbase.TableName;
    import org.apache.hadoop.hbase.client.Connection;
    import org.apache.hadoop.hbase.client.Put;
    import org.apache.hadoop.hbase.client.Table;
    import org.apache.hadoop.hbase.util.Bytes;
    
    public class WriteBatch {
    
      private static final byte[] COLUMN_FAMILY_NAME = Bytes.toBytes("stats_summary");
    
      public static void writeBatch(String projectId, String instanceId, String tableId) {
        // String projectId = "my-project-id";
        // String instanceId = "my-instance-id";
        // String tableId = "mobile-time-series";
    
        try (Connection connection = BigtableConfiguration.connect(projectId, instanceId)) {
          final Table table = connection.getTable(TableName.valueOf(Bytes.toBytes(tableId)));
          long timestamp = System.currentTimeMillis();
          byte[] one = new byte[]{0, 0, 0, 0, 0, 0, 0, 1};
    
          List<Put> puts = new ArrayList<Put>();
          puts.add(new Put(Bytes.toBytes("tablet#a0b81f74#20190501")));
          puts.add(new Put(Bytes.toBytes("tablet#a0b81f74#20190502")));
    
          puts.get(0).addColumn(COLUMN_FAMILY_NAME, Bytes.toBytes("connected_wifi"), timestamp, one);
          puts.get(0)
              .addColumn(
                  COLUMN_FAMILY_NAME,
                  Bytes.toBytes("os_build"),
                  timestamp,
                  Bytes.toBytes("12155.0.0-rc1"));
    
          puts.get(1).addColumn(COLUMN_FAMILY_NAME, Bytes.toBytes("connected_wifi"), timestamp, one);
          puts.get(1)
              .addColumn(
                  COLUMN_FAMILY_NAME,
                  Bytes.toBytes("os_build"),
                  timestamp,
                  Bytes.toBytes("12145.0.0-rc6"));
    
          table.put(puts);
    
          System.out.print("Successfully wrote 2 rows");
        } catch (Exception e) {
          System.out.println("Error during WriteBatch: \n" + e.toString());
        }
      }
    }
    

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
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
    

### Python asyncio

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    from google.cloud.bigtable.data import BigtableDataClientAsync
    from google.cloud.bigtable.data.mutations import [SetCell](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.mutations.SetCell.html)
    from google.cloud.bigtable.data.mutations import [RowMutationEntry](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.mutations.RowMutationEntry.html)
    from google.cloud.bigtable.data.exceptions import [MutationsExceptionGroup](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.exceptions.MutationsExceptionGroup.html)
    
    async def write_batch(project_id, instance_id, table_id):
        async with BigtableDataClientAsync(project=project_id) as client:
            async with client.get_table(instance_id, table_id) as table:
                family_id = "stats_summary"
                try:
                    async with table.mutations_batcher() as batcher:
                        mutation_list = [
                            SetCell(family_id, "connected_cell", 1),
                            SetCell(family_id, "connected_wifi", 1),
                            SetCell(family_id, "os_build", "12155.0.0-rc1"),
                        ]
                        # awaiting the batcher.append method adds the RowMutationEntry
                        # to the batcher's queue to be written in the next flush.
                        await batcher.append(
                            RowMutationEntry("tablet#a0b81f74#20190501", mutation_list)
                        )
                        await batcher.append(
                            RowMutationEntry("tablet#a0b81f74#20190502", mutation_list)
                        )
                except MutationsExceptionGroup as e:
                    # MutationsExceptionGroup contains a FailedMutationEntryError for
                    # each mutation that failed.
                    for sub_exception in e.[exceptions](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.exceptions.html):
                        failed_entry: RowMutationEntry = sub_exception.entry
                        cause: Exception = sub_exception.__cause__
                        print(
                            f"Failed mutation: {failed_entry.row_key} with error: {cause!r}"
                        )
    

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    from datetime import datetime, timezone
    
    from google.cloud import bigtable
    from google.cloud.bigtable.batcher import MutationsBatcher
    
    
    def write_batch(project_id, instance_id, table_id):
        client = bigtable.Client(project=project_id, admin=True)
        instance = client.instance(instance_id)
        table = instance.table(table_id)
    
        with MutationsBatcher(table=table) as batcher:
            timestamp = datetime.now(timezone.utc)
            column_family_id = "stats_summary"
    
            rows = [
                table.direct_row("tablet#a0b81f74#20190501"),
                table.direct_row("tablet#a0b81f74#20190502"),
            ]
    
            rows[0].set_cell(column_family_id, "connected_wifi", 1, timestamp)
            rows[0].set_cell(column_family_id, "os_build", "12155.0.0-rc1", timestamp)
            rows[1].set_cell(column_family_id, "connected_wifi", 1, timestamp)
            rows[1].set_cell(column_family_id, "os_build", "12145.0.0-rc6", timestamp)
    
            batcher.mutate_rows(rows)
    
        print("Successfully wrote 2 rows.")
    
    

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    using System;
    using Google.Cloud.Bigtable.V2;
    using Google.Cloud.Bigtable.Common.V2;
    
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
                BigtableClient bigtableClient = BigtableClient.Create();
    
                TableName tableName = new TableName(projectId, instanceId, tableId);
                BigtableVersion timestamp = new BigtableVersion(DateTime.UtcNow);
                string COLUMN_FAMILY = "stats_summary";
    
                MutateRowsRequest.Types.Entry mutations1 = Mutations.CreateEntry(new BigtableByteString("tablet#a0b81f74#20190501"),
                    Mutations.SetCell(COLUMN_FAMILY, "connected_cell", 1, timestamp),
                    Mutations.SetCell(COLUMN_FAMILY, "os_build", "12155.0.0-rc1", timestamp)
                );
                MutateRowsRequest.Types.Entry mutations2 = Mutations.CreateEntry(new BigtableByteString("tablet#a0b81f74#20190502"),
                    Mutations.SetCell(COLUMN_FAMILY, "connected_cell", 1, timestamp),
                    Mutations.SetCell(COLUMN_FAMILY, "os_build", "12145.0.0-rc6", timestamp)
                );
                MutateRowsRequest.Types.Entry[] entries = {
                        mutations1,
                        mutations2
                    };
                MutateRowsResponse mutateRowResponse = bigtableClient.MutateRows(tableName, entries);
                foreach (MutateRowsResponse.Types.Entry entry in mutateRowResponse.Entries)
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

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
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

### Node.js

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const instanceId = 'YOUR_INSTANCE_ID';
    // const tableId = 'YOUR_TABLE_ID';
    
    const {Bigtable} = require('@google-cloud/bigtable');
    
    const bigtable = new Bigtable();
    
    async function writeBatch() {
      const instance = bigtable.instance(instanceId);
      const table = instance.table(tableId);
    
      const timestamp = new Date();
      const rowsToInsert = [
        {
          key: 'tablet#a0b81f74#20190501',
          data: {
            stats_summary: {
              connected_wifi: {
                value: 1,
                timestamp,
              },
              os_build: {
                value: '12155.0.0-rc1',
                timestamp,
              },
            },
          },
        },
        {
          key: 'tablet#a0b81f74#20190502',
          data: {
            stats_summary: {
              connected_wifi: {
                value: 1,
                timestamp,
              },
              os_build: {
                value: '12145.0.0-rc6',
                timestamp,
              },
            },
          },
        },
      ];
    
      await table.insert(rowsToInsert);
    
      console.log(
        `Successfully wrote 2 rows: ${rowsToInsert[0].key} and ${rowsToInsert[1].key}`,
      );
    }
    
    writeBatch();

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
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

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
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

## Enable batch write flow control

The following code snippets demonstrate how to enable [batch write flow control](https://docs.cloud.google.com/bigtable/docs/writes#flow-control) when you send batch writes to Bigtable. This feature is available in the [ Bigtable Beam connector (`BigtableIO`)](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/gcp/bigtable/BigtableIO.html) and the [Bigtable HBase Beam connector (`CloudBigtableIO`)](https://docs.cloud.google.com/bigtable/docs/hbase-dataflow-java). To view the entire sample, including import statements, click more_vert and then click **View on GitHub**.

### BigtableIO

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    mutations.apply(
        String.format("Write data to table %s via BigtableIO", options.getBigtableTableId()),
        BigtableIO.write()
            .withProjectId(options.getProject())
            .withInstanceId(options.getBigtableInstanceId())
            .withTableId(options.getBigtableTableId())
            .withFlowControl(true) // This enables batch write flow control
    );

### CloudBigtableIO

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    mutations.apply(
        String.format("Write data to table %s via CloudBigtableIO", options.getBigtableTableId()),
        CloudBigtableIO.writeToTable(
            new CloudBigtableTableConfiguration.Builder()
                .withProjectId(options.getProject())
                .withInstanceId(options.getBigtableInstanceId())
                .withTableId(options.getBigtableTableId())
                .withConfiguration(
                    BigtableOptionsFactory.BIGTABLE_ENABLE_BULK_MUTATION_FLOW_CONTROL, "true")
                .build()));

## Write to an authorized view

The following example shows how to send a write request to an authorized view. The syntax is similar to writing to a table except you must also provide the authorized view ID.

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    try {
      System.out.println("\nWriting to authorized view");
      String[] names = {"World", "Bigtable", "Java"};
      for (int i = 0; i < names.length; i++) {
        String greeting = "Hello " + names[i] + "!";
        RowMutation rowMutation =
            RowMutation.create(AuthorizedViewId.of(tableId, authorizedViewId), ROW_KEY_PREFIX + i)
                .setCell(COLUMN_FAMILY, COLUMN_QUALIFIER_NAME, names[i])
                .setCell(COLUMN_FAMILY, COLUMN_QUALIFIER_GREETING, greeting);
        dataClient.mutateRow(rowMutation);
        System.out.println(greeting);
      }
    } catch (Exception e) {
      if (e instanceof NotFoundException) {
        System.err.println("Failed to write to non-existent authorized view: " + e.getMessage());
      } else if (e instanceof PermissionDeniedException) {
        System.err.println(
            "Failed to apply mutations outside of the authorized view: " + e.getMessage());
      }
    }

## What's next

  * [Learn how to set garbage collection policies.](https://docs.cloud.google.com/bigtable/docs/configuring-garbage-collection)
  * [Explore more Bigtable code samples.](https://docs.cloud.google.com/bigtable/docs/samples)
  * [Use the Bigtable emulator.](https://docs.cloud.google.com/bigtable/docs/emulator)
  * [Implement counters by using aggregate cells.](https://docs.cloud.google.com/bigtable/docs/aggregates)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
