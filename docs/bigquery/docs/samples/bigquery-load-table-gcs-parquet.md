---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-load-table-gcs-parquet/
title: Load a Parquet file \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:06:43.999071+00:00
---

# Load a Parquet file  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-load-table-gcs-parquet/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Load a Parquet file Stay organized with collections  Save and categorize content based on your preferences. 

Load a Parquet file from Cloud Storage into a new table.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Load Parquet data from Cloud Storage](https://docs.cloud.google.com/bigquery/docs/loading-data-cloud-storage-parquet)



## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Go API reference documentation](https://godoc.org/cloud.google.com/go/bigquery). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import (
    	"context"
    	"fmt"
    
    	"cloud.google.com/go/bigquery"
    )
    
    // importParquet demonstrates loading Apache Parquet data from Cloud Storage into a table.
    func importParquet(projectID, datasetID, tableID string) error {
    	// projectID := "my-project-id"
    	// datasetID := "mydataset"
    	// tableID := "mytable"
    	ctx := context.Background()
    	client, err := bigquery.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("bigquery.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	gcsRef := bigquery.[NewGCSReference](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_GCSReference_NewGCSReference)("gs://cloud-samples-data/bigquery/us-states/us-states.parquet")
    	gcsRef.SourceFormat = bigquery.[Parquet](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_CSV_Avro_JSON_DatastoreBackup_GoogleSheets_Bigtable_Parquet_ORC_TFSavedModel_XGBoostBooster_Iceberg)
    	gcsRef.AutoDetect = true
    	loader := client.Dataset(datasetID).Table(tableID).[LoaderFrom](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_Table_LoaderFrom)(gcsRef)
    
    	job, err := loader.Run(ctx)
    	if err != nil {
    		return err
    	}
    	status, err := job.Wait(ctx)
    	if err != nil {
    		return err
    	}
    
    	if status.[Err](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_JobStatus_Err)() != nil {
    		return fmt.Errorf("job completed with error: %w", status.[Err](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_JobStatus_Err)())
    	}
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import com.google.cloud.bigquery.[BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html);
    import com.google.cloud.bigquery.[BigQueryException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html);
    import com.google.cloud.bigquery.[BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html);
    import com.google.cloud.bigquery.[FormatOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.FormatOptions.html);
    import com.google.cloud.bigquery.[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Job.html);
    import com.google.cloud.bigquery.[JobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobInfo.html);
    import com.google.cloud.bigquery.[LoadJobConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.LoadJobConfiguration.html);
    import com.google.cloud.bigquery.[TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId.html);
    import java.math.BigInteger;
    
    public class LoadParquet {
    
      public static void main(String[] args) {
        // TODO(developer): Replace these variables before running the sample.
        String datasetName = "MY_DATASET_NAME";
        String sourceUri = "gs://cloud-samples-data/bigquery/us-states/us-states.parquet";
        String tableName = "us_states";
        loadParquet(datasetName, tableName, sourceUri);
      }
    
      public static void loadParquet(String datasetName, String tableName, String sourceUri) {
        try {
          // Initialize client that will be used to send requests. This client only needs to be created
          // once, and can be reused for multiple requests.
          [BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html) bigquery = [BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html).getDefaultInstance().getService();
    
          [TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId.html) tableId = [TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId.html).of(datasetName, tableName);
    
          [LoadJobConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.LoadJobConfiguration.html) configuration =
              [LoadJobConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.LoadJobConfiguration.html).builder(tableId, sourceUri)
                  .setFormatOptions([FormatOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.FormatOptions.html).[parquet](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.FormatOptions.html#com_google_cloud_bigquery_FormatOptions_parquet__)())
                  .build();
    
          // For more information on Job see:
          // https://googleapis.dev/java/google-cloud-clients/latest/index.html?com/google/cloud/bigquery/package-summary.html
          // Load the table
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Job.html) job = bigquery.[create](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html#com_google_cloud_bigquery_BigQuery_create_com_google_cloud_bigquery_DatasetInfo_com_google_cloud_bigquery_BigQuery_DatasetOption____)(JobInfo.of(configuration));
    
          // Blocks until this load table job completes its execution, either failing or succeeding.
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Job.html) completedJob = job.[waitFor](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Job.html#com_google_cloud_bigquery_Job_waitFor_com_google_cloud_bigquery_BigQueryRetryConfig_com_google_cloud_RetryOption____)();
          if (completedJob == null) {
            System.out.println("Job not executed since it no longer exists.");
            return;
          } else if (completedJob.getStatus().getError() != null) {
            System.out.println(
                "BigQuery was unable to load the table due to an error: \n"
                    + job.getStatus().getError());
            return;
          }
    
          // Check number of rows loaded into the table
          BigInteger numRows = bigquery.[getTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html#com_google_cloud_bigquery_BigQuery_getTable_com_google_cloud_bigquery_TableId_com_google_cloud_bigquery_BigQuery_TableOption____)(tableId).getNumRows();
          System.out.printf("Loaded %d rows. \n", numRows);
    
          System.out.println("GCS parquet loaded successfully.");
        } catch ([BigQueryException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html) | InterruptedException e) {
          System.out.println("GCS Parquet was not loaded. \n" + e.toString());
        }
      }
    }

### PHP

Before trying this sample, follow the PHP setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery PHP API reference documentation](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/BigQueryClient). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    use Google\Cloud\BigQuery\BigQueryClient;
    
    /**
     * Import data from storage parquet.
     *
     * @param string $projectId The project Id of your Google Cloud Project.
     * @param string $datasetId The BigQuery dataset ID.
     * @param string $tableId The BigQuery table ID.
     */
    function import_from_storage_parquet(
        string $projectId,
        string $datasetId,
        string $tableId = 'us_states'
    ): void {
        // instantiate the bigquery table service
        $bigQuery = new BigQueryClient([
          'projectId' => $projectId,
        ]);
        $dataset = $bigQuery->dataset($datasetId);
        $table = $dataset->table($tableId);
    
        // create the import job
        $gcsUri = 'gs://cloud-samples-data/bigquery/us-states/us-states.parquet';
        $loadConfig = $table->loadFromStorage($gcsUri)->sourceFormat('PARQUET');
        $job = $table->runJob($loadConfig);
    
        // check if the job is complete
        $job->reload();
        if (!$job->isComplete()) {
            throw new \Exception('Job has not yet completed', 500);
        }
        // check if the job has errors
        if (isset($job->info()['status']['errorResult'])) {
            $error = $job->info()['status']['errorResult']['message'];
            printf('Error running job: %s' . PHP_EOL, $error);
        } else {
            print('Data imported successfully' . PHP_EOL);
        }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    from google.cloud import [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest)
    
    # Construct a BigQuery client object.
    client = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html)()
    
    # TODO(developer): Set table_id to the ID of the table to create.
    # table_id = "your-project.your_dataset.your_table_name"
    
    job_config = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[LoadJobConfig](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.job.LoadJobConfig.html)(
        source_format=[bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[SourceFormat](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.enums.SourceFormat.html).PARQUET,
    )
    uri = "gs://cloud-samples-data/bigquery/us-states/us-states.parquet"
    
    load_job = client.[load_table_from_uri](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_load_table_from_uri)(
        uri, table_id, job_config=job_config
    )  # Make an API request.
    
    load_job.result()  # Waits for the job to complete.
    
    destination_table = client.[get_table](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_get_table)(table_id)
    print("Loaded {} rows.".format(destination_table.[num_rows](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.table.Table.html#google_cloud_bigquery_table_Table_num_rows)))

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
