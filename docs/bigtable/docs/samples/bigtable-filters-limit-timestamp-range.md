---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-filters-limit-timestamp-range/
title: Read using a timestamp range filter \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:02.523653+00:00
---

# Read using a timestamp range filter  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-filters-limit-timestamp-range/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  Read using a timestamp range filter Stay organized with collections  Save and categorize content based on your preferences. 

Creates a limiting filter on a range of cell timestamps.

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

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    func filterLimitTimestampRange(w io.Writer, projectID, instanceID string, tableName string) error {
    	startTime := time.Unix(0, 0)
    	endTime := time.Now().Add(-1 * time.Hour)
    	filter := bigtable.TimestampRangeFilter(startTime, endTime)
    
    	return readWithFilter(w, projectID, instanceID, tableName, filter)
    }
    

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def filter_limit_timestamp_range(project_id, instance_id, table_id):
        import datetime
    
        from google.cloud import [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest)
        from google.cloud.bigtable import row_filters
    
        client = [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html)(project=project_id, admin=True)
        instance = [client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.html).[instance](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html#google_cloud_bigtable_client_Client_instance)(instance_id)
        table = instance.table(table_id)
    
        end = datetime.datetime(2019, 5, 1)
    
        rows = table.read_rows(
            filter_=row_filters.TimestampRangeFilter(row_filters.TimestampRange(end=end))
        )
        for row in rows:
            print_row(row)
    
    

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # instance_id = "my-instance"
    # table_id    = "my-table"
    timestamp_minus_hr = (Time.now.to_f * 1_000_000).round(-3) - (60 * 60 * 1000 * 1000)
    puts timestamp_minus_hr
    filter = Google::Cloud::Bigtable::RowFilter.timestamp_range from: 0, to: timestamp_minus_hr
    
    read_with_filter instance_id, table_id, filter

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
