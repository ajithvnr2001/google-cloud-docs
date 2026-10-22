---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-hw-create-filter/
title: Version limit \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:57:17.786771+00:00
---

# Version limit  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-hw-create-filter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  Version limit Stay organized with collections  Save and categorize content based on your preferences. 

Create a filter to limit the number of versions of columns to retrieve.

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
    
    
    cbt::Filter filter = cbt::Filter::ColumnRangeClosed("family", "c0", "c0");

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    RowFilter filter = RowFilters.CellsPerRowLimit(1);

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    public void filterLimitCellsPerCol(String tableId) {
      // A filter that matches only the most recent cell within each column
      Filter filter = FILTERS.limit().cellsPerColumn(1);
      readRowFilter(tableId, filter);
      readFilter(tableId, filter);
    }
    

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Create a filter to only retrieve the most recent version of the cell
    # for each column across entire row.
    row_filter = bigtable.row_filters.CellsColumnLimitFilter(1)

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Only retrieve the most recent version of the cell.
    filter = Google::Cloud::Bigtable::RowFilter.cells_per_column 1

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
