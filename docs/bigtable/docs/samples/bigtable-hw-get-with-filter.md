---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-hw-get-with-filter/
title: Read with a filter \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:11:54.430817+00:00
---

# Read with a filter  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-hw-get-with-filter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  Read with a filter Stay organized with collections  Save and categorize content based on your preferences. 

Read the most recent value in a given column using a filter.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [C# hello world](https://docs.cloud.google.com/bigtable/docs/samples-c-sharp-hello)
  * [C++ hello world](https://docs.cloud.google.com/bigtable/docs/samples-cpp-hello)
  * [Node.js hello world](https://docs.cloud.google.com/bigtable/docs/samples-nodejs-hello)
  * [PHP hello world](https://docs.cloud.google.com/bigtable/docs/samples-php-hello)
  * [Python hello world](https://docs.cloud.google.com/bigtable/docs/samples-python-hello)
  * [Ruby hello world](https://docs.cloud.google.com/bigtable/docs/samples-ruby-hello)



## Code sample

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    StatusOr<std::pair<bool, cbt::Row>> result = table.ReadRow("key-0", filter);
    if (!result) throw std::move(result).status();
    if (!result->first) {
      std::cout << "Cannot find row 'key-0' in the table: " << table.table_name()
                << "\n";
      return;
    }
    cbt::Cell const& cell = result->second.cells().front();
    std::cout << cell.family_name() << ":" << cell.column_qualifier() << "    @ "
              << cell.timestamp().count() << "us\n"
              << '"' << cell.value() << '"' << "\n";

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Read from the table.
    Console.WriteLine("Read the first row");
    
    int rowIndex = 0;
    
    // Read a specific row. Apply a filter to return latest only cell value accross entire row.
    Row rowRead = bigtableClient.ReadRow(
        tableName, rowKey: rowKeyPrefix + rowIndex, filter: filter);
    Console.WriteLine(
        $"\tRow key: {rowRead.Key.ToStringUtf8()} " +
        $"  -- Value: {rowRead.Families[0].Columns[0].Cells[0].Value.ToStringUtf8(),-16} " +
        $"  -- Time Stamp: {rowRead.Families[0].Columns[0].Cells[0].TimestampMicros}");

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    private void readRowFilter(String tableId, Filter filter) {
      String rowKey =
          Base64.getEncoder().encodeToString("greeting0".getBytes(StandardCharsets.UTF_8));
      Row row = dataClient.readRow(TableId.of(tableId), rowKey, filter);
      printRow(row);
      System.out.println("Row filter completed.");
    }
    

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    printf('Getting a single greeting by row key.' . PHP_EOL);
    $key = 'greeting0';
    // Only retrieve the most recent version of the cell.
    $rowFilter = (new RowFilter())->setCellsPerColumnLimitFilter(1);
    
    $column = 'greeting';
    $columnFamilyId = 'cf1';
    
    $row = $table->readRow($key, [
        'filter' => $rowFilter
    ]);
    printf('%s' . PHP_EOL, $row[$columnFamilyId][$column][0]['value']);

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    print("Getting a single greeting by row key.")
    key = b"greeting0"
    
    row = table.read_row(key, row_filter)
    cell = row.cells[column_family_id.decode("utf-8")][column][0]
    print(cell.value.decode("utf-8"))

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    puts "Reading a single row by row key"
    row = table.read_row "greeting0", filter: filter
    puts "Row key: #{row.key}, Value: #{row.cells[column_family].first.value}"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
