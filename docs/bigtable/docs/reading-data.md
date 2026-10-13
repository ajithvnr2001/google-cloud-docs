---
url: https://docs.cloud.google.com/bigtable/docs/reading-data/
title: Read examples \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:08:16.142173+00:00
---

# Read examples  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/reading-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Read examples

Cloud Bigtable client libraries provide the ability to read data from a table. This page provides examples of each type of read request in multiple languages. For an overview, see [Reads](https://docs.cloud.google.com/bigtable/docs/reads).

The Python client library for Bigtable offers two APIs, `asyncio` and a synchronous API. If your application is asynchronous, use `asyncio`. 

## Required roles

To get the permissions that you need to read data from a table, ask your administrator to grant you the [**Bigtable reader** ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigtable#bigtable.reader) (`roles/bigtable.reader`) IAM role on the table. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Read a single row

The following code samples show how to get a **single row** of data using the row key.

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    func readRow(w io.Writer, projectID, instanceID string, tableName string) error {
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
    	rowKey := "phone#4c410523#20190501"
    	row, err := tbl.ReadRow(ctx, rowKey)
    	if err != nil {
    		return fmt.Errorf("could not read row with key %s: %w", rowKey, err)
    	}
    
    	printRow(w, row)
    	return nil
    }
    

### HBase

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    /**
     * Example of reading an individual row key.
     */
    public static void readRow() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      readRow(projectId, instanceId, tableId);
    }
    
    public static void readRow(String projectId, String instanceId, String tableId) {
      // Initialize client that will be used to send requests. This client only needs to be created
      // once, and can be reused for multiple requests.
      try (Connection connection = BigtableConfiguration.connect(projectId, instanceId)) {
        Table table = connection.getTable(TableName.valueOf(tableId));
    
        byte[] rowkey = Bytes.toBytes("phone#4c410523#20190501");
    
        Result row = table.get(new Get(rowkey));
        printRow(row);
    
      } catch (IOException e) {
        System.out.println(
            "Unable to initialize service client, as a network error occurred: \n" + e.toString());
      }
    }

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    public static void readRow() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      readRow(projectId, instanceId, tableId);
    }
    
    public static void readRow(String projectId, String instanceId, String tableId) {
      // Initialize client that will be used to send requests. This client only needs to be created
      // once, and can be reused for multiple requests. After completing all of your requests, call
      // the "close" method on the client to safely clean up any remaining background resources.
      try (BigtableDataClient dataClient = BigtableDataClient.create(projectId, instanceId)) {
        String rowkey = "phone#4c410523#20190501";
    
        Row row = dataClient.readRow(TableId.of(tableId), rowkey);
        printRow(row);
    
      } catch (IOException e) {
        System.out.println(
            "Unable to initialize service client, as a network error occurred: \n" + e.toString());
      }
    }
    

### Python asyncio

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    from google.cloud.bigtable.data import BigtableDataClientAsync
    
    async def read_row(project_id, instance_id, table_id):
        async with BigtableDataClientAsync(project=project_id) as client:
            async with client.get_table(instance_id, table_id) as table:
                row_key = "phone#4c410523#20190501"
                row = await table.read_row(row_key)
                print(row)
    

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    def read_row(project_id, instance_id, table_id):
        from google.cloud import [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest)
    
        client = [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html)(project=project_id, admin=True)
        instance = [client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.html).[instance](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html#google_cloud_bigtable_client_Client_instance)(instance_id)
        table = instance.table(table_id)
    
        row_key = "phone#4c410523#20190501"
    
        row = table.read_row(row_key)
        print_row(row)
    
    

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    /// <summary>
    /// /// Reads one row from an existing table.
    ///</summary>
    /// <param name="projectId">Your Google Cloud Project ID.</param>
    /// <param name="instanceId">Your Google Cloud Bigtable Instance ID.</param>
    /// <param name="tableId">Your Google Cloud Bigtable table ID.</param>
    public string ReadRow(
        string projectId = "YOUR-PROJECT-ID", string instanceId = "YOUR-INSTANCE-ID", string tableId = "YOUR-TABLE-ID")
    {
        BigtableClient bigtableClient = BigtableClient.Create();
        TableName tableName = new TableName(projectId, instanceId, tableId);
        Row row = bigtableClient.ReadRow(tableName, rowKey: "phone#4c410523#20190501");
    
        return PrintRow(row);
    }

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    namespace cbt = ::google::cloud::bigtable;
    using ::google::cloud::StatusOr;
    [](google::cloud::bigtable::Table table, std::string const& row_key) {
      StatusOr<std::pair<bool, cbt::Row>> tuple =
          table.ReadRow(row_key, cbt::Filter::PassAllFilter());
      if (!tuple) throw std::move(tuple).status();
      if (!tuple->first) {
        std::cout << "Row " << row_key << " not found\n";
        return;
      }
      PrintRow(tuple->second);
    }

### Node.js

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    const rowkey = 'phone#4c410523#20190501';
    
    const [row] = await table.row(rowkey).get();
    printRow(rowkey, row.data);

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Bigtable\BigtableClient;
    
    /**
     * Read a row using the row key
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance
     * @param string $tableId The ID of the table to read from
     */
    function read_row(
        string $projectId,
        string $instanceId,
        string $tableId
    ): void {
        // Connect to an existing table with an existing instance.
        $dataClient = new BigtableClient([
            'projectId' => $projectId,
        ]);
        $table = $dataClient->table($instanceId, $tableId);
    
        $rowkey = 'phone#4c410523#20190501';
        $row = $table->readRow($rowkey);
    
        print_row($rowkey, $row);
    }

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
      # instance_id = "my-instance"
      # table_id    = "my-table"
      bigtable = Google::Cloud::[Bigtable](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable.html)
      table = bigtable.table instance_id, table_id
    
      row = table.read_row "phone#4c410523#20190501"
      print_row row
    end
    

## Read a partial row

The following code samples show how to get **specific columns** from a row.

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    func readRowPartial(w io.Writer, projectID, instanceID string, tableName string) error {
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
    	rowKey := "phone#4c410523#20190501"
    	row, err := tbl.ReadRow(ctx, rowKey, bigtable.RowFilter(bigtable.ColumnFilter("os_build")))
    	if err != nil {
    		return fmt.Errorf("could not read row with key %s: %w", rowKey, err)
    	}
    
    	printRow(w, row)
    
    	return nil
    }
    

### HBase

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    /**
     * Example of reading a subset of the columns for a single row.
     */
    public static void readRowPartial() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      readRowPartial(projectId, instanceId, tableId);
    }
    
    public static void readRowPartial(String projectId, String instanceId, String tableId) {
      // Initialize client that will be used to send requests. This client only needs to be created
      // once, and can be reused for multiple requests.
      try (Connection connection = BigtableConfiguration.connect(projectId, instanceId)) {
        Table table = connection.getTable(TableName.valueOf(tableId));
        byte[] rowkey = Bytes.toBytes("phone#4c410523#20190501");
    
        Result row =
            table.get(
                new Get(rowkey).addColumn(Bytes.toBytes("stats_summary"), Bytes.toBytes("os_build")));
        printRow(row);
    
      } catch (IOException e) {
        System.out.println(
            "Unable to initialize service client, as a network error occurred: \n" + e.toString());
      }
    }

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    public static void readRowPartial() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      readRowPartial(projectId, instanceId, tableId);
    }
    
    public static void readRowPartial(String projectId, String instanceId, String tableId) {
      // Initialize client that will be used to send requests. This client only needs to be created
      // once, and can be reused for multiple requests. After completing all of your requests, call
      // the "close" method on the client to safely clean up any remaining background resources.
      try (BigtableDataClient dataClient = BigtableDataClient.create(projectId, instanceId)) {
        String rowkey = "phone#4c410523#20190501";
        Filters.Filter filter =
            FILTERS
                .chain()
                .filter(FILTERS.family().exactMatch("stats_summary"))
                .filter(FILTERS.qualifier().exactMatch("os_build"));
    
        Row row = dataClient.readRow(TableId.of(tableId), rowkey, filter);
        printRow(row);
    
      } catch (IOException e) {
        System.out.println(
            "Unable to initialize service client, as a network error occurred: \n" + e.toString());
      }
    }
    

