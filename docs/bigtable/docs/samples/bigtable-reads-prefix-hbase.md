---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-reads-prefix-hbase/
title: Read rows with a prefix (HBase) \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:56:56.845737+00:00
---

# Read rows with a prefix (HBase)  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-reads-prefix-hbase/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  Read rows with a prefix (HBase) Stay organized with collections  Save and categorize content based on your preferences. 

Create a query with a prefix.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Read examples](https://docs.cloud.google.com/bigtable/docs/reading-data)



## Code sample

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
