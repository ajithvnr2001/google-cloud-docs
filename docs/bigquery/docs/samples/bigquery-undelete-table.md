---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-undelete-table/
title: Undelete \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:59:31.224832+00:00
---

# Undelete  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-undelete-table/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Undelete Stay organized with collections  Save and categorize content based on your preferences. 

Undelete a table.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Access historical data](https://docs.cloud.google.com/bigquery/docs/access-historical-data)
  * [Restore deleted tables](https://docs.cloud.google.com/bigquery/docs/restore-deleted-tables)



## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Go API reference documentation](https://godoc.org/cloud.google.com/go/bigquery). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import (
    	"context"
    	"fmt"
    	"time"
    
    	"cloud.google.com/go/bigquery"
    )
    
    // deleteAndUndeleteTable demonstrates how to recover a deleted table by copying it from a point in time
    // that predates the deletion event.
    func deleteAndUndeleteTable(projectID, datasetID, tableID string) error {
    	// projectID := "my-project-id"
    	// datasetID := "mydataset"
    	// tableID := "mytable"
    	ctx := context.Background()
    	client, err := bigquery.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("bigquery.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ds := client.Dataset(datasetID)
    	if _, err := ds.Table(tableID).Metadata(ctx); err != nil {
    		return err
    	}
    	// Record the current time.  We'll use this as the snapshot time
    	// for recovering the table.
    	snapTime := time.Now()
    
    	// "Accidentally" delete the table.
    	if err := client.Dataset(datasetID).Table(tableID).Delete(ctx); err != nil {
    		return err
    	}
    
    	// Construct the restore-from tableID using a snapshot decorator.
    	snapshotTableID := fmt.Sprintf("%s@%d", tableID, snapTime.UnixNano()/1e6)
    	// Choose a new table ID for the recovered table data.
    	recoverTableID := fmt.Sprintf("%s_recovered", tableID)
    
    	// Construct and run a copy job.
    	copier := ds.Table(recoverTableID).[CopierFrom](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_Table_CopierFrom)(ds.Table(snapshotTableID))
    	copier.WriteDisposition = bigquery.[WriteTruncate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_WriteAppend_WriteTruncate_WriteTruncateData_WriteEmpty)
    	job, err := copier.Run(ctx)
    	if err != nil {
    		return err
    	}
    	status, err := job.Wait(ctx)
    	if err != nil {
    		return err
    	}
    	if err := status.[Err](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_JobStatus_Err)(); err != nil {
    		return err
    	}
    
    	ds.Table(recoverTableID).Delete(ctx)
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import com.google.cloud.bigquery.[BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html);
    import com.google.cloud.bigquery.[BigQueryException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html);
    import com.google.cloud.bigquery.[BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html);
    import com.google.cloud.bigquery.[CopyJobConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.CopyJobConfiguration.html);
    import com.google.cloud.bigquery.[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Job.html);
    import com.google.cloud.bigquery.[JobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobInfo.html);
    import com.google.cloud.bigquery.[Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1.Table.html);
    import com.google.cloud.bigquery.[TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId.html);
    import org.threeten.bp.Instant;
    
    // Sample to undeleting a table
    public class UndeleteTable {
    
      public static void main(String[] args) {
        // TODO(developer): Replace these variables before running the sample.
        String datasetName = "MY_DATASET_NAME";
        String tableName = "MY_TABLE_TABLE";
        String recoverTableName = "MY_RECOVER_TABLE_TABLE";
        undeleteTable(datasetName, tableName, recoverTableName);
      }
    
      public static void undeleteTable(String datasetName, String tableName, String recoverTableName) {
        try {
          // Initialize client that will be used to send requests. This client only needs to be created
          // once, and can be reused for multiple requests.
          [BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html) bigquery = [BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html).getDefaultInstance().getService();
    
          // Record the current time.  We'll use this as the snapshot time
          // for recovering the table.
          long snapshotEpoch = Instant.now().toEpochMilli();
    
          // ...
    
          // "Accidentally" delete the table.
          bigquery.[delete](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html#com_google_cloud_bigquery_BigQuery_delete_com_google_cloud_bigquery_DatasetId_com_google_cloud_bigquery_BigQuery_DatasetDeleteOption____)(TableId.of(datasetName, tableName));
    
          // Construct the restore-from tableID using a snapshot decorator.
          String snapshotTableId = String.format("%s@%d", tableName, snapshotEpoch);
    
          // Construct and run a copy job.
          [CopyJobConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.CopyJobConfiguration.html) configuration =
              [CopyJobConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.CopyJobConfiguration.html).newBuilder(
                      // Choose a new table ID for the recovered table data.
                      [TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId.html).of(datasetName, recoverTableName),
                      [TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId.html).of(datasetName, snapshotTableId))
                  .build();
    
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Job.html) job = bigquery.[create](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html#com_google_cloud_bigquery_BigQuery_create_com_google_cloud_bigquery_DatasetInfo_com_google_cloud_bigquery_BigQuery_DatasetOption____)(JobInfo.of(configuration));
          job = job.[waitFor](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Job.html#com_google_cloud_bigquery_Job_waitFor_com_google_cloud_bigquery_BigQueryRetryConfig_com_google_cloud_RetryOption____)();
          if (job.[isDone](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Job.html#com_google_cloud_bigquery_Job_isDone__)() && job.getStatus().getError() == null) {
            System.out.println("Undelete table recovered successfully.");
          } else {
            System.out.println(
                "BigQuery was unable to copy the table due to an error: \n"
                    + job.getStatus().getError());
            return;
          }
        } catch ([BigQueryException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html) | InterruptedException e) {
          System.out.println("Table not found. \n" + e.toString());
        }
      }
    }

### PHP

Before trying this sample, follow the PHP setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery PHP API reference documentation](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/BigQueryClient). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    use Google\Cloud\BigQuery\BigQueryClient;
    
    /**
     * Restore a deleted table from its snapshot.
     *
     * @param string $projectId The project Id of your Google Cloud Project.
     * @param string $datasetId The BigQuery dataset ID.
     * @param string $tableId Table ID of the table to delete.
     * @param string $restoredTableId Table Id for the restored table.
     */
    function undelete_table(
        string $projectId,
        string $datasetId,
        string $tableId,
        string $restoredTableId
    ): void {
        $bigQuery = new BigQueryClient(['projectId' => $projectId]);
        $dataset = $bigQuery->dataset($datasetId);
    
        // Choose an appropriate snapshot point as epoch milliseconds.
        // For this example, we choose the current time as we're about to delete the
        // table immediately afterwards
        $snapshotEpoch = date_create()->format('Uv');
    
        // Delete the table.
        $dataset->table($tableId)->delete();
    
        // Construct the restore-from table ID using a snapshot decorator.
        $snapshotId = "{$tableId}@{$snapshotEpoch}";
    
        // Restore the deleted table
        $restoredTable = $dataset->table($restoredTableId);
        $copyConfig = $dataset->table($snapshotId)->copy($restoredTable);
        $job = $bigQuery->runJob($copyConfig);
    
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
            print('Snapshot restored successfully' . PHP_EOL);
        }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import time
    
    from google.cloud import [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest)
    
    # Construct a BigQuery client object.
    client = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html)()
    
    # TODO(developer): Choose a table to recover.
    # table_id = "your-project.your_dataset.your_table"
    
    # TODO(developer): Choose a new table ID for the recovered table data.
    # recovered_table_id = "your-project.your_dataset.your_table_recovered"
    
    # TODO(developer): Choose an appropriate snapshot point as epoch
    # milliseconds. For this example, we choose the current time as we're about
    # to delete the table immediately afterwards.
    snapshot_epoch = int(time.time() * 1000)
    
    # ...
    
    # "Accidentally" delete the table.
    client.[delete_table](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_delete_table)(table_id)  # Make an API request.
    
    # Construct the restore-from table ID using a snapshot decorator.
    snapshot_table_id = "{}@{}".format(table_id, snapshot_epoch)
    
    # Construct and run a copy job.
    job = client.[copy_table](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_copy_table)(
        snapshot_table_id,
        recovered_table_id,
        # Must match the source and destination tables location.
        location="US",
    )  # Make an API request.
    
    [job](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.job.html).result()  # Wait for the job to complete.
    
    print(
        "Copied data from deleted table {} to {}".format(table_id, recovered_table_id)
    )

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
