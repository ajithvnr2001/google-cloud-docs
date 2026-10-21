---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-hw-scan-with-filter/
title: Read using a filter \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:01.660729+00:00
---

# Read using a filter  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-hw-scan-with-filter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  Read using a filter Stay organized with collections  Save and categorize content based on your preferences. 

Read the most recent value in a given column using a filter.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [C# hello world](https://docs.cloud.google.com/bigtable/docs/samples-c-sharp-hello)
  * [C++ hello world](https://docs.cloud.google.com/bigtable/docs/samples-cpp-hello)
  * [Node.js hello world](https://docs.cloud.google.com/bigtable/docs/samples-nodejs-hello)
  * [Python hello world](https://docs.cloud.google.com/bigtable/docs/samples-python-hello)
  * [Ruby hello world](https://docs.cloud.google.com/bigtable/docs/samples-ruby-hello)



## Code sample

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    for (auto& row : table.ReadRows(cbt::RowRange::InfiniteRange(),
                                    cbt::Filter::PassAllFilter())) {
      if (!row) throw std::move(row).status();
      std::cout << row->row_key() << ":\n";
      for (cbt::Cell const& c : row->cells()) {
        std::cout << "\t" << c.family_name() << ":" << c.column_qualifier()
                  << "    @ " << c.timestamp().count() << "us\n"
                  << "\t\"" << c.value() << '"' << "\n";
      }
    }

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    Console.WriteLine("Read all rows using streaming");
    // stream the content of the whole table. Apply a filter to return latest only cell values accross all rows.
    ReadRowsStream responseRead = bigtableClient.ReadRows(tableName, filter: filter);
    
    Task printRead = PrintReadRowsAsync();
    printRead.Wait();
    
    async Task PrintReadRowsAsync()
    {
        var responseEnumerator = responseRead.GetAsyncEnumerator(default);
        while (await responseEnumerator.MoveNextAsync())
        {
            Row row = responseEnumerator.Current;
            Console.WriteLine(
                $"\tRow key: {row.Key.ToStringUtf8()} " +
                $"  -- Value: {row.Families[0].Columns[0].Cells[0].Value.ToStringUtf8(),-16} " +
                $"  -- Time Stamp: {row.Families[0].Columns[0].Cells[0].TimestampMicros}");
        }
    }

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    private void readFilter(String tableId, Filter filter) {
      Query query = Query.create(TableId.of(tableId)).filter(filter);
      ServerStream<Row> rows = dataClient.readRows(query);
      for (Row row : rows) {
        printRow(row);
      }
      System.out.println("Table filter completed.");
    }
    

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    print("Scanning for all greetings:")
    partial_rows = table.read_rows(filter_=row_filter)
    
    for row in partial_rows:
        column_family_id_str = column_family_id.decode("utf-8")
        cell = row.cells[column_family_id_str][column][0]
        print(cell.value.decode("utf-8"))

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    puts "Reading the entire table"
    table.read_rows.each do |row|
      puts "Row key: #{row.key}, Value: #{row.cells[column_family].first.value}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
