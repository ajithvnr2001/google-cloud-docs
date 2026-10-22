---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-add-column-query-append/
title: Add a column using a query job \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:13.747420+00:00
---

# Add a column using a query job  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-add-column-query-append/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Add a column using a query job Stay organized with collections  Save and categorize content based on your preferences. 

Add a new column to a BigQuery table while appending rows using a query job with an explicit destination table.

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
    
    // createTableAndWidenQuery demonstrates how the schema of a table can be modified to add columns by appending
    // query results that include the new columns.
    func createTableAndWidenQuery(projectID, datasetID, tableID string) error {
    	// projectID := "my-project-id"
    	// datasetID := "mydataset"
    	// tableID := "mytable"
    	ctx := context.Background()
    	client, err := bigquery.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("bigquery.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	// First, we create a sample table.
    	sampleSchema := bigquery.[Schema](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_Schema){
    		{Name: "full_name", Type: bigquery.[StringFieldType](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_StringFieldType_BytesFieldType_IntegerFieldType_FloatFieldType_BooleanFieldType_TimestampFieldType_RecordFieldType_DateFieldType_TimeFieldType_DateTimeFieldType_NumericFieldType_GeographyFieldType_BigNumericFieldType_IntervalFieldType_JSONFieldType_RangeFieldType), Required: true},
    		{Name: "age", Type: bigquery.[IntegerFieldType](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_StringFieldType_BytesFieldType_IntegerFieldType_FloatFieldType_BooleanFieldType_TimestampFieldType_RecordFieldType_DateFieldType_TimeFieldType_DateTimeFieldType_NumericFieldType_GeographyFieldType_BigNumericFieldType_IntervalFieldType_JSONFieldType_RangeFieldType), Required: true},
    	}
    	original := &bigquery.[TableMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_TableMetadata){
    		Schema: sampleSchema,
    	}
    	tableRef := client.Dataset(datasetID).Table(tableID)
    	if err := tableRef.Create(ctx, original); err != nil {
    		return err
    	}
    	// Our table has two columns.  We'll introduce a new favorite_color column via
    	// a subsequent query that appends to the table.
    	q := client.Query("SELECT \"Timmy\" as full_name, 85 as age, \"Blue\" as favorite_color")
    	q.SchemaUpdateOptions = []string{"ALLOW_FIELD_ADDITION"}
    	q.[QueryConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_QueryConfig).Dst = client.Dataset(datasetID).Table(tableID)
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
    

### PHP

Before trying this sample, follow the PHP setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery PHP API reference documentation](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/BigQueryClient). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    use Google\Cloud\BigQuery\BigQueryClient;
    
    /**
     * Append a column using a query job.
     *
     * @param string $projectId The project Id of your Google Cloud Project.
     * @param string $datasetId The BigQuery dataset ID.
     * @param string $tableId The BigQuery table ID.
     */
    function add_column_query_append(
        string $projectId,
        string $datasetId,
        string $tableId
    ): void {
        $bigQuery = new BigQueryClient([
          'projectId' => $projectId,
        ]);
        $dataset = $bigQuery->dataset($datasetId);
        $table = $dataset->table($tableId);
    
        // In this example, the existing table contains only the 'Name' and 'Title'.
        // A new column 'Description' gets added after the query job.
    
        // Define query
        $query = sprintf('SELECT "John" as name, "Unknown" as title, "Dummy person" as description;');
    
        // Set job configs
        $queryJobConfig = $bigQuery->query($query);
        $queryJobConfig->destinationTable($table);
        $queryJobConfig->schemaUpdateOptions(['ALLOW_FIELD_ADDITION']);
        $queryJobConfig->writeDisposition('WRITE_APPEND');
    
        // Run query with query job configuration
        $bigQuery->runQuery($queryJobConfig);
    
        // Print all the columns
        $columns = $table->info()['schema']['fields'];
        printf('The columns in the table are ');
        foreach ($columns as $column) {
            printf('%s ', $column['name']);
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
    
    # Retrieves the destination table and checks the length of the schema.
    table = client.[get_table](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_get_table)(table_id)  # Make an API request.
    print("Table {} contains {} columns".format(table_id, len(table.schema)))
    
    # Configures the query to append the results to a destination table,
    # allowing field addition.
    job_config = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[QueryJobConfig](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.job.QueryJobConfig.html)(
        destination=table_id,
        schema_update_options=[[bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[SchemaUpdateOption](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.enums.SchemaUpdateOption.html).[ALLOW_FIELD_ADDITION](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.enums.SchemaUpdateOption.html#google_cloud_bigquery_enums_SchemaUpdateOption_ALLOW_FIELD_ADDITION)],
        write_disposition=[bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[WriteDisposition](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.enums.WriteDisposition.html).[WRITE_APPEND](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.enums.WriteDisposition.html#google_cloud_bigquery_enums_WriteDisposition_WRITE_APPEND),
    )
    
    # Start the query, passing in the extra configuration.
    client.[query_and_wait](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_query_and_wait)(
        # In this example, the existing table contains only the 'full_name' and
        # 'age' columns, while the results of this query will contain an
        # additional 'favorite_color' column.
        'SELECT "Timmy" as full_name, 85 as age, "Blue" as favorite_color;',
        job_config=job_config,
    )  # Make an API request and wait for job to complete.
    
    # Checks the updated length of the schema.
    table = client.[get_table](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_get_table)(table_id)  # Make an API request.
    print("Table {} now contains {} columns".format(table_id, len(table.schema)))

### Rust
    
    
    use google_cloud_bigquery::client::BigQuery;
    use google_cloud_bigquery_v2::model::TableReference;
    
    pub async fn sample(project_id: &str, dataset_id: &str, table_id: &str) -> anyhow::Result<()> {
        let client = BigQuery::builder().build().await?;
    
        // Query parameters cannot be used as substitutes for identifiers, column names or table
        // names. Ensure resource identifiers are validated before formatting into SQL statements
        // to prevent SQL injection.
        validate_resource_names(project_id, dataset_id, table_id)?;
    
        // First, initialize the destination table with a single column
        let create_sql = format!(
            "CREATE OR REPLACE TABLE `{project_id}.{dataset_id}.{table_id}` \
             (name STRING) AS \
             SELECT 'Alice' AS name;"
        );
        client
            .query(create_sql)
            .with_project_id(project_id)
            .set_location("US")
            .until_done()
            .await?;
    
        // Append rows using a query job that introduces a new column (`age`),
        // automatically updating the destination table schema.
        let append_sql = "SELECT 'Bob' AS name, 30 AS age;";
        let res = client
            .query(append_sql)
            .with_project_id(project_id)
            .set_destination_table(
                TableReference::new()
                    .set_project_id(project_id)
                    .set_dataset_id(dataset_id)
                    .set_table_id(table_id),
            )
            .set_write_disposition("WRITE_APPEND")
            .set_schema_update_options(["ALLOW_FIELD_ADDITION"])
            .set_location("US")
            .until_done()
            .await?;
    
        println!("Appended rows with new column successfully: {:?}", res);
        Ok(())
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
