---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-table-insert-rows/
title: Streaming insert \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:23.292138+00:00
---

# Streaming insert  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-table-insert-rows/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Streaming insert Stay organized with collections  Save and categorize content based on your preferences. 

Inserts simple rows into a table using the streaming API (insertAll).

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Use the Storage Write API (REST)](https://docs.cloud.google.com/bigquery/docs/write-api-rest)



## Code sample

### C#

Before trying this sample, follow the C# setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    using [Google.Cloud.BigQuery.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.html);
    
    public class BigQueryTableInsertRows
    {
        public void TableInsertRows(
            string projectId = "your-project-id",
            string datasetId = "your_dataset_id",
            string tableId = "your_table_id"
        )
        {
            [BigQueryClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient.html) client = [BigQueryClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient.html#Google_Cloud_BigQuery_V2_BigQueryClient_Create_System_String_Google_Apis_Auth_OAuth2_GoogleCredential_)(projectId);
            [BigQueryInsertRow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryInsertRow.html)[] rows = new [BigQueryInsertRow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryInsertRow.html)[]
            {
                // The insert ID is optional, but can avoid duplicate data
                // when retrying inserts.
                new [BigQueryInsertRow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryInsertRow.html)(insertId: "row1") {
                    { "name", "Washington" },
                    { "post_abbr", "WA" }
                },
                new [BigQueryInsertRow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryInsertRow.html)(insertId: "row2") {
                    { "name", "Colorado" },
                    { "post_abbr", "CO" }
                }
            };
            client.[InsertRows](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryClient.html#Google_Cloud_BigQuery_V2_BigQueryClient_InsertRows_Google_Apis_Bigquery_v2_Data_TableReference_Google_Cloud_BigQuery_V2_BigQueryInsertRow___)(datasetId, tableId, rows);
        }
    }

### Go

Before trying this sample, follow the Go setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Go API reference documentation](https://godoc.org/cloud.google.com/go/bigquery). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import (
    	"context"
    	"fmt"
    
    	"cloud.google.com/go/bigquery"
    )
    
    // Item represents a row item.
    type Item struct {
    	Name string
    	Age  int
    }
    
    // Save implements the ValueSaver interface.
    // This example disables best-effort de-duplication, which allows for higher throughput.
    func (i *Item) Save() (map[string]bigquery.[Value](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_Value), string, error) {
    	return map[string]bigquery.[Value](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_Value){
    		"full_name": i.Name,
    		"age":       i.Age,
    	}, bigquery.[NoDedupeID](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_NoDedupeID), nil
    }
    
    // insertRows demonstrates inserting data into a table using the streaming insert mechanism.
    func insertRows(projectID, datasetID, tableID string) error {
    	// projectID := "my-project-id"
    	// datasetID := "mydataset"
    	// tableID := "mytable"
    	ctx := context.Background()
    	client, err := bigquery.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("bigquery.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	inserter := client.Dataset(datasetID).Table(tableID).Inserter()
    	items := []*Item{
    		// Item implements the ValueSaver interface.
    		{Name: "Phred Phlyntstone", Age: 32},
    		{Name: "Wylma Phlyntstone", Age: 29},
    	}
    	if err := inserter.[Put](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_Inserter_Put)(ctx, items); err != nil {
    		return err
    	}
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import com.google.cloud.bigquery.[BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html);
    import com.google.cloud.bigquery.[BigQueryError](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryError.html);
    import com.google.cloud.bigquery.[BigQueryException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html);
    import com.google.cloud.bigquery.[BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html);
    import com.google.cloud.bigquery.[InsertAllRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.InsertAllRequest.html);
    import com.google.cloud.bigquery.[InsertAllResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.InsertAllResponse.html);
    import com.google.cloud.bigquery.[TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId.html);
    import java.util.HashMap;
    import java.util.List;
    import java.util.Map;
    
    // Sample to inserting rows into a table without running a load job.
    public class TableInsertRows {
    
      public static void main(String[] args) {
        // TODO(developer): Replace these variables before running the sample.
        String datasetName = "MY_DATASET_NAME";
        String tableName = "MY_TABLE_NAME";
        // Create a row to insert
        Map<String, Object> rowContent = new HashMap<>();
        rowContent.put("booleanField", true);
        rowContent.put("numericField", "3.14");
        // TODO(developer): Replace the row id with a unique value for each row.
        String rowId = "ROW_ID";
        tableInsertRows(datasetName, tableName, rowId, rowContent);
      }
    
      public static void tableInsertRows(
          String datasetName, String tableName, String rowId, Map<String, Object> rowContent) {
        try {
          // Initialize client that will be used to send requests. This client only needs to be created
          // once, and can be reused for multiple requests.
          BigQuery bigquery = BigQueryOptions.getDefaultInstance().getService();
    
          // Get table
          TableId tableId = TableId.of(datasetName, tableName);
    
          // Inserts rowContent into datasetName:tableId.
          InsertAllResponse response =
              bigquery.insertAll(
                  InsertAllRequest.newBuilder(tableId)
                      // More rows can be added in the same RPC by invoking .addRow() on the builder.
                      // You can omit the unique row ids to disable de-duplication.
                      .addRow(rowId, rowContent)
                      .build());
    
          if (response.hasErrors()) {
            // If any of the insertions failed, this lets you inspect the errors
            for (Map.Entry<Long, List<BigQueryError>> entry : response.getInsertErrors().entrySet()) {
              System.out.println("Response error: \n" + entry.getValue());
            }
          }
          System.out.println("Rows successfully inserted into table");
        } catch (BigQueryException e) {
          System.out.println("Insert operation not performed \n" + e.toString());
        }
      }
    }

### PHP

Before trying this sample, follow the PHP setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery PHP API reference documentation](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/BigQueryClient). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    use Google\Cloud\BigQuery\BigQueryClient;
    
    /**
     * Stream data into bigquery
     *
     * @param string $projectId The project Id of your Google Cloud Project.
     * @param string $datasetId The BigQuery dataset ID.
     * @param string $tableId The BigQuery table ID.
     * @param string $data Json encoded data For eg,
     *    $data = json_encode([
     *       "field1" => "value1",
     *       "field2" => "value2",
     *    ]);
     */
    function stream_row(
        string $projectId,
        string $datasetId,
        string $tableId,
        string $data
    ): void {
        // instantiate the bigquery table service
        $bigQuery = new BigQueryClient([
          'projectId' => $projectId,
        ]);
        $dataset = $bigQuery->dataset($datasetId);
        $table = $dataset->table($tableId);
    
        $data = json_decode($data, true);
        $insertResponse = $table->insertRows([
          ['data' => $data],
          // additional rows can go here
        ]);
        if ($insertResponse->isSuccessful()) {
            print('Data streamed into BigQuery successfully' . PHP_EOL);
        } else {
            foreach ($insertResponse->failedRows() as $row) {
                foreach ($row['errors'] as $error) {
                    printf('%s: %s' . PHP_EOL, $error['reason'], $error['message']);
                }
            }
        }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    from google.cloud import [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest)
    
    # Construct a BigQuery client object.
    client = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html)()
    
    # TODO(developer): Set table_id to the ID of table to append to.
    # table_id = "your-project.your_dataset.your_table"
    
    rows_to_insert = [
        {"full_name": "Phred Phlyntstone", "age": 32},
        {"full_name": "Wylma Phlyntstone", "age": 29},
    ]
    
    errors = client.[insert_rows_json](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_insert_rows_json)(table_id, rows_to_insert)  # Make an API request.
    if errors == []:
        print("New rows have been added.")
    else:
        print("Encountered errors while inserting rows: {}".format(errors))

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-bigquery/latest/Google/Cloud/Bigquery.html). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    require "google/cloud/bigquery"
    
    def table_insert_rows dataset_id = "your_dataset_id", table_id = "your_table_id"
      bigquery = Google::Cloud::[Bigquery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-data_policies-v1beta1/latest/Google-Cloud-Bigquery.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery/latest/Google-Cloud-Bigquery.html)
      dataset  = bigquery.dataset dataset_id
      table    = dataset.table table_id
    
      row_data = [
        { name: "Alice", value: 5  },
        { name: "Bob",   value: 10 }
      ]
      response = table.insert row_data
    
      if response.success?
        puts "Inserted rows successfully"
      else
        puts "Failed to insert #{response.error_rows.count} rows"
      end
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
