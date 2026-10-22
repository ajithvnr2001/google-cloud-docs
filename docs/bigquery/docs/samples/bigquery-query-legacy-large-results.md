---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-query-legacy-large-results/
title: Enable large results \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:11.577209+00:00
---

# Enable large results  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-query-legacy-large-results/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Enable large results Stay organized with collections  Save and categorize content based on your preferences. 

Query enables large result sets using legacy SQL.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Write query results](https://docs.cloud.google.com/bigquery/docs/writing-results)



## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Go API reference documentation](https://godoc.org/cloud.google.com/go/bigquery). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/bigquery"
    	"google.golang.org/api/iterator"
    )
    
    // queryLegacyLargeResults demonstrates issuing a legacy SQL query and writing a large result set
    // into a destination table.
    func queryLegacyLargeResults(w io.Writer, projectID, datasetID, tableID string) error {
    	// projectID := "my-project-id"
    	// datasetID := "destinationdataset"
    	// tableID := "destinationtable"
    	ctx := context.Background()
    	client, err := bigquery.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("bigquery.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	q := client.Query(
    		"SELECT corpus FROM [bigquery-public-data:samples.shakespeare] GROUP BY corpus;")
    	q.UseLegacySQL = true
    	q.AllowLargeResults = true
    	q.[QueryConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_QueryConfig).Dst = client.Dataset(datasetID).Table(tableID)
    	// Run the query and process the returned row iterator.
    	it, err := q.Read(ctx)
    	if err != nil {
    		return fmt.Errorf("query.Read(): %w", err)
    	}
    	for {
    		var row []bigquery.[Value](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_Value)
    		err := it.Next(&row)
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return err
    		}
    		fmt.Fprintln(w, row)
    	}
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import com.google.cloud.bigquery.[BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html);
    import com.google.cloud.bigquery.[BigQueryException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html);
    import com.google.cloud.bigquery.[BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html);
    import com.google.cloud.bigquery.[QueryJobConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration.html);
    import com.google.cloud.bigquery.[TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId.html);
    import com.google.cloud.bigquery.[TableResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableResult.html);
    
    // Sample to run query with large results and save the results to a table.
    public class QueryLargeResults {
    
      public static void main(String[] args) {
        // TODO(developer): Replace these variables before running the sample.
        String destinationDataset = "MY_DESTINATION_DATASET_NAME";
        String destinationTable = "MY_DESTINATION_TABLE_NAME";
        String query = "SELECT corpus FROM [bigquery-public-data:samples.shakespeare] GROUP BY corpus;";
        queryLargeResults(destinationDataset, destinationTable, query);
      }
    
      public static void queryLargeResults(
          String destinationDataset, String destinationTable, String query) {
        try {
          // Initialize client that will be used to send requests. This client only needs to be created
          // once, and can be reused for multiple requests.
          [BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html) bigquery = [BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html).getDefaultInstance().getService();
    
          [QueryJobConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration.html) queryConfig =
              // To use legacy SQL syntax, set useLegacySql to true.
              [QueryJobConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration.html).newBuilder(query)
                  .setUseLegacySql(true)
                  // Save the results of the query to a permanent table.
                  .setDestinationTable([TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId.html).of(destinationDataset, destinationTable))
                  // Allow results larger than the maximum response size.
                  // If true, a destination table must be set.
                  .setAllowLargeResults(true)
                  .build();
    
          [TableResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableResult.html) results = bigquery.[query](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html#com_google_cloud_bigquery_BigQuery_query_com_google_cloud_bigquery_QueryJobConfiguration_com_google_cloud_bigquery_BigQuery_JobOption____)(queryConfig);
    
          results
              .[iterateAll](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableResult.html#com_google_cloud_bigquery_TableResult_iterateAll__)()
              .forEach(row -> row.forEach(val -> System.out.printf("%s,", val.toString())));
    
          System.out.println("Query large results performed successfully.");
        } catch ([BigQueryException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html) | InterruptedException e) {
          System.out.println("Query not performed \n" + e.toString());
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
    
    # Set the destination table and use_legacy_sql to True to use
    # legacy SQL syntax.
    job_config = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[QueryJobConfig](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.job.QueryJobConfig.html)(
        allow_large_results=True, destination=table_id, use_legacy_sql=True
    )
    
    sql = """
        SELECT corpus
        FROM [bigquery-public-data:samples.shakespeare]
        GROUP BY corpus;
    """
    
    # Start the query, passing in the extra configuration.
    client.[query_and_wait](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_query_and_wait)(
        sql, job_config=job_config
    )  # Make an API request and wait for the query to finish.
    
    print("Query results loaded to the table {}".format(table_id))

### Rust
    
    
    use google_cloud_bigquery::client::BigQuery;
    use google_cloud_bigquery_v2::model::TableReference;
    
    pub async fn sample(project_id: &str, dataset_id: &str, table_id: &str) -> anyhow::Result<()> {
        let client = BigQuery::builder().build().await?;
    
        let destination = TableReference::new()
            .set_project_id(project_id)
            .set_dataset_id(dataset_id)
            .set_table_id(table_id);
    
        let mut rows = client
            .query(
                "SELECT \
            name FROM [bigquery-public-data:usa_names.usa_1910_2013] \
            WHERE state = 'TX' \
            LIMIT 100",
            )
            .with_project_id(project_id)
            .set_use_legacy_sql(true)
            .set_allow_large_results(true)
            .set_destination_table(destination)
            .set_location("US")
            .until_done()
            .await?
            .read();
    
        while let Some(row) = rows.next().await.transpose()? {
            let name: String = row.get("name")?;
            println!("Name: {name}");
        }
        Ok(())
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
