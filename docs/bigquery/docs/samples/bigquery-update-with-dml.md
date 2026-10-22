---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-update-with-dml/
title: Update table with DML \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:31.442659+00:00
---

# Update table with DML  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-update-with-dml/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Update table with DML Stay organized with collections  Save and categorize content based on your preferences. 

Update data in a BigQuery table using a DML query.

## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import com.google.cloud.bigquery.[BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html);
    import com.google.cloud.bigquery.[BigQueryException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html);
    import com.google.cloud.bigquery.[BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html);
    import com.google.cloud.bigquery.[FormatOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.FormatOptions.html);
    import com.google.cloud.bigquery.[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Job.html);
    import com.google.cloud.bigquery.[JobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobId.html);
    import com.google.cloud.bigquery.[QueryJobConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration.html);
    import com.google.cloud.bigquery.[TableDataWriteChannel](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableDataWriteChannel.html);
    import com.google.cloud.bigquery.[TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId.html);
    import com.google.cloud.bigquery.[TableResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableResult.html);
    import com.google.cloud.bigquery.[WriteChannelConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.WriteChannelConfiguration.html);
    import java.io.IOException;
    import java.io.OutputStream;
    import java.nio.channels.Channels;
    import java.nio.file.FileSystems;
    import java.nio.file.Files;
    import java.nio.file.Path;
    import java.util.UUID;
    
    // Sample to update data in BigQuery tables using DML query
    public class UpdateTableDml {
    
      public static void main(String[] args) throws IOException, InterruptedException {
        // TODO(developer): Replace these variables before running the sample.
        String datasetName = "MY_DATASET_NAME";
        String tableName = "MY_TABLE_NAME";
        updateTableDml(datasetName, tableName);
      }
    
      public static void updateTableDml(String datasetName, String tableName)
          throws IOException, InterruptedException {
        try {
          // Initialize client that will be used to send requests. This client only needs to be created
          // once, and can be reused for multiple requests.
          [BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html) bigquery = [BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html).getDefaultInstance().getService();
    
          // Load JSON file into UserSessions table
          [TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId.html) tableId = [TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId.html).of(datasetName, tableName);
    
          [WriteChannelConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.WriteChannelConfiguration.html) writeChannelConfiguration =
              [WriteChannelConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.WriteChannelConfiguration.html).newBuilder(tableId)
                  .setFormatOptions([FormatOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.FormatOptions.html).json())
                  .build();
    
          // Imports a local JSON file into a table.
          Path jsonPath =
              FileSystems.getDefault().getPath("src/test/resources", "userSessionsData.json");
    
          // The location and JobName must be specified; other fields can be auto-detected.
          String jobName = "jobId_" + UUID.randomUUID().toString();
          [JobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobId.html) jobId = [JobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.JobId.html).newBuilder().setLocation("us").setJob(jobName).build();
    
          try ([TableDataWriteChannel](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableDataWriteChannel.html) writer = bigquery.[writer](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html#com_google_cloud_bigquery_BigQuery_writer_com_google_cloud_bigquery_JobId_com_google_cloud_bigquery_WriteChannelConfiguration_)(jobId, writeChannelConfiguration);
              OutputStream stream = Channels.newOutputStream(writer)) {
            Files.[copy](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Table.html#com_google_cloud_bigquery_Table_copy_com_google_cloud_bigquery_TableId_com_google_cloud_bigquery_BigQuery_JobOption____)(jsonPath, stream);
          }
    
          // Get the Job created by the TableDataWriteChannel and wait for it to complete.
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Job.html) job = bigquery.[getJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html#com_google_cloud_bigquery_BigQuery_getJob_com_google_cloud_bigquery_JobId_com_google_cloud_bigquery_BigQuery_JobOption____)(jobId);
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Job.html) completedJob = job.[waitFor](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Job.html#com_google_cloud_bigquery_Job_waitFor_com_google_cloud_bigquery_BigQueryRetryConfig_com_google_cloud_RetryOption____)();
          if (completedJob == null) {
            System.out.println("Job not executed since it no longer exists.");
            return;
          } else if (completedJob.getStatus().getError() != null) {
            System.out.println(
                "BigQuery was unable to load local file to the table due to an error: \n"
                    + job.getStatus().getError());
            return;
          }
    
          System.out.println(
              job.getStatistics().toString() + " userSessionsData json uploaded successfully");
    
          // Write a DML query to modify UserSessions table
          // To create DML query job to mask the last octet in every row's ip_address column
          String dmlQuery =
              String.format(
                  "UPDATE `%s.%s` \n"
                      + "SET ip_address = REGEXP_REPLACE(ip_address, r\"(\\.[0-9]+)$\", \".0\")\n"
                      + "WHERE TRUE",
                  datasetName, tableName);
    
          [QueryJobConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration.html) dmlQueryConfig = [QueryJobConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration.html).newBuilder(dmlQuery).build();
    
          // Execute the query.
          [TableResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableResult.html) result = bigquery.[query](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html#com_google_cloud_bigquery_BigQuery_query_com_google_cloud_bigquery_QueryJobConfiguration_com_google_cloud_bigquery_BigQuery_JobOption____)(dmlQueryConfig);
    
          // Print the results.
          result.[iterateAll](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableResult.html#com_google_cloud_bigquery_TableResult_iterateAll__)().forEach(rows -> rows.forEach(row -> System.out.println(row.getValue())));
    
          System.out.println("Table updated successfully using DML");
        } catch ([BigQueryException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html) e) {
          System.out.println("Table update failed \n" + e.toString());
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import pathlib
    from typing import Dict, Optional
    
    from google.cloud import [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest)
    from google.cloud.bigquery import [enums](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.enums.html)
    
    
    def load_from_newline_delimited_json(
        client: [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html),
        filepath: pathlib.Path,
        project_id: str,
        dataset_id: str,
        table_id: str,
    ) -> None:
        full_table_id = f"{project_id}.{dataset_id}.{table_id}"
        job_config = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[LoadJobConfig](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.job.LoadJobConfig.html)()
        job_config.source_format = [enums](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.enums.html).[SourceFormat](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.enums.SourceFormat.html).NEWLINE_DELIMITED_JSON
        job_config.schema = [
            [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[SchemaField](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.schema.SchemaField.html)("id", [enums](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.enums.html).[SqlTypeNames](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.enums.SqlTypeNames.html).[STRING](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.enums.DecimalTargetType.html#google_cloud_bigquery_enums_DecimalTargetType_STRING)),
            [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[SchemaField](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.schema.SchemaField.html)("user_id", [enums](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.enums.html).[SqlTypeNames](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.enums.SqlTypeNames.html).INTEGER),
            [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[SchemaField](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.schema.SchemaField.html)("login_time", [enums](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.enums.html).[SqlTypeNames](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.enums.SqlTypeNames.html).TIMESTAMP),
            [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[SchemaField](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.schema.SchemaField.html)("logout_time", [enums](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.enums.html).[SqlTypeNames](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.enums.SqlTypeNames.html).TIMESTAMP),
            [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[SchemaField](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.schema.SchemaField.html)("ip_address", [enums](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.enums.html).[SqlTypeNames](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.enums.SqlTypeNames.html).[STRING](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.enums.DecimalTargetType.html#google_cloud_bigquery_enums_DecimalTargetType_STRING)),
        ]
    
        with open(filepath, "rb") as json_file:
            load_job = client.[load_table_from_file](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_load_table_from_file)(
                json_file, full_table_id, job_config=job_config
            )
    
        # Wait for load job to finish.
        load_job.result()
    
    
    def update_with_dml(
        client: [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html), project_id: str, dataset_id: str, table_id: str
    ) -> int:
        query_text = f"""
        UPDATE `{project_id}.{dataset_id}.{table_id}`
        SET ip_address = REGEXP_REPLACE(ip_address, r"(\\.[0-9]+)$", ".0")
        WHERE TRUE
        """
        query_job = client.[query](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html)(query_text)
    
        # Wait for query job to finish.
        [query_job](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dbapi.Cursor.html#google_cloud_bigquery_dbapi_Cursor_query_job).result()
    
        assert [query_job](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dbapi.Cursor.html#google_cloud_bigquery_dbapi_Cursor_query_job).num_dml_affected_rows is not None
    
        print(f"DML query modified {[query_job](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dbapi.Cursor.html#google_cloud_bigquery_dbapi_Cursor_query_job).num_dml_affected_rows} rows.")
        return [query_job](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dbapi.Cursor.html#google_cloud_bigquery_dbapi_Cursor_query_job).num_dml_affected_rows
    
    
    def run_sample(override_values: Optional[Dict[str, str]] = None) -> int:
        if override_values is None:
            override_values = {}
    
        client = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html)()
        filepath = pathlib.Path(__file__).parent / "user_sessions_data.json"
        project_id = client.project
        dataset_id = "sample_db"
        table_id = "UserSessions"
        load_from_newline_delimited_json(client, filepath, project_id, dataset_id, table_id)
        return update_with_dml(client, project_id, dataset_id, table_id)
    
    

### Rust
    
    
    use google_cloud_bigquery::client::BigQuery;
    
    pub async fn sample(project_id: &str, dataset_id: &str, table_id: &str) -> anyhow::Result<()> {
        let client = BigQuery::builder().build().await?;
    
        // Query parameters cannot be used as substitutes for identifiers, column names or table
        // names. Ensure resource identifiers are validated before formatting into SQL statements
        // to prevent SQL injection.
        validate_resource_names(project_id, dataset_id, table_id)?;
    
        // First, create a sample table with initial data
        let create_sql = format!(
            "CREATE OR REPLACE TABLE `{project_id}.{dataset_id}.{table_id}` \
             (name STRING, quantity INT64) AS \
             SELECT 'Item A' AS name, 10 AS quantity UNION ALL \
             SELECT 'Item B' AS name, 20 AS quantity;"
        );
        client
            .query(create_sql)
            .with_project_id(project_id)
            .set_location("US")
            .until_done()
            .await?;
    
        // Execute a DML UPDATE query to modify existing rows in the table
        let dml_sql = format!(
            "UPDATE `{project_id}.{dataset_id}.{table_id}` \
             SET quantity = quantity + 5 \
             WHERE name = 'Item A';"
        );
        let res = client
            .query(dml_sql)
            .with_project_id(project_id)
            .set_location("US")
            .until_done()
            .await?;
    
        println!("DML UPDATE job completed successfully: {:?}", res);
        Ok(())
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
