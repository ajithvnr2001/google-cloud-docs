---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-create-table-external-hivepartitioned/
title: Create external table with hive partitioning \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:41:18.975784+00:00
---

# Create external table with hive partitioning  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-create-table-external-hivepartitioned/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Create external table with hive partitioning Stay organized with collections  Save and categorize content based on your preferences. 

Create an external table using hive partitioning.

## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Go API reference documentation](https://godoc.org/cloud.google.com/go/bigquery). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import (
    	"context"
    	"fmt"
    
    	"cloud.google.com/go/bigquery"
    )
    
    // createTableExternalHivePartitioned demonstrates creating an external table with hive partitioning.
    func createTableExternalHivePartitioned(projectID, datasetID, tableID string) error {
    	// projectID := "my-project-id"
    	// datasetID := "mydatasetid"
    	// tableID := "mytableid"
    	ctx := context.Background()
    
    	client, err := bigquery.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("bigquery.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	// First, we'll define table metadata to represent a table that's backed by parquet files held in
    	// Cloud Storage.
    	//
    	// Example file:
    	// gs://cloud-samples-data/bigquery/hive-partitioning-samples/autolayout/dt=2020-11-15/file1.parquet
    	metadata := &bigquery.[TableMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_TableMetadata){
    		Description: "An example table that demonstrates hive partitioning against external parquet files",
    		ExternalDataConfig: &bigquery.[ExternalDataConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_ExternalDataConfig){
    			SourceFormat: bigquery.[Parquet](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_CSV_Avro_JSON_DatastoreBackup_GoogleSheets_Bigtable_Parquet_ORC_TFSavedModel_XGBoostBooster_Iceberg),
    			SourceURIs:   []string{"gs://cloud-samples-data/bigquery/hive-partitioning-samples/autolayout/*"},
    			AutoDetect:   true,
    		},
    	}
    
    	// The layout of the files in here is compatible with the layout requirements for hive partitioning,
    	// so we can add an optional Hive partitioning configuration to leverage the object paths for deriving
    	// partitioning column information.
    	//
    	// For more information on how partitions are extracted, see:
    	// https://cloud.google.com/bigquery/docs/hive-partitioned-queries-gcs
    	//
    	// We have a "/dt=YYYY-MM-DD/" path component in our example files as documented above.  Autolayout will
    	// expose this as a column named "dt" of type DATE.
    	metadata.[ExternalDataConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_ExternalDataConfig).[HivePartitioningOptions](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_HivePartitioningOptions) = &bigquery.[HivePartitioningOptions](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_HivePartitioningOptions){
    		Mode:                   bigquery.[AutoHivePartitioningMode](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_AutoHivePartitioningMode_StringHivePartitioningMode_CustomHivePartitioningMode),
    		SourceURIPrefix:        "gs://cloud-samples-data/bigquery/hive-partitioning-samples/autolayout/",
    		RequirePartitionFilter: true,
    	}
    
    	// Create the external table.
    	tableRef := client.Dataset(datasetID).Table(tableID)
    	if err := tableRef.Create(ctx, metadata); err != nil {
    		return fmt.Errorf("table creation failure: %w", err)
    	}
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import com.google.cloud.bigquery.[BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html);
    import com.google.cloud.bigquery.[BigQueryException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html);
    import com.google.cloud.bigquery.[BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html);
    import com.google.cloud.bigquery.[ExternalTableDefinition](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.ExternalTableDefinition.html);
    import com.google.cloud.bigquery.[FormatOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.FormatOptions.html);
    import com.google.cloud.bigquery.[HivePartitioningOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.HivePartitioningOptions.html);
    import com.google.cloud.bigquery.[TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId.html);
    import com.google.cloud.bigquery.[TableInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableInfo.html);
    
    // Sample to create external table using hive partitioning
    public class CreateTableExternalHivePartitioned {
    
      public static void main(String[] args) {
        // TODO(developer): Replace these variables before running the sample.
        String datasetName = "MY_DATASET_NAME";
        String tableName = "MY_TABLE_NAME";
        String sourceUri = "gs://cloud-samples-data/bigquery/hive-partitioning-samples/customlayout/*";
        String sourceUriPrefix =
            "gs://cloud-samples-data/bigquery/hive-partitioning-samples/customlayout/{pkey:STRING}/";
        createTableExternalHivePartitioned(datasetName, tableName, sourceUriPrefix, sourceUri);
      }
    
      public static void createTableExternalHivePartitioned(
          String datasetName, String tableName, String sourceUriPrefix, String sourceUri) {
        try {
          // Initialize client that will be used to send requests. This client only needs to be created
          // once, and can be reused for multiple requests.
          [BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html) bigquery = [BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html).getDefaultInstance().getService();
    
          // Configuring partitioning options
          [HivePartitioningOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.HivePartitioningOptions.html) hivePartitioningOptions =
              [HivePartitioningOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.HivePartitioningOptions.html).newBuilder()
                  .setMode("CUSTOM")
                  .setRequirePartitionFilter(true)
                  .[setSourceUriPrefix](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.HivePartitioningOptions.Builder.html#com_google_cloud_bigquery_HivePartitioningOptions_Builder_setSourceUriPrefix_java_lang_String_)(sourceUriPrefix)
                  .build();
    
          [TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId.html) tableId = [TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId.html).of(datasetName, tableName);
          [ExternalTableDefinition](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.ExternalTableDefinition.html) customTable =
              [ExternalTableDefinition](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.ExternalTableDefinition.html).newBuilder(sourceUri, [FormatOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.FormatOptions.html).[parquet](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.FormatOptions.html#com_google_cloud_bigquery_FormatOptions_parquet__)())
                  .setAutodetect(true)
                  .setHivePartitioningOptions(hivePartitioningOptions)
                  .build();
          bigquery.[create](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html#com_google_cloud_bigquery_BigQuery_create_com_google_cloud_bigquery_DatasetInfo_com_google_cloud_bigquery_BigQuery_DatasetOption____)(TableInfo.of(tableId, customTable));
          System.out.println("External table created using hivepartitioningoptions");
        } catch ([BigQueryException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html) e) {
          System.out.println("External table was not created" + e.toString());
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    # Demonstrates creating an external table with hive partitioning.
    
    # TODO(developer): Set table_id to the ID of the table to create.
    table_id = "your-project.your_dataset.your_table_name"
    
    # TODO(developer): Set source uri.
    # Example file:
    # gs://cloud-samples-data/bigquery/hive-partitioning-samples/autolayout/dt=2020-11-15/file1.parquet
    uri = "gs://cloud-samples-data/bigquery/hive-partitioning-samples/autolayout/*"
    
    # TODO(developer): Set source uri prefix.
    source_uri_prefix = (
        "gs://cloud-samples-data/bigquery/hive-partitioning-samples/autolayout/"
    )
    
    from google.cloud import [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest)
    
    # Construct a BigQuery client object.
    client = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html)()
    
    # Configure the external data source.
    external_config = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[ExternalConfig](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.external_config.ExternalConfig.html)("PARQUET")
    [external_config](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.external_config.html).source_uris = [uri]
    [external_config](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.external_config.html).autodetect = True
    
    # Configure partitioning options.
    hive_partitioning_opts = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[HivePartitioningOptions](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.external_config.HivePartitioningOptions.html)()
    
    # The layout of the files in here is compatible with the layout requirements for hive partitioning,
    # so we can add an optional Hive partitioning configuration to leverage the object paths for deriving
    # partitioning column information.
    
    # For more information on how partitions are extracted, see:
    # https://cloud.google.com/bigquery/docs/hive-partitioned-queries-gcs
    
    # We have a "/dt=YYYY-MM-DD/" path component in our example files as documented above.
    # Autolayout will expose this as a column named "dt" of type DATE.
    hive_partitioning_opts.mode = "AUTO"
    hive_partitioning_opts.require_partition_filter = True
    hive_partitioning_opts.[source_uri_prefix](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.external_config.HivePartitioningOptions.html#google_cloud_bigquery_external_config_HivePartitioningOptions_source_uri_prefix) = source_uri_prefix
    
    [external_config](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.external_config.html).hive_partitioning = hive_partitioning_opts
    
    table = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[Table](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.table.Table.html)(table_id)
    table.[external_data_configuration](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.table.Table.html#google_cloud_bigquery_table_Table_external_data_configuration) = external_config
    
    table = client.[create_table](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_create_table)(table)  # Make an API request.
    print(
        "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
    )

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
