---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-filters-limit-value-range/
title: Read using a value range filter \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:47.861181+00:00
---

# Read using a value range filter  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-filters-limit-value-range/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  Read using a value range filter Stay organized with collections  Save and categorize content based on your preferences. 

Creates a limiting filter on a range of cell values.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Use filters](https://docs.cloud.google.com/bigtable/docs/using-filters)



## Code sample

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    func filterLimitValueRange(w io.Writer, projectID, instanceID string, tableName string) error {
    	filter := bigtable.ValueRangeFilter([]byte("PQ2A.190405"), []byte("PQ2A.190406"))
    	return readWithFilter(w, projectID, instanceID, tableName, filter)
    }
    

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    
    

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # instance_id = "my-instance"
    # table_id    = "my-table"
    range = Google::Cloud::Bigtable::ValueRange.new.from("PQ2A.190405").to("PQ2A.190406")
    filter = Google::Cloud::Bigtable::RowFilter.value_range range
    read_with_filter instance_id, table_id, filter

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
