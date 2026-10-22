---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-query-script/
title: Query script \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:33.057455+00:00
---

# Query script  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-query-script/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Query script Stay organized with collections  Save and categorize content based on your preferences. 

Run a query script.

## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import com.google.api.gax.paging.[Page](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html);
    import com.google.cloud.bigquery.[BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html);
    import com.google.cloud.bigquery.[BigQueryException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html);
    import com.google.cloud.bigquery.[BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html);
    import com.google.cloud.bigquery.[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Job.html);
    import com.google.cloud.bigquery.[JobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobInfo.html);
    import com.google.cloud.bigquery.[QueryJobConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration.html);
    
    // Sample to run query script.
    public class QueryScript {
    
      public static void main(String[] args) {
        String script =
            "-- Declare a variable to hold names as an array.\n"
                + "DECLARE top_names ARRAY<STRING>;\n"
                + "-- Build an array of the top 100 names from the year 2017.\n"
                + "SET top_names = (\n"
                + "  SELECT ARRAY_AGG(name ORDER BY number DESC LIMIT 100)\n"
                + "  FROM `bigquery-public-data`.usa_names.usa_1910_current\n"
                + "  WHERE year = 2017\n"
                + ");\n"
                + "-- Which names appear as words in Shakespeare's plays?\n"
                + "SELECT\n"
                + "  name AS shakespeare_name\n"
                + "FROM UNNEST(top_names) AS name\n"
                + "WHERE name IN (\n"
                + "  SELECT word\n"
                + "  FROM `bigquery-public-data`.samples.shakespeare\n"
                + ");";
        queryScript(script);
      }
    
      public static void queryScript(String script) {
        try {
          // Initialize client that will be used to send requests. This client only needs to be created
          // once, and can be reused for multiple requests.
          [BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html) bigquery = [BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html).getDefaultInstance().getService();
    
          [QueryJobConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration.html) queryConfig = [QueryJobConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration.html).newBuilder(script).build();
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Job.html) createJob = bigquery.[create](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html#com_google_cloud_bigquery_BigQuery_create_com_google_cloud_bigquery_DatasetInfo_com_google_cloud_bigquery_BigQuery_DatasetOption____)(JobInfo.of(queryConfig));
          // Wait for the whole script to finish.
          [JobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobInfo.html) jobInfo = createJob.[waitFor](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Job.html#com_google_cloud_bigquery_Job_waitFor_com_google_cloud_bigquery_BigQueryRetryConfig_com_google_cloud_RetryOption____)();
          String parentJobId = jobInfo.[getJobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobInfo.html#com_google_cloud_bigquery_JobInfo_getJobId__)().getJob();
    
          // Fetch jobs created by the SQL script.
          Page<Job> childJobs = bigquery.[listJobs](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html#com_google_cloud_bigquery_BigQuery_listJobs_com_google_cloud_bigquery_BigQuery_JobListOption____)(BigQuery.JobListOption.parentJobId(parentJobId));
          childJobs
              .iterateAll()
              .forEach(job -> System.out.printf("Child Job Id: ", job.getJobId().getJob()));
    
          System.out.println("Query script performed successfully.");
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
    
    # Run a SQL script.
    sql_script = """
    -- Declare a variable to hold names as an array.
    DECLARE top_names ARRAY<STRING>;
    
    -- Build an array of the top 100 names from the year 2017.
    SET top_names = (
    SELECT ARRAY_AGG(name ORDER BY number DESC LIMIT 100)
    FROM `bigquery-public-data.usa_names.usa_1910_2013`
    WHERE year = 2000
    );
    
    -- Which names appear as words in Shakespeare's plays?
    SELECT
    name AS shakespeare_name
    FROM UNNEST(top_names) AS name
    WHERE name IN (
    SELECT word
    FROM `bigquery-public-data.samples.shakespeare`
    );
    """
    parent_job = client.[query](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html)(sql_script)
    
    # Wait for the whole script to finish.
    rows_iterable = parent_job.result()
    print("Script created {} child jobs.".format(parent_job.num_child_jobs))
    
    # Fetch result rows for the final sub-job in the script.
    rows = list(rows_iterable)
    print(
        "{} of the top 100 names from year 2000 also appear in Shakespeare's works.".format(
            len(rows)
        )
    )
    
    # Fetch jobs created by the SQL script.
    child_jobs_iterable = client.[list_jobs](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_list_jobs)(parent_job=parent_job)
    for child_job in child_jobs_iterable:
        child_rows = list(child_job.result())
        print(
            "Child job with ID {} produced {} row(s).".format(
                child_job.job_id, len(child_rows)
            )
        )
    

### Rust
    
    
    use google_cloud_bigquery::client::BigQuery;
    
    pub async fn sample(project_id: &str) -> anyhow::Result<()> {
        let client = BigQuery::builder().build().await?;
    
        let mut rows = client
            .query(
                r#"
    DECLARE target_state STRING DEFAULT 'TX';
    SELECT name FROM `bigquery-public-data.usa_names.usa_1910_2013`
    WHERE state = target_state
    LIMIT 10;
    "#,
            )
            .with_project_id(project_id)
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
