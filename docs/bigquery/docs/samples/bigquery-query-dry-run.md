---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-query-dry-run/
title: Dry run query \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:49.047407+00:00
---

# Dry run query  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-query-dry-run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Dry run query Stay organized with collections  Save and categorize content based on your preferences. 

Run a dry run query.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Estimate and control costs](https://docs.cloud.google.com/bigquery/docs/best-practices-costs)
  * [Run a query](https://docs.cloud.google.com/bigquery/docs/running-queries)



## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Go API reference documentation](https://godoc.org/cloud.google.com/go/bigquery). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/bigquery"
    )
    
    // queryDryRun demonstrates issuing a dry run query to validate query structure and
    // provide an estimate of the bytes scanned.
    func queryDryRun(w io.Writer, projectID string) error {
    	// projectID := "my-project-id"
    	ctx := context.Background()
    	client, err := bigquery.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("bigquery.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	q := client.Query(`
    	SELECT
    		name,
    		COUNT(*) as name_count
    	FROM ` + "`bigquery-public-data.usa_names.usa_1910_2013`" + `
    	WHERE state = 'WA'
    	GROUP BY name`)
    	q.DryRun = true
    	// Location must match that of the dataset(s) referenced in the query.
    	q.[Location](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_Job_Location) = "US"
    
    	job, err := q.Run(ctx)
    	if err != nil {
    		return err
    	}
    	// Dry run is not asynchronous, so get the latest status and statistics.
    	status := job.[LastStatus](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_Job_LastStatus)()
    	if err := status.[Err](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_JobStatus_Err)(); err != nil {
    		return err
    	}
    	fmt.Fprintf(w, "This query will process %d bytes\n", status.[Statistics](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_Statistics).TotalBytesProcessed)
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
    import com.google.cloud.bigquery.[JobStatistics](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobStatistics.html);
    import com.google.cloud.bigquery.[QueryJobConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration.html);
    
    // Sample to run dry query on the table
    public class QueryDryRun {
    
      public static void main(String[] args) {
        String query =
            "SELECT name, COUNT(*) as name_count "
                + "FROM `bigquery-public-data.usa_names.usa_1910_2013` "
                + "WHERE state = 'WA' "
                + "GROUP BY name";
        queryDryRun(query);
      }
    
      public static void queryDryRun(String query) {
        try {
          // Initialize client that will be used to send requests. This client only needs to be created
          // once, and can be reused for multiple requests.
          [BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html) bigquery = [BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html).getDefaultInstance().getService();
    
          [QueryJobConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration.html) queryConfig =
              [QueryJobConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration.html).newBuilder(query).[setDryRun](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration.Builder.html#com_google_cloud_bigquery_QueryJobConfiguration_Builder_setDryRun_java_lang_Boolean_)(true).setUseQueryCache(false).build();
    
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Job.html) job = bigquery.[create](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html#com_google_cloud_bigquery_BigQuery_create_com_google_cloud_bigquery_DatasetInfo_com_google_cloud_bigquery_BigQuery_DatasetOption____)(JobInfo.of(queryConfig));
          [JobStatistics](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobStatistics.html).[QueryStatistics](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobStatistics.QueryStatistics.html) statistics = job.getStatistics();
    
          System.out.println(
              "Query dry run performed successfully." + statistics.getTotalBytesProcessed());
        } catch ([BigQueryException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html) e) {
          System.out.println("Query not performed \n" + e.toString());
        }
      }
    }

### PHP

Before trying this sample, follow the PHP setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery PHP API reference documentation](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/BigQueryClient). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    use Google\Cloud\BigQuery\BigQueryClient;
    
    /**
     * Dry runs the given query
     *
     * @param string $projectId The project Id of your Google Cloud Project.
     * @param string $query The query to be run. For eg: $query = 'SELECT id, view_count FROM `bigquery-public-data.stackoverflow.posts_questions`'
     */
    function dry_run_query(string $projectId, string $query): void
    {
        // Construct a BigQuery client object.
        $bigQuery = new BigQueryClient([
          'projectId' => $projectId,
        ]);
    
        // Set job configs
        $jobConfig = $bigQuery->query($query);
        $jobConfig->useQueryCache(false);
        $jobConfig->dryRun(true);
    
        // Extract query results
        $queryJob = $bigQuery->startJob($jobConfig);
        $info = $queryJob->info();
    
        printf('This query will process %s bytes' . PHP_EOL, $info['statistics']['totalBytesProcessed']);
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    from google.cloud import [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest)
    
    # Construct a BigQuery client object.
    client = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html)()
    
    job_config = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[QueryJobConfig](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.job.QueryJobConfig.html)(dry_run=True, use_query_cache=False)
    
    # Start the query, passing in the extra configuration.
    query_job = client.[query](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html)(
        (
            "SELECT name, COUNT(*) as name_count "
            "FROM `bigquery-public-data.usa_names.usa_1910_2013` "
            "WHERE state = 'WA' "
            "GROUP BY name"
        ),
        job_config=job_config,
    )  # Make an API request.
    
    # A dry run query completes immediately.
    print("This query will process {} bytes.".format([query_job](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dbapi.Cursor.html#google_cloud_bigquery_dbapi_Cursor_query_job).total_bytes_processed))

### Rust
    
    
    use google_cloud_bigquery::client::BigQuery;
    
    pub async fn sample(project_id: &str) -> anyhow::Result<()> {
        let client = BigQuery::builder().build().await?;
    
        let query = client
            .query(
                "SELECT \
            name FROM `bigquery-public-data.usa_names.usa_1910_2013` \
            WHERE state = 'TX' \
            LIMIT 100",
            )
            .with_project_id(project_id)
            .set_dry_run(true)
            .set_location("US")
            .send()
            .await?;
    
        let bytes = query.metadata().total_bytes_processed.unwrap_or(0);
        println!("This query will process {bytes} bytes.");
    
        let stats = query.metadata().statistics.as_ref();
        println!("Job Statistics: {stats:?}");
    
        Ok(())
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
