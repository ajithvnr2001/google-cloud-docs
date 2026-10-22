---
url: https://docs.cloud.google.com/bigtable/docs/samples-java-hello-world/
title: Java hello world \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:35.351420+00:00
---

# Java hello world  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples-java-hello-world/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Java hello world

This code sample is a "hello world" application written in Java, using the Bigtable client library for Java. The sample illustrates how to complete the following tasks:

  * Set up authentication
  * Connect to a Bigtable instance.
  * Create a new table.
  * Write data to the table.
  * Read the data back.
  * Delete the table.



## Running the sample

This code communicates with Bigtable using the Bigtable client library in the [Google Cloud client libraries for Java](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/overview).

Before you begin, follow the setup steps described in the [reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/overview#getting-started).

## Using the Cloud Client Libraries with Bigtable

The sample application connects to Bigtable and demonstrates some basic operations.

### Connecting to Bigtable

To get started, you need a data client that you use to communicate with the data API client library and a table admin client that you use to communicate with the admin API client library.

First, instantiate a [`BigtableDataSettings`](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataSettings) object that includes the project ID and instance ID that the `hello world` application will use. Then pass the settings to the [`BigtableDataClient.create()`](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient#com_google_cloud_bigtable_data_v2_BigtableDataClient_create_com_google_cloud_bigtable_data_v2_BigtableDataSettings_) method to create the data client.

Similarly, for the admin client, first establish the settings by creating a [`BigtableTableAdminSettings`](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.BigtableTableAdminSettings) object, then use the settings to create a [`BigtableTableAdminClient`](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.BigtableTableAdminClient) object.

As a best practice, when you use Bigtable you should always create a client once and reuse it throughout the application.
    
    
    // Creates the settings to configure a bigtable data client.
    BigtableDataSettings settings =
        BigtableDataSettings.newBuilder().setProjectId(projectId).setInstanceId(instanceId).build();
    
    // Creates a bigtable data client.
    dataClient = BigtableDataClient.create(settings);
    
    // Creates a bigtable table admin client.
    adminClient = BigtableTableAdminClientV2.create();

### Creating a table

To create a table, build a [`CreateTableRequest`](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.BigtableTableAdminClient#com_google_cloud_bigtable_admin_v2_BigtableTableAdminClient_createTable_com_google_cloud_bigtable_admin_v2_models_CreateTableRequest_) object and pass it to the admin client's [`createTable()`](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.BigtableTableAdminClient#com_google_cloud_bigtable_admin_v2_BigtableTableAdminClient_createTable_com_google_cloud_bigtable_admin_v2_models_CreateTableRequest_) method.

**Note:** Columns that are related to one another are typically grouped into a column family. For more information about column families, see the [Bigtable storage model](https://docs.cloud.google.com/bigtable/docs/overview#storage-model).
    
    
    // Checks if table exists, creates table if does not exist.
    boolean exists = false;
    try {
      adminClient.getTable(
          GetTableRequest.newBuilder()
              .setName("projects/" + projectId + "/instances/" + instanceId + "/tables/" + tableId)
              .setView(Table.View.NAME_ONLY)
              .build());
      exists = true;
    } catch (NotFoundException e) {
      // ignore
    }
    if (!exists) {
      System.out.println("Creating table: " + tableId);
      String parent = "projects/" + projectId + "/instances/" + instanceId;
      CreateTableRequest request =
          CreateTableRequest.newBuilder()
              .setParent(parent)
              .setTableId(tableId)
              .setTable(
                  Table.newBuilder()
                      .putColumnFamilies(COLUMN_FAMILY, ColumnFamily.getDefaultInstance())
                      .build())
              .build();
      adminClient.createTable(request);
      System.out.printf("Table %s created successfully%n", tableId);
    }

### Writing rows to a table

Create a `greetings[]` string array containing three greetings, to use as a source of data to write to the table. Loop through the array. In each iteration of the loop, create a [`RowMutation`](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient#com_google_cloud_bigtable_data_v2_BigtableDataClient_readRows_com_google_cloud_bigtable_data_v2_models_Query_) object and use the [`setCell()`](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.RowMutation) method to add an entry to the mutation.

**Note:** In this sample application, `setCell()` is only called once per mutation, but you can call it up to 10,000 times per single mutation.
    
    
    try {
      System.out.println("\nWriting some greetings to the table");
      String[] names = {"World", "Bigtable", "Java"};
      for (int i = 0; i < names.length; i++) {
        String greeting = "Hello " + names[i] + "!";
        RowMutation rowMutation =
            RowMutation.create(TableId.of(tableId), ROW_KEY_PREFIX + i)
                .setCell(COLUMN_FAMILY, COLUMN_QUALIFIER_NAME, names[i])
                .setCell(COLUMN_FAMILY, COLUMN_QUALIFIER_GREETING, greeting);
        dataClient.mutateRow(rowMutation);
        System.out.println(greeting);
      }
    } catch (NotFoundException e) {
      System.err.println("Failed to write to non-existent table: " + e.getMessage());
    }

### Reading a row by its row key

Use the data client's [`readRow()`](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient#com_google_cloud_bigtable_data_v2_BigtableDataClient_readRow_java_lang_String_com_google_protobuf_ByteString_) method to read the first row that you wrote.
    
    
    try {
      System.out.println("\nReading a single row by row key");
      Row row = dataClient.readRow(TableId.of(tableId), ROW_KEY_PREFIX + 0);
      System.out.println("Row: " + row.getKey().toStringUtf8());
      for (RowCell cell : row.getCells()) {
        System.out.printf(
            "Family: %s    Qualifier: %s    Value: %s%n",
            cell.getFamily(), cell.getQualifier().toStringUtf8(), cell.getValue().toStringUtf8());
      }
      return row;
    } catch (NotFoundException e) {
      System.err.println("Failed to read from a non-existent table: " + e.getMessage());
      return null;
    }
    try {
      System.out.println("\nReading specific cells by family and qualifier");
      Row row = dataClient.readRow(TableId.of(tableId), ROW_KEY_PREFIX + 0);
      System.out.println("Row: " + row.getKey().toStringUtf8());
      List<RowCell> cells = row.getCells(COLUMN_FAMILY, COLUMN_QUALIFIER_NAME);
      for (RowCell cell : cells) {
        System.out.printf(
            "Family: %s    Qualifier: %s    Value: %s%n",
            cell.getFamily(), cell.getQualifier().toStringUtf8(), cell.getValue().toStringUtf8());
      }
      return cells;
    } catch (NotFoundException e) {
      System.err.println("Failed to read from a non-existent table: " + e.getMessage());
      return null;
    }

### Scanning all table rows

Next, scan the entire table. Create a [`Query`](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Query) object, pass it to the [`readRows()`](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient#com_google_cloud_bigtable_data_v2_BigtableDataClient_readRows_com_google_cloud_bigtable_data_v2_models_Query_) method, and assign the results to a row stream.
    
    
    try {
      System.out.println("\nReading the entire table");
      Query query = Query.create(TableId.of(tableId));
      ServerStream<Row> rowStream = dataClient.readRows(query);
      List<Row> tableRows = new ArrayList<>();
      for (Row r : rowStream) {
        System.out.println("Row Key: " + r.getKey().toStringUtf8());
        tableRows.add(r);
        for (RowCell cell : r.getCells()) {
          System.out.printf(
              "Family: %s    Qualifier: %s    Value: %s%n",
              cell.getFamily(), cell.getQualifier().toStringUtf8(), cell.getValue().toStringUtf8());
        }
      }
      return tableRows;
    } catch (NotFoundException e) {
      System.err.println("Failed to read a non-existent table: " + e.getMessage());
      return null;
    }

### Deleting a table

Finally, delete the table with the [`deleteTable()`](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.BigtableTableAdminClient#com_google_cloud_bigtable_admin_v2_BigtableTableAdminClient_deleteTable_java_lang_String_) method.
    
    
    System.out.println("\nDeleting table: " + tableId);
    try {
      String tableName =
          "projects/" + projectId + "/instances/" + instanceId + "/tables/" + tableId;
      adminClient.deleteTable(tableName);
      System.out.printf("Table %s deleted successfully%n", tableId);
    } catch (NotFoundException e) {
      System.err.println("Failed to delete a non-existent table: " + e.getMessage());
    }

## Putting it all together

Here is the full code sample without comments.
    
    
    package com.example.bigtable;
    
    
    import static com.google.cloud.bigtable.data.v2.models.[Filters](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Filters.html).FILTERS;
    
    import com.google.api.gax.rpc.[NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html);
    import com.google.api.gax.rpc.[ServerStream](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ServerStream.html);
    import com.google.bigtable.admin.v2.[ColumnFamily](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.ColumnFamily.html);
    import com.google.bigtable.admin.v2.[CreateTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.CreateTableRequest.html);
    import com.google.bigtable.admin.v2.GetTableRequest;
    import com.google.bigtable.admin.v2.[Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.Table.html);
    import com.google.cloud.bigtable.admin.v2.[BigtableTableAdminClientV2](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.BigtableTableAdminClientV2.html);
    import com.google.cloud.bigtable.data.v2.[BigtableDataClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html);
    import com.google.cloud.bigtable.data.v2.[BigtableDataSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataSettings.html);
    import com.google.cloud.bigtable.data.v2.models.[Filters](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Filters.html).Filter;
    import com.google.cloud.bigtable.data.v2.models.[Query](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Query.html);
    import com.google.cloud.bigtable.data.v2.models.[Row](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Row.html);
    import com.google.cloud.bigtable.data.v2.models.[RowCell](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.RowCell.html);
    import com.google.cloud.bigtable.data.v2.models.[RowMutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.RowMutation.html);
    import com.google.cloud.bigtable.data.v2.models.[TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.TableId.html);
    import java.io.IOException;
    import java.nio.charset.StandardCharsets;
    import java.util.ArrayList;
    import java.util.Base64;
    import java.util.List;
    
    
    public class HelloWorld {
    
      private static final String COLUMN_FAMILY = "cf1";
      private static final String COLUMN_QUALIFIER_GREETING = "greeting";
      private static final String COLUMN_QUALIFIER_NAME = "name";
      private static final String ROW_KEY_PREFIX = "rowKey";
      private final String projectId;
      private final String instanceId;
      private final String tableId;
      private final [BigtableDataClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html) dataClient;
      private final [BigtableTableAdminClientV2](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.BigtableTableAdminClientV2.html) adminClient;
    
      public static void main(String[] args) throws Exception {
    
        if (args.length != 2) {
          System.out.println("Missing required project id or instance id");
          return;
        }
        String projectId = args[0];
        String instanceId = args[1];
    
        HelloWorld helloWorld = new HelloWorld(projectId, instanceId, "test-table");
        helloWorld.[run](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.Watchdog.html#com_google_api_gax_rpc_Watchdog_run__)();
      }
    
      public HelloWorld(String projectId, String instanceId, String tableId) throws IOException {
        this.projectId = projectId;
        this.instanceId = instanceId;
        this.tableId = tableId;
    
        [BigtableDataSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataSettings.html) settings =
            [BigtableDataSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataSettings.html).newBuilder().setProjectId(projectId).setInstanceId(instanceId).build();
    
        dataClient = [BigtableDataClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html).create(settings);
    
        adminClient = [BigtableTableAdminClientV2](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.BigtableTableAdminClientV2.html).create();
      }
    
      public void run() throws Exception {
        createTable();
        writeToTable();
        readSingleRow();
        readSpecificCells();
        readTable();
        filterLimitCellsPerCol(tableId);
        deleteTable();
        close();
      }
    
      public void close() {
        dataClient.[close](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html#com_google_cloud_bigtable_data_v2_BigtableDataClient_close__)();
        adminClient.[close](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.BigtableTableAdminClientV2.html#com_google_cloud_bigtable_admin_v2_BigtableTableAdminClientV2_close__)();
      }
    
      public void createTable() {
        boolean exists = false;
        try {
          adminClient.getTable(
              GetTableRequest.newBuilder()
                  .setName("projects/" + projectId + "/instances/" + instanceId + "/tables/" + tableId)
                  .setView([Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.Table.html).View.NAME_ONLY)
                  .build());
          exists = true;
        } catch ([NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html) e) {
        }
        if (!exists) {
          System.out.println("Creating table: " + tableId);
          String parent = "projects/" + projectId + "/instances/" + instanceId;
          [CreateTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.CreateTableRequest.html) request =
              [CreateTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.CreateTableRequest.html).newBuilder()
                  .setParent(parent)
                  .[setTableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.RestoreTableRequest.html#com_google_cloud_bigtable_admin_v2_models_RestoreTableRequest_setTableId_java_lang_String_)(tableId)
                  .setTable(
                      [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.Table.html).newBuilder()
                          .putColumnFamilies(COLUMN_FAMILY, [ColumnFamily](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.ColumnFamily.html).[getDefaultInstance](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.EndpointContext.html#com_google_api_gax_rpc_EndpointContext_getDefaultInstance__)())
                          .build())
                  .build();
          adminClient.createTable(request);
          System.out.printf("Table %s created successfully%n", tableId);
        }
      }
    
      public void writeToTable() {
        try {
          System.out.println("\nWriting some greetings to the table");
          String[] names = {"World", "Bigtable", "Java"};
          for (int i = 0; i < names.length; i++) {
            String greeting = "Hello " + names[i] + "!";
            [RowMutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.RowMutation.html) rowMutation =
                [RowMutation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.RowMutation.html).create([TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.TableId.html).of(tableId), ROW_KEY_PREFIX + i)
                    .setCell(COLUMN_FAMILY, COLUMN_QUALIFIER_NAME, names[i])
                    .setCell(COLUMN_FAMILY, COLUMN_QUALIFIER_GREETING, greeting);
            dataClient.[mutateRow](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html#com_google_cloud_bigtable_data_v2_BigtableDataClient_mutateRow_com_google_cloud_bigtable_data_v2_models_RowMutation_)(rowMutation);
            System.out.println(greeting);
          }
        } catch ([NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html) e) {
          System.err.println("Failed to write to non-existent table: " + e.getMessage());
        }
      }
    
      public [Row](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Row.html) readSingleRow() {
        try {
          System.out.println("\nReading a single row by row key");
          [Row](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Row.html) row = dataClient.[readRow](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html#com_google_cloud_bigtable_data_v2_BigtableDataClient_readRow_com_google_cloud_bigtable_data_v2_models_TargetId_com_google_protobuf_ByteString_)([TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.TableId.html).of(tableId), ROW_KEY_PREFIX + 0);
          System.out.println("Row: " + row.[getKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Row.html#com_google_cloud_bigtable_data_v2_models_Row_getKey__)().toStringUtf8());
          for ([RowCell](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.RowCell.html) cell : row.[getCells](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Row.html#com_google_cloud_bigtable_data_v2_models_Row_getCells__)()) {
            System.out.printf(
                "Family: %s    Qualifier: %s    Value: %s%n",
                cell.getFamily(), cell.getQualifier().toStringUtf8(), cell.getValue().toStringUtf8());
          }
          return row;
        } catch ([NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html) e) {
          System.err.println("Failed to read from a non-existent table: " + e.getMessage());
          return null;
        }
      }
    
      public List<RowCell> readSpecificCells() {
        try {
          System.out.println("\nReading specific cells by family and qualifier");
          [Row](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Row.html) row = dataClient.[readRow](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html#com_google_cloud_bigtable_data_v2_BigtableDataClient_readRow_com_google_cloud_bigtable_data_v2_models_TargetId_com_google_protobuf_ByteString_)([TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.TableId.html).of(tableId), ROW_KEY_PREFIX + 0);
          System.out.println("Row: " + row.[getKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Row.html#com_google_cloud_bigtable_data_v2_models_Row_getKey__)().toStringUtf8());
          List<RowCell> cells = row.[getCells](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Row.html#com_google_cloud_bigtable_data_v2_models_Row_getCells__)(COLUMN_FAMILY, COLUMN_QUALIFIER_NAME);
          for ([RowCell](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.RowCell.html) cell : cells) {
            System.out.printf(
                "Family: %s    Qualifier: %s    Value: %s%n",
                cell.getFamily(), cell.getQualifier().toStringUtf8(), cell.getValue().toStringUtf8());
          }
          return cells;
        } catch ([NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html) e) {
          System.err.println("Failed to read from a non-existent table: " + e.getMessage());
          return null;
        }
      }
    
      public List<Row> readTable() {
        try {
          System.out.println("\nReading the entire table");
          [Query](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Query.html) query = [Query](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Query.html).create([TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.TableId.html).of(tableId));
          ServerStream<Row> rowStream = dataClient.[readRows](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html#com_google_cloud_bigtable_data_v2_BigtableDataClient_readRows_com_google_cloud_bigtable_data_v2_models_Query_)(query);
          List<Row> tableRows = new ArrayList<>();
          for ([Row](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Row.html) r : rowStream) {
            System.out.println("Row Key: " + r.getKey().toStringUtf8());
            tableRows.add(r);
            for ([RowCell](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.RowCell.html) cell : r.getCells()) {
              System.out.printf(
                  "Family: %s    Qualifier: %s    Value: %s%n",
                  cell.getFamily(), cell.getQualifier().toStringUtf8(), cell.getValue().toStringUtf8());
            }
          }
          return tableRows;
        } catch ([NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html) e) {
          System.err.println("Failed to read a non-existent table: " + e.getMessage());
          return null;
        }
      }
    
      public void filterLimitCellsPerCol(String tableId) {
        Filter filter = FILTERS.limit().cellsPerColumn(1);
        readRowFilter(tableId, filter);
        readFilter(tableId, filter);
      }
    
    
      private void readRowFilter(String tableId, Filter filter) {
        String rowKey =
            Base64.getEncoder().encodeToString("greeting0".getBytes(StandardCharsets.UTF_8));
        [Row](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Row.html) row = dataClient.[readRow](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html#com_google_cloud_bigtable_data_v2_BigtableDataClient_readRow_com_google_cloud_bigtable_data_v2_models_TargetId_com_google_protobuf_ByteString_)([TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.TableId.html).of(tableId), rowKey, filter);
        printRow(row);
        System.out.println("Row filter completed.");
      }
    
    
      private void readFilter(String tableId, Filter filter) {
        [Query](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Query.html) query = [Query](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Query.html).create([TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.TableId.html).of(tableId)).filter(filter);
        ServerStream<Row> rows = dataClient.[readRows](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html#com_google_cloud_bigtable_data_v2_BigtableDataClient_readRows_com_google_cloud_bigtable_data_v2_models_Query_)(query);
        for ([Row](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Row.html) row : rows) {
          printRow(row);
        }
        System.out.println("Table filter completed.");
      }
    
    
      public void deleteTable() {
        System.out.println("\nDeleting table: " + tableId);
        try {
          String tableName =
              "projects/" + projectId + "/instances/" + instanceId + "/tables/" + tableId;
          adminClient.deleteTable(tableName);
          System.out.printf("Table %s deleted successfully%n", tableId);
        } catch ([NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html) e) {
          System.err.println("Failed to delete a non-existent table: " + e.getMessage());
        }
      }
    
      private static void printRow([Row](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Row.html) row) {
        if (row == null) {
          return;
        }
        System.out.printf("Reading data for %s%n", row.[getKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Row.html#com_google_cloud_bigtable_data_v2_models_Row_getKey__)().toStringUtf8());
        String colFamily = "";
        for ([RowCell](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.RowCell.html) cell : row.[getCells](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Row.html#com_google_cloud_bigtable_data_v2_models_Row_getCells__)()) {
          if (!cell.getFamily().equals(colFamily)) {
            colFamily = cell.getFamily();
            System.out.printf("Column Family %s%n", colFamily);
          }
          String labels =
              cell.getLabels().size() == 0 ? "" : " [" + String.join(",", cell.getLabels()) + "]";
          System.out.printf(
              "\t%s: %s @%s%s%n",
              cell.getQualifier().toStringUtf8(),
              cell.getValue().toStringUtf8(),
              cell.getTimestamp(),
              labels);
        }
        System.out.println();
      }
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
