---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-hw-scan-all/
title: Read all \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:11:28.577430+00:00
---

# Read all  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-hw-scan-all/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  Read all Stay organized with collections  Save and categorize content based on your preferences. 

Perform a full table scan.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Go hello world](https://docs.cloud.google.com/bigtable/docs/samples-go-hello)
  * [Java hello world](https://docs.cloud.google.com/bigtable/docs/samples-java-hello-world)
  * [PHP hello world](https://docs.cloud.google.com/bigtable/docs/samples-php-hello)



## Code sample

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    log.Printf("Reading all greeting rows:")
    err = tbl.ReadRows(ctx, bigtable.PrefixRange(columnName), func(row bigtable.Row) bool {
    	item := row[columnFamilyName][0]
    	log.Printf("\t%s = %s\n", item.Row, string(item.Value))
    	return true
    }, bigtable.RowFilter(bigtable.ColumnFilter(columnName)))
    
    if err = client.Close(); err != nil {
    	log.Fatalf("Could not close data operations client: %v", err)
    }

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    try {
      System.out.println("\nReading the entire table");
      Query query = Query.create(TableId.of(tableId));
      ServerStream<Row> rowStream = dataClient.readRows(query);
      List<Row> tableRows = new ArrayList<>();
      for (Row r : rowStream) {
        System.out.println("Row Key: " + r.getKey().toStringUtf8());
        tableRows.add(r);
        for (RowCell cell : r.getCells()) {
          System.out.printf(
              "Family: %s    Qualifier: %s    Value: %s%n",
              cell.getFamily(), cell.getQualifier().toStringUtf8(), cell.getValue().toStringUtf8());
        }
      }
      return tableRows;
    } catch (NotFoundException e) {
      System.err.println("Failed to read a non-existent table: " + e.getMessage());
      return null;
    }

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    $columnFamilyId = 'cf1';
    $column = 'greeting';
    printf('Scanning for all greetings:' . PHP_EOL);
    $partialRows = $table->readRows([])->readAll();
    foreach ($partialRows as $row) {
        printf('%s' . PHP_EOL, $row[$columnFamilyId][$column][0]['value']);
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

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
