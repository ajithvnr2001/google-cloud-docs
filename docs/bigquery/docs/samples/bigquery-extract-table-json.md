---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-extract-table-json/
title: Export a table to a JSON file \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:27.680133+00:00
---

# Export a table to a JSON file  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-extract-table-json/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Export a table to a JSON file Stay organized with collections  Save and categorize content based on your preferences. 

Exports a table to a newline-delimited JSON file in a Cloud Storage bucket.

## Code sample

### C#

Before trying this sample, follow the C# setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    using [Google.Cloud.BigQuery.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.html);
    using System;
    
    public class BigQueryExtractTableJson
    {
        public void ExtractTableJson(
            string projectId = "your-project-id",
            string bucketName = "your-bucket-name")
        {
            [BigQueryClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient.html) client = [BigQueryClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient.html#Google_Cloud_BigQuery_V2_BigQueryClient_Create_System_String_Google_Apis_Auth_OAuth2_GoogleCredential_)(projectId);
            string destinationUri = $"gs://{bucketName}/shakespeare.json";
            var jobOptions = new [CreateExtractJobOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.CreateExtractJobOptions.html)()
            {
                DestinationFormat = [FileFormat](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.FileFormat.html).[NewlineDelimitedJson](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.FileFormat.html#Google_Cloud_BigQuery_V2_FileFormat_NewlineDelimitedJson)
            };
            [BigQueryJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryJob.html) job = client.[CreateExtractJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient.html#Google_Cloud_BigQuery_V2_BigQueryClient_CreateExtractJob_Google_Apis_Bigquery_v2_Data_TableReference_System_Collections_Generic_IEnumerable_System_String__Google_Cloud_BigQuery_V2_CreateExtractJobOptions_)(
                projectId: "bigquery-public-data",
                datasetId: "samples",
                tableId: "shakespeare",
                destinationUri: destinationUri,
                options: jobOptions
            );
            job = job.[PollUntilCompleted](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryJob.html#Google_Cloud_BigQuery_V2_BigQueryJob_PollUntilCompleted_Google_Cloud_BigQuery_V2_GetJobOptions_Google_Api_Gax_PollSettings_)().ThrowOnAnyError();  // Waits for the job to complete.
            Console.Write($"Exported table to {destinationUri}.");
        }
    }

### Go

Before trying this sample, follow the Go setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Go API reference documentation](https://godoc.org/cloud.google.com/go/bigquery). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import (
    	"context"
    	"fmt"
    
    	"cloud.google.com/go/bigquery"
    )
    
    // exportTableAsJSON demonstrates using an export job to
    // write the contents of a table into Cloud Storage as newline delimited JSON.
    func exportTableAsJSON(projectID, gcsURI string) error {
    	// projectID := "my-project-id"
    	// gcsURI := "gs://mybucket/shakespeare.json"
    	ctx := context.Background()
    	client, err := bigquery.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("bigquery.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	srcProject := "bigquery-public-data"
    	srcDataset := "samples"
    	srcTable := "shakespeare"
    
    	gcsRef := bigquery.[NewGCSReference](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_GCSReference_NewGCSReference)(gcsURI)
    	gcsRef.DestinationFormat = bigquery.[JSON](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_CSV_Avro_JSON_DatastoreBackup_GoogleSheets_Bigtable_Parquet_ORC_TFSavedModel_XGBoostBooster_Iceberg)
    
    	extractor := client.[DatasetInProject](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_Client_DatasetInProject)(srcProject, srcDataset).Table(srcTable).ExtractorTo(gcsRef)
    	// You can choose to run the job in a specific location for more complex data locality scenarios.
    	// Ex: In this example, source dataset and GCS bucket are in the US.
    	extractor.[Location](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_Job_Location) = "US"
    
    	job, err := extractor.Run(ctx)
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
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import com.google.cloud.[RetryOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.RetryOption.html);
    import com.google.cloud.bigquery.[BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html);
    import com.google.cloud.bigquery.[BigQueryException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html);
    import com.google.cloud.bigquery.[BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html);
    import com.google.cloud.bigquery.[FormatOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.FormatOptions.html);
    import com.google.cloud.bigquery.[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html);
    import com.google.cloud.bigquery.[Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1.Table.html);
    import com.google.cloud.bigquery.[TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId.html);
    import org.threeten.bp.[Duration](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Duration.html);
    
    public class ExtractTableToJson {
    
      public static void main([String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html)[] args) {
        // TODO(developer): Replace these variables before running the sample.
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) projectId = "bigquery-public-data";
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) datasetName = "samples";
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) tableName = "shakespeare";
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) bucketName = "my-bucket";
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) destinationUri = "gs://" + bucketName + "/path/to/file";
        // For more information on export formats available see:
        // https://cloud.google.com/bigquery/docs/exporting-data#export_formats_and_compression_types
        // For more information on Job see:
        // https://googleapis.dev/java/google-cloud-clients/latest/index.html?com/google/cloud/bigquery/package-summary.html
    
        // Note that FormatOptions.json().toString() is not "JSON" but "NEWLINE_DELIMITED_JSON"
        // Using FormatOptions Enum for this will prevent problems with unexpected format names.
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) dataFormat = [FormatOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.FormatOptions.html).json().getType();
    
        extractTableToJson(projectId, datasetName, tableName, destinationUri, dataFormat);
      }
    
      // Exports datasetName:tableName to destinationUri as a JSON file
      public static void extractTableToJson(
          [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) projectId,
          [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) datasetName,
          [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) tableName,
          [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) destinationUri,
          [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) dataFormat) {
        try {
          // Initialize client that will be used to send requests. This client only needs to be created
          // once, and can be reused for multiple requests.
          [BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html) bigquery = [BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html).getDefaultInstance().getService();
    
          [TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId.html) tableId = [TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId.html).of(projectId, datasetName, tableName);
          [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.bigquery.biglake.v1.Table.html) table = bigquery.[getTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html#com_google_cloud_bigquery_BigQuery_getTable_com_google_cloud_bigquery_TableId_com_google_cloud_bigquery_BigQuery_TableOption____)(tableId);
    
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html) job = table.[extract](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Table.html#com_google_cloud_bigquery_Table_extract_java_lang_String_java_lang_String_com_google_cloud_bigquery_BigQuery_JobOption____)(dataFormat, destinationUri);
    
          // Blocks until this job completes its execution, either failing or succeeding.
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html) completedJob =
              job.[waitFor](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Job.html#com_google_cloud_bigquery_Job_waitFor_com_google_cloud_bigquery_BigQueryRetryConfig_com_google_cloud_RetryOption____)(
                  RetryOption.initialRetryDelay(Duration.ofSeconds(1)),
                  RetryOption.totalTimeout(Duration.ofMinutes(3)));
          if (completedJob == null) {
            System.out.println("Job not executed since it no longer exists.");
            return;
          } else if (completedJob.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html#com_google_cloud_batch_v1_Job_getStatus__)().getError() != null) {
            System.out.println(
                "BigQuery was unable to extract due to an error: \n" + job.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.html#com_google_cloud_batch_v1_Job_getStatus__)().getError());
            return;
          }
          System.out.println(
              "Table export successful. Check in GCS bucket for the " + dataFormat + " file.");
        } catch ([BigQueryException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html) | InterruptedException e) {
          System.out.println("Table extraction job was interrupted. \n" + e.toString());
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import bigframes.pandas as bpd
    from google.cloud import [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest)
    
    # Set partial ordering mode for BigQuery DataFrames.
    bpd.[options](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.external_config.ExternalConfig.html#google_cloud_bigquery_external_config_ExternalConfig_options).[bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).ordering_mode = "partial"
    
    
    def extract_table_json_bigframes(bucket_name: str = "my-bucket") -> None:
        """Exports a BigQuery table to Cloud Storage in newline-delimited JSON format using BigQuery DataFrames."""
        project = "bigquery-public-data"
        dataset_id = "samples"
        table_id = "shakespeare"
        destination_uri = f"gs://{bucket_name}/shakespeare-*.json"
    
        full_table_id = f"{project}.{dataset_id}.{table_id}"
        df = bpd.read_gbq(full_table_id)
        df.to_json(destination_uri, orient="records", lines=True)
        print(f"Exported {full_table_id} to {destination_uri} using BigQuery DataFrames.")
    
    
    def extract_table_json_client(bucket_name: str = "my-bucket") -> None:
        """Exports a BigQuery table to Cloud Storage in newline-delimited JSON format using google-cloud-bigquery."""
        project = "bigquery-public-data"
        dataset_id = "samples"
        table_id = "shakespeare"
        destination_uri = f"gs://{bucket_name}/shakespeare-*.json"
    
        client = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html)()
        dataset_ref = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[DatasetReference](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dataset.DatasetReference.html)(project, dataset_id)
        table_ref = dataset_ref.[table](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dataset.DatasetReference.html#google_cloud_bigquery_dataset_DatasetReference_table)(table_id)
        job_config = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[job](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.job.html).[ExtractJobConfig](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.job.ExtractJobConfig.html)()
        job_config.destination_format = (
            [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[job](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.job.html).[DestinationFormat](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.enums.DestinationFormat.html).NEWLINE_DELIMITED_JSON
        )
    
        extract_job = client.[extract_table](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_extract_table)(
            table_ref,
            destination_uri,
            job_config=job_config,
            # Location must match that of the source table.
            location="US",
        )  # API request
        extract_job.result()  # Waits for job to complete.
    
        print(
            f"Exported {project}:{dataset_id}.{table_id} to {destination_uri} using client library."
        )
    
    
    # [Preferred] Run using BigQuery DataFrames:
    # extract_table_json_bigframes("my-bucket")
    
    # Alternatively, run using google-cloud-bigquery client library:
    # extract_table_json_client("my-bucket")

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
