---
url: https://docs.cloud.google.com/bigquery/docs/paging-results/
title: Using pagination with the BigQuery API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:44:48.772363+00:00
---

# Using pagination with the BigQuery API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/paging-results/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Guides ](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Using pagination with the BigQuery API

This document describes how to read table data and query results in large datasets by using pagination with the BigQuery API.

With _pagination_ , BigQuery breaks a large dataset into smaller chunks called _pages_. For most users, Cloud Client Libraries handle this process automatically, but you can also manually control pagination for specific use cases like web applications.

## Use automatic pagination

Cloud Client Libraries handle the low-level details of API pagination and provide an iterator-like experience. When you iterate through results, the library automatically fetches the next page of data when it's needed.

The following samples demonstrate how to automatically iterate through BigQuery table data.

### C#

Before trying this sample, follow the C# setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    using [Google.Api.Gax](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.html);
    using Google.Apis.Bigquery.v2.Data;
    using [Google.Cloud.BigQuery.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.html);
    using System;
    using System.Linq;
    
    public class BigQueryBrowseTable
    {
        public void BrowseTable(
            string projectId = "your-project-id"
        )
        {
            [BigQueryClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient.html) client = [BigQueryClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient.html#Google_Cloud_BigQuery_V2_BigQueryClient_Create_System_String_Google_Apis_Auth_OAuth2_GoogleCredential_)(projectId);
            TableReference tableReference = new TableReference()
            {
                TableId = "shakespeare",
                DatasetId = "samples",
                ProjectId = "bigquery-public-data"
            };
            // Load all rows from a table
            PagedEnumerable<TableDataList, BigQueryRow> result = client.[ListRows](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient.html#Google_Cloud_BigQuery_V2_BigQueryClient_ListRows_Google_Apis_Bigquery_v2_Data_TableReference_Google_Apis_Bigquery_v2_Data_TableSchema_Google_Cloud_BigQuery_V2_ListRowsOptions_)(
                tableReference: tableReference,
                schema: null
            );
            // Print the first 10 rows
            foreach ([BigQueryRow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryRow.html) row in result.Take(10))
            {
                Console.WriteLine($"{row["corpus"]}: {row["word_count"]}");
            }
        }
    }

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
    
    // browseTable demonstrates reading data from a BigQuery table directly without the use of a query.
    // For large tables, we also recommend the BigQuery Storage API.
    func browseTable(w io.Writer, projectID, datasetID, tableID string) error {
    	// projectID := "my-project-id"
    	// datasetID := "mydataset"
    	// tableID := "mytable"
    	ctx := context.Background()
    	client, err := bigquery.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("bigquery.NewClient: %v", err)
    	}
    	defer client.Close()
    
    	table := client.Dataset(datasetID).Table(tableID)
    	it := table.Read(ctx)
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
    import com.google.cloud.bigquery.[BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html).[TableDataListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.TableDataListOption.html);
    import com.google.cloud.bigquery.[BigQueryException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html);
    import com.google.cloud.bigquery.[BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html);
    import com.google.cloud.bigquery.[TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId.html);
    import com.google.cloud.bigquery.[TableResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableResult.html);
    
    // Sample to directly browse a table with optional paging
    public class BrowseTable {
    
      public static void runBrowseTable() {
        // TODO(developer): Replace these variables before running the sample.
        String table = "MY_TABLE_NAME";
        String dataset = "MY_DATASET_NAME";
        browseTable(dataset, table);
      }
    
      public static void browseTable(String dataset, String table) {
        try {
          // Initialize client that will be used to send requests. This client only needs to be created
          // once, and can be reused for multiple requests.
          BigQuery bigquery = BigQueryOptions.getDefaultInstance().getService();
    
          // Identify the table itself
          TableId tableId = TableId.of(dataset, table);
    
          // Page over 100 records. If you don't need pagination, remove the pageSize parameter.
          TableResult result = bigquery.listTableData(tableId, TableDataListOption.pageSize(100));
    
          // Print the records
          result
              .iterateAll()
              .forEach(
                  row -> {
                    row.forEach(fieldValue -> System.out.print(fieldValue.toString() + ", "));
                    System.out.println();
                  });
    
          System.out.println("Query ran successfully");
        } catch ([BigQueryException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html) e) {
          System.out.println("Query failed to run \n" + e.toString());
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Node.js API reference documentation](https://googleapis.dev/nodejs/bigquery/latest/index.html). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    // Import the Google Cloud client library using default credentials
    const {BigQuery} = require('[@google-cloud/bigquery](https://docs.cloud.google.com/nodejs/docs/reference/bigquery/latest/overview.html)');
    const bigquery = new [BigQuery](https://docs.cloud.google.com/nodejs/docs/reference/bigquery/latest/bigquery/bigquery.html)();
    
    async function browseTable() {
      // Retrieve a table's rows using manual pagination.
    
      /**
       * TODO(developer): Uncomment the following lines before running the sample.
       */
      // const datasetId = 'my_dataset'; // Existing dataset
      // const tableId = 'my_table'; // Table to create
    
      const query = `SELECT name, SUM(number) as total_people
        FROM \`bigquery-public-data.usa_names.usa_1910_2013\`
        GROUP BY name 
        ORDER BY total_people 
        DESC LIMIT 100`;
    
      // Create table reference.
      const dataset = bigquery.dataset(datasetId);
      const destinationTable = dataset.table(tableId);
    
      // For all options, see https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#jobconfigurationquery
      const queryOptions = {
        query: query,
        destination: destinationTable,
      };
    
      // Run the query as a job
      const [job] = await bigquery.createQueryJob(queryOptions);
    
      // For all options, see https://cloud.google.com/bigquery/docs/reference/v2/jobs/getQueryResults
      const queryResultsOptions = {
        // Retrieve zero resulting rows.
        maxResults: 0,
      };
    
      // Wait for the job to finish.
      await [job](https://docs.cloud.google.com/nodejs/docs/reference/bigquery/latest/bigquery/bigquery.html).[getQueryResults](https://docs.cloud.google.com/nodejs/docs/reference/bigquery/latest/bigquery/job.html)(queryResultsOptions);
    
      function manualPaginationCallback(err, rows, nextQuery) {
        rows.forEach(row => {
          console.log(`name: ${row.name}, ${row.total_people} total people`);
        });
    
        if (nextQuery) {
          // More results exist.
          destinationTable.getRows(nextQuery, manualPaginationCallback);
        }
      }
    
      // For all options, see https://cloud.google.com/bigquery/docs/reference/v2/tabledata/list
      const getRowsOptions = {
        autoPaginate: false,
        maxResults: 20,
      };
    
      // Retrieve all rows.
      destinationTable.getRows(getRowsOptions, manualPaginationCallback);
    }
    browseTable();

### PHP

Before trying this sample, follow the PHP setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery PHP API reference documentation](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/BigQueryClient). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    use Google\Cloud\BigQuery\BigQueryClient;
    
    /** Uncomment and populate these variables in your code */
    // $projectId = 'The Google project ID';
    // $datasetId = 'The BigQuery dataset ID';
    // $tableId   = 'The BigQuery table ID';
    // $maxResults = 10;
    
    $maxResults = 10;
    $startIndex = 0;
    
    $options = [
        'maxResults' => $maxResults,
        'startIndex' => $startIndex
    ];
    $bigQuery = new BigQueryClient([
        'projectId' => $projectId,
    ]);
    $dataset = $bigQuery->dataset($datasetId);
    $table = $dataset->table($tableId);
    $numRows = 0;
    foreach ($table->rows($options) as $row) {
        print('---');
        foreach ($row as $column => $value) {
            printf('%s: %s' . PHP_EOL, $column, $value);
        }
        $numRows++;
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    from google.cloud import [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest)
    
    # Construct a BigQuery client object.
    client = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html)()
    
    # TODO(developer): Set table_id to the ID of the table to browse data rows.
    # table_id = "your-project.your_dataset.your_table_name"
    
    # Download all rows from a table.
    rows_iter = client.[list_rows](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_list_rows)(table_id)  # Make an API request.
    
    # Iterate over rows to make the API requests to fetch row data.
    rows = list(rows_iter)
    print("Downloaded {} rows from table {}".format(len(rows), table_id))
    
    # Download at most 10 rows.
    rows_iter = client.[list_rows](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_list_rows)(table_id, max_results=10)
    rows = list(rows_iter)
    print("Downloaded {} rows from table {}".format(len(rows), table_id))
    
    # Specify selected fields to limit the results to certain columns.
    table = client.[get_table](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_get_table)(table_id)  # Make an API request.
    fields = table.schema[:2]  # First two columns.
    rows_iter = client.[list_rows](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_list_rows)(table_id, selected_fields=fields, max_results=10)
    rows = list(rows_iter)
    print("Selected {} columns from table {}.".format(len(rows_iter.schema), table_id))
    print("Downloaded {} rows from table {}".format(len(rows), table_id))
    
    # Print row data in tabular format.
    rows = client.[list_rows](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_list_rows)(table, max_results=10)
    format_string = "{!s:<16} " * len([rows](https://docs.cloud.google.com/python/docs/reference/bigquerystorage/latest/google.cloud.bigquery_storage_v1.reader.ReadRowsStream.html#google_cloud_bigquery_storage_v1_reader_ReadRowsStream_rows).schema)
    field_names = [field.name for field in [rows](https://docs.cloud.google.com/python/docs/reference/bigquerystorage/latest/google.cloud.bigquery_storage_v1.reader.ReadRowsStream.html#google_cloud_bigquery_storage_v1_reader_ReadRowsStream_rows).schema]
    print(format_string.format(*field_names))  # Prints column headers.
    for row in rows:
        print(format_string.format(*row))  # Prints row data.

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-bigquery/latest/Google/Cloud/Bigquery.html). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    require "google/cloud/bigquery"
    
    def browse_table
      bigquery = Google::Cloud::[Bigquery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-data_policies-v1/latest/Google-Cloud-Bigquery.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery/latest/Google-Cloud-Bigquery.html) project_id: "bigquery-public-data"
      dataset  = bigquery.dataset "samples"
      table    = dataset.table "shakespeare"
    
      # Load all rows from a table
      rows = table.data
    
      # Load the first 10 rows
      rows = table.data max: 10
    
      # Print row data
      rows.each { |row| puts row }
    end

## Control page size

You can specify the maximum number of rows returned in each network request by setting a page size. Setting the page size is useful for optimizing network usage or fitting data into memory.

In most client libraries, you can use a `max_results` or `page_size` parameter when you call methods like `list_rows` or `query`.

## Use manual pagination with page tokens

Manual pagination is useful for _stateless_ applications, such as a web service where a user clicks **Next** to see the next set of results. In this scenario, the server does not maintain an active iterator between requests.

Instead, you use a _page token_ as follows:

  1. **Request a page.** Call the API and receive a `pageToken` parameter along with the rows.
  2. **Resume.** In the next request, pass that same `pageToken` parameter back to BigQuery to retrieve the next chunk of data.



The following samples show how to retrieve a page token and use it to fetch the next page of query results.

### API

Read the [`jobs.config.query.destinationTable`](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/Job#JobConfigurationQuery.FIELDS.destination_table) field to determine the table that query results have been written to. Call the [`tabledata.list`](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tabledata/list) to read the query results.

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import com.google.cloud.bigquery.[BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html);
    import com.google.cloud.bigquery.[BigQueryException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html);
    import com.google.cloud.bigquery.[BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html);
    import com.google.cloud.bigquery.[QueryJobConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration.html);
    import com.google.cloud.bigquery.[TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId.html);
    import com.google.cloud.bigquery.[TableResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableResult.html);
    
    // Sample to run query with pagination.
    public class QueryPagination {
    
      public static void main(String[] args) {
        String datasetName = "MY_DATASET_NAME";
        String tableName = "MY_TABLE_NAME";
        String query =
            "SELECT name, SUM(number) as total_people"
                + " FROM `bigquery-public-data.usa_names.usa_1910_2013`"
                + " GROUP BY name"
                + " ORDER BY total_people DESC"
                + " LIMIT 100";
        queryPagination(datasetName, tableName, query);
      }
    
      public static void queryPagination(String datasetName, String tableName, String query) {
        try {
          // Initialize client that will be used to send requests. This client only needs to be created
          // once, and can be reused for multiple requests.
          [BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html) bigquery = [BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html).getDefaultInstance().getService();
    
          [TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId.html) tableId = [TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId.html).of(datasetName, tableName);
          [QueryJobConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration.html) queryConfig =
              [QueryJobConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.QueryJobConfiguration.html).newBuilder(query)
                  // save results into a table.
                  .setDestinationTable(tableId)
                  .build();
    
          bigquery.[query](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html#com_google_cloud_bigquery_BigQuery_query_com_google_cloud_bigquery_QueryJobConfiguration_com_google_cloud_bigquery_BigQuery_JobOption____)(queryConfig);
    
          [TableResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableResult.html) results =
              bigquery.[listTableData](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html#com_google_cloud_bigquery_BigQuery_listTableData_com_google_cloud_bigquery_TableId_com_google_cloud_bigquery_BigQuery_TableDataListOption____)(tableId, BigQuery.TableDataListOption.pageSize(20));
    
          // First Page
          results
              .getValues()
              .forEach(row -> row.forEach(val -> System.out.printf("%s,\n", val.toString())));
    
          while (results.[hasNextPage](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableResult.html#com_google_cloud_bigquery_TableResult_hasNextPage__)()) {
            // Remaining Pages
            results = results.[getNextPage](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableResult.html#com_google_cloud_bigquery_TableResult_getNextPage__)();
            results
                .getValues()
                .forEach(row -> row.forEach(val -> System.out.printf("%s,\n", val.toString())));
          }
    
          System.out.println("Query pagination performed successfully.");
        } catch ([BigQueryException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html) | InterruptedException e) {
          System.out.println("Query not performed \n" + e.toString());
        }
      }
    }

To set the number of rows returned on each page, use a [`GetQueryResults` job](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Job#com_google_cloud_bigquery_Job_getQueryResults_com_google_cloud_bigquery_BigQuery_QueryResultsOption____) and set the [`pageSize` option](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.QueryResultsOption#com_google_cloud_bigquery_BigQuery_QueryResultsOption_pageSize_long_) of the [`QueryResultsOption` object](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.QueryResultsOption) that you pass in, as shown in the following example:
    
    
    TableResult result = job.getQueryResults();
    QueryResultsOption queryResultsOption = QueryResultsOption.pageSize(20);
    
    TableResult result = job.getQueryResults(queryResultsOption);
    

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Node.js API reference documentation](https://googleapis.dev/nodejs/bigquery/latest/index.html). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    // Import the Google Cloud client library using default credentials
    const {BigQuery} = require('[@google-cloud/bigquery](https://docs.cloud.google.com/nodejs/docs/reference/bigquery/latest/overview.html)');
    const bigquery = new [BigQuery](https://docs.cloud.google.com/nodejs/docs/reference/bigquery/latest/bigquery/bigquery.html)();
    
    async function queryPagination() {
      // Run a query and get rows using automatic pagination.
    
      const query = `SELECT name, SUM(number) as total_people
      FROM \`bigquery-public-data.usa_names.usa_1910_2013\`
      GROUP BY name
      ORDER BY total_people DESC
      LIMIT 100`;
    
      // Run the query as a job.
      const [job] = await bigquery.createQueryJob(query);
    
      // Wait for job to complete and get rows.
      const [rows] = await [job](https://docs.cloud.google.com/nodejs/docs/reference/bigquery/latest/bigquery/bigquery.html).[getQueryResults](https://docs.cloud.google.com/nodejs/docs/reference/bigquery/latest/bigquery/job.html)();
    
      console.log('Query results:');
      rows.forEach(row => {
        console.log(`name: ${row.name}, ${row.total_people} total people`);
      });
    }
    queryPagination();

### Python

The [`QueryJob.result`](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.job.QueryJob#google_cloud_bigquery_job_QueryJob_result) method returns an iterable of the query results. Alternatively,

  1. Read the [`QueryJob.destination`](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.job.QueryJob#google_cloud_bigquery_job_QueryJob_destination) property. If this property is not configured, it is set by the API to a reference to a [temporary anonymous table](https://docs.cloud.google.com/bigquery/docs/writing-results#temporary_and_permanent_tables).
  2. Get the table schema with the [`Client.get_table`](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client#google_cloud_bigquery_client_Client_get_table) method.
  3. Create an iterable over all rows in the destination table with the [`Client.list_rows`](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client#google_cloud_bigquery_client_Client_list_rows) method.



Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    from google.cloud import [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest)
    
    # Construct a BigQuery client object.
    client = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html)()
    
    query = """
        SELECT name, SUM(number) as total_people
        FROM `bigquery-public-data.usa_names.usa_1910_2013`
        GROUP BY name
        ORDER BY total_people DESC
    """
    query_job = client.[query](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html)(query)  # Make an API request.
    [query_job](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dbapi.Cursor.html#google_cloud_bigquery_dbapi_Cursor_query_job).result()  # Wait for the query to complete.
    
    # Get the destination table for the query results.
    #
    # All queries write to a destination table. If a destination table is not
    # specified, the BigQuery populates it with a reference to a temporary
    # anonymous table after the query completes.
    destination = [query_job](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dbapi.Cursor.html#google_cloud_bigquery_dbapi_Cursor_query_job).destination
    
    # Get the schema (and other properties) for the destination table.
    #
    # A schema is useful for converting from BigQuery types to Python types.
    destination = client.[get_table](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_get_table)(destination)
    
    # Download rows.
    #
    # The client library automatically handles pagination.
    print("The query data:")
    rows = client.[list_rows](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_list_rows)(destination, max_results=20)
    for row in rows:
        print("name={}, count={}".format(row["name"], row["total_people"]))

## Optimize with ETags

When you page backwards or jump to arbitrary pages using cached `pageToken` values, it is possible that the data in your pages might have changed since it was last viewed. To mitigate this outcome, you can use the `etag` property.

Every `collection.list` method (except for `Tabledata`) returns an `etag` property in the result. This property is a hash of the page results that can be used to verify whether the page has changed since the last request. When you make a request to BigQuery with an ETag value, BigQuery compares the ETag value to the ETag value returned by the API and responds based on whether the ETag values match. You can use ETags to avoid redundant list calls as follows:

  * To return values only if they have changed, make a list call with a previously-stored ETag using the [HTTP `If-None-Match` header](https://www.rfc-editor.org/rfc/rfc9110.html#name-if-none-match). If the ETags match, BigQuery returns an `HTTP 304 Not Modified` status code and no data, saving bandwidth.
  * To return values only if they have **not** changed, use the [HTTP `If-Match` header](https://www.rfc-editor.org/rfc/rfc9110.html#name-if-match). BigQuery returns a `412 Precondition Failed` if the page has changed.



**Note:** Although ETags are a great way to avoid making redundant list calls, you can apply the same methods to identifying if any objects have changed. For example, you can perform a `GET` request for a specific table and use ETags to determine if the table has changed before returning the full response.

## Reference: API limits and criteria

All `*collection*.list` methods return paginated results under certain circumstances. The `maxResults` property limits the number of results per page.

Method | Pagination criteria | Default `maxResults` limit | Maximum `maxResults` limit | Maximum `maxFieldValues` limit  
---|---|---|---|---  
`tabledata.list` | Returns paginated results if the response size is more than 10 MB1 of data or more than `maxResults` rows. | Unlimited | Unlimited | Unlimited  
All other `*collection*.list` methods | Returns paginated results if the response is more than `maxResults` rows and also less than the maximum limits. | 10,000 | Unlimited | 300,000  
  
If the result is larger than the byte or field limit, the result is trimmed to fit the limit. If one row is greater than the byte or field limit, the `tabledata.list` method can return up to 100 MB of data1, which is consistent with the maximum row size limit for query results. There is no minimum size per page, and some pages might return more rows than others.

The `jobs.getQueryResults` REST API method can return 20 MB of data unless you explicitly request more through support.

1The row size is approximate, as the size is based on the internal representation of row data. The maximum row size limit is enforced during certain stages of query job execution.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
