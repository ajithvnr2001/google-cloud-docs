---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-query-external-bigtable-perm/
title: Query Bigtable using a permanent table \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:42:03.758260+00:00
---

# Query Bigtable using a permanent table  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-query-external-bigtable-perm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Query Bigtable using a permanent table Stay organized with collections  Save and categorize content based on your preferences. 

Query data from a Bigtable instance by creating a permanent table.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create a Bigtable external table](https://docs.cloud.google.com/bigquery/docs/create-bigtable-external-table)



## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import com.google.api.client.util.[Base64](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Base64.html);
    import com.google.cloud.bigquery.[BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html);
    import com.google.cloud.bigquery.[BigQueryException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html);
    import com.google.cloud.bigquery.[BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html);
    import com.google.cloud.bigquery.[BigtableColumn](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigtableColumn.html);
    import com.google.cloud.bigquery.[BigtableColumnFamily](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigtableColumnFamily.html);
    import com.google.cloud.bigquery.[BigtableOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigtableOptions.html);
    import com.google.cloud.bigquery.[ExternalTableDefinition](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.ExternalTableDefinition.html);
    import com.google.cloud.bigquery.[QueryJobConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration.html);
    import com.google.cloud.bigquery.[TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId.html);
    import com.google.cloud.bigquery.[TableInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableInfo.html);
    import com.google.cloud.bigquery.[TableResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableResult.html);
    import com.google.common.collect.ImmutableList;
    
    // Sample to queries an external bigtable data source using a permanent table
    public class QueryExternalBigtablePerm {
    
      public static void main(String[] args) {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "MY_PROJECT_ID";
        String bigtableInstanceId = "MY_INSTANCE_ID";
        String bigtableTableName = "MY_BIGTABLE_NAME";
        String bigqueryDatasetName = "MY_DATASET_NAME";
        String bigqueryTableName = "MY_TABLE_NAME";
        String sourceUri =
            String.format(
                "https://googleapis.com/bigtable/projects/%s/instances/%s/tables/%s",
                projectId, bigtableInstanceId, bigtableTableName);
        String query = String.format("SELECT * FROM %s ", bigqueryTableName);
        queryExternalBigtablePerm(bigqueryDatasetName, bigqueryTableName, sourceUri, query);
      }
    
      public static void queryExternalBigtablePerm(
          String datasetName, String tableName, String sourceUri, String query) {
        try {
          // Initialize client that will be used to send requests. This client only needs to be created
          // once, and can be reused for multiple requests.
          [BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html) bigquery = [BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html).getDefaultInstance().getService();
    
          [BigtableColumnFamily](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigtableColumnFamily.html).Builder statsSummary = [BigtableColumnFamily](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigtableColumnFamily.html).newBuilder();
    
          // Configuring Columns
          [BigtableColumn](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigtableColumn.html) connectedCell =
              [BigtableColumn](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigtableColumn.html).newBuilder()
                  .[setQualifierEncoded](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigtableColumn.Builder.html#com_google_cloud_bigquery_BigtableColumn_Builder_setQualifierEncoded_java_lang_String_)([Base64](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Base64.html).[encodeBase64String](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Base64.html#com_google_api_client_util_Base64_encodeBase64String_byte___)("connected_cell".[getBytes](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery-jdbc/latest/com.google.cloud.bigquery.jdbc.BigQueryBaseResultSet.html#com_google_cloud_bigquery_jdbc_BigQueryBaseResultSet_getBytes_int_)()))
                  .[setFieldName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigtableColumn.Builder.html#com_google_cloud_bigquery_BigtableColumn_Builder_setFieldName_java_lang_String_)("connected_cell")
                  .setType("STRING")
                  .setEncoding("TEXT")
                  .build();
          [BigtableColumn](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigtableColumn.html) connectedWifi =
              [BigtableColumn](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigtableColumn.html).newBuilder()
                  .[setQualifierEncoded](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigtableColumn.Builder.html#com_google_cloud_bigquery_BigtableColumn_Builder_setQualifierEncoded_java_lang_String_)([Base64](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Base64.html).[encodeBase64String](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Base64.html#com_google_api_client_util_Base64_encodeBase64String_byte___)("connected_wifi".[getBytes](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery-jdbc/latest/com.google.cloud.bigquery.jdbc.BigQueryBaseResultSet.html#com_google_cloud_bigquery_jdbc_BigQueryBaseResultSet_getBytes_int_)()))
                  .[setFieldName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigtableColumn.Builder.html#com_google_cloud_bigquery_BigtableColumn_Builder_setFieldName_java_lang_String_)("connected_wifi")
                  .setType("STRING")
                  .setEncoding("TEXT")
                  .build();
          [BigtableColumn](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigtableColumn.html) osBuild =
              [BigtableColumn](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigtableColumn.html).newBuilder()
                  .[setQualifierEncoded](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigtableColumn.Builder.html#com_google_cloud_bigquery_BigtableColumn_Builder_setQualifierEncoded_java_lang_String_)([Base64](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Base64.html).[encodeBase64String](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Base64.html#com_google_api_client_util_Base64_encodeBase64String_byte___)("os_build".[getBytes](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery-jdbc/latest/com.google.cloud.bigquery.jdbc.BigQueryBaseResultSet.html#com_google_cloud_bigquery_jdbc_BigQueryBaseResultSet_getBytes_int_)()))
                  .[setFieldName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigtableColumn.Builder.html#com_google_cloud_bigquery_BigtableColumn_Builder_setFieldName_java_lang_String_)("os_build")
                  .setType("STRING")
                  .setEncoding("TEXT")
                  .build();
    
          // Configuring column family and columns
          statsSummary
              .setColumns(ImmutableList.of(connectedCell, connectedWifi, osBuild))
              .[setFamilyID](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigtableColumnFamily.Builder.html#com_google_cloud_bigquery_BigtableColumnFamily_Builder_setFamilyID_java_lang_String_)("stats_summary")
              .setOnlyReadLatest(true)
              .setEncoding("TEXT")
              .setType("STRING")
              .build();
    
          // Configuring BigtableOptions is optional.
          [BigtableOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigtableOptions.html) options =
              [BigtableOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigtableOptions.html).newBuilder()
                  .[setIgnoreUnspecifiedColumnFamilies](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigtableOptions.Builder.html#com_google_cloud_bigquery_BigtableOptions_Builder_setIgnoreUnspecifiedColumnFamilies_java_lang_Boolean_)(true)
                  .[setReadRowkeyAsString](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigtableOptions.Builder.html#com_google_cloud_bigquery_BigtableOptions_Builder_setReadRowkeyAsString_java_lang_Boolean_)(true)
                  .[setColumnFamilies](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigtableOptions.Builder.html#com_google_cloud_bigquery_BigtableOptions_Builder_setColumnFamilies_java_util_List_com_google_cloud_bigquery_BigtableColumnFamily__)(ImmutableList.of(statsSummary.build()))
                  .build();
    
          [TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId.html) tableId = [TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId.html).of(datasetName, tableName);
          // Create a permanent table linked to the Bigtable table
          [ExternalTableDefinition](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.ExternalTableDefinition.html) externalTable =
              [ExternalTableDefinition](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.ExternalTableDefinition.html).newBuilder(sourceUri, options).build();
          bigquery.[create](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html#com_google_cloud_bigquery_BigQuery_create_com_google_cloud_bigquery_DatasetInfo_com_google_cloud_bigquery_BigQuery_DatasetOption____)(TableInfo.of(tableId, externalTable));
    
          // Example query
          [TableResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableResult.html) results = bigquery.[query](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html#com_google_cloud_bigquery_BigQuery_query_com_google_cloud_bigquery_QueryJobConfiguration_com_google_cloud_bigquery_BigQuery_JobOption____)([QueryJobConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration.html).of(query));
    
          results
              .[iterateAll](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableResult.html#com_google_cloud_bigquery_TableResult_iterateAll__)()
              .forEach(row -> row.forEach(val -> System.out.printf("%s,", val.toString())));
    
          System.out.println("Query on external permanent table performed successfully.");
        } catch ([BigQueryException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html) | InterruptedException e) {
          System.out.println("Query not performed \n" + e.toString());
        }
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