### Python asyncio

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    from google.cloud.bigtable.data import BigtableDataClientAsync
    from google.cloud.bigtable.data import [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html)
    
    async def read_row_partial(project_id, instance_id, table_id):
        async with BigtableDataClientAsync(project=project_id) as client:
            async with client.get_table(instance_id, table_id) as table:
                row_key = "phone#4c410523#20190501"
                col_filter = [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[ColumnQualifierRegexFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.ColumnQualifierRegexFilter.html)(b"os_build")
    
                row = await table.read_row(row_key, row_filter=col_filter)
                print(row)
    

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    def read_row_partial(project_id, instance_id, table_id):
        from google.cloud import [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest)
        from google.cloud.bigtable import row_filters
    
        client = [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html)(project=project_id, admin=True)
        instance = [client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.html).[instance](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html#google_cloud_bigtable_client_Client_instance)(instance_id)
        table = instance.table(table_id)
    
        row_key = "phone#4c410523#20190501"
        col_filter = row_filters.ColumnQualifierRegexFilter(b"os_build")
    
        row = table.read_row(row_key, filter_=col_filter)
        print_row(row)
    
    

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    /// <summary>
    /// /// Reads part of one row from an existing table.
    ///</summary>
    /// <param name="projectId">Your Google Cloud Project ID.</param>
    /// <param name="instanceId">Your Google Cloud Bigtable Instance ID.</param>
    /// <param name="tableId">Your Google Cloud Bigtable table ID.</param>
    
    public string ReadRowPartial(string projectId = "YOUR-PROJECT-ID", string instanceId = "YOUR-INSTANCE-ID", string tableId = "YOUR-TABLE-ID")
    {
        BigtableClient bigtableClient = BigtableClient.Create();
        TableName tableName = new TableName(projectId, instanceId, tableId);
        string rowkey = "phone#4c410523#20190501";
        RowFilter filter = RowFilters.ColumnQualifierExact("os_build");
        Row row = bigtableClient.ReadRow(tableName, rowkey, filter);
        return PrintRow(row);
    }

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    namespace cbt = ::google::cloud::bigtable;
    using ::google::cloud::StatusOr;
    [](google::cloud::bigtable::Table table, std::string const& row_key) {
      StatusOr<std::pair<bool, cbt::Row>> tuple = table.ReadRow(
          row_key, cbt::Filter::ColumnName("stats_summary", "os_build"));
      if (!tuple) throw std::move(tuple).status();
      if (!tuple->first) {
        std::cout << "Row " << row_key << " not found\n";
        return;
      }
      PrintRow(tuple->second);
    }

### Node.js

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    const COLUMN_FAMILY = 'stats_summary';
    const COLUMN_QUALIFIER = 'os_build';
    const rowkey = 'phone#4c410523#20190501';
    
    const [row] = await table
      .row(rowkey)
      .get([`${COLUMN_FAMILY}:${COLUMN_QUALIFIER}`]);
    
    printRow(rowkey, row);

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Bigtable\BigtableClient;
    use Google\Cloud\Bigtable\Filter;
    
    /**
     * Read partial row data
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance
     * @param string $tableId The ID of the table to read from
     */
    function read_row_partial(
        string $projectId,
        string $instanceId,
        string $tableId
    ): void {
        // Connect to an existing table with an existing instance.
        $dataClient = new BigtableClient([
            'projectId' => $projectId,
        ]);
        $table = $dataClient->table($instanceId, $tableId);
    
        $rowkey = 'phone#4c410523#20190501';
        $rowFilter = Filter::qualifier()->regex('os_build');
        $row = $table->readRow($rowkey, ['filter' => $rowFilter]);
    
        print_row($rowkey, $row);
    }

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
      # instance_id = "my-instance"
      # table_id    = "my-table"
      bigtable = Google::Cloud::[Bigtable](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable.html)
      table = bigtable.table instance_id, table_id
      filter = Google::Cloud::[Bigtable](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable.html)::[RowFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-RowFilter.html).qualifier "os_build"
    
      row = table.read_row "phone#4c410523#20190501", filter: filter
      print_row row
    end
    

## Read multiple rows

The following code samples show how to get **multiple rows** of data using a set of row keys.

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
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
    

### HBase

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    /**
     * Example of reading multiple row keys.
     */
    public static void readRows() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      readRows(projectId, instanceId, tableId);
    }
    
    public static void readRows(String projectId, String instanceId, String tableId) {
      // Initialize client that will be used to send requests. This client only needs to be created
      // once, and can be reused for multiple requests.
      try (Connection connection = BigtableConfiguration.connect(projectId, instanceId)) {
        Table table = connection.getTable(TableName.valueOf(tableId));
        List<Get> queryRowList = new ArrayList<Get>();
        queryRowList.add(new Get(Bytes.toBytes("phone#4c410523#20190501")));
        queryRowList.add(new Get(Bytes.toBytes("phone#4c410523#20190502")));
    
        Result[] rows = table.get(queryRowList);
    
        for (Result row : rows) {
          printRow(row);
        }
      } catch (IOException e) {
        System.out.println(
            "Unable to initialize service client, as a network error occurred: \n" + e.toString());
      }
    }

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
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
    

### Python asyncio

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    from google.cloud.bigtable.data import BigtableDataClientAsync
    from google.cloud.bigtable.data import [ReadRowsQuery](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.read_rows_query.ReadRowsQuery.html)
    
    async def read_rows(project_id, instance_id, table_id):
        async with BigtableDataClientAsync(project=project_id) as client:
            async with client.get_table(instance_id, table_id) as table:
    
                query = ReadRowsQuery(
                    row_keys=[b"phone#4c410523#20190501", b"phone#4c410523#20190502"]
                )
                async for row in await table.read_rows_stream(query):
                    print(row)
    

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
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
    
    

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    
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

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
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

### Node.js

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    const rowKeys = ['phone#4c410523#20190501', 'phone#4c410523#20190502'];
    const [rows] = await table.getRows({keys: rowKeys});
    rows.forEach(row => printRow(row.id, row.data));

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
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

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    # instance_id = "my-instance"
    # table_id    = "my-table"
    bigtable = Google::Cloud::[Bigtable](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable.html)
    table = bigtable.table instance_id, table_id
    
    table.read_rows(keys: ["phone#4c410523#20190501", "phone#4c410523#20190502"]).[each](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-ColumnFamilyMap.html) do |row|
      print_row row
    end

## Read a range of rows

The following code samples show how to get **multiple rows** of data using a **start key and an end key**.

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    func readRowRange(w io.Writer, projectID, instanceID string, tableName string) error {
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
    	err = tbl.ReadRows(ctx, bigtable.NewRange("phone#4c410523#20190501", "phone#4c410523#201906201"),
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
    

### HBase

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    /**
     * Example of reading a range of rows using a key range.
     */
    public static void readRowRange() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      readRowRange(projectId, instanceId, tableId);
    }
    
    public static void readRowRange(String projectId, String instanceId, String tableId) {
      // Initialize client that will be used to send requests. This client only needs to be created
      // once, and can be reused for multiple requests.
      try (Connection connection = BigtableConfiguration.connect(projectId, instanceId)) {
        Table table = connection.getTable(TableName.valueOf(tableId));
    
        Scan rangeQuery =
            new Scan()
                .withStartRow(Bytes.toBytes("phone#4c410523#20190501"))
                .withStopRow(Bytes.toBytes("phone#4c410523#201906201"));
    
        ResultScanner rows = table.getScanner(rangeQuery);
    
        for (Result row : rows) {
          printRow(row);
        }
    
      } catch (IOException e) {
        System.out.println(
            "Unable to initialize service client, as a network error occurred: \n" + e.toString());
      }
    }

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    public static void readRowRange() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      readRowRange(projectId, instanceId, tableId);
    }
    
    public static void readRowRange(String projectId, String instanceId, String tableId) {
      String start = "phone#4c410523#20190501";
      String end = "phone#4c410523#201906201";
    
      // Initialize client that will be used to send requests. This client only needs to be created
      // once, and can be reused for multiple requests. After completing all of your requests, call
      // the "close" method on the client to safely clean up any remaining background resources.
      try (BigtableDataClient dataClient = BigtableDataClient.create(projectId, instanceId)) {
        Query query = Query.create(TableId.of(tableId)).range(start, end);
        ServerStream<Row> rows = dataClient.readRows(query);
        for (Row row : rows) {
          printRow(row);
        }
      } catch (IOException e) {
        System.out.println(
            "Unable to initialize service client, as a network error occurred: \n" + e.toString());
      }
    }
    

### Python asyncio

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    from google.cloud.bigtable.data import BigtableDataClientAsync
    from google.cloud.bigtable.data import [ReadRowsQuery](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.read_rows_query.ReadRowsQuery.html)
    from google.cloud.bigtable.data import [RowRange](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.read_rows_query.RowRange.html)
    
    async def read_row_range(project_id, instance_id, table_id):
        async with BigtableDataClientAsync(project=project_id) as client:
            async with client.get_table(instance_id, table_id) as table:
    
                row_range = RowRange(
                    start_key=b"phone#4c410523#20190501",
                    end_key=b"phone#4c410523#201906201",
                )
                query = ReadRowsQuery(row_ranges=[row_range])
    
                async for row in await table.read_rows_stream(query):
                    print(row)
    

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    def read_row_range(project_id, instance_id, table_id):
        from google.cloud import [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest)
        from google.cloud.bigtable.row_set import [RowSet](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.row_set.RowSet.html)
    
        client = [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html)(project=project_id, admin=True)
        instance = [client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.html).[instance](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html#google_cloud_bigtable_client_Client_instance)(instance_id)
        table = instance.table(table_id)
    
        row_set = RowSet()
        [row_set](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.row_set.html).[add_row_range_from_keys](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.row_set.RowSet.html#google_cloud_bigtable_row_set_RowSet_add_row_range_from_keys)(
            start_key=b"phone#4c410523#20190501", end_key=b"phone#4c410523#201906201"
        )
    
        rows = table.read_rows(row_set=row_set)
        for row in rows:
            print_row(row)
    
    

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    /// <summary>
    /// /// Reads a range of rows from an existing table.
    ///</summary>
    /// <param name="projectId">Your Google Cloud Project ID.</param>
    /// <param name="instanceId">Your Google Cloud Bigtable Instance ID.</param>
    /// <param name="tableId">Your Google Cloud Bigtable table ID.</param>
    
    public async Task<string> ReadRowRange(string projectId = "YOUR-PROJECT-ID", string instanceId = "YOUR-INSTANCE-ID", string tableId = "YOUR-TABLE-ID")
    {
        string start = "phone#4c410523#20190501";
        string end = "phone#4c410523#201906201";
    
        BigtableClient bigtableClient = BigtableClient.Create();
        TableName tableName = new TableName(projectId, instanceId, tableId);
        RowSet rowSet = RowSet.FromRowRanges(RowRange.ClosedOpen(start, end));
        ReadRowsStream readRowsStream = bigtableClient.ReadRows(tableName, rowSet);
    
        string result = "";
        await foreach (var row in readRowsStream)
        {
            result += PrintRow(row);
        }
    
        return result;
    }

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    namespace cbt = ::google::cloud::bigtable;
    using ::google::cloud::StatusOr;
    [](cbt::Table table) {
      // Read and print the rows.
      for (StatusOr<cbt::Row>& row :
           table.ReadRows(cbt::RowRange::Range("phone#4c410523#20190501",
                                               "phone#4c410523#201906201"),
                          cbt::Filter::PassAllFilter())) {
        if (!row) throw std::move(row).status();
        PrintRow(*row);
      }
    }

### Node.js

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    const start = 'phone#4c410523#20190501';
    const end = 'phone#4c410523#201906201';
    
    await table
      .createReadStream({
        start,
        end,
      })
      .on('error', err => {
        // Handle the error.
        console.log(err);
      })
      .on('data', row => printRow(row.id, row.data))
      .on('end', () => {
        // All rows retrieved.
      });

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Bigtable\BigtableClient;
    
    /**
     * Read using a range for row keys
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance
     * @param string $tableId The ID of the table to read from
     */
    function read_row_range(
        string $projectId,
        string $instanceId,
        string $tableId
    ): void {
        // Connect to an existing table with an existing instance.
        $dataClient = new BigtableClient([
            'projectId' => $projectId,
        ]);
        $table = $dataClient->table($instanceId, $tableId);
    
        $rows = $table->readRows([
            'rowRanges' => [
                [
                    'startKeyClosed' => 'phone#4c410523#20190501',
                    'endKeyOpen' => 'phone#4c410523#201906201'
                ]
            ]
        ]);
    
        foreach ($rows as $key => $row) {
            print_row($key, $row);
        }
    }

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    # instance_id = "my-instance"
    # table_id    = "my-table"
    bigtable = Google::Cloud::[Bigtable](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable.html)
    table = bigtable.table instance_id, table_id
    
    range = table.[new_row_range](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-ReadOperations.html).between "phone#4c410523#20190501", "phone#4c410523#201906201"
    table.read_rows(ranges: range).[each](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-ColumnFamilyMap.html) do |row|
      print_row row
    end

## Read multiple ranges of rows

The following code samples show how to get **multiple rows** of data using **multiple start key and end keys**. Be aware that requesting a large number of row ranges in a single request can have an impact on [read performance](https://docs.cloud.google.com/bigtable/docs/reads#many-row-ranges).

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    func readRowRanges(w io.Writer, projectID, instanceID string, tableName string) error {
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
    	err = tbl.ReadRows(ctx, bigtable.RowRangeList{
    		bigtable.NewRange("phone#4c410523#20190501", "phone#4c410523#201906201"),
    		bigtable.NewRange("phone#5c10102#20190501", "phone#5c10102#201906201"),
    	},
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
    

### HBase

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    /**
     * Example of reading multiple disjoint row ranges.
     */
    public static void readRowRanges() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      readRowRanges(projectId, instanceId, tableId);
    }
    
    public static void readRowRanges(String projectId, String instanceId, String tableId) {
      // Initialize client that will be used to send requests. This client only needs to be created
      // once, and can be reused for multiple requests.
      try (Connection connection = BigtableConfiguration.connect(projectId, instanceId)) {
        Table table = connection.getTable(TableName.valueOf(tableId));
        List<RowRange> ranges = new ArrayList<>();
    
        ranges.add(
            new RowRange(
                Bytes.toBytes("phone#4c410523#20190501"),
                true,
                Bytes.toBytes("phone#4c410523#20190601"),
                false));
        ranges.add(
            new RowRange(
                Bytes.toBytes("phone#5c10102#20190501"),
                true,
                Bytes.toBytes("phone#5c10102#20190601"),
                false));
        Filter filter = new MultiRowRangeFilter(ranges);
        Scan scan = new Scan().setFilter(filter);
    
        ResultScanner rows = table.getScanner(scan);
    
        for (Result row : rows) {
          printRow(row);
        }
      } catch (IOException e) {
        System.out.println(
            "Unable to initialize service client, as a network error occurred: \n" + e.toString());
      }
    }

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    public static void readRowRanges() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      readRowRanges(projectId, instanceId, tableId);
    }
    
    public static void readRowRanges(String projectId, String instanceId, String tableId) {
      // Initialize client that will be used to send requests. This client only needs to be created
      // once, and can be reused for multiple requests. After completing all of your requests, call
      // the "close" method on the client to safely clean up any remaining background resources.
      try (BigtableDataClient dataClient = BigtableDataClient.create(projectId, instanceId)) {
        Query query =
            Query.create(TableId.of(tableId))
                .range("phone#4c410523#20190501", "phone#4c410523#20190601")
                .range("phone#5c10102#20190501", "phone#5c10102#20190601");
        ServerStream<Row> rows = dataClient.readRows(query);
        for (Row row : rows) {
          printRow(row);
        }
      } catch (IOException e) {
        System.out.println(
            "Unable to initialize service client, as a network error occurred: \n" + e.toString());
      }
    }
    

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    def read_row_ranges(project_id, instance_id, table_id):
        from google.cloud import [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest)
        from google.cloud.bigtable.row_set import [RowSet](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.row_set.RowSet.html)
    
        client = [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html)(project=project_id, admin=True)
        instance = [client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.html).[instance](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html#google_cloud_bigtable_client_Client_instance)(instance_id)
        table = instance.table(table_id)
    
        row_set = RowSet()
        [row_set](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.row_set.html).[add_row_range_from_keys](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.row_set.RowSet.html#google_cloud_bigtable_row_set_RowSet_add_row_range_from_keys)(
            start_key=b"phone#4c410523#20190501", end_key=b"phone#4c410523#201906201"
        )
        [row_set](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.row_set.html).[add_row_range_from_keys](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.row_set.RowSet.html#google_cloud_bigtable_row_set_RowSet_add_row_range_from_keys)(
            start_key=b"phone#5c10102#20190501", end_key=b"phone#5c10102#201906201"
        )
    
        rows = table.read_rows(row_set=row_set)
        for row in rows:
            print_row(row)
    
    

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    /// <summary>
    /// /// Reads multiple ranges of rows from an existing table.
    ///</summary>
    /// <param name="projectId">Your Google Cloud Project ID.</param>
    /// <param name="instanceId">Your Google Cloud Bigtable Instance ID.</param>
    /// <param name="tableId">Your Google Cloud Bigtable table ID.</param>
    
    public async Task<string> ReadRowRanges(string projectId = "YOUR-PROJECT-ID", string instanceId = "YOUR-INSTANCE-ID", string tableId = "YOUR-TABLE-ID")
    {
        BigtableClient bigtableClient = BigtableClient.Create();
        TableName tableName = new TableName(projectId, instanceId, tableId);
        RowSet rowSet = RowSet.FromRowRanges(RowRange.ClosedOpen("phone#4c410523#20190501", "phone#4c410523#20190601"),
        RowRange.ClosedOpen("phone#5c10102#20190501", "phone#5c10102#20190601"));
        ReadRowsStream readRowsStream = bigtableClient.ReadRows(tableName, rowSet);
    
        string result = "";
        await foreach (var row in readRowsStream)
        {
            result += PrintRow(row);
        }
    
        return result;
    }

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    namespace cbt = ::google::cloud::bigtable;
    using ::google::cloud::StatusOr;
    [](cbt::Table table) {
      // Read and print the rows.
      for (StatusOr<cbt::Row>& row : table.ReadRows(
               cbt::RowSet({cbt::RowRange::Range("phone#4c410523#20190501",
                                                 "phone#4c410523#20190601"),
                            cbt::RowRange::Range("phone#5c10102#20190501",
                                                 "phone#5c10102#20190601")}),
               cbt::Filter::PassAllFilter())) {
        if (!row) throw std::move(row).status();
        PrintRow(*row);
      }
    }

### Node.js

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    await table
      .createReadStream({
        ranges: [
          {
            start: 'phone#4c410523#20190501',
            end: 'phone#4c410523#20190601',
          },
          {
            start: 'phone#5c10102#20190501',
            end: 'phone#5c10102#20190601',
          },
        ],
      })
      .on('error', err => {
        // Handle the error.
        console.log(err);
      })
      .on('data', row => printRow(row.id, row.data))
      .on('end', () => {
        // All rows retrieved.
      });

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Bigtable\BigtableClient;
    
    /**
     * Read using multiple ranges for row keys
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance
     * @param string $tableId The ID of the table to read from
     */
    function read_row_ranges(
        string $projectId,
        string $instanceId,
        string $tableId
    ): void {
        // Connect to an existing table with an existing instance.
        $dataClient = new BigtableClient([
            'projectId' => $projectId,
        ]);
        $table = $dataClient->table($instanceId, $tableId);
    
        $rows = $table->readRows([
            'rowRanges' => [
                [
                    'startKeyClosed' => 'phone#4c410523#20190501',
                    'endKeyOpen' => 'phone#4c410523#201906201'
                ],
                [
                    'startKeyClosed' => 'phone#5c10102#20190501',
                    'endKeyOpen' => 'phone#5c10102#201906201'
                ]
            ]
        ]);
    
        foreach ($rows as $key => $row) {
            print_row($key, $row);
        }
    }

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    # instance_id = "my-instance"
    # table_id    = "my-table"
    bigtable = Google::Cloud::[Bigtable](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable.html)
    table = bigtable.table instance_id, table_id
    
    ranges = []
    ranges <<
      table.[new_row_range](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-ReadOperations.html).between("phone#4c410523#20190501", "phone#4c410523#201906201") <<
      table.[new_row_range](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-ReadOperations.html).between("phone#5c10102#20190501", "phone#5c10102#201906201")
    table.read_rows(ranges: ranges).[each](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-ColumnFamilyMap.html) do |row|
      print_row row
    end

## Read multiple rows using a row key prefix

The following code samples show how to get **multiple rows** of data using a **row key prefix**.

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    func readPrefix(w io.Writer, projectID, instanceID string, tableName string) error {
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
    	err = tbl.ReadRows(ctx, bigtable.PrefixRange("phone#"),
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
    

### HBase

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    /**
     * Example of reading a range of rows using a row prefix.
     */
    public static void readPrefix() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      readPrefix(projectId, instanceId, tableId);
    }
    
    public static void readPrefix(String projectId, String instanceId, String tableId) {
      // Initialize client that will be used to send requests. This client only needs to be created
      // once, and can be reused for multiple requests.
      try (Connection connection = BigtableConfiguration.connect(projectId, instanceId)) {
        Table table = connection.getTable(TableName.valueOf(tableId));
        Scan prefixScan = new Scan().setRowPrefixFilter(Bytes.toBytes("phone"));
        ResultScanner rows = table.getScanner(prefixScan);
    
        for (Result row : rows) {
          printRow(row);
        }
      } catch (IOException e) {
        System.out.println(
            "Unable to initialize service client, as a network error occurred: \n" + e.toString());
      }
    }

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    public static void readPrefix() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      readPrefix(projectId, instanceId, tableId);
    }
    
    public static void readPrefix(String projectId, String instanceId, String tableId) {
      // Initialize client that will be used to send requests. This client only needs to be created
      // once, and can be reused for multiple requests. After completing all of your requests, call
      // the "close" method on the client to safely clean up any remaining background resources.
      try (BigtableDataClient dataClient = BigtableDataClient.create(projectId, instanceId)) {
        Query query = Query.create(TableId.of(tableId)).prefix("phone");
        ServerStream<Row> rows = dataClient.readRows(query);
        for (Row row : rows) {
          printRow(row);
        }
      } catch (IOException e) {
        System.out.println(
            "Unable to initialize service client, as a network error occurred: \n" + e.toString());
      }
    }
    

### Python asyncio

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    from google.cloud.bigtable.data import BigtableDataClientAsync
    from google.cloud.bigtable.data import [ReadRowsQuery](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.read_rows_query.ReadRowsQuery.html)
    from google.cloud.bigtable.data import [RowRange](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.read_rows_query.RowRange.html)
    
    async def read_prefix(project_id, instance_id, table_id):
        async with BigtableDataClientAsync(project=project_id) as client:
            async with client.get_table(instance_id, table_id) as table:
    
                prefix = "phone#"
                end_key = prefix[:-1] + chr(ord(prefix[-1]) + 1)
                prefix_range = RowRange(start_key=prefix, end_key=end_key)
                query = ReadRowsQuery(row_ranges=[prefix_range])
    
                async for row in await table.read_rows_stream(query):
                    print(row)
    

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    def read_prefix(project_id, instance_id, table_id):
        from google.cloud import [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest)
        from google.cloud.bigtable.row_set import [RowSet](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.row_set.RowSet.html)
    
        client = [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html)(project=project_id, admin=True)
        instance = [client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.html).[instance](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html#google_cloud_bigtable_client_Client_instance)(instance_id)
        table = instance.table(table_id)
        prefix = "phone#"
        end_key = prefix[:-1] + chr(ord(prefix[-1]) + 1)
    
        row_set = RowSet()
        [row_set](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.row_set.html).[add_row_range_from_keys](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.row_set.RowSet.html#google_cloud_bigtable_row_set_RowSet_add_row_range_from_keys)(prefix.encode("utf-8"), [end_key](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.read_rows_query.RowRange.html#google_cloud_bigtable_data_read_rows_query_RowRange_end_key).encode("utf-8"))
    
        rows = table.read_rows(row_set=row_set)
        for row in rows:
            print_row(row)
    
    

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    /// <summary>
    /// /// Reads rows starting with a prefix from an existing table.
    ///</summary>
    /// <param name="projectId">Your Google Cloud Project ID.</param>
    /// <param name="instanceId">Your Google Cloud Bigtable Instance ID.</param>
    /// <param name="tableId">Your Google Cloud Bigtable table ID.</param>
    public async Task<string> ReadPrefix(string projectId = "YOUR-PROJECT-ID", string instanceId = "YOUR-INSTANCE-ID", string tableId = "YOUR-TABLE-ID")
    {
        BigtableClient bigtableClient = BigtableClient.Create();
        TableName tableName = new TableName(projectId, instanceId, tableId);
    
        string prefix = "phone";
        char prefixEndChar = prefix[prefix.Length - 1];
        prefixEndChar++;
        string end = prefix.Substring(0, prefix.Length - 1) + prefixEndChar;
        RowSet rowSet = RowSet.FromRowRanges(RowRange.Closed(prefix, end));
        ReadRowsStream readRowsStream = bigtableClient.ReadRows(tableName, rowSet);
    
        string result = "";
        await foreach (var row in readRowsStream)
        {
            result += PrintRow(row);
        }
    
        return result;
    }

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    namespace cbt = ::google::cloud::bigtable;
    using ::google::cloud::StatusOr;
    [](cbt::Table table) {
      // Read and print the rows.
      for (StatusOr<cbt::Row>& row : table.ReadRows(
               cbt::RowRange::Prefix("phone"), cbt::Filter::PassAllFilter())) {
        if (!row) throw std::move(row).status();
        PrintRow(*row);
      }
    }

### Node.js

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    const prefix = 'phone#';
    
    await table
      .createReadStream({
        prefix,
      })
      .on('error', err => {
        // Handle the error.
        console.log(err);
      })
      .on('data', row => printRow(row.id, row.data))
      .on('end', () => {
        // All rows retrieved.
      });

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Bigtable\BigtableClient;
    
    /**
     * Read using a row key prefix
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance
     * @param string $tableId The ID of the table to read from
     */
    function read_prefix(
        string $projectId,
        string $instanceId,
        string $tableId
    ): void {
        // Connect to an existing table with an existing instance.
        $dataClient = new BigtableClient([
            'projectId' => $projectId,
        ]);
        $table = $dataClient->table($instanceId, $tableId);
    
        $prefix = 'phone#';
        $end = $prefix;
        // Increment the last character of the prefix so the filter matches everything in between
        $end[-1] = chr(
            ord($end[-1]) + 1
        );
    
        $rows = $table->readRows([
            'rowRanges' => [
                [
                    'startKeyClosed' => $prefix,
                    'endKeyClosed' => $end,
                ]
            ]
        ]);
    
        foreach ($rows as $key => $row) {
            print_row($key, $row);
        }
    }

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    # instance_id = "my-instance"
    # table_id    = "my-table"
    bigtable = Google::Cloud::[Bigtable](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable.html)
    table = bigtable.table instance_id, table_id
    
    prefix = "phone#"
    end_key = prefix[0...-1] + prefix[-1].next
    range = table.[new_row_range](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-ReadOperations.html).between prefix, end_key
    table.read_rows(ranges: range).[each](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-ColumnFamilyMap.html) do |row|
      print_row row
    end

## Scan in reverse

The following code samples show how to scan in reverse. See the details at [Reverse scans](https://docs.cloud.google.com/bigtable/docs/reads#reverse-scans). To avoid inefficiency, limit a reverse scan to about 50 rows.

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    func readRowsReversed(w io.Writer, projectID, instanceID string, tableName string) error {
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
    	err = tbl.ReadRows(ctx, bigtable.NewRange("phone#5c10102", "phone#5c10103"),
    		func(row bigtable.Row) bool {
    			printRow(w, row)
    			return true
    		},
    		bigtable.ReverseScan())
    	if err != nil {
    		return fmt.Errorf("tbl.ReadRows: %w", err)
    	}
    
    	return nil
    }
    

### HBase

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    /**
     * Example of reading a range of rows in reverse order.
     */
    public static void readRowsReversed() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      readRowsReversed(projectId, instanceId, tableId);
    }
    
    public static void readRowsReversed(String projectId, String instanceId, String tableId) {
      // Initialize client that will be used to send requests. This client only needs to be created
      // once, and can be reused for multiple requests.
      try (Connection connection = BigtableConfiguration.connect(projectId, instanceId)) {
        Table table = connection.getTable(TableName.valueOf(tableId));
        Scan revScan =
            new Scan()
                .setReversed(true)
                .setLimit(2)
                .withStartRow(Bytes.toBytes("phone#4c410523#20190505"));
        ResultScanner rows = table.getScanner(revScan);
    
        for (Result row : rows) {
          printRow(row);
        }
      } catch (IOException e) {
        System.out.println(
            "Unable to initialize service client, as a network error occurred: \n" + e.toString());
      }
    }

### Java

Because this example uses a prefix _and_ start and end row keys, it returns a result from the union of those two filters.

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    public static void readRowsReversed() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      readRowsReversed(projectId, instanceId, tableId);
    }
    
    public static void readRowsReversed(String projectId, String instanceId, String tableId) {
      // Initialize client that will be used to send requests. This client only needs to be created
      // once, and can be reused for multiple requests. After completing all of your requests, call
      // the "close" method on the client to safely clean up any remaining background resources.
      try (BigtableDataClient dataClient = BigtableDataClient.create(projectId, instanceId)) {
        Query query =
            Query.create(TableId.of(tableId))
                .reversed(true)
                .limit(3)
                .prefix("phone#4c410523")
                .range("phone#5c10102", "phone#5c10103");
        ServerStream<Row> rows = dataClient.readRows(query);
        for (Row row : rows) {
          printRow(row);
        }
      } catch (IOException e) {
        System.out.println(
            "Unable to initialize service client, as a network error occurred: \n" + e.toString());
      }
    }
    

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    namespace cbt = ::google::cloud::bigtable;
    using ::google::cloud::Options;
    using ::google::cloud::StatusOr;
    [](cbt::Table table) {
      // Read and print the rows.
      auto reader = table.ReadRows(
          cbt::RowRange::RightOpen("phone#5c10102", "phone#5c10103"), 3,
          cbt::Filter::PassAllFilter(),
          Options{}.set<cbt::ReverseScanOption>(true));
      for (StatusOr<cbt::Row>& row : reader) {
        if (!row) throw std::move(row).status();
        PrintRow(*row);
      }
    }

## Read with filters

The following code samples show how to get **multiple rows** of data using a **row filter**. To learn more about the types of filters that you can use in read requests, see the [overview of filters](https://docs.cloud.google.com/bigtable/docs/filters). Additional [code samples](https://docs.cloud.google.com/bigtable/docs/using-filters) showing how to implement various types of filters in multiple languages are also available.

**Note:** The HBase client for Java uses HBase's filter APIs instead of the Bigtable Data API. To learn about HBase's filter APIs, see the [HBase documentation](https://hbase.apache.org/book.html#client.filter). 

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    func readFilter(w io.Writer, projectID, instanceID string, tableName string) error {
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
    	err = tbl.ReadRows(ctx, bigtable.RowRange{},
    		func(row bigtable.Row) bool {
    			printRow(w, row)
    			return true
    		},
    		bigtable.RowFilter(bigtable.ValueFilter("PQ2A.*$")),
    	)
    	if err != nil {
    		return fmt.Errorf("tbl.ReadRows: %w", err)
    	}
    
    	return nil
    }
    

### HBase

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    /**
     * Example of filtering row contents using filters.
     */
    public static void readFilter() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      readFilter(projectId, instanceId, tableId);
    }
    
    public static void readFilter(String projectId, String instanceId, String tableId) {
      // Initialize client that will be used to send requests. This client only needs to be created
      // once, and can be reused for multiple requests.
      try (Connection connection = BigtableConfiguration.connect(projectId, instanceId)) {
        Table table = connection.getTable(TableName.valueOf(tableId));
    
        ValueFilter valueFilter =
            new ValueFilter(CompareOp.EQUAL, new RegexStringComparator("PQ2A.*"));
        Scan scan = new Scan().setFilter(valueFilter);
    
        ResultScanner rows = table.getScanner(scan);
    
        for (Result row : rows) {
          printRow(row);
        }
      } catch (IOException e) {
        System.out.println(
            "Unable to initialize service client, as a network error occurred: \n" + e.toString());
      }
    }

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    public static void readFilter() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      readFilter(projectId, instanceId, tableId);
    }
    
    public static void readFilter(String projectId, String instanceId, String tableId) {
      Filters.Filter filter = FILTERS.value().regex("PQ2A.*");
    
      // Initialize client that will be used to send requests. This client only needs to be created
      // once, and can be reused for multiple requests. After completing all of your requests, call
      // the "close" method on the client to safely clean up any remaining background resources.
      try (BigtableDataClient dataClient = BigtableDataClient.create(projectId, instanceId)) {
        Query query = Query.create(TableId.of(tableId)).filter(filter);
        ServerStream<Row> rows = dataClient.readRows(query);
        for (Row row : rows) {
          printRow(row);
        }
      } catch (IOException e) {
        System.out.println(
            "Unable to initialize service client, as a network error occurred: \n" + e.toString());
      }
    }
    

### Python asyncio

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    from google.cloud.bigtable.data import BigtableDataClientAsync
    from google.cloud.bigtable.data import [ReadRowsQuery](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.read_rows_query.ReadRowsQuery.html)
    from google.cloud.bigtable.data import [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html)
    
    async def read_with_filter(project_id, instance_id, table_id):
        async with BigtableDataClientAsync(project=project_id) as client:
            async with client.get_table(instance_id, table_id) as table:
    
                row_filter = [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[ValueRegexFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.ValueRegexFilter.html)(b"PQ2A.*$")
                query = ReadRowsQuery(row_filter=row_filter)
    
                async for row in await table.read_rows_stream(query):
                    print(row)
    

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    def read_filter(project_id, instance_id, table_id):
        from google.cloud import [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest)
        from google.cloud.bigtable import row_filters
    
        client = [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html)(project=project_id, admin=True)
        instance = [client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.html).[instance](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html#google_cloud_bigtable_client_Client_instance)(instance_id)
        table = instance.table(table_id)
    
        rows = table.read_rows(filter_=row_filters.ValueRegexFilter(b"PQ2A.*$"))
        for row in rows:
            print_row(row)
    
    

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    /// <summary>
    /// /// Reads using a filter from an existing table.
    ///</summary>
    /// <param name="projectId">Your Google Cloud Project ID.</param>
    /// <param name="instanceId">Your Google Cloud Bigtable Instance ID.</param>
    /// <param name="tableId">Your Google Cloud Bigtable table ID.</param>
    
    public async Task<string> ReadFilter(string projectId = "YOUR-PROJECT-ID", string instanceId = "YOUR-INSTANCE-ID", string tableId = "YOUR-TABLE-ID")
    {
        BigtableClient bigtableClient = BigtableClient.Create();
        TableName tableName = new TableName(projectId, instanceId, tableId);
    
        RowFilter filter = RowFilters.ValueRegex("PQ2A.*");
    
        ReadRowsStream readRowsStream = bigtableClient.ReadRows(tableName, filter: filter);
        string result = "";
        await foreach (var row in readRowsStream)
        {
            result += PrintRow(row);
        }
    
        return result;
    }

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    namespace cbt = ::google::cloud::bigtable;
    using ::google::cloud::StatusOr;
    [](cbt::Table table) {
      // Read and print the rows.
      for (StatusOr<cbt::Row>& row :
           table.ReadRows(cbt::RowRange::InfiniteRange(),
                          cbt::Filter::ValueRegex("PQ2A.*"))) {
        if (!row) throw std::move(row).status();
        PrintRow(*row);
      }
    }

### Node.js

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    const filter = {
      value: /PQ2A.*$/,
    };
    
    await table
      .createReadStream({
        filter,
      })
      .on('error', err => {
        // Handle the error.
        console.log(err);
      })
      .on('data', row => printRow(row.id, row.data))
      .on('end', () => {
        // All rows retrieved.
      });

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Bigtable\BigtableClient;
    use Google\Cloud\Bigtable\Filter;
    
    /**
     * Read using a filter
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance
     * @param string $tableId The ID of the table to read from
     */
    function read_filter(
        string $projectId,
        string $instanceId,
        string $tableId
    ): void {
        // Connect to an existing table with an existing instance.
        $dataClient = new BigtableClient([
            'projectId' => $projectId,
        ]);
        $table = $dataClient->table($instanceId, $tableId);
    
        $rowFilter = Filter::value()->regex('PQ2A.*$');
    
        $rows = $table->readRows([
            'filter' => $rowFilter
        ]);
    
        foreach ($rows as $key => $row) {
            print_row($key, $row);
        }
    }

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    # instance_id = "my-instance"
    # table_id    = "my-table"
    bigtable = Google::Cloud::[Bigtable](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable.html)
    table = bigtable.table instance_id, table_id
    
    filter = Google::Cloud::[Bigtable](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable.html)::[RowFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-RowFilter.html).value "PQ2A.*$"
    table.read_rows(filter: filter).[each](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-ColumnFamilyMap.html) do |row|
      print_row row
    end

## Read from an authorized view

The following examples show how to send a read request to an authorized view. The syntax is similar to reading from a table except you must also provide the authorized view ID.

### Java

This example shows how to read a single row from an authorized view.

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    try {
      System.out.println("\nReading a single row by row key from an authorized view");
      Row row =
          dataClient.readRow(AuthorizedViewId.of(tableId, authorizedViewId), ROW_KEY_PREFIX + 0);
      System.out.println("Row: " + row.getKey().toStringUtf8());
      for (RowCell cell : row.getCells()) {
        System.out.printf(
            "Family: %s    Qualifier: %s    Value: %s%n",
            cell.getFamily(), cell.getQualifier().toStringUtf8(), cell.getValue().toStringUtf8());
      }
      return row;
    } catch (NotFoundException e) {
      System.err.println("Failed to read from a non-existent authorized view: " + e.getMessage());
      return null;
    }

This example shows how to read from an authorized view with a filter.

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    try {
      // A filter that matches only the most recent cell within each column
      Filter filter = FILTERS.limit().cellsPerColumn(1);
      System.out.println("\nScanning authorized view with filter");
      Query query = Query.create(AuthorizedViewId.of(tableId, authorizedViewId)).filter(filter);
      ServerStream<Row> rowStream = dataClient.readRows(query);
      List<Row> authorizedViewRows = new ArrayList<>();
      for (Row r : rowStream) {
        System.out.println("Row Key: " + r.getKey().toStringUtf8());
        authorizedViewRows.add(r);
        for (RowCell cell : r.getCells()) {
          System.out.printf(
              "Family: %s    Qualifier: %s    Value: %s%n",
              cell.getFamily(), cell.getQualifier().toStringUtf8(), cell.getValue().toStringUtf8());
        }
      }
      return authorizedViewRows;
    } catch (NotFoundException e) {
      System.err.println("Failed to read a non-existent authorized view: " + e.getMessage());
      return null;
    }

## What's next

  * [Learn more about reading data.](https://docs.cloud.google.com/bigtable/docs/reads)
  * [Explore the types of filters that you can use.](https://docs.cloud.google.com/bigtable/docs/filters)
  * [Review code samples that show how to implement filters.](https://docs.cloud.google.com/bigtable/docs/using-filters)
  * [Read about Bigtable writes.](https://docs.cloud.google.com/bigtable/docs/writes)
  * [Use the Bigtable emulator.](https://docs.cloud.google.com/bigtable/docs/emulator)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
