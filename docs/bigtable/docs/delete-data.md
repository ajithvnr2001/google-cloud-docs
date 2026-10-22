---
url: https://docs.cloud.google.com/bigtable/docs/delete-data/
title: Deletes \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:40.351324+00:00
---

# Deletes  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/delete-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Deletes

This document describes how to delete data stored in Bigtable tables, discusses when you should use each approach, and provides examples. Before you read this page, you should be familiar with the [Bigtable overview](https://docs.cloud.google.com/bigtable/docs/overview) and understand the concepts involved in [schema design](https://docs.cloud.google.com/bigtable/docs/schema-design).

For consistency, descriptions on this page refer to the API methods that are used for each type of request. However, we strongly recommend that you always use one of the [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries) to access the Bigtable APIs instead of using REST or RPC.

Examples on this page use [sample data](https://docs.cloud.google.com/bigtable/docs/using-filters#data) similar to the data that you might store in Bigtable.

To learn the number of times that you can use the operations described on this page per day, see [Quotas and limits](https://docs.cloud.google.com/bigtable/quotas).

## How Bigtable deletes data

When you send a delete request, cells are marked for deletion and cannot be read. The data is removed up to a week later during [compaction](https://docs.cloud.google.com/bigtable/docs/overview#compactions), a background process that continuously optimizes the table. Deletion metadata can cause your data to take up slightly more space (several kb per row) for a few days after you send a delete request, until the next compaction occurs.

You can always send a delete request, even if your cluster has exceeded the storage limit and reads and writes are blocked.

## Delete a range of rows

If you want to delete a large amount of data stored in contiguous rows, use `dropRowRange`. This operation deletes all rows for a range of rows identified by a starting and ending row or a row key prefix.

The row key values that you provide when you delete a range of rows are treated as service data. For information about how service data is handled, see the [Google Cloud Privacy Notice](https://cloud.google.com/terms/cloud-privacy-notice).

After a successful deletion is complete and you receive a response, you can safely write data to the same row range.

The `dropRowRange` operation has the following restrictions:

  * You can't drop a range of rows from an authorized view.
  * You can't call the `dropRowRange` method asynchronously. If you send a `dropRowRange` request to a table while another request is in progress, Bigtable returns an `UNAVAILABLE` error with the message `A DropRowRange operation is already ongoing`. To resolve the error, send the request again.
  * With instances that use replication, be aware that Bigtable might take a long time to complete the operation due to increased replication latency and CPU usage. To delete data from an instance that uses replication, use the Data API to read and then delete your data.



The following code samples show how to drop a range of rows that start with the row key prefix `phone#5c10102`:

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/bigtable"
    )
    
    func dropRowRange(w io.Writer, projectID, instanceID, tableName string) error {
    	ctx := context.Background()
    	adminClient, err := bigtable.[NewAdminClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_AdminClient_NewAdminClient)(ctx, projectID, instanceID)
    	if err != nil {
    		return fmt.Errorf("bigtable.NewAdminClient: %w", err)
    	}
    	defer adminClient.Close()
    
    	// Use a specific row key prefix to drop.
    	prefix := "phone#4c410523"
    	if err := adminClient.DropRowRange(ctx, tableName, prefix); err != nil {
    		return fmt.Errorf("adminClient.DropRowRange: %w", err)
    	}
    
    	fmt.Fprintf(w, "Successfully dropped row range with prefix: %s\n", prefix)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    import com.google.bigtable.admin.v2.DropRowRangeRequest;
    import com.google.cloud.bigtable.admin.v2.[BigtableTableAdminClientV2](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.BigtableTableAdminClientV2.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.IOException;
    
    public class DropRowRangeExample {
      public void dropRowRange(String projectId, String instanceId, String tableId) throws IOException {
        try ([BigtableTableAdminClientV2](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.BigtableTableAdminClientV2.html) tableAdminClient = [BigtableTableAdminClientV2](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.BigtableTableAdminClientV2.html).create()) {
          DropRowRangeRequest request =
              DropRowRangeRequest.newBuilder()
                  .setName("projects/" + projectId + "/instances/" + instanceId + "/tables/" + tableId)
                  .setRowKeyPrefix([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFromUtf8](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFromUtf8_java_lang_String_)("phone#4c410523"))
                  .build();
          tableAdminClient.dropRowRange(request);
        }
      }
    }

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    def drop_row_range(project_id, instance_id, table_id):
        from google.cloud.bigtable import [Client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html)
    
        client = Client(project=project_id, admin=True)
        instance = [client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.html).[instance](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html#google_cloud_bigtable_client_Client_instance)(instance_id)
        table = instance.table(table_id)
        row_key_prefix = "phone#4c410523"
        table.[drop_by_prefix](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.table.Table.html#google_cloud_bigtable_table_Table_drop_by_prefix)(row_key_prefix, timeout=200)
    
    

### Node.js

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    await table.deleteRows('phone#5c10102');
    await printRows();

**Note:** You can delete all rows in the table without specifying the row key prefix when you use the [`cbt deleteallrows`](https://docs.cloud.google.com/bigtable/docs/cbt-reference#delete_all_rows) command. If the command times out, you can rerun the command until the operation completes.

## Delete data using Data API methods

If you need to delete small amounts of non-contiguous data, deleting data using a method that calls the Cloud Bigtable API (Data API) is often the best choice. Use these methods if you are deleting MB, not GB, of data in a request. Using the Data API is the only way to delete data from a column (not column family).

Data API methods call `MutateRows` with one of three mutation types:

  * DeleteFromColumn
  * DeleteFromFamily
  * DeleteFromRow



A delete request using the Data API is atomic: either the request succeeds and all data is deleted, or the request fails and no data is removed.

In most cases, avoid using `CheckAndMutate` methods to delete data. In the rare event that you require strong consistency, you might want to use this approach, but be aware that it is resource-intensive and performance might be affected.

To use `MutateRows` to delete data, you send a `readRows` request with a filter to determine what you want to delete, and then you send the deletion request. For a list of the filters that are available, see [Filters](https://docs.cloud.google.com/bigtable/docs/filters).

**Samples in this section assume that you have already determined what data to delete.**

### Delete from a column

The following code samples demonstrate how to delete all the cells from a column in a row:

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/bigtable"
    )
    
    func deleteFromColumn(w io.Writer, projectID, instanceID, tableName string) error {
    	ctx := context.Background()
    	client, err := bigtable.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Client_NewClient)(ctx, projectID, instanceID)
    	if err != nil {
    		return fmt.Errorf("bigtable.NewClient: %w", err)
    	}
    	defer client.Close()
    	tbl := client.[Open](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Client_Open)(tableName)
    
    	// Use a specific row key, column family, and column name that exists in your table.
    	// This sample assumes a schema with a "cell_plan" column family.
    	rowKey := "phone#4c410523#20190501"
    	columnFamilyName := "cell_plan"
    	columnName := "data_plan_01gb"
    	mut := bigtable.[NewMutation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Mutation_NewMutation)()
    	mut.[DeleteCellsInColumn](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Mutation_DeleteCellsInColumn)(columnFamilyName, columnName)
    
    	if err := tbl.Apply(ctx, rowKey, mut); err != nil {
    		return fmt.Errorf("tbl.Apply: %w", err)
    	}
    
    	fmt.Fprintf(w, "Successfully deleted cells from column %s:%s for row: %s\n", columnFamilyName, columnName, rowKey)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    import com.google.cloud.bigtable.data.v2.[BigtableDataClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html);
    import com.google.cloud.bigtable.data.v2.models.[Mutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Mutation.html);
    import com.google.cloud.bigtable.data.v2.models.[RowMutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.RowMutation.html);
    import com.google.cloud.bigtable.data.v2.models.[TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.TableId.html);
    import java.io.IOException;
    
    public class DeleteFromColumnExample {
      public void deleteFromColumnCells(String projectId, String instanceId, String tableId)
          throws IOException {
        try ([BigtableDataClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html) dataClient = [BigtableDataClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html).create(projectId, instanceId)) {
          [Mutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Mutation.html) mutation = [Mutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Mutation.html).create().deleteCells("cell_plan", "data_plan_01gb");
          dataClient.[mutateRow](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html#com_google_cloud_bigtable_data_v2_BigtableDataClient_mutateRow_com_google_cloud_bigtable_data_v2_models_RowMutation_)(
              [RowMutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.RowMutation.html).create([TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.TableId.html).of(tableId), "phone#4c410523#20190501", mutation));
        }
      }
    }

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    def delete_from_column(project_id, instance_id, table_id):
        from google.cloud.bigtable import [Client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html)
    
        client = Client(project=project_id, admin=True)
        instance = [client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.html).[instance](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html#google_cloud_bigtable_client_Client_instance)(instance_id)
        table = instance.table(table_id)
        row = table.row("phone#4c410523#20190501")
        row.delete_cell(column_family_id="cell_plan", column="data_plan_01gb")
        row.commit()
    
    

### Python asyncio

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    async def delete_from_column(project_id, instance_id, table_id):
        from google.cloud.bigtable.data import BigtableDataClientAsync
        from google.cloud.bigtable.data import [DeleteRangeFromColumn](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.mutations.DeleteRangeFromColumn.html)
    
        client = BigtableDataClientAsync(project=project_id)
        table = client.get_table(instance_id, table_id)
    
        await table.mutate_row(
            "phone#4c410523#20190501",
            DeleteRangeFromColumn(family="cell_plan", qualifier=b"data_plan_01gb"),
        )
    
        await table.close()
        await client.close()
    
    

### Node.js

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    await table.mutate({
      key: 'phone#4c410523#20190501',
      method: 'delete',
      data: {
        column: 'cell_plan:data_plan_05gb',
      },
    });
    await printRows();

### Delete from a column family

The following code samples demonstrate how to delete cells from a column family in a row:

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/bigtable"
    )
    
    func deleteFromColumnFamily(w io.Writer, projectID, instanceID, tableName string) error {
    	ctx := context.Background()
    	client, err := bigtable.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Client_NewClient)(ctx, projectID, instanceID)
    	if err != nil {
    		return fmt.Errorf("bigtable.NewClient: %w", err)
    	}
    	defer client.Close()
    	tbl := client.[Open](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Client_Open)(tableName)
    
    	// Use a specific row key and column family that exists in your table.
    	// This sample assumes a schema with a "stats_summary" column family.
    	rowKey := "phone#5c10102#20190501"
    	columnFamilyName := "stats_summary"
    	mut := bigtable.[NewMutation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Mutation_NewMutation)()
    	mut.[DeleteCellsInFamily](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Mutation_DeleteCellsInFamily)(columnFamilyName)
    
    	if err := tbl.Apply(ctx, rowKey, mut); err != nil {
    		return fmt.Errorf("tbl.Apply: %w", err)
    	}
    
    	fmt.Fprintf(w, "Successfully deleted cells from family %s for row: %s\n", columnFamilyName, rowKey)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    import com.google.cloud.bigtable.data.v2.[BigtableDataClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html);
    import com.google.cloud.bigtable.data.v2.models.[RowMutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.RowMutation.html);
    import com.google.cloud.bigtable.data.v2.models.[TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.TableId.html);
    import java.io.IOException;
    
    public class DeleteFromColumnFamilyExample {
      public void deleteFromColumnFamily(String projectId, String instanceId, String tableId)
          throws IOException {
        try ([BigtableDataClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html) dataClient = [BigtableDataClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html).create(projectId, instanceId)) {
          dataClient.[mutateRow](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html#com_google_cloud_bigtable_data_v2_BigtableDataClient_mutateRow_com_google_cloud_bigtable_data_v2_models_RowMutation_)(
              [RowMutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.RowMutation.html).create([TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.TableId.html).of(tableId), "phone#5c10102#20190501")
                  .deleteFamily("stats_summary"));
        }
      }
    }

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    def delete_from_column_family(project_id, instance_id, table_id):
        from google.cloud.bigtable import [Client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html)
    
        client = Client(project=project_id, admin=True)
        instance = [client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.html).[instance](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html#google_cloud_bigtable_client_Client_instance)(instance_id)
        table = instance.table(table_id)
        row = table.row("phone#4c410523#20190501")
        row.delete_cells(column_family_id="cell_plan", columns=row.ALL_COLUMNS)
        row.commit()
    
    

### Python asyncio

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    async def delete_from_column_family(project_id, instance_id, table_id):
        from google.cloud.bigtable.data import BigtableDataClientAsync
        from google.cloud.bigtable.data import [DeleteAllFromFamily](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.mutations.DeleteAllFromFamily.html)
    
        client = BigtableDataClientAsync(project=project_id)
        table = client.get_table(instance_id, table_id)
    
        await table.mutate_row("phone#4c410523#20190501", DeleteAllFromFamily("cell_plan"))
    
        await table.close()
        await client.close()
    
    

### Node.js

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    await table.mutate({
      key: 'phone#4c410523#20190501',
      method: 'delete',
      data: {
        column: 'cell_plan',
      },
    });
    await printRows();

### Delete from a row

The following code snippets demonstrate how to delete all the cells from a row:

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/bigtable"
    )
    
    func deleteFromRow(w io.Writer, projectID, instanceID, tableName string) error {
    	ctx := context.Background()
    	client, err := bigtable.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Client_NewClient)(ctx, projectID, instanceID)
    	if err != nil {
    		return fmt.Errorf("bigtable.NewClient: %w", err)
    	}
    	defer client.Close()
    	tbl := client.[Open](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Client_Open)(tableName)
    
    	// Use a specific row key that exists in your table.
    	rowKey := "phone#4c410523#20190501"
    	mut := bigtable.[NewMutation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Mutation_NewMutation)()
    	mut.[DeleteRow](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Mutation_DeleteRow)()
    
    	if err := tbl.Apply(ctx, rowKey, mut); err != nil {
    		return fmt.Errorf("tbl.Apply: %w", err)
    	}
    
    	fmt.Fprintf(w, "Successfully deleted row: %s\n", rowKey)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    import com.google.cloud.bigtable.data.v2.[BigtableDataClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html);
    import com.google.cloud.bigtable.data.v2.models.[Mutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Mutation.html);
    import com.google.cloud.bigtable.data.v2.models.[RowMutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.RowMutation.html);
    import com.google.cloud.bigtable.data.v2.models.[TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.TableId.html);
    import java.io.IOException;
    
    public class DeleteFromRowExample {
      public void deleteFromRow(String projectId, String instanceId, String tableId)
          throws IOException {
        try ([BigtableDataClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html) dataClient = [BigtableDataClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html).create(projectId, instanceId)) {
          [Mutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Mutation.html) mutation = [Mutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Mutation.html).create().deleteRow();
          dataClient.[mutateRow](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html#com_google_cloud_bigtable_data_v2_BigtableDataClient_mutateRow_com_google_cloud_bigtable_data_v2_models_RowMutation_)(
              [RowMutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.RowMutation.html).create([TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.TableId.html).of(tableId), "phone#4c410523#20190501", mutation));
        }
      }
    }

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    def delete_from_row(project_id, instance_id, table_id):
        from google.cloud.bigtable import [Client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html)
    
        client = Client(project=project_id, admin=True)
        instance = [client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.html).[instance](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html#google_cloud_bigtable_client_Client_instance)(instance_id)
        table = instance.table(table_id)
        row = table.row("phone#4c410523#20190501")
        row.delete()
        row.commit()
    
    

### Python asyncio

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    async def delete_from_row(project_id, instance_id, table_id):
        from google.cloud.bigtable.data import BigtableDataClientAsync
        from google.cloud.bigtable.data import [DeleteAllFromRow](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.mutations.DeleteAllFromRow.html)
    
        client = BigtableDataClientAsync(project=project_id)
        table = client.get_table(instance_id, table_id)
    
        await table.mutate_row("phone#4c410523#20190501", DeleteAllFromRow())
    
        await table.close()
        await client.close()
    
    

### Node.js

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    const row = table.row('phone#4c410523#20190501');
    await row.delete();
    await printRows();

## Delete by streaming and batching

Streaming and batching your delete requests is often the best way to delete large amounts of data. This strategy can be useful when you have finer-grained data retention requirements than [garbage collection](https://docs.cloud.google.com/bigtable/docs/garbage-collection) policies allow.

If your application is written in Java, you can enable batch write flow control when you send batch deletes to Bigtable. For more information, see [Batch write flow control](https://docs.cloud.google.com/bigtable/docs/writes#flow-control) and [Enable batch write flow control](https://docs.cloud.google.com/bigtable/docs/writing-data#batch-write-flow-control).

The following code samples start a stream of data (reading rows), batch them, and then go through the batch and delete all the cells in column `data_plan_01gb1` in the `cell_plan` column family:

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    // Copyright 2025 Google LLC
    //
    // Licensed under the Apache License, Version 2.0 (the "License");
    // you may not use this file except in compliance with the License.
    // You may obtain a copy of the License at
    //
    //     https://www.apache.org/licenses/LICENSE-2.0
    //
    // Unless required by applicable law or agreed to in writing, software
    // distributed under the License is distributed on an "AS IS" BASIS,
    // WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    // See the License for the specific language governing permissions and
    // limitations under the License.
    
    package deletes
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/bigtable"
    )
    
    // streamingAndBatching starts a stream of data (reading rows), batches them, and then goes through the batch and deletes all the cells in column
    func streamingAndBatching(w io.Writer, projectID, instanceID string, tableName string) error {
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
    
    	// Slices to hold the row keys and the corresponding mutations.
    	var rowKeys []string
    	var mutations []*bigtable.Mutation
    
    	// Read all rows from the table.
    	err = tbl.ReadRows(ctx, bigtable.[InfiniteRange](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_RowRange_InfiniteRange)(""), func(row bigtable.Row) bool {
    		// For each row, create a mutation to delete the specified cell.
    		mut := bigtable.[NewMutation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Mutation_NewMutation)()
    		mut.[DeleteCellsInColumn](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Mutation_DeleteCellsInColumn)("cell_plan", "data_plan_01gb")
    
    		// Append the row key and mutation to the slices.
    		rowKeys = append(rowKeys, row.[Key](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Row_Key)())
    		mutations = append(mutations, mut)
    
    		// Continue processing rows.
    		return true
    	})
    	if err != nil {
    		return fmt.Errorf("tbl.ReadRows: %w", err)
    	}
    
    	if len(mutations) == 0 {
    		return nil
    	}
    	// If there are mutations to apply, apply them in a single bulk request.
    	// ApplyBulk returns a slice of errors, one for each mutation.
    	var errs []error
    	if errs, err = tbl.ApplyBulk(ctx, rowKeys, mutations); err != nil {
    		return fmt.Errorf("tbl.ApplyBulk: %w", err)
    	}
    	if errs != nil {
    		// Log any individual errors that occurred during the bulk operation.
    		var errorCount int
    		for _, individualErr := range errs {
    			if individualErr != nil {
    				fmt.Fprintf(w, "Error applying mutation: %v\n", individualErr)
    				errorCount++
    			}
    		}
    		if errorCount > 0 {
    			return fmt.Errorf("encountered %d error(s) out of %d mutations", errorCount, len(errs))
    		}
    	}
    
    	fmt.Fprintf(w, "Successfully deleted cells from all rows")
    	return nil
    }
    
    

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    import com.google.api.gax.[batching](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.Callables.html#com_google_api_gax_rpc_Callables__RequestT_ResponseT_batching_com_google_api_gax_rpc_UnaryCallable_RequestT_ResponseT__com_google_api_gax_rpc_BatchingCallSettings_RequestT_ResponseT__com_google_api_gax_rpc_ClientContext_).[Batcher](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.batching.Batcher.html);
    import com.google.api.gax.rpc.[ServerStream](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ServerStream.html);
    import com.google.cloud.bigtable.data.v2.[BigtableDataClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html);
    import com.google.cloud.bigtable.data.v2.models.[Query](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Query.html);
    import com.google.cloud.bigtable.data.v2.models.[Row](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Row.html);
    import com.google.cloud.bigtable.data.v2.models.[RowMutationEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.RowMutationEntry.html);
    import com.google.cloud.bigtable.data.v2.models.[TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.TableId.html);
    import java.io.IOException;
    
    public class BatchDeleteExample {
      public void batchDelete(String projectId, String instanceId, String tableId)
          throws InterruptedException, IOException {
        try ([BigtableDataClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html) dataClient = [BigtableDataClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html).create(projectId, instanceId)) {
          try (Batcher<RowMutationEntry, Void> batcher =
              dataClient.[newBulkMutationBatcher](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html#com_google_cloud_bigtable_data_v2_BigtableDataClient_newBulkMutationBatcher_com_google_cloud_bigtable_data_v2_models_TargetId_)([TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.TableId.html).of(tableId))) {
            ServerStream<Row> rows = dataClient.[readRows](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html#com_google_cloud_bigtable_data_v2_BigtableDataClient_readRows_com_google_cloud_bigtable_data_v2_models_Query_)([Query](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Query.html).create([TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.TableId.html).of(tableId)));
            for ([Row](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Row.html) row : rows) {
              batcher.add(
                  [RowMutationEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.RowMutationEntry.html).create(row.getKey()).deleteCells("cell_plan", "data_plan_05gb"));
            }
            // Blocks until mutations are applied on all submitted row entries.
            batcher.flush();
          }
        }
      }
    }

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    def streaming_and_batching(project_id, instance_id, table_id):
        from google.cloud.bigtable import [Client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html)
    
        client = Client(project=project_id, admin=True)
        instance = [client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.html).[instance](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html#google_cloud_bigtable_client_Client_instance)(instance_id)
        table = instance.table(table_id)
        batcher = table.mutations_batcher(flush_count=2)
        rows = table.read_rows()
        for row in rows:
            row = table.row(row.row_key)
            row.delete_cell(column_family_id="cell_plan", column="data_plan_01gb")
    
        [batcher](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.batcher.html).mutate_rows(rows)
    
    

### Python asyncio

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    async def streaming_and_batching(project_id, instance_id, table_id):
        from google.cloud.bigtable.data import BigtableDataClientAsync
        from google.cloud.bigtable.data import [DeleteRangeFromColumn](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.mutations.DeleteRangeFromColumn.html)
        from google.cloud.bigtable.data import [RowMutationEntry](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.mutations.RowMutationEntry.html)
        from google.cloud.bigtable.data import [ReadRowsQuery](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.read_rows_query.ReadRowsQuery.html)
    
        client = BigtableDataClientAsync(project=project_id)
        table = client.get_table(instance_id, table_id)
    
        async with table.mutations_batcher() as batcher:
            async for row in await table.read_rows_stream(ReadRowsQuery(limit=10)):
                await batcher.append(
                    RowMutationEntry(
                        [row](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row.html).row_key,
                        DeleteRangeFromColumn(
                            family="cell_plan", qualifier=b"data_plan_01gb"
                        ),
                    )
                )
    
        await table.close()
        await client.close()
    
    

### Node.js

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    const rows = (await table.getRows({limit: 2}))[0];
    const entries = rows.map(row => {
      return {
        key: row.id,
        method: 'delete',
        data: {
          column: 'cell_plan:data_plan_05gb',
        },
      };
    });
    await table.mutate(entries);
    await printRows();

## Delete data in an authorized view

You can delete table data by sending a delete request to an authorized view. You must use one of the following:

  * gcloud CLI
  * Bigtable client for Java



When you delete data from an authorized view, you supply the authorized view ID in addition to the table ID.

The data that you can delete from an authorized view is limited by the authorized view definition. You can only delete data that is included in the authorized view. If you attempt to delete data that is outside of the authorized view definition or is subject to the following rules, an error of `PERMISSION_DENIED` is returned:

  * Deleting a range of rows from an authorized view using `DropRowRange` in the admin API is not supported.
  * Deleting from a row is not supported.
  * Deleting from a column is supported as long as it's for rows that are in the authorized view.
  * Deleting from a column family is only permitted if the specified column family is configured to allow all column qualifier prefixes (`qualifier_prefixes=""`) in the authorized view.



For example, if you attempt to delete from a specified row, and that row contains columns in the underlying table that are not in your authorized view, then the request fails.

## What's next

  * [Review the list of unsupported HBase deletes.](https://docs.cloud.google.com/bigtable/docs/hbase-differences#mutations_and_deletions)
  * [Monitor your Bigtable resources.](https://docs.cloud.google.com/bigtable/docs/monitoring-instance)

  * [Implement counters by using aggregate cells.](https://docs.cloud.google.com/bigtable/docs/aggregates)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
