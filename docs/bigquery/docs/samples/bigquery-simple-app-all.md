---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-simple-app-all/
title: Query with the BigQuery API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:32.406877+00:00
---

# Query with the BigQuery API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-simple-app-all/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Query with the BigQuery API Stay organized with collections  Save and categorize content based on your preferences. 

Create a simple app with BigQuery.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [BigQuery API Client Libraries](https://docs.cloud.google.com/bigquery/docs/reference/libraries)
  * [Get started with authentication](https://docs.cloud.google.com/bigquery/docs/authentication/getting-started)
  * [Query a public dataset with the BigQuery client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries)



## Code sample

### C#

Before trying this sample, follow the C# setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    using System;
    using [Google.Cloud.BigQuery.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.html);
    
    namespace GoogleCloudSamples
    {
        public class Program
        {
            public static void Main(string[] args)
            {
                string projectId = Environment.GetEnvironmentVariable("GOOGLE_PROJECT_ID");
                var client = [BigQueryClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient.html#Google_Cloud_BigQuery_V2_BigQueryClient_Create_System_String_Google_Apis_Auth_OAuth2_GoogleCredential_)(projectId);
                string query = @"SELECT
                    CONCAT(
                        'https://stackoverflow.com/questions/',
                        CAST(id as STRING)) as url, view_count
                    FROM `bigquery-public-data.stackoverflow.posts_questions`
                    WHERE tags like '%google-bigquery%'
                    ORDER BY view_count DESC
                    LIMIT 10";
                var result = client.[ExecuteQuery](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient.html#Google_Cloud_BigQuery_V2_BigQueryClient_ExecuteQuery_System_String_System_Collections_Generic_IEnumerable_Google_Cloud_BigQuery_V2_BigQueryParameter__Google_Cloud_BigQuery_V2_QueryOptions_Google_Cloud_BigQuery_V2_GetQueryResultsOptions_)(query, parameters: null);
                Console.Write("\nQuery Results:\n------------\n");
                foreach (var row in result)
                {
                    Console.WriteLine($"{row["url"]}: {row["view_count"]} views");
                }
            }
        }
    }
    

### Go

Before trying this sample, follow the Go setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Go API reference documentation](https://godoc.org/cloud.google.com/go/bigquery). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    // Command simpleapp queries the Stack Overflow public dataset in Google BigQuery.
    package main
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"log"
    	"os"
    
    	"cloud.google.com/go/bigquery"
    	"google.golang.org/api/iterator"
    )
    
    
    func main() {
    	projectID := os.Getenv("GOOGLE_CLOUD_PROJECT")
    	if projectID == "" {
    		fmt.Println("GOOGLE_CLOUD_PROJECT environment variable must be set.")
    		os.Exit(1)
    	}
    
    	ctx := context.Background()
    
    	client, err := bigquery.NewClient(ctx, projectID)
    	if err != nil {
    		log.Fatalf("bigquery.NewClient: %v", err)
    	}
    	defer client.Close()
    
    	rows, err := query(ctx, client)
    	if err != nil {
    		log.Fatal(err)
    	}
    	if err := printResults(os.Stdout, rows); err != nil {
    		log.Fatal(err)
    	}
    }
    
    // query returns a row iterator suitable for reading query results.
    func query(ctx context.Context, client *bigquery.Client) (*bigquery.[RowIterator](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_RowIterator), error) {
    
    	query := client.Query(
    		`SELECT
    			CONCAT(
    				'https://stackoverflow.com/questions/',
    				CAST(id as STRING)) as url,
    			view_count
    		FROM ` + "`bigquery-public-data.stackoverflow.posts_questions`" + `
    		WHERE tags like '%google-bigquery%'
    		ORDER BY view_count DESC
    		LIMIT 10;`)
    	return query.Read(ctx)
    }
    
    type StackOverflowRow struct {
    	URL       string `bigquery:"url"`
    	ViewCount int64  `bigquery:"view_count"`
    }
    
    // printResults prints results from a query to the Stack Overflow public dataset.
    func printResults(w io.Writer, iter *bigquery.[RowIterator](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_RowIterator)) error {
    	for {
    		var row StackOverflowRow
    		err := iter.Next(&row)
    		if err == iterator.Done {
    			return nil
    		}
    		if err != nil {
    			return fmt.Errorf("error iterating through results: %w", err)
    		}
    
    		fmt.Fprintf(w, "url: %s views: %d\n", row.URL, row.ViewCount)
    	}
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import com.google.cloud.bigquery.[BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html);
    import com.google.cloud.bigquery.[BigQueryException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html);
    import com.google.cloud.bigquery.[BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html);
    import com.google.cloud.bigquery.[FieldValueList](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.FieldValueList.html);
    import com.google.cloud.bigquery.[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Job.html);
    import com.google.cloud.bigquery.[JobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobId.html);
    import com.google.cloud.bigquery.[JobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobInfo.html);
    import com.google.cloud.bigquery.[QueryJobConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration.html);
    import com.google.cloud.bigquery.[TableResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableResult.html);
    
    
    public class SimpleApp {
    
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the app.
        String projectId = "MY_PROJECT_ID";
        simpleApp(projectId);
      }
    
      public static void simpleApp(String projectId) {
        try {
          [BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html) bigquery = [BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html).getDefaultInstance().getService();
          [QueryJobConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration.html) queryConfig =
              [QueryJobConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration.html).newBuilder(
                      "SELECT CONCAT('https://stackoverflow.com/questions/', "
                          + "CAST(id as STRING)) as url, view_count "
                          + "FROM `bigquery-public-data.stackoverflow.posts_questions` "
                          + "WHERE tags like '%google-bigquery%' "
                          + "ORDER BY view_count DESC "
                          + "LIMIT 10")
                  // Use standard SQL syntax for queries.
                  // See: https://cloud.google.com/bigquery/sql-reference/
                  .setUseLegacySql(false)
                  .build();
    
          [JobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobId.html) jobId = [JobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobId.html).newBuilder().setProject(projectId).build();
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Job.html) queryJob = bigquery.[create](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html#com_google_cloud_bigquery_BigQuery_create_com_google_cloud_bigquery_DatasetInfo_com_google_cloud_bigquery_BigQuery_DatasetOption____)(JobInfo.newBuilder(queryConfig).setJobId(jobId).build());
    
          // Wait for the query to complete.
          queryJob = queryJob.[waitFor](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Job.html#com_google_cloud_bigquery_Job_waitFor_com_google_cloud_bigquery_BigQueryRetryConfig_com_google_cloud_RetryOption____)();
    
          // Check for errors
          if (queryJob == null) {
            throw new RuntimeException("Job no longer exists");
          } else if (queryJob.getStatus().[getExecutionErrors](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobStatus.html#com_google_cloud_bigquery_JobStatus_getExecutionErrors__)() != null
              && queryJob.getStatus().getExecutionErrors().size() > 0) {
            // TODO(developer): Handle errors here. An error here do not necessarily mean that the job
            // has completed or was unsuccessful.
            // For more details: https://cloud.google.com/bigquery/troubleshooting-errors
            throw new RuntimeException("An unhandled error has occurred");
          }
    
          // Get the results.
          [TableResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableResult.html) result = queryJob.[getQueryResults](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Job.html#com_google_cloud_bigquery_Job_getQueryResults_com_google_cloud_bigquery_BigQuery_QueryResultsOption____)();
    
          // Print all pages of the results.
          for ([FieldValueList](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.FieldValueList.html) row : result.[iterateAll](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableResult.html#com_google_cloud_bigquery_TableResult_iterateAll__)()) {
            // String type
            String url = row.get("url").getStringValue();
            String viewCount = row.get("view_count").getStringValue();
            System.out.printf("%s : %s views\n", url, viewCount);
          }
        } catch ([BigQueryException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html) | InterruptedException e) {
          System.out.println("Simple App failed due to error: \n" + e.toString());
        }
      }
    }

### PHP

Before trying this sample, follow the PHP setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery PHP API reference documentation](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/BigQueryClient). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    <?php
    # ...
    
    require __DIR__ . '/vendor/autoload.php';
    
    use Google\Cloud\BigQuery\BigQueryClient;
    
    
    $bigQuery = new BigQueryClient();
    $query = <<<ENDSQL
    SELECT
      CONCAT(
        'https://stackoverflow.com/questions/',
        CAST(id as STRING)) as url,
      view_count
    FROM `bigquery-public-data.stackoverflow.posts_questions`
    WHERE tags like '%google-bigquery%'
    ORDER BY view_count DESC
    LIMIT 10;
    ENDSQL;
    $queryJobConfig = $bigQuery->query($query);
    $queryResults = $bigQuery->runQuery($queryJobConfig);
    
    if ($queryResults->isComplete()) {
        $i = 0;
        $rows = $queryResults->rows();
        foreach ($rows as $row) {
            printf('--- Row %s ---' . PHP_EOL, ++$i);
            printf('url: %s, %s views' . PHP_EOL, $row['url'], $row['view_count']);
        }
        printf('Found %s row(s)' . PHP_EOL, $i);
    } else {
        throw new Exception('The query failed to complete');
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    from google.cloud import [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest)
    
    
    
    def query_stackoverflow() -> None:
        client = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html)()
        results = client.[query_and_wait](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_query_and_wait)(
            """
            SELECT
              CONCAT(
                'https://stackoverflow.com/questions/',
                CAST(id as STRING)) as url,
              view_count
            FROM `bigquery-public-data.stackoverflow.posts_questions`
            WHERE tags like '%google-bigquery%'
            ORDER BY view_count DESC
            LIMIT 10"""
        )  # Waits for job to complete.
    
        for row in results:
            print("{} : {} views".format(row.url, row.view_count))
    
    
    if __name__ == "__main__":
        query_stackoverflow()

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-bigquery/latest/Google/Cloud/Bigquery.html). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    require "google/cloud/bigquery"
    
    # This uses Application Default Credentials to authenticate.
    # @see https://cloud.google.com/bigquery/docs/authentication/getting-started
    bigquery = Google::Cloud::[Bigquery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-data_policies-v1beta1/latest/Google-Cloud-Bigquery.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery/latest/Google-Cloud-Bigquery.html)
    
    sql     = "SELECT " \
              "CONCAT('https://stackoverflow.com/questions/', CAST(id as STRING)) as url, view_count " \
              "FROM `bigquery-public-data.stackoverflow.posts_questions` " \
              "WHERE tags like '%google-bigquery%' " \
              "ORDER BY view_count DESC LIMIT 10"
    results = bigquery.query sql
    
    results.each do |row|
      puts "#{[row](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery/latest/Google-Cloud-Bigquery-InsertResponse-InsertError.html)[:url]}: #{[row](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery/latest/Google-Cloud-Bigquery-InsertResponse-InsertError.html)[:view_count]} views"
    end

### Rust
    
    
    use google_cloud_bigquery::client::BigQuery;
    use google_cloud_bigquery::query::FromRow;
    
    pub async fn sample(project_id: &str) -> anyhow::Result<()> {
        let client = BigQuery::builder().build().await?;
    
        let query = r#"
    SELECT
        CONCAT('https://stackoverflow.com/questions/', CAST(id as STRING)) as url,
        view_count
    FROM `bigquery-public-data.stackoverflow.posts_questions`
    WHERE tags like '%google-bigquery%'
    ORDER BY view_count DESC
    LIMIT 10;
    "#;
        let mut rows = client
            .query(query)
            .with_project_id(project_id)
            .until_done()
            .await?
            .read();
    
        #[derive(FromRow, Debug)]
        struct StackOverflowRow {
            url: String,
            view_count: i64,
        }
    
        while let Some(row) = rows.next().await.transpose()? {
            let row: StackOverflowRow = row.try_into()?;
            println!("url: {} views: {}", row.url, row.view_count);
        }
    
        Ok(())
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
