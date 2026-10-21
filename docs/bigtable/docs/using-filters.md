---
url: https://docs.cloud.google.com/bigtable/docs/using-filters/
title: Use filters \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:08.277281+00:00
---

# Use filters  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/using-filters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use filters

Bigtable provides the following types of filters:

  * _Limiting filters_, which control which rows or cells are included in the response.
  * _Modifying filters_, which affect the data or metadata for individual cells.
  * _Composing filters_, which allow you to combine multiple filters into one.



This page describes each Bigtable filter in detail and shows how to use each type of filter using the Cloud Client Libraries. Before you read this page, read [Filters](https://docs.cloud.google.com/bigtable/docs/filters).

**Note:** The HBase client for Java uses HBase's filter APIs instead of the Bigtable Data API. To learn about HBase's filter APIs, see the [HBase documentation](https://hbase.apache.org/book.html#client.filter). 

Additional samples showing how to use filters to read multiple rows of data are available on [Reading data](https://docs.cloud.google.com/bigtable/docs/reading-data#reading-filters).

**Warning:** If you don't specify a row key or range of rows for a filter, the filter is applied to _all rows_ in a full table scan. One exception to this is row key regex, which can restrict the row range in certain cases if the regex is a fixed prefix.

## Data for examples

The examples on this page assume that you're storing time-series data for smartphones and tablets, and that the following data has been written to a table. The table has two column families, `stats_summary` and `cell_plan`. Each column family has three columns.

| stats_summary |  |  | cell_plan |  |   
---|---|---|---|---|---|---  
_row key_ | connected_cell | connected_wifi | os_build | data_plan_01gb | data_plan_05gb | data_plan_10gb  
phone#4c410523#20190501  | 1 | 1 | PQ2A.190405.003 | true@time minus one hour  
  
False @time | true |   
phone#4c410523#20190502  | 1 | 1 | PQ2A.190405.004 |  | true |   
phone#4c410523#20190505  | 0 | 1 | PQ2A.190406.000 |  | true |   
phone#5c10102#20190501 | 1 | 1 | PQ2A.190401.002 |  |  | true  
phone#5c10102#20190502 | 1 | 0 | PQ2A.190406.000 |  |  | true  
  
## Limiting filters

The following sections describe each limiting filter. Limiting filters control which rows or cells are included in the response, based on whether they match specific criteria.

When you use a chain to combine multiple limiting filters, keep in mind that the input row for each filter in the chain is the output row from the previous filter in the chain. For example, if you chain two filters, and the first filter outputs only two of the cells from the original row, the second filter sees only those two cells.

### Row selection filters

This section describes the filters that you can use to retrieve rows in a table.

#### Row sample

This filter lets you retrieve a random sample of rows within a given range. Based on a probability that you specify, the filter chooses at random whether the output row should be the same as the input row or whether it should be omitted from the results.

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    func filterLimitRowSample(w io.Writer, projectID, instanceID string, tableName string) error {
    	filter := bigtable.RowSampleFilter(.75)
    	return readWithFilter(w, projectID, instanceID, tableName, filter)
    }
    

### HBase

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    public static void filterLimitRowSample() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      filterLimitRowSample(projectId, instanceId, tableId);
    }
    
    public static void filterLimitRowSample(String projectId, String instanceId, String tableId) {
      // A filter that matches cells from a row with probability .75
      Filter filter = new RandomRowFilter(.75f);
      Scan scan = new Scan().setFilter(filter);
      readWithFilter(projectId, instanceId, tableId, scan);
    }

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    public static void filterLimitRowSample() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      filterLimitRowSample(projectId, instanceId, tableId);
    }
    
    public static void filterLimitRowSample(String projectId, String instanceId, String tableId) {
      // A filter that matches cells from a row with probability .75
      Filter filter = FILTERS.key().sample(.75);
      readFilter(projectId, instanceId, tableId, filter);
    }
    

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    def filter_limit_row_sample(project_id, instance_id, table_id):
        from google.cloud import [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest)
        from google.cloud.bigtable import row_filters
    
        client = [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html)(project=project_id, admin=True)
        instance = [client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.html).[instance](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html#google_cloud_bigtable_client_Client_instance)(instance_id)
        table = instance.table(table_id)
    
        rows = table.read_rows(filter_=row_filters.RowSampleFilter(0.75))
        for row in rows:
            print_row(row)
    
    

### Python asyncio

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    async def filter_limit_row_sample(project_id, instance_id, table_id):
        from google.cloud.bigtable.data import (
            BigtableDataClientAsync,
            [ReadRowsQuery](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.read_rows_query.ReadRowsQuery.html),
            [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html),
        )
    
        query = ReadRowsQuery(row_filter=[row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[RowSampleFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.RowSampleFilter.html)(0.75))
    
        async with BigtableDataClientAsync(project=project_id) as client:
            async with client.get_table(instance_id, table_id) as table:
                for row in await table.read_rows(query):
                    print_row(row)
    
    

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    /// <summary>
    /// /// Read using a row sample filter from an existing table.
    ///</summary>
    /// <param name="projectId">Your Google Cloud Project ID.</param>
    /// <param name="instanceId">Your Google Cloud Bigtable Instance ID.</param>
    /// <param name="tableId">Your Google Cloud Bigtable table ID.</param>
    
    public Task<string> FilterLimitRowSample(string projectId = "YOUR-PROJECT-ID", string instanceId = "YOUR-INSTANCE-ID", string tableId = "YOUR-TABLE-ID")
    {
        // A filter that matches cells from a row with probability .75
        RowFilter filter = RowFilters.RowSample(.75);
        return ReadFilter(projectId, instanceId, tableId, filter);
    }

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    namespace cbt = ::google::cloud::bigtable;
    using ::google::cloud::StatusOr;
    [](cbt::Table table) {
      // Filter the results, only include rows with a given probability
      cbt::Filter filter = cbt::Filter::RowSample(0.75);
    
      // Read and print the rows.
      for (StatusOr<cbt::Row>& row :
           table.ReadRows(cbt::RowSet(cbt::RowRange::InfiniteRange()), filter)) {
        if (!row) throw std::move(row).status();
        std::cout << row->row_key() << " = ";
        for (auto const& cell : row->cells()) {
          std::cout << "[" << cell.family_name() << ", "
                    << cell.column_qualifier() << ", " << cell.value() << "],";
        }
        std::cout << "\n";
      }
    }

### Node.js

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    const filter = {
      row: {
        sample: 0.75,
      },
    };
    readWithFilter(filter);

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Bigtable\BigtableClient;
    use Google\Cloud\Bigtable\Filter;
    
    /**
     * Create a limiting filter on rows using a random sampling
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance
     * @param string $tableId The ID of the table to read from
     */
    function filter_limit_row_sample(
        string $projectId,
        string $instanceId,
        string $tableId
    ): void {
        // Connect to an existing table with an existing instance.
        $dataClient = new BigtableClient([
            'projectId' => $projectId,
        ]);
        $table = $dataClient->table($instanceId, $tableId);
    
        $filter = Filter::key()->sample(.75);
    
        $rows = $table->readRows([
            'filter' => $filter
        ]);
    
        foreach ($rows as $key => $row) {
            // The "print_row" helper function is defined in https://cloud.google.com/bigtable/docs/samples/bigtable-reads-print
            print_row($key, $row);
        }
    }

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    # instance_id = "my-instance"
    # table_id    = "my-table"
    filter = Google::Cloud::Bigtable::RowFilter.sample 0.75
    read_with_filter instance_id, table_id, filter

#### Row key regex

This filter checks whether the input row's row key matches a regular expression. The regular expression must use [RE2 syntax](https://github.com/google/re2/wiki/Syntax). Because row keys can contain arbitrary bytes, use `\C` as the wildcard expression instead of the `.` expression to match any character, including newlines.

To improve performance, Bigtable attempts to optimize the filter by extracting a literal prefix from the start of the regular expression. If a prefix is identified, Bigtable narrows its search to the key range that begins with that prefix, avoiding a full table scan.

This optimization only occurs under the following conditions:

  * The prefix can only contain alphanumeric characters and the following unescaped symbols: `-`, `_`, `:`, `,`.
  * The prefix extraction stops at the first unescaped character that is not in the allowed set. For example, common key separators such as a hash (`#`) or regular expression metacharacters, such as an unescaped period (`.`), stop the extraction. To include special characters in the optimized prefix, escape them with a backslash (`\`) or use RE2 client library functions such as [`RE2.quoteMeta`](https://github.com/google/re2j/blob/84237cbbd0fbd637c6eb6856717c1e248daae729/java/com/google/re2j/RE2.java#L495) in Java.
  * A pipe character (`|`) is not supported.



If your regular expression can't be resolved to a literal prefix—for example, if it begins with a wildcard or searches for a substring, Bigtable requires a full table scan.

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    func filterLimitRowRegex(w io.Writer, projectID, instanceID string, tableName string) error {
    	filter := bigtable.RowKeyFilter(".*#20190501$")
    	return readWithFilter(w, projectID, instanceID, tableName, filter)
    }
    

### HBase

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    public static void filterLimitRowRegex() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      filterLimitRowRegex(projectId, instanceId, tableId);
    }
    
    public static void filterLimitRowRegex(String projectId, String instanceId, String tableId) {
      // A filter that matches cells from rows whose keys satisfy the given regex
      Filter filter = new RowFilter(CompareOp.EQUAL, new RegexStringComparator(".*#20190501$"));
      Scan scan = new Scan().setFilter(filter).setMaxVersions();
      readWithFilter(projectId, instanceId, tableId, scan);
    }

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    public static void filterLimitRowRegex() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      filterLimitRowRegex(projectId, instanceId, tableId);
    }
    
    public static void filterLimitRowRegex(String projectId, String instanceId, String tableId) {
      // A filter that matches cells from rows whose keys satisfy the given regex
      Filter filter = FILTERS.key().regex(".*#20190501$");
      readFilter(projectId, instanceId, tableId, filter);
    }
    

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    def filter_limit_row_regex(project_id, instance_id, table_id):
        from google.cloud import [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest)
        from google.cloud.bigtable import row_filters
    
        client = [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html)(project=project_id, admin=True)
        instance = [client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.html).[instance](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html#google_cloud_bigtable_client_Client_instance)(instance_id)
        table = instance.table(table_id)
    
        rows = table.read_rows(
            filter_=row_filters.RowKeyRegexFilter(".*#20190501$".encode("utf-8"))
        )
        for row in rows:
            print_row(row)
    
    

### Python asyncio

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    async def filter_limit_row_regex(project_id, instance_id, table_id):
        from google.cloud.bigtable.data import (
            BigtableDataClientAsync,
            [ReadRowsQuery](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.read_rows_query.ReadRowsQuery.html),
            [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html),
        )
    
        query = ReadRowsQuery(
            row_filter=[row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[RowKeyRegexFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.RowKeyRegexFilter.html)(".*#20190501$".encode("utf-8"))
        )
    
        async with BigtableDataClientAsync(project=project_id) as client:
            async with client.get_table(instance_id, table_id) as table:
                for row in await table.read_rows(query):
                    print_row(row)
    
    

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    /// <summary>
    /// /// Read using a row regex filter from an existing table.
    ///</summary>
    /// <param name="projectId">Your Google Cloud Project ID.</param>
    /// <param name="instanceId">Your Google Cloud Bigtable Instance ID.</param>
    /// <param name="tableId">Your Google Cloud Bigtable table ID.</param>
    
    public Task<string> FilterLimitRowRegex(string projectId = "YOUR-PROJECT-ID", string instanceId = "YOUR-INSTANCE-ID", string tableId = "YOUR-TABLE-ID")
    {
        // A filter that matches cells from rows whose keys satisfy the given regex
        RowFilter filter = RowFilters.RowKeyRegex(".*#20190501$");
        return ReadFilter(projectId, instanceId, tableId, filter);
    }

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    namespace cbt = ::google::cloud::bigtable;
    using ::google::cloud::StatusOr;
    [](cbt::Table table) {
      // Filter the results, only include rows where row_key matches given regular
      // expression
      cbt::Filter filter = cbt::Filter::RowKeysRegex(".*#20190501$");
      // Read and print the rows.
      for (StatusOr<cbt::Row>& row :
           table.ReadRows(cbt::RowSet(cbt::RowRange::InfiniteRange()), filter)) {
        if (!row) throw std::move(row).status();
        std::cout << row->row_key() << " = ";
        for (auto const& cell : row->cells()) {
          std::cout << "[" << cell.family_name() << ", "
                    << cell.column_qualifier() << ", " << cell.value() << "],";
        }
        std::cout << "\n";
      }
    }

### Node.js

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    const filter = {
      row: /.*#20190501$/,
    };
    readWithFilter(filter);

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Bigtable\BigtableClient;
    use Google\Cloud\Bigtable\Filter;
    
    /**
     * Create a limiting filter on a cell value using a regex
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance
     * @param string $tableId The ID of the table to read from
     */
    function filter_limit_row_regex(
        string $projectId,
        string $instanceId,
        string $tableId
    ): void {
        // Connect to an existing table with an existing instance.
        $dataClient = new BigtableClient([
            'projectId' => $projectId,
        ]);
        $table = $dataClient->table($instanceId, $tableId);
    
        $filter = Filter::key()->regex('.*#20190501$');
    
        $rows = $table->readRows([
            'filter' => $filter
        ]);
    
        foreach ($rows as $key => $row) {
            // The "print_row" helper function is defined in https://cloud.google.com/bigtable/docs/samples/bigtable-reads-print
            print_row($key, $row);
        }
    }

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    # instance_id = "my-instance"
    # table_id    = "my-table"
    filter = Google::Cloud::Bigtable::RowFilter.key ".*#20190501$"
    read_with_filter instance_id, table_id, filter

### Cell selection filters

This section describes the filters that you can use to retrieve cells in a table.

#### Cells per column limit

This filter limits the number of cells in each column that are included in the output row. When this filter is applied, each output row includes the _N_ most recent cells from each column and omits all other cells from that column.

If you are also using an interleave filter and the interleave filter produces duplicate copies of a cell, each copy counts towards the limit.

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    func filterLimitCellsPerCol(w io.Writer, projectID, instanceID string, tableName string) error {
    	filter := bigtable.LatestNFilter(2)
    	return readWithFilter(w, projectID, instanceID, tableName, filter)
    }
    

### HBase

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    public static void filterLimitCellsPerCol() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      filterLimitCellsPerCol(projectId, instanceId, tableId);
    }
    
    public static void filterLimitCellsPerCol(String projectId, String instanceId, String tableId) {
      // A filter that matches only the most recent 2 cells within each column
      Scan scan = new Scan().setMaxVersions(2);
      readWithFilter(projectId, instanceId, tableId, scan);
    }

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    public static void filterLimitCellsPerCol() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      filterLimitCellsPerCol(projectId, instanceId, tableId);
    }
    
    public static void filterLimitCellsPerCol(String projectId, String instanceId, String tableId) {
      // A filter that matches only the most recent 2 cells within each column
      Filter filter = FILTERS.limit().cellsPerColumn(2);
      readFilter(projectId, instanceId, tableId, filter);
    }
    

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    def filter_limit_cells_per_col(project_id, instance_id, table_id):
        from google.cloud import [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest)
        from google.cloud.bigtable import row_filters
    
        client = [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html)(project=project_id, admin=True)
        instance = [client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.html).[instance](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html#google_cloud_bigtable_client_Client_instance)(instance_id)
        table = instance.table(table_id)
    
        rows = table.read_rows(filter_=row_filters.CellsColumnLimitFilter(2))
        for row in rows:
            print_row(row)
    
    

### Python ayncio

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    # Copyright 2024, Google LLC
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #    http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    
    async def filter_limit_row_sample(project_id, instance_id, table_id):
        from google.cloud.bigtable.data import (
            BigtableDataClientAsync,
            [ReadRowsQuery](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.read_rows_query.ReadRowsQuery.html),
            [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html),
        )
    
        query = ReadRowsQuery(row_filter=[row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[RowSampleFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.RowSampleFilter.html)(0.75))
    
        async with BigtableDataClientAsync(project=project_id) as client:
            async with client.get_table(instance_id, table_id) as table:
                for row in await table.read_rows(query):
                    print_row(row)
    
    
    async def filter_limit_row_regex(project_id, instance_id, table_id):
        from google.cloud.bigtable.data import (
            BigtableDataClientAsync,
            [ReadRowsQuery](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.read_rows_query.ReadRowsQuery.html),
            [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html),
        )
    
        query = ReadRowsQuery(
            row_filter=[row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[RowKeyRegexFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.RowKeyRegexFilter.html)(".*#20190501$".encode("utf-8"))
        )
    
        async with BigtableDataClientAsync(project=project_id) as client:
            async with client.get_table(instance_id, table_id) as table:
                for row in await table.read_rows(query):
                    print_row(row)
    
    
    async def filter_limit_cells_per_col(project_id, instance_id, table_id):
        from google.cloud.bigtable.data import (
            BigtableDataClientAsync,
            [ReadRowsQuery](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.read_rows_query.ReadRowsQuery.html),
            [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html),
        )
    
        query = ReadRowsQuery(row_filter=[row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[CellsColumnLimitFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.CellsColumnLimitFilter.html)(2))
    
        async with BigtableDataClientAsync(project=project_id) as client:
            async with client.get_table(instance_id, table_id) as table:
                for row in await table.read_rows(query):
                    print_row(row)
    
    
    async def filter_limit_cells_per_row(project_id, instance_id, table_id):
        from google.cloud.bigtable.data import (
            BigtableDataClientAsync,
            [ReadRowsQuery](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.read_rows_query.ReadRowsQuery.html),
            [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html),
        )
    
        query = ReadRowsQuery(row_filter=[row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[CellsRowLimitFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.CellsRowLimitFilter.html)(2))
    
        async with BigtableDataClientAsync(project=project_id) as client:
            async with client.get_table(instance_id, table_id) as table:
                for row in await table.read_rows(query):
                    print_row(row)
    
    
    async def filter_limit_cells_per_row_offset(project_id, instance_id, table_id):
        from google.cloud.bigtable.data import (
            BigtableDataClientAsync,
            [ReadRowsQuery](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.read_rows_query.ReadRowsQuery.html),
            [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html),
        )
    
        query = ReadRowsQuery(row_filter=[row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[CellsRowOffsetFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.CellsRowOffsetFilter.html)(2))
    
        async with BigtableDataClientAsync(project=project_id) as client:
            async with client.get_table(instance_id, table_id) as table:
                for row in await table.read_rows(query):
                    print_row(row)
    
    
    async def filter_limit_col_family_regex(project_id, instance_id, table_id):
        from google.cloud.bigtable.data import (
            BigtableDataClientAsync,
            [ReadRowsQuery](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.read_rows_query.ReadRowsQuery.html),
            [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html),
        )
    
        query = ReadRowsQuery(
            row_filter=[row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[FamilyNameRegexFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.FamilyNameRegexFilter.html)("stats_.*$".encode("utf-8"))
        )
    
        async with BigtableDataClientAsync(project=project_id) as client:
            async with client.get_table(instance_id, table_id) as table:
                for row in await table.read_rows(query):
                    print_row(row)
    
    
    async def filter_limit_col_qualifier_regex(project_id, instance_id, table_id):
        from google.cloud.bigtable.data import (
            BigtableDataClientAsync,
            [ReadRowsQuery](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.read_rows_query.ReadRowsQuery.html),
            [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html),
        )
    
        query = ReadRowsQuery(
            row_filter=[row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[ColumnQualifierRegexFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.ColumnQualifierRegexFilter.html)(
                "connected_.*$".encode("utf-8")
            )
        )
    
        async with BigtableDataClientAsync(project=project_id) as client:
            async with client.get_table(instance_id, table_id) as table:
                for row in await table.read_rows(query):
                    print_row(row)
    
    
    async def filter_limit_col_range(project_id, instance_id, table_id):
        from google.cloud.bigtable.data import (
            BigtableDataClientAsync,
            [ReadRowsQuery](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.read_rows_query.ReadRowsQuery.html),
            [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html),
        )
    
        query = ReadRowsQuery(
            row_filter=[row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[ColumnRangeFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.ColumnRangeFilter.html)(
                "cell_plan", b"data_plan_01gb", b"data_plan_10gb", inclusive_end=False
            )
        )
    
        async with BigtableDataClientAsync(project=project_id) as client:
            async with client.get_table(instance_id, table_id) as table:
                for row in await table.read_rows(query):
                    print_row(row)
    
    
    async def filter_limit_value_range(project_id, instance_id, table_id):
        from google.cloud.bigtable.data import (
            BigtableDataClientAsync,
            [ReadRowsQuery](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.read_rows_query.ReadRowsQuery.html),
            [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html),
        )
    
        query = ReadRowsQuery(
            row_filter=[row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[ValueRangeFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.ValueRangeFilter.html)(b"PQ2A.190405", b"PQ2A.190406")
        )
    
        async with BigtableDataClientAsync(project=project_id) as client:
            async with client.get_table(instance_id, table_id) as table:
                for row in await table.read_rows(query):
                    print_row(row)
    
    
    
    
    async def filter_limit_value_regex(project_id, instance_id, table_id):
        from google.cloud.bigtable.data import (
            BigtableDataClientAsync,
            [ReadRowsQuery](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.read_rows_query.ReadRowsQuery.html),
            [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html),
        )
    
        query = ReadRowsQuery(
            row_filter=[row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[ValueRegexFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.ValueRegexFilter.html)("PQ2A.*$".encode("utf-8"))
        )
    
        async with BigtableDataClientAsync(project=project_id) as client:
            async with client.get_table(instance_id, table_id) as table:
                for row in await table.read_rows(query):
                    print_row(row)
    
    
    async def filter_limit_timestamp_range(project_id, instance_id, table_id):
        import datetime
    
        from google.cloud.bigtable.data import (
            BigtableDataClientAsync,
            [ReadRowsQuery](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.read_rows_query.ReadRowsQuery.html),
            [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html),
        )
    
        end = datetime.datetime(2019, 5, 1)
    
        query = ReadRowsQuery(row_filter=[row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[TimestampRangeFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.TimestampRangeFilter.html)(end=end))
    
        async with BigtableDataClientAsync(project=project_id) as client:
            async with client.get_table(instance_id, table_id) as table:
                for row in await table.read_rows(query):
                    print_row(row)
    
    
    async def filter_limit_block_all(project_id, instance_id, table_id):
        from google.cloud.bigtable.data import (
            BigtableDataClientAsync,
            [ReadRowsQuery](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.read_rows_query.ReadRowsQuery.html),
            [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html),
        )
    
        query = ReadRowsQuery(row_filter=[row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[BlockAllFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.BlockAllFilter.html)(True))
    
        async with BigtableDataClientAsync(project=project_id) as client:
            async with client.get_table(instance_id, table_id) as table:
                for row in await table.read_rows(query):
                    print_row(row)
    
    
    async def filter_limit_pass_all(project_id, instance_id, table_id):
        from google.cloud.bigtable.data import (
            BigtableDataClientAsync,
            [ReadRowsQuery](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.read_rows_query.ReadRowsQuery.html),
            [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html),
        )
    
        query = ReadRowsQuery(row_filter=[row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[PassAllFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.PassAllFilter.html)(True))
    
        async with BigtableDataClientAsync(project=project_id) as client:
            async with client.get_table(instance_id, table_id) as table:
                for row in await table.read_rows(query):
                    print_row(row)
    
    
    async def filter_modify_strip_value(project_id, instance_id, table_id):
        from google.cloud.bigtable.data import (
            BigtableDataClientAsync,
            [ReadRowsQuery](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.read_rows_query.ReadRowsQuery.html),
            [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html),
        )
    
        query = ReadRowsQuery(row_filter=[row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[StripValueTransformerFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.StripValueTransformerFilter.html)(True))
    
        async with BigtableDataClientAsync(project=project_id) as client:
            async with client.get_table(instance_id, table_id) as table:
                for row in await table.read_rows(query):
                    print_row(row)
    
    
    async def filter_modify_apply_label(project_id, instance_id, table_id):
        from google.cloud.bigtable.data import (
            BigtableDataClientAsync,
            [ReadRowsQuery](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.read_rows_query.ReadRowsQuery.html),
            [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html),
        )
    
        query = ReadRowsQuery(row_filter=[row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[ApplyLabelFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.ApplyLabelFilter.html)(label="labelled"))
    
        async with BigtableDataClientAsync(project=project_id) as client:
            async with client.get_table(instance_id, table_id) as table:
                for row in await table.read_rows(query):
                    print_row(row)
    
    
    async def filter_composing_chain(project_id, instance_id, table_id):
        from google.cloud.bigtable.data import (
            BigtableDataClientAsync,
            [ReadRowsQuery](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.read_rows_query.ReadRowsQuery.html),
            [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html),
        )
    
        query = ReadRowsQuery(
            row_filter=[row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[RowFilterChain](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.RowFilterChain.html)(
                filters=[
                    [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[CellsColumnLimitFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.CellsColumnLimitFilter.html)(1),
                    [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[FamilyNameRegexFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.FamilyNameRegexFilter.html)("cell_plan"),
                ]
            )
        )
    
        async with BigtableDataClientAsync(project=project_id) as client:
            async with client.get_table(instance_id, table_id) as table:
                for row in await table.read_rows(query):
                    print_row(row)
    
    
    async def filter_composing_interleave(project_id, instance_id, table_id):
        from google.cloud.bigtable.data import (
            BigtableDataClientAsync,
            [ReadRowsQuery](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.read_rows_query.ReadRowsQuery.html),
            [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html),
        )
    
        query = ReadRowsQuery(
            row_filter=[row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[RowFilterUnion](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.RowFilterUnion.html)(
                filters=[
                    [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[ValueRegexFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.ValueRegexFilter.html)("true"),
                    [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[ColumnQualifierRegexFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.ColumnQualifierRegexFilter.html)("os_build"),
                ]
            )
        )
    
        async with BigtableDataClientAsync(project=project_id) as client:
            async with client.get_table(instance_id, table_id) as table:
                for row in await table.read_rows(query):
                    print_row(row)
    
    
    async def filter_composing_condition(project_id, instance_id, table_id):
        from google.cloud.bigtable.data import (
            BigtableDataClientAsync,
            [ReadRowsQuery](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.read_rows_query.ReadRowsQuery.html),
            [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html),
        )
    
        query = ReadRowsQuery(
            row_filter=[row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[ConditionalRowFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.ConditionalRowFilter.html)(
                predicate_filter=[row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[RowFilterChain](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.RowFilterChain.html)(
                    filters=[
                        [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[ColumnQualifierRegexFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.ColumnQualifierRegexFilter.html)("data_plan_10gb"),
                        [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[ValueRegexFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.ValueRegexFilter.html)("true"),
                    ]
                ),
                true_filter=[row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[ApplyLabelFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.ApplyLabelFilter.html)(label="passed-filter"),
                false_filter=[row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[ApplyLabelFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.ApplyLabelFilter.html)(label="filtered-out"),
            )
        )
    
        async with BigtableDataClientAsync(project=project_id) as client:
            async with client.get_table(instance_id, table_id) as table:
                for row in await table.read_rows(query):
                    print_row(row)
    
    
    
    
    def print_row(row):
        from google.cloud._helpers import _datetime_from_microseconds
    
        print("Reading data for {}:".format([row](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row.html).row_key.decode("utf-8")))
        last_family = None
        for cell in [row](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row.html).cells:
            if last_family != cell.family:
                print("Column Family {}".format(cell.family))
                last_family = cell.family
    
            labels = " [{}]".format(",".join(cell.labels)) if len(cell.labels) else ""
            print(
                "\t{}: {} @{}{}".format(
                    cell.qualifier.decode("utf-8"),
                    cell.value.decode("utf-8"),
                    _datetime_from_microseconds(cell.timestamp_micros),
                    labels,
                )
            )
        print("")
    

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    /// <summary>
    /// /// Read using a cells per column filter from an existing table.
    ///</summary>
    /// <param name="projectId">Your Google Cloud Project ID.</param>
    /// <param name="instanceId">Your Google Cloud Bigtable Instance ID.</param>
    /// <param name="tableId">Your Google Cloud Bigtable table ID.</param>
    
    public Task<string> FilterLimitCellsPerCol(string projectId = "YOUR-PROJECT-ID", string instanceId = "YOUR-INSTANCE-ID", string tableId = "YOUR-TABLE-ID")
    {
        // A filter that matches only the most recent 2 cells within each column
        RowFilter filter = RowFilters.CellsPerColumnLimit(2);
        return ReadFilter(projectId, instanceId, tableId, filter);
    }

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    namespace cbt = ::google::cloud::bigtable;
    using ::google::cloud::StatusOr;
    [](cbt::Table table) {
      // Filter the results, only include limited cells
      cbt::Filter filter = cbt::Filter::Latest(2);
      // Read and print the rows.
      for (StatusOr<cbt::Row>& row :
           table.ReadRows(cbt::RowSet(cbt::RowRange::InfiniteRange()), filter)) {
        if (!row) throw std::move(row).status();
        std::cout << row->row_key() << " = ";
        for (auto const& cell : row->cells()) {
          std::cout << "[" << cell.family_name() << ", "
                    << cell.column_qualifier() << ", " << cell.value() << "],";
        }
        std::cout << "\n";
      }
    }

### Node.js

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    const filter = {
      column: {
        cellLimit: 2,
      },
    };
    readWithFilter(filter);

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Bigtable\BigtableClient;
    use Google\Cloud\Bigtable\Filter;
    
    /**
     * Create a limiting filter on cells per column
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance
     * @param string $tableId The ID of the table to read from
     */
    function filter_limit_cells_per_col(
        string $projectId,
        string $instanceId,
        string $tableId
    ): void {
        // Connect to an existing table with an existing instance.
        $dataClient = new BigtableClient([
            'projectId' => $projectId,
        ]);
        $table = $dataClient->table($instanceId, $tableId);
    
        $filter = Filter::limit()->cellsPerColumn(2);
    
        $rows = $table->readRows([
            'filter' => $filter
        ]);
    
        foreach ($rows as $key => $row) {
            // The "print_row" helper function is defined in https://cloud.google.com/bigtable/docs/samples/bigtable-reads-print
            print_row($key, $row);
        }
    }

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    # instance_id = "my-instance"
    # table_id    = "my-table"
    filter = Google::Cloud::Bigtable::RowFilter.cells_per_column 2
    read_with_filter instance_id, table_id, filter

#### Cells per row limit

This filter limits the number of cells in each output row. When this filter is applied, each output row includes the first _N_ cells from the input row and omits all of the following cells from that row. The first _N_ cells are read regardless of which column they are in, in the order in which they are stored in Bigtable.

To learn more about how data is stored in Bigtable, see [Schema design best practices](https://docs.cloud.google.com/bigtable/docs/schema-design).

A column in a row can contain multiple cells. Each cell contains a value for the column and a unique timestamp. As a result, limiting a row to _N_ cells might differ from retrieving the first _N_ columns from the row. For example, if you use a filter with a cell per row limit of 20 to read a row that has 30 columns, and each column has 10 timestamped cells, the output row returns values from only the first two columns in the row (2 * 10 = 20).

**Note:** If you are also using an interleave filter, and the interleave filter produces duplicate copies of a cell, each copy counts towards the limit.

Using this filter in combination with an offset filter is useful for pagination if you need to [read a large row](https://docs.cloud.google.com/bigtable/docs/reads#large-rows).

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    func filterLimitCellsPerRow(w io.Writer, projectID, instanceID string, tableName string) error {
    	filter := bigtable.CellsPerRowLimitFilter(2)
    	return readWithFilter(w, projectID, instanceID, tableName, filter)
    }
    

### HBase

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    public static void filterLimitCellsPerRow() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      filterLimitCellsPerRow(projectId, instanceId, tableId);
    }
    
    public static void filterLimitCellsPerRow(String projectId, String instanceId, String tableId) {
      // A filter that matches the first 2 cells of each row
      //    Filter filter = new ColumnCountGetFilter(2);
      Filter filter = new ColumnPaginationFilter(2, 0);
    
      Scan scan = new Scan().setFilter(filter);
      readWithFilter(projectId, instanceId, tableId, scan);
    }

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    public static void filterLimitCellsPerRow() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      filterLimitCellsPerRow(projectId, instanceId, tableId);
    }
    
    public static void filterLimitCellsPerRow(String projectId, String instanceId, String tableId) {
      // A filter that matches the first 2 cells of each row
      Filter filter = FILTERS.limit().cellsPerRow(2);
      readFilter(projectId, instanceId, tableId, filter);
    }
    

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    def filter_limit_cells_per_row(project_id, instance_id, table_id):
        from google.cloud import [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest)
        from google.cloud.bigtable import row_filters
    
        client = [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html)(project=project_id, admin=True)
        instance = [client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.html).[instance](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html#google_cloud_bigtable_client_Client_instance)(instance_id)
        table = instance.table(table_id)
    
        rows = table.read_rows(filter_=row_filters.CellsRowLimitFilter(2))
        for row in rows:
            print_row(row)
    
    

### Python asyncio

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    async def filter_limit_cells_per_row(project_id, instance_id, table_id):
        from google.cloud.bigtable.data import (
            BigtableDataClientAsync,
            [ReadRowsQuery](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.read_rows_query.ReadRowsQuery.html),
            [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html),
        )
    
        query = ReadRowsQuery(row_filter=[row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[CellsRowLimitFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.CellsRowLimitFilter.html)(2))
    
        async with BigtableDataClientAsync(project=project_id) as client:
            async with client.get_table(instance_id, table_id) as table:
                for row in await table.read_rows(query):
                    print_row(row)
    
    

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    /// <summary>
    /// /// Read using a cells per row filter from an existing table.
    ///</summary>
    /// <param name="projectId">Your Google Cloud Project ID.</param>
    /// <param name="instanceId">Your Google Cloud Bigtable Instance ID.</param>
    /// <param name="tableId">Your Google Cloud Bigtable table ID.</param>
    
    public Task<string> FilterLimitCellsPerRow(string projectId = "YOUR-PROJECT-ID", string instanceId = "YOUR-INSTANCE-ID", string tableId = "YOUR-TABLE-ID")
    {
        // A filter that matches the first 2 cells of each row
        RowFilter filter = RowFilters.CellsPerRowLimit(2);
        return ReadFilter(projectId, instanceId, tableId, filter);
    }

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    namespace cbt = ::google::cloud::bigtable;
    using ::google::cloud::StatusOr;
    [](cbt::Table table) {
      // Filter the results, only include limited cells per row
      cbt::Filter filter = cbt::Filter::CellsRowLimit(2);
      // Read and print the rows.
      for (StatusOr<cbt::Row>& row :
           table.ReadRows(cbt::RowSet(cbt::RowRange::InfiniteRange()), filter)) {
        if (!row) throw std::move(row).status();
        std::cout << row->row_key() << " = ";
        for (auto const& cell : row->cells()) {
          std::cout << "[" << cell.family_name() << ", "
                    << cell.column_qualifier() << ", " << cell.value() << "],";
        }
        std::cout << "\n";
      }
    }

### Node.js

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    const filter = {
      row: {
        cellLimit: 2,
      },
    };
    readWithFilter(filter);

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Bigtable\BigtableClient;
    use Google\Cloud\Bigtable\Filter;
    
    /**
     * Create a limiting filter on cells per row
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance
     * @param string $tableId The ID of the table to read from
     */
    function filter_limit_cells_per_row(
        string $projectId,
        string $instanceId,
        string $tableId
    ): void {
        // Connect to an existing table with an existing instance.
        $dataClient = new BigtableClient([
            'projectId' => $projectId,
        ]);
        $table = $dataClient->table($instanceId, $tableId);
    
        $filter = Filter::limit()->cellsPerRow(2);
    
        $rows = $table->readRows([
            'filter' => $filter
        ]);
    
        foreach ($rows as $key => $row) {
            // The "print_row" helper function is defined in https://cloud.google.com/bigtable/docs/samples/bigtable-reads-print
            print_row($key, $row);
        }
    }

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    # instance_id = "my-instance"
    # table_id    = "my-table"
    filter = Google::Cloud::Bigtable::RowFilter.cells_per_row 2
    read_with_filter instance_id, table_id, filter

#### Cells per row offset

This filter omits the first _N_ cells from each output row. All of the remaining cells are included in the output row. The first _N_ cells are skipped regardless of which column they are in.

A column in a row can contain multiple cells. Each cell contains a value for the column and a unique timestamp. As a result, skipping the first _N_ cells from a row might differ from skipping the first _N_ columns in the row. For example, if you use a filter with a cell per row offset of 20 to read a row that has 30 columns, and each column has 10 timestamped cells, the output row returns values all cells in the row except for those in the first two columns (2 * 10 = 20).

If you are also using an interleave filter, and the interleave filter produces duplicate copies of a cell, each copy counts towards the offset.

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    func filterLimitCellsPerRowOffset(w io.Writer, projectID, instanceID string, tableName string) error {
    	filter := bigtable.CellsPerRowOffsetFilter(2)
    	return readWithFilter(w, projectID, instanceID, tableName, filter)
    }
    

### HBase

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    public static void filterLimitCellsPerRowOffset() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      filterLimitCellsPerRowOffset(projectId, instanceId, tableId);
    }
    
    public static void filterLimitCellsPerRowOffset(
        String projectId, String instanceId, String tableId) {
      // A filter that skips the first 2 cells per row
      Filter filter = new ColumnPaginationFilter(Integer.MAX_VALUE, 2);
      Scan scan = new Scan().setFilter(filter);
      readWithFilter(projectId, instanceId, tableId, scan);
    }

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    public static void filterLimitCellsPerRowOffset() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      filterLimitCellsPerRowOffset(projectId, instanceId, tableId);
    }
    
    public static void filterLimitCellsPerRowOffset(
        String projectId, String instanceId, String tableId) {
      // A filter that skips the first 2 cells per row
      Filter filter = FILTERS.offset().cellsPerRow(2);
      readFilter(projectId, instanceId, tableId, filter);
    }
    

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    def filter_limit_cells_per_row_offset(project_id, instance_id, table_id):
        from google.cloud import [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest)
        from google.cloud.bigtable import row_filters
    
        client = [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html)(project=project_id, admin=True)
        instance = [client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.html).[instance](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html#google_cloud_bigtable_client_Client_instance)(instance_id)
        table = instance.table(table_id)
    
        rows = table.read_rows(filter_=row_filters.CellsRowOffsetFilter(2))
        for row in rows:
            print_row(row)
    
    

### Python asyncio

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    async def filter_limit_cells_per_row_offset(project_id, instance_id, table_id):
        from google.cloud.bigtable.data import (
            BigtableDataClientAsync,
            [ReadRowsQuery](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.read_rows_query.ReadRowsQuery.html),
            [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html),
        )
    
        query = ReadRowsQuery(row_filter=[row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[CellsRowOffsetFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.CellsRowOffsetFilter.html)(2))
    
        async with BigtableDataClientAsync(project=project_id) as client:
            async with client.get_table(instance_id, table_id) as table:
                for row in await table.read_rows(query):
                    print_row(row)
    
    

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    /// <summary>
    /// /// Read using a cells per row offset filter from an existing table.
    ///</summary>
    /// <param name="projectId">Your Google Cloud Project ID.</param>
    /// <param name="instanceId">Your Google Cloud Bigtable Instance ID.</param>
    /// <param name="tableId">Your Google Cloud Bigtable table ID.</param>
    
    public Task<string> FilterLimitCellsPerRowOffset(string projectId, string instanceId, string tableId)
    {
        // A filter that skips the first 2 cells per row
        RowFilter filter = RowFilters.CellsPerRowOffset(2);
        return ReadFilter(projectId, instanceId, tableId, filter);
    }

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    namespace cbt = ::google::cloud::bigtable;
    using ::google::cloud::StatusOr;
    [](cbt::Table table) {
      cbt::Filter filter = cbt::Filter::CellsRowOffset(2);
      // Read and print the rows.
      for (StatusOr<cbt::Row>& row :
           table.ReadRows(cbt::RowSet(cbt::RowRange::InfiniteRange()), filter)) {
        if (!row) throw std::move(row).status();
        std::cout << row->row_key() << " = ";
        for (auto const& cell : row->cells()) {
          std::cout << "[" << cell.family_name() << ", "
                    << cell.column_qualifier() << ", " << cell.value() << "],";
        }
        std::cout << "\n";
      }
    }

### Node.js

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    const filter = {
      row: {
        cellOffset: 2,
      },
    };
    readWithFilter(filter);

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Bigtable\BigtableClient;
    use Google\Cloud\Bigtable\Filter;
    
    /**
     * Create a limiting filter offsetting cells per row
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance
     * @param string $tableId The ID of the table to read from
     */
    function filter_limit_cells_per_row_offset(
        string $projectId,
        string $instanceId,
        string $tableId
    ): void {
        // Connect to an existing table with an existing instance.
        $dataClient = new BigtableClient([
            'projectId' => $projectId,
        ]);
        $table = $dataClient->table($instanceId, $tableId);
    
        $filter = Filter::offset()->cellsPerRow(2);
    
        $rows = $table->readRows([
            'filter' => $filter
        ]);
    
        foreach ($rows as $key => $row) {
            // The "print_row" helper function is defined in https://cloud.google.com/bigtable/docs/samples/bigtable-reads-print
            print_row($key, $row);
        }
    }

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    # instance_id = "my-instance"
    # table_id    = "my-table"
    filter = Google::Cloud::Bigtable::RowFilter.cells_per_row_offset 2
    read_with_filter instance_id, table_id, filter

#### Column family regex

This filter includes cells in the output row only if the column family for a cell matches a regular expression.

The regular expression must use [RE2 syntax](https://github.com/google/re2/wiki/Syntax). The regular expression must not contain the `:` character, even if the character is not used as a literal. Because column families cannot contain newline characters, you can use either `.` or `\C` as the wildcard expression.

**Note:** This filter lets you filter on the _column family_ , which is the name for a group of columns. To filter on the _column qualifier_ , which is a unique name within a column family, use the column qualifier regular expression filter.

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    func filterLimitColFamilyRegex(w io.Writer, projectID, instanceID string, tableName string) error {
    	filter := bigtable.FamilyFilter("stats_.*$")
    	return readWithFilter(w, projectID, instanceID, tableName, filter)
    }
    

### HBase

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    public static void filterLimitColFamilyRegex() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      filterLimitColFamilyRegex(projectId, instanceId, tableId);
    }
    
    public static void filterLimitColFamilyRegex(
        String projectId, String instanceId, String tableId) {
      // A filter that matches cells whose column family satisfies the given regex
      Filter filter = new FamilyFilter(CompareOp.EQUAL, new RegexStringComparator("stats_.*$"));
      Scan scan = new Scan().setFilter(filter);
      readWithFilter(projectId, instanceId, tableId, scan);
    }

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    public static void filterLimitColFamilyRegex() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      filterLimitColFamilyRegex(projectId, instanceId, tableId);
    }
    
    public static void filterLimitColFamilyRegex(
        String projectId, String instanceId, String tableId) {
      // A filter that matches cells whose column family satisfies the given regex
      Filter filter = FILTERS.family().regex("stats_.*$");
      readFilter(projectId, instanceId, tableId, filter);
    }
    

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    def filter_limit_col_family_regex(project_id, instance_id, table_id):
        from google.cloud import [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest)
        from google.cloud.bigtable import row_filters
    
        client = [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html)(project=project_id, admin=True)
        instance = [client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.html).[instance](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html#google_cloud_bigtable_client_Client_instance)(instance_id)
        table = instance.table(table_id)
    
        rows = table.read_rows(
            filter_=row_filters.FamilyNameRegexFilter("stats_.*$".encode("utf-8"))
        )
        for row in rows:
            print_row(row)
    
    

### Python asyncio

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    async def filter_limit_col_family_regex(project_id, instance_id, table_id):
        from google.cloud.bigtable.data import (
            BigtableDataClientAsync,
            [ReadRowsQuery](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.read_rows_query.ReadRowsQuery.html),
            [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html),
        )
    
        query = ReadRowsQuery(
            row_filter=[row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[FamilyNameRegexFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.FamilyNameRegexFilter.html)("stats_.*$".encode("utf-8"))
        )
    
        async with BigtableDataClientAsync(project=project_id) as client:
            async with client.get_table(instance_id, table_id) as table:
                for row in await table.read_rows(query):
                    print_row(row)
    
    

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    /// <summary>
    /// /// Read using a family regex filter from an existing table.
    ///</summary>
    /// <param name="projectId">Your Google Cloud Project ID.</param>
    /// <param name="instanceId">Your Google Cloud Bigtable Instance ID.</param>
    /// <param name="tableId">Your Google Cloud Bigtable table ID.</param>
    
    public Task<string> FilterLimitColFamilyRegex(string projectId, string instanceId, string tableId)
    {
        // A filter that matches cells whose column family satisfies the given regex
        RowFilter filter = RowFilters.FamilyNameRegex("stats_.*$");
        return ReadFilter(projectId, instanceId, tableId, filter);
    }

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    namespace cbt = ::google::cloud::bigtable;
    using ::google::cloud::StatusOr;
    [](cbt::Table table) {
      cbt::Filter filter = cbt::Filter::FamilyRegex("stats_.*$");
      // Read and print the rows.
      for (StatusOr<cbt::Row>& row :
           table.ReadRows(cbt::RowSet(cbt::RowRange::InfiniteRange()), filter)) {
        if (!row) throw std::move(row).status();
        std::cout << row->row_key() << " = ";
        for (auto const& cell : row->cells()) {
          std::cout << "[" << cell.family_name() << ", "
                    << cell.column_qualifier() << ", " << cell.value() << "],";
        }
        std::cout << "\n";
      }
    }

### Node.js

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    const filter = {
      family: /stats_.*$/,
    };
    readWithFilter(filter);

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Bigtable\BigtableClient;
    use Google\Cloud\Bigtable\Filter;
    
    /**
     * Create a limiting filter on a column family with a regex
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance
     * @param string $tableId The ID of the table to read from
     */
    function filter_limit_col_family_regex(
        string $projectId,
        string $instanceId,
        string $tableId
    ): void {
        // Connect to an existing table with an existing instance.
        $dataClient = new BigtableClient([
            'projectId' => $projectId,
        ]);
        $table = $dataClient->table($instanceId, $tableId);
    
        $filter = Filter::family()->regex('stats_.*$');
    
        $rows = $table->readRows([
            'filter' => $filter
        ]);
    
        foreach ($rows as $key => $row) {
            // The "print_row" helper function is defined in https://cloud.google.com/bigtable/docs/samples/bigtable-reads-print
            print_row($key, $row);
        }
    }

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    # instance_id = "my-instance"
    # table_id    = "my-table"
    filter = Google::Cloud::Bigtable::RowFilter.family "stats_.*$"
    read_with_filter instance_id, table_id, filter

#### Column qualifier regex

This filter includes cells in the output row only if the column qualifier for a cell matches a regular expression.

The regular expression must use [RE2 syntax](https://github.com/google/re2/wiki/Syntax). Because column qualifiers can contain arbitrary bytes, including newline characters, you should use `\C` as the wildcard expression in most cases. The `.` expression does not match newline characters.

**Note:** This filter lets you filter on the _column qualifier_ , which is a unique name within a column family. To filter on the _column family_ , which is the name for a group of columns, use the column family regular expression filter.**Note:** If a column qualifier is used in more than one column family, all columns with that column qualifier are returned. To target a specific column qualifier, use a chain filter.

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    func filterLimitColQualifierRegex(w io.Writer, projectID, instanceID string, tableName string) error {
    	filter := bigtable.ColumnFilter("connected_.*$")
    	return readWithFilter(w, projectID, instanceID, tableName, filter)
    }
    

### HBase

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    public static void filterLimitColQualifierRegex() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      filterLimitColQualifierRegex(projectId, instanceId, tableId);
    }
    
    public static void filterLimitColQualifierRegex(
        String projectId, String instanceId, String tableId) {
      // A filter that matches cells whose column qualifier satisfies the given regex
      Filter filter =
          new QualifierFilter(CompareOp.EQUAL, new RegexStringComparator("connected_.*$"));
      Scan scan = new Scan().setFilter(filter);
      readWithFilter(projectId, instanceId, tableId, scan);
    }

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    public static void filterLimitColQualifierRegex() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      filterLimitColQualifierRegex(projectId, instanceId, tableId);
    }
    
    public static void filterLimitColQualifierRegex(
        String projectId, String instanceId, String tableId) {
      // A filter that matches cells whose column qualifier satisfies the given regex
      Filter filter = FILTERS.qualifier().regex("connected_.*$");
      readFilter(projectId, instanceId, tableId, filter);
    }
    

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    def filter_limit_col_qualifier_regex(project_id, instance_id, table_id):
        from google.cloud import [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest)
        from google.cloud.bigtable import row_filters
    
        client = [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html)(project=project_id, admin=True)
        instance = [client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.html).[instance](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html#google_cloud_bigtable_client_Client_instance)(instance_id)
        table = instance.table(table_id)
    
        rows = table.read_rows(
            filter_=row_filters.ColumnQualifierRegexFilter("connected_.*$".encode("utf-8"))
        )
        for row in rows:
            print_row(row)
    
    

### Python asyncio

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    async def filter_limit_col_qualifier_regex(project_id, instance_id, table_id):
        from google.cloud.bigtable.data import (
            BigtableDataClientAsync,
            [ReadRowsQuery](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.read_rows_query.ReadRowsQuery.html),
            [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html),
        )
    
        query = ReadRowsQuery(
            row_filter=[row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[ColumnQualifierRegexFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.ColumnQualifierRegexFilter.html)(
                "connected_.*$".encode("utf-8")
            )
        )
    
        async with BigtableDataClientAsync(project=project_id) as client:
            async with client.get_table(instance_id, table_id) as table:
                for row in await table.read_rows(query):
                    print_row(row)
    
    

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    /// <summary>
    /// /// Read using a qualifier regex filter from an existing table.
    ///</summary>
    /// <param name="projectId">Your Google Cloud Project ID.</param>
    /// <param name="instanceId">Your Google Cloud Bigtable Instance ID.</param>
    /// <param name="tableId">Your Google Cloud Bigtable table ID.</param>
    
    public Task<string> FilterLimitColQualifierRegex(string projectId, string instanceId, string tableId)
    {
        // A filter that matches cells whose column qualifier satisfies the given regex
        RowFilter filter = RowFilters.ColumnQualifierRegex("connected_.*$");
        return ReadFilter(projectId, instanceId, tableId, filter);
    }

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    namespace cbt = ::google::cloud::bigtable;
    using ::google::cloud::StatusOr;
    [](cbt::Table table) {
      cbt::Filter filter = cbt::Filter::ColumnRegex("connected_.*$");
      // Read and print the rows.
      for (StatusOr<cbt::Row>& row :
           table.ReadRows(cbt::RowSet(cbt::RowRange::InfiniteRange()), filter)) {
        if (!row) throw std::move(row).status();
        std::cout << row->row_key() << " = ";
        for (auto const& cell : row->cells()) {
          std::cout << "[" << cell.family_name() << ", "
                    << cell.column_qualifier() << ", " << cell.value() << "],";
        }
        std::cout << "\n";
      }
    }

### Node.js

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    const filter = {
      column: /connected_.*$/,
    };
    readWithFilter(filter);

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Bigtable\BigtableClient;
    use Google\Cloud\Bigtable\Filter;
    
    /**
     * Create a limiting filter on a column qualifier with a regex
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance
     * @param string $tableId The ID of the table to read from
     */
    function filter_limit_col_qualifier_regex(
        string $projectId,
        string $instanceId,
        string $tableId
    ): void {
        // Connect to an existing table with an existing instance.
        $dataClient = new BigtableClient([
            'projectId' => $projectId,
        ]);
        $table = $dataClient->table($instanceId, $tableId);
    
        $filter = Filter::qualifier()->regex('connected_.*$');
    
        $rows = $table->readRows([
            'filter' => $filter
        ]);
    
        foreach ($rows as $key => $row) {
            // The "print_row" helper function is defined in https://cloud.google.com/bigtable/docs/samples/bigtable-reads-print
            print_row($key, $row);
        }
    }

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    # instance_id = "my-instance"
    # table_id    = "my-table"
    filter = Google::Cloud::Bigtable::RowFilter.qualifier "connected_.*$"
    read_with_filter instance_id, table_id, filter

#### Column range

This filter includes cells in the output row only if they are in a specific column family, and only if their column qualifiers are within a specific range. You specify the range by providing a start qualifier and an end qualifier.

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    func filterLimitColRange(w io.Writer, projectID, instanceID string, tableName string) error {
    	filter := bigtable.ColumnRangeFilter("cell_plan", "data_plan_01gb", "data_plan_10gb")
    	return readWithFilter(w, projectID, instanceID, tableName, filter)
    }
    

### HBase

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    public static void filterLimitColRange() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      filterLimitColRange(projectId, instanceId, tableId);
    }
    
    public static void filterLimitColRange(String projectId, String instanceId, String tableId) {
      // A filter that matches cells whose column qualifiers are between data_plan_01gb and
      // data_plan_10gb in the column family cell_plan
      Filter filter =
          new ColumnRangeFilter(
              Bytes.toBytes("data_plan_01gb"), true, Bytes.toBytes("data_plan_10gb"), false);
      Scan scan = new Scan().addFamily(Bytes.toBytes("cell_plan")).setFilter(filter).setMaxVersions();
      readWithFilter(projectId, instanceId, tableId, scan);
    }

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    public static void filterLimitColRange() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      filterLimitColRange(projectId, instanceId, tableId);
    }
    
    public static void filterLimitColRange(String projectId, String instanceId, String tableId) {
      // A filter that matches cells whose column qualifiers are between data_plan_01gb and
      // data_plan_10gb in the column family cell_plan
      Filter filter =
          FILTERS
              .qualifier()
              .rangeWithinFamily("cell_plan")
              .startClosed("data_plan_01gb")
              .endOpen("data_plan_10gb");
      readFilter(projectId, instanceId, tableId, filter);
    }
    

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    def filter_limit_col_range(project_id, instance_id, table_id):
        from google.cloud import [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest)
        from google.cloud.bigtable import row_filters
    
        client = [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html)(project=project_id, admin=True)
        instance = [client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.html).[instance](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html#google_cloud_bigtable_client_Client_instance)(instance_id)
        table = instance.table(table_id)
    
        rows = table.read_rows(
            filter_=row_filters.ColumnRangeFilter(
                "cell_plan", b"data_plan_01gb", b"data_plan_10gb", inclusive_end=False
            )
        )
        for row in rows:
            print_row(row)
    
    

### Python asyncio

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    async def filter_limit_col_range(project_id, instance_id, table_id):
        from google.cloud.bigtable.data import (
            BigtableDataClientAsync,
            [ReadRowsQuery](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.read_rows_query.ReadRowsQuery.html),
            [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html),
        )
    
        query = ReadRowsQuery(
            row_filter=[row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[ColumnRangeFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.ColumnRangeFilter.html)(
                "cell_plan", b"data_plan_01gb", b"data_plan_10gb", inclusive_end=False
            )
        )
    
        async with BigtableDataClientAsync(project=project_id) as client:
            async with client.get_table(instance_id, table_id) as table:
                for row in await table.read_rows(query):
                    print_row(row)
    
    

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    /// <summary>
    /// /// Read using a qualifer range filter from an existing table.
    ///</summary>
    /// <param name="projectId">Your Google Cloud Project ID.</param>
    /// <param name="instanceId">Your Google Cloud Bigtable Instance ID.</param>
    /// <param name="tableId">Your Google Cloud Bigtable table ID.</param>
    
    public Task<string> FilterLimitColRange(string projectId = "YOUR-PROJECT-ID", string instanceId = "YOUR-INSTANCE-ID", string tableId = "YOUR-TABLE-ID")
    {
        // A filter that matches cells whose column qualifiers are between data_plan_01gb and
        // data_plan_10gb in the column family cell_plan
        RowFilter filter = RowFilters.ColumnRange(ColumnRange.ClosedOpen("cell_plan", "data_plan_01gb", "data_plan_10gb"));
        return ReadFilter(projectId, instanceId, tableId, filter);
    }

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    namespace cbt = ::google::cloud::bigtable;
    using ::google::cloud::StatusOr;
    [](cbt::Table table) {
      cbt::Filter filter = cbt::Filter::ColumnRange("cell_plan", "data_plan_01gb",
                                                    "data_plan_10gb");
      // Read and print the rows.
      for (StatusOr<cbt::Row>& row :
           table.ReadRows(cbt::RowSet(cbt::RowRange::InfiniteRange()), filter)) {
        if (!row) throw std::move(row).status();
        std::cout << row->row_key() << " = ";
        for (auto const& cell : row->cells()) {
          std::cout << "[" << cell.family_name() << ", "
                    << cell.column_qualifier() << ", " << cell.value() << "],";
        }
        std::cout << "\n";
      }
    }

### Node.js

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    const filter = {
      column: {
        family: 'cell_plan',
        start: 'data_plan_01gb',
        end: {
          value: 'data_plan_10gb',
          inclusive: false,
        },
      },
    };
    readWithFilter(filter);

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Bigtable\BigtableClient;
    use Google\Cloud\Bigtable\Filter;
    
    /**
     * Create a limiting filter on a range of columns
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance
     * @param string $tableId The ID of the table to read from
     */
    function filter_limit_col_range(
        string $projectId,
        string $instanceId,
        string $tableId
    ): void {
        // Connect to an existing table with an existing instance.
        $dataClient = new BigtableClient([
            'projectId' => $projectId,
        ]);
        $table = $dataClient->table($instanceId, $tableId);
    
        $filter = Filter::qualifier()
            ->rangeWithinFamily('cell_plan')
            ->startClosed('data_plan_01gb')
            ->endOpen('data_plan_10gb');
    
        $rows = $table->readRows([
            'filter' => $filter
        ]);
    
        foreach ($rows as $key => $row) {
            // The "print_row" helper function is defined in https://cloud.google.com/bigtable/docs/samples/bigtable-reads-print
            print_row($key, $row);
        }
    }

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    # instance_id = "my-instance"
    # table_id    = "my-table"
    range = Google::Cloud::Bigtable::ColumnRange.new("cell_plan").from("data_plan_01gb").to("data_plan_10gb")
    filter = Google::Cloud::Bigtable::RowFilter.column_range range
    read_with_filter instance_id, table_id, filter

#### Value range

This filter includes cells in the output row only if their values are within a specific range. You specify the range by providing a start value and an end value.

  * **To get cells whose value comes before a specific value** , specify that value as the exclusive end value, and omit the start value.
  * **To get cells whose value is equal to or after a specific value** , specify that value as the inclusive start value, and omit the end value.




### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    func filterLimitValueRange(w io.Writer, projectID, instanceID string, tableName string) error {
    	filter := bigtable.ValueRangeFilter([]byte("PQ2A.190405"), []byte("PQ2A.190406"))
    	return readWithFilter(w, projectID, instanceID, tableName, filter)
    }
    

### HBase

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    public static void filterLimitValueRange() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      filterLimitValueRange(projectId, instanceId, tableId);
    }
    
    public static void filterLimitValueRange(String projectId, String instanceId, String tableId) {
      // A filter that matches cells whose values are between the given values
      ValueFilter valueGreaterFilter =
          new ValueFilter(
              CompareFilter.CompareOp.GREATER_OR_EQUAL,
              new BinaryComparator(Bytes.toBytes("PQ2A.190405")));
      ValueFilter valueLesserFilter =
          new ValueFilter(
              CompareFilter.CompareOp.LESS_OR_EQUAL,
              new BinaryComparator(Bytes.toBytes("PQ2A.190406")));
    
      FilterList filter = new FilterList(FilterList.Operator.MUST_PASS_ALL);
      filter.addFilter(valueGreaterFilter);
      filter.addFilter(valueLesserFilter);
    
      Scan scan = new Scan().setFilter(filter);
      readWithFilter(projectId, instanceId, tableId, scan);
    }

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    public static void filterLimitValueRange() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      filterLimitValueRange(projectId, instanceId, tableId);
    }
    
    public static void filterLimitValueRange(String projectId, String instanceId, String tableId) {
      // A filter that matches cells whose values are between the given values
      Filter filter = FILTERS.value().range().startClosed("PQ2A.190405").endClosed("PQ2A.190406");
      readFilter(projectId, instanceId, tableId, filter);
    }
    

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    def filter_limit_value_range(project_id, instance_id, table_id):
        from google.cloud import [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest)
        from google.cloud.bigtable import row_filters
    
        client = [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html)(project=project_id, admin=True)
        instance = [client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.html).[instance](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html#google_cloud_bigtable_client_Client_instance)(instance_id)
        table = instance.table(table_id)
    
        rows = table.read_rows(
            filter_=row_filters.ValueRangeFilter(b"PQ2A.190405", b"PQ2A.190406")
        )
    
        for row in rows:
            print_row(row)
    
    

### Python asyncio

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    async def filter_limit_value_range(project_id, instance_id, table_id):
        from google.cloud.bigtable.data import (
            BigtableDataClientAsync,
            [ReadRowsQuery](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.read_rows_query.ReadRowsQuery.html),
            [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html),
        )
    
        query = ReadRowsQuery(
            row_filter=[row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[ValueRangeFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.ValueRangeFilter.html)(b"PQ2A.190405", b"PQ2A.190406")
        )
    
        async with BigtableDataClientAsync(project=project_id) as client:
            async with client.get_table(instance_id, table_id) as table:
                for row in await table.read_rows(query):
                    print_row(row)
    
    

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    /// <summary>
    /// /// Read using a value range filter from an existing table.
    ///</summary>
    /// <param name="projectId">Your Google Cloud Project ID.</param>
    /// <param name="instanceId">Your Google Cloud Bigtable Instance ID.</param>
    /// <param name="tableId">Your Google Cloud Bigtable table ID.</param>
    
    public Task<string> FilterLimitValueRange(string projectId = "YOUR-PROJECT-ID", string instanceId = "YOUR-INSTANCE-ID", string tableId = "YOUR-TABLE-ID")
    {
        // A filter that matches cells whose values are between the given values
        RowFilter filter = RowFilters.ValueRange(ValueRange.Closed("PQ2A.190405", "PQ2A.190406"));
        return ReadFilter(projectId, instanceId, tableId, filter);
    }

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    namespace cbt = ::google::cloud::bigtable;
    using ::google::cloud::StatusOr;
    [](cbt::Table table) {
      cbt::Filter filter = cbt::Filter::ValueRange("PQ2A.190405", "PQ2A.190406");
      // Read and print the rows.
      for (StatusOr<cbt::Row>& row :
           table.ReadRows(cbt::RowSet(cbt::RowRange::InfiniteRange()), filter)) {
        if (!row) throw std::move(row).status();
        std::cout << row->row_key() << " = ";
        for (auto const& cell : row->cells()) {
          std::cout << "[" << cell.family_name() << ", "
                    << cell.column_qualifier() << ", " << cell.value() << "],";
        }
        std::cout << "\n";
      }
    }

### Node.js

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    const filter = {
      value: {
        start: 'PQ2A.190405',
        end: 'PQ2A.190406',
      },
    };
    readWithFilter(filter);

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Bigtable\BigtableClient;
    use Google\Cloud\Bigtable\Filter;
    
    /**
     * Create a limiting filter on a range of cell values
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance
     * @param string $tableId The ID of the table to read from
     */
    function filter_limit_value_range(
        string $projectId,
        string $instanceId,
        string $tableId
    ): void {
        // Connect to an existing table with an existing instance.
        $dataClient = new BigtableClient([
            'projectId' => $projectId,
        ]);
        $table = $dataClient->table($instanceId, $tableId);
    
        $filter = Filter::value()
            ->range()
            ->startClosed('PQ2A.190405')
            ->endOpen('PQ2A.190406');
    
        $rows = $table->readRows([
            'filter' => $filter
        ]);
    
        foreach ($rows as $key => $row) {
            // The "print_row" helper function is defined in https://cloud.google.com/bigtable/docs/samples/bigtable-reads-print
            print_row($key, $row);
        }
    }

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    # instance_id = "my-instance"
    # table_id    = "my-table"
    range = Google::Cloud::Bigtable::ValueRange.new.from("PQ2A.190405").to("PQ2A.190406")
    filter = Google::Cloud::Bigtable::RowFilter.value_range range
    read_with_filter instance_id, table_id, filter

#### Value regex

This filter includes cells in the output row only if the value of the cell matches a regular expression.

The regular expression must use [RE2 syntax](https://github.com/google/re2/wiki/Syntax). Because values can contain arbitrary bytes, including newline characters, you should use `\C` as the wildcard expression in most cases. The `.` expression does not match newline characters.

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    func filterLimitValueRegex(w io.Writer, projectID, instanceID string, tableName string) error {
    	filter := bigtable.ValueFilter("PQ2A.*$")
    	return readWithFilter(w, projectID, instanceID, tableName, filter)
    }
    

### HBase

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    public static void filterLimitValueRegex() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      filterLimitValueRegex(projectId, instanceId, tableId);
    }
    
    public static void filterLimitValueRegex(String projectId, String instanceId, String tableId) {
      // A filter that matches cells whose value satisfies the given regex
      Filter filter = new ValueFilter(CompareOp.EQUAL, new RegexStringComparator("PQ2A.*$"));
    
      Scan scan = new Scan().setFilter(filter);
      readWithFilter(projectId, instanceId, tableId, scan);
    }

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    public static void filterLimitValueRegex() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      filterLimitValueRegex(projectId, instanceId, tableId);
    }
    
    public static void filterLimitValueRegex(String projectId, String instanceId, String tableId) {
      // A filter that matches cells whose value satisfies the given regex
      Filter filter = FILTERS.value().regex("PQ2A.*$");
      readFilter(projectId, instanceId, tableId, filter);
    }
    

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    
    def filter_limit_value_regex(project_id, instance_id, table_id):
        from google.cloud import [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest)
        from google.cloud.bigtable import row_filters
    
        client = [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html)(project=project_id, admin=True)
        instance = [client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.html).[instance](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html#google_cloud_bigtable_client_Client_instance)(instance_id)
        table = instance.table(table_id)
    
        rows = table.read_rows(
            filter_=row_filters.ValueRegexFilter("PQ2A.*$".encode("utf-8"))
        )
        for row in rows:
            print_row(row)
    
    

### Python ayncio

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    
    async def filter_limit_value_regex(project_id, instance_id, table_id):
        from google.cloud.bigtable.data import (
            BigtableDataClientAsync,
            [ReadRowsQuery](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.read_rows_query.ReadRowsQuery.html),
            [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html),
        )
    
        query = ReadRowsQuery(
            row_filter=[row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[ValueRegexFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.ValueRegexFilter.html)("PQ2A.*$".encode("utf-8"))
        )
    
        async with BigtableDataClientAsync(project=project_id) as client:
            async with client.get_table(instance_id, table_id) as table:
                for row in await table.read_rows(query):
                    print_row(row)
    
    

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    /// <summary>
    /// /// Read using a value regex filter from an existing table.
    ///</summary>
    /// <param name="projectId">Your Google Cloud Project ID.</param>
    /// <param name="instanceId">Your Google Cloud Bigtable Instance ID.</param>
    /// <param name="tableId">Your Google Cloud Bigtable table ID.</param>
    
    public Task<string> FilterLimitValueRegex(string projectId = "YOUR-PROJECT-ID", string instanceId = "YOUR-INSTANCE-ID", string tableId = "YOUR-TABLE-ID")
    {
        // A filter that matches cells whose value satisfies the given regex
        RowFilter filter = RowFilters.ValueRegex("PQ2A.*$");
        return ReadFilter(projectId, instanceId, tableId, filter);
    }

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    namespace cbt = ::google::cloud::bigtable;
    using ::google::cloud::StatusOr;
    [](cbt::Table table) {
      cbt::Filter filter = cbt::Filter::ValueRegex("PQ2A.*$");
      // Read and print the rows.
      for (StatusOr<cbt::Row>& row :
           table.ReadRows(cbt::RowSet(cbt::RowRange::InfiniteRange()), filter)) {
        if (!row) throw std::move(row).status();
        std::cout << row->row_key() << " = ";
        for (auto const& cell : row->cells()) {
          std::cout << "[" << cell.family_name() << ", "
                    << cell.column_qualifier() << ", " << cell.value() << "],";
        }
        std::cout << "\n";
      }
    }

### Node.js

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    const filter = {
      value: /PQ2A.*$/,
    };
    readWithFilter(filter);

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Bigtable\BigtableClient;
    use Google\Cloud\Bigtable\Filter;
    
    /**
     * Create a limiting filter on a cell value using a regex
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance
     * @param string $tableId The ID of the table to read from
     */
    function filter_limit_value_regex(
        string $projectId,
        string $instanceId,
        string $tableId
    ): void {
        // Connect to an existing table with an existing instance.
        $dataClient = new BigtableClient([
            'projectId' => $projectId,
        ]);
        $table = $dataClient->table($instanceId, $tableId);
    
        $filter = Filter::value()->regex('PQ2A.*$');
    
        $rows = $table->readRows([
            'filter' => $filter
        ]);
    
        foreach ($rows as $key => $row) {
            // The "print_row" helper function is defined in https://cloud.google.com/bigtable/docs/samples/bigtable-reads-print
            print_row($key, $row);
        }
    }

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    # instance_id = "my-instance"
    # table_id    = "my-table"
    filter = Google::Cloud::Bigtable::RowFilter.value "PQ2A.*$"
    read_with_filter instance_id, table_id, filter

#### Timestamp range

This filter includes cells in the output row only if their timestamps are within a specific range. You specify the range by providing a start time, which is inclusive, and an end time, which is exclusive. The default unit is _microseconds_ , and the timestamp must be a multiple of 1,000.

  * **To get cells whose timestamps are older than a specific time** , specify that time as the end time, and omit the start time to make it unbounded.
  * **To get cells whose timestamps are equal to or newer than a specific time** , specify that time as the start time, and omit the end time to make it unbounded.




### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    func filterLimitTimestampRange(w io.Writer, projectID, instanceID string, tableName string) error {
    	startTime := time.Unix(0, 0)
    	endTime := time.Now().Add(-1 * time.Hour)
    	filter := bigtable.TimestampRangeFilter(startTime, endTime)
    
    	return readWithFilter(w, projectID, instanceID, tableName, filter)
    }
    

### HBase

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    public static void filterLimitTimestampRange() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      filterLimitTimestampRange(projectId, instanceId, tableId);
    }
    
    public static void filterLimitTimestampRange(
        String projectId, String instanceId, String tableId) {
      // A filter that matches cells whose timestamp is from an hour ago or earlier
      // Get a time representing one hour ago
      long timestamp = Instant.now().minus(1, ChronoUnit.HOURS).toEpochMilli();
      try {
        Scan scan = new Scan().setTimeRange(0, timestamp).setMaxVersions();
        readWithFilter(projectId, instanceId, tableId, scan);
      } catch (IOException e) {
        System.out.println("There was an issue with your timestamp \n" + e.toString());
      }
    }

### Java

Note: The methods [`startOpen()`](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/overview) and [`endClosed()`](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/overview) are not supported for timestamp range filters in this client library.

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    public static void filterLimitTimestampRange() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      filterLimitTimestampRange(projectId, instanceId, tableId);
    }
    
    public static void filterLimitTimestampRange(
        String projectId, String instanceId, String tableId) {
      // Get a time representing one hour ago
      long timestamp = Instant.now().minus(1, ChronoUnit.HOURS).toEpochMilli() * 1000;
    
      // A filter that matches cells whose timestamp is from an hour ago or earlier
      Filter filter = FILTERS.timestamp().range().startClosed(0L).endOpen(timestamp);
      readFilter(projectId, instanceId, tableId, filter);
    }
    

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    def filter_limit_timestamp_range(project_id, instance_id, table_id):
        from google.cloud import [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest)
        from google.cloud.bigtable import row_filters
        import datetime
    
        client = [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html)(project=project_id, admin=True)
        instance = [client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.html).[instance](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html#google_cloud_bigtable_client_Client_instance)(instance_id)
        table = instance.table(table_id)
    
        end = datetime.datetime(2019, 5, 1)
    
        rows = table.read_rows(
            filter_=row_filters.TimestampRangeFilter(row_filters.TimestampRange(end=end))
        )
        for row in rows:
            print_row(row)
    
    

### Python asyncio

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    async def filter_limit_timestamp_range(project_id, instance_id, table_id):
        import datetime
    
        from google.cloud.bigtable.data import (
            BigtableDataClientAsync,
            [ReadRowsQuery](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.read_rows_query.ReadRowsQuery.html),
            [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html),
        )
    
        end = datetime.datetime(2019, 5, 1)
    
        query = ReadRowsQuery(row_filter=[row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[TimestampRangeFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.TimestampRangeFilter.html)(end=end))
    
        async with BigtableDataClientAsync(project=project_id) as client:
            async with client.get_table(instance_id, table_id) as table:
                for row in await table.read_rows(query):
                    print_row(row)
    
    

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    /// <summary>
    /// /// Read using a timestamp range filter from an existing table.
    ///</summary>
    /// <param name="projectId">Your Google Cloud Project ID.</param>
    /// <param name="instanceId">Your Google Cloud Bigtable Instance ID.</param>
    /// <param name="tableId">Your Google Cloud Bigtable table ID.</param>
    
    public Task<string> FilterLimitTimestampRange(string projectId, string instanceId, string tableId)
    {
        BigtableVersion timestamp_minus_hr = new BigtableVersion(new DateTime(2020, 1, 10, 13, 0, 0, DateTimeKind.Utc));
    
        // A filter that matches cells whose timestamp is from an hour ago or earlier
        RowFilter filter = RowFilters.TimestampRange(new DateTime(0), timestamp_minus_hr.ToDateTime());
        return ReadFilter(projectId, instanceId, tableId, filter);
    }

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    namespace cbt = ::google::cloud::bigtable;
    using ::google::cloud::StatusOr;
    [](cbt::Table table) {
      cbt::Filter filter =
          cbt::Filter::TimestampRange(microseconds(1000), milliseconds(2));
      // Read and print the rows.
      for (StatusOr<cbt::Row>& row :
           table.ReadRows(cbt::RowSet(cbt::RowRange::InfiniteRange()), filter)) {
        if (!row) throw std::move(row).status();
        std::cout << row->row_key() << " = ";
        for (auto const& cell : row->cells()) {
          std::cout << "[" << cell.family_name() << ", "
                    << cell.column_qualifier() << ", " << cell.value() << "],";
        }
        std::cout << "\n";
      }
    }

### Node.js

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    const start = 0;
    const end = new Date(2019, 5, 1);
    end.setUTCHours(0);
    const filter = {
      time: {
        start,
        end,
      },
    };
    readWithFilter(filter);

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Bigtable\BigtableClient;
    use Google\Cloud\Bigtable\Filter;
    
    /**
     * Create a limiting filter on a range of cell timestamps
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance
     * @param string $tableId The ID of the table to read from
     * @param int $endTime The timestamp upto which you want to fetch the rows
     */
    function filter_limit_timestamp_range(
        string $projectId,
        string $instanceId,
        string $tableId,
        int $endTime = null
    ): void {
        // Connect to an existing table with an existing instance.
        $dataClient = new BigtableClient([
            'projectId' => $projectId,
        ]);
        $table = $dataClient->table($instanceId, $tableId);
        $endTime = is_null($endTime) ? (time() - 60 * 60) * 1000 * 1000 : $endTime;
    
        $start = 0;
        $filter = Filter::timestamp()
            ->range()
            ->startClosed($start)
            ->endOpen($endTime);
    
        $rows = $table->readRows([
            'filter' => $filter
        ]);
    
        foreach ($rows as $key => $row) {
            // The "print_row" helper function is defined in https://cloud.google.com/bigtable/docs/samples/bigtable-reads-print
            print_row($key, $row);
        }
    }

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    # instance_id = "my-instance"
    # table_id    = "my-table"
    timestamp_minus_hr = (Time.now.to_f * 1_000_000).round(-3) - (60 * 60 * 1000 * 1000)
    puts timestamp_minus_hr
    filter = Google::Cloud::Bigtable::RowFilter.timestamp_range from: 0, to: timestamp_minus_hr
    
    read_with_filter instance_id, table_id, filter

### Advanced single filters

The following filters can be difficult to use.

#### Block all

This filter removes all of the cells from the output row.

If you are using an interleave filter, you can combine the block all filter with the chain filter to temporarily disable part of the interleave.

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    func filterLimitBlockAll(w io.Writer, projectID, instanceID string, tableName string) error {
    	filter := bigtable.BlockAllFilter()
    	return readWithFilter(w, projectID, instanceID, tableName, filter)
    }
    

### HBase

This client library does not support this filter.

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    public static void filterLimitBlockAll() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      filterLimitBlockAll(projectId, instanceId, tableId);
    }
    
    public static void filterLimitBlockAll(String projectId, String instanceId, String tableId) {
      // A filter that does not match any cells
      Filter filter = FILTERS.block();
      readFilter(projectId, instanceId, tableId, filter);
    }
    

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    def filter_limit_block_all(project_id, instance_id, table_id):
        from google.cloud import [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest)
        from google.cloud.bigtable import row_filters
    
        client = [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html)(project=project_id, admin=True)
        instance = [client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.html).[instance](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html#google_cloud_bigtable_client_Client_instance)(instance_id)
        table = instance.table(table_id)
    
        rows = table.read_rows(filter_=row_filters.BlockAllFilter(True))
        for row in rows:
            print_row(row)
    
    

### Python asyncio

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    async def filter_limit_block_all(project_id, instance_id, table_id):
        from google.cloud.bigtable.data import (
            BigtableDataClientAsync,
            [ReadRowsQuery](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.read_rows_query.ReadRowsQuery.html),
            [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html),
        )
    
        query = ReadRowsQuery(row_filter=[row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[BlockAllFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.BlockAllFilter.html)(True))
    
        async with BigtableDataClientAsync(project=project_id) as client:
            async with client.get_table(instance_id, table_id) as table:
                for row in await table.read_rows(query):
                    print_row(row)
    
    

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    /// <summary>
    /// /// Read using a block all filter from an existing table.
    ///</summary>
    /// <param name="projectId">Your Google Cloud Project ID.</param>
    /// <param name="instanceId">Your Google Cloud Bigtable Instance ID.</param>
    /// <param name="tableId">Your Google Cloud Bigtable table ID.</param>
    
    public Task<string> FilterLimitBlockAll(string projectId = "YOUR-PROJECT-ID", string instanceId = "YOUR-INSTANCE-ID", string tableId = "YOUR-TABLE-ID")
    {
        // A filter that does not match any cells
        RowFilter filter = RowFilters.BlockAllFilter();
        return ReadFilter(projectId, instanceId, tableId, filter);
    }

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    namespace cbt = ::google::cloud::bigtable;
    using ::google::cloud::StatusOr;
    [](cbt::Table table) {
      cbt::Filter filter = cbt::Filter::BlockAllFilter();
      // Read and print the rows.
      for (StatusOr<cbt::Row>& row :
           table.ReadRows(cbt::RowSet(cbt::RowRange::InfiniteRange()), filter)) {
        if (!row) throw std::move(row).status();
        std::cout << row->row_key();
        std::cout << row->row_key() << " = ";
        for (auto const& cell : row->cells()) {
          std::cout << "[" << cell.family_name() << ", "
                    << cell.column_qualifier() << ", " << cell.value() << "],";
        }
        std::cout << "\n";
      }
    }

### Node.js

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    const filter = {
      all: false,
    };
    readWithFilter(filter);

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Bigtable\BigtableClient;
    use Google\Cloud\Bigtable\Filter;
    
    /**
     * Create a block all filter
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance
     * @param string $tableId The ID of the table to read from
     */
    function filter_limit_block_all(
        string $projectId,
        string $instanceId,
        string $tableId
    ): void {
        // Connect to an existing table with an existing instance.
        $dataClient = new BigtableClient([
            'projectId' => $projectId,
        ]);
        $table = $dataClient->table($instanceId, $tableId);
    
        $filter = Filter::block();
    
        $rows = $table->readRows([
            'filter' => $filter
        ]);
    
        foreach ($rows as $key => $row) {
            // The "print_row" helper function is defined in https://cloud.google.com/bigtable/docs/samples/bigtable-reads-print
            print_row($key, $row);
        }
    }

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    # instance_id = "my-instance"
    # table_id    = "my-table"
    filter = Google::Cloud::Bigtable::RowFilter.block
    read_with_filter instance_id, table_id, filter

#### Pass all

This filter includes all of the input row's cells in the output row. It is equivalent to a read with no filter.

The pass all filter can be useful if you are composing multiple filters, and you need to output cells in some cases but not others.

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    func filterLimitPassAll(w io.Writer, projectID, instanceID string, tableName string) error {
    	filter := bigtable.PassAllFilter()
    	return readWithFilter(w, projectID, instanceID, tableName, filter)
    }
    

### HBase

This client library does not support this filter.

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    public static void filterLimitPassAll() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      filterLimitPassAll(projectId, instanceId, tableId);
    }
    
    public static void filterLimitPassAll(String projectId, String instanceId, String tableId) {
      // A filter that matches all cells
      Filter filter = FILTERS.pass();
      readFilter(projectId, instanceId, tableId, filter);
    }
    

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    def filter_limit_pass_all(project_id, instance_id, table_id):
        from google.cloud import [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest)
        from google.cloud.bigtable import row_filters
    
        client = [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html)(project=project_id, admin=True)
        instance = [client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.html).[instance](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html#google_cloud_bigtable_client_Client_instance)(instance_id)
        table = instance.table(table_id)
    
        rows = table.read_rows(filter_=row_filters.PassAllFilter(True))
        for row in rows:
            print_row(row)
    
    

### Python asyncio

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    async def filter_limit_pass_all(project_id, instance_id, table_id):
        from google.cloud.bigtable.data import (
            BigtableDataClientAsync,
            [ReadRowsQuery](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.read_rows_query.ReadRowsQuery.html),
            [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html),
        )
    
        query = ReadRowsQuery(row_filter=[row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[PassAllFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.PassAllFilter.html)(True))
    
        async with BigtableDataClientAsync(project=project_id) as client:
            async with client.get_table(instance_id, table_id) as table:
                for row in await table.read_rows(query):
                    print_row(row)
    
    

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    /// <summary>
    /// /// Read using a pass all filter from an existing table.
    ///</summary>
    /// <param name="projectId">Your Google Cloud Project ID.</param>
    /// <param name="instanceId">Your Google Cloud Bigtable Instance ID.</param>
    /// <param name="tableId">Your Google Cloud Bigtable table ID.</param>
    
    public Task<string> FilterLimitPassAll(string projectId = "YOUR-PROJECT-ID", string instanceId = "YOUR-INSTANCE-ID", string tableId = "YOUR-TABLE-ID")
    {
        // A filter that matches all cells
        RowFilter filter = RowFilters.PassAllFilter();
        return ReadFilter(projectId, instanceId, tableId, filter);
    }

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    namespace cbt = ::google::cloud::bigtable;
    using ::google::cloud::StatusOr;
    [](cbt::Table table) {
      cbt::Filter filter = cbt::Filter::PassAllFilter();
      // Read and print the rows.
      for (StatusOr<cbt::Row>& row :
           table.ReadRows(cbt::RowSet(cbt::RowRange::InfiniteRange()), filter)) {
        if (!row) throw std::move(row).status();
        std::cout << row->row_key() << " = ";
        for (auto const& cell : row->cells()) {
          std::cout << "[" << cell.family_name() << ", "
                    << cell.column_qualifier() << ", " << cell.value() << "],";
        }
        std::cout << "\n";
      }
    }

### Node.js

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    const filter = {
      all: true,
    };
    readWithFilter(filter);

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Bigtable\BigtableClient;
    use Google\Cloud\Bigtable\Filter;
    
    /**
     * Create a pass all filter
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance
     * @param string $tableId The ID of the table to read from
     */
    function filter_limit_pass_all(
        string $projectId,
        string $instanceId,
        string $tableId
    ): void {
        // Connect to an existing table with an existing instance.
        $dataClient = new BigtableClient([
            'projectId' => $projectId,
        ]);
        $table = $dataClient->table($instanceId, $tableId);
    
        $filter = Filter::pass();
    
        $rows = $table->readRows([
            'filter' => $filter
        ]);
    
        foreach ($rows as $key => $row) {
            // The "print_row" helper function is defined in https://cloud.google.com/bigtable/docs/samples/bigtable-reads-print
            print_row($key, $row);
        }
    }

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    # instance_id = "my-instance"
    # table_id    = "my-table"
    filter = Google::Cloud::Bigtable::RowFilter.pass
    read_with_filter instance_id, table_id, filter

#### Sink

This filter copies all of the input row's cells into the final output row, even if another filter would normally remove or change those cells.

**Note:** In general, you probably don't need to use the sink filter. It's designed to support a small number of advanced use cases. It can also be useful for debugging complex combinations of filters.

When you use a chain of filters, other limiting filters can only affect their own output row, which becomes the input row for the next filter in the chain. The sink filter is different—it inserts cells directly into the final output row, which appears in the read results.

For example, suppose that you create a chain of two filters:

  1. The sink filter
  2. The block all filter, which deletes all cells from the row



On its own, the block all filter would result in an empty row, which wouldn't be included in the read results. However, the sink filter forces all of the cells from the input row to be copied to the final output row, regardless of what other filters in the chain might do. As a result, combining the sink filter and the block all filter has the same effect as not using a filter at all, and the original input row, with all of its cells, appears in the read results.

## Modifying filters

The following sections describe each modifying filter. Modifying filters affect the data or metadata for individual cells.

#### Apply label

This filter adds a label to all of the cells in a row. Use this filter as part of an interleave to indicate which filter caused a cell to be included in the output row. Your application can use each cell's label to perform additional client-side processing.

**Note:** The apply label filter is not related to the [labels you can add to your Bigtable resources](https://docs.cloud.google.com/bigtable/docs/creating-managing-labels). Labeling your Bigtable resources has no effect on reading data.

Each label must be no longer than 15 characters. In addition, each label must match the [RE2 regular expression](https://github.com/google/re2/wiki/Syntax) `[a-z0-9\\-]+`.

Each cell can have only one label. As a result, a chain of filters can include the apply label filter only once.

### Go

This client library does not support this filter.

### HBase

This client library does not support this filter.

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    public static void filterModifyApplyLabel() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      filterModifyApplyLabel(projectId, instanceId, tableId);
    }
    
    public static void filterModifyApplyLabel(String projectId, String instanceId, String tableId) {
      // A filter that applies the given label to the outputted cell
      Filter filter = FILTERS.label("labelled");
      readFilter(projectId, instanceId, tableId, filter);
    }
    

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    def filter_modify_apply_label(project_id, instance_id, table_id):
        from google.cloud import [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest)
        from google.cloud.bigtable import row_filters
    
        client = [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html)(project=project_id, admin=True)
        instance = [client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.html).[instance](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html#google_cloud_bigtable_client_Client_instance)(instance_id)
        table = instance.table(table_id)
    
        rows = table.read_rows(filter_=row_filters.ApplyLabelFilter(label="labelled"))
        for row in rows:
            print_row(row)
    
    

### Python asyncio

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    async def filter_modify_apply_label(project_id, instance_id, table_id):
        from google.cloud.bigtable.data import (
            BigtableDataClientAsync,
            [ReadRowsQuery](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.read_rows_query.ReadRowsQuery.html),
            [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html),
        )
    
        query = ReadRowsQuery(row_filter=[row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[ApplyLabelFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.ApplyLabelFilter.html)(label="labelled"))
    
        async with BigtableDataClientAsync(project=project_id) as client:
            async with client.get_table(instance_id, table_id) as table:
                for row in await table.read_rows(query):
                    print_row(row)
    
    

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    /// <summary>
    /// /// Read using a strip value filter from an existing table.
    ///</summary>
    /// <param name="projectId">Your Google Cloud Project ID.</param>
    /// <param name="instanceId">Your Google Cloud Bigtable Instance ID.</param>
    /// <param name="tableId">Your Google Cloud Bigtable table ID.</param>
    
    public Task<string> FilterModifyApplyLabel(string projectId = "YOUR-PROJECT-ID", string instanceId = "YOUR-INSTANCE-ID", string tableId = "YOUR-TABLE-ID")
    {
        // A filter that applies the given label to the outputted cell
        RowFilter filter = new RowFilter { ApplyLabelTransformer = "labelled" };
        return ReadFilter(projectId, instanceId, tableId, filter);
    }

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    namespace cbt = ::google::cloud::bigtable;
    using ::google::cloud::StatusOr;
    [](cbt::Table table) {
      cbt::Filter filter = cbt::Filter::ApplyLabelTransformer("labelled");
      // Read and print the rows.
      for (StatusOr<cbt::Row>& row :
           table.ReadRows(cbt::RowSet(cbt::RowRange::InfiniteRange()), filter)) {
        if (!row) throw std::move(row).status();
        std::cout << row->row_key() << " = ";
        for (auto const& cell : row->cells()) {
          std::cout << "[" << cell.family_name() << ", "
                    << cell.column_qualifier() << ", " << cell.value()
                    << ", label(";
          for (auto const& label : cell.labels()) {
            std::cout << label << ",";
          }
          std::cout << ")],";
        }
        std::cout << "\n";
      }
    }

### Node.js

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    const filter = {
      label: 'labelled',
    };
    readWithFilter(filter);

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Bigtable\BigtableClient;
    use Google\Cloud\Bigtable\Filter;
    
    /**
     * Create a filter that applies a label
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance
     * @param string $tableId The ID of the table to read from
     */
    function filter_modify_apply_label(
        string $projectId,
        string $instanceId,
        string $tableId
    ): void {
        // Connect to an existing table with an existing instance.
        $dataClient = new BigtableClient([
            'projectId' => $projectId,
        ]);
        $table = $dataClient->table($instanceId, $tableId);
    
        $filter = Filter::label('labelled');
    
        $rows = $table->readRows([
            'filter' => $filter
        ]);
    
        foreach ($rows as $key => $row) {
            // The "print_row" helper function is defined in https://cloud.google.com/bigtable/docs/samples/bigtable-reads-print
            print_row($key, $row);
        }
    }

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    # instance_id = "my-instance"
    # table_id    = "my-table"
    filter = Google::Cloud::Bigtable::RowFilter.label "labelled"
    read_with_filter instance_id, table_id, filter

#### Strip value

This filter replaces the value of each cell with an empty string. Use this filter when you only need to count the number of rows or cells that match your criteria, rather than retrieving all of the data from those rows or cells.

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    func filterModifyStripValue(w io.Writer, projectID, instanceID string, tableName string) error {
    	filter := bigtable.StripValueFilter()
    	return readWithFilter(w, projectID, instanceID, tableName, filter)
    }
    

### HBase

In the HBase client library, the strip value filter is called `KeyOnlyFilter`. A sample is not available.

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    public static void filterModifyStripValue() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      filterModifyStripValue(projectId, instanceId, tableId);
    }
    
    public static void filterModifyStripValue(String projectId, String instanceId, String tableId) {
      // A filter that replaces the outputted cell value with the empty string
      Filter filter = FILTERS.value().strip();
      readFilter(projectId, instanceId, tableId, filter);
    }
    

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    def filter_modify_strip_value(project_id, instance_id, table_id):
        from google.cloud import [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest)
        from google.cloud.bigtable import row_filters
    
        client = [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html)(project=project_id, admin=True)
        instance = [client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.html).[instance](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html#google_cloud_bigtable_client_Client_instance)(instance_id)
        table = instance.table(table_id)
    
        rows = table.read_rows(filter_=row_filters.StripValueTransformerFilter(True))
        for row in rows:
            print_row(row)
    
    

### Python asyncio

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    async def filter_modify_strip_value(project_id, instance_id, table_id):
        from google.cloud.bigtable.data import (
            BigtableDataClientAsync,
            [ReadRowsQuery](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.read_rows_query.ReadRowsQuery.html),
            [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html),
        )
    
        query = ReadRowsQuery(row_filter=[row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[StripValueTransformerFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.StripValueTransformerFilter.html)(True))
    
        async with BigtableDataClientAsync(project=project_id) as client:
            async with client.get_table(instance_id, table_id) as table:
                for row in await table.read_rows(query):
                    print_row(row)
    
    

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    /// <summary>
    /// /// Read using a strip value filter from an existing table.
    ///</summary>
    /// <param name="projectId">Your Google Cloud Project ID.</param>
    /// <param name="instanceId">Your Google Cloud Bigtable Instance ID.</param>
    /// <param name="tableId">Your Google Cloud Bigtable table ID.</param>
    
    public Task<string> FilterModifyStripValue(string projectId = "YOUR-PROJECT-ID", string instanceId = "YOUR-INSTANCE-ID", string tableId = "YOUR-TABLE-ID")
    {
        // A filter that replaces the outputted cell value with the empty string
        RowFilter filter = RowFilters.StripValueTransformer();
        return ReadFilter(projectId, instanceId, tableId, filter);
    }

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    namespace cbt = ::google::cloud::bigtable;
    using ::google::cloud::StatusOr;
    [](cbt::Table table) {
      cbt::Filter filter = cbt::Filter::StripValueTransformer();
      // Read and print the rows.
      for (StatusOr<cbt::Row>& row :
           table.ReadRows(cbt::RowSet(cbt::RowRange::InfiniteRange()), filter)) {
        if (!row) throw std::move(row).status();
        std::cout << row->row_key() << " = ";
        for (auto const& cell : row->cells()) {
          std::cout << "[" << cell.family_name() << ", "
                    << cell.column_qualifier() << ", " << cell.value() << "],";
        }
        std::cout << "\n";
      }
    }

### Node.js

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    const filter = {
      value: {
        strip: true,
      },
    };
    readWithFilter(filter);

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Bigtable\BigtableClient;
    use Google\Cloud\Bigtable\Filter;
    
    /**
     * Create a filter that strips the value
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance
     * @param string $tableId The ID of the table to read from
     */
    function filter_modify_strip_value(
        string $projectId,
        string $instanceId,
        string $tableId
    ): void {
        // Connect to an existing table with an existing instance.
        $dataClient = new BigtableClient([
            'projectId' => $projectId,
        ]);
        $table = $dataClient->table($instanceId, $tableId);
    
        $filter = Filter::value()->strip();
    
        $rows = $table->readRows([
            'filter' => $filter
        ]);
    
        foreach ($rows as $key => $row) {
            // The "print_row" helper function is defined in https://cloud.google.com/bigtable/docs/samples/bigtable-reads-print
            print_row($key, $row);
        }
    }

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    # instance_id = "my-instance"
    # table_id    = "my-table"
    filter = Google::Cloud::Bigtable::RowFilter.strip_value
    read_with_filter instance_id, table_id, filter

## Composing filters

The following sections describe each composing filter. Composing filters allow you to combine multiple filters into one, which makes it possible to apply more than one filter to a single read request.

#### Chain

This filter applies a series of filters, in order, to each output row. A chain filter is like using a logical AND.

Each filter in the chain sees only the output of the previous filter. For example, if you chain two filters, and the first filter removes half of the cells from the output row, the second filter does not have access to the cells that were removed.

In other words, the order of the filters is important. If you change the order of chained filters, you might get different data in your output rows.

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    func filterComposingChain(w io.Writer, projectID, instanceID string, tableName string) error {
    	filter := bigtable.ChainFilters(bigtable.LatestNFilter(1), bigtable.FamilyFilter("cell_plan"))
    	return readWithFilter(w, projectID, instanceID, tableName, filter)
    }
    

### HBase

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    public static void filterComposingChain() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      filterComposingChain(projectId, instanceId, tableId);
    }
    
    public static void filterComposingChain(String projectId, String instanceId, String tableId) {
      // A filter that selects one cell per row AND within the column family cell_plan
      Filter familyFilter =
          new FamilyFilter(CompareOp.EQUAL, new BinaryComparator(Bytes.toBytes("cell_plan")));
      Filter columnCountGetFilter = new ColumnCountGetFilter(3);
    
      FilterList filter = new FilterList(FilterList.Operator.MUST_PASS_ALL);
      filter.addFilter(columnCountGetFilter);
      filter.addFilter(familyFilter);
      Scan scan = new Scan().setFilter(filter);
      readWithFilter(projectId, instanceId, tableId, scan);
    }

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    public static void filterComposingChain() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      filterComposingChain(projectId, instanceId, tableId);
    }
    
    public static void filterComposingChain(String projectId, String instanceId, String tableId) {
      // A filter that selects one cell per column AND within the column family cell_plan
      Filter filter =
          FILTERS
              .chain()
              .filter(FILTERS.limit().cellsPerColumn(1))
              .filter(FILTERS.family().exactMatch("cell_plan"));
      readFilter(projectId, instanceId, tableId, filter);
    }
    

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    def filter_composing_chain(project_id, instance_id, table_id):
        from google.cloud import [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest)
        from google.cloud.bigtable import row_filters
    
        client = [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html)(project=project_id, admin=True)
        instance = [client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.html).[instance](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html#google_cloud_bigtable_client_Client_instance)(instance_id)
        table = instance.table(table_id)
    
        rows = table.read_rows(
            filter_=row_filters.RowFilterChain(
                filters=[
                    row_filters.CellsColumnLimitFilter(1),
                    row_filters.FamilyNameRegexFilter("cell_plan"),
                ]
            )
        )
        for row in rows:
            print_row(row)
    
    

### Python asyncio

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    async def filter_composing_chain(project_id, instance_id, table_id):
        from google.cloud.bigtable.data import (
            BigtableDataClientAsync,
            [ReadRowsQuery](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.read_rows_query.ReadRowsQuery.html),
            [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html),
        )
    
        query = ReadRowsQuery(
            row_filter=[row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[RowFilterChain](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.RowFilterChain.html)(
                filters=[
                    [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[CellsColumnLimitFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.CellsColumnLimitFilter.html)(1),
                    [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[FamilyNameRegexFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.FamilyNameRegexFilter.html)("cell_plan"),
                ]
            )
        )
    
        async with BigtableDataClientAsync(project=project_id) as client:
            async with client.get_table(instance_id, table_id) as table:
                for row in await table.read_rows(query):
                    print_row(row)
    
    

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    /// <summary>
    /// /// Read using a chain filter from an existing table.
    ///</summary>
    /// <param name="projectId">Your Google Cloud Project ID.</param>
    /// <param name="instanceId">Your Google Cloud Bigtable Instance ID.</param>
    /// <param name="tableId">Your Google Cloud Bigtable table ID.</param>
    
    public Task<string> FilterComposingChain(string projectId = "YOUR-PROJECT-ID", string instanceId = "YOUR-INSTANCE-ID", string tableId = "YOUR-TABLE-ID")
    {
        // A filter that selects one cell per column AND within the column family cell_plan
        RowFilter filter = RowFilters.Chain(RowFilters.CellsPerColumnLimit(1), RowFilters.FamilyNameExact("cell_plan"));
        return ReadFilter(projectId, instanceId, tableId, filter);
    }

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    namespace cbt = ::google::cloud::bigtable;
    using ::google::cloud::StatusOr;
    [](cbt::Table table) {
      cbt::Filter filter = cbt::Filter::Chain(
          cbt::Filter::Latest(1), cbt::Filter::FamilyRegex("cell_plan"));
      // Read and print the rows.
      for (StatusOr<cbt::Row>& row :
           table.ReadRows(cbt::RowSet(cbt::RowRange::InfiniteRange()), filter)) {
        if (!row) throw std::move(row).status();
        std::cout << row->row_key() << " = ";
        for (auto const& cell : row->cells()) {
          std::cout << "[" << cell.family_name() << ", "
                    << cell.column_qualifier() << ", " << cell.value() << "],";
        }
        std::cout << "\n";
      }
    }

### Node.js

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    const filter = [
      {
        column: {
          cellLimit: 1,
        },
      },
      {
        family: 'cell_plan',
      },
    ];
    readWithFilter(filter);

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Bigtable\BigtableClient;
    use Google\Cloud\Bigtable\Filter;
    
    /**
     * Create a composite filter using chaining
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance
     * @param string $tableId The ID of the table to read from
     */
    function filter_composing_chain(
        string $projectId,
        string $instanceId,
        string $tableId
    ): void {
        // Connect to an existing table with an existing instance.
        $dataClient = new BigtableClient([
            'projectId' => $projectId,
        ]);
        $table = $dataClient->table($instanceId, $tableId);
    
        $filter = Filter::chain()
            ->addFilter(Filter::limit()->cellsPerColumn(1))
            ->addFilter(Filter::family()->exactMatch('cell_plan'));
    
        $rows = $table->readRows([
            'filter' => $filter
        ]);
    
        foreach ($rows as $key => $row) {
            // The "print_row" helper function is defined in https://cloud.google.com/bigtable/docs/samples/bigtable-reads-print
            print_row($key, $row);
        }
    }

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    # instance_id = "my-instance"
    # table_id    = "my-table"
    filter = Google::Cloud::Bigtable::RowFilter.chain.cells_per_column(1).family("cell_plan")
    read_with_filter instance_id, table_id, filter

#### Interleave

This filter sends the input row through multiple component filters, generating a temporary output row from each component filter. All of the cells from the temporary output rows are then combined into a final output row. An interleave filter is like using a logical OR.

Interleaves can cause cells to be duplicated in the output row. For example, if your interleave includes two filters, and both filters include a specific cell in their temporary output rows, the final output row will include two copies of that cell.

If the component filters output multiple cells that all have the same column family, column qualifier, and timestamp, the final output row will group all of those cells together in an unspecified order.

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    func filterComposingInterleave(w io.Writer, projectID, instanceID string, tableName string) error {
    	filter := bigtable.InterleaveFilters(bigtable.ValueFilter("true"), bigtable.ColumnFilter("os_build"))
    	return readWithFilter(w, projectID, instanceID, tableName, filter)
    }
    

### HBase

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    public static void filterComposingInterleave() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      filterComposingInterleave(projectId, instanceId, tableId);
    }
    
    public static void filterComposingInterleave(
        String projectId, String instanceId, String tableId) {
      // A filter that matches cells with the value true OR with the column qualifier os_build
      Filter qualifierFilter =
          new QualifierFilter(CompareOp.EQUAL, new BinaryComparator(Bytes.toBytes("os_build")));
      Filter valueFilter =
          new ValueFilter(CompareOp.EQUAL, new BinaryComparator(Bytes.toBytes("true")));
    
      FilterList filter = new FilterList(Operator.MUST_PASS_ONE);
      filter.addFilter(qualifierFilter);
      filter.addFilter(valueFilter);
    
      Scan scan = new Scan().setFilter(filter).setMaxVersions();
      readWithFilter(projectId, instanceId, tableId, scan);
    }

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    public static void filterComposingInterleave() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      filterComposingInterleave(projectId, instanceId, tableId);
    }
    
    public static void filterComposingInterleave(
        String projectId, String instanceId, String tableId) {
      // A filter that matches cells with the value true OR with the column qualifier os_build
      Filter filter =
          FILTERS
              .interleave()
              .filter(FILTERS.value().exactMatch("true"))
              .filter(FILTERS.qualifier().exactMatch("os_build"));
      readFilter(projectId, instanceId, tableId, filter);
    }
    

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    def filter_composing_interleave(project_id, instance_id, table_id):
        from google.cloud import [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest)
        from google.cloud.bigtable import row_filters
    
        client = [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html)(project=project_id, admin=True)
        instance = [client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.html).[instance](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html#google_cloud_bigtable_client_Client_instance)(instance_id)
        table = instance.table(table_id)
    
        rows = table.read_rows(
            filter_=row_filters.RowFilterUnion(
                filters=[
                    row_filters.ValueRegexFilter("true"),
                    row_filters.ColumnQualifierRegexFilter("os_build"),
                ]
            )
        )
        for row in rows:
            print_row(row)
    
    

### Python asyncio

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    async def filter_composing_interleave(project_id, instance_id, table_id):
        from google.cloud.bigtable.data import (
            BigtableDataClientAsync,
            [ReadRowsQuery](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.read_rows_query.ReadRowsQuery.html),
            [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html),
        )
    
        query = ReadRowsQuery(
            row_filter=[row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[RowFilterUnion](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.RowFilterUnion.html)(
                filters=[
                    [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[ValueRegexFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.ValueRegexFilter.html)("true"),
                    [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[ColumnQualifierRegexFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.ColumnQualifierRegexFilter.html)("os_build"),
                ]
            )
        )
    
        async with BigtableDataClientAsync(project=project_id) as client:
            async with client.get_table(instance_id, table_id) as table:
                for row in await table.read_rows(query):
                    print_row(row)
    
    

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    /// <summary>
    /// /// Read using an interleave filter from an existing table.
    ///</summary>
    /// <param name="projectId">Your Google Cloud Project ID.</param>
    /// <param name="instanceId">Your Google Cloud Bigtable Instance ID.</param>
    /// <param name="tableId">Your Google Cloud Bigtable table ID.</param>
    
    public Task<string> FilterComposingInterleave(string projectId, string instanceId, string tableId)
    {
        // A filter that matches cells with the value true OR with the column qualifier os_build
        RowFilter filter = RowFilters.Interleave(RowFilters.ValueExact("true"), RowFilters.ColumnQualifierExact("os_build"));
        return ReadFilter(projectId, instanceId, tableId, filter);
    }

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    namespace cbt = ::google::cloud::bigtable;
    using ::google::cloud::StatusOr;
    [](cbt::Table table) {
      cbt::Filter filter = cbt::Filter::Interleave(
          cbt::Filter::ValueRegex("true"), cbt::Filter::ColumnRegex("os_build"));
      // Read and print the rows.
      for (StatusOr<cbt::Row>& row :
           table.ReadRows(cbt::RowSet(cbt::RowRange::InfiniteRange()), filter)) {
        if (!row) throw std::move(row).status();
        std::cout << row->row_key() << " = ";
        for (auto const& cell : row->cells()) {
          std::cout << "[" << cell.family_name() << ", "
                    << cell.column_qualifier() << ", " << cell.value() << "],";
        }
        std::cout << "\n";
      }
    }

### Node.js

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    const filter = {
      interleave: [
        {
          value: 'true',
        },
        {column: 'os_build'},
      ],
    };
    readWithFilter(filter);

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Bigtable\BigtableClient;
    use Google\Cloud\Bigtable\Filter;
    
    /**
     * Create a composite filter using interleaving
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance
     * @param string $tableId The ID of the table to read from
     */
    function filter_composing_interleave(
        string $projectId,
        string $instanceId,
        string $tableId
    ): void {
        // Connect to an existing table with an existing instance.
        $dataClient = new BigtableClient([
            'projectId' => $projectId,
        ]);
        $table = $dataClient->table($instanceId, $tableId);
    
        $filter = Filter::interleave()
            ->addFilter(Filter::value()->exactMatch('1'))
            ->addFilter(Filter::qualifier()->exactMatch('os_build'));
    
        $rows = $table->readRows([
            'filter' => $filter
        ]);
    
        foreach ($rows as $key => $row) {
            // The "print_row" helper function is defined in https://cloud.google.com/bigtable/docs/samples/bigtable-reads-print
            print_row($key, $row);
        }
    }

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    # instance_id = "my-instance"
    # table_id    = "my-table"
    filter = Google::Cloud::Bigtable::RowFilter.interleave.value("true").qualifier("os_build")
    read_with_filter instance_id, table_id, filter

#### Condition

This filter applies either a _true filter_ or a _false filter_ to the input row.

**Caution:** The condition filter is much slower than other filters, especially when the condition filter specifies a false filter. We recommend that you _not use_ condition filters.

To choose between the true and false filters, a _predicate filter_ is applied to the input row. If the predicate filter's output contains at least one cell, the true filter is applied. If the predicate filter's output is empty, the false filter is applied.

The predicate filter's output row is used only to choose between the true and false filters. It does not appear in the response to your read request.

The predicate filter is not executed atomically with the true or false filter. In other words, the data in the input row can change between the time when the predicate filter is executed and the time when the true or false filter is executed. This behavior can lead to inconsistent or unexpected results.

When you use the condition filter, you can omit the true or false filter. Omitting a filter is the same as specifying the block all filter. If the predicate filter chooses a condition that you omitted, the output row will be empty.

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    func filterComposingCondition(w io.Writer, projectID, instanceID string, tableName string) error {
    	filter := bigtable.ConditionFilter(
    		bigtable.ChainFilters(bigtable.ColumnFilter("data_plan_10gb"), bigtable.ValueFilter("true")),
    		bigtable.StripValueFilter(),
    		bigtable.PassAllFilter())
    	return readWithFilter(w, projectID, instanceID, tableName, filter)
    }
    

### HBase

This client library does not support this filter.

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    public static void filterComposingCondition() {
      // TODO(developer): Replace these variables before running the sample.
      String projectId = "my-project-id";
      String instanceId = "my-instance-id";
      String tableId = "mobile-time-series";
      filterComposingCondition(projectId, instanceId, tableId);
    }
    
    public static void filterComposingCondition(String projectId, String instanceId, String tableId) {
      // A filter that applies the label passed-filter IF the cell has the column qualifier
      // data_plan_10gb AND the value true, OTHERWISE applies the label filtered-out
      Filter filter =
          FILTERS
              .condition(
                  FILTERS
                      .chain()
                      .filter(FILTERS.qualifier().exactMatch("data_plan_10gb"))
                      .filter(FILTERS.value().exactMatch("true")))
              .then(FILTERS.label("passed-filter"))
              .otherwise(FILTERS.label("filtered-out"));
      readFilter(projectId, instanceId, tableId, filter);
    }
    

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    def filter_composing_condition(project_id, instance_id, table_id):
        from google.cloud import [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest)
        from google.cloud.bigtable import row_filters
    
        client = [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html)(project=project_id, admin=True)
        instance = [client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.html).[instance](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html#google_cloud_bigtable_client_Client_instance)(instance_id)
        table = instance.table(table_id)
    
        rows = table.read_rows(
            filter_=row_filters.ConditionalRowFilter(
                base_filter=row_filters.RowFilterChain(
                    filters=[
                        row_filters.ColumnQualifierRegexFilter("data_plan_10gb"),
                        row_filters.ValueRegexFilter("true"),
                    ]
                ),
                true_filter=row_filters.ApplyLabelFilter(label="passed-filter"),
                false_filter=row_filters.ApplyLabelFilter(label="filtered-out"),
            )
        )
        for row in rows:
            print_row(row)
    
    

### Python asyncio

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    async def filter_composing_condition(project_id, instance_id, table_id):
        from google.cloud.bigtable.data import (
            BigtableDataClientAsync,
            [ReadRowsQuery](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.read_rows_query.ReadRowsQuery.html),
            [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html),
        )
    
        query = ReadRowsQuery(
            row_filter=[row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[ConditionalRowFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.ConditionalRowFilter.html)(
                predicate_filter=[row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[RowFilterChain](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.RowFilterChain.html)(
                    filters=[
                        [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[ColumnQualifierRegexFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.ColumnQualifierRegexFilter.html)("data_plan_10gb"),
                        [row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[ValueRegexFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.ValueRegexFilter.html)("true"),
                    ]
                ),
                true_filter=[row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[ApplyLabelFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.ApplyLabelFilter.html)(label="passed-filter"),
                false_filter=[row_filters](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.html).[ApplyLabelFilter](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row_filters.ApplyLabelFilter.html)(label="filtered-out"),
            )
        )
    
        async with BigtableDataClientAsync(project=project_id) as client:
            async with client.get_table(instance_id, table_id) as table:
                for row in await table.read_rows(query):
                    print_row(row)
    
    

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    /// <summary>
    /// /// Read using a conditional filter from an existing table.
    ///</summary>
    /// <param name="projectId">Your Google Cloud Project ID.</param>
    /// <param name="instanceId">Your Google Cloud Bigtable Instance ID.</param>
    /// <param name="tableId">Your Google Cloud Bigtable table ID.</param>
    
    public Task<string> FilterComposingCondition(string projectId = "YOUR-PROJECT-ID", string instanceId = "YOUR-INSTANCE-ID", string tableId = "YOUR-TABLE-ID")
    {
        // A filter that applies the label passed-filter IF the cell has the column qualifier
        // data_plan_10gb AND the value true, OTHERWISE applies the label filtered-out
        RowFilter filter = RowFilters.Condition(
            RowFilters.Chain(RowFilters.ColumnQualifierExact("data_plan_10gb"), RowFilters.ValueExact("true")),
            new RowFilter { ApplyLabelTransformer = "passed-filter" },
            new RowFilter { ApplyLabelTransformer = "filtered-out" }
            );
        return ReadFilter(projectId, instanceId, tableId, filter);
    }

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    namespace cbt = ::google::cloud::bigtable;
    using ::google::cloud::StatusOr;
    [](cbt::Table table) {
      cbt::Filter filter = cbt::Filter::Condition(
          cbt::Filter::Chain(cbt::Filter::ValueRegex("true"),
                             cbt::Filter::ColumnRegex("data_plan_10gb")),
          cbt::Filter::ApplyLabelTransformer("passed-filter"),
          cbt::Filter::ApplyLabelTransformer("filtered-out"));
      // Read and print the rows.
      for (StatusOr<cbt::Row>& row :
           table.ReadRows(cbt::RowSet(cbt::RowRange::InfiniteRange()), filter)) {
        if (!row) throw std::move(row).status();
        std::cout << row->row_key() << " = ";
        for (auto const& cell : row->cells()) {
          std::cout << "[" << cell.family_name() << ", "
                    << cell.column_qualifier() << ", " << cell.value()
                    << ", label(";
          for (auto const& label : cell.labels()) {
            std::cout << label << ",";
          }
          std::cout << ")],";
        }
        std::cout << "\n";
      }
    }

### Node.js

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    const filter = {
      condition: {
        test: [
          {column: 'data_plan_10gb'},
          {
            value: 'true',
          },
        ],
        pass: {
          label: 'passed-filter',
        },
        fail: {
          label: 'filtered-out',
        },
      },
    };
    readWithFilter(filter);

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Bigtable\BigtableClient;
    use Google\Cloud\Bigtable\Filter;
    
    /**
     * Create a composite filter using a conditional
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance
     * @param string $tableId The ID of the table to read from
     */
    function filter_composing_condition(
        string $projectId,
        string $instanceId,
        string $tableId
    ): void {
        // Connect to an existing table with an existing instance.
        $dataClient = new BigtableClient([
            'projectId' => $projectId,
        ]);
        $table = $dataClient->table($instanceId, $tableId);
    
        $filter = Filter::condition(
            Filter::chain()
                ->addFilter(Filter::value()->exactMatch('1'))
                ->addFilter(Filter::qualifier()->exactMatch('data_plan_10gb'))
        )
            ->then(Filter::label('passed-filter'))
            ->otherwise(Filter::label('filtered-out'));
    
        $rows = $table->readRows([
            'filter' => $filter
        ]);
    
        foreach ($rows as $key => $row) {
            // The "print_row" helper function is defined in https://cloud.google.com/bigtable/docs/samples/bigtable-reads-print
            print_row($key, $row);
        }
    }

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    # instance_id = "my-instance"
    # table_id    = "my-table"
    filter = Google::Cloud::Bigtable::RowFilter.condition(
      Google::Cloud::Bigtable::RowFilter.chain.qualifier("data_plan_10gb").value("true")
    )
                                               .on_match(Google::Cloud::Bigtable::RowFilter.label("passed-filter"))
                                               .otherwise(Google::Cloud::Bigtable::RowFilter.label("filtered-out"))
    read_with_filter instance_id, table_id, filter

## What's next

  * [Read an overview of reads.](https://docs.cloud.google.com/bigtable/docs/reads)
  * [Learn about writes.](https://docs.cloud.google.com/bigtable/docs/writes)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
