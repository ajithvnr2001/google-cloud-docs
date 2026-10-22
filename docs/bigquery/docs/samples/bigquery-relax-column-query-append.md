---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-relax-column-query-append/
title: Relax a column in a query append job \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:08.876320+00:00
---

# Relax a column in a query append job  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-relax-column-query-append/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Relax a column in a query append job Stay organized with collections  Save and categorize content based on your preferences. 

Change a column from required to nullable in a query append job.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Modifying table schemas](https://docs.cloud.google.com/bigquery/docs/managing-table-schemas)



## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Go API reference documentation](https://godoc.org/cloud.google.com/go/bigquery). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import (
    	"context"
    	"fmt"
    
    	"cloud.google.com/go/bigquery"
    )
    
    // relaxTableQuery demonstrates relaxing the schema of a table by appending query results to
    // enable the table to allow NULL values.
    func relaxTableQuery(projectID, datasetID, tableID string) error {
    	// projectID := "my-project-id"
    	// datasetID := "mydataset"
    	// tableID := "mytable"
    	ctx := context.Background()
    	client, err := bigquery.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("bigquery.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	sampleSchema := bigquery.[Schema](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_Schema){
    		{Name: "full_name", Type: bigquery.[StringFieldType](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_StringFieldType_BytesFieldType_IntegerFieldType_FloatFieldType_BooleanFieldType_TimestampFieldType_RecordFieldType_DateFieldType_TimeFieldType_DateTimeFieldType_NumericFieldType_GeographyFieldType_BigNumericFieldType_IntervalFieldType_JSONFieldType_RangeFieldType), Required: true},
    		{Name: "age", Type: bigquery.[IntegerFieldType](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_StringFieldType_BytesFieldType_IntegerFieldType_FloatFieldType_BooleanFieldType_TimestampFieldType_RecordFieldType_DateFieldType_TimeFieldType_DateTimeFieldType_NumericFieldType_GeographyFieldType_BigNumericFieldType_IntervalFieldType_JSONFieldType_RangeFieldType), Required: true},
    	}
    	meta := &bigquery.[TableMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_TableMetadata){
    		Schema: sampleSchema,
    	}
    	tableRef := client.Dataset(datasetID).Table(tableID)
    	if err := tableRef.Create(ctx, meta); err != nil {
    		return err
    	}
    	// Now, append a query result that includes nulls, but allow the job to relax
    	// all required columns.
    	q := client.Query("SELECT \"Beyonce\" as full_name")
    	q.[QueryConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_QueryConfig).Dst = client.Dataset(datasetID).Table(tableID)
    	q.SchemaUpdateOptions = []string{"ALLOW_FIELD_RELAXATION"}
    	q.WriteDisposition = bigquery.[WriteAppend](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_WriteAppend_WriteTruncate_WriteTruncateData_WriteEmpty)
    	q.[Location](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_Job_Location) = "US"
    	job, err := q.Run(ctx)
    	if err != nil {
    		return err
    	}
    	_, err = job.Wait(ctx)
    	if err != nil {
    		return err
    	}
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import com.google.cloud.bigquery.[BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html);
    import com.google.cloud.bigquery.[BigQueryException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html);
    import com.google.cloud.bigquery.[BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html);
    import com.google.cloud.bigquery.[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Job.html);
    import com.google.cloud.bigquery.[JobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobInfo.html);
    import com.google.cloud.bigquery.[JobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobInfo.html).[SchemaUpdateOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobInfo.SchemaUpdateOption.html);
    import com.google.cloud.bigquery.[JobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobInfo.html).[WriteDisposition](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobInfo.WriteDisposition.html);
    import com.google.cloud.bigquery.[QueryJobConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration.html);
    import com.google.cloud.bigquery.[TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId.html);
    import com.google.cloud.bigquery.[TableResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableResult.html);
    import com.google.common.collect.ImmutableList;
    
    public class RelaxTableQuery {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "MY_PROJECT_ID";
        String datasetName = "MY_DATASET_NAME";
        String tableName = "MY_TABLE_NAME";
        relaxTableQuery(projectId, datasetName, tableName);
      }
    
      // To relax all columns in a destination table when you append data to it during a query job
      public static void relaxTableQuery(String projectId, String datasetName, String tableName)
          throws Exception {
        try {
          // Initialize client that will be used to send requests. This client only needs to be created
          // once, and can be reused for multiple requests.
          BigQuery bigquery = BigQueryOptions.getDefaultInstance().getService();
    
          TableId tableId = TableId.of(datasetName, tableName);
    
          String sourceTable = "`" + projectId + "." + datasetName + "." + tableName + "`";
          String query = "SELECT word FROM " + sourceTable + " WHERE word like '%is%'";
    
          QueryJobConfiguration queryConfig =
              QueryJobConfiguration.newBuilder(query)
                  // Use standard SQL syntax for queries.
                  // See: https://cloud.google.com/bigquery/sql-reference/
                  .setUseLegacySql(false)
                  .setSchemaUpdateOptions(ImmutableList.of(SchemaUpdateOption.ALLOW_FIELD_RELAXATION))
                  .setWriteDisposition(WriteDisposition.WRITE_APPEND)
                  .setDestinationTable(tableId)
                  .build();
    
          Job queryJob = bigquery.create(JobInfo.newBuilder(queryConfig).build());
    
          queryJob = queryJob.waitFor();
    
          // Check for errors
          if (queryJob == null) {
            throw new Exception("Job no longer exists");
          } else if (queryJob.getStatus().getError() != null) {
            // You can also look at queryJob.getStatus().getExecutionErrors() for all
            // errors, not just the latest one.
            throw new Exception(queryJob.getStatus().getError().toString());
          }
    
          // Get the results.
          TableResult results = queryJob.getQueryResults();
    
          // Print all pages of the results.
          results
              .iterateAll()
              .forEach(
                  rows -> {
                    rows.forEach(row -> System.out.println("row: " + row.toString()));
                  });
    
          System.out.println("Successfully relaxed all columns in destination table during query job");
        } catch ([BigQueryException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html) | InterruptedException e) {
          System.out.println("Columns not relaxed during query job \n" + e.toString());
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    from google.cloud import [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest)
    
    # Construct a BigQuery client object.
    client = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html)()
    
    # TODO(developer): Set table_id to the ID of the destination table.
    # table_id = "your-project.your_dataset.your_table_name"
    
    # Retrieves the destination table and checks the number of required fields.
    table = client.[get_table](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_get_table)(table_id)  # Make an API request.
    original_required_fields = sum(field.mode == "REQUIRED" for field in table.schema)
    
    # In this example, the existing table has 2 required fields.
    print("{} fields in the schema are required.".format(original_required_fields))
    
    # Configures the query to append the results to a destination table,
    # allowing field relaxation.
    job_config = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[QueryJobConfig](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.job.QueryJobConfig.html)(
        destination=table_id,
        schema_update_options=[[bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[SchemaUpdateOption](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.enums.SchemaUpdateOption.html).[ALLOW_FIELD_RELAXATION](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.enums.SchemaUpdateOption.html#google_cloud_bigquery_enums_SchemaUpdateOption_ALLOW_FIELD_RELAXATION)],
        write_disposition=[bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[WriteDisposition](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.enums.WriteDisposition.html).[WRITE_APPEND](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.enums.WriteDisposition.html#google_cloud_bigquery_enums_WriteDisposition_WRITE_APPEND),
    )
    
    # Start the query, passing in the extra configuration.
    client.[query_and_wait](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_query_and_wait)(
        # In this example, the existing table contains 'full_name' and 'age' as
        # required columns, but the query results will omit the second column.
        'SELECT "Beyonce" as full_name;',
        job_config=job_config,
    )  # Make an API request and wait for job to complete
    
    # Checks the updated number of required fields.
    table = client.[get_table](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_get_table)(table_id)  # Make an API request.
    current_required_fields = sum(field.mode == "REQUIRED" for field in table.schema)
    print("{} fields in the schema are now required.".format(current_required_fields))

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
