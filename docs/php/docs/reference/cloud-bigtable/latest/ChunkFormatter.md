---
url: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/ChunkFormatter/
title: Cloud Bigtable Client - Class ChunkFormatter (2.31.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:10.034181+00:00
---

# Cloud Bigtable Client - Class ChunkFormatter (2.31.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/ChunkFormatter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Bigtable Client - Class ChunkFormatter (2.31.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.31.0 (latest)  2.30.0  2.29.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.1  2.20.2  2.19.2  2.18.0  2.17.1  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.1  2.9.1  2.8.0  2.7.0  2.6.3  2.5.0  2.4.0  2.3.0  2.2.1  2.1.0  2.0.1  1.32.1  1.31.1  1.30.0  1.29.2  1.28.3  1.27.0  1.26.2  1.25.0  1.24.1  1.23.0  1.22.2  1.21.1  1.20.3 

Reference documentation and code samples for the Cloud Bigtable Client class ChunkFormatter.

Converts cell chunks into an easily digestable format. Please note this class implements the IteratorAggregate interface, and as such can be iterated over directly in order to access the formatted rows.

Example:
    
    
    use Google\Cloud\Bigtable\BigtableClient;
    
    $bigtable = new BigtableClient();
    $table = $bigtable->table('my-instance', 'my-table');
    $formatter = $table->readRows();
    

## Namespace

Google \ Cloud \ Bigtable

## Implements

\IteratorAggregate

## Methods 

### __construct

Constructs the ChunkFormatter.

**Parameters**  
---  
**Name** | **Description**  
`gapicClient` |  `[V2\Client\BigtableClient](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/V2.Client.BigtableClient)`   
The GAPIC client to use in order to send requests.  
`request` |  `[V2\ReadRowsRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/V2.ReadRowsRequest)`   
The proto request to be passed to the Gapic client.  
`options` |  `array`   
[optional] Configuration options for read rows call.  
  
### readAll

Formats the row's chunks into a friendly format.

Example:
    
    
    $rows = $formatter->readAll();
    

**Returns**  
---  
**Type** | **Description**  
`Generator` |   
  
### getIterator

**Returns**  
---  
**Type** | **Description**  
`Generator` |   
  
### __debugInfo

Represent the class in a more readable and digestable fashion.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
