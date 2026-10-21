---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-query-params-positional-types/
title: Positional parameters and provided types \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:42:03.033576+00:00
---

# Positional parameters and provided types  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-query-params-positional-types/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Positional parameters and provided types Stay organized with collections  Save and categorize content based on your preferences. 

Run a query with positional parameters and provided parameter types.

## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import com.google.cloud.bigquery.[BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html);
    import com.google.cloud.bigquery.[BigQueryException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html);
    import com.google.cloud.bigquery.[BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html);
    import com.google.cloud.bigquery.[QueryJobConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration.html);
    import com.google.cloud.bigquery.[QueryParameterValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryParameterValue.html);
    import com.google.cloud.bigquery.[StandardSQLTypeName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.StandardSQLTypeName.html);
    import com.google.cloud.bigquery.[TableResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableResult.html);
    
    // Sample to run query with positional types parameters.
    public class QueryWithPositionalTypesParameters {
    
      public static void main(String[] args) {
        String[] words = {"and", "is", "the", "moon"};
        String corpus = "romeoandjuliet";
        Integer wordsCount = 250;
        String query =
            "SELECT word, word_count"
                + " FROM `bigquery-public-data.samples.shakespeare`"
                + " WHERE word IN UNNEST(?)"
                + " AND corpus = ?"
                + " AND word_count >= ?"
                + " ORDER BY word_count DESC";
        queryWithPositionalTypesParameters(query, words, corpus, wordsCount);
      }
    
      public static void queryWithPositionalTypesParameters(
          String query, String[] words, String corpus, Integer wordsCount) {
        try {
          // Initialize client that will be used to send requests. This client only needs to be created
          // once, and can be reused for multiple requests.
          [BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html) bigquery = [BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html).getDefaultInstance().getService();
    
          [QueryParameterValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryParameterValue.html) wordList = [QueryParameterValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryParameterValue.html).[array](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryParameterValue.html#com_google_cloud_bigquery_QueryParameterValue__T_array_T___com_google_cloud_bigquery_StandardSQLTypeName_)(words, [StandardSQLTypeName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.StandardSQLTypeName.html).STRING);
          [QueryParameterValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryParameterValue.html) corpusParam = [QueryParameterValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryParameterValue.html).of(corpus, [StandardSQLTypeName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.StandardSQLTypeName.html).STRING);
          [QueryParameterValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryParameterValue.html) minWordCount =
              [QueryParameterValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryParameterValue.html).of(wordsCount, [StandardSQLTypeName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.StandardSQLTypeName.html).INT64);
    
          // Note: Standard SQL is required to use query parameters.
          [QueryJobConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration.html) queryConfig =
              [QueryJobConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration.html).newBuilder(query)
                  .[addPositionalParameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration.Builder.html#com_google_cloud_bigquery_QueryJobConfiguration_Builder_addPositionalParameter_com_google_cloud_bigquery_QueryParameterValue_)(wordList)
                  .[addPositionalParameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration.Builder.html#com_google_cloud_bigquery_QueryJobConfiguration_Builder_addPositionalParameter_com_google_cloud_bigquery_QueryParameterValue_)(corpusParam)
                  .[addPositionalParameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration.Builder.html#com_google_cloud_bigquery_QueryJobConfiguration_Builder_addPositionalParameter_com_google_cloud_bigquery_QueryParameterValue_)(minWordCount)
                  .build();
    
          [TableResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableResult.html) results = bigquery.[query](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html#com_google_cloud_bigquery_BigQuery_query_com_google_cloud_bigquery_QueryJobConfiguration_com_google_cloud_bigquery_BigQuery_JobOption____)(queryConfig);
    
          results
              .[iterateAll](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableResult.html#com_google_cloud_bigquery_TableResult_iterateAll__)()
              .forEach(row -> row.forEach(val -> System.out.printf("%s,", val.toString())));
    
          System.out.println("Query with positional types parameters performed successfully.");
        } catch ([BigQueryException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html) | InterruptedException e) {
          System.out.println("Query not performed \n" + e.toString());
        }
      }
    }

### Rust
    
    
    use google_cloud_bigquery::client::BigQuery;
    use google_cloud_bigquery_v2::model::{QueryParameter, QueryParameterType, QueryParameterValue};
    
    pub async fn sample(project_id: &str) -> anyhow::Result<()> {
        let client = BigQuery::builder().build().await?;
    
        let mut rows = client
            .query("SELECT ? AS str_col, ? AS int_col, ? AS float_col;")
            .with_project_id(project_id)
            .set_parameter_mode("POSITIONAL")
            .set_query_parameters([
                QueryParameter::new()
                    .set_parameter_type(QueryParameterType::new().set_type("STRING"))
                    .set_parameter_value(QueryParameterValue::new().set_value("example string")),
                QueryParameter::new()
                    .set_parameter_type(QueryParameterType::new().set_type("INT64"))
                    .set_parameter_value(QueryParameterValue::new().set_value("42")),
                QueryParameter::new()
                    .set_parameter_type(QueryParameterType::new().set_type("FLOAT64"))
                    .set_parameter_value(QueryParameterValue::new().set_value("3.14159")),
            ])
            .set_location("US")
            .until_done()
            .await?
            .read();
    
        while let Some(row) = rows.next().await.transpose()? {
            let str_col: String = row.get("str_col")?;
            let int_col: i64 = row.get("int_col")?;
            let float_col: f64 = row.get("float_col")?;
            println!("String: {str_col}, Int: {int_col}, Float: {float_col}");
        }
        Ok(())
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
