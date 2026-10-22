---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-reads-rows/
title: Read rows \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:04.546718+00:00
---

# Read rows  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-reads-rows/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  Read rows Stay organized with collections  Save and categorize content based on your preferences. 

Reads multiple rows.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Read examples](https://docs.cloud.google.com/bigtable/docs/reading-data)



## Code sample

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace cbt = ::google::cloud::bigtable;
    using ::google::cloud::StatusOr;
    [](cbt::Table table) {
      // Read and print the rows.
      for (StatusOr<cbt::Row>& row : table.ReadRows(
               cbt::RowSet("phone#4c410523#20190501", "phone#4c410523#20190502"),
               cbt::Filter::PassAllFilter())) {
        if (!row) throw std::move(row).status();
        PrintRow(*row);
      }
    }

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    
    /// <summary>
    /// /// Reads multiple rows from an existing table.
    ///</summary>
    /// <param name="projectId">Your Google Cloud Project ID.</param>
    /// <param name="instanceId">Your Google Cloud Bigtable Instance ID.</param>
    /// <param name="tableId">Your Google Cloud Bigtable table ID.</param>
    public async Task<string> ReadRows(string projectId = "YOUR-PROJECT-ID", string instanceId = "YOUR-INSTANCE-ID", string tableId = "YOUR-TABLE-ID")
    {
        BigtableClient bigtableClient = BigtableClient.Create();
        TableName tableName = new TableName(projectId, instanceId, tableId);
    
        RowSet rowSet = RowSet.FromRowKeys("phone#4c410523#20190501", "phone#4c410523#20190502");
        ReadRowsStream readRowsStream = bigtableClient.ReadRows(tableName, rowSet);
    
        string result = "";
        await foreach(var row in readRowsStream)
        {
            result += PrintRow(row);
        }
    
        return result;
    }

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    func readRows(w io.Writer, projectID, instanceID string, tableName string) error {
    	// projectID := "my-project-id"
    	// instanceID := "my-instance-id"
    	// tableName := "mobile-time-series"
    
    	ctx := context.Background()
    	client, err := bigtable.NewClient(ctx, projectID, instanceID)
    	if err != nil {
    		return fmt.Errorf("bigtable.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	tbl := client.Open(tableName)
    	err = tbl.ReadRows(ctx, bigtable.RowList{"phone#4c410523#20190501", "phone#4c410523#20190502"},
    		func(row bigtable.Row) bool {
    			printRow(w, row)
    			return true
    		},
    	)
    	if err != nil {
    		return fmt.Errorf("tbl.ReadRows: %w", err)
    	}
    
    	return nil
    }
    

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    public static void readRows() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      readRows(projectId, instanceId, tableId);
    }
    
    public static void readRows(String projectId, String instanceId, String tableId) {
      // Initialize client that will be used to send requests. This client only needs to be created
      // once, and can be reused for multiple requests. After completing all of your requests, call
      // the "close" method on the client to safely clean up any remaining background resources.
      try (BigtableDataClient dataClient = BigtableDataClient.create(projectId, instanceId)) {
        Query query =
            Query.create(TableId.of(tableId))
                .rowKey("phone#4c410523#20190501")
                .rowKey("phone#4c410523#20190502");
        ServerStream<Row> rows = dataClient.readRows(query);
        for (Row row : rows) {
          printRow(row);
        }
      } catch (IOException e) {
        System.out.println(
            "Unable to initialize service client, as a network error occurred: \n" + e.toString());
      }
    }
    

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Bigtable\BigtableClient;
    
    /**
     * Read rows using an array of keys
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance
     * @param string $tableId The ID of the table to read from
     */
    function read_rows(
        string $projectId,
        string $instanceId,
        string $tableId
    ): void {
        // Connect to an existing table with an existing instance.
        $dataClient = new BigtableClient([
            'projectId' => $projectId,
        ]);
        $table = $dataClient->table($instanceId, $tableId);
    
        $rows = $table->readRows(
            ['rowKeys' => ['phone#4c410523#20190501', 'phone#4c410523#20190502']]
        );
    
        foreach ($rows as $key => $row) {
            print_row($key, $row);
        }
    }

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def read_rows(project_id, instance_id, table_id):
        from google.cloud import [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest)
        from google.cloud.bigtable.row_set import [RowSet](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.row_set.RowSet.html)
    
        client = [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html)(project=project_id, admin=True)
        instance = [client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.html).[instance](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html#google_cloud_bigtable_client_Client_instance)(instance_id)
        table = instance.table(table_id)
    
        row_set = RowSet()
        [row_set](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.row_set.html).[add_row_key](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.row_set.RowSet.html#google_cloud_bigtable_row_set_RowSet_add_row_key)(b"phone#4c410523#20190501")
        [row_set](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.row_set.html).[add_row_key](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.row_set.RowSet.html#google_cloud_bigtable_row_set_RowSet_add_row_key)(b"phone#4c410523#20190502")
    
        rows = table.read_rows(row_set=row_set)
        for row in rows:
            print_row(row)
    
    

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # instance_id = "my-instance"
    # table_id    = "my-table"
    bigtable = Google::Cloud::[Bigtable](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable.html)
    table = bigtable.table instance_id, table_id
    
    table.read_rows(keys: ["phone#4c410523#20190501", "phone#4c410523#20190502"]).[each](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-ColumnFamilyMap.html) do |row|
      print_row row
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
